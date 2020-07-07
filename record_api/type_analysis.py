"""
Functions and tools to unify types.

Note that this uses dicts as ordered sets in many places so that input and output
has the same ordering, so that git diffs are better
"""
from __future__ import annotations

import typing
import collections
import pydantic
import abc

import libcst as cst


__all__ = [
    "create_type",
    "OutputType",
    "unify",
    "annotation",
    "NoneOutput",
    "StringOutput",
    "ListOutput",
    "TupleOutput",
    "DictOutput",
    "ObjectOutput",
    "OtherOutput",
    "ModuleOutput",
    "SliceOutput",
    "TypeOutput",
    "FunctionOutput",
    "MethodWithoutSelfOutput",
    "MethodOutput",
    "ClassMethodOutput",
    "UnionOutput",
    "BottomOutput",
    "MethodDescriptorOutput",
    "parser_config",
    "NumpyUfuncOutput",
]

# If there are more than this amount in a union, just use any
MAX_UNION_ITEMS = 5
# If there are more than this amount in a string literal, just use any
MAX_STRING_ITEMS = 5
# More than this and it will be tuple of arbitrary length
MAX_TUPLE_ITEMS = 2


parser_config = cst.PartialParserConfig(
    python_version="3.8", encoding="utf-8", default_indent="    ", default_newline="\n",
)


def annotation(tp: OutputType) -> typing.Optional[cst.BaseExpression]:
    if is_unknown(tp):
        return None
    return tp.annotation


def create_type(o: object) -> OutputType:
    try:
        tp = pydantic.parse_obj_as(InputType, o)  # type: ignore
    except pydantic.error_wrappers.ValidationError:
        raise ValueError(f"Could not parse JSON as input type: {o}")
    return to_output(tp)


def unify_inputs(types: typing.Iterable[InputType]) -> OutputType:
    return unify(map(to_output, types))


def unify(types: typing.Iterable[OutputType]) -> OutputType:
    # groupby by the type to collect all types with same kind together
    tp_tps_to_tps: typing.DefaultDict[
        # Use dict for values as ordered set to preserve ordering
        typing.Type[OutputType],
        typing.Dict[OutputType, None],
    ] = collections.defaultdict(dict)

    types = list(types)
    while types:
        tp = types.pop()
        if isinstance(tp, ObjectOutput):
            return ObjectOutput()
        # If we have a union, add all to existing types
        if isinstance(tp, UnionOutput):
            types.extend(tp.options)
            continue
        tp_tps_to_tps[type(tp)][tp] = None

    # OK now we know that tp_tps_to_tps contains no union types
    # Now try to unify each of the kinds to give us a set of types to add to to the unified
    # Used a dict here as an ordered set
    unified_types: typing.Dict[OutputType, None] = {}

    # Sort so order of final types is preserved
    for tp_tp, tps in tp_tps_to_tps.items():
        res: OutputType = _unify_output_tp(tp_tp, tps.keys())
        if isinstance(res, UnionOutput):
            for o in res.options:
                unified_types[o] = None
        else:
            unified_types[res] = None

    if not unified_types:
        return BottomOutput()
    if len(unified_types) > MAX_UNION_ITEMS:
        return ObjectOutput()
    if len(unified_types) == 1:
        return next(iter(unified_types.keys()))
    return UnionOutput(options=tuple(unified_types.keys()))


OUTPUT_TYPE = typing.TypeVar("OUTPUT_TYPE", bound="OutputTypeBase")


# Define this function for typing purposes
def _unify_output_tp(
    cls: typing.Type[OUTPUT_TYPE], tps: typing.Iterable[OUTPUT_TYPE]
) -> OutputType:
    return cls.unify(tps)


class BaseModel(pydantic.BaseModel):
    class Config:
        extra = "forbid"

    # https://github.com/samuelcolvin/pydantic/issues/1303#issuecomment-599712964
    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))


