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
import pydantic
import warnings
import ast
import networkx

import tqdm.std
import orjson
from typing_extensions import TypedDict

from . import jsonl
from .type_analysis import *

__all__ = ["API", "Module", "Class", "Signature"]
Type = OutputType


def orjson_dumps(v, *, default):
    # orjson.dumps returns bytes, to match standard json.dumps we need to decode
    return orjson.dumps(v, default=default, option=orjson.OPT_INDENT_2).decode()  # type: ignore


class API(pydantic.BaseModel):
    # Dotted module name to module
    modules: typing.Dict[str, Module] = pydantic.Field(default_factory=dict)

    class Config:
        json_loads = orjson.loads
        json_dumps = orjson_dumps

    def __ior__(self, other: API) -> API:
        update(self.modules, other.modules, operator.ior)
        return self


class Module(pydantic.BaseModel):
    functions: typing.Dict[str, Signature] = pydantic.Field(default_factory=dict)
    classes: typing.Dict[str, Class] = pydantic.Field(default_factory=dict)
    properties: typing.Dict[str, Type] = pydantic.Field(default_factory=dict)

    def __ior__(self, other: Module) -> Module:
        update(self.classes, other.classes, operator.ior)
        update(self.functions, other.functions, operator.ior)

        # properties are union of properties, minus any things that are already classes/functins
        update(self.properties, other.properties, lambda l, r: unify((l, r)))
        remove_keys(self.properties, self.classes.keys())
        remove_keys(self.properties, self.functions.keys())
        return self


class Class(pydantic.BaseModel):
    constructor: typing.Union[Signature, None] = None
    methods: typing.Dict[str, Signature] = pydantic.Field(default_factory=dict)
    classmethods: typing.Dict[str, Signature] = pydantic.Field(default_factory=dict)
    properties: typing.Dict[str, Type] = pydantic.Field(default_factory=dict)
    classproperties: typing.Dict[str, Type] = pydantic.Field(default_factory=dict)

    def __ior__(self, other: Class) -> Class:
        if self.constructor and other.constructor:
            self.constructor |= other.constructor
        else:
            self.constructor = other.constructor
        update(self.methods, other.methods, operator.ior)
        update(self.classmethods, other.classmethods, operator.ior)

        update(self.classproperties, other.classproperties, lambda l, r: unify((l, r)))
        remove_keys(self.classproperties, self.methods.keys())
        remove_keys(self.classproperties, self.classmethods.keys())

        update(self.properties, other.properties, lambda l, r: unify((l, r)))
        remove_keys(self.properties, self.methods.keys())
        remove_keys(self.properties, self.classmethods.keys())
        # Anything that is both a class property and a property should be only a class property
        remove_keys(self.properties, self.classproperties.keys())

        return self


