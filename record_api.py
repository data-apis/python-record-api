import importlib
import inspect
import io
import json
import os
import runpy
import sys
import types
import dis

from typing import *

import get_stack

__all__ = ["tracer"]
TRACE_MODULE = os.environ["PYTHON_API_TRACE_MODULE"]


def type_name(value: object) -> str:
    tp = type(value)
    module = inspect.getmodule(tp)
    return f"{module.__name__}.{tp.__qualname__}"


def save_log(
    fn: str,
    caller_args: List[str],
    caller_kwargs: List[str],
    signature_available: bool,
    fn_arguments: Optional[Dict[str, str]],
    fn_varargs: Optional[List[str]],
    fn_varkw: Optional[Dict[str, str]],
) -> None:
    data = {
        "function": fn,
        "caller_args": caller_args,
        "caller_kwargs": caller_kwargs,
        "signature_available": signature_available,
        "function_arguments": fn_arguments,
        "function_var_positional": fn_varargs,
        "function_var_keyword": fn_varkw,
    }
    writer.write((json.dumps(data) + "\n").encode())


def log_call(fn: types.FunctionType, module_name: str, *args, **kwargs):
    fn_name = f"{module_name}.{fn.__qualname__}"
    arg_types = list(map(type_name, args))
    kwarg_types = {key: type_name(value) for key, value in kwargs.items()}

    try:
        sig = inspect.signature(fn)
    except ValueError:
        bound_arguments = None
        vararg_types = None
        varkw_types = None
        signature_available = False
    else:
        # pop off var args and var kwargs from bound arguments
        # so we can save log them seperately
        vararg_param = None
        varkw_param = None
        for param in sig.parameters.values():
            if param.kind == inspect.Parameter.VAR_POSITIONAL:
                vararg_param = param.name
            elif param.kind == inspect.Parameter.VAR_KEYWORD:
                varkw_param = param.name

        bound_arguments = sig.bind(*arg_types, **kwarg_types).arguments

        vararg_types = (
            bound_arguments.pop(vararg_param, []) if vararg_param is not None else []
        )
        varkw_types = (
            bound_arguments.pop(varkw_param, {}) if varkw_param is not None else {}
        )
        signature_available = True

    save_log(
        fn_name,
        arg_types,
        kwarg_types,
        signature_available,
        bound_arguments,
        vararg_types,
        varkw_types,
    )


# Keep a set of frames that we have recorded a call
# from. We should add to this when we record a bytecode
# trace from a function call
# we should pop one off this to check if we should keep tracing
# below this frame
RECORDED_CALL_FRAMES = set()


def record_function(fn: types.FunctionType, *args: object, **kwargs) -> bool:
    module = inspect.getmodule(fn)
    if not module:
        return False
    module_name = module.__name__
    if module_name.startswith(TRACE_MODULE):
        log_call(fn, module_name, *args, **kwargs)
        return True
    return False


def record_method(
    method_name: str, self_, *args: object, **kwargs
) -> Optional[Callable]:
    cls = type(self_)
    module_name = inspect.getmodule(cls).__name__
    if module_name.startswith(TRACE_MODULE) and hasattr(cls, method_name):
        log_call(getattr(cls, method_name), module_name, self_, *args, **kwargs)
        return lambda: getattr(self_, method_name)(*args, **kwargs)
    return None


def record_binary_method(stack, name):
    """
    Tries recording regular method, and if you cant, record reflected
    """
    if not record_method(f"__{name}__", stack.TOS1, stack.TOS):
        record_method(f"__r{name}__", stack.TOS, stack.TOS1)


def record_binary_inplace_method(stack, name):
    """
    Tries inplace method, and if cannot be found, uses regular method
    """
    if not record_method(f"__i{name}__", stack.TOS1, stack.TOS):
        record_binary_method(stack, name)


def record_comparison(stack, name, inverse):
    m = record_method(name, stack.TOS, stack.TOS1)
    if (not m) or (m() is NotImplemented):
        record_method(inverse, stack.TOS1, stack.TOS)


def get_instruction(frame):
    for instruction in dis.get_instructions(frame.f_code):
        if instruction.offset == frame.f_lasti:
            return instruction
    raise ValueError("Couldn't find instruction by offset")