class OutputTypeBase(BaseModel, abc.ABC):
    @classmethod
    @abc.abstractmethod
    def unify(
        cls: typing.Type[OUTPUT_TYPE], tps: typing.Iterable[OUTPUT_TYPE]
    ) -> OutputType:
        ...

    @property
    @abc.abstractmethod
    def annotation(self) -> cst.BaseExpression:
        ...

    @property
    def module(self) -> typing.Optional[str]:
        return None


class InputTypeBase(BaseModel, abc.ABC):
    @abc.abstractmethod
    def to_output(self) -> OutputType:
        ...


def to_output(tp: InputType) -> OutputType:
    if tp is None:
        return NoneOutput()
    return tp.to_output()


def is_unknown(tp: object) -> bool:
    return isinstance(tp, (ObjectOutput, BottomOutput))


class NoneOutput(OutputTypeBase):
    type: typing.Literal["None"] = "None"

    @classmethod
    def unify(cls, tps: typing.Iterable[NoneOutput]) -> NoneOutput:
        return NoneOutput()

    @property
    def annotation(self):
        return cst.Name("None")


class StringInput(InputTypeBase):
    __root__: str

    def to_output(self) -> StringOutput:
        return StringOutput(options=[self.__root__])


class StringOutput(OutputTypeBase):

    type: typing.Literal["str"] = "str"
    options: typing.Union[typing.Tuple[str, ...], None] = None

    @property
    def annotation(self) -> cst.BaseExpression:
        if self.options:
            return cst.Subscript(
                cst.Name("Literal"),
                [
                    cst.SubscriptElement(cst.Index(cst.SimpleString(repr(option))))
                    for option in self.options
                ],
            )
        return cst.Name("str")

    @classmethod
    def unify(cls, tps: typing.Iterable[StringOutput]) -> StringOutput:
        options: typing.Dict[str, None] = {}
        for tp in tps:
            if tp.options is None:
                return StringOutput()
            for o in tp.options:
                options[o] = None
            if len(options) > MAX_STRING_ITEMS:
                return StringOutput()
        return StringOutput(options=tuple(options.keys()))


class ListInput(InputTypeBase):
    __root__: typing.List[InputType]

    def to_output(self) -> ListOutput:
        return ListOutput(item=unify(map(to_output, self.__root__)))


class ListOutput(OutputTypeBase):
    type: typing.Literal["list"] = "list"
    item: OutputType

    @property
    def annotation(self):
        if is_unknown(self.item):
            return cst.Name("list")
        return cst.helpers.parse_template_expression(
            "List[{item}]", parser_config, item=self.item.annotation
        )

    @classmethod
    def unify(cls, tps: typing.Iterable[ListOutput]) -> ListOutput:
        return ListOutput(item=unify(tp.item for tp in tps))


class TupleInput(InputTypeBase):
    t: typing.Literal["tuple"]
    v: typing.List[InputType]

    def to_output(self) -> TupleOutput:
        return TupleOutput(items=list(map(to_output, self.v)))


class TupleOutput(OutputTypeBase):
    type: typing.Literal["tuple"] = "tuple"
    # If just one item then tuple of arbitrary length of all the same type
    items: typing.Union[OutputType, typing.Tuple[OutputType, ...]]

    @property
    def annotation(self):
        if is_unknown(self.items):
            return cst.Name("tuple")
        if isinstance(self.items, tuple):
            return cst.Subscript(
                cst.Name("Tuple"),
                [cst.SubscriptElement(cst.Index(s.annotation)) for s in self.items],
            )

        return cst.helpers.parse_template_expression(
            "Tuple[{item}, ...]", parser_config, item=self.items.annotation
        )

    @classmethod
    def unify(cls, tps: typing.Iterable[TupleOutput]) -> TupleOutput:
        lengths = {len(tp.items) if isinstance(tp.items, tuple) else None for tp in tps}
        # only should be None if we have a fixed length tuple
        length = None if None in lengths or len(lengths) != 1 else lengths.pop()
        if length is not None and length > MAX_UNION_ITEMS:
            length = None
        if length is None:
            possible_values: typing.List[OutputType] = []
            for tp in tps:
                items = tp.items
                if isinstance(items, tuple):
                    possible_values.extend(items)
                else:
                    possible_values.append(items)
            return TupleOutput(items=unify(possible_values))
        i_to_possible_values: typing.List[typing.List[OutputType]] = [
            [] for _ in range(length)
        ]
        for tp in tps:
            items = tp.items
            assert isinstance(items, tuple)
            for i, item in enumerate(items):
                i_to_possible_values[i].append(item)

        return TupleOutput(items=tuple(map(unify, i_to_possible_values)))


