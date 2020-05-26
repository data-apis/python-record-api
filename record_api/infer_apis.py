"""
This analysis is meant to run on the raw data and produce a JSON represenation of a minimal
inferred API.
"""
from __future__ import annotations

from typing_extensions import TypedDict
import os
import collections
import warnings
import operator

from dataclasses import dataclass, field, asdict, asdict
import typing
import tqdm.std
import json
from .type_analysis import *

INPUT = os.environ["PYTHON_RECORD_API_INPUT"]
OUTPUT = os.environ["PYTHON_RECORD_API_OUTPUT"]


def __main__():
    print(f"Infering API: {INPUT}")
    api = API()
    with open(INPUT, "r", encoding="utf-8") as f:
        for line in tqdm.std.tqdm(f, "reading"):
            row = json.loads(line)
            api |= read_line(row)
    with open(OUTPUT, "w",) as f:
        json.dump(asdict(api), f)


Line = TypedDict(
    "Line", {"location": str, "function": str, "params": typing.Dict[str, object]}
)


def read_line(line: Line) -> API:
    fn = line["function"]
    # Skip operators and builtins for now
    if fn.startswith("_operator") or fn.startswith("builtins"):
        return API()
    args, kwargs = from_params(line["params"])

    *modules, function_name = fn.split(".")
    module_name = ".".join(modules)

    return API(
        modules={
            module_name: Module(
                functions={
                    function_name: Signature(
                        required_unnamed=args, required_named=kwargs
                    )
                }
            )
        }
    )


@dataclass
class API:
    # Dotted module name to module
    modules: typing.Dict[str, Module] = field(default_factory=dict)

    def __ior__(self, other: API) -> API:
        update(self.modules, other.modules, self.merge_modules)
        return self

    def merge_modules(
        self, module_name: str, l: Module, r: Module
    ) -> typing.Union[Module, DontAdd]:
        # If the incoming module r has any classes in that are currently modules of our current API
        # Change those modules to be classes
        for class_name, class_ in r.classes.items():
            old_module_name = f"{module_name}.{class_name}"
            if old_module_name in self.modules:
                class_.move_module(self.modules.pop(old_module_name))

        # If the incoming module has any functions that are module here, assume they are class constructors
        for function_name, sig in r.functions.items():
            old_module_name = f"{module_name}.{function_name}"
            if old_module_name in self.modules:
                # TODO: ...
                r.classes

        l |= r

        # If the module name is already a class, make the module functions methods on that class
        *modules, class_name = module_name.split(".")
        new_module_name = ".".join(modules)
        if (
            new_module_name in self.modules
            and class_name in self.modules[new_module_name].classes
        ):
            self.modules[new_module_name].classes[class_name].move_module(l)
            return DONT_ADD
        return l


@dataclass
class Module:
    functions: typing.Dict[str, Signature] = field(default_factory=dict)
    classes: typing.Dict[str, Class] = field(default_factory=dict)
    # TODO: properties

    def __ior__(self, other: Module) -> Module:
        update(self.classes, other.classes, lambda k, l, r: operator.ior(l, r))
        update(self.functions, other.functions, self.merge_functions)
        return self

    def merge_functions(
        self, function_name: str, l: Signature, r: Signature
    ) -> typing.Union[Signature, DontAdd]:
        # If there is a function with the same name as the class, make it a class constructor instead
        l |= r

        if function_name in self.classes:
            self.classes[function_name] |= Class(constructor=l)
            return DONT_ADD
        return l


@dataclass
class Class:
    constructor: typing.Union[Signature, None] = None
    methods: typing.Dict[str, Signature] = field(default_factory=dict)
    # TODO: properties

    def __ior__(self, other: Class) -> Class:
        if self.constructor and other.constructor:
            self.constructor |= other.constructor
        else:
            self.constructor = other.constructor
        update(self.methods, other.methods, lambda k, l, r: operator.ior(l, r))
        return self

    def move_module(self, module: Module) -> None:
        """
        Move functions from a module to methods
        """
        # no subclasses allowed
        assert not module.classes
        self |= Class(methods=module.functions)


# @dataclass
# class Method:
#     signature: Signature
#     is_classmethod: bool = field(default=False)

#     def __ior__(self, other: Method) -> Method:
#         assert self.is_classmethod == other.is_classmethod
#         self.signature |= other.signature
#         return self


@dataclass
class Signature:
    # Unnamed positional args that are required
    required_unnamed: typing.List[Type] = field(default_factory=list)
    # Type of variadic args if allowed, if not allowed this will be None
    variadic_unnamed: Type = None
    # Named arguments that are always present
    required_named: typing.Dict[str, Type] = field(default_factory=dict)
    # Named arguments that are sometimes present
    optional_named: typing.Dict[str, Type] = field(default_factory=dict)

    def __ior__(self, other: Signature) -> Signature:
        # If we have different numbers of required_unnamed, then the extras should be added to the variadic_unnamed
        # and the same index ones should be unified
        required_unnamed = list(
            map(unify, zip(self.required_unnamed, other.required_unnamed))
        )
        n_required_unnamed = len(required_unnamed)
        variadic_unnamed: Type = unify(
            [self.variadic_unnamed, other.variadic_unnamed]
            + self.required_unnamed[n_required_unnamed:]
            + other.required_unnamed[n_required_unnamed:]
        )
        self.required_unnamed = required_unnamed
        self.variadic_unnamed = variadic_unnamed

        # Similarly, any required named that are present in one and not the other should be moved to optional named
        update(self.optional_named, other.optional_named, lambda k, l, r: unify((l, r)))

        for name, tp in other.required_named.items():
            if name in self.required_named:
                self.required_named[name] = unify((self.required_named[name], tp))
            elif name in self.optional_named:
                self.optional_named[name] = unify((self.optional_named[name], tp))
            else:
                self.optional_named[name] = tp

        # Present in self but not in other, so should be removed from self
        new_optional_names: typing.Set[str] = set(self.required_named.keys()) - set(
            other.required_named.keys()
        )
        for name in new_optional_names:
            tp = self.required_named.pop(name)
            self.optional_named[name] = unify((tp, self.optional_named[name]))
        return self


K = typing.TypeVar("K")
V = typing.TypeVar("V")


class DontAdd:
    pass


DONT_ADD = DontAdd()


def update(
    l: typing.Dict[K, V],
    r: typing.Dict[K, V],
    f: typing.Callable[[K, V, V], typing.Union[DontAdd, V]],
) -> None:
    """
    Updates the left dict with the right dict.

    On conflicting keys calls function with left and right values to return result.
    """
    for k, v in r.items():
        if k in l:
            res = f(k, l[k], v)
            if isinstance(res, DontAdd):
                del l[k]
            else:
                l[k] = res
        else:
            l[k] = v


if __name__ == "__main__":
    __main__()
