from typing import *


class Series:
    def __init__(
        data: List[
            Literal[
                ("a", "b", "c", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
            ]
        ] = ...
    ):
        "usage.dask: 5"

    __name__ = ...
    __module__ = ...

    @classmethod
    def __ne__(_0: Type[pandas.core.series.Series], /):
        ""

    dt = ...
    values = ...
    index = ...
    name: Union[(None, str)] = ...
    loc = ...
    dtype = ...
    iloc = ...
    _data = ...
    cat = ...
    str = ...
    empty = ...
    div = ...
    divide = ...
    rdiv = ...
    __class__ = ...
    shape = ...
    ndim = ...
    _values = ...
    size = ...
    nbytes = ...

    def rank(self, /, method: Literal[("dense",)], ascending: bool):
        "usage.xarray: 1"

    def astype(
        self,
        /,
        dtype: Union[
            (type, str, pandas.core.dtypes.dtypes.CategoricalDtype, numpy.dtype)
        ],
    ):
        "usage.xarray: 1, usage.dask: 52"

    def median(self, /):
        "usage.xarray: 1"

    def reset_index(self=..., /):
        "usage.xarray: 2, usage.dask: 6"

    def unstack(self, /):
        "usage.xarray: 1"

    def groupby(
        self,
        /,
        level: Union[(List[int], int)] = ...,
        sort: bool = ...,
        by=...,
        group_keys: bool = ...,
    ):
        "usage.xarray: 1, usage.dask: 64"

    def isnull(self, /):
        "usage.xarray: 1, usage.dask: 5"

    def any(self, /, axis: int = ..., skipna: bool = ...):
        "usage.xarray: 1, usage.dask: 8"

    def resample(
        self,
        /,
        rule=...,
        closed: Union[(None, Literal[("left", "right")])] = ...,
        label: Union[(None, Literal[("left", "right")])] = ...,
    ):
        "usage.xarray: 14, usage.dask: 83"

    def dropna(self, /):
        "usage.xarray: 1, usage.dask: 7"

    def to_frame(self=..., /):
        "usage.xarray: 2, usage.dask: 26"

    def equals(self, /, other: pandas.core.series.Series):
        "usage.xarray: 1, usage.dask: 3"

    def __setitem__(
        self, _0: Union[(pandas.core.series.Series, int)], _1: Union[(int, float)], /
    ):
        ""

    def shift(self, /, periods: int = ..., freq=...):
        "usage.xarray: 1, usage.dask: 32"

    def rolling(
        self,
        /,
        window: Union[
            (Literal[("3S", "2S", "1S")], int, pandas.tseries.offsets.Second)
        ],
        min_periods: Union[(None, int)] = ...,
        center: bool = ...,
        win_type: None = ...,
        axis: int = ...,
    ):
        "usage.xarray: 3, usage.dask: 24"

    def iteritems(self, /):
        "usage.xarray: 1, usage.dask: 4"

    def __getitem__(self, _0, /):
        ""

    def sum(
        self=...,
        /,
        axis: Union[(Literal[("columns",)], None, int)] = ...,
        skipna: bool = ...,
    ):
        "usage.xarray: 2, usage.dask: 42"

    def min(
        self,
        /,
        axis: Union[(Literal[("columns",)], None, int)] = ...,
        skipna: bool = ...,
    ):
        "usage.xarray: 1, usage.dask: 15"

    def max(
        self,
        /,
        axis: Union[(Literal[("columns",)], None, int)] = ...,
        skipna: bool = ...,
    ):
        "usage.xarray: 1, usage.dask: 19"

    def mean(
        self,
        /,
        axis: Union[(Literal[("columns",)], None, int)] = ...,
        skipna: bool = ...,
    ):
        "usage.xarray: 1, usage.dask: 25"

    def var(
        self,
        /,
        axis: Union[(Literal[("columns",)], None, int)] = ...,
        skipna: Union[(None, bool)] = ...,
        ddof: int = ...,
    ):
        "usage.xarray: 1, usage.dask: 14"

    def prod(
        self,
        /,
        axis: Union[(Literal[("columns",)], None, int)] = ...,
        skipna: bool = ...,
        min_count: int = ...,
    ):
        "usage.xarray: 1, usage.dask: 10"

    def __eq__(
        self,
        _0: Union[
            (
                int,
                pandas.core.series.Series,
                dask.dataframe.core.Series,
                Literal[("object", "a", "i8", "category")],
                Type[numpy.float64],
            )
        ],
        /,
    ):
        ""

    def to_dict(self, /):
        "usage.dask: 5"

    def all(self, /, axis: int = ..., skipna: bool = ...):
        "usage.dask: 24"

    def unique(self, /):
        "usage.dask: 9"

    def tolist(self, /):
        "usage.dask: 3"

    def memory_usage(self, /, index: bool = ...):
        "usage.dask: 6"

    def __iter__(self, /):
        ""

    def searchsorted(
        self, /, value: pandas.core.series.Series, side: Literal[("right",)]
    ):
        "usage.dask: 1"

    def __ge__(self, _0, /):
        ""

    def __invert__(self, /):
        ""

    def __mod__(self, _0: Union[(pandas.core.series.Series, int)], /):
        ""

    def __mul__(self, _0: Union[(int, float, pandas.core.series.Series)], /):
        ""

    def __truediv__(self, _0: Union[(int, float, pandas.core.series.Series)], /):
        ""

    def drop_duplicates(self=..., /):
        "usage.dask: 12"

    def count(self, /, *, axis: Union[(Literal[("columns",)], int)] = ...):
        "usage.dask: 10"

    def sort_values(self=..., /):
        "usage.dask: 4"

    def sort_index(self=..., /):
        "usage.dask: 4"

    def __add__(self, _0, /):
        ""

    def __radd__(
        self,
        _0: Union[
            (
                numpy.ndarray,
                dask.dataframe.core.Series,
                pandas.core.series.Series,
                int,
                dask.dataframe.core.Scalar,
            )
        ],
        /,
    ):
        ""

    def __rmul__(
        self, _0: Union[(dask.dataframe.core.Series, pandas.core.series.Series, int)], /
    ):
        ""

    def __sub__(self, _0: Union[(numpy.float64, pandas.core.series.Series, int)], /):
        ""

    def __rsub__(
        self,
        _0: Union[
            (
                pandas.core.frame.DataFrame,
                int,
                pandas.core.series.Series,
                dask.dataframe.core.Series,
            )
        ],
        /,
    ):
        ""

    def __rtruediv__(
        self, _0: Union[(dask.dataframe.core.Series, pandas.core.series.Series, int)], /
    ):
        ""

    def __floordiv__(self, _0: Union[(float, pandas.core.series.Series, int)], /):
        ""

    def __rfloordiv__(
        self, _0: Union[(dask.dataframe.core.Series, pandas.core.series.Series, int)], /
    ):
        ""

    def __pow__(self, _0: Union[(float, pandas.core.series.Series, int)], /):
        ""

    def __rpow__(
        self, _0: Union[(dask.dataframe.core.Series, pandas.core.series.Series, int)], /
    ):
        ""

    def __rmod__(
        self, _0: Union[(dask.dataframe.core.Series, pandas.core.series.Series, int)], /
    ):
        ""

    def __and__(self, _0: Union[(bool, pandas.core.series.Series)], /):
        ""

    def __rand__(
        self,
        _0: Union[(dask.dataframe.core.Series, pandas.core.series.Series, bool)],
        /,
    ):
        ""

    def __or__(self, _0: Union[(bool, pandas.core.series.Series)], /):
        ""

    def __ror__(
        self,
        _0: Union[(dask.dataframe.core.Series, pandas.core.series.Series, bool)],
        /,
    ):
        ""

    def __xor__(self, _0: Union[(bool, pandas.core.series.Series)], /):
        ""

    def __rxor__(
        self,
        _0: Union[(dask.dataframe.core.Series, pandas.core.series.Series, bool)],
        /,
    ):
        ""

    def __gt__(
        self, _0: Union[(numpy.int64, int, pandas.core.series.Series, numpy.float64)], /
    ):
        ""

    def __lt__(
        self,
        _0: Union[
            (
                pandas._libs.tslibs.timedeltas.Timedelta,
                dask.dataframe.core.Series,
                pandas.core.series.Series,
                int,
                pandas.core.frame.DataFrame,
            )
        ],
        /,
    ):
        ""

    def __le__(self, _0, /):
        ""

    def __ne__(
        self, _0: Union[(dask.dataframe.core.Series, pandas.core.series.Series, int)], /
    ):
        ""

    def lt(self, /, other: Union[(pandas.core.series.Series, int)] = ...):
        "usage.dask: 3"

    def gt(self, /, other: Union[(pandas.core.series.Series, int)] = ...):
        "usage.dask: 3"

    def le(self, /, other: Union[(pandas.core.series.Series, int)] = ...):
        "usage.dask: 3"

    def ge(self, /, other: Union[(pandas.core.series.Series, int)] = ...):
        "usage.dask: 3"

    def ne(self, /, other: Union[(pandas.core.series.Series, int)] = ...):
        "usage.dask: 3"

    def eq(self, /, other: Union[(pandas.core.series.Series, int)] = ...):
        "usage.dask: 3"

    def __neg__(self, /):
        ""

    def add(self, /, other: Union[(pandas.core.series.Series, int)] = ...):
        "usage.dask: 7"

    def sub(self, /, other: Union[(int, pandas.core.series.Series)], fill_value: int):
        "usage.dask: 2"

    def mul(self, /, other: Union[(pandas.core.series.Series, int)] = ...):
        "usage.dask: 4"

    def truediv(
        self, /, other: Union[(int, pandas.core.series.Series)], fill_value: int
    ):
        "usage.dask: 6"

    def floordiv(
        self, /, other: Union[(int, pandas.core.series.Series)], fill_value: int
    ):
        "usage.dask: 2"

    def pow(self, /, other: Union[(int, pandas.core.series.Series)], fill_value: int):
        "usage.dask: 2"

    def mod(self, /, other: Union[(int, pandas.core.series.Series)], fill_value: int):
        "usage.dask: 2"

    def radd(self, /, other: Union[(int, pandas.core.series.Series)], fill_value: int):
        "usage.dask: 2"

    def rsub(self, /, other: Union[(int, pandas.core.series.Series)], fill_value: int):
        "usage.dask: 2"

    def rmul(self, /, other: Union[(int, pandas.core.series.Series)], fill_value: int):
        "usage.dask: 2"

    def rtruediv(
        self, /, other: Union[(int, pandas.core.series.Series)], fill_value: int
    ):
        "usage.dask: 4"

    def rpow(self, /, other: Union[(int, pandas.core.series.Series)], fill_value: int):
        "usage.dask: 2"

    def rmod(self, /, other: Union[(int, pandas.core.series.Series)], fill_value: int):
        "usage.dask: 2"

    def std(
        self,
        /,
        axis: Union[(Literal[("columns",)], None, int)] = ...,
        skipna: bool = ...,
        ddof: int = ...,
    ):
        "usage.dask: 12"

    def sem(
        self,
        /,
        axis: Union[(Literal[("columns",)], int)] = ...,
        skipna: Union[(bool, None)] = ...,
        ddof: int = ...,
    ):
        "usage.dask: 9"

    def nunique(self, /):
        "usage.dask: 5"

    def value_counts(self, /):
        "usage.dask: 9"

    def rename(self=..., /, *, inplace: bool = ...):
        "usage.dask: 23"

    def copy(self, /):
        "usage.dask: 3"

    def head(self, /, n: int):
        "usage.dask: 7"

    def tail(self, /, n: int):
        "usage.dask: 4"

    def quantile(self=..., /):
        "usage.dask: 7"

    def describe(
        self,
        /,
        include: List[
            Union[(Type[numpy.timedelta64], Literal[("number", "object")])]
        ] = ...,
        exclude: None = ...,
    ):
        "usage.dask: 7"

    def apply(
        self,
        /,
        func: Callable,
        convert_dtype: bool = ...,
        args: Tuple[(None, ...)] = ...,
    ):
        "usage.dask: 9"

    def where(self=..., /, cond: pandas.core.series.Series = ...):
        "usage.dask: 8"

    def cumsum(self, /, axis: None = ..., skipna: bool = ...):
        "usage.dask: 5"

    def cumprod(self, /, axis: None = ..., skipna: bool = ...):
        "usage.dask: 4"

    def cummin(self, /, axis: None = ..., skipna: bool = ...):
        "usage.dask: 4"

    def cummax(self, /, axis: None = ..., skipna: bool = ...):
        "usage.dask: 4"

    def notna(self, /):
        "usage.dask: 1"

    def clip(
        self,
        /,
        lower: Union[(None, int, float)] = ...,
        upper: Union[(float, int, None)] = ...,
    ):
        "usage.dask: 13"

    def squeeze(self, /):
        "usage.dask: 1"

    def mask(self, /, cond: pandas.core.series.Series = ...):
        "usage.dask: 4"

    def to_string(self, /, max_rows: int):
        "usage.dask: 1"

    def isin(self, /, values: Union[(pandas.core.series.Series, List[int])]):
        "usage.dask: 6"

    def map(
        self,
        /,
        arg: Union[
            (Callable, pandas.core.series.Series, Dict[(numpy.int64, numpy.int64)])
        ] = ...,
    ):
        "usage.dask: 15"

    def align(
        self,
        /,
        other: pandas.core.series.Series,
        join: Literal[("right", "left", "outer", "inner")],
        axis: Union[(int, None)] = ...,
        fill_value: Union[(None, int)] = ...,
    ):
        "usage.dask: 20"

    def combine(
        self,
        /,
        other: pandas.core.series.Series,
        func: Callable,
        fill_value: Union[(None, int)],
    ):
        "usage.dask: 6"

    def combine_first(self, /, other: pandas.core.series.Series):
        "usage.dask: 5"

    def round(self=..., /):
        "usage.dask: 2"

    def between(self, /, left: int, right: int = ...):
        "usage.dask: 2"

    def notnull(self, /):
        "usage.dask: 3"

    def fillna(
        self,
        /,
        value: Union[(pandas.core.series.Series, numpy.float64, int, None)] = ...,
        method: Union[(None, Literal[("bfill", "ffill", "pad")])] = ...,
        axis: int = ...,
        limit: Union[(None, int)] = ...,
    ):
        "usage.dask: 23"

    def nlargest(self, /, n: int):
        "usage.dask: 4"

    def abs(self, /):
        "usage.dask: 3"

    def cov(self, /, other: pandas.core.series.Series = ...):
        "usage.dask: 2"

    def replace(
        self,
        /,
        to_replace: Union[(Dict[(int, int)], int, Literal[("c",)])],
        value: Union[(None, float, int)] = ...,
        regex: bool = ...,
    ):
        "usage.dask: 5"

    def autocorr(self, /, lag: int):
        "usage.dask: 4"

    def nsmallest(self, /, n: int):
        "usage.dask: 2"

    def diff(self=..., /):
        "usage.dask: 7"

    def first(self, /, offset: str):
        "usage.dask: 24"

    def last(self, /, offset: str):
        "usage.dask: 8"

    def explode(self, /):
        "usage.dask: 5"

    def __itruediv__(self, _0: pandas.core.series.Series, /):
        ""

    def reindex(
        self,
        /,
        index: Union[
            (
                pandas.core.indexes.datetimes.DatetimeIndex,
                pandas.core.indexes.multi.MultiIndex,
                pandas.core.indexes.numeric.Int64Index,
                numpy.ndarray,
            )
        ],
    ):
        "usage.dask: 8"

    def idxmax(self, /):
        "usage.dask: 1"

    def items(self, /):
        "usage.dask: 1"

    def append(self, /, to_append: pandas.core.series.Series):
        "usage.dask: 2"

    def __array_wrap__(self, /, result: numpy.ndarray):
        "usage.dask: 3"