class DictInput(InputTypeBase):
    t: typing.Literal["dict"]
    v: typing.List[typing.Tuple[InputType, InputType]]

    def to_output(self) -> DictOutput:
        if self.v:
            key, value = map(unify_inputs, zip(*self.v))
        else:
            key = BottomOutput()
            value = BottomOutput()
        return DictOutput(key=key, value=value)


class DictOutput(OutputTypeBase):
    type: typing.Literal["dict"] = "dict"
    key: OutputType
    value: OutputType

    @property
    def annotation(self):
        if is_unknown(self.key) and is_unknown(self.value):
            return cst.Name("dict")
        return cst.Subscript(
            cst.Name("Dict"),
            [
                cst.SubscriptElement(cst.Index(self.key.annotation)),
                cst.SubscriptElement(cst.Index(self.value.annotation)),
            ],
        )

    @classmethod
    def unify(cls, tps: typing.Iterable[DictOutput]) -> DictOutput:
        return DictOutput(
            key=unify(tp.key for tp in tps), value=unify(tp.value for tp in tps)
        )


class ObjectOutput(OutputTypeBase):
    type: typing.Literal["object"] = "object"

    @property
    def annotation(self):
        return cst.Name("object")

    @classmethod
    def unify(cls, tps: typing.Iterable[ObjectOutput]) -> ObjectOutput:
        return ObjectOutput()


class BuiltinNamedInput(BaseModel):
    __root__: str


class ModuleNamedInput(BaseModel):
    module: str
    name: str


NamedInput = typing.Union[BuiltinNamedInput, ModuleNamedInput]


class OtherInputType(InputTypeBase):
    t: NamedInput

    def to_output(self) -> typing.Union[OtherOutput, StringOutput, ObjectOutput]:
        if self.t == BuiltinNamedInput(__root__="str"):
            return StringOutput()
        return OtherOutput.safe_create(self.t)


class NamedOutput(BaseModel):
    # None if builtin
    module: typing.Optional[str] = None
    name: str

    @classmethod
    def from_input(cls, input: NamedInput) -> typing.Optional[NamedOutput]:
        if isinstance(input, BuiltinNamedInput):
            return cls(name=input.__root__)
        if "<" in input.name:
            return None
        return cls(name=input.name, module=input.module)

    @property
    def annotation(self) -> typing.Union[cst.Name, cst.Attribute]:
        first_name, *rest = (
            self.module.split(".") + [self.name] if self.module else [self.name]
        )
        expr: typing.Union[cst.Name, cst.Attribute] = cst.Name(first_name)
        for name in rest:
            expr = cst.Attribute(expr, cst.Name(name))
        return expr


class OtherOutput(OutputTypeBase):
    type: NamedOutput

    @classmethod
    def safe_create(cls, tp_i: NamedInput) -> typing.Union[OtherOutput, ObjectOutput]:
        tp = NamedOutput.from_input(tp_i)
        if tp is None:
            return ObjectOutput()
        return cls(type=tp)

    @property
    def annotation(self):
        return self.type.annotation

    @classmethod
    def unify(
        cls, tps: typing.Iterable[OtherOutput]
    ) -> typing.Union[OtherOutput, UnionOutput]:
        tps = {t: None for t in tps}
        if len(tps) == 1:
            return next(iter(tps.keys()))
        return UnionOutput(options=tuple(tps.keys()))

    @property
    def module(self) -> typing.Optional[str]:
        return self.type.module


class ModuleInput(InputTypeBase):
    t: typing.Literal["module"]
    v: str

    def to_output(self) -> ModuleOutput:
        return ModuleOutput(name=self.v)


