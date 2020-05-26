"""
Functions and tools to unify types
"""
from __future__ import annotations

import typing
import collections
import dataclasses

__all__ = ["from_params", "create_type", "Type", "unify"]


def from_params(
    params: typing.Dict[str, object]
) -> typing.Tuple[typing.List[Type], typing.Dict[str, Type]]:
    args: typing.Dict[int, Type] = {}
    kwargs: typing.Dict[str, Type] = {}
    for key, value in params.items():
        try:
            idx = int(key)
        except ValueError:
            kwargs[key] = create_type(value)
        else:
            args[idx] = create_type(value)
    return list(args[i] for i in range(len(args))), kwargs


def create_type(v: object) -> Type:
    """
    Create a structured type from the output
    """
    if isinstance(v, dict):
        tp = v["t"]
        if tp == "tuple" and v["v"]:
            return Generic("tuple", tuple(map(create_type, v["v"])))
        if tp == "builtins.module":
            return Module(v["v"])
        if tp == "builtins.type":
            return Generic("Type", (v["v"],))
        if tp == "builtins.slice":
            return Generic("slice", tuple(map(create_type, v["v"])))
        return tp
    if isinstance(v, list) and v:
        return Generic("list", (unify(map(create_type, v)),))
    if isinstance(v, str):
        return LiteralString(v)
    return type(v).__name__


# If thera are more than this amount in a union, just use any
MAX_UNION_ITEMS = 5


def unify(types: typing.Iterable[Type]) -> Type:
    types = set(types)
    if len(types) == 1:
        return types.pop()
    if not types:
        return "object"
    # mapping of generic type name and n args to args
    generic_types: typing.Dict[
        typing.Tuple[str, int], typing.Set[typing.Tuple[Type, ...]]
    ] = collections.defaultdict(set)
    regular_types: typing.List[Type] = []
    while types:
        t = types.pop()
        if isinstance(t, Generic):
            generic_types[(t.name, len(t.args))].add(t.args)
        elif isinstance(t, Union):
            types.update(t.args)
        elif t is None:
            # Don't add never type
            pass
        else:
            regular_types.append(t)

    # Unify each generic type and add to regular_types
    for keys, args in generic_types.items():
        regular_types.append(Generic(keys[0], tuple(map(unify, zip(*args)))))

    # If we have all Bottom types emit the bottom
    if not regular_types:
        return None
    if len(regular_types) == 1:
        return regular_types[0]

    # If we have an any in the regular types, just emit that
    if "object" in regular_types:
        return "object"

    # If we have a `str` type, remove all string literals
    if "str" in regular_types:
        regular_types = list(
            filter(lambda t: not isinstance(t, LiteralString), regular_types)
        )
    if len(regular_types) > MAX_UNION_ITEMS:
        return "object"
    return Union(tuple(regular_types))


# "object" is top and None is bottom
# None is used to represent type params that don't exist. We dont need it but adding
# it makes unfication of variadic args easier since they always have a type, sometimes
# it's just None
Type = typing.Union[str, None, "Generic", "Union", "LiteralString", "Module"]


@dataclasses.dataclass(frozen=True)
class Module:
    name: str

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return str(self)


@dataclasses.dataclass(frozen=True)
class LiteralString:
    value: str

    def __str__(self):
        return repr(self.value)

    def __repr__(self):
        return str(self)


@dataclasses.dataclass(frozen=True)
class Generic:
    name: str
    args: typing.Tuple[Type, ...]

    def __str__(self):
        return f"{self.name}[{', '.join(map(str, self.args))}]"

    def __repr__(self):
        return str(self)


@dataclasses.dataclass(frozen=True)
class Union:
    args: typing.Tuple[Type, ...]

    def __str__(self):
        return f"Union[{', '.join(sorted(map(str, self.args)))}]"

    def __repr__(self):
        return str(self)
