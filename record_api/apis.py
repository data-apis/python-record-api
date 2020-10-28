"""
This analysis is meant to run on the raw data and produce a JSON represenation of a minimal
inferred API.
"""
from __future__ import annotations
import functools
import operator
import typing

import libcst as cst
import networkx
import orjson
import pydantic

from .type_analysis import *

__all__ = ["API", "Module", "Class", "Signature", "Metadata"]
Type = OutputType


# If there are more than 2 optional positional only args, convert them all to variadic positional args
MAX_OPTIONAL_POSITIONAL_ONLY_ARGS = 2


def orjson_dumps(v, *, default):
    # orjson.dumps returns bytes, to match standard json.dumps we need to decode
    return orjson.dumps(v, default=default, option=orjson.OPT_INDENT_2).decode()  # type: ignore


Metadata = typing.Dict[str, int]


def bad_name(name: str) -> bool:
    return not name.isidentifier()


class BaseModel(pydantic.BaseModel):
    class Config:
        extra = "forbid"

    # Set fields set to be all those that are truthy, so only those are expoed with `skip_defaults`
    @property  # type: ignore
    def __fields_set__(self) -> typing.Set[str]:  # type: ignore
        s = set()
        for k, v in self.__values__.items():
            if v:
                s.add(k)
        return s

    @__fields_set__.setter
    def __fields_set__(self, val: typing.Set[str]) -> None:
        pass

    def __repr_args__(self) -> pydantic.ReprArgs:  # type: ignore
        # Dont show empty valyes
        for k, v in super().__repr_args__():
            if v:
                yield k, v

    def validate_again(self) -> None:
        """
        Use to manually validate for debugging when fields change
        """
        _, _, validation_error = pydantic.validate_model(type(self), self.dict())
        if validation_error:
            raise validation_error


class API(BaseModel):
    # Dotted module name to module
    modules: typing.Dict[str, Module] = pydantic.Field(default_factory=dict)

    class Config:
        json_loads = orjson.loads
        json_dumps = orjson_dumps

    def __ior__(self, other: API) -> API:
        update_ior(self.modules, other.modules)
        # Remove any properties which are other just other modules
        for module_name, module in self.modules.items():
            for property_ in list(module.properties.keys()):
                if f"{module_name}.{property_}" in self.modules:
                    del module.properties[property_]
        return self

    def json(self, **kwargs) -> str:
        return super().json(exclude_none=True, skip_defaults=True, **kwargs)


class Module(BaseModel):
    function_overloads: typing.Dict[str, typing.List[Signature]] = pydantic.Field(
        default_factory=dict
    )
    functions: typing.Dict[str, Signature] = pydantic.Field(default_factory=dict)
    classes: typing.Dict[str, Class] = pydantic.Field(default_factory=dict)
    properties: typing.Dict[str, typing.Tuple[Metadata, Type]] = pydantic.Field(
        default_factory=dict
    )

    @pydantic.root_validator
    def set_overloads(cls, values):
        """
        Set the overloads to be the values, if they are not set
        """
        values["function_overloads"] = values.get("function_overloads", {}) or {
            k: create_overloads(v) for k, v in values["functions"].items()
        }
        return values

    @property
    def source(self) -> str:
        # try:
        module = cst.Module(list(self.body))
        # except libcst.CSTValidationError:
        #     raise RuntimeError(f"Could not output source for:\n{self!r}")

        return module.code

    @property
    def body(
        self,
    ) -> typing.Iterable[
        typing.Union[cst.BaseCompoundStatement, cst.SimpleStatementLine]
    ]:
        yield cst.SimpleStatementLine(
            [cst.ImportFrom(cst.Name("typing"), names=cst.ImportStar())]
        )
        yield from assign_properties(self.properties)

        yield from function_defs(self.function_overloads, self.functions, "function")

        for name, class_ in sort_items(self.classes):
            yield class_.class_def(name)

    def __ior__(self, other: Module) -> Module:
        """
        property -> function
        function -> class constructor
        """
        # properties
        update_metadata_and_types(self.properties, other.properties)

        # functions
        update_ior(self.functions, other.functions)
        # property -> function
        merge_intersection(self.functions, self.properties, merge_property_into_method)
        # function overloads
        update_overloads(self.function_overloads, other.function_overloads)

        # classes
        update_ior(self.classes, other.classes)
        # property -> classes
        merge_intersection(
            self.classes, self.properties, lambda class_, property: class_
        )

        # function -> class constructor
        merge_intersection(self.classes, self.functions, merge_method_class)
        merge_intersection(
            self.classes, self.function_overloads, merge_method_overloads_class
        )

        return self