class ModuleOutput(OutputTypeBase):
    type: typing.Literal["module"] = "module"
    name: typing.Optional[str] = None

    @property
    def annotation(self):
        return cst.Attribute(cst.Name("types"), cst.Name("ModuleType"))

    @classmethod
    def unify(cls, tps: typing.Iterable[ModuleOutput]) -> ModuleOutput:
        names = set(tps)
        if len(names) == 1:
            return names.pop()
        return ModuleOutput()

    @property
    def module(self) -> typing.Optional[str]:
        return self.name


class SliceInput(InputTypeBase):
    t: typing.Literal["slice"]
    v: SliceInputValue

    def to_output(self) -> SliceOutput:
        v = self.v
        return SliceOutput(
            start=to_output(v.start), stop=to_output(v.stop), step=to_output(v.step),
        )


class SliceInputValue(BaseModel):
    start: InputType
    stop: InputType
    step: InputType


class SliceOutput(OutputTypeBase):

    type: typing.Literal["slice"] = "slice"
    start: OutputType
    stop: OutputType
    step: OutputType

    @property
    def annotation(self):
        """
        Doesn't exist yet as generic type, but should

        https://github.com/python/typing/issues/159
        """
        if is_unknown(self.start) and is_unknown(self.stop) and is_unknown(self.step):
            return cst.Name("slice")
        return cst.Subscript(
            cst.Name("slice"),
            [
                cst.SubscriptElement(cst.Index(self.start.annotation)),
                cst.SubscriptElement(cst.Index(self.stop.annotation)),
                cst.SubscriptElement(cst.Index(self.start.annotation)),
            ],
        )

    @classmethod
    def unify(cls, tps: typing.Iterable[SliceOutput]) -> SliceOutput:
        start: typing.List[OutputType] = []
        stop: typing.List[OutputType] = []
        step: typing.List[OutputType] = []
        for tp in tps:
            start.append(tp.start)
            stop.append(tp.stop)
            step.append(tp.step)
        return SliceOutput(start=unify(start), step=unify(step), stop=unify(stop))


class TypeInput(InputTypeBase):
    t: typing.Literal["type"]
    v: NamedInput

    def to_output(self) -> TypeOutput:
        return TypeOutput(name=NamedOutput.from_input(self.v))


class TypeOutput(OutputTypeBase):
    type: typing.Literal["type"] = "type"
    # If none, then any type
    name: typing.Optional[NamedOutput] = None

    @property
    def annotation(self):
        if self.name is None:
            return cst.Name("type")
        return cst.Subscript(
            cst.Name("Type"), [cst.SubscriptElement(cst.Index(self.name.annotation))]
        )

    @classmethod
    def unify(cls, tps: typing.Iterable[TypeOutput]) -> TypeOutput:
        names = set(tp.name for tp in tps)
        if len(names) == 1:
            return TypeOutput(name=names.pop())
        return TypeOutput()

    @property
    def module(self) -> typing.Optional[str]:
        if self.name:
            return self.name.module
        return None


class FunctionInput(InputTypeBase):
    t: typing.Literal["function"]
    v: NamedInput

    def to_output(self) -> typing.Union[FunctionOutput, MethodWithoutSelfOutput]:
        name = NamedOutput.from_input(self.v)
        # We are in some lambda
        if not name:
            return FunctionOutput()
        if "." in name.name:
            # For some reason happens with MaskedArray.mean
            classname, methodname = name.name.split(".")
            return MethodWithoutSelfOutput(
                name=methodname, class_=NamedOutput(name=classname, module=name.module)
            )
        return FunctionOutput(name=name)


class MethodWithoutSelfOutput(OutputTypeBase):
    type: typing.Literal["method_no_self"] = "method_no_self"
    class_: NamedOutput
    name: str

    @property
    def annotation(self):
        return cst.Name("Callable")

    @classmethod
    def unify(
        cls, tps: typing.Iterable[MethodWithoutSelfOutput]
    ) -> typing.Union[MethodWithoutSelfOutput, FunctionOutput]:
        tps = set(tps)
        if len(tps) == 1:
            return tps.pop()
        return FunctionOutput()

    @property
    def module(self) -> typing.Optional[str]:
        return self.class_.name