class Stack:
    NULL = object()

    def __init__(self, frame):
        self.op_stack = get_stack.OpStack(frame)
        self.current_i = 0

    @property
    def TOS(self):
        return self.op_stack[-1]

    @property
    def TOS1(self):
        return self.op_stack[-2]

    @property
    def TOS2(self):
        return self.op_stack[-3]

    def pop(self):
        """
        return the top item on the stack and removes it from the stack
        """
        self.current_i += 1
        try:
            return self.op_stack[-self.current_i]
        except ValueError:
            # raised when "PyObject is NULL"
            return self.NULL

    def pop_n(self, n: int):
        """
        removes the top N items from the stack and returns them so the top item is on the left.
        """
        return [self.pop() for _ in range(n)]


def tracer(frame, event, arg):
    frame.f_trace_opcodes = True
    if event == "call":
        try:
            RECORDED_CALL_FRAMES.remove(frame.f_back)
        except KeyError:
            # we didnt record the call frame, so keep tracing
            return tracer
        # we did record this call frame, so dont trace below here
        return None
    if event != "opcode":
        return

    instruction = get_instruction(frame)
    oparg = instruction.argval
    opname = instruction.opname
    stack = Stack(frame)

    # handle all opcodes from https://docs.python.org/3/library/dis.html
    # that we care about

    # Unary
    if opname == "UNARY_POSITIVE":
        record_method("__pos__", stack.TOS)
    if opname == "UNARY_NEGATIVE":
        record_method("__neg__", stack.TOS)
    if opname == "UNARY_NOT":
        # try bool first and if that isn't method record length
        if not record_method("__bool__", stack.TOS):
            record_method("__len__", stack.TOS)
    if opname == "UNARY_INVERT":
        record_method("__invert__", stack.TOS)
    if opname == "GET_ITER":
        record_method("__iter__", stack.TOS)
    if opname == "GET_YIELD_FROM_ITER":
        record_method("__iter__", stack.TOS)

    # binary
    if opname == "BINARY_SUBSCR":
        record_method("__getitem__", stack.TOS, stack.TOS1)

    if opname == "BINARY_POWER":
        record_binary_method(stack, "pow")

    if opname == "BINARY_MULTIPLY":
        record_binary_method(stack, "mul")

    if opname == "BINARY_MATRIX_MULTIPLY":
        record_binary_method(stack, "matmul")

    if opname == "BINARY_FLOOR_DIVIDE":
        record_binary_method(stack, "floordiv")

    if opname == "BINARY_TRUE_DIVIDE":
        record_binary_method(stack, "truediv")

    if opname == "BINARY_MODULO":
        record_binary_method(stack, "mod")

    if opname == "BINARY_ADD":
        record_binary_method(stack, "add")

    if opname == "BINARY_SUBTRACT":
        record_binary_method(stack, "sub")

    if opname == "BINARY_LSHIFT":
        record_binary_method(stack, "lshift")

    if opname == "BINARY_RSHIFT":
        record_binary_method(stack, "rshift")

    if opname == "BINARY_AND":
        record_binary_method(stack, "and")

    if opname == "BINARY_XOR":
        record_binary_method(stack, "xor")

    if opname == "BINARY_OR":
        record_binary_method(stack, "or")

    # inplace
    if opname == "INPLACE_POWER":
        record_binary_inplace_method(stack, "pow")

    if opname == "INPLACE_MULTIPLY":
        record_binary_inplace_method(stack, "mul")

    if opname == "INPLACE_MATRIX_MULTIPLY":
        record_binary_inplace_method(stack, "matmul")

    if opname == "INPLACE_FLOOR_DIVIDE":
        record_binary_inplace_method(stack, "div")

    if opname == "INPLACE_TRUE_DIVIDE":
        record_binary_inplace_method(stack, "truediv")

    if opname == "INPLACE_MODULO":
        record_binary_inplace_method(stack, "mod")

    if opname == "INPLACE_ADD":
        record_binary_inplace_method(stack, "add")

    if opname == "INPLACE_SUBTRACT":
        record_binary_inplace_method(stack, "sub")

    if opname == "INPLACE_LSHIFT":
        record_binary_inplace_method(stack, "lshift")

    if opname == "INPLACE_RSHIFT":
        record_binary_inplace_method(stack, "rshift")

    if opname == "INPLACE_AND":
        record_binary_inplace_method(stack, "and")

    if opname == "INPLACE_XOR":
        record_binary_inplace_method(stack, "xor")

    if opname == "STORE_SUBSCR":
        record_method("__setitem__", stack.TOS1, stack.TOS, stack.TOS2)

    if opname == "DELETE_SUBSCR":
        record_method("__delitem__", stack.TOS1, stack.TOS)

    # misc
    if opname == "UNPACK_SEQUENCE":
        record_method("__iter__", stack.TOS)
    if opname == "UNPACK_EX":
        record_method("__iter__", stack.TOS)

    if opname == "STORE_ATTR":
        record_method("__setattr__", stack.TOS, oparg, stack.TOS1)

    if opname == "DELETE_ATTR":
        record_method("__delattr__", stack.TOS, oparg)

    if opname in ("BUILD_TUPLE_UNPACK", "BUILD_LIST_UNPACK", "BUILD_SET_UNPACK"):
        for value in stack.pop_n(oparg):
            record_method("__iter__", value)

    if opname == "BUILD_TUPLE_UNPACK_WITH_CALL":
        args = []
        for _ in range(oparg):
            arg = stack.pop()
            args.extend(list(arg))
            record_method("__iter__", arg)
        fn = stack.pop()
        if record_function(fn, *args):
            RECORDED_CALL_FRAMES.add(frame)
    # TODO: BUILD_MAP_UNPACK, BUILD_MAP_UNPACK_WITH_CALL
    if opname == "LOAD_ATTR":
        record_method("__getattr__", stack.TOS, oparg)
    if opname == "COMPARE_OP":
        if oparg == "<":
            record_comparison(stack, "__lt__", "__gt__")
        if oparg == "<=":
            record_comparison(stack, "__le__", "__ge__")
        if oparg == "==":
            record_comparison(stack, "__eq__", "__ne__")
        if oparg == "!=":
            record_comparison(stack, "__ne__", "__eq__")
        if oparg == ">":
            record_comparison(stack, "__gt__", "__lt__")
        if oparg == ">=":
            record_comparison(stack, "__ge__", "__le__")
        if oparg in ("in", "not in"):
            # https://docs.python.org/3/reference/expressions.html#membership-test-operations
            if not record_method("__contains__", stack.TOS1, stack.TOS):
                if not record_method("__iter__", stack.TOS1):
                    record_method("__getitem__", stack.TOS1, 0)

    if opname == "FOR_ITER":
        record_method("__next__", stack.TOS)
    if opname == "CALL_FUNCTION":
        args = stack.pop_n(oparg)
        fn = stack.pop()
        if record_function(fn, *args):
            RECORDED_CALL_FRAMES.add(frame)
    if opname == "CALL_FUNCTION_KW":
        kwargs_names = stack.pop()
        kwargs = {name: stack.pop() for name in kwargs_names}
        args = stack.pop_n(oparg - len(kwargs_names))
        fn = stack.pop()
        if record_function(fn, *args, **kwargs):
            RECORDED_CALL_FRAMES.add(frame)
    if opname == "CALL_FUNCTION_EX":
        has_kwarg = oparg & int("01", 2)
        if has_kwarg:
            kwargs = stack.pop()
            args = stack.pop()
            fn = stack.pop()
        else:
            kwargs = {}
            args = stack.pop()
            fn = stack.pop()
        if record_function(fn, *args, **kwargs):
            RECORDED_CALL_FRAMES.add(frame)
    if opname == "CALL_METHOD":
        args = stack.pop_n(oparg)
        self_ = stack.pop()
        method = stack.pop()

        if self_ is stack.NULL:
            res = record_function(method, *args)
        else:
            res = record_function(method, self_, *args)
        if res:
            RECORDED_CALL_FRAMES.add(frame)


if __name__ == "__main__":
    FILE_NAME = os.environ["PYTHON_API_OUTPUT_FILE"]
    IMPORT_MODULES = os.environ.get("PYTHON_API_IMPORT_MODULES", "")
    RUN_MODULE = os.environ["PYTHON_API_RUN_MODULE"]

    rand_file = io.FileIO(FILE_NAME, "w")
    writer = io.BufferedWriter(rand_file)

    if IMPORT_MODULES:
        for module in IMPORT_MODULES.split(","):
            importlib.import_module(module)
    try:
        sys.settrace(tracer)
        runpy.run_module(RUN_MODULE, run_name="__main__", alter_sys=True)
    except Exception:
        sys.settrace(None)
        raise Exception(f"Error running {RUN_MODULE}")
    else:
        sys.settrace(None)
    finally:
        writer.flush()
        rand_file.close()