def create_overloads(s: Signature) -> typing.List[Signature]:
    """
    Copies signature to create overloads. Needs to copy because we inplace update the signature later on
    """
    return [s.copy(deep=True)]


class Class(BaseModel):
    constructor_overloads: typing.List[Signature] = pydantic.Field(default_factory=list)
    constructor: typing.Union[Signature, None] = None
    method_overloads: typing.Dict[str, typing.List[Signature]] = pydantic.Field(
        default_factory=dict
    )
    methods: typing.Dict[str, Signature] = pydantic.Field(default_factory=dict)
    classmethod_overloads: typing.Dict[str, typing.List[Signature]] = pydantic.Field(
        default_factory=dict
    )
    classmethods: typing.Dict[str, Signature] = pydantic.Field(default_factory=dict)
    properties: typing.Dict[str, typing.Tuple[Metadata, Type]] = pydantic.Field(
        default_factory=dict
    )
    classproperties: typing.Dict[str, typing.Tuple[Metadata, Type]] = pydantic.Field(
        default_factory=dict
    )

    @pydantic.root_validator
    def set_overloads(cls, values):
        """
        Set the overloads to be the values, if not passed in.
        """
        if values["constructor"] and not values["constructor_overloads"]:
            values["constructor_overloads"] = create_overloads(values["constructor"])
        values["method_overloads"] = values.get("method_overloads", {}) or {
            k: create_overloads(v) for k, v in values["methods"].items()
        }
        values["classmethod_overloads"] = values.get("classmethod_overloads", {}) or {
            k: create_overloads(v) for k, v in values["classmethods"].items()
        }
        return values

    def class_def(self, name: str) -> cst.ClassDef:
        return cst.ClassDef(cst.Name(name), cst.IndentedBlock(list(self.body)),)

    @property
    def body(self) -> typing.Iterable[cst.BaseStatement]:
        if self.constructor is not None:
            function_def_with_overloads(
                "__init__",
                self.constructor_overloads,
                self.constructor,
                "method",
                indent=1,
            )
        yield from assign_properties(self.classproperties, True)

        yield from function_defs(
            self.classmethod_overloads, self.classmethods, "classmethod", 1
        )
        yield from assign_properties(self.properties)

        yield from function_defs(self.method_overloads, self.methods, "method", 1)

    def ior_constructor(self, other: typing.Optional[Signature]) -> None:
        if self.constructor and other:
            self.constructor |= other
        else:
            self.constructor = other

    def __ior__(self, other: Class) -> Class:
        """
        There is a partial ordering of things here which define which get combined to which:

        * property -> classproperty
        * property -> method
        * method -> classmethod
        * classproperty -> classmethod

        * (implicit) property -> classmethod 
        """
        self.ior_constructor(other.constructor)
        merge_overloads(self.constructor_overloads, other.constructor_overloads)

        # properties
        update_metadata_and_types(self.properties, other.properties)

        # class properties
        update_metadata_and_types(self.classproperties, other.classproperties)
        # property -> classproperty
        merge_intersection(
            self.classproperties, self.properties, merge_methods_properties
        )

        # methods
        update_ior(self.methods, other.methods)
        # property -> method
        merge_intersection(self.methods, self.properties, merge_property_into_method)
        # method overloads
        update_overloads(self.method_overloads, other.method_overloads)

        # class methods
        update_ior(self.classmethods, other.classmethods)
        # method -> classmethod
        merge_intersection(self.classmethods, self.methods, operator.ior)
        # classmethod overloads
        merge_intersection(
            self.classmethod_overloads, self.method_overloads, merge_overloads
        )
        update_overloads(self.classmethod_overloads, other.classmethod_overloads)

        # classproperty -> classmethod
        merge_intersection(
            self.classmethods, self.classproperties, merge_property_into_method
        )

        return self