class FunctionOutput(OutputTypeBase):
    type: typing.Literal["function"] = "function"
    # If none, then any function
    name: typing.Optional[NamedOutput] = None

    @property
    def annotation(self):
        return cst.Name("Callable")

    @classmethod
    def unify(cls, tps: typing.Iterable[FunctionOutput]) -> FunctionOutput:
        names = set(tp.name for tp in tps)
        if len(names) == 1:
            return FunctionOutput(name=names.pop())
        return FunctionOutput()

    @property
    def module(self) -> typing.Optional[str]:
        if self.name:
            return self.name.module
        return None


class BuiltinFunctionInput(InputTypeBase):
    t: typing.Literal["builtin_function_or_method"] = "builtin_function_or_method"
    v: NamedInput

    def to_output(self) -> FunctionOutput:
        return FunctionOutput(name=NamedOutput.from_input(self.v))


class BuiltinMethodInput(InputTypeBase):
    t: typing.Literal["builtin_function_or_method"] = "builtin_function_or_method"
    v: MethodInputValue

    def to_output(self) -> MethodOutput:
        return MethodOutput(name=self.v.name, self=to_output(self.v.self))


class MethodInputValue(BaseModel):  # type: ignore
    name: str
    self: InputType


class MethodOutput(OutputTypeBase):  # type: ignore
    type: typing.Literal["method"] = "method"
    name: str
    self: OutputType

    @property
    def annotation(self):
        return cst.Name("Callable")

    @classmethod
    def unify(
        cls, tps: typing.Iterable[MethodOutput]
    ) -> typing.Union[MethodOutput, FunctionOutput]:
        tps = set(tps)
        if len(tps) == 1:
            return tps.pop()
        return FunctionOutput()

    @property
    def module(self) -> typing.Optional[str]:
        return self.self.module


class MethodInput(InputTypeBase):
    t: typing.Literal["method"]
    v: MethodInputValue

    def to_output(self) -> MethodOutput:
        return MethodOutput(name=self.v.name, self=to_output(self.v.self))


class MethodDescriptorInput(InputTypeBase):
    t: typing.Literal["method_descriptor"]
    # TODO: Remove value, b/c its on signature
    v: MethodDescriptorInputValue

    def to_output(self) -> MethodDescriptorOutput:
        return MethodDescriptorOutput(name=self.v.name)


class MethodDescriptorOutput(OutputTypeBase):  # type: ignore
    type: typing.Literal["method_descriptor"] = "method_descriptor"
    name: str

    @property
    def annotation(self):
        return cst.Name("Callable")

    @classmethod
    def unify(
        cls, tps: typing.Iterable[MethodDescriptorOutput]
    ) -> typing.Union[MethodDescriptorOutput, FunctionOutput]:
        tps = set(tps)
        if len(tps) == 1:
            return tps.pop()
        return FunctionOutput()


class MethodDescriptorInputValue(BaseModel):
    name: str
    class_: TypeInput = pydantic.Field(alias="class")


class ClassMethodOutput(OutputTypeBase):  # type: ignore
    type: typing.Literal["classmethod"] = "classmethod"
    class_: NamedOutput
    name: str

    @property
    def annotation(self):
        return cst.Name("Callable")

    @classmethod
    def unify(
        cls, tps: typing.Iterable[ClassMethodOutput]
    ) -> typing.Union[ClassMethodOutput, FunctionOutput]:
        tps = set(tps)
        if len(tps) == 1:
            return tps.pop()
        return FunctionOutput()

    @property
    def module(self) -> typing.Optional[str]:
        return self.class_.module


class NumpyUfuncInput(InputTypeBase):
    t: NumpyUfuncInputType
    v: str

    def to_output(self) -> NumpyUfuncOutput:
        return NumpyUfuncOutput(name=self.v)


