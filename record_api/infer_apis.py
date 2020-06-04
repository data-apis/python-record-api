"""
This analysis is meant to run on the raw data and produce a JSON represenation of a minimal
inferred API.
"""
from __future__ import annotations

import collections
import operator
import os
import typing
import warnings
import itertools
import dataclasses
import warnings
import functools

import tqdm.std
import orjson
from typing_extensions import TypedDict

from . import jsonl
from .type_analysis import *
from .apis import *


INPUT = os.environ["PYTHON_RECORD_API_INPUT"]
OUTPUT = os.environ["PYTHON_RECORD_API_OUTPUT"]
LABEL = os.environ["PYTHON_RECORD_API_LABEL"]


def __main__():
    api = API()
    with jsonl.read(INPUT) as f:
        for row in f:
            new_api = parse_line(**row)
            if new_api:
                api |= new_api
    res = api.json()
    with open(OUTPUT, "w") as o:
        o.write(res)


def parse_line(
    n: int, function: object, params=None, bound_params=None,
) -> typing.Optional[API]:
    if bound_params:
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
def _function(f: FunctionOutput, s: Signature) -> typing.Optional[API]:
    assert f.name
    module = f.name.module
    name = f.name.name
    try:
        callback = FUNCTIONS[module, name]
    except KeyError:
        if module is None:
            warnings.warn(f"could not handle builtin {name}")
    else:
        return callback(*s.initial_args)
    return API(modules={module: Module(functions={name: s})})


def _iter(instance: OutputType) -> typing.Optional[API]:
    if not isinstance(instance, OtherOutput) or not instance.type.module:
        warnings.warn(f"iter with {instance}")
        return None
    return API(
        modules={
            instance.type.module: Module(
                classes={instance.type.name: Class(methods={"__iter__": Signature()})}
            )
        }
    )


def _setattr(
    instance: OutputType, attr_type: OutputType, value_type: OutputType
) -> typing.Optional[API]:
    if (
        not isinstance(attr_type, StringOutput)
        or not attr_type.options
        or not len(attr_type.options) == 1
    ):
        warnings.warn(f"{attr_type}")
        return None

    attr = next(iter(attr_type.options))
    if isinstance(instance, OtherOutput):
        # getting an attribute on a instance
        return API(
            modules={
                instance.type.module: Module(
                    classes={instance.type.name: Class(properties={attr: value_type})}
                )
            }
        )
    if isinstance(instance, ModuleOutput):
        assert instance.name
        return API(modules={instance.name: Module(properties={attr: value_type})})
    if isinstance(instance, TypeOutput):
        assert instance.name
        assert instance.name.module
        return API(
            modules={
                instance.name.module: Module(
                    classes={
                        instance.name.name: Class(classproperties={attr: value_type})
                    }
                )
            }
        )
    warnings.warn(f"Ignoring setattr on {instance}")
    return None


FunctionCallback = typing.Union[
    typing.Callable[[], typing.Optional[API]],
    typing.Callable[[OutputType], typing.Optional[API]],
    typing.Callable[[OutputType, OutputType], typing.Optional[API]],
    typing.Callable[[OutputType, OutputType, OutputType], typing.Optional[API]],
]


FUNCTIONS: typing.Dict[typing.Tuple[typing.Optional[str], str], FunctionCallback] = {
    (None, "iter"): _iter,
    (None, "setattr"): _setattr,
    (None, "getattr"): functools.partial(_setattr, value_type=BottomOutput()),
    (None, "delattr"): functools.partial(_setattr, value_type=BottomOutput()),
}


@process_function.register
def _method(f: MethodOutput, s: Signature) -> typing.Optional[API]:
    name = f.name
    self_ = f.self
    if isinstance(self_, OtherOutput):
        module = self_.type.module
        cls_name = self_.type.name
        if module is None:
            warnings.warn(f"Ignoring method {name} on builtin type {cls_name}")
            return None
        return API(
            modules={module: Module(classes={cls_name: Class(methods={name: s})})}
        )
    if isinstance(self_, TypeOutput) and self_.name is not None:
        module = self_.name.module
        cls_name = self_.name.name
        if module is None:
            warnings.warn(f"Ignoring classmethod {name} on builtin type {cls_name}")
            return None
        return API(
            modules={module: Module(classes={cls_name: Class(classmethods={name: s})})}
        )
    warnings.warn(f"Ignoring method {name} on {self_}")
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
