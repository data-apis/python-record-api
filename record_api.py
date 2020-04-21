from __future__ import annotations
import importlib
import inspect
import io
import json
import os
import runpy
import sys
import types
import dis
import operator as op
import dataclasses
import warnings

from typing import *

import get_stack

__all__ = ["Tracer"]

DEBUG = os.environ.get("PYTHON_API_DEBUG", False)


def type_name(value: object) -> str:
    tp = type(value)
    module = inspect.getmodule(tp)
    if not module:
        raise ValueError(f"Cannot get module for {tp}")
    return f"{module.__name__}.{tp.__qualname__}"


def save_log(
    fn: str,
    caller_args: List[str],
    caller_kwargs: Dict[str, str],
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


def log_call(fn: Callable, *args, **kwargs) -> None:
    module = inspect.getmodule(fn)
    if not module:
        warnings.warn("Cannot get module for {fn}")
        return
    fn_name = f"{module.__name__}.{fn.__qualname__}"
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


def get_instruction(frame):
    for instruction in dis.get_instructions(frame.f_code):
        if instruction.offset == frame.f_lasti:
            return instruction
    raise ValueError("Couldn't find instruction by offset")


@dataclasses.dataclass
class Stack:
    NULL: ClassVar[object] = object()
    tracer: Tracer
    frame: object
    op_stack: get_stack.OpStack = dataclasses.field(init=False)
    current_i: int = dataclasses.field(init=False, default=0)

    def __post_init__(self):
        self.op_stack = get_stack.OpStack(self.frame)

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

    def pop_n(self, n: int) -> List:
        """
        removes the top N items from the stack and returns them so the top item is on the left.
        """
        l = [self.pop() for _ in range(n)]
        # so that top of the stack is on the right
        l.reverse()
        return l

    def process(self, keyed_args: Tuple, fn: Callable, *args, **kwargs) -> None:
        if self.tracer.should_trace(*keyed_args):
            log_call(fn, *args, **kwargs)
            self.tracer.recorded_calls.add(self.tracer._frame_to_key(self.frame))


@dataclasses.dataclass
class Tracer:
    # the module we should trace
    module: str

    # Keep a set of frames that we have recorded a call
    # from. We should add to this when we record a bytecode
    # trace from a function call
    # we should pop one off this to check if we should keep tracing
    # below this frame

    # Tuple of code id and index of instruction
    recorded_calls: Set[Tuple[int, int]] = dataclasses.field(default_factory=set)

    def __enter__(self):
        # also set tracing on parent frames
        frame = inspect.currentframe()
        if frame:
            frame.f_trace = self  # type: ignore
            frame.f_trace_opcodes = True
            parent_frame = frame.f_back
            if parent_frame:
                parent_frame.f_trace = self  # type: ignore
                parent_frame.f_trace_opcodes = True
        sys.settrace(self)

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.settrace(None)

    @staticmethod
    def _frame_to_key(frame):
        return (id(frame.f_code), frame.f_lasti)

    def should_trace(self, *values) -> bool:
        for value in values:
            module = inspect.getmodule(value) or inspect.getmodule(type(value))
            if not module:
                warnings.warn(f"Cannot get module of {value}")
                continue
            if module.__name__.startswith(self.module):
                return True
        return False

    def __call__(self, frame, event, arg) -> Optional[Tracer]:
        frame.f_trace_opcodes = True
        if event == "call":
            try:
                self.recorded_calls.remove(self._frame_to_key(frame.f_back))
            except KeyError:
                # we didnt record the call frame, so keep tracing
                return self
            frame.f_trace_opcodes = False
            # we did record this call frame, so dont trace below here
            return None
        if event != "opcode":
            return None

        instruction = get_instruction(frame)
        oparg = instruction.argval
        opname = instruction.opname
        stack = Stack(self, frame)
        process = stack.process
        # handle all opcodes from https://docs.python.org/3/library/dis.html
        # that we care about

        if DEBUG:
            bytecode = dis.Bytecode(frame.f_code, current_offset=frame.f_lasti)
            print(bytecode.dis())

        # print(opname)
        # Unary
        UNARY_OPS = {
            "UNARY_POSITIVE": op.pos,
            "UNARY_NEGATIVE": op.neg,
            "UNARY_NOT": op.not_,
            "UNARY_INVERT": op.invert,
            "GET_ITER": iter,
            "GET_YIELD_FROM_ITER": iter,
            "UNPACK_SEQUENCE": iter,
            "UNPACK_EX": iter,
            "FOR_ITER": iter,
        }
        if opname in UNARY_OPS:
            process((stack.TOS,), UNARY_OPS[opname], stack.TOS)

        # binary

        BINARY_OPS = {
            "BINARY_POWER": op.pow,
            "BINARY_MULTIPLY": op.mul,
            "BINARY_MATRIX_MULTIPLY": op.matmul,
            "BINARY_FLOOR_DIVIDE": op.floordiv,
            "BINARY_TRUE_DIVIDE": op.truediv,
            "BINARY_MODULO": op.mod,
            "BINARY_ADD": op.add,
            "BINARY_SUBTRACT": op.sub,
            "BINARY_LSHIFT": op.lshift,
            "BINARY_RSHIFT": op.rshift,
            "BINARY_AND": op.and_,
            "BINARY_XOR": op.xor,
            "BINARY_OR": op.or_,
            "INPLACE_POWER": op.ipow,
            "INPLACE_MULTIPLY": op.imul,
            "INPLACE_MATRIX_MULTIPLY": op.imatmul,
            "INPLACE_FLOOR_DIVIDE": op.ifloordiv,
            "INPLACE_TRUE_DIVIDE": op.itruediv,
            "INPLACE_MODULO": op.imod,
            "INPLACE_ADD": op.iadd,
            "INPLACE_SUBTRACT": op.isub,
            "INPLACE_LSHIFT": op.ilshift,
            "INPLACE_RSHIFT": op.irshift,
            "INPLACE_AND": op.iand,
            "INPLACE_OR": op.ior,
            "INPLACE_XOR": op.ixor,
        }
        if opname in BINARY_OPS:
            process((stack.TOS, stack.TOS1), BINARY_OPS[opname], stack.TOS1, stack.TOS)

        # special case subscr b/c we only check first arg, not both
        if opname == "BINARY_SUBSCR":
            process((stack.TOS1,), op.getitem, stack.TOS1, stack.TOS)

        if opname == "STORE_SUBSCR":
            process((stack.TOS1,), op.setitem, stack.TOS1, stack.TOS, stack.TOS2)

        if opname == "DELETE_SUBSCR":
            process((stack.TOS1,), op.delitem, stack.TOS1, stack.TOS)

        if opname == "LOAD_ATTR":
            process((stack.TOS,), getattr, stack.TOS, oparg)

        if opname == "STORE_ATTR":
            process((stack.TOS,), setattr, stack.TOS, oparg, stack.TOS1)

        if opname == "DELETE_ATTR":
            process((stack.TOS,), delattr, stack.TOS, oparg)

        if opname in ("BUILD_TUPLE_UNPACK", "BUILD_LIST_UNPACK", "BUILD_SET_UNPACK"):
            for value in stack.pop_n(oparg):
                process((value,), iter, value)

        if opname == "BUILD_TUPLE_UNPACK_WITH_CALL":
            args = []
            for _ in range(oparg):
                arg = stack.pop()
                args.extend(list(arg))
                process((arg,), iter, arg)
            fn = stack.pop()
            process((fn,), fn, *args)

        # TODO: BUILD_MAP_UNPACK, BUILD_MAP_UNPACK_WITH_CALL

        if opname == "COMPARE_OP":
            # list from
            # https://github.com/python/cpython/blob/81de3c225774179cdc82a1733a64e4a876ff02b5/Lib/opcode.py#L24-L25
            COMPARISONS = {
                "<": op.lt,
                "<": op.le,
                "==": op.eq,
                "!=": op.ne,
                ">": op.gt,
                ">=": op.ge,
                "in": op.contains,
                "not in": op.contains,
                "is": op.is_,
                "is not": op.is_not,
            }
            if oparg in COMPARISONS:
                process(
                    (stack.TOS, stack.TOS1), COMPARISONS[oparg], stack.TOS1, stack.TOS
                )

        if opname == "CALL_FUNCTION":
            args = stack.pop_n(oparg)
            fn = stack.pop()
            process((fn,), fn, *args)

        if opname == "CALL_FUNCTION_KW":
            kwargs_names = stack.pop()
            kwargs = {name: stack.pop() for name in kwargs_names}
            args = stack.pop_n(oparg - len(kwargs_names))
            fn = stack.pop()
            process((fn,), fn, *args, **kwargs)

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
            process((fn,), fn, *args, **kwargs)

        if opname == "CALL_METHOD":
            args = stack.pop_n(oparg)
            self_ = stack.pop()
            method = stack.pop()

            if self_ is stack.NULL:
                process((method,), method, *args)
            else:
                process((method,), method, self_, *args)
        return None


if __name__ == "__main__":
    FILE_NAME = os.environ["PYTHON_API_OUTPUT_FILE"]
    IMPORT_MODULES = os.environ.get("PYTHON_API_IMPORT_MODULES", "")
    RUN_MODULE = os.environ["PYTHON_API_RUN_MODULE"]
    TRACE_MODULE = os.environ["PYTHON_API_TRACE_MODULE"]

    rand_file = io.FileIO(FILE_NAME, "w")
    writer = io.BufferedWriter(rand_file)

    if IMPORT_MODULES:
        for module in IMPORT_MODULES.split(","):
            importlib.import_module(module)
    try:
        with Tracer(TRACE_MODULE):
            runpy.run_module(RUN_MODULE, run_name="__main__", alter_sys=True)
    except Exception:
        raise Exception(f"Error running {RUN_MODULE}")
    finally:
        writer.flush()
        rand_file.close()