class NumpyUfuncOutput(OutputTypeBase):
    type: typing.Literal["numpy.ufunc"] = "numpy.ufunc"
    name: typing.Optional[str] = None

    @property
    def annotation(self):
        return NamedOutput(module="numpy", name="ufunc").annotation

    @classmethod
    def unify(cls, tps: typing.Iterable[NumpyUfuncOutput]) -> NumpyUfuncOutput:
        names = set(tp.name for tp in tps)
        if len(names) == 1:
            return NumpyUfuncOutput(name=names.pop())
        return NumpyUfuncOutput()


class NumpyUfuncInputType(BaseModel):
    module: typing.Literal["numpy"]
    name: typing.Literal["ufunc"]


class NumpyConvert2MAInput(InputTypeBase):
    t: NumpyConvert2MAInputType
    v: str

    def to_output(self) -> FunctionOutput:
        return FunctionOutput(name=NamedOutput(module="numpy.ma", name=self.v))


class NumpyConvert2MAInputType(BaseModel):
    module: typing.Literal["numpy.ma.core"]
    name: typing.Literal["_convert2ma"]


class NumpyNDArrayInput(InputTypeBase):
    t: ModuleNamedInput
    v: NumpyNDArrayValue

    def to_output(self) -> typing.Union[OtherOutput, ObjectOutput]:
        return OtherOutput.safe_create(self.t)


class NumpyNDArrayValue(BaseModel):
    dtype: str


class NumpyDTypeInput(InputTypeBase):
    t: ModuleNamedInput
    v: str

    def to_output(self) -> typing.Union[OtherOutput, ObjectOutput]:
        return OtherOutput.safe_create(self.t)


class UnionOutput(OutputTypeBase):
    type: typing.Literal["union"] = "union"
    # Can't be sets because when serializing, serialized as dicts
    options: typing.Tuple[OutputType, ...]

    @property
    def annotation(self):
        return cst.Subscript(
            cst.Name("Union"),
            [cst.SubscriptElement(cst.Index(o.annotation)) for o in self.options],
        )

    @classmethod
    def unify(cls, unions: typing.Iterable[UnionOutput]) -> OutputType:
        # This should never be called
        raise NotImplementedError()


class BottomOutput(OutputTypeBase):
    """
    Like any but represents an unkown type, so a union with it is always the other
    """

    type: typing.Literal["bottom"] = "bottom"

    @classmethod
    def unify(cls, tps: typing.Iterable[BottomOutput]) -> UnionOutput:
        # So that when unified will give back no more options
        return UnionOutput(options=[])

    @property
    def annotation(self):
        return cst.Name("object")


class OtherTypeInput(InputTypeBase):
    """
    Types that have different metaclasses will have a `t` that isn't `type` but their metaclass.
    """

    t: NamedInput
    v: NamedInput

    def to_output(self) -> TypeOutput:
        return TypeOutput(name=NamedOutput.from_input(self.v))


# Make them unions not subclasses so they are closed
# and pydantic will iterate through to find right one
InputType = typing.Union[
    None,
    StringInput,
    ListInput,
    TupleInput,
    DictInput,
    OtherInputType,
    ModuleInput,
    SliceInput,
    TypeInput,
    FunctionInput,
    BuiltinFunctionInput,
    BuiltinMethodInput,
    MethodInput,
    MethodDescriptorInput,
    NumpyUfuncInput,
    NumpyConvert2MAInput,
    NumpyNDArrayInput,
    NumpyDTypeInput,
    OtherTypeInput,
]
OutputType = typing.Union[
    NoneOutput,
    StringOutput,
    ListOutput,
    TupleOutput,
    DictOutput,
    ObjectOutput,
    OtherOutput,
    ModuleOutput,
    SliceOutput,
    TypeOutput,
    FunctionOutput,
    MethodWithoutSelfOutput,
    MethodOutput,
    ClassMethodOutput,
    UnionOutput,
    BottomOutput,
    MethodDescriptorOutput,
    NumpyUfuncOutput,
]

for cls in (InputType.__args__ + OutputType.__args__) + (  # type: ignore
    SliceInputValue,
    MethodInputValue,
):
    if cls is type(None):
        continue
    cls.update_forward_refs()
