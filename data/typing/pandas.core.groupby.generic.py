from typing import *


class DataFrameGroupBy:

    # usage.dask: 1
    __name__: ClassVar[object]

    # usage.dask: 1
    A: object

    # usage.dask: 1
    # usage.koalas: 1
    B: object

    # usage.dask: 1
    _selected_obj: object

    # usage.dask: 24
    # usage.koalas: 6
    a: object

    # usage.koalas: 7
    agg: object

    # usage.dask: 20
    # usage.koalas: 1
    b: object

    # usage.koalas: 1
    c: object

    # usage.dask: 1
    e: object

    # usage.koalas: 14
    fillna: object

    # usage.dask: 1
    grouper: object

    # usage.dask: 2
    # usage.statsmodels: 5
    groups: object

    # usage.dask: 1
    # usage.koalas: 2
    idxmax: object

    # usage.dask: 1
    # usage.koalas: 2
    idxmin: object

    # usage.dask: 5
    obj: object

    # usage.dask: 1
    x: object

    # usage.dask: 3
    # usage.seaborn: 1
    y: object

    # usage.dask: 2
    z: object

    def __eq__(self, _0: dask.dataframe.groupby.DataFrameGroupBy, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["B"], /):
        """
        usage.dask: 12
        usage.koalas: 9
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["b"], /):
        """
        usage.dask: 8
        usage.koalas: 22
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["b"]], /):
        """
        usage.dask: 7
        usage.koalas: 9
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["a"], /):
        """
        usage.dask: 8
        usage.koalas: 36
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["a"]], /):
        """
        usage.dask: 5
        usage.koalas: 20
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["c"], /):
        """
        usage.dask: 9
        usage.koalas: 7
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["0"], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["v"], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["B"]], /):
        """
        usage.koalas: 3
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["c", "a"]], /):
        """
        usage.koalas: 8
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["b", "a"]], /):
        """
        usage.dask: 3
        usage.koalas: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["C"], /):
        """
        usage.dask: 1
        usage.koalas: 8
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["C"]], /):
        """
        usage.koalas: 8
        """
        ...

    @overload
    def __getitem__(self, _0: List[Tuple[Literal["y"], Literal["c"]]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["c", "b"]], /):
        """
        usage.dask: 5
        usage.koalas: 1
        """
        ...

    @overload
    def __getitem__(self, _0: list, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["factor"], /):
        """
        usage.alphalens: 3
        """
        ...

    @overload
    def __getitem__(self, _0: pandas.core.indexes.base.Index, /):
        """
        usage.alphalens: 3
        usage.dask: 3
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["rank"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["DV"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["myshapes"], /):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["geometry"], /):
        """
        usage.geopandas: 2
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
    def __getitem__(self, _0: List[Literal["d", "c"]], /):
        """
        usage.dask: 5
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["d"]], /):
        """
        usage.dask: 1
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
        usage.alphalens: 6
        usage.dask: 166
        usage.geopandas: 3
        usage.koalas: 137
        usage.statsmodels: 2
        """
        ...

    def __iter__(self, /):
        """
        usage.alphalens: 3
        usage.seaborn: 3
        usage.statsmodels: 1
        """
        ...

    @overload
    def aggregate(self, /, func: Literal["sum"]):
        """
        usage.dask: 1
        usage.koalas: 5
        """
        ...

    @overload
    def aggregate(self, /, func: Dict[Literal["C", "B"], Literal["sum", "min"]]):
        """
        usage.koalas: 3
        """
        ...

    @overload
    def aggregate(
        self,
        /,
        func: Dict[
            Literal["C", "B"], Union[Literal["sum"], List[Literal["max", "min"]]]
        ],
    ):
        """
        usage.koalas: 3
        """
        ...

    @overload
    def aggregate(self, /, func: List[Literal["sum"]]):
        """
        usage.koalas: 3
        """
        ...

    @overload
    def aggregate(
        self,
        /,
        func: Dict[Tuple[Literal["X", "Y"], Literal["B", "C"]], Literal["sum", "min"]],
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def aggregate(
        self,
        /,
        func: Dict[
            Tuple[Literal["X", "Y"], Literal["B", "C"]],
            Union[Literal["sum"], List[Literal["max", "min"]]],
        ],
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def aggregate(self, /, func: Literal["max"]):
        """
        usage.dask: 1
        usage.koalas: 2
        """
        ...

    @overload
    def aggregate(self, /, func: Literal["min"]):
        """
        usage.dask: 1
        usage.koalas: 2
        """
        ...

    @overload
    def aggregate(self, /, func: List[Literal["max", "min"]]):
        """
        usage.dask: 1
        usage.koalas: 2
        """
        ...

    @overload
    def aggregate(self, /):
        """
        usage.koalas: 7
        """
        ...

    @overload
    def aggregate(self, /, func: Dict[Literal["b"], Literal["nunique"]]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def aggregate(self, /, func: List[Literal["count", "std", "mean"]]):
        """
        usage.alphalens: 2
        """
        ...

    @overload
    def aggregate(self, /, func: List[Literal["count", "std", "mean", "max", "min"]]):
        """
        usage.alphalens: 1
        """
        ...

    @overload
    def aggregate(self, /, func: List[Callable]):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def aggregate(self, /, func: Callable):
        """
        usage.geopandas: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    def aggregate(self, /, func: Callable):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def aggregate(self, /, func: Callable):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def aggregate(self, /, func: List[Literal["count", "mean"]]):
        """
        usage.prophet: 1
        """
        ...

    @overload
    def aggregate(self, /, func: Literal["first"]):
        """
        usage.dask: 1
        usage.geopandas: 1
        """
        ...

    @overload
    def aggregate(self, /, func: Literal["mean"]):
        """
        usage.dask: 3
        usage.geopandas: 1
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
            List[Union[Callable, str]],
            str,
            Dict[
                Union[
                    Literal["C", "B", "b", "c", "e"],
                    Tuple[Literal["X", "Y"], Literal["B", "C"]],
                ],
                Union[str, List[Literal["sum", "mean", "max", "min"]]],
            ],
            Callable,
        ] = ...,
    ):
        """
        usage.alphalens: 3
        usage.dask: 22
        usage.geopandas: 3
        usage.koalas: 33
        usage.prophet: 1
        usage.statsmodels: 5
        """
        ...

    def all(self, /):
        """
        usage.koalas: 3
        """
        ...

    def any(self, /):
        """
        usage.koalas: 3
        """
        ...

    @overload
    def apply(self, /, func: Callable):
        """
        usage.alphalens: 1
        usage.dask: 36
        usage.koalas: 14
        usage.statsmodels: 6
        """
        ...

    @overload
    def apply(self, /, func: Callable):
        """
        usage.dask: 2
        usage.koalas: 4
        """
        ...

    @overload
    def apply(self, /, func: int, *args: Literal["v", "t"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def apply(self, /, func: Callable, *args: Literal["v", "t"]):
        """
        usage.dask: 11
        usage.koalas: 2
        """
        ...

    @overload
    def apply(self, /, func: Callable):
        """
        usage.koalas: 3
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
        func: Union[
            dask.utils.methodcaller, numpy.int64, int, Literal["sum"], Callable
        ],
        *args: Literal["v", "t"],
    ):
        """
        usage.alphalens: 1
        usage.dask: 64
        usage.koalas: 24
        usage.statsmodels: 6
        """
        ...

    def backfill(self, /):
        """
        usage.koalas: 3
        """
        ...

    def count(self, /):
        """
        usage.dask: 12
        usage.geopandas: 1
        usage.koalas: 6
        """
        ...

    @overload
    def cumcount(self, /, ascending: bool):
        """
        usage.koalas: 9
        """
        ...

    @overload
    def cumcount(self, /):
        """
        usage.dask: 3
        """
        ...

    def cumcount(self, /, ascending: bool = ...):
        """
        usage.dask: 3
        usage.koalas: 9
        """
        ...

    def cummax(self, /):
        """
        usage.koalas: 9
        """
        ...

    def cummin(self, /):
        """
        usage.koalas: 9
        """
        ...

    @overload
    def cumprod(self, /):
        """
        usage.dask: 3
        usage.koalas: 9
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
        usage.koalas: 9
        """
        ...

    @overload
    def cumsum(self, /):
        """
        usage.dask: 3
        usage.koalas: 9
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
        usage.koalas: 9
        """
        ...

    def describe(self, /):
        """
        usage.koalas: 2
        """
        ...

    def expanding(self, /, *args: Literal["v", "t"]):
        """
        usage.koalas: 8
        """
        ...

    def filter(self, /, func: Callable):
        """
        usage.koalas: 10
        """
        ...

    def first(self, /):
        """
        usage.dask: 12
        usage.koalas: 6
        """
        ...

    @overload
    def get_group(self, /, name: pandas._libs.tslibs.timedeltas.Timedelta):
        """
        usage.prophet: 1
        """
        ...

    @overload
    def get_group(self, /, name: numpy.int64):
        """
        usage.prophet: 1
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: numpy.float64):
        """
        usage.prophet: 1
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Literal["_nolegend_"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Literal["a"]):
        """
        usage.seaborn: 2
        """
        ...

    @overload
    def get_group(self, /, name: Literal["b"]):
        """
        usage.seaborn: 2
        """
        ...

    @overload
    def get_group(self, /, name: Literal["c"]):
        """
        usage.seaborn: 2
        """
        ...

    @overload
    def get_group(self, /, name: Literal["d"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Literal["e"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["b"], Literal["b"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["b"], Literal["a"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["b"], Literal["c"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["a"], Literal["b"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["a"], Literal["a"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["a"], Literal["c"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["c"], Literal["b"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["c"], Literal["a"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["c"], Literal["c"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["b"], numpy.int64]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["a"], numpy.int64]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["c"], numpy.int64]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["b"], numpy.int64, Literal["b"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["b"], numpy.int64, Literal["a"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["b"], numpy.int64, Literal["c"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["a"], numpy.int64, Literal["b"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["a"], numpy.int64, Literal["a"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["a"], numpy.int64, Literal["c"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["c"], numpy.int64, Literal["b"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["c"], numpy.int64, Literal["a"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["c"], numpy.int64, Literal["c"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["b"], numpy.int64, Literal["p"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["b"], numpy.int64, Literal["n"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["b"], numpy.int64, Literal["o"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["b"], numpy.int64, Literal["m"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["a"], numpy.int64, Literal["p"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["a"], numpy.int64, Literal["n"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["a"], numpy.int64, Literal["o"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["a"], numpy.int64, Literal["m"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["c"], numpy.int64, Literal["p"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["c"], numpy.int64, Literal["n"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["c"], numpy.int64, Literal["o"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["c"], numpy.int64, Literal["m"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Literal["x"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Literal["y"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Literal["z"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Literal["s"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Literal["f"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Literal["_"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["b"], Literal["_"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["a"], Literal["_"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["c"], Literal["_"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["b"], Literal["p"], Literal["p"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["b"], Literal["p"], Literal["n"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["b"], Literal["p"], Literal["o"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["b"], Literal["p"], Literal["m"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["b"], Literal["n"], Literal["p"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["b"], Literal["n"], Literal["n"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["b"], Literal["n"], Literal["o"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["b"], Literal["n"], Literal["m"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["b"], Literal["o"], Literal["p"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["b"], Literal["o"], Literal["n"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["b"], Literal["o"], Literal["o"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["b"], Literal["o"], Literal["m"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["b"], Literal["m"], Literal["p"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["b"], Literal["m"], Literal["n"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["b"], Literal["m"], Literal["o"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["b"], Literal["m"], Literal["m"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["a"], Literal["p"], Literal["p"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["a"], Literal["p"], Literal["n"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["a"], Literal["p"], Literal["o"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["a"], Literal["p"], Literal["m"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["a"], Literal["n"], Literal["p"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["a"], Literal["n"], Literal["n"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["a"], Literal["n"], Literal["o"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["a"], Literal["n"], Literal["m"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["a"], Literal["o"], Literal["p"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["a"], Literal["o"], Literal["n"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["a"], Literal["o"], Literal["o"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["a"], Literal["o"], Literal["m"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["a"], Literal["m"], Literal["p"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["a"], Literal["m"], Literal["n"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["a"], Literal["m"], Literal["o"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["a"], Literal["m"], Literal["m"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["c"], Literal["p"], Literal["p"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["c"], Literal["p"], Literal["n"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["c"], Literal["p"], Literal["o"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["c"], Literal["p"], Literal["m"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["c"], Literal["n"], Literal["p"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["c"], Literal["n"], Literal["n"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["c"], Literal["n"], Literal["o"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["c"], Literal["n"], Literal["m"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["c"], Literal["o"], Literal["p"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["c"], Literal["o"], Literal["n"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["c"], Literal["o"], Literal["o"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["c"], Literal["o"], Literal["m"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["c"], Literal["m"], Literal["p"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["c"], Literal["m"], Literal["n"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["c"], Literal["m"], Literal["o"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["c"], Literal["m"], Literal["m"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[int, int]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["b"], Literal["p"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["b"], Literal["n"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["b"], Literal["m"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["b"], Literal["o"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["a"], Literal["p"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["a"], Literal["n"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["a"], Literal["m"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["a"], Literal["o"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["c"], Literal["p"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["c"], Literal["n"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["c"], Literal["m"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["c"], Literal["o"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["b"], numpy.float64]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["a"], numpy.float64]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[Literal["c"], numpy.float64]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[int, float]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Tuple[numpy.float64, int]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Literal["12"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Literal["15"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Literal["3"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Literal["18"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Literal["10"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Literal["9"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Literal["11"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Literal["7"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Literal["16"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Literal["0"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Literal["13"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Literal["2"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Literal["8"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Literal["20"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Literal["4"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Literal["1"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Literal["6"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Literal["5"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Literal["14"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Literal["17"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Literal["19"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: int):
        """
        usage.dask: 4
        usage.geopandas: 1
        """
        ...

    def get_group(self, /, name: object):
        """
        usage.dask: 4
        usage.geopandas: 1
        usage.prophet: 3
        usage.seaborn: 140
        """
        ...

    def head(self, /, n: int):
        """
        usage.koalas: 17
        """
        ...

    def last(self, /):
        """
        usage.dask: 10
        usage.koalas: 6
        """
        ...

    def max(self, /):
        """
        usage.dask: 10
        usage.koalas: 6
        """
        ...

    def mean(self, /):
        """
        usage.alphalens: 2
        usage.dask: 15
        usage.koalas: 6
        usage.statsmodels: 2
        """
        ...

    def min(self, /):
        """
        usage.dask: 9
        usage.koalas: 6
        """
        ...

    @overload
    def nunique(self, /):
        """
        usage.dask: 1
        usage.koalas: 2
        """
        ...

    @overload
    def nunique(self, /, dropna: bool):
        """
        usage.koalas: 2
        """
        ...

    def nunique(self, /, dropna: bool = ...):
        """
        usage.dask: 1
        usage.koalas: 4
        """
        ...

    def pad(self, /):
        """
        usage.koalas: 3
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

    def quantile(self, /, q: List[float], interpolation: Literal["nearest"]):
        """
        usage.koalas: 1
        """
        ...

    def rank(self, /):
        """
        usage.koalas: 8
        """
        ...

    def rolling(self, /, *args: Literal["v", "t"]):
        """
        usage.koalas: 8
        """
        ...

    def shift(self, /):
        """
        usage.koalas: 5
        """
        ...

    def size(self, /):
        """
        usage.dask: 9
        usage.koalas: 5
        usage.modin: 2
        usage.prophet: 1
        """
        ...

    @overload
    def std(self, /):
        """
        usage.dask: 7
        usage.koalas: 6
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
        usage.koalas: 6
        """
        ...

    @overload
    def sum(self, /):
        """
        usage.alphalens: 1
        usage.dask: 26
        usage.geopandas: 1
        usage.koalas: 31
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
        usage.alphalens: 1
        usage.dask: 27
        usage.geopandas: 1
        usage.koalas: 31
        """
        ...

    @overload
    def transform(self, /, func: Callable):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def transform(self, /, func: Callable):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def transform(self, /, func: Callable):
        """
        usage.alphalens: 1
        usage.dask: 13
        usage.koalas: 12
        """
        ...

    @overload
    def transform(self, /, func: Callable):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def transform(self, /, func: Callable):
        """
        usage.pyjanitor: 1
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

    def transform(self, /, func: Union[Literal["sum"], Callable]):
        """
        usage.alphalens: 1
        usage.dask: 19
        usage.koalas: 14
        usage.pyjanitor: 2
        """
        ...

    @overload
    def var(self, /):
        """
        usage.dask: 5
        usage.koalas: 6
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
        usage.koalas: 6
        """
        ...


class NamedAgg:
    pass


class SeriesGroupBy:

    # usage.dask: 1
    __name__: ClassVar[object]

    # usage.koalas: 6
    fillna: object

    # usage.statsmodels: 1
    groups: object

    # usage.dask: 1
    idxmax: object

    # usage.dask: 1
    idxmin: object

    # usage.dask: 5
    obj: object

    def __iter__(self, /):
        """
        usage.alphalens: 1
        usage.dask: 2
        usage.geopandas: 1
        """
        ...

    @overload
    def aggregate(self, /, func: Literal["mean"]):
        """
        usage.dask: 3
        usage.seaborn: 1
        """
        ...

    @overload
    def aggregate(self, /, func: Callable):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def aggregate(self, /, func: List[Literal["max", "min"]]):
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
            List[Literal["max", "min", "mean", "sum"]],
            Literal["var", "sum", "mean"],
            Callable,
        ],
    ):
        """
        usage.dask: 10
        usage.geopandas: 1
        usage.seaborn: 1
        """
        ...

    def all(self, /):
        """
        usage.koalas: 1
        """
        ...

    def any(self, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def apply(self, /, func: Callable):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def apply(self, /, func: int, *args: Literal["v", "t"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def apply(self, /, func: Callable, *args: Literal["v", "t"]):
        """
        usage.alphalens: 19
        usage.koalas: 2
        """
        ...

    @overload
    def apply(self, /, func: Callable):
        """
        usage.alphalens: 1
        usage.dask: 16
        usage.geopandas: 2
        usage.koalas: 8
        usage.seaborn: 1
        """
        ...

    @overload
    def apply(self, /, func: Callable):
        """
        usage.dask: 2
        usage.koalas: 2
        """
        ...

    @overload
    def apply(self, /, func: Callable):
        """
        usage.koalas: 1
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
        self, /, func: Union[Literal["sum"], Callable, int], *args: Literal["v", "t"]
    ):
        """
        usage.alphalens: 20
        usage.dask: 20
        usage.geopandas: 2
        usage.koalas: 15
        usage.seaborn: 1
        """
        ...

    def backfill(self, /):
        """
        usage.koalas: 2
        """
        ...

    def count(self, /):
        """
        usage.alphalens: 1
        usage.dask: 15
        usage.koalas: 7
        """
        ...

    @overload
    def cumcount(self, /, ascending: bool):
        """
        usage.koalas: 6
        """
        ...

    @overload
    def cumcount(self, /):
        """
        usage.dask: 2
        """
        ...

    def cumcount(self, /, ascending: bool = ...):
        """
        usage.dask: 2
        usage.koalas: 6
        """
        ...

    def cummax(self, /):
        """
        usage.koalas: 6
        """
        ...

    def cummin(self, /):
        """
        usage.koalas: 6
        """
        ...

    def cumprod(self, /):
        """
        usage.dask: 3
        usage.koalas: 6
        """
        ...

    def cumsum(self, /):
        """
        usage.dask: 3
        usage.koalas: 6
        """
        ...

    def expanding(self, /, *args: Literal["v", "t"]):
        """
        usage.koalas: 7
        """
        ...

    def filter(self, /, func: Callable):
        """
        usage.koalas: 6
        """
        ...

    def first(self, /):
        """
        usage.dask: 14
        usage.koalas: 7
        usage.xarray: 1
        """
        ...

    @overload
    def get_group(self, /, name: Literal["Thur"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Literal["Fri"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Literal["Sat"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Literal["Sun"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Literal["Dinner"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Literal["Lunch"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Literal["Male"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Literal["Female"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Literal["1 min"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Literal["15 min"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Literal["30 min"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Literal["yes"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Literal["no"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Literal["Southampton"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Literal["Cherbourg"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Literal["Queenstown"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Literal["man"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Literal["woman"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Literal["child"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: numpy.int64):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Literal["m"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Literal["n"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Literal["_nolegend_"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: Literal["a"]):
        """
        usage.seaborn: 2
        """
        ...

    @overload
    def get_group(self, /, name: Literal["b"]):
        """
        usage.seaborn: 2
        """
        ...

    @overload
    def get_group(self, /, name: Literal["c"]):
        """
        usage.seaborn: 2
        """
        ...

    @overload
    def get_group(self, /, name: Literal["d"]):
        """
        usage.seaborn: 2
        """
        ...

    @overload
    def get_group(self, /, name: Literal["e"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get_group(self, /, name: int):
        """
        usage.dask: 3
        """
        ...

    def get_group(self, /, name: Union[int, numpy.int64, str]):
        """
        usage.dask: 3
        usage.seaborn: 32
        """
        ...

    def head(self, /, n: int):
        """
        usage.koalas: 11
        """
        ...

    def last(self, /):
        """
        usage.dask: 10
        usage.koalas: 7
        """
        ...

    def max(self, /):
        """
        usage.dask: 11
        usage.koalas: 7
        """
        ...

    def mean(self, /):
        """
        usage.dask: 13
        usage.koalas: 7
        usage.seaborn: 2
        """
        ...

    def min(self, /):
        """
        usage.dask: 10
        usage.koalas: 7
        """
        ...

    @overload
    def nunique(self, /):
        """
        usage.dask: 14
        usage.koalas: 1
        """
        ...

    @overload
    def nunique(self, /, dropna: bool):
        """
        usage.koalas: 1
        """
        ...

    def nunique(self, /, dropna: bool = ...):
        """
        usage.dask: 14
        usage.koalas: 2
        """
        ...

    def pad(self, /):
        """
        usage.koalas: 2
        """
        ...

    def prod(self, /):
        """
        usage.dask: 9
        """
        ...

    def rank(self, /):
        """
        usage.alphalens: 1
        usage.koalas: 3
        """
        ...

    def rolling(self, /, *args: Literal["v", "t"]):
        """
        usage.koalas: 7
        """
        ...

    def shift(self, /):
        """
        usage.koalas: 7
        """
        ...

    def size(self, /):
        """
        usage.dask: 10
        usage.koalas: 1
        """
        ...

    @overload
    def std(self, /):
        """
        usage.dask: 7
        usage.koalas: 8
        usage.seaborn: 1
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
        usage.koalas: 8
        usage.seaborn: 1
        """
        ...

    def sum(self, /):
        """
        usage.dask: 20
        usage.koalas: 24
        """
        ...

    @overload
    def transform(self, /, func: Callable):
        """
        usage.dask: 13
        usage.koalas: 7
        usage.statsmodels: 1
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

    def transform(self, /, func: Union[Literal["sum"], Callable]):
        """
        usage.dask: 19
        usage.koalas: 7
        usage.statsmodels: 1
        """
        ...

    @overload
    def value_counts(self, /):
        """
        usage.dask: 2
        usage.koalas: 4
        """
        ...

    @overload
    def value_counts(self, /, sort: bool, ascending: bool):
        """
        usage.koalas: 2
        """
        ...

    def value_counts(self, /, sort: bool = ..., ascending: bool = ...):
        """
        usage.dask: 2
        usage.koalas: 6
        """
        ...

    @overload
    def var(self, /):
        """
        usage.dask: 5
        usage.koalas: 7
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
        usage.koalas: 7
        """
        ...
