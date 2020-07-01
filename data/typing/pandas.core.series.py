from typing import *


class Series:
    def __init__(
        data: List[
            Literal["a", "b", "c", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"]
        ]
    ):
        """
        usage.dask: 5
        """
        ...

    # usage.dask: 5
    __name__: ClassVar[object]

    # usage.dask: 4
    __module__: ClassVar[object]

    @classmethod
    def __ne__(_0: Type[pandas.core.series.Series], /):
        """
        usage.dask: 2
        """
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
        """
        usage.xarray: 1
        """
        ...

    def astype(
        self: object,
        /,
        dtype: Union[
            type, str, pandas.core.dtypes.dtypes.CategoricalDtype, numpy.dtype
        ],
    ):
        """
        usage.xarray: 1
        usage.dask: 52
        """
        ...

    def median(self: object, /):
        """
        usage.xarray: 1
        """
        ...

    def reset_index(self: object, /):
        """
        usage.xarray: 2
        usage.dask: 6
        """
        ...

    def unstack(self: object, /):
        """
        usage.xarray: 1
        """
        ...

    def groupby(
        self: object,
        /,
        level: Union[List[int], int] = ...,
        sort: bool = ...,
        by: object = ...,
        group_keys: bool = ...,
    ):
        """
        usage.xarray: 1
        usage.dask: 64
        """
        ...

    def isnull(self: object, /):
        """
        usage.xarray: 1
        usage.dask: 5
        """
        ...

    def any(self: object, /, axis: int = ..., skipna: bool = ...):
        """
        usage.xarray: 1
        usage.dask: 8
        """
        ...

    def resample(
        self: object,
        /,
        rule: object,
        closed: Union[None, Literal["left", "right"]] = ...,
        label: Union[None, Literal["left", "right"]] = ...,
    ):
        """
        usage.xarray: 14
        usage.dask: 83
        """
        ...

    def dropna(self: object, /):
        """
        usage.xarray: 1
        usage.dask: 7
        """
        ...

    def to_frame(self: object, /):
        """
        usage.xarray: 2
        usage.dask: 26
        """
        ...

    def equals(self: object, /, other: pandas.core.series.Series):
        """
        usage.xarray: 1
        usage.dask: 3
        """
        ...

    def __setitem__(
        self: object,
        _0: Union[pandas.core.series.Series, int],
        _1: Union[int, float],
        /,
    ):
        """
        usage.xarray: 2
        usage.dask: 3
        """
        ...

    def shift(self: object, /, periods: int = ..., freq: object = ...):
        """
        usage.xarray: 1
        usage.dask: 32
        """
        ...

    def rolling(
        self: object,
        /,
        window: Union[Literal["3S", "2S", "1S"], int, pandas.tseries.offsets.Second],
        min_periods: Union[None, int] = ...,
        center: bool = ...,
        win_type: None = ...,
        axis: int = ...,
    ):
        """
        usage.xarray: 3
        usage.dask: 24
        """
        ...

    def iteritems(self: object, /):
        """
        usage.xarray: 1
        usage.dask: 4
        """
        ...

    def __getitem__(self: object, _0: object, /):
        """
        usage.xarray: 2
        usage.dask: 83
        """
        ...

    def sum(
        self: object,
        /,
        axis: Union[Literal["columns"], None, int] = ...,
        skipna: bool = ...,
    ):
        """
        usage.xarray: 2
        usage.dask: 42
        """
        ...

    def min(
        self: object,
        /,
        axis: Union[Literal["columns"], None, int] = ...,
        skipna: bool = ...,
    ):
        """
        usage.xarray: 1
        usage.dask: 15
        """
        ...

    def max(
        self: object,
        /,
        axis: Union[Literal["columns"], None, int] = ...,
        skipna: bool = ...,
    ):
        """
        usage.xarray: 1
        usage.dask: 19
        """
        ...

    def mean(
        self: object,
        /,
        axis: Union[Literal["columns"], None, int] = ...,
        skipna: bool = ...,
    ):
        """
        usage.xarray: 1
        usage.dask: 25
        """
        ...

    def var(
        self: object,
        /,
        axis: Union[Literal["columns"], None, int] = ...,
        skipna: Union[None, bool] = ...,
        ddof: int = ...,
    ):
        """
        usage.xarray: 1
        usage.dask: 14
        """
        ...

    def prod(
        self: object,
        /,
        axis: Union[Literal["columns"], None, int] = ...,
        skipna: bool = ...,
        min_count: int = ...,
    ):
        """
        usage.xarray: 1
        usage.dask: 10
        """
        ...

    def __eq__(
        self: object,
        _0: Union[
            int,
            pandas.core.series.Series,
            dask.dataframe.core.Series,
            Literal["object", "a", "i8", "category"],
            Type[numpy.float64],
        ],
        /,
    ):
        """
        usage.sklearn: 1
        usage.dask: 48
        """
        ...

    def to_dict(self: object, /):
        """
        usage.dask: 5
        """
        ...

    def all(self: object, /, axis: int = ..., skipna: bool = ...):
        """
        usage.dask: 24
        """
        ...

    def unique(self: object, /):
        """
        usage.dask: 9
        """
        ...

    def tolist(self: object, /):
        """
        usage.dask: 3
        """
        ...

    def memory_usage(self: object, /, index: bool):
        """
        usage.dask: 6
        """
        ...

    def __iter__(self: object, /):
        """
        usage.dask: 5
        """
        ...

    def searchsorted(
        self: object, /, value: pandas.core.series.Series, side: Literal["right"]
    ):
        """
        usage.dask: 1
        """
        ...

    def __ge__(self: object, _0: object, /):
        """
        usage.dask: 22
        """
        ...

    def __invert__(self: object, /):
        """
        usage.dask: 2
        """
        ...

    def __mod__(self: object, _0: Union[pandas.core.series.Series, int], /):
        """
        usage.dask: 7
        """
        ...

    def __mul__(self: object, _0: Union[int, float, pandas.core.series.Series], /):
        """
        usage.dask: 8
        """
        ...

    def __truediv__(self: object, _0: Union[int, float, pandas.core.series.Series], /):
        """
        usage.dask: 12
        """
        ...

    def drop_duplicates(self: object, /):
        """
        usage.dask: 12
        """
        ...

    def count(self: object, /, *, axis: Union[Literal["columns"], int] = ...):
        """
        usage.dask: 10
        """
        ...

    def sort_values(self: object, /):
        """
        usage.dask: 4
        """
        ...

    def sort_index(self: object, /):
        """
        usage.dask: 4
        """
        ...

    def __add__(self: object, _0: object, /):
        """
        usage.dask: 57
        """
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
        """
        usage.dask: 20
        """
        ...

    def __rmul__(
        self: object,
        _0: Union[dask.dataframe.core.Series, pandas.core.series.Series, int],
        /,
    ):
        """
        usage.dask: 6
        """
        ...

    def __sub__(
        self: object, _0: Union[numpy.float64, pandas.core.series.Series, int], /
    ):
        """
        usage.dask: 20
        """
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
        """
        usage.dask: 13
        """
        ...

    def __rtruediv__(
        self: object,
        _0: Union[dask.dataframe.core.Series, pandas.core.series.Series, int],
        /,
    ):
        """
        usage.dask: 11
        """
        ...

    def __floordiv__(self: object, _0: Union[float, pandas.core.series.Series, int], /):
        """
        usage.dask: 5
        """
        ...

    def __rfloordiv__(
        self: object,
        _0: Union[dask.dataframe.core.Series, pandas.core.series.Series, int],
        /,
    ):
        """
        usage.dask: 3
        """
        ...

    def __pow__(self: object, _0: Union[float, pandas.core.series.Series, int], /):
        """
        usage.dask: 8
        """
        ...

    def __rpow__(
        self: object,
        _0: Union[dask.dataframe.core.Series, pandas.core.series.Series, int],
        /,
    ):
        """
        usage.dask: 3
        """
        ...

    def __rmod__(
        self: object,
        _0: Union[dask.dataframe.core.Series, pandas.core.series.Series, int],
        /,
    ):
        """
        usage.dask: 3
        """
        ...

    def __and__(self: object, _0: Union[bool, pandas.core.series.Series], /):
        """
        usage.dask: 7
        """
        ...

    def __rand__(
        self: object,
        _0: Union[dask.dataframe.core.Series, pandas.core.series.Series, bool],
        /,
    ):
        """
        usage.dask: 8
        """
        ...

    def __or__(self: object, _0: Union[bool, pandas.core.series.Series], /):
        """
        usage.dask: 5
        """
        ...

    def __ror__(
        self: object,
        _0: Union[dask.dataframe.core.Series, pandas.core.series.Series, bool],
        /,
    ):
        """
        usage.dask: 6
        """
        ...

    def __xor__(self: object, _0: Union[bool, pandas.core.series.Series], /):
        """
        usage.dask: 3
        """
        ...

    def __rxor__(
        self: object,
        _0: Union[dask.dataframe.core.Series, pandas.core.series.Series, bool],
        /,
    ):
        """
        usage.dask: 4
        """
        ...

    def __gt__(
        self: object,
        _0: Union[numpy.int64, int, pandas.core.series.Series, numpy.float64],
        /,
    ):
        """
        usage.dask: 60
        """
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
        """
        usage.dask: 7
        """
        ...

    def __le__(self: object, _0: object, /):
        """
        usage.dask: 21
        """
        ...

    def __ne__(
        self: object,
        _0: Union[dask.dataframe.core.Series, pandas.core.series.Series, int],
        /,
    ):
        """
        usage.dask: 5
        """
        ...

    def lt(self: object, /, other: Union[pandas.core.series.Series, int]):
        """
        usage.dask: 3
        """
        ...

    def gt(self: object, /, other: Union[pandas.core.series.Series, int]):
        """
        usage.dask: 3
        """
        ...

    def le(self: object, /, other: Union[pandas.core.series.Series, int]):
        """
        usage.dask: 3
        """
        ...

    def ge(self: object, /, other: Union[pandas.core.series.Series, int]):
        """
        usage.dask: 3
        """
        ...

    def ne(self: object, /, other: Union[pandas.core.series.Series, int]):
        """
        usage.dask: 3
        """
        ...

    def eq(self: object, /, other: Union[pandas.core.series.Series, int]):
        """
        usage.dask: 3
        """
        ...

    def __neg__(self: object, /):
        """
        usage.dask: 3
        """
        ...

    def add(self: object, /, other: Union[pandas.core.series.Series, int]):
        """
        usage.dask: 7
        """
        ...

    def sub(
        self: object, /, other: Union[int, pandas.core.series.Series], fill_value: int
    ):
        """
        usage.dask: 2
        """
        ...

    def mul(self: object, /, other: Union[pandas.core.series.Series, int]):
        """
        usage.dask: 4
        """
        ...

    def truediv(
        self: object, /, other: Union[int, pandas.core.series.Series], fill_value: int
    ):
        """
        usage.dask: 6
        """
        ...

    def floordiv(
        self: object, /, other: Union[int, pandas.core.series.Series], fill_value: int
    ):
        """
        usage.dask: 2
        """
        ...

    def pow(
        self: object, /, other: Union[int, pandas.core.series.Series], fill_value: int
    ):
        """
        usage.dask: 2
        """
        ...

    def mod(
        self: object, /, other: Union[int, pandas.core.series.Series], fill_value: int
    ):
        """
        usage.dask: 2
        """
        ...

    def radd(
        self: object, /, other: Union[int, pandas.core.series.Series], fill_value: int
    ):
        """
        usage.dask: 2
        """
        ...

    def rsub(
        self: object, /, other: Union[int, pandas.core.series.Series], fill_value: int
    ):
        """
        usage.dask: 2
        """
        ...

    def rmul(
        self: object, /, other: Union[int, pandas.core.series.Series], fill_value: int
    ):
        """
        usage.dask: 2
        """
        ...

    def rtruediv(
        self: object, /, other: Union[int, pandas.core.series.Series], fill_value: int
    ):
        """
        usage.dask: 4
        """
        ...

    def rpow(
        self: object, /, other: Union[int, pandas.core.series.Series], fill_value: int
    ):
        """
        usage.dask: 2
        """
        ...

    def rmod(
        self: object, /, other: Union[int, pandas.core.series.Series], fill_value: int
    ):
        """
        usage.dask: 2
        """
        ...

    def std(
        self: object,
        /,
        axis: Union[Literal["columns"], None, int] = ...,
        skipna: bool = ...,
        ddof: int = ...,
    ):
        """
        usage.dask: 12
        """
        ...

    def sem(
        self: object,
        /,
        axis: Union[Literal["columns"], int] = ...,
        skipna: Union[bool, None] = ...,
        ddof: int = ...,
    ):
        """
        usage.dask: 9
        """
        ...

    def nunique(self: object, /):
        """
        usage.dask: 5
        """
        ...

    def value_counts(self: object, /):
        """
        usage.dask: 9
        """
        ...

    def rename(self: object, /, *, inplace: bool = ...):
        """
        usage.dask: 23
        """
        ...

    def copy(self: object, /):
        """
        usage.dask: 3
        """
        ...

    def head(self: object, /, n: int):
        """
        usage.dask: 7
        """
        ...

    def tail(self: object, /, n: int):
        """
        usage.dask: 4
        """
        ...

    def quantile(self: object, /):
        """
        usage.dask: 7
        """
        ...

    def describe(
        self: object,
        /,
        include: List[
            Union[Type[numpy.timedelta64], Literal["number", "object"]]
        ] = ...,
        exclude: None = ...,
    ):
        """
        usage.dask: 7
        """
        ...

    def apply(
        self: object,
        /,
        func: Callable,
        convert_dtype: bool = ...,
        args: Tuple[None, ...] = ...,
    ):
        """
        usage.dask: 9
        """
        ...

    def where(self: object, /, cond: pandas.core.series.Series):
        """
        usage.dask: 8
        """
        ...

    def cumsum(self: object, /, axis: None = ..., skipna: bool = ...):
        """
        usage.dask: 5
        """
        ...

    def cumprod(self: object, /, axis: None = ..., skipna: bool = ...):
        """
        usage.dask: 4
        """
        ...

    def cummin(self: object, /, axis: None = ..., skipna: bool = ...):
        """
        usage.dask: 4
        """
        ...

    def cummax(self: object, /, axis: None = ..., skipna: bool = ...):
        """
        usage.dask: 4
        """
        ...

    def notna(self: object, /):
        """
        usage.dask: 1
        """
        ...

    def clip(
        self: object,
        /,
        lower: Union[None, int, float] = ...,
        upper: Union[float, int, None] = ...,
    ):
        """
        usage.dask: 13
        """
        ...

    def squeeze(self: object, /):
        """
        usage.dask: 1
        """
        ...

    def mask(self: object, /, cond: pandas.core.series.Series):
        """
        usage.dask: 4
        """
        ...

    def to_string(self: object, /, max_rows: int):
        """
        usage.dask: 1
        """
        ...

    def isin(self: object, /, values: Union[pandas.core.series.Series, List[int]]):
        """
        usage.dask: 6
        """
        ...

    def map(
        self: object,
        /,
        arg: Union[Callable, pandas.core.series.Series, Dict[numpy.int64, numpy.int64]],
    ):
        """
        usage.dask: 15
        """
        ...

    def align(
        self: object,
        /,
        other: pandas.core.series.Series,
        join: Literal["right", "left", "outer", "inner"],
        axis: Union[int, None] = ...,
        fill_value: Union[None, int] = ...,
    ):
        """
        usage.dask: 20
        """
        ...

    def combine(
        self: object,
        /,
        other: pandas.core.series.Series,
        func: Callable,
        fill_value: Union[None, int],
    ):
        """
        usage.dask: 6
        """
        ...

    def combine_first(self: object, /, other: pandas.core.series.Series):
        """
        usage.dask: 5
        """
        ...

    def round(self: object, /):
        """
        usage.dask: 2
        """
        ...

    def between(self: object, /, left: int, right: int):
        """
        usage.dask: 2
        """
        ...

    def notnull(self: object, /):
        """
        usage.dask: 3
        """
        ...

    def fillna(
        self: object,
        /,
        value: Union[pandas.core.series.Series, numpy.float64, int, None] = ...,
        method: Union[None, Literal["bfill", "ffill", "pad"]] = ...,
        axis: int = ...,
        limit: Union[None, int] = ...,
    ):
        """
        usage.dask: 23
        """
        ...

    def nlargest(self: object, /, n: int):
        """
        usage.dask: 4
        """
        ...

    def abs(self: object, /):
        """
        usage.dask: 3
        """
        ...

    def cov(self: object, /, other: pandas.core.series.Series):
        """
        usage.dask: 2
        """
        ...

    def replace(
        self: object,
        /,
        to_replace: Union[Dict[int, int], int, Literal["c"]],
        value: Union[None, float, int] = ...,
        regex: bool = ...,
    ):
        """
        usage.dask: 5
        """
        ...

    def autocorr(self: object, /, lag: int):
        """
        usage.dask: 4
        """
        ...

    def nsmallest(self: object, /, n: int):
        """
        usage.dask: 2
        """
        ...

    def diff(self: object, /):
        """
        usage.dask: 7
        """
        ...

    def first(self: object, /, offset: str):
        """
        usage.dask: 24
        """
        ...

    def last(self: object, /, offset: str):
        """
        usage.dask: 8
        """
        ...

    def explode(self: object, /):
        """
        usage.dask: 5
        """
        ...

    def __itruediv__(self: object, _0: pandas.core.series.Series, /):
        """
        usage.dask: 1
        """
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
        """
        usage.dask: 8
        """
        ...

    def idxmax(self: object, /):
        """
        usage.dask: 1
        """
        ...

    def items(self: object, /):
        """
        usage.dask: 1
        """
        ...

    def append(self: object, /, to_append: pandas.core.series.Series):
        """
        usage.dask: 2
        """
        ...

    def __array_wrap__(self: object, /, result: numpy.ndarray):
        """
        usage.dask: 3
        """
        ...
