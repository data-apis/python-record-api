from typing import *


class Series:
    def __init__(self, /, data: List[str]):
        """
        usage.dask: 5
        usage.sklearn: 1
        """
        ...

    # usage.dask: 4
    __module__: ClassVar[object]

    # usage.dask: 7
    # usage.sklearn: 1
    __name__: ClassVar[object]

    @classmethod
    def __ne__(cls, _0: Union[numpy.ndarray, Type[pandas.core.series.Series]], /):
        """
        usage.dask: 4
        usage.pandas: 6
        """
        ...

    @classmethod
    def __rmod__(cls, _0: Union[numpy.timedelta64, numpy.float64, str], /):
        """
        usage.pandas: 2
        usage.sklearn: 1
        """
        ...

    # usage.dask: 6
    # usage.sklearn: 1
    __class__: object

    # usage.dask: 2
    _constructor: object

    # usage.dask: 1
    _data: object

    # usage.dask: 3
    _values: object

    # usage.dask: 28
    cat: object

    # usage.dask: 1
    div: object

    # usage.dask: 1
    divide: object

    # usage.dask: 2
    # usage.xarray: 2
    dt: object

    # usage.dask: 65
    # usage.sklearn: 9
    dtype: object

    # usage.sklearn: 2
    dtypes: object

    # usage.dask: 1
    empty: object

    # usage.dask: 31
    # usage.sklearn: 1
    # usage.xarray: 3
    iloc: object

    # usage.dask: 83
    # usage.sklearn: 3
    # usage.xarray: 23
    index: object

    # usage.dask: 25
    # usage.sklearn: 1
    # usage.xarray: 3
    loc: object

    # usage.dask: 48
    # usage.sklearn: 6
    # usage.xarray: 5
    name: Union[str, None]

    # usage.dask: 2
    nbytes: object

    # usage.dask: 6
    # usage.sklearn: 4
    ndim: object

    # usage.dask: 1
    rdiv: object

    # usage.dask: 7
    # usage.sklearn: 12
    shape: object

    # usage.dask: 2
    size: object

    # usage.dask: 26
    str: object

    # usage.dask: 40
    # usage.xarray: 16
    values: object

    def __add__(self, _0: object, /):
        """
        usage.dask: 55
        usage.pandas: 39
        """
        ...

    def __and__(self, _0: Union[pandas.core.series.Series, numpy.ndarray], /):
        """
        usage.dask: 5
        usage.pandas: 3
        """
        ...

    def __array_wrap__(self, /, result: numpy.ndarray):
        """
        usage.dask: 3
        """
        ...

    def __contains__(self, _0: Literal["bool"], /):
        """
        usage.pandas: 1
        """
        ...

    def __eq__(self, _0: object, /):
        """
        usage.dask: 43
        usage.pandas: 52
        usage.sklearn: 10
        """
        ...

    def __floordiv__(self, _0: Union[int, float, numpy.ndarray, numpy.timedelta64], /):
        """
        usage.dask: 3
        usage.pandas: 6
        """
        ...

    def __ge__(self, _0: object, /):
        """
        usage.dask: 17
        usage.pandas: 7
        """
        ...

    def __getitem__(self, _0: object, /):
        """
        usage.dask: 84
        usage.xarray: 23
        """
        ...

    def __gt__(self, _0: object, /):
        """
        usage.dask: 59
        usage.pandas: 5
        """
        ...

    def __iadd__(self, _0: Union[numpy.ndarray, numpy.timedelta64], /):
        """
        usage.pandas: 2
        """
        ...

    def __invert__(self, /):
        """
        usage.dask: 1
        usage.xarray: 1
        """
        ...

    def __isub__(self, _0: Union[numpy.ndarray, numpy.timedelta64], /):
        """
        usage.pandas: 2
        """
        ...

    def __iter__(self, /):
        """
        usage.dask: 4
        usage.sklearn: 12
        """
        ...

    def __itruediv__(self, _0: pandas.core.series.Series, /):
        """
        usage.dask: 1
        """
        ...

    def __le__(self, _0: object, /):
        """
        usage.dask: 16
        usage.pandas: 7
        """
        ...

    def __lt__(self, _0: object, /):
        """
        usage.dask: 4
        usage.pandas: 4
        """
        ...

    def __mod__(self, _0: Union[int, numpy.ndarray, numpy.timedelta64], /):
        """
        usage.dask: 5
        usage.pandas: 57
        """
        ...

    def __mul__(self, _0: object, /):
        """
        usage.dask: 6
        usage.pandas: 29
        """
        ...

    def __neg__(self, /):
        """
        usage.dask: 2
        """
        ...

    def __or__(self, _0: Union[pandas.core.series.Series, numpy.ndarray], /):
        """
        usage.dask: 3
        usage.pandas: 3
        """
        ...

    def __pow__(self, _0: Union[float, int, numpy.timedelta64], /):
        """
        usage.dask: 5
        usage.pandas: 1
        """
        ...

    def __radd__(self, _0: object, /):
        """
        usage.dask: 17
        usage.pandas: 46
        """
        ...

    def __rand__(self, _0: pandas.core.series.Series, /):
        """
        usage.dask: 5
        """
        ...

    def __rfloordiv__(
        self, _0: Union[numpy.float64, numpy.int64, numpy.ndarray, numpy.timedelta64], /
    ):
        """
        usage.pandas: 6
        """
        ...

    def __rmul__(self, _0: object, /):
        """
        usage.dask: 3
        usage.pandas: 30
        usage.sklearn: 2
        """
        ...

    def __ror__(self, _0: Union[pandas.core.series.Series, numpy.ndarray], /):
        """
        usage.dask: 3
        usage.pandas: 1
        """
        ...

    def __rpow__(self, _0: Union[numpy.float64, numpy.int64, numpy.timedelta64], /):
        """
        usage.pandas: 10
        """
        ...

    def __rsub__(self, _0: object, /):
        """
        usage.dask: 10
        usage.pandas: 44
        """
        ...

    def __rtruediv__(self, _0: object, /):
        """
        usage.dask: 8
        usage.pandas: 37
        """
        ...

    def __rxor__(self, _0: pandas.core.series.Series, /):
        """
        usage.dask: 1
        """
        ...

    def __setitem__(
        self, _0: Union[pandas.core.series.Series, int], _1: Union[int, float], /
    ):
        """
        usage.dask: 3
        usage.xarray: 2
        """
        ...

    def __sub__(self, _0: object, /):
        """
        usage.dask: 18
        usage.pandas: 35
        """
        ...

    def __truediv__(self, _0: object, /):
        """
        usage.dask: 10
        usage.pandas: 29
        """
        ...

    def __xor__(self, _0: Union[pandas.core.series.Series, numpy.ndarray], /):
        """
        usage.dask: 1
        usage.pandas: 1
        """
        ...

    def abs(self, /):
        """
        usage.dask: 3
        """
        ...

    def add(self, /, other: Union[pandas.core.series.Series, int]):
        """
        usage.dask: 7
        """
        ...

    def align(
        self,
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

    def all(self, /, axis: int = ..., skipna: bool = ...):
        """
        usage.dask: 24
        """
        ...

    def any(self, /, axis: int = ..., skipna: bool = ...):
        """
        usage.dask: 8
        usage.sklearn: 2
        usage.xarray: 1
        """
        ...

    def append(self, /, to_append: pandas.core.series.Series):
        """
        usage.dask: 2
        """
        ...

    def apply(
        self, /, func: Callable, convert_dtype: bool = ..., args: Tuple[None, ...] = ...
    ):
        """
        usage.dask: 9
        usage.sklearn: 1
        """
        ...

    def astype(
        self,
        /,
        dtype: Union[
            pandas.core.dtypes.dtypes.CategoricalDtype, numpy.dtype, str, type
        ],
    ):
        """
        usage.dask: 53
        usage.sklearn: 10
        usage.xarray: 1
        """
        ...

    def autocorr(self, /, lag: int):
        """
        usage.dask: 4
        """
        ...

    def between(self, /, left: int, right: int):
        """
        usage.dask: 2
        """
        ...

    def clip(
        self,
        /,
        lower: Union[None, int, float] = ...,
        upper: Union[float, int, None] = ...,
    ):
        """
        usage.dask: 13
        """
        ...

    def combine(
        self,
        /,
        other: pandas.core.series.Series,
        func: Callable,
        fill_value: Union[None, int],
    ):
        """
        usage.dask: 6
        """
        ...

    def combine_first(self, /, other: pandas.core.series.Series):
        """
        usage.dask: 5
        """
        ...

    def copy(self, /):
        """
        usage.dask: 3
        """
        ...

    def count(self, /, *, axis: Union[Literal["columns"], int] = ...):
        """
        usage.dask: 10
        """
        ...

    def cov(self, /, other: pandas.core.series.Series):
        """
        usage.dask: 2
        """
        ...

    def cummax(self, /, axis: None = ..., skipna: bool = ...):
        """
        usage.dask: 4
        """
        ...

    def cummin(self, /, axis: None = ..., skipna: bool = ...):
        """
        usage.dask: 4
        """
        ...

    def cumprod(self, /, axis: None = ..., skipna: bool = ...):
        """
        usage.dask: 4
        """
        ...

    def cumsum(self, /, axis: None = ..., skipna: bool = ...):
        """
        usage.dask: 5
        """
        ...

    def describe(
        self,
        /,
        include: Union[
            List[
                Union[
                    Type[numpy.timedelta64],
                    Literal["number", "object", "bool", "datetime"],
                ]
            ],
            Literal["all"],
            None,
        ] = ...,
        exclude: Union[None, List[Literal["object", "number"]]] = ...,
    ):
        """
        usage.dask: 10
        """
        ...

    def diff(self, /):
        """
        usage.dask: 7
        """
        ...

    def drop_duplicates(self, /):
        """
        usage.dask: 12
        """
        ...

    def dropna(self, /):
        """
        usage.dask: 7
        usage.xarray: 2
        """
        ...

    def duplicated(self, /, keep: Literal["last"]):
        """
        usage.xarray: 1
        """
        ...

    def eq(self, /, other: pandas.core.series.Series, fill_value: int):
        """
        usage.dask: 1
        """
        ...

    def equals(self, /, other: pandas.core.series.Series):
        """
        usage.dask: 3
        usage.xarray: 8
        """
        ...

    def explode(self, /):
        """
        usage.dask: 5
        """
        ...

    def fillna(
        self,
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

    def first(self, /, offset: str):
        """
        usage.dask: 24
        """
        ...

    def floordiv(
        self, /, other: Union[int, pandas.core.series.Series], fill_value: int
    ):
        """
        usage.dask: 2
        """
        ...

    def ge(self, /, other: pandas.core.series.Series, fill_value: int):
        """
        usage.dask: 1
        """
        ...

    def groupby(
        self,
        /,
        level: Union[List[int], int] = ...,
        sort: bool = ...,
        by: object = ...,
        group_keys: bool = ...,
    ):
        """
        usage.dask: 64
        usage.xarray: 1
        """
        ...

    def gt(self, /, other: pandas.core.series.Series, fill_value: int):
        """
        usage.dask: 1
        """
        ...

    def head(self, /, n: int):
        """
        usage.dask: 7
        """
        ...

    def idxmax(self, /):
        """
        usage.dask: 8
        """
        ...

    def idxmin(self, /, skipna: bool):
        """
        usage.dask: 4
        """
        ...

    def isin(self, /, values: Union[pandas.core.series.Series, List[int]]):
        """
        usage.dask: 6
        """
        ...

    def isnull(self, /):
        """
        usage.dask: 5
        usage.xarray: 1
        """
        ...

    def items(self, /):
        """
        usage.dask: 1
        """
        ...

    def iteritems(self, /):
        """
        usage.dask: 4
        usage.xarray: 1
        """
        ...

    def last(self, /, offset: str):
        """
        usage.dask: 8
        """
        ...

    def le(self, /, other: pandas.core.series.Series, fill_value: int):
        """
        usage.dask: 1
        """
        ...

    def lt(self, /, other: pandas.core.series.Series, fill_value: int):
        """
        usage.dask: 1
        """
        ...

    def map(
        self,
        /,
        arg: Union[Callable, Dict[numpy.int64, numpy.int64], pandas.core.series.Series],
    ):
        """
        usage.dask: 16
        """
        ...

    def mask(self, /, cond: pandas.core.series.Series):
        """
        usage.dask: 4
        """
        ...

    def max(
        self, /, axis: Union[Literal["columns"], None, int] = ..., skipna: bool = ...
    ):
        """
        usage.dask: 22
        usage.xarray: 1
        """
        ...

    def mean(
        self, /, axis: Union[Literal["columns"], None, int] = ..., skipna: bool = ...
    ):
        """
        usage.dask: 25
        usage.xarray: 1
        """
        ...

    def median(self, /):
        """
        usage.xarray: 1
        """
        ...

    def memory_usage(self, /, index: bool):
        """
        usage.dask: 6
        """
        ...

    def min(
        self, /, axis: Union[Literal["columns"], None, int] = ..., skipna: bool = ...
    ):
        """
        usage.dask: 17
        usage.xarray: 1
        """
        ...

    def mod(self, /, other: Union[int, pandas.core.series.Series], fill_value: int):
        """
        usage.dask: 2
        """
        ...

    def mode(self, /):
        """
        usage.dask: 1
        """
        ...

    def mul(self, /, other: Union[pandas.core.series.Series, int]):
        """
        usage.dask: 4
        """
        ...

    def ne(self, /, other: pandas.core.series.Series, fill_value: int):
        """
        usage.dask: 1
        """
        ...

    def nlargest(self, /, n: int):
        """
        usage.dask: 4
        """
        ...

    def notna(self, /):
        """
        usage.dask: 1
        """
        ...

    def notnull(self, /):
        """
        usage.dask: 3
        """
        ...

    def nsmallest(self, /, n: int):
        """
        usage.dask: 2
        """
        ...

    def nunique(self, /):
        """
        usage.dask: 5
        """
        ...

    def pow(self, /, other: Union[int, pandas.core.series.Series]):
        """
        usage.dask: 3
        """
        ...

    def prod(
        self,
        /,
        axis: Union[Literal["columns"], None, int] = ...,
        skipna: bool = ...,
        min_count: int = ...,
    ):
        """
        usage.dask: 10
        usage.xarray: 1
        """
        ...

    def quantile(self, /):
        """
        usage.dask: 7
        """
        ...

    def radd(self, /, other: Union[int, pandas.core.series.Series], fill_value: int):
        """
        usage.dask: 2
        """
        ...

    def rank(self, /, method: Literal["dense"], ascending: bool):
        """
        usage.xarray: 1
        """
        ...

    def reindex(
        self,
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

    def rename(self, /, *, inplace: bool = ...):
        """
        usage.dask: 25
        """
        ...

    def replace(
        self,
        /,
        to_replace: Union[Dict[int, int], int, Literal["c"]],
        value: Union[None, float, int] = ...,
        regex: bool = ...,
    ):
        """
        usage.dask: 5
        """
        ...

    def resample(
        self,
        /,
        rule: object,
        closed: Union[None, Literal["left", "right"]] = ...,
        label: Union[None, Literal["left", "right"]] = ...,
    ):
        """
        usage.dask: 88
        usage.xarray: 14
        """
        ...

    def reset_index(self, /):
        """
        usage.dask: 7
        """
        ...

    def rmod(self, /, other: Union[int, pandas.core.series.Series], fill_value: int):
        """
        usage.dask: 2
        """
        ...

    def rmul(self, /, other: Union[int, pandas.core.series.Series], fill_value: int):
        """
        usage.dask: 2
        """
        ...

    def rolling(
        self,
        /,
        window: Union[Literal["3S", "2S", "1S"], int, pandas.tseries.offsets.Second],
        min_periods: Union[None, int] = ...,
        center: bool = ...,
        win_type: None = ...,
        axis: int = ...,
    ):
        """
        usage.dask: 24
        usage.xarray: 3
        """
        ...

    def round(self, /):
        """
        usage.dask: 2
        """
        ...

    def rpow(self, /, other: Union[int, pandas.core.series.Series], fill_value: int):
        """
        usage.dask: 2
        """
        ...

    def rsub(self, /, other: Union[int, pandas.core.series.Series], fill_value: int):
        """
        usage.dask: 2
        """
        ...

    def rtruediv(
        self, /, other: Union[int, pandas.core.series.Series], fill_value: int
    ):
        """
        usage.dask: 4
        """
        ...

    def searchsorted(self, /, value: pandas.core.series.Series, side: Literal["right"]):
        """
        usage.dask: 1
        """
        ...

    def sem(
        self,
        /,
        axis: Union[Literal["columns"], int] = ...,
        skipna: Union[bool, None] = ...,
        ddof: int = ...,
    ):
        """
        usage.dask: 9
        """
        ...

    def shift(self, /, periods: int = ..., freq: object = ...):
        """
        usage.dask: 32
        usage.xarray: 1
        """
        ...

    def sort_index(self, /):
        """
        usage.dask: 4
        """
        ...

    def sort_values(self, /):
        """
        usage.dask: 5
        """
        ...

    def squeeze(self, /):
        """
        usage.dask: 1
        """
        ...

    def std(
        self,
        /,
        axis: Union[Literal["columns"], None, int] = ...,
        skipna: bool = ...,
        ddof: int = ...,
    ):
        """
        usage.dask: 12
        """
        ...

    def sub(self, /, other: Union[int, pandas.core.series.Series], fill_value: int):
        """
        usage.dask: 2
        """
        ...

    def sum(
        self, /, axis: Union[Literal["columns"], None, int] = ..., skipna: bool = ...
    ):
        """
        usage.dask: 41
        usage.sklearn: 1
        usage.xarray: 2
        """
        ...

    def tail(self, /, n: int):
        """
        usage.dask: 4
        """
        ...

    def take(self, /, indices: numpy.ndarray):
        """
        usage.dask: 1
        """
        ...

    def to_dict(self, /):
        """
        usage.dask: 5
        """
        ...

    def to_frame(self, /):
        """
        usage.dask: 29
        usage.sklearn: 2
        usage.xarray: 2
        """
        ...

    def to_string(self, /, max_rows: int):
        """
        usage.dask: 1
        """
        ...

    def to_timestamp(
        self,
        /,
        freq: Union[Literal["M"], None] = ...,
        how: Literal["s", "start"] = ...,
        copy: int = ...,
    ):
        """
        usage.dask: 4
        """
        ...

    def tolist(self, /):
        """
        usage.dask: 4
        """
        ...

    def truediv(self, /, other: Union[int, pandas.core.series.Series], fill_value: int):
        """
        usage.dask: 6
        """
        ...

    def unique(self, /):
        """
        usage.dask: 9
        """
        ...

    def unstack(self, /):
        """
        usage.xarray: 1
        """
        ...

    def value_counts(self, /):
        """
        usage.dask: 11
        """
        ...

    def var(
        self,
        /,
        axis: Union[Literal["columns"], None, int] = ...,
        skipna: Union[None, bool] = ...,
        ddof: int = ...,
    ):
        """
        usage.dask: 14
        usage.xarray: 1
        """
        ...

    def where(self, /, cond: pandas.core.series.Series):
        """
        usage.dask: 8
        usage.xarray: 1
        """
        ...
