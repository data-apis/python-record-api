from __future__ import annotations

import dataclasses
import dis
import functools
import inspect
import itertools
import operator as op
import os
import sys
import types
import warnings
from typing import *

from . import jsonl

import opcode

from . import get_stack

__all__ = ["Tracer", "setup", "finalize", "get_tracer"]

DEBUG = os.environ.get("PYTHON_RECORD_API_DEBUG", False)


# global cache for tracer based on env variables
TRACER = None

context_manager: Optional[ContextManager] = None
write_line: Optional[Callable[[dict], None]] = None


def get_tracer() -> Tracer:
    global TRACER
    if not TRACER:
        FROM_MODULES = os.environ["PYTHON_RECORD_API_TO_MODULES"].split(",")
        TO_MODULES = os.environ["PYTHON_RECORD_API_FROM_MODULES"].split(",")
        TRACER = Tracer(FROM_MODULES, TO_MODULES)
    return TRACER


def getmodulename(v):
    if isinstance(v, types.ModuleType):
        return v.__name__
    if isinstance(v, types.MethodDescriptorType):
        return getmodulename(v.__objclass__)
    return getattr(v, "__module__", None)


@functools.singledispatch
def encode(o: object) -> object:
    """
    Encodes an object for serialization. Type is always serialized as well
    If falsy is returned, the value is not included.
    """
    return None


@encode.register
def _encode_module(o: types.ModuleType):
    return o.__name__


@encode.register
def _encode_slice(s: slice):
    return {
        "start": preprocess(s.start),
        "stop": preprocess(s.stop),
        "step": preprocess(s.step),
    }


# # cache this b/c its expesnive
# @functools.lru_cache(None, False)
# def find_root_module(o: object):
#     """
#     Looks from the top of the module tree down to see if it is exportd from a parent module
#     """
#     full_module = o.__module__
#     modules = full_module.split(".")
#     if len(modules) == 1:
#         return modules[0]
#     for i in range(len(modules) - 1):
#         parent_module = ".".join(modules[i:])
#         mod = importlib.import_module(parent_module)
#         # Export by module
#         if o in mod


@encode.register(types.FunctionType)
@encode.register(type)
def encode_module_value(v):
    """
    For all things not in builtins, return the module name, otherwise just return the name
    """
    mod = v.__module__
    v = getattr(v, "__qualname__", v.__name__)
    if mod == "builtins":
        return v
    return {"module": mod, "name": v}


@encode.register
def _encode_builtin_function_method(m: types.BuiltinMethodType):
    self = m.__self__
    # If the self is a module, then this is a function and we can just emit the module
    # as a string
    if isinstance(self, types.ModuleType):
        return encode_module_value(m)
    # otherwise it's a method, so actually emit the self
    return {"name": m.__name__, "self": preprocess(self)}


@encode.register
def _encode_method(m: types.MethodType):
    return {"self": preprocess(m.__self__), "name": m.__name__}


@encode.register
def _encode_method_descriptor(m: types.MethodDescriptorType):
    """
    This is actually a method, not a classmethod!

    np.ndarray.mean(x)
    or
    np.arange(10).mean()

    both end up being the same call, we can't tell the difference.
    """
    # TODO: Remove class, we can grab off of first arg
    return {"name": m.__name__, "class": m.__objclass__}


try:
    import numpy
except ImportError:
    pass
else:

    @encode.register
    def encode_array(a: numpy.ndarray):
        return {"dtype": a.dtype.name}

    @encode.register
    def encode_dtype(d: numpy.dtype):
        return d.name

    @encode.register
    def encode_ufunc(u: numpy.ufunc):
        return u.__name__

    @encode.register
    def encode_convert_to_ma(u: numpy.ma.core._convert2ma):
        return u._func.__name__


MAX_LIST = 10
MAX_TUPLE = 10
MAX_DICT = 10
MAX_STRING = 20


def preprocess(o):
    """
    Preserves lists, strings, and None. Tuples and dicts are recursed.
    
    All others primitive subclasses are replaced with their types.

    All non primitives subclasses are passed through to be handled by `default`.
    """
    tp = type(o)
    if tp == str and len(o) <= MAX_STRING:
        return o
    if tp == list:
        return [preprocess(v) for v in o[:MAX_LIST]]
    if tp == dict:
        return {
            "t": "dict",
            "v": [
                [preprocess(k), preprocess(v)] for k, v in list(o.items())[:MAX_DICT]
            ],
        }
    if tp == tuple:
        return {
            "t": "tuple",
            "v": [preprocess(v) for v in o[:MAX_TUPLE]],
        }
    if isinstance(o, (int, float, bool, list, str, dict, tuple)):
        # Don't send literals of these
        return {"t": encode_module_value(tp)}
    # Other types will be encoded by the `default` function.
    return o


def default(o: object) -> object:
    """
    JSON encoder that special cases some types 
    """

    t = encode_module_value(type(o))
    v = encode(o)
    if v:
        return {"t": t, "v": v}
    return {"t": t}


# cache this b/c its expesnive
@functools.lru_cache(None, False)
def signature(fn):
    return inspect.signature(fn)


