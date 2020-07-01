from typing import *


class Series:
    def __init__(
        data: List[
            Literal[
                ("a", "b", "c", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
            ]
        ]
    ):
        "\n    usage.dask: 5\n    "
        ...

    # usage.dask: 5
    __name__: ClassVar[object]

    # usage.dask: 4
    __module__: ClassVar[object]

    @classmethod
    def __ne__(_0: Type[pandas.core.series.Series], /):
        "\n    usage.dask: 2\n    "
        ...

    # usage.xarray: 4
    # usage.dask: 2
    dt: object

    # usage.xarray: 18
    # usage.dask: 40
    values: object

    # usage.xarray: 23
    # usage.dask: 80
    index: object

    # usage.xarray: 5
    # usage.dask: 42
    name: Union[None, str]

    # usage.xarray: 1
    # usage.dask: 19
    loc: object

    # usage.dask: 65
    dtype: object

    # usage.dask: 31
    iloc: object

    # usage.dask: 1
    _data: object

    # usage.dask: 28
    cat: object

    # usage.dask: 25
    str: object

    # usage.dask: 2
    empty: object

    # usage.dask: 1
    div: object

    # usage.dask: 1
    divide: object

    # usage.dask: 1
    rdiv: object

    # usage.dask: 6
    __class__: object

    # usage.dask: 7
    shape: object

    # usage.dask: 6
    ndim: object

    # usage.dask: 3
    _values: object

    # usage.dask: 2
    size: object

    # usage.dask: 2
    nbytes: object

    def rank(self: object, /, method: Literal["dense"], ascending: bool):
        "\n    usage.xarray: 1\n    "
        ...

    def astype(
        self: object,
        /,
        dtype: Union[
            type, str, pandas.core.dtypes.dtypes.CategoricalDtype, numpy.dtype
        ],
    ):
        "\n    usage.xarray: 1\n    usage.dask: 52\n    "
        ...

    def median(self: object, /):
        "\n    usage.xarray: 1\n    "
        ...

    def reset_index(self: object, /):
        "\n    usage.xarray: 2\n    usage.dask: 6\n    "
        ...

    def unstack(self: object, /):
        "\n    usage.xarray: 1\n    "
        ...

    def groupby(
        self: object,
        /,
        level: Union[List[int], int] = ...,
        sort: bool = ...,
        by: object = ...,
        group_keys: bool = ...,
    ):
        "\n    usage.xarray: 1\n    usage.dask: 64\n    "
        ...

    def isnull(self: object, /):
        "\n    usage.xarray: 1\n    usage.dask: 5\n    "
        ...

    def any(self: object, /, axis: int = ..., skipna: bool = ...):
        "\n    usage.xarray: 1\n    usage.dask: 8\n    "
        ...

    def resample(
        self: object,
        /,
        rule: object,
        closed: Union[None, Literal[("left", "right")]] = ...,
        label: Union[None, Literal[("left", "right")]] = ...,
    ):
        "\n    usage.xarray: 14\n    usage.dask: 83\n    "
        ...

    def dropna(self: object, /):
        "\n    usage.xarray: 1\n    usage.dask: 7\n    "
        ...

    def to_frame(self: object, /):
        "\n    usage.xarray: 2\n    usage.dask: 26\n    "
        ...

    def equals(self: object, /, other: pandas.core.series.Series):
        "\n    usage.xarray: 1\n    usage.dask: 3\n    "
        ...

    def __setitem__(
        self: object,
        _0: Union[pandas.core.series.Series, int],
        _1: Union[int, float],
        /,
    ):
        "\n    usage.xarray: 2\n    usage.dask: 3\n    "
        ...

    def shift(self: object, /, periods: int = ..., freq: object = ...):
        "\n    usage.xarray: 1\n    usage.dask: 32\n    "
        ...

    def rolling(
        self: object,
        /,
        window: Union[Literal[("3S", "2S", "1S")], int, pandas.tseries.offsets.Second],
        min_periods: Union[None, int] = ...,
        center: bool = ...,
        win_type: None = ...,
        axis: int = ...,
    ):
        "\n    usage.xarray: 3\n    usage.dask: 24\n    "
        ...

    def iteritems(self: object, /):
        "\n    usage.xarray: 1\n    usage.dask: 4\n    "
        ...

    def __getitem__(self: object, _0: object, /):
        "\n    usage.xarray: 2\n    usage.dask: 83\n    "
        ...

    def sum(
        self: object,
        /,
        axis: Union[Literal["columns"], None, int] = ...,
        skipna: bool = ...,
    ):
        "\n    usage.xarray: 2\n    usage.dask: 42\n    "
        ...

    def min(
        self: object,
        /,
        axis: Union[Literal["columns"], None, int] = ...,
        skipna: bool = ...,
    ):
        "\n    usage.xarray: 1\n    usage.dask: 15\n    "
        ...

    def max(
        self: object,
        /,
        axis: Union[Literal["columns"], None, int] = ...,
        skipna: bool = ...,
    ):
        "\n    usage.xarray: 1\n    usage.dask: 19\n    "
        ...

    def mean(
        self: object,
        /,
        axis: Union[Literal["columns"], None, int] = ...,
        skipna: bool = ...,
    ):
        "\n    usage.xarray: 1\n    usage.dask: 25\n    "
        ...

    def var(
        self: object,
        /,
        axis: Union[Literal["columns"], None, int] = ...,
        skipna: Union[None, bool] = ...,
        ddof: int = ...,
    ):
        "\n    usage.xarray: 1\n    usage.dask: 14\n    "
        ...

    def prod(
        self: object,
        /,
        axis: Union[Literal["columns"], None, int] = ...,
        skipna: bool = ...,
        min_count: int = ...,
    ):
        "\n    usage.xarray: 1\n    usage.dask: 10\n    "
        ...

    def __eq__(
        self: object,
        _0: Union[
            int,
            pandas.core.series.Series,
            dask.dataframe.core.Series,
            Literal[("object", "a", "i8", "category")],
            Type[numpy.float64],
        ],
        /,
    ):
        "\n    usage.sklearn: 1\n    usage.dask: 48\n    "
        ...

    def to_dict(self: object, /):
        "\n    usage.dask: 5\n    "
        ...

    def all(self: object, /, axis: int = ..., skipna: bool = ...):
        "\n    usage.dask: 24\n    "
        ...

    def unique(self: object, /):
        "\n    usage.dask: 9\n    "
        ...

    def tolist(self: object, /):
        "\n    usage.dask: 3\n    "
        ...

    def memory_usage(self: object, /, index: bool):
        "\n    usage.dask: 6\n    "
        ...

    def __iter__(self: object, /):
        "\n    usage.dask: 5\n    "
        ...

    def searchsorted(
        self: object, /, value: pandas.core.series.Series, side: Literal["right"]
    ):
        "\n    usage.dask: 1\n    "
        ...

    def __ge__(self: object, _0: object, /):
        "\n    usage.dask: 22\n    "
        ...

    def __invert__(self: object, /):
        "\n    usage.dask: 2\n    "
        ...

    def __mod__(self: object, _0: Union[pandas.core.series.Series, int], /):
        "\n    usage.dask: 7\n    "
        ...

    def __mul__(self: object, _0: Union[int, float, pandas.core.series.Series], /):
        "\n    usage.dask: 8\n    "
        ...

    def __truediv__(self: object, _0: Union[int, float, pandas.core.series.Series], /):
        "\n    usage.dask: 12\n    "
        ...

    def drop_duplicates(self: object, /):
        "\n    usage.dask: 12\n    "
        ...

    def count(self: object, /, *, axis: Union[Literal["columns"], int] = ...):
        "\n    usage.dask: 10\n    "
        ...

    def sort_values(self: object, /):
        "\n    usage.dask: 4\n    "
        ...

    def sort_index(self: object, /):
        "\n    usage.dask: 4\n    "
        ...

    def __add__(self: object, _0: object, /):
        "\n    usage.dask: 57\n    "
        ...

    def __radd__(
        self: object,
        _0: Union[
            numpy.ndarray,
            dask.dataframe.core.Series,
            pandas.core.series.Series,
            int,
            dask.dataframe.core.Scalar,
        ],
        /,
    ):
        "\n    usage.dask: 20\n    "
        ...

    def __rmul__(
        self: object,
        _0: Union[dask.dataframe.core.Series, pandas.core.series.Series, int],
        /,
    ):
        "\n    usage.dask: 6\n    "
        ...

    def __sub__(
        self: object, _0: Union[numpy.float64, pandas.core.series.Series, int], /
    ):
        "\n    usage.dask: 20\n    "
        ...

    def __rsub__(
        self: object,
        _0: Union[
            pandas.core.frame.DataFrame,
            int,
            pandas.core.series.Series,
            dask.dataframe.core.Series,
        ],
        /,
    ):
        "\n    usage.dask: 13\n    "
        ...

    def __rtruediv__(
        self: object,
        _0: Union[dask.dataframe.core.Series, pandas.core.series.Series, int],
        /,
    ):
        "\n    usage.dask: 11\n    "
        ...

    def __floordiv__(self: object, _0: Union[float, pandas.core.series.Series, int], /):
        "\n    usage.dask: 5\n    "
        ...

    def __rfloordiv__(
        self: object,
        _0: Union[dask.dataframe.core.Series, pandas.core.series.Series, int],
        /,
    ):
        "\n    usage.dask: 3\n    "
        ...

    def __pow__(self: object, _0: Union[float, pandas.core.series.Series, int], /):
        "\n    usage.dask: 8\n    "
        ...

    def __rpow__(
        self: object,
        _0: Union[dask.dataframe.core.Series, pandas.core.series.Series, int],
        /,
    ):
        "\n    usage.dask: 3\n    "
        ...

    def __rmod__(
        self: object,
        _0: Union[dask.dataframe.core.Series, pandas.core.series.Series, int],
        /,
    ):
        "\n    usage.dask: 3\n    "
        ...

    def __and__(self: object, _0: Union[bool, pandas.core.series.Series], /):
        "\n    usage.dask: 7\n    "
        ...

    def __rand__(
        self: object,
        _0: Union[dask.dataframe.core.Series, pandas.core.series.Series, bool],
        /,
    ):
        "\n    usage.dask: 8\n    "
        ...

    def __or__(self: object, _0: Union[bool, pandas.core.series.Series], /):
        "\n    usage.dask: 5\n    "
        ...

    def __ror__(
        self: object,
        _0: Union[dask.dataframe.core.Series, pandas.core.series.Series, bool],
        /,
    ):
        "\n    usage.dask: 6\n    "
        ...

    def __xor__(self: object, _0: Union[bool, pandas.core.series.Series], /):
        "\n    usage.dask: 3\n    "
        ...

    def __rxor__(
        self: object,
        _0: Union[dask.dataframe.core.Series, pandas.core.series.Series, bool],
        /,
    ):
        "\n    usage.dask: 4\n    "
        ...

    def __gt__(
        self: object,
        _0: Union[numpy.int64, int, pandas.core.series.Series, numpy.float64],
        /,
    ):
        "\n    usage.dask: 60\n    "
        ...

    def __lt__(
        self: object,
        _0: Union[
            pandas._libs.tslibs.timedeltas.Timedelta,
            dask.dataframe.core.Series,
            pandas.core.series.Series,
            int,
            pandas.core.frame.DataFrame,
        ],
        /,
    ):
        "\n    usage.dask: 7\n    "
        ...

    def __le__(self: object, _0: object, /):
        "\n    usage.dask: 21\n    "
        ...

    def __ne__(
        self: object,
        _0: Union[dask.dataframe.core.Series, pandas.core.series.Series, int],
        /,
    ):
        "\n    usage.dask: 5\n    "
        ...

    def lt(self: object, /, other: Union[pandas.core.series.Series, int]):
        "\n    usage.dask: 3\n    "
        ...

    def gt(self: object, /, other: Union[pandas.core.series.Series, int]):
        "\n    usage.dask: 3\n    "
        ...

    def le(self: object, /, other: Union[pandas.core.series.Series, int]):
        "\n    usage.dask: 3\n    "
        ...

    def ge(self: object, /, other: Union[pandas.core.series.Series, int]):
        "\n    usage.dask: 3\n    "
        ...

    def ne(self: object, /, other: Union[pandas.core.series.Series, int]):
        "\n    usage.dask: 3\n    "
        ...

    def eq(self: object, /, other: Union[pandas.core.series.Series, int]):
        "\n    usage.dask: 3\n    "
        ...

    def __neg__(self: object, /):
        "\n    usage.dask: 3\n    "
        ...

    def add(self: object, /, other: Union[pandas.core.series.Series, int]):
        "\n    usage.dask: 7\n    "
        ...

    def sub(
        self: object, /, other: Union[int, pandas.core.series.Series], fill_value: int
    ):
        "\n    usage.dask: 2\n    "
        ...

    def mul(self: object, /, other: Union[pandas.core.series.Series, int]):
        "\n    usage.dask: 4\n    "
        ...

    def truediv(
        self: object, /, other: Union[int, pandas.core.series.Series], fill_value: int
    ):
        "\n    usage.dask: 6\n    "
        ...

    def floordiv(
        self: object, /, other: Union[int, pandas.core.series.Series], fill_value: int
    ):
        "\n    usage.dask: 2\n    "
        ...

    def pow(
        self: object, /, other: Union[int, pandas.core.series.Series], fill_value: int
    ):
        "\n    usage.dask: 2\n    "
        ...

    def mod(
        self: object, /, other: Union[int, pandas.core.series.Series], fill_value: int
    ):
        "\n    usage.dask: 2\n    "
        ...

    def radd(
        self: object, /, other: Union[int, pandas.core.series.Series], fill_value: int
    ):
        "\n    usage.dask: 2\n    "
        ...

    def rsub(
        self: object, /, other: Union[int, pandas.core.series.Series], fill_value: int
    ):
        "\n    usage.dask: 2\n    "
        ...

    def rmul(
        self: object, /, other: Union[int, pandas.core.series.Series], fill_value: int
    ):
        "\n    usage.dask: 2\n    "
        ...

    def rtruediv(
        self: object, /, other: Union[int, pandas.core.series.Series], fill_value: int
    ):
        "\n    usage.dask: 4\n    "
        ...

    def rpow(
        self: object, /, other: Union[int, pandas.core.series.Series], fill_value: int
    ):
        "\n    usage.dask: 2\n    "
        ...

    def rmod(
        self: object, /, other: Union[int, pandas.core.series.Series], fill_value: int
    ):
        "\n    usage.dask: 2\n    "
        ...

    def std(
        self: object,
        /,
        axis: Union[Literal["columns"], None, int] = ...,
        skipna: bool = ...,
        ddof: int = ...,
    ):
        "\n    usage.dask: 12\n    "
        ...

    def sem(
        self: object,
        /,
        axis: Union[Literal["columns"], int] = ...,
        skipna: Union[bool, None] = ...,
        ddof: int = ...,
    ):
        "\n    usage.dask: 9\n    "
        ...

    def nunique(self: object, /):
        "\n    usage.dask: 5\n    "
        ...

    def value_counts(self: object, /):
        "\n    usage.dask: 9\n    "
        ...

    def rename(self: object, /, *, inplace: bool = ...):
        "\n    usage.dask: 23\n    "
        ...

    def copy(self: object, /):
        "\n    usage.dask: 3\n    "
        ...

    def head(self: object, /, n: int):
        "\n    usage.dask: 7\n    "
        ...

    def tail(self: object, /, n: int):
        "\n    usage.dask: 4\n    "
        ...

    def quantile(self: object, /):
        "\n    usage.dask: 7\n    "
        ...

    def describe(
        self: object,
        /,
        include: List[
            Union[Type[numpy.timedelta64], Literal[("number", "object")]]
        ] = ...,
        exclude: None = ...,
    ):
        "\n    usage.dask: 7\n    "
        ...

    def apply(
        self: object,
        /,
        func: Callable,
        convert_dtype: bool = ...,
        args: Tuple[None, ...] = ...,
    ):
        "\n    usage.dask: 9\n    "
        ...

    def where(self: object, /, cond: pandas.core.series.Series):
        "\n    usage.dask: 8\n    "
        ...

    def cumsum(self: object, /, axis: None = ..., skipna: bool = ...):
        "\n    usage.dask: 5\n    "
        ...

    def cumprod(self: object, /, axis: None = ..., skipna: bool = ...):
        "\n    usage.dask: 4\n    "
        ...

    def cummin(self: object, /, axis: None = ..., skipna: bool = ...):
        "\n    usage.dask: 4\n    "
        ...

    def cummax(self: object, /, axis: None = ..., skipna: bool = ...):
        "\n    usage.dask: 4\n    "
        ...

    def notna(self: object, /):
        "\n    usage.dask: 1\n    "
        ...

    def clip(
        self: object,
        /,
        lower: Union[None, int, float] = ...,
        upper: Union[float, int, None] = ...,
    ):
        "\n    usage.dask: 13\n    "
        ...

    def squeeze(self: object, /):
        "\n    usage.dask: 1\n    "
        ...

    def mask(self: object, /, cond: pandas.core.series.Series):
        "\n    usage.dask: 4\n    "
        ...

    def to_string(self: object, /, max_rows: int):
        "\n    usage.dask: 1\n    "
        ...

    def isin(self: object, /, values: Union[pandas.core.series.Series, List[int]]):
        "\n    usage.dask: 6\n    "
        ...

    def map(
        self: object,
        /,
        arg: Union[Callable, pandas.core.series.Series, Dict[numpy.int64, numpy.int64]],
    ):
        "\n    usage.dask: 15\n    "
        ...

    def align(
        self: object,
        /,
        other: pandas.core.series.Series,
        join: Literal[("right", "left", "outer", "inner")],
        axis: Union[int, None] = ...,
        fill_value: Union[None, int] = ...,
    ):
        "\n    usage.dask: 20\n    "
        ...

    def combine(
        self: object,
        /,
        other: pandas.core.series.Series,
        func: Callable,
        fill_value: Union[None, int],
    ):
        "\n    usage.dask: 6\n    "
        ...

    def combine_first(self: object, /, other: pandas.core.series.Series):
        "\n    usage.dask: 5\n    "
        ...

    def round(self: object, /):
        "\n    usage.dask: 2\n    "
        ...

    def between(self: object, /, left: int, right: int):
        "\n    usage.dask: 2\n    "
        ...

    def notnull(self: object, /):
        "\n    usage.dask: 3\n    "
        ...

    def fillna(
        self: object,
        /,
        value: Union[pandas.core.series.Series, numpy.float64, int, None] = ...,
        method: Union[None, Literal[("bfill", "ffill", "pad")]] = ...,
        axis: int = ...,
        limit: Union[None, int] = ...,
    ):
        "\n    usage.dask: 23\n    "
        ...

    def nlargest(self: object, /, n: int):
        "\n    usage.dask: 4\n    "
        ...

    def abs(self: object, /):
        "\n    usage.dask: 3\n    "
        ...

    def cov(self: object, /, other: pandas.core.series.Series):
        "\n    usage.dask: 2\n    "
        ...

    def replace(
        self: object,
        /,
        to_replace: Union[Dict[int, int], int, Literal["c"]],
        value: Union[None, float, int] = ...,
        regex: bool = ...,
    ):
        "\n    usage.dask: 5\n    "
        ...

    def autocorr(self: object, /, lag: int):
        "\n    usage.dask: 4\n    "
        ...

    def nsmallest(self: object, /, n: int):
        "\n    usage.dask: 2\n    "
        ...

    def diff(self: object, /):
        "\n    usage.dask: 7\n    "
        ...

    def first(self: object, /, offset: str):
        "\n    usage.dask: 24\n    "
        ...

    def last(self: object, /, offset: str):
        "\n    usage.dask: 8\n    "
        ...

    def explode(self: object, /):
        "\n    usage.dask: 5\n    "
        ...

    def __itruediv__(self: object, _0: pandas.core.series.Series, /):
        "\n    usage.dask: 1\n    "
        ...

    def reindex(
        self: object,
        /,
        index: Union[
            pandas.core.indexes.datetimes.DatetimeIndex,
            pandas.core.indexes.multi.MultiIndex,
            pandas.core.indexes.numeric.Int64Index,
            numpy.ndarray,
        ],
    ):
        "\n    usage.dask: 8\n    "
        ...

    def idxmax(self: object, /):
        "\n    usage.dask: 1\n    "
        ...

    def items(self: object, /):
        "\n    usage.dask: 1\n    "
        ...

    def append(self: object, /, to_append: pandas.core.series.Series):
        "\n    usage.dask: 2\n    "
        ...

    def __array_wrap__(self: object, /, result: numpy.ndarray):
        "\n    usage.dask: 3\n    "
        ...
