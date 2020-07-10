"""
This analysis is meant to run on the raw data and produce a JSON represenation of a minimal
inferred API.
"""
from __future__ import annotations
import functools
import os
import typing
import warnings

from . import jsonl
from .apis import *
from .type_analysis import *

INPUT = os.environ["PYTHON_RECORD_API_INPUT"]
OUTPUT = os.environ["PYTHON_RECORD_API_OUTPUT"]
LABEL = os.environ["PYTHON_RECORD_API_LABEL"]
# Must pass in modules to constrain to, because when we see `__add__`
# we trace on both inputs, which could lead to adding traces on modules
# we don't care about
MODULES = os.environ["PYTHON_RECORD_API_MODULES"].split(",")


def __main__():
    api = API()
    with jsonl.read(INPUT) as f:
        for row in f:
            new_api = parse_line(**row)
            if new_api:
                # Enable for debugging
                # new_api.validate_again()
                try:
                    api |= new_api
                except Exception:
                    raise ValueError(
                        f"Could not process line:\n\n  line={row!r}\n\n  new_api={new_api!r}"
                    )
                api.validate_again()
    res = api.json()
    with open(OUTPUT, "w") as o:
        o.write(res)


def parse_line(
    n: int, function: object, params=None, bound_params=None,
) -> typing.Optional[API]:
    if bound_params is not None:
        signature = Signature.from_bound_params(**bound_params)
    else:
        signature = Signature.from_params(**params)
    signature.metadata[f"usage.{LABEL}"] = n
    return process_function(create_type(function), s=signature)


@functools.singledispatch
def process_function(f: OutputType, s: Signature) -> typing.Optional[API]:
    warnings.warn(f"Ignoring function {f}")
    return None


@process_function.register
def _type(f: TypeOutput, s: Signature) -> typing.Optional[API]:
    assert f.name
    module = f.name.module
    name = f.name.name
    if module is None:
        warnings.warn(f"Ignoring call to builtin type {name}")
        return None
    return API(modules={module: Module(classes={name: Class(constructor=s)})})


@process_function.register
def _method_descriptor(f: MethodDescriptorOutput, s: Signature) -> typing.Optional[API]:
    """
    Method where type is first arg of signature...
    """
    if "_0" not in s.pos_only_required:
        # TODO: Might have to support other initial self arg if there is a method_descriptor with a signature set!
        warnings.warn(
            f"Cannot deal with method descriptor with signature that doesn't have _0 pos only required\n{f!r}\n{s!r}"
        )
        return None
    self_arg = s.pos_only_required["_0"]
    # Move all other integer keys down one
    s.pos_only_required = {
        (f"_{(int(k[1:]) - 1)}" if k.startswith("_") else k): v
        for k, v in s.pos_only_required.items()
        if k != "_0"
    }
    if isinstance(self_arg, OtherOutput):
        tp = self_arg.type
        if not tp.module:
            warnings.warn(
                f"Cannot deal with method descriptor with no module\n{f!r}\n{s!r}"
            )
            return None
        return API(
            modules={tp.module: Module(classes={tp.name: Class(methods={f.name: s})})}
        )
    if isinstance(self_arg, NumpyUfuncOutput):
        return API(
            modules={"numpy": Module(classes={"ufunc": Class(methods={f.name: s})})}
        )
    warnings.warn(
        f"Cannot deal with method descriptor with non other output self arg\n{f!r}\n{s!r}\n{self_arg!r}"
    )
    return None


@process_function.register
def _ufunc(f: NumpyUfuncOutput, s: Signature) -> typing.Optional[API]:
    """
    Calling ufuncs should translate to __call__ of ufunc class + attribute with type ufunc for name
    """
    # Otherwise assume this is a normal function
    return API(
        modules={
            "numpy": Module(
                properties={f.name: (s.metadata, f)},
                classes={"ufunc": Class(methods={"__call__": s})},
            )
        }
    )


@process_function.register
def _function(f: FunctionOutput, s: Signature) -> typing.Optional[API]:
    if not f.name:
        warnings.warn(f"cannot deal with function with no name {f} {s}")
        return None
    module = f.name.module
    name = f.name.name
    # See if we special case the function
    try:
        callback = FUNCTIONS[module, name]
    except KeyError:
        pass
    else:
        return callback(s.metadata, *s.initial_args)
    # Otherwise skip if we have a builtin in operator we don't handle yet
    if module is None:
        warnings.warn(f"could not handle builtin {name}")
        return None
    if module == "_operator":
        warnings.warn(f"ignoring operator {name}")
        return None
    # Otherwise assume this is a normal function
    return API(modules={module: Module(functions={name: s})})


@process_function.register
def _method_no_self(f: MethodWithoutSelfOutput, s: Signature) -> typing.Optional[API]:
    # assume that the signature has a default bound param of self, like MaskedArray.mean
    module = f.class_.module
    cls_name = f.class_.name
    assert module
    del s.pos_or_kw_required[next(iter(s.pos_or_kw_required.keys()))]
    return API(modules={module: Module(classes={cls_name: Class(methods={f.name: s})})})


