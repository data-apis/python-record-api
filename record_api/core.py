from __future__ import annotations
import inspect
import io
import json
import os
import sys
import types
import dis
import operator as op
import dataclasses
import warnings
import opcode
import functools
from typing import *
import itertools

from . import get_stack

__all__ = ["Tracer", "setup", "finalize", "get_tracer"]

DEBUG = os.environ.get("PYTHON_RECORD_API_DEBUG", False)

MAX_LENGTH = 50

# global cache for tracer based on env variables
TRACER = None


def get_tracer() -> Tracer:
    global TRACER
    if not TRACER:
        FROM_MODULE = os.environ["PYTHON_RECORD_API_TO_MODULE"]
        TO_MODULE = os.environ["PYTHON_RECORD_API_FROM_MODULE"]
        TRACER = Tracer(FROM_MODULE, TO_MODULE)
    return TRACER


def getmodulename(v):
    if isinstance(v, types.ModuleType):
        return v.__name__
    return getattr(v, "__module__", None)


def type_repr(tp: Type) -> str:
    module = getmodulename(tp)
    assert module
    return f"{module}.{tp.__qualname__}"


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

    def encode_array(a: numpy.ndarray):
        return [list(a.shape), a.dtype.name]

    def encode_dtype(d: numpy.dtype):
        return d.name

    ENCODERS[numpy.ndarray] = encode_array
    ENCODERS[numpy.dtype] = encode_dtype


PRIMITIVE_TYPES = (str, int, float)


def preprocess(o):
    """
    Turns tuples into dicts, removes long values, and turns dicts into lists (so that keys can be any type).

    Also wraps types that are subtypes of primitives, but not primitives themselves, to provide types.
    """
    tp = type(o)
    if isinstance(o, PRIMITIVE_TYPES) and tp not in PRIMITIVE_TYPES:
        return {"t": type_repr(tp), "v": o}
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


def save_log(filename: str, line: int, fn: str, params: Dict[str, object],) -> None:
    assert writer
    data = {
        "location": f"{filename}:{line}",
        "function": fn,
        "params": {k: preprocess(v) for k, v in params.items()},
    }
    writer.write((json.dumps(data, cls=JSONEncoder) + "\n").encode())


# cache this b/c its expesnive
@functools.lru_cache(None, False)
def signature(fn):
    return inspect.signature(fn)


def get_arguments(fn, args, kwargs):
    try:
        sig = signature(fn)
    except ValueError:
        return None
    try:
        return sig.bind(*args, **kwargs).arguments
    except TypeError:
        return None