class Signature(pydantic.BaseModel):
    # See for a helpful spec https://www.python.org/dev/peps/pep-0570/#syntax-and-semantics
    # Also keyword only PEP https://www.python.org/dev/peps/pep-3102/

    pos_only_required: typing.Dict[str, Type] = pydantic.Field(default_factory=dict)
    pos_only_optional: typing.Dict[str, Type] = pydantic.Field(default_factory=dict)

    # If there are any pos_only_optional, then there cannot be any required pos_or_kw
    pos_or_kw_required: typing.Dict[str, Type] = pydantic.Field(default_factory=dict)
    pos_or_kw_optional: typing.Dict[str, Type] = pydantic.Field(default_factory=dict)

    # Variable args are allowed if it this is not none
    var_pos: typing.Optional[typing.Tuple[str, Type]] = None

    kw_only_required: typing.Dict[str, Type] = pydantic.Field(default_factory=dict)
    kw_only_optional: typing.Dict[str, Type] = pydantic.Field(default_factory=dict)

    # Variable kwargs are allowed if this is not none
    var_kw: typing.Optional[typing.Tuple[str, Type]] = None

    metadata: typing.Dict[str, int] = pydantic.Field(default_factory=dict)

    @property
    def ast(self) -> ast.arguments:
        return ast.arguments(
            posonlyargs=[
                ast.arg(k, v.annotation)
                for k, v in itertools.chain(
                    self.pos_only_required.items(), self.pos_only_optional.items()
                )
            ],
            args=[
                ast.arg(k, v.annotation)
                for k, v in itertools.chain(
                    self.pos_or_kw_required.items(), self.pos_or_kw_optional.items()
                )
            ],
            defaults=[
                ast.Constant(..., None)
                for _ in range(
                    len(self.pos_only_optional) + len(self.pos_or_kw_optional)
                )
            ],
            vararg=(
                ast.arg(self.var_pos[0], self.var_pos[1].annotation)
                if self.var_pos
                else None
            ),
            kwarg=(
                ast.arg(self.var_kw[0], self.var_kw[1].annotation)
                if self.var_kw
                else None
            ),
            kwonlyargs=[
                ast.arg(k, v.annotation)
                for k, v in itertools.chain(
                    self.kw_only_required.items(), self.kw_only_optional.items()
                )
            ],
            kw_defaults=(
                [ast.Constant(None, None) for _ in range(len(self.kw_only_required))]
                + [ast.Constant(..., None) for _ in range(len(self.kw_only_optional))]
            ),
        )

    @property
    def initial_args(self) -> typing.Iterator[Type]:
        """
        Iterates through default args
        """
        yield from self.pos_only_required.values()
        yield from self.pos_or_kw_required.values()
        yield from self.kw_only_required.values()

    @classmethod
    def from_params(
        cls, args: typing.List[object] = [], kwargs: typing.Dict[str, object] = {}
    ) -> Signature:
        # If we don't know what the args/kwargs are, assume the args are positional only
        # and the kwargs and keyword only
        return cls(
            pos_only_required={f"_{i}": create_type(v) for i, v in enumerate(args)},
            kw_only_required={k: create_type(v) for k, v in kwargs.items()},
        )

    @classmethod
    def from_bound_params(
        cls,
        pos_only: typing.List[typing.Tuple[str, object]] = [],
        pos_or_kw: typing.List[typing.Tuple[str, object]] = [],
        var_pos: typing.Optional[typing.Tuple[str, typing.List[object]]] = None,
        kw_only: typing.Dict[str, object] = {},
        var_kw: typing.Optional[typing.Tuple[str, typing.Dict[str, object]]] = None,
    ) -> Signature:
        return cls(
            pos_only_required={k: create_type(v) for k, v in pos_only},
            pos_or_kw_required={k: create_type(v) for k, v in pos_or_kw},
            var_pos=(
                (var_pos[0], unify(map(create_type, var_pos[1]))) if var_pos else None
            ),
            kw_only_required={k: create_type(v) for k, v in kw_only.items()},
            var_kw=(
                (var_kw[0], unify(map(create_type, var_kw[1].values())))
                if var_kw
                else None
            ),
        )

    def __ior__(self, other: Signature) -> Signature:

        self._copy_pos_only(other)
        self._copy_pos_or_kw(other)
        self._copy_var_pos(other)
        self._copy_kw_only(other)
        self._copy_var_kw(other)
        # Merge metata, throwing away duplicate keys
        update(self.metadata, other.metadata, lambda l, r: l + r)
        return self

    def _copy_pos_only(self, other: Signature) -> None:
        pos_only_required = dict(
            map(
                unify_named_types,
                zip(self.pos_only_required.items(), other.pos_only_required.items()),
            )
        )
        n_pos_only_required = len(pos_only_required)

        # any leftover, are optional positional only args
        # These should be combined with the existing optional position only
        self.pos_only_optional = interleave_dicts(
            slice_dict(self.pos_only_required, n_pos_only_required),
            slice_dict(other.pos_only_required, n_pos_only_required),
            self.pos_only_optional,
            other.pos_only_optional,
        )
        self.pos_only_required = pos_only_required

    def _copy_pos_or_kw(self, other: Signature) -> None:
        # First take off new optional keys from self and other, making sure to keep order
        self_pos_or_kw_required_keys = list(self.pos_or_kw_required.keys())
        other_pos_or_kw_required_keys = list(other.pos_or_kw_required.keys())
        pos_or_kw_required_keys = set(self_pos_or_kw_required_keys) & set(
            other_pos_or_kw_required_keys
        )
        self_new_optional = {
            k: self.pos_or_kw_required.pop(k)
            for k in self_pos_or_kw_required_keys
            if k not in pos_or_kw_required_keys
        }
        other_new_optional = {
            k: other.pos_or_kw_required.pop(k)
            for k in other_pos_or_kw_required_keys
            if k not in pos_or_kw_required_keys
        }
        # Now we can merge the required keys
        update(
            self.pos_or_kw_required,
            other.pos_or_kw_required,
            lambda l, r: unify((l, r)),
        )

        self.pos_or_kw_optional = interleave_dicts(
            self_new_optional,
            other_new_optional,
            self.pos_or_kw_optional,
            other.pos_or_kw_optional,
        )

    def _copy_var_pos(self, other: Signature) -> None:
        self.var_pos = (
            unify_named_types((self.var_pos, other.var_pos,))
            if self.var_pos and other.var_pos
            else (self.var_pos or other.var_pos)
        )

    def _copy_kw_only(self, other: Signature) -> None:
        # Move over all required keys that aren't present in both to optional
        self_kw_only_required_keys = set(self.kw_only_required.keys())
        other_kw_only_required_keys = set(other.kw_only_required.keys())
        kw_only_required_keys = self_kw_only_required_keys & other_kw_only_required_keys
        move(
            self.kw_only_optional,
            self.kw_only_required,
            self_kw_only_required_keys - kw_only_required_keys,
            lambda l, r: unify((l, r)),
        )
        move(
            self.kw_only_optional,
            other.kw_only_required,
            other_kw_only_required_keys - kw_only_required_keys,
            lambda l, r: unify((l, r)),
        )
        # merge required and optional
        update(
            self.kw_only_required, other.kw_only_required, lambda l, r: unify((l, r)),
        )
        update(
            self.kw_only_optional, other.kw_only_optional, lambda l, r: unify((l, r)),
        )

    def _copy_var_kw(self, other: Signature) -> None:
        self.var_kw = (
            unify_named_types((self.var_kw, other.var_kw,))
            if self.var_kw and other.var_kw
            else (self.var_kw or other.var_kw)
        )


