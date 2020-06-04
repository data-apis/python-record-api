"""
Functions and tools to unify types.

__str__ of output types should be representation as type signature in function paramater
"""
from __future__ import annotations

import typing
import collections
import pydantic
import abc
import ast


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
]

# If thera are more than this amount in a union, just use any
MAX_UNION_ITEMS = 5
# More than this and it will be tuple of arbitrary length
MAX_TUPLE_ITEMS = 2


def annotation(tp: OutputType) -> typing.Optional[ast.AST]:
    if is_unknown(tp):
        return None
    return tp.annotation


def create_type(o: object) -> OutputType:
    try:
        tp = pydantic.parse_obj_as(InputType, o)  # type: ignore
    except pydantic.error_wrappers.ValidationError:
        raise ValueError(o)
    return to_output(tp)


def unify_inputs(types: typing.Iterable[InputType]) -> OutputType:
    return unify(map(to_output, types))


def unify(types: typing.Iterable[OutputType]) -> OutputType:
    types = set(types)
    tp_tps_to_tps: typing.DefaultDict[
        typing.Type[OutputType], typing.Set[OutputType]
    ] = collections.defaultdict(set)
    for tp in types:
        tp_tps_to_tps[type(tp)].add(tp)

    unified_types: typing.Set[OutputType] = set()

    if ObjectOutput in tp_tps_to_tps:
        return ObjectOutput()

    for tp_tp, tps in tp_tps_to_tps.items():
        res: OutputType = _unify_output_tp(tp_tp, tps)
        if isinstance(res, UnionOutput):
            unified_types |= set(res.options)
        else:
            unified_types.add(res)

    if not unified_types:
        return BottomOutput()
    if len(unified_types) > MAX_UNION_ITEMS:
        return ObjectOutput()
    if len(unified_types) == 1:
        return unified_types.pop()
    return UnionOutput(options=unified_types)


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
    def annotation(self) -> ast.AST:
        ...


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
        return ast.Constant(None, None)


class StringInput(InputTypeBase):
    __root__: str

    def to_output(self) -> StringOutput:
        return StringOutput(options=[self.__root__])


class StringOutput(OutputTypeBase):
    """
    >>> str(StringOutput())
    str
    >>> str(StringOutput(options=["hi", "there"]))
    Literal["hi", "there"]
    """

    type: typing.Literal["str"] = "str"
    options: typing.Union[typing.FrozenSet[str], None] = None

    @property
    def annotation(self) -> ast.AST:
        if self.options:
            return ast.Subscript(
                ast.Name("Literal", ast.Load()),
                ast.Index(
                    ast.Tuple([ast.Constant(s, None) for s in self.options], ast.Load())
                ),
                ast.Load(),
            )
            return f'Literal[{", ".join(map(str, self.options))}]'
        return ast.Name("int", ast.Load())

    @classmethod
    def unify(cls, tps: typing.Iterable[StringOutput]) -> StringOutput:
        options: typing.Set[str] = set()
        for tp in tps:
            if tp.options is None:
                return StringOutput()
            options.update(tp.options)
        return StringOutput(options=options)


class ListInput(InputTypeBase):
    __root__: typing.List[InputType]

    def to_output(self) -> ListOutput:
        return ListOutput(item=unify(map(to_output, self.__root__)))