def log_call(filename: str, line: int, fn: Callable, *args, **kwargs) -> None:
    if isinstance(fn, types.MethodDescriptorType):
        module = getmodulename(fn.__objclass__)
    else:
        # for ufuuncs get module of type of ufunc
        module = getmodulename(fn) or getmodulename(type(fn))
    if not module:
        warnings.warn(f"Cannot get module for {fn}")
        return
    # ufuncs dont have qualname
    name = getattr(fn, "__qualname__", getattr(fn, "__name__", fn))
    fn_name = f"{module}.{name}"

    params = get_arguments(fn, args, kwargs)
    if params is None:
        params = kwargs
        for i, value in enumerate(args):
            params[str(i)] = value
    save_log(filename, line, fn_name, params)


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
        to later, so we can only self.process instructions we care about.
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

    def process(
        self, keyed_args: Tuple, fn: Callable, args: Iterable, kwargs: Mapping = {}
    ) -> None:
        if self.tracer.should_trace(*keyed_args):
            # If this is a method implemented in C, expand it
            # to classes function and add self as an arg
            if isinstance(fn, types.BuiltinMethodType) and not isinstance(
                fn.__self__, (types.ModuleType, type)
            ):
                self_ = fn.__self__
                args = (self_, *args)
                fn = getattr(type(self_), fn.__name__)
            filename = self.frame.f_code.co_filename
            line = self.frame.f_lineno
            log_call(filename, line, fn, *args, **kwargs)

    def __call__(self) -> None:
        """
        handle all opcodes from https://docs.python.org/3/library/dis.html
        that we care about
        """
        opname = self.opname
        if opname in UNARY_OPS:
            return self.process((self.TOS,), UNARY_OPS[opname], (self.TOS,))

        if opname in BINARY_OPS:
            return self.process(
                (self.TOS, self.TOS1), BINARY_OPS[opname], (self.TOS1, self.TOS)
            )

        method_name = f"op_{opname}"
        if hasattr(self, method_name):
            getattr(self, method_name)()
        return None

    # special case subscr b/c we only check first arg, not both
    def op_BINARY_SUBSCR(self):
        self.process((self.TOS1,), op.getitem, (self.TOS1, self.TOS))

    def op_STORE_SUBSCR(self):
        self.process((self.TOS1,), op.setitem, (self.TOS1, self.TOS, self.TOS2))

    def op_DELETE_SUBSCR(self):
        self.process((self.TOS1,), op.delitem, (self.TOS1, self.TOS))

    def op_LOAD_ATTR(self):
        self.process((self.TOS,), getattr, (self.TOS, self.opvalname))

    def op_STORE_ATTR(self):
        self.process((self.TOS,), setattr, (self.TOS, self.opvalname, self.TOS1))

    def op_DELETE_ATTR(self):
        self.process((self.TOS,), delattr, (self.TOS, self.opvalname))

    def op_BUILD_TUPLE_UNPACK(self):
        for value in self.pop_n(self.oparg):
            self.process((value,), iter, (value,))

    def op_BUILD_LIST_UNPACK(self):
        self.op_BUILD_TUPLE_UNPACK()

    def op_BUILD_SET_UNPACK(self):
        self.op_BUILD_TUPLE_UNPACK()

    def op_BUILD_TUPLE_UNPACK_WITH_CALL(self):
        args = []
        for _ in range(self.oparg):
            arg = self.pop()
            args.extend(list(arg))
            self.process((arg,), iter, (arg,))
        fn = self.pop()
        self.process((fn,), fn, args)

    # TODO: BUILD_MAP_UNPACK, BUILD_MAP_UNPACK_WITH_CALL

    def op_COMPARE_OP(self):
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
        if self.opvalcompare in COMPARISONS:
            self.process(
                (self.TOS, self.TOS1),
                COMPARISONS[self.opvalcompare],
                (self.TOS1, self.TOS,),
            )

    def op_CALL_FUNCTION(self):
        args = self.pop_n(self.oparg)
        fn = self.pop()
        self.process((fn,), fn, args)

    def op_CALL_FUNCTION_KW(self):
        kwargs_names = self.pop()
        kwargs = {name: self.pop() for name in kwargs_names}
        args = self.pop_n(self.oparg - len(kwargs_names))
        fn = self.pop()
        self.process((fn,), fn, args, kwargs)

    def op_CALL_FUNCTION_EX(self):
        has_kwarg = self.oparg & int("01", 2)
        if has_kwarg:
            kwargs = self.pop()
            args = self.pop()
            fn = self.pop()
        else:
            kwargs = {}
            args = self.pop()
            fn = self.pop()
        self.process((fn,), fn, args, kwargs)

    def op_CALL_METHOD(self):
        args = self.pop_n(self.oparg)
        function_or_self = self.pop()
        null_or_method = self.pop()
        if null_or_method is self.NULL:
            self.process((function_or_self,), function_or_self, args)
        else:
            self.process(
                (function_or_self,),
                null_or_method,
                itertools.chain((function_or_self,), args),
            )


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


@dataclasses.dataclass
class Tracer:
    # the module we should trace calls to
    calls_to_module: str
    # the module we should trace calls from
    calls_from_module: str

    def __enter__(self):
        sys.settrace(self)

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.settrace(None)

    def should_trace(self, *values) -> bool:
        for value in values:
            if isinstance(value, types.BuiltinMethodType):
                # if this was a method defined in C, use the instance as the value
                value = value.__self__
            module = getmodulename(value) or getmodulename(type(value))
            if not module:
                warnings.warn(f"Cannot get module of {value}")
                continue
            if module.startswith(self.calls_to_module):
                return True
        return False

    def __call__(self, frame, event, arg) -> Optional[Tracer]:
        if event == "call":
            frame.f_trace_opcodes = True
            return self
        elif event != "opcode":
            return None

        if self.should_trace_frame(frame):
            Stack(self, frame)()
        return None

    def should_trace_frame(self, frame) -> bool:
        # Ignore frames which are not from the `calls_from_module`
        try:
            frame_module_name = frame.f_globals["__name__"]
        except KeyError:
            return False
        return (
            frame_module_name == "__main__"
            or frame_module_name == self.calls_from_module
            or frame_module_name.startswith(self.calls_from_module + ".")
        )


writer = None
rand_file = None


def setup():
    global writer, rand_file
    FILE_NAME = os.environ["PYTHON_RECORD_API_OUTPUT_FILE"]
    rand_file = io.FileIO(FILE_NAME, "w")
    writer = io.BufferedWriter(rand_file)


def finalize():
    assert writer
    assert rand_file
    writer.flush()
    rand_file.close()