API.update_forward_refs()
Class.update_forward_refs()
Module.update_forward_refs()


def interleave_dicts(*ds: typing.Dict[str, Type]) -> typing.Dict[str, Type]:
    # Now we just need to merge all the items, making sure that if any two items
    # had an ordering in an existing optional that ordering is preserved.

    # We do this by creating a graph of all the nodes, with a `types` atribute for a set of the types
    # We should have an edge pointing from all earlier params to later ones, so then we can
    # topologically sort it to get proper ordering
    g = networkx.DiGraph()
    for d in ds:
        prev_key = None
        for key, tp in d.items():
            if key in g:
                g.nodes[key]["types"].add(tp)
            else:
                g.add_node(key, types={tp})
            if prev_key is not None:
                g.add_edge(prev_key, key)
            prev_key = key
    return {k: unify(g.nodes[k]["types"]) for k in networkx.topological_sort(g)}


def unify_named_types(
    name_and_types: typing.Iterable[typing.Tuple[typing.Optional[str], Type]]
) -> typing.Tuple[str, Type]:
    """
    Verifies the names are the same and unifies the types. Returns None if no args passed in
    or all are none
    """
    names, tps = zip(*filter(lambda x: x is not None, name_and_types))  # type: ignore
    unique_names = set(filter(lambda x: x is not None, names))
    assert len(unique_names) == 1
    return unique_names.pop(), unify(tps)


K = typing.TypeVar("K")
V = typing.TypeVar("V")


class DontAdd:
    pass


DONT_ADD = DontAdd()


def slice_dict(d: typing.Dict[K, V], n: int) -> typing.Dict[K, V]:
    """
    Slices n off the front of the dict
    """
    return dict(kv for i, kv in enumerate(d.items()) if i < n)


def remove_keys(d: typing.Dict[K, V], ks: typing.Iterable[K]) -> None:
    for k in ks:
        if k in d:
            del d[k]


def move(
    l: typing.Dict[K, V],
    r: typing.Dict[K, V],
    keys: typing.Iterable[K],
    f: typing.Callable[[V, V], V],
) -> None:
    """
    Moves keys from right to left
    """
    for k in keys:
        v = r.pop(k)
        if k in l:
            v = f(l[k], v)
        l[k] = v


def update(
    l: typing.Dict[K, V],
    r: typing.Dict[K, V],
    f: typing.Callable[[V, V], typing.Union[DontAdd, V]],
) -> None:
    """
    Updates the left dict with the right dict.

    On conflicting keys calls function with left and right values to return result.
    """
    for k, v in r.items():
        if k in l:
            res = f(l[k], v)
            if isinstance(res, DontAdd):
                del l[k]
            else:
                l[k] = res
        else:
            l[k] = v