class ListOutput(OutputTypeBase):
    type: typing.Literal["list"] = "list"
    item: OutputType

    @property
    def annotation(self) -> ast.AST:
        if is_unknown(self.item):
            return ast.Name("list", ast.Load())
        return ast.Subscript(
            ast.Name("List", ast.Load()), ast.Index(self.item.annotation), ast.Load()
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
    def annotation(self) -> ast.AST:
        if is_unknown(self.items):
            return ast.Name("tuple", ast.Load())
        if isinstance(self.items, tuple):
            return ast.Subscript(
                ast.Name("Tuple", ast.Load()),
                ast.Index(ast.Tuple([s.annotation for s in self.items], ast.Load())),
                ast.Load(),
            )
        return ast.Subscript(
            ast.Name("Tuple", ast.Load()),
            ast.Index(
                ast.Tuple([self.items.annotation, ast.Constant(..., None)], ast.Load())
            ),
            ast.Load(),
        )

    @classmethod
    def unify(cls, tps: typing.Iterable[TupleOutput]) -> TupleOutput:
        lengths = {len(tp.items) if isinstance(tp.items, tuple) else None for tp in tps}
        # only should be None if we have a fixed length tuple
        length = None if None in lengths or len(lengths) != 1 else lengths.pop()
        if length is not None and length > MAX_UNION_ITEMS:
            length = None
        # Is list if we have a fixed length typle
        all_items: typing.Union[
            typing.Set[OutputType], typing.List[typing.Set[OutputType]]
        ] = [set() for _ in range(length)] if length is not None else set()
        for tp in tps:
            items = tp.items
            if isinstance(all_items, set):
                if isinstance(items, tuple):
                    all_items |= set(items)
                else:
                    all_items.add(items)
            else:
                assert isinstance(items, tuple)
                for i, item in enumerate(items):
                    all_items[i].add(item)

        return TupleOutput(
            items=unify(all_items)
            if isinstance(all_items, set)
            else tuple(map(unify, all_items))
        )


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
    def annotation(self) -> ast.AST:
        if is_unknown(self.key) and is_unknown(self.value):
            return ast.Name("dict", ast.Load())
        return ast.Subscript(
            ast.Name("Dict", ast.Load()),
            ast.Index(
                ast.Tuple([self.key.annotation, self.value.annotation], ast.Load())
            ),
            ast.Load(),
        )

    @classmethod
    def unify(cls, tps: typing.Iterable[DictOutput]) -> DictOutput:
        return DictOutput(
            key=unify(tp.key for tp in tps), value=unify(tp.value for tp in tps)
        )


class ObjectOutput(OutputTypeBase):
    type: typing.Literal["object"] = "object"

    @property
    def annotation(self) -> ast.AST:
        return ast.Name("object", ast.Load())

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

    def to_output(self) -> typing.Union[OtherOutput, ObjectOutput]:
        return OtherOutput.safe_create(self.t)


class NamedOutput(BaseModel):
    # None if builtin
    module: typing.Optional[str] = None
    name: str

    @classmethod
    def from_input(cls, input: NamedInput) -> typing.Optional[NamedOutput]:
        if isinstance(input, BuiltinNamedInput):
            return cls(name=input.__root__)
        if '<' in input.name:
            return None
        return cls(name=input.name, module=input.module)

    @property
    def annotation(self) -> ast.AST:
        if self.module is None:
            return ast.Name(self.name, ast.Load())
        return ast.Attribute(ast.Name(self.module, ast.Load()), self.name, ast.Load())


class OtherOutput(OutputTypeBase):
    type: NamedOutput

    @classmethod
    def safe_create(cls, tp_i: NamedInput) -> typing.Union[OtherOutput, ObjectOutput]:
        tp = NamedOutput.from_input(tp_i)
        if tp is None:
            return ObjectOutput()
        return cls(type=tp)
    @property
    def annotation(self) -> ast.AST:
        return self.type.annotation

    @classmethod
    def unify(
        cls, tps: typing.Iterable[OtherOutput]
    ) -> typing.Union[OtherOutput, UnionOutput]:
        tps = set(tps)
        if len(tps) == 1:
            return tps.pop()
        return UnionOutput(options=tps)


class ModuleInput(InputTypeBase):
    t: typing.Literal["module"]
    v: str

    def to_output(self) -> ModuleOutput:
        return ModuleOutput(name=self.v)


class ModuleOutput(OutputTypeBase):
    type: typing.Literal["module"] = "module"
    name: typing.Optional[str] = None

    @property
    def annotation(self) -> ast.AST:
        return ast.Attribute(ast.Name("types", ast.Load()), "ModuleType", ast.Load())

    @classmethod
    def unify(cls, tps: typing.Iterable[ModuleOutput]) -> ModuleOutput:
        names = set(tp.name for tp in tps)
        if len(names) == 1:
            return ModuleOutput(name=names.pop())
        return ModuleOutput()


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
    def annotation(self) -> ast.AST:
        """
        Doesn't exist yet as generic type, but should

        https://github.com/python/typing/issues/159
        """
        if is_unknown(self.start) and is_unknown(self.stop) and is_unknown(self.step):
            return ast.Name("slice", ast.Load())
        return ast.Subscript(
            ast.Name("slice", ast.Load()),
            ast.Index(
                ast.Tuple(
                    [self.start.annotation, self.stop.annotation, self.step.annotation],
                    ast.Load(),
                )
            ),
            ast.Load(),
        )

    @classmethod
    def unify(cls, tps: typing.Iterable[SliceOutput]) -> SliceOutput:
        start: typing.Set[OutputType] = set()
        stop: typing.Set[OutputType] = set()
        step: typing.Set[OutputType] = set()
        for tp in tps:
            start.add(tp.start)
            stop.add(tp.stop)
            step.add(tp.step)
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
    def annotation(self) -> ast.AST:
        if self.name is None:
            return ast.Name("type", ast.Load())
        return ast.Subscript(
            ast.Name("Type", ast.Load()), ast.Index(self.name.annotation), ast.Load()
        )

    @classmethod
    def unify(cls, tps: typing.Iterable[TypeOutput]) -> TypeOutput:
        names = set(tp.name for tp in tps)
        if len(names) == 1:
            return TypeOutput(name=names.pop())
        return TypeOutput()


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
    def annotation(self) -> ast.AST:
        return ast.Name("Callable", ast.Load())

    @classmethod
    def unify(
        cls, tps: typing.Iterable[MethodWithoutSelfOutput]
    ) -> typing.Union[MethodWithoutSelfOutput, FunctionOutput]:
        tps = set(tps)
        if len(tps) == 1:
            return tps.pop()
        return FunctionOutput()


class FunctionOutput(OutputTypeBase):
    type: typing.Literal["function"] = "function"
    # If none, then any function
    name: typing.Optional[NamedOutput] = None

    @property
    def annotation(self) -> ast.AST:
        return ast.Name("Callable", ast.Load())

    @classmethod
    def unify(cls, tps: typing.Iterable[FunctionOutput]) -> FunctionOutput:
        names = set(tp.name for tp in tps)
        if len(names) == 1:
            return FunctionOutput(name=names.pop())
        return FunctionOutput()


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
    def annotation(self) -> ast.AST:
        return ast.Name("Callable", ast.Load())

    @classmethod
    def unify(
        cls, tps: typing.Iterable[MethodOutput]
    ) -> typing.Union[MethodOutput, FunctionOutput]:
        tps = set(tps)
        if len(tps) == 1:
            return tps.pop()
        return FunctionOutput()


class MethodInput(InputTypeBase):
    t: typing.Literal["method"] = "method"
    v: MethodInputValue

    def to_output(self) -> MethodOutput:
        return MethodOutput(name=self.v.name, self=to_output(self.v.self))


class MethodDescriptorInput(InputTypeBase):
    t: typing.Literal["method_descriptor"] = "method_descriptor"
    v: MethodDescriptorInputValue

    def to_output(self) -> ClassMethodOutput:
        return ClassMethodOutput(
            name=self.v.name, class_=self.v.class_.to_output().name
        )


class MethodDescriptorInputValue(BaseModel):
    name: str
    class_: TypeInput = pydantic.Field(alias="class")


class ClassMethodOutput(OutputTypeBase):  # type: ignore
    type: typing.Literal["classmethod"] = "classmethod"
    class_: NamedOutput
    name: str

    @property
    def annotation(self) -> ast.AST:
        return ast.Name("Callable", ast.Load())

    @classmethod
    def unify(
        cls, tps: typing.Iterable[ClassMethodOutput]
    ) -> typing.Union[ClassMethodOutput, FunctionOutput]:
        tps = set(tps)
        if len(tps) == 1:
            return tps.pop()
        return FunctionOutput()


class NumpyUfuncInput(InputTypeBase):
    t: NumpyUfuncInputType
    v: str

    def to_output(self) -> FunctionOutput:
        return FunctionOutput(name=NamedOutput(module="numpy", name=self.v))


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
    options: typing.Tuple[OutputType, ...]

    @property
    def annotation(self) -> ast.AST:
        return ast.Subscript(
            ast.Name("Union", ast.Load()),
            ast.Index(ast.Tuple([o.annotation for o in self.options], ast.Load())),
            ast.Load(),
        )

    @classmethod
    def unify(cls, tps: typing.Iterable[UnionOutput]) -> OutputType:
        options: typing.Set[OutputType] = set()
        for tp in tps:
            options |= set(tp.options)
        if len(options) == 1:
            return options.pop()
        return UnionOutput(options=options)


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
    def annotation(self) -> ast.AST:
        return ast.Name("object", ast.Load())


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
]

for cls in (InputType.__args__ + OutputType.__args__) + (  # type: ignore
    SliceInputValue,
    MethodInputValue,
):
    if cls is type(None):
        continue
    cls.update_forward_refs()
