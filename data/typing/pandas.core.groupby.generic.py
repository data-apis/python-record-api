from typing import *


class DataFrameGroupBy:

    # usage.dask: 1
    __name__: ClassVar[object]

    # usage.dask: 1
    A: object

    # usage.dask: 1
    B: object

    # usage.dask: 1
    _selected_obj: object

    # usage.dask: 24
    a: object

    # usage.dask: 20
    b: object

    # usage.dask: 1
    e: object

    # usage.dask: 1
    grouper: object

    # usage.dask: 2
    groups: object

    # usage.dask: 1
    idxmax: object

    # usage.dask: 1
    idxmin: object

    # usage.dask: 5
    obj: object

    # usage.dask: 1
    x: object

    # usage.dask: 3
    y: object

    # usage.dask: 2
    z: object

    def __eq__(self, _0: dask.dataframe.groupby.DataFrameGroupBy, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["z", "x"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["y"], /):
        """
        usage.dask: 4
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["y"]], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["C"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: str, /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["x"], /):
        """
        usage.dask: 5
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["x"]], /):
        """
        usage.dask: 3
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["A"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["A", "x"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["does_not_exist"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["b"], /):
        """
        usage.dask: 8
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["d", "c"]], /):
        """
        usage.dask: 5
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["c"], /):
        """
        usage.dask: 9
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["c", "b"]], /):
        """
        usage.dask: 5
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["b"]], /):
        """
        usage.dask: 7
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["d"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: pandas.core.indexes.base.Index, /):
        """
        usage.dask: 3
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["d", "c", "b"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["d", "b"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["a"], /):
        """
        usage.dask: 8
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["data"], /):
        """
        usage.dask: 4
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["data"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["A"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["a"]], /):
        """
        usage.dask: 5
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["b", "a"]], /):
        """
        usage.dask: 3
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["b"], Literal["x"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["x", "b"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["B"], /):
        """
        usage.dask: 12
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["C", "B"]], /):
        """
        usage.dask: 8
        """
        ...

    @overload
    def __getitem__(self, _0: List[int], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["d"], /):
        """
        usage.dask: 4
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["d", "b", "c"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["d", "a", "b", "c"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["c"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["z"], /):
        """
        usage.dask: 3
        """
        ...

    @overload
    def __getitem__(self, _0: int, /):
        """
        usage.dask: 4
        """
        ...

    @overload
    def __getitem__(self, _0: numpy.int64, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["__dask_tokenize__"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["ones"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["twos"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["c", "b", "a"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["z", "y"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["z"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: pandas.core.indexes.numeric.Int64Index, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["val3", "val2", "val1"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["value"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["value"], /):
        """
        usage.dask: 11
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["bar"], /):
        """
        usage.dask: 5
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["divisions"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["dask"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["to_pandas"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["__array_struct__"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["__array_interface__"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["__array__"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["e"], /):
        """
        usage.dask: 4
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["e", "c", "b"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["e", "c", "a"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["e", "b", "a"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["e", "c"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["e", "b"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["e", "a"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["e"]], /):
        """
        usage.dask: 1
        """
        ...

    def __getitem__(self, _0: object, /):
        """
        usage.dask: 167
        """
        ...

    @overload
    def aggregate(self, /, func: Literal["sum"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def aggregate(self, /, func: Literal["mean"]):
        """
        usage.dask: 3
        """
        ...

    @overload
    def aggregate(self, /, func: Literal["min"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def aggregate(self, /, func: Literal["max"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def aggregate(self, /, func: Literal["count"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def aggregate(self, /, func: Literal["size"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def aggregate(self, /, func: Literal["std"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def aggregate(self, /, func: Literal["var"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def aggregate(self, /, func: Literal["first"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def aggregate(self, /, func: Literal["last"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def aggregate(self, /, func: Literal["prod"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def aggregate(self, /, func: List[Literal["max", "min"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def aggregate(self, /, func: Dict[Literal["b"], Literal["mean"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def aggregate(self, /, func: Dict[Literal["b"], Literal["sum"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def aggregate(self, /, func: List[Literal["sum", "mean"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def aggregate(self, /, func: Dict[Literal["b"], List[Literal["sum", "mean"]]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def aggregate(self, /, func: Dict[Literal["c", "b"], Literal["sum", "mean"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def aggregate(self, /, func: Dict[Literal["e"], Literal["count"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def aggregate(self, /, func: Dict[Literal["e"], Literal["mean"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def aggregate(self, /, func: Dict[Literal["e"], Literal["std"]]):
        """
        usage.dask: 1
        """
        ...

    def aggregate(
        self,
        /,
        func: Union[
            Dict[
                Literal["b", "c", "e"],
                Union[
                    Literal["mean", "sum", "count", "std"], List[Literal["sum", "mean"]]
                ],
            ],
            str,
            List[Literal["max", "min", "sum", "mean"]],
        ],
    ):
        """
        usage.dask: 22
        """
        ...

    @overload
    def apply(self, /, func: dask.utils.methodcaller):
        """
        usage.dask: 1
        """
        ...

    @overload
    def apply(self, /, func: Callable):
        """
        usage.dask: 1
        """
        ...

    @overload
    def apply(self, /, func: Callable):
        """
        usage.dask: 36
        """
        ...

    @overload
    def apply(self, /, func: Callable, *args: Literal["v", "t"]):
        """
        usage.dask: 11
        """
        ...

    @overload
    def apply(self, /, func: numpy.int64, *args: Literal["v", "t"]):
        """
        usage.dask: 2
        """
        ...

    @overload
    def apply(self, /, func: Callable):
        """
        usage.dask: 1
        """
        ...

    @overload
    def apply(self, /, func: Callable):
        """
        usage.dask: 1
        """
        ...

    @overload
    def apply(self, /, func: Callable):
        """
        usage.dask: 1
        """
        ...

    @overload
    def apply(self, /, func: Callable):
        """
        usage.dask: 2
        """
        ...

    @overload
    def apply(self, /, func: Callable):
        """
        usage.dask: 3
        """
        ...

    @overload
    def apply(self, /, func: Callable):
        """
        usage.dask: 3
        """
        ...

    @overload
    def apply(self, /, func: Callable):
        """
        usage.dask: 1
        """
        ...

    @overload
    def apply(self, /, func: Literal["sum"]):
        """
        usage.dask: 1
        """
        ...

    def apply(
        self,
        /,
        func: Union[Callable, Literal["sum"], numpy.int64, dask.utils.methodcaller],
        *args: Literal["v", "t"],
    ):
        """
        usage.dask: 64
        """
        ...

    def count(self, /):
        """
        usage.dask: 12
        """
        ...

    def cumcount(self, /):
        """
        usage.dask: 3
        """
        ...

    @overload
    def cumprod(self, /):
        """
        usage.dask: 3
        """
        ...

    @overload
    def cumprod(self, /, axis: int):
        """
        usage.dask: 1
        """
        ...

    def cumprod(self, /, axis: int = ...):
        """
        usage.dask: 4
        """
        ...

    @overload
    def cumsum(self, /):
        """
        usage.dask: 3
        """
        ...

    @overload
    def cumsum(self, /, axis: int):
        """
        usage.dask: 1
        """
        ...

    def cumsum(self, /, axis: int = ...):
        """
        usage.dask: 4
        """
        ...

    def first(self, /):
        """
        usage.dask: 12
        """
        ...

    def get_group(self, /, name: int):
        """
        usage.dask: 4
        """
        ...

    def last(self, /):
        """
        usage.dask: 10
        """
        ...

    def max(self, /):
        """
        usage.dask: 10
        """
        ...

    def mean(self, /):
        """
        usage.dask: 15
        """
        ...

    def min(self, /):
        """
        usage.dask: 9
        """
        ...

    def nunique(self, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def prod(self, /):
        """
        usage.dask: 10
        """
        ...

    @overload
    def prod(self, /, min_count: int):
        """
        usage.dask: 1
        """
        ...

    def prod(self, /, min_count: int = ...):
        """
        usage.dask: 11
        """
        ...

    def size(self, /):
        """
        usage.dask: 9
        """
        ...

    @overload
    def std(self, /):
        """
        usage.dask: 7
        """
        ...

    @overload
    def std(self, /, ddof: int):
        """
        usage.dask: 2
        """
        ...

    def std(self, /, ddof: int = ...):
        """
        usage.dask: 9
        """
        ...

    @overload
    def sum(self, /):
        """
        usage.dask: 25
        """
        ...

    @overload
    def sum(self, /, min_count: int):
        """
        usage.dask: 1
        """
        ...

    def sum(self, /, min_count: int = ...):
        """
        usage.dask: 26
        """
        ...

    @overload
    def transform(self, /, func: Callable):
        """
        usage.dask: 13
        """
        ...

    @overload
    def transform(self, /, func: Callable):
        """
        usage.dask: 3
        """
        ...

    @overload
    def transform(self, /, func: Literal["sum"]):
        """
        usage.dask: 3
        """
        ...

    def transform(self, /, func: Union[Callable, Literal["sum"]]):
        """
        usage.dask: 19
        """
        ...

    @overload
    def var(self, /):
        """
        usage.dask: 5
        """
        ...

    @overload
    def var(self, /, ddof: int):
        """
        usage.dask: 2
        """
        ...

    def var(self, /, ddof: int = ...):
        """
        usage.dask: 7
        """
        ...


class SeriesGroupBy:

    # usage.dask: 1
    __name__: ClassVar[object]

    # usage.dask: 1
    idxmax: object

    # usage.dask: 1
    idxmin: object

    # usage.dask: 5
    obj: object

    def __iter__(self, /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def aggregate(self, /, func: List[Literal["max", "min"]]):
        """
        usage.dask: 3
        """
        ...

    @overload
    def aggregate(self, /, func: Literal["mean"]):
        """
        usage.dask: 3
        """
        ...

    @overload
    def aggregate(self, /, func: List[Literal["mean"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def aggregate(self, /, func: List[Literal["sum", "mean"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def aggregate(self, /, func: Literal["sum"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def aggregate(self, /, func: Literal["var"]):
        """
        usage.dask: 1
        """
        ...

    def aggregate(
        self,
        /,
        func: Union[
            Literal["var", "sum", "mean"], List[Literal["max", "min", "mean", "sum"]]
        ],
    ):
        """
        usage.dask: 10
        """
        ...

    @overload
    def apply(self, /, func: Callable):
        """
        usage.dask: 16
        """
        ...

    @overload
    def apply(self, /, func: Callable):
        """
        usage.dask: 2
        """
        ...

    @overload
    def apply(self, /, func: Callable):
        """
        usage.dask: 1
        """
        ...

    @overload
    def apply(self, /, func: Literal["sum"]):
        """
        usage.dask: 1
        """
        ...

    def apply(self, /, func: Union[Callable, Literal["sum"]]):
        """
        usage.dask: 20
        """
        ...

    def count(self, /):
        """
        usage.dask: 15
        """
        ...

    def cumcount(self, /):
        """
        usage.dask: 2
        """
        ...

    def cumprod(self, /):
        """
        usage.dask: 3
        """
        ...

    def cumsum(self, /):
        """
        usage.dask: 3
        """
        ...

    def first(self, /):
        """
        usage.dask: 14
        usage.xarray: 1
        """
        ...

    def get_group(self, /, name: int):
        """
        usage.dask: 3
        """
        ...

    def last(self, /):
        """
        usage.dask: 10
        """
        ...

    def max(self, /):
        """
        usage.dask: 11
        """
        ...

    def mean(self, /):
        """
        usage.dask: 13
        """
        ...

    def min(self, /):
        """
        usage.dask: 10
        """
        ...

    def nunique(self, /):
        """
        usage.dask: 14
        """
        ...

    def prod(self, /):
        """
        usage.dask: 9
        """
        ...

    def size(self, /):
        """
        usage.dask: 10
        """
        ...

    @overload
    def std(self, /):
        """
        usage.dask: 7
        """
        ...

    @overload
    def std(self, /, ddof: int):
        """
        usage.dask: 3
        """
        ...

    def std(self, /, ddof: int = ...):
        """
        usage.dask: 10
        """
        ...

    def sum(self, /):
        """
        usage.dask: 20
        """
        ...

    @overload
    def transform(self, /, func: Callable):
        """
        usage.dask: 13
        """
        ...

    @overload
    def transform(self, /, func: Callable):
        """
        usage.dask: 3
        """
        ...

    @overload
    def transform(self, /, func: Literal["sum"]):
        """
        usage.dask: 3
        """
        ...

    def transform(self, /, func: Union[Callable, Literal["sum"]]):
        """
        usage.dask: 19
        """
        ...

    def value_counts(self, /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def var(self, /):
        """
        usage.dask: 5
        """
        ...

    @overload
    def var(self, /, ddof: int):
        """
        usage.dask: 3
        """
        ...

    def var(self, /, ddof: int = ...):
        """
        usage.dask: 8
        """
        ...