def assign_properties(
    p: typing.Dict[str, typing.Tuple[Metadata, Type]], is_classvar=False
) -> typing.Iterable[cst.SimpleStatementLine]:
    for name, metadata_and_tp in sort_items(p):
        if bad_name(name):
            continue
        metadata, tp = metadata_and_tp
        ann = tp.annotation
        yield cst.SimpleStatementLine(
            [
                cst.AnnAssign(
                    cst.Name(name),
                    cst.Annotation(
                        cst.Subscript(
                            cst.Name("ClassVar"), [cst.SubscriptElement(cst.Index(ann))]
                        )
                        if is_classvar
                        else ann
                    ),
                )
            ],
            leading_lines=[cst.EmptyLine()]
            + [
                cst.EmptyLine(comment=cst.Comment("# " + l))
                for l in metadata_lines(metadata)
            ],
        )


def sort_items(d: typing.Dict[str, V]) -> typing.Iterable[typing.Tuple[str, V]]:
    return sorted(d.items(), key=lambda kv: kv[0])


PartialKeyOrdering = typing.List[typing.Tuple[str, str]]


def function_defs(
    overloads: typing.Dict[str, typing.List[Signature]],
    functions: typing.Dict[str, Signature],
    type: typing.Literal["function", "classmethod", "method"],
    indent: int = 0,
) -> typing.Iterable[cst.FunctionDef]:
    """
    Exports CST for functions plus overloads
    """
    for name, sig in sort_items(functions):
        if bad_name(name):
            continue
        yield from function_def_with_overloads(
            name, overloads.get(name, []), sig, type, indent
        )


def function_def_with_overloads(
    name: str,
    overloads: typing.List[Signature],
    fn: Signature,
    type: typing.Literal["function", "classmethod", "method"],
    indent: int = 0,
) -> typing.Iterable[cst.FunctionDef]:
    # Don't print overloads if just one!
    if len(overloads) > 1:
        for overload in overloads:
            yield overload.function_def(name, type, indent=indent, overload=True)
    yield fn.function_def(name, type, indent=indent)


