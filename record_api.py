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

MAX_LENGTH = 50

ENCODERS: Dict[Type, Callable[[object], object]] = {
    tuple: lambda o: o,
    types.ModuleType: lambda o: o.__name__,
    slice: lambda s: (s.start, s.stop, s.step),
}

try:
    import numpy
except ImportError:
    pass
else:
    ENCODERS[numpy.ndarray] = lambda a: {"shape": a.shape, "dtype": a.dtype}


class JSONEncoder(json.JSONEncoder):
    def default(self, o: object) -> object:
        """
        JSON encoder that special cases some types 
        """

        if isinstance(o, (str, list)):
            o = o[:MAX_LENGTH]
        elif isinstance(o, (dict, int, float, bool, type(None))):
            pass
        else:
            tp = type(o)
            module = inspect.getmodule(tp)
            assert module
            tp_name = f"{module.__name__}.{tp.__qualname__}"

            if tp in ENCODERS:
                o = {"__tp": tp_name, "__v": ENCODERS[tp](o)}
            else:
                o = {"__tp": tp_name}
        return o


def save_log(fn: str, params: Dict[str, object],) -> None:
    data = {
        "function": fn,
        "params": params,
    }
    writer.write((json.dumps(data, cls=JSONEncoder) + "\n").encode())


def log_call(fn: Callable, *args, **kwargs) -> None:
    if isinstance(fn, types.MethodDescriptorType):
        module = inspect.getmodule(fn.__objclass__)
    else:
        # for ufuuncs get module of type of ufunc
        module = inspect.getmodule(fn) or inspect.getmodule(type(fn))
    if not module:
        warnings.warn(f"Cannot get module for {fn}")
        return
    # ufuncs dont have qualname
    fn_name = f"{module.__name__}.{getattr(fn, '__qualname__', fn.__name__)}"

    try:
        sig = inspect.signature(fn)
    except ValueError:
        params = kwargs
        for i, value in enumerate(args):
            params[str(i)] = value
    else:
        params = sig.bind(*args, **kwargs).arguments

    save_log(fn_name, params)


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
            # If this is a method implemented in C, expand it
            # to classes function and add self as an arg
            if isinstance(fn, types.BuiltinMethodType) and not isinstance(
                fn.__self__, types.ModuleType
            ):
                self_ = fn.__self__
                args = (self_, *args)
                fn = getattr(type(self_), fn.__name__)
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

    # A set of all the IDs of code objects which we have ignored. Their parent
    # frame calls are in `record_calls`. We need to save this so that if we
    # end up in a frame of a child call where we shouldnt be tracing we
    # can exit early. It's unclear why we need this, because we shouldn't
    # hit these frames anyway. But if we dont, we go into them unintentionally.
    # See this Python bug: https://bugs.python.org/issue11992
    ignored_code_ids: Set[int] = dataclasses.field(default_factory=set)

    def __enter__(self):
        # also set tracing on parent frames
        frame = inspect.currentframe()
        if frame:
            # frame.f_trace = self  # type: ignore
            # frame.f_trace_opcodes = True
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
            if isinstance(value, types.BuiltinMethodType):
                # if this was a method defined in C, use the instance as the value
                value = value.__self__
            module = inspect.getmodule(value) or inspect.getmodule(type(value))
            if not module:
                warnings.warn(f"Cannot get module of {value}")
                continue
            if module.__name__.startswith(self.module):
                return True
        return False

    def __call__(self, frame, event, arg) -> Optional[Tracer]:
        outer_frame = frame
        while outer_frame:
            if id(outer_frame.f_code) in self.ignored_code_ids:
                return None
            outer_frame = outer_frame.f_back

        if event == "call":
            try:
                self.recorded_calls.remove(self._frame_to_key(frame.f_back))
            except KeyError:
                # we didnt record the call frame, so keep tracing
                frame.f_trace_opcodes = True
                return self
            self.ignored_code_ids.add(id(frame.f_code))
            frame.f_trace = None
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
            function_or_self = stack.pop()
            null_or_method = stack.pop()
            if null_or_method is stack.NULL:
                process((function_or_self,), function_or_self, *args)
            else:
                process((function_or_self,), null_or_method, function_or_self, *args)
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
