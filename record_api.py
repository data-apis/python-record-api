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

from get_stack import OpStack

FILE_NAME = os.environ["PYTHON_API_OUTPUT_FILE"]
TRACE_MODULE = os.environ["PYTHON_API_TRACE_MODULE"]
RUN_MODULE = os.environ["PYTHON_API_RUN_MODULE"]
IMPORT_MODULES = os.environ.get("PYTHON_API_IMPORT_MODULES", "")


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


def record_function(fn: types.FunctionType, *args: object) -> bool:
    module = inspect.getmodule(fn)
    if not module:
        return False
    module_name = module.__name__
    if module_name.startswith(TRACE_MODULE):
        log_call(fn, module_name, *args)
        return True
    return False


def record_method(method_name: str, self_, *args: object,) -> Optional[Callable]:
    cls = type(self_)
    module_name = inspect.getmodule(cls).__name__
    if module_name.startswith(TRACE_MODULE) and hasattr(cls, method_name):
        log_call(
            getattr(cls, method_name), module_name, self_, *args,
        )
        return lambda: getattr(self_, method_name)(*args)
    return None


def record_binary_method(stack, name):
    """
    Tries recording regular method, and if you cant, record reflected
    """
    if not record_method(f"__{name}__", stack[-2], stack[-1]):
        record_method(f"__r{name}__", stack[-1], stack[-2])


def record_binary_inplace_method(stack, name):
    """
    Tries inplace method, and if cannot be found, uses regular method
    """
    if not record_method(f"__i{name}__", stack[-2], stack[-1]):
        record_binary_method(stack, name)


def record_comparison(stack, name, inverse):
    m = record_method(name, stack[-1], stack[-2])
    if not m or m() == NotImplemented:
        record_method(inverse, stack[-2], stack[-1])


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
    stack = OpStack(frame)
    instruction = list(dis.get_instructions(frame.f_code))[frame.f_lasti]
    oparg = instruction.argval
    opname = instruction.opname

    # handle all opcodes from https://docs.python.org/3/library/dis.html
    # that we care about

    # Unary
    if opname == "UNARY_POSITIVE":
        record_method("__pos__", stack[-1])
    if opname == "UNARY_NEGATIVE":
        record_method("__neg__", stack[-1])
    if opname == "UNARY_NOT":
        # try bool first and if that isn't method record length
        if not record_method("__bool__", stack[-1]):
            record_method("__len__", stack[-1])
    if opname == "UNARY_INVERT":
        record_method("__invert__", stack[-1])
    if opname == "GET_ITER":
        record_method("__iter__", stack[-1])
    if opname == "GET_YIELD_FROM_ITER":
        record_method("__iter__", stack[-1])

    # binary
    if opname == "BINARY_SUBSCR":
        record_method("__getitem__", stack[-1], stack[-2])

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
        record_method("__setitem__", stack[-2], stack[-1], stack[-3])

    if opname == "DELETE_SUBSCR":
        record_method("__delitem__", stack[-2], stack[-1])

    # misc
    if opname == "UNPACK_SEQUENCE":
        record_method("__iter__", stack[-1])
    if opname == "UNPACK_EX":
        record_method("__iter__", stack[-1])

    if opname == "STORE_ATTR":
        record_method("__setattr__", stack[-1], oparg, stack[-2])

    if opname == "DELETE_ATTR":
        record_method("__delattr__", stack[-1], oparg)

    if opname in ("BUILD_TUPLE_UNPACK", "BUILD_LIST_UNPACK", "BUILD_SET_UNPACK"):
        for i in range(1, oparg + 1):
            record_method("__iter__", stack[-i])

    if opname == "BUILD_TUPLE_UNPACK_WITH_CALL":
        args = []
        for i in range(1, oparg + 1):
            arg = stack[-i]
            args.extend(list(arg))
            record_method("__iter__", arg)
        fn = stack[-(oparg + 1)]
        if record_function(fn, *args):
            RECORDED_CALL_FRAMES.add(frame)
    # TODO: BUILD_MAP_UNPACK, BUILD_MAP_UNPACK_WITH_CALL
    if opname == "LOAD_ATTR":
        record_method("__getattr__", stack[-1], oparg)
    if opname == "COMPARE_OP":
        if oparg == "<":
            record_comparison("__lt__", "__gt__")
        if oparg == "<=":
            record_comparison("__le__", "__ge__")
        if oparg == "==":
            record_comparison("__eq__", "__ne__")
        if oparg == "!=":
            record_comparison("__ne__", "__eq__")
        if oparg == ">":
            record_comparison("__gt__", "__lt__")
        if oparg == ">=":
            record_comparison("__ge__", "__le__")
        if oparg in ("in", "not in"):
            # https://docs.python.org/3/reference/expressions.html#membership-test-operations
            if not record_method("__contains__", stack[-2], stack[-1]):
                if not record_method("__iter__", stack[-2]):
                    record_method("__getitem__", stack[-2], 0)

    if opname == "FOR_ITER":
        record_method("__next__", stack[-1])
    if opname == "CALL_FUNCTION":
        args = []
        print(oparg, len(stack))
        for i in range(oparg):
            args.append(stack[-(i + 1)])
            print(args)
        try:
            fn = stack[-(oparg + 1)]
        except IndexError:
            print("failed", args)
            return
        if record_function(fn, *args):
            RECORDED_CALL_FRAMES.add(frame)
    if opname == "CALL_FUNCTION_KW":
        kwargs_names = stack[-1]
        kwargs = {}
        for i, name in enumerate(kwargs_names):
            kwargs[name] = stack[-(i + 2)]
        args = []
        for i in range(oparg):
            args.append(stack[-(i + 1 + len(kwargs_names))])
        fn = stack[-(len(oparg) + 1 + len(kwargs_names))]
        if record_function(fn, *args, **kwargs):
            RECORDED_CALL_FRAMES.add(frame)
    if opname == "CALL_FUNCTION_EX":
        has_kwarg = oparg & int("01", 2)
        if has_kwarg:
            kwargs = stack[-1]
            args = stack[-2]
            fn = stack[-3]
        else:
            kwargs = {}
            args = [-1]
            fn = [-2]
        if record_function(fn, *args, **kwargs):
            RECORDED_CALL_FRAMES.add(frame)
    if opname == "CALL_METHOD":
        args = []
        for i in range(oparg):
            args.append(stack[-(i + 1)])
        self_ = stack[-(oparg + 1)]
        method = stack[-(oparg + 2)]
        if self_:
            res = record_function(method, self_, *args)
        else:
            res = record_function(method, *args)
        if res:
            RECORDED_CALL_FRAMES.add(frame)


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