def _iter(metadata: Metadata, instance: OutputType) -> typing.Optional[API]:
    if not isinstance(instance, OtherOutput) or not instance.type.module:
        warnings.warn(f"iter with {instance}")
        return None
    return API(
        modules={
            instance.type.module: Module(
                classes={
                    instance.type.name: Class(
                        methods={"__iter__": Signature(metadata=metadata)}
                    )
                }
            )
        }
    )


def _setattr(
    metadata: Metadata,
    instance: OutputType,
    attr_type: OutputType,
    value_type: OutputType,
) -> typing.Optional[API]:
    if (
        not isinstance(attr_type, StringOutput)
        or not attr_type.options
        or not len(attr_type.options) == 1
    ):
        warnings.warn(f"{attr_type}")
        return None

    attr = next(iter(attr_type.options))
    properties = {attr: (metadata, value_type)}
    if isinstance(instance, OtherOutput):
        # getting an attribute on a instance
        return API(
            modules={
                instance.type.module: Module(
                    classes={instance.type.name: Class(properties=properties)}
                )
            }
        )
    if isinstance(instance, ModuleOutput):
        if attr == "__warningregistry__":
            # Skip this check on modules
            # https://docs.python.org/3/library/warnings.html#warnings.warn_explicit
            return None
        assert instance.name
        return API(modules={instance.name: Module(properties=properties)})
    if isinstance(instance, TypeOutput):
        assert instance.name
        assert instance.name.module
        return API(
            modules={
                instance.name.module: Module(
                    classes={instance.name.name: Class(classproperties=properties)}
                )
            }
        )
    warnings.warn(f"Ignoring setattr of {attr} on {instance}")
    return None


def _getitem(
    metadata: Metadata, inst: OutputType, idx: OutputType
) -> typing.Optional[API]:
    return record_method(inst, "__getitem__", sig(metadata, idx))


def _contains(
    metadata: Metadata, container: OutputType, item: OutputType
) -> typing.Optional[API]:
    return record_method(container, "__contains__", sig(metadata, item))


def _setitem(
    metadata: Metadata, inst: OutputType, idx: OutputType, value: OutputType
) -> typing.Optional[API]:
    return record_method(inst, "__setitem__", sig(metadata, idx, value))


def _unary_op(
    method_name: str, metadata: Metadata, inst: OutputType
) -> typing.Optional[API]:
    return record_method(inst, f"__{method_name}__", sig(metadata))


def should_output(o: OutputType) -> bool:
    module = o.module
    if module is None:
        return False
    return any(module == mod or module.startswith(f"{mod}.") for mod in MODULES)


def _binary_op(
    method_name: str, metadata: Metadata, inst: OutputType, arg: OutputType
) -> typing.Optional[API]:

    l = (
        record_method(inst, f"__{method_name}__", sig(metadata, arg))
        if should_output(inst)
        else None
    )
    r = (
        record_method(arg, f"__r{method_name}__", sig(metadata, inst))
        if should_output(arg)
        else None
    )
    if l and r:
        l |= r
    return l or r


def _comparator(
    left_method_name: str,
    right_method_name: str,
    metadata: Metadata,
    inst: OutputType,
    arg: OutputType,
) -> typing.Optional[API]:

    l = (
        record_method(inst, f"__{left_method_name}__", sig(metadata, arg))
        if should_output(inst)
        else None
    )
    r = (
        record_method(arg, f"__{right_method_name}__", sig(metadata, inst))
        if should_output(arg)
        else None
    )
    if l and r:
        l |= r
    return l or r


def _binary_inplace_op(
    method_name: str, metadata: Metadata, inst: OutputType, arg: OutputType
) -> typing.Optional[API]:
    # If we can trace the inst, do this
    if should_output(inst):
        return record_method(inst, f"__i{method_name}__", sig(metadata, arg))
    # otherwise, try recording reversed one for right arg
    if should_output(arg):
        return record_method(arg, f"__r{method_name}__", sig(metadata, inst))
    return None


def sig(metadata: Metadata, *args: OutputType) -> Signature:
    return Signature(
        metadata=metadata, pos_only_required={f"_{i}": v for i, v in enumerate(args)}
    )


FunctionCallback = typing.Union[
    typing.Callable[[Metadata], typing.Optional[API]],
    typing.Callable[[Metadata, OutputType], typing.Optional[API]],
    typing.Callable[[Metadata, OutputType, OutputType], typing.Optional[API]],
    typing.Callable[
        [Metadata, OutputType, OutputType, OutputType], typing.Optional[API]
    ],
]


