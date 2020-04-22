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
import opcode
from typing import *

import get_stack

__all__ = ["Tracer"]

DEBUG = os.environ.get("PYTHON_API_DEBUG", False)

MAX_LENGTH = 50


def type_repr(tp: Type) -> str:
    module = inspect.getmodule(tp)
    assert module
    return f"{module.__name__}.{tp.__qualname__}"


ENCODERS: Dict[Type, Callable[[Any], object]] = {
    types.ModuleType: lambda o: o.__name__,
    slice: lambda s: [s.start, s.stop, s.step],
    type: type_repr,
    types.MethodType: lambda m: [m.__self__, m.__name__],
}

try:
    import numpy
except ImportError:
    pass
else:
    ENCODERS[numpy.ndarray] = lambda a: [list(a.shape), a.dtype.name]
    ENCODERS[numpy.dtype] = lambda d: d.name


def preprocess(o):
    """
    Turns tuples into dicts, removes long values, and turns dicts into lists (so that keys can be any type)
    """
    if isinstance(o, str):
        return o[:MAX_LENGTH]
    elif isinstance(o, list):
        return [preprocess(v) for v in o[:MAX_LENGTH]]
    elif isinstance(o, dict):
        return {
            "t": "dict",
            "v": [
                [preprocess(k), preprocess(v)] for k, v in list(o.items())[:MAX_LENGTH]
            ],
        }
    elif isinstance(o, tuple):
        return {"t": "tuple", "v": preprocess(list(o))}
    return o


class JSONEncoder(json.JSONEncoder):
    def default(self, o: object) -> object:
        """
        JSON encoder that special cases some types 
        """

        tp = type(o)
        for encoder_tp, encoder in ENCODERS.items():
            if issubclass(tp, encoder_tp):
                return {"t": type_repr(tp), "v": preprocess(encoder(o))}
        return {"t": type_repr(tp)}


def save_log(fn: str, params: Dict[str, object],) -> None:
    data = {
        "function": fn,
        "params": {k: preprocess(v) for k, v in params.items()},
    }
    writer.write((json.dumps(data, cls=JSONEncoder) + "\n").encode())


def get_arguments(fn, args, kwargs):
    try:
        sig = inspect.signature(fn)
    except ValueError:
        return None
    try:
        return sig.bind(*args, **kwargs).arguments
    except TypeError:
        return None


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
    name = getattr(fn, "__qualname__", getattr(fn, "__name__", fn))
    fn_name = f"{module.__name__}.{name}"

    params = get_arguments(fn, args, kwargs)
    if params is None:
        params = kwargs
        for i, value in enumerate(args):
            params[str(i)] = value
    save_log(fn_name, params)


@dataclasses.dataclass
class Stack:
    tracer: Tracer
    frame: Any
    NULL: ClassVar[object] = object()
    current_i: int = dataclasses.field(init=False, default=0)
    opcode: int = dataclasses.field(init=False)

    def __post_init__(self):
        self.op_stack = get_stack.OpStack(self.frame)
        self.opcode = self.frame.f_code.co_code[self.frame.f_lasti]

    @property
    def oparg(self):
        # sort of replicates logic in dis._unpack_opargs but doesn't account for extended
        # args, oh well!
        return self.frame.f_code.co_code[self.frame.f_lasti + 1]

    @property
    def opname(self):
        return opcode.opname[self.opcode]

    @property
    def opvalname(self):
        """
        We could use `dis.get_instructions` but it's really slow!
        We move some of the logic as in `_get_instructions_bytes`
        to later, so we can only process instructions we care about.
        """
        return self.frame.f_code.co_names[self.oparg]

    @property
    def opvalcompare(self):
        """

        We also remove the switches we dont use
        """
        return dis.cmp_op[self.oparg]

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

    top_level_frame: object = dataclasses.field(default=None)

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
                self.top_level_frame = parent_frame
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
        if (event != "opcode") and (event != "call"):
            return None
        outer_frame = frame
        while outer_frame and outer_frame is not self.top_level_frame:
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

        stack = Stack(self, frame)
        opname = stack.opname
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
            process((stack.TOS,), getattr, stack.TOS, stack.opvalname)

        if opname == "STORE_ATTR":
            process((stack.TOS,), setattr, stack.TOS, stack.opvalname, stack.TOS1)

        if opname == "DELETE_ATTR":
            process((stack.TOS,), delattr, stack.TOS, stack.opvalname)

        if opname in ("BUILD_TUPLE_UNPACK", "BUILD_LIST_UNPACK", "BUILD_SET_UNPACK"):
            for value in stack.pop_n(stack.oparg):
                process((value,), iter, value)

        if opname == "BUILD_TUPLE_UNPACK_WITH_CALL":
            args = []
            for _ in range(stack.oparg):
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
                # Ignore these for now since there are so many of them!
                # "is": op.is_,
                # "is not": op.is_not,
            }
            if stack.opvalcompare in COMPARISONS:
                process(
                    (stack.TOS, stack.TOS1),
                    COMPARISONS[stack.opvalcompare],
                    stack.TOS1,
                    stack.TOS,
                )

        if opname == "CALL_FUNCTION":
            args = stack.pop_n(stack.oparg)
            fn = stack.pop()
            process((fn,), fn, *args)

        if opname == "CALL_FUNCTION_KW":
            kwargs_names = stack.pop()
            kwargs = {name: stack.pop() for name in kwargs_names}
            args = stack.pop_n(stack.oparg - len(kwargs_names))
            fn = stack.pop()
            process((fn,), fn, *args, **kwargs)

        if opname == "CALL_FUNCTION_EX":
            has_kwarg = stack.oparg & int("01", 2)
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
            args = stack.pop_n(stack.oparg)
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
        for name in IMPORT_MODULES.split(","):
            importlib.import_module(name)

    try:
        with Tracer(TRACE_MODULE):
            runpy.run_module(RUN_MODULE, run_name="__main__", alter_sys=True)
    except Exception:
        raise Exception(f"Error running {RUN_MODULE}")
    finally:
        writer.flush()
        rand_file.close()