class Signature(BaseModel):
    # See for a helpful spec https://www.python.org/dev/peps/pep-0570/#syntax-and-semantics
    # Also keyword only PEP https://www.python.org/dev/peps/pep-3102/

    pos_only_required: typing.Dict[str, Type] = pydantic.Field(default_factory=dict)
    pos_only_optional: typing.Dict[str, Type] = pydantic.Field(default_factory=dict)
    # If there are any pos_only_optional, then there cannot be any required pos_or_kw
    pos_only_optional_ordering: PartialKeyOrdering = pydantic.Field(
        default_factory=list
    )

    pos_or_kw_required: typing.Dict[str, Type] = pydantic.Field(default_factory=dict)
    pos_or_kw_optional: typing.Dict[str, Type] = pydantic.Field(default_factory=dict)
    # Partial ordering of args, (pred, suc) pairs
    pos_or_kw_optional_ordering: PartialKeyOrdering = pydantic.Field(
        default_factory=list
    )
    # Variable args are allowed if it this is not none
    var_pos: typing.Optional[typing.Tuple[str, Type]] = None

    kw_only_required: typing.Dict[str, Type] = pydantic.Field(default_factory=dict)
    kw_only_optional: typing.Dict[str, Type] = pydantic.Field(default_factory=dict)

    # Variable kwargs are allowed if this is not none
    var_kw: typing.Optional[typing.Tuple[str, Type]] = None

    metadata: typing.Dict[str, int] = pydantic.Field(default_factory=dict)

    @pydantic.validator("pos_only_required")
    @classmethod
    def validate_pos_only_required_ordering(cls, v):
        last_i = None
        for k in v:
            if k.startswith("_"):
                i = int(k[1:])
                if last_i is not None:
                    if i <= last_i:
                        raise ValueError(repr(v))
                last_i = i
        return v

    @pydantic.root_validator()
    @classmethod
    def validate_keys_unique(cls, values) -> None:
        all_keys = [
            *values["pos_only_required"].keys(),
            *values["pos_only_optional"].keys(),
            *values["pos_or_kw_required"].keys(),
            *values["pos_or_kw_optional"].keys(),
            *values["kw_only_required"].keys(),
            *values["kw_only_optional"].keys(),
        ]
        if values["var_pos"]:
            all_keys.append(values["var_pos"][0])
        if values["var_kw"]:
            all_keys.append(values["var_kw"][0])

        if len(all_keys) != len(set(all_keys)):
            raise ValueError(repr(all_keys))
        return values

    def function_def(
        self,
        name: str,
        type: typing.Literal["function", "classmethod", "method"],
        indent=0,
        overload=False,
    ) -> cst.FunctionDef:
        decorators: typing.List[cst.Decorator] = []
        if overload:
            decorators.append(cst.Decorator(cst.Name("overload")))
        if type == "classmethod":
            decorators.append(cst.Decorator(cst.Name("classmethod")))
        return cst.FunctionDef(
            cst.Name(name),
            self.parameters(type),
            cst.IndentedBlock(
                [cst.SimpleStatementLine([s]) for s in self.body(indent)]
            ),
            decorators,
        )

    def body(self, indent: int) -> typing.Iterable[cst.BaseSmallStatement]:
        yield cst.Expr(self.docstring(indent))
        yield cst.Expr(cst.Ellipsis())

    def docstring(self, indent: int) -> cst.BaseExpression:
        i = " " * ((indent + 1) * 4)
        inner = f"\n{i}".join(metadata_lines(self.metadata))
        return cst.SimpleString(f'"""\n{i}{inner}\n{i}"""')

    def parameters(
        self, type: typing.Literal["function", "classmethod", "method"]
    ) -> cst.Parameters:
        posonly_params = [
            cst.Param(cst.Name(k), cst.Annotation(v.annotation))
            for k, v in self.pos_only_required.items()
        ] + [
            cst.Param(cst.Name(k), cst.Annotation(v.annotation), default=cst.Ellipsis())
            for k, v in possibly_order_dict(
                self.pos_only_optional, self.pos_only_optional_ordering
            ).items()
        ]

        if type == "classmethod":
            posonly_params.insert(0, cst.Param(cst.Name("cls")))
        elif type == "method":
            posonly_params.insert(0, cst.Param(cst.Name("self")))

        return cst.Parameters(
            posonly_params=posonly_params,
            params=[
                cst.Param(cst.Name(k), cst.Annotation(v.annotation))
                for k, v in self.pos_or_kw_required.items()
            ]
            + [
                cst.Param(
                    cst.Name(k), cst.Annotation(v.annotation), default=cst.Ellipsis()
                )
                for k, v in possibly_order_dict(
                    self.pos_or_kw_optional, self.pos_or_kw_optional_ordering
                ).items()
            ],
            star_arg=(
                cst.Param(
                    cst.Name(self.var_pos[0]),
                    cst.Annotation(self.var_pos[1].annotation),
                )
                if self.var_pos
                else cst.MaybeSentinel.DEFAULT
            ),
            star_kwarg=(
                cst.Param(
                    cst.Name(self.var_kw[0]), cst.Annotation(self.var_kw[1].annotation)
                )
                if self.var_kw
                else None
            ),
            kwonly_params=[
                cst.Param(cst.Name(k), cst.Annotation(v.annotation))
                for k, v in self.kw_only_required.items()
            ]
            + [
                cst.Param(
                    cst.Name(k), cst.Annotation(v.annotation), default=cst.Ellipsis()
                )
                for k, v in self.kw_only_optional.items()
            ],
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

    def content_equal(self, other: Signature) -> bool:
        """
        Returns true if all fields besides metadata are equal
        """
        for field in self.__fields__.keys():
            if field == "metadata":
                continue
            if getattr(self, field) != getattr(other, field):
                return False
        return True

    def __ior__(self, other: Signature) -> Signature:
        self._copy_pos_only(other)
        self._copy_pos_or_kw(other)
        self._copy_var_pos(other)
        self._copy_kw_only(other)
        self._copy_var_kw(other)

        update_add(self.metadata, other.metadata)
        self._trim_positional_only_args()
        return self

    def _trim_positional_only_args(self):
        """
        If there are excss positional only args, move them to variable positional only args
        """
        # if we already have var pos only args, remove all positional only args
        if (
            self.var_pos
            or len(self.pos_only_optional) > MAX_OPTIONAL_POSITIONAL_ONLY_ARGS
        ):
            var_pos_output = unify(
                [
                    self.var_pos[1] if self.var_pos else BottomOutput(),
                    *self.pos_only_optional.values(),
                ]
            )
            var_pos_label = self.var_pos[0] if self.var_pos else "_args"
            self.var_pos = (var_pos_label, var_pos_output)
            self.pos_only_optional = {}
            self.pos_only_optional_ordering = []

    def _copy_pos_only(self, other: Signature) -> None:
        pos_only_required = dict(
            map(
                unify_named_types,
                zip(self.pos_only_required.items(), other.pos_only_required.items()),
            )
        )
        n_pos_only_required = len(pos_only_required)
        self_new_pos_only_optional = slice_dict(
            self.pos_only_required, n_pos_only_required
        )
        other_new_pos_only_optional = slice_dict(
            other.pos_only_required, n_pos_only_required
        )
        self.pos_only_required = pos_only_required

        addititional_ordering: PartialKeyOrdering = []
        # also add to ordering that new optional keys must come before old ones, because
        # they used to be required
        if self_new_pos_only_optional and self.pos_only_optional:
            add_list(
                addititional_ordering,
                (
                    # last of required is before first of optional
                    next(iter(reversed(self_new_pos_only_optional.keys()))),
                    next(iter(self.pos_only_optional.keys())),
                ),
            )
        if other_new_pos_only_optional and other.pos_only_optional:
            add_list(
                addititional_ordering,
                (
                    next(iter(reversed(other_new_pos_only_optional.keys()))),
                    next(iter(other.pos_only_optional.keys())),
                ),
            )
        update_unify(
            self.pos_only_optional,
            self_new_pos_only_optional,
            other.pos_only_optional,
            other_new_pos_only_optional,
        )
        update_list(
            self.pos_only_optional_ordering,
            other.pos_only_optional_ordering,
            partial_key_ordering(self_new_pos_only_optional),
            partial_key_ordering(other_new_pos_only_optional),
            addititional_ordering,
        )

    def _copy_pos_or_kw(self, other: Signature) -> None:
        # First take off new optional keys from self and other, making sure to keep order
        self_pos_or_kw_required_keys = list(self.pos_or_kw_required.keys())
        other_pos_or_kw_required_keys = list(other.pos_or_kw_required.keys())
        pos_or_kw_required_keys = set(self_pos_or_kw_required_keys) & set(
            other_pos_or_kw_required_keys
        )
        # Pop off all required keys that are not in both sets
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
        update_unify(
            self.pos_or_kw_required, other.pos_or_kw_required,
        )

        update_unify(
            self.pos_or_kw_optional,
            other_new_optional,
            self_new_optional,
            other.pos_or_kw_optional,
        )
        update_list(
            self.pos_or_kw_optional_ordering,
            other.pos_or_kw_optional_ordering,
            partial_key_ordering(self_new_optional),
            partial_key_ordering(other_new_optional),
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
        update_unify(self.kw_only_required, other.kw_only_required)
        update_unify(self.kw_only_optional, other.kw_only_optional)

        # Move any kw_only to pos_or_kw that already exist there
        # (this pops up when sometimes a function is bound and sometimes it isn't, like numpy.amin in dask, not sure why this is)
        move(
            self.pos_or_kw_required,
            self.kw_only_required,
            set(self.kw_only_required) & set(self.pos_or_kw_required),
            lambda l, r: unify((l, r)),
        )
        move(
            self.pos_or_kw_optional,
            self.kw_only_optional,
            set(self.kw_only_optional) & set(self.pos_or_kw_optional),
            lambda l, r: unify((l, r)),
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


def metadata_lines(m: Metadata) -> typing.Iterable[str]:
    for k, v in sort_items(m):
        yield f"{k}: {v}"


def partial_key_ordering(d: typing.Dict[str, Type]) -> PartialKeyOrdering:
    prev_key = None
    pairs: PartialKeyOrdering = []
    for key in d.keys():
        if prev_key is not None:
            add_list(pairs, (prev_key, key))
        prev_key = key
    return pairs


def possibly_order_dict(
    d: typing.Dict[str, Type], order: PartialKeyOrdering
) -> typing.Dict[str, Type]:
    """
    Resort dict by topographical sorting of order
    """
    return {k: d[k] for k in networkx.topological_sort(networkx.DiGraph(order))} or d


def unify_named_types(
    name_and_types: typing.Iterable[typing.Tuple[typing.Optional[str], Type]]
) -> typing.Tuple[str, Type]:
    """
    Verifies the names are the same and unifies the types. Returns None if no args passed in
    or all are none
    """
    names, tps = zip(*filter(lambda x: x is not None, name_and_types))  # type: ignore
    unique_names = set(filter(lambda x: x is not None, names))
    if len(unique_names) != 1:
        raise ValueError(f"Cannot unify the types {name_and_types!r}")
    return unique_names.pop(), unify(tps)


K = typing.TypeVar("K")
V = typing.TypeVar("V")
VR = typing.TypeVar("VR")


class DontAdd:
    pass


DONT_ADD = DontAdd()


def slice_dict(d: typing.Dict[K, V], n: int) -> typing.Dict[K, V]:
    """
    Slices n off the front of the dict
    """
    return dict(kv for i, kv in enumerate(d.items()) if i >= n)


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
    Moves keys from right to left, making sure to use original ordering in r
    """
    for k, v in r.items():
        if k not in keys:
            continue
        if k in l:
            v = f(l[k], v)
        l[k] = v

    for k in keys:
        del r[k]


def merge_intersection(
    l: typing.Dict[K, V], r: typing.Dict[K, VR], f: typing.Callable[[V, VR], V]
) -> None:
    """
    Moves all keys that are present in both left and right only to left, using function to merge them!
    """
    for k in set(l.keys()) & set(r.keys()):
        vr = r.pop(k)
        l[k] = f(l[k], vr)


def update(
    l: typing.Dict[K, V],
    *rs: typing.Dict[K, V],
    f: typing.Callable[[V, V], typing.Union[DontAdd, V]],
) -> None:
    """
    Updates the left dict with the right dict.

    On conflicting keys calls function with left and right values to return result.
    """
    for r in rs:
        for k, v in r.items():
            if k in l:
                res = f(l[k], v)
                if isinstance(res, DontAdd):
                    del l[k]
                else:
                    l[k] = res
            else:
                l[k] = v


update_ior = functools.partial(update, f=operator.ior)
update_add = functools.partial(update, f=operator.add)
update_unify = functools.partial(update, f=lambda l, r: unify((l, r)))


def merge_property_into_method(
    l: Signature, r: typing.Tuple[Metadata, OutputType]
) -> Signature:
    """
    Merges a property into a method by just using method
    """
    return l


def merge_method_class(l: Class, r: Signature) -> Class:
    l.ior_constructor(r)
    return l


def merge_method_overloads_class(l: Class, r: typing.List[Signature]) -> Class:
    merge_overloads(l.constructor_overloads, r)
    return l


def merge_methods_properties(
    l: typing.Tuple[Metadata, OutputType], r: typing.Tuple[Metadata, OutputType]
) -> typing.Tuple[Metadata, OutputType]:
    update_add(l[0], r[0])
    return (l[0], unify((l[1], r[1])))


update_metadata_and_types = functools.partial(update, f=merge_methods_properties)


def merge_overloads(
    old: typing.List[Signature], new: typing.List[Signature]
) -> typing.List[Signature]:
    """
    Merges the two lists of overloads, updating the old list. Any signatures that match, we take the union of their metadata.
    """
    for new_sig in new:
        # Iterate through all the old signatures, if we find one which matches, update that and break
        for old_sig in old:
            if new_sig.content_equal(old_sig):
                update_add(old_sig.metadata, new_sig.metadata)
                break
        # Otherwise, we didn't find one, so add the new one to the old
        else:
            old.append(new_sig)
    return old


update_overloads = functools.partial(update, f=merge_overloads)


T = typing.TypeVar("T")

# Set theoretic functions on lists
# Don't use sets because we want to preserve insertion order for determinism


def add_list(l: typing.List[T], a: T) -> None:
    if a not in l:
        l.append(a)


def update_list(l: typing.List[T], *others: typing.Iterable[T]) -> None:
    for other in others:
        for x in other:
            add_list(l, x)