FUNCTIONS: typing.Dict[typing.Tuple[typing.Optional[str], str], FunctionCallback] = {
    (None, "iter"): _iter,
    (None, "setattr"): _setattr,
    (None, "getattr"): functools.partial(_setattr, value_type=BottomOutput()),
    (None, "delattr"): functools.partial(_setattr, value_type=BottomOutput()),
    ("_operator", "getitem"): _getitem,
    ("_operator", "setitem"): _setitem,
    ("_operator", "contains"): _contains,
    # Unary
    ("_operator", "pos"): functools.partial(_unary_op, "pos"),
    ("_operator", "neg"): functools.partial(_unary_op, "neg"),
    ("_operator", "invert"): functools.partial(_unary_op, "invert"),
    ("_operator", "not_"): functools.partial(_unary_op, "bool"),
    # Binary
    ("_operator", "pow"): functools.partial(_binary_op, "pow"),
    ("_operator", "mul"): functools.partial(_binary_op, "mul"),
    ("_operator", "matmul"): functools.partial(_binary_op, "matmul"),
    ("_operator", "floordiv"): functools.partial(_binary_op, "floordiv"),
    ("_operator", "truediv"): functools.partial(_binary_op, "truediv"),
    ("_operator", "mod"): functools.partial(_binary_op, "mod"),
    ("_operator", "add"): functools.partial(_binary_op, "add"),
    ("_operator", "sub"): functools.partial(_binary_op, "sub"),
    ("_operator", "lshift"): functools.partial(_binary_op, "lshift"),
    ("_operator", "rshift"): functools.partial(_binary_op, "rshift"),
    ("_operator", "and_"): functools.partial(_binary_op, "and"),
    ("_operator", "xor"): functools.partial(_binary_op, "xor"),
    ("_operator", "or_"): functools.partial(_binary_op, "or"),
    # binary inplace
    ("_operator", "ipow"): functools.partial(_binary_inplace_op, "pow"),
    ("_operator", "imul"): functools.partial(_binary_inplace_op, "mul"),
    ("_operator", "imatmul"): functools.partial(_binary_inplace_op, "matmul"),
    ("_operator", "ifloordiv"): functools.partial(_binary_inplace_op, "floordiv"),
    ("_operator", "itruediv"): functools.partial(_binary_inplace_op, "truediv"),
    ("_operator", "imod"): functools.partial(_binary_inplace_op, "mod"),
    ("_operator", "iadd"): functools.partial(_binary_inplace_op, "add"),
    ("_operator", "isub"): functools.partial(_binary_inplace_op, "sub"),
    ("_operator", "ilshift"): functools.partial(_binary_inplace_op, "lshift"),
    ("_operator", "irshift"): functools.partial(_binary_inplace_op, "rshift"),
    ("_operator", "iand"): functools.partial(_binary_inplace_op, "and"),
    ("_operator", "ixor"): functools.partial(_binary_inplace_op, "xor"),
    ("_operator", "ior"): functools.partial(_binary_inplace_op, "or"),
    # Comparator
    ("_operator", "lt"): functools.partial(_comparator, "lt", "gt"),
    ("_operator", "le"): functools.partial(_comparator, "le", "ge"),
    ("_operator", "gt"): functools.partial(_comparator, "gt", "lt"),
    ("_operator", "ge"): functools.partial(_comparator, "ge", "le"),
    ("_operator", "eq"): functools.partial(_comparator, "eq", "eq"),
    ("_operator", "ne"): functools.partial(_comparator, "ne", "ne"),
}


@process_function.register
def _method(f: MethodOutput, s: Signature) -> typing.Optional[API]:
    name = f.name
    self_ = f.self

    if isinstance(self_, TypeOutput) and self_.name is not None:
        module = self_.name.module
        cls_name = self_.name.name
        if module is None:
            warnings.warn(f"Ignoring classmethod {name} on builtin type {cls_name}")
            return None
        return API(
            modules={module: Module(classes={cls_name: Class(classmethods={name: s})})}
        )
    return record_method(self_, name, s)


def record_method(inst: OutputType, name: str, s: Signature) -> typing.Optional[API]:
    if isinstance(inst, OtherOutput):
        module = inst.type.module
        cls_name = inst.type.name
        if module is None:
            warnings.warn(f"Ignoring method {name} on builtin type {cls_name}")
            return None
        return API(
            modules={module: Module(classes={cls_name: Class(methods={name: s})})}
        )
    if isinstance(inst, TypeOutput):
        if name in ("__eq__" or "__ne__"):
            # Assume checking for equality on types just uses builtin
            return None
        if inst.name is None:
            warnings.warn(f"Ignoring method {name} on Any type")
            return None
        module = inst.name.module
        cls_name = inst.name.name
        if module is None:
            warnings.warn(f"Ignoring method {name} on {cls_name} builtin type")
            return None
        return API(
            modules={module: Module(classes={cls_name: Class(classmethods={name: s})})}
        )
    warnings.warn(f"Ignoring method {name} on {inst}")
    return None


@process_function.register
def _classmethod(f: ClassMethodOutput, s: Signature) -> typing.Optional[API]:
    name = f.name
    module = f.class_.module
    cls_name = f.class_.name
    if module is None:
        warnings.warn(f"Ignoring classmethod {name} on builtin type {cls_name}")
        return None
    return API(
        modules={module: Module(classes={cls_name: Class(classmethods={name: s})})}
    )


if __name__ == "__main__":
    __main__()