@dataclasses.dataclass
class Bound:
    """
    Bound args returns 
    """

    pos_only: List[Tuple[str, object]] = dataclasses.field(default_factory=list)
    pos_or_kw: List[Tuple[str, object]] = dataclasses.field(default_factory=list)
    var_pos: Optional[Tuple[str, List[object]]] = None
    kw_only: Dict[str, object] = dataclasses.field(default_factory=dict)
    var_kw: Optional[Tuple[str, Dict[str, object]]] = None

    def as_dict(self):
        """
        Turn into dict, ignoring empty values
        """
        d = {}
        for f in ["pos_only", "pos_or_kw", "var_pos", "kw_only", "var_kw"]:
            v = getattr(self, f)
            if v:
                d[f] = v
        return d

    @classmethod
    def create(cls, fn, args, kwargs) -> Optional[Bound]:
        try:
            sig = signature(fn)
        except ValueError:
            return None
        try:
            bound = sig.bind(*args, **kwargs)
        except TypeError:
            return None
        b = cls()
        for k, v in bound.arguments.items():
            kind = sig.parameters[k].kind
            if kind == inspect.Parameter.POSITIONAL_ONLY:
                b.pos_only.append((k, preprocess(v)))
            elif kind == inspect.Parameter.POSITIONAL_OR_KEYWORD:
                b.pos_or_kw.append((k, preprocess(v)))
            elif kind == inspect.Parameter.VAR_POSITIONAL:
                b.var_pos = k, preprocess(v)
            elif kind == inspect.Parameter.KEYWORD_ONLY:
                b.kw_only[k] = preprocess(v)
        return b


# TODO: Make not args kwargs, since kwarg could be fn
def log_call(location: str, fn: Callable, *args, **kwargs) -> None:
    bound = Bound.create(fn, args, kwargs)
    line: Dict = {"location": location, "function": preprocess(fn)}
    if bound is None:
        line["params"] = {}
        if args:
            line["params"]["args"] = [preprocess(a) for a in args]
        if kwargs:
            line["params"]["kwargs"] = {k: preprocess(v) for k, v in kwargs.items()}
    else:
        line["bound_params"] = bound.as_dict()
    assert write_line
    write_line(line)


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
        # Note: This take args as an iterable, instead of as a varargs, so that if we don't trace we don't have to expand the iterable
        if self.tracer.should_trace(*keyed_args):
            filename = self.frame.f_code.co_filename
            line = self.frame.f_lineno
            log_call(f"{filename}:{line}", fn, *args, **kwargs)

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
        iterables = []
        for _ in range(self.oparg):
            arg = self.pop()
            if inspect.isgenerator(arg):
                return
            iterables.append(arg)
            self.process((arg,), iter, (arg,))
        fn = self.pop()
        self.process((fn,), fn, itertools.chain.from_iterable(iterables))

    # TODO: BUILD_MAP_UNPACK, BUILD_MAP_UNPACK_WITH_CALL

    def op_COMPARE_OP(self):
        # list from
        # https://github.com/python/cpython/blob/81de3c225774179cdc82a1733a64e4a876ff02b5/Lib/opcode.py#L24-L25
        val = self.opvalcompare
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
        if val in COMPARISONS:
            self.process(
                (self.TOS, self.TOS1) if "in" not in val else (self.TOS),
                COMPARISONS[val],
                # "in" and "not in" are reversed
                (self.TOS1, self.TOS,) if "in" not in val else (self.TOS, self.TOS1,),
            )

    def op_CALL_FUNCTION(self):
        args = self.pop_n(self.oparg)
        fn = self.pop()
        self.process((fn,), fn, args)

    def op_CALL_FUNCTION_KW(self):
        kwargs_keys = self.pop()
        n_kwargs = len(kwargs_keys)
        kwarg_values = self.pop_n(n_kwargs)
        kwargs = {k: v for k, v in zip(kwargs_keys, kwarg_values)}
        args = self.pop_n(self.oparg - n_kwargs)
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
        if inspect.isgenerator(args):
            return
        self.process((fn,), fn, args, kwargs)

    def op_CALL_METHOD(self):
        args = self.pop_n(self.oparg)
        function_or_self = self.pop()
        null_or_method = self.pop()
        if null_or_method is self.NULL:
            function = function_or_self
            self.process((function,), function, args)
        else:
            self_ = function_or_self
            method = null_or_method
            self.process(
                (self_,), method, itertools.chain((self_,), args),
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
    # the modules we should trace calls to
    calls_to_modules: List[str]
    # the modules we should trace calls from
    calls_from_modules: List[str]

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
            if any(module.startswith(mod) for mod in self.calls_to_modules):
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
        return frame_module_name == "__main__" or any(
            frame_module_name == mod or frame_module_name.startswith(mod + ".")
            for mod in self.calls_from_modules
        )


def setup():
    global write_line, context_manager
    FILE_NAME = os.environ["PYTHON_RECORD_API_OUTPUT_FILE"]
    context_manager = jsonl.write(FILE_NAME, default=default)
    write_line = context_manager.__enter__()


def finalize():
    assert context_manager
    context_manager.__exit__(*sys.exc_info())
