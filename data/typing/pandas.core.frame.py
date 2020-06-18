from typing import *


class DataFrame:
    def __init__(
        data: Union[(Dict[(Literal[("x",)], List[Literal[("a",)]])], List[List[int]])]
    ):
        "usage.xarray: 1, usage.dask: 1"

    __name__ = ...
    shape = ...
    __module__ = ...

    @classmethod
    def __ne__(_0: type, /):
        ""

    @classmethod
    def from_dict(
        data: List[
            Dict[(Literal[("y", "x")], Union[(Literal[("a", "b", "c", "d")], int)])]
        ]
    ):
        "usage.dask: 1"

    index = ...
    columns = ...
    values = ...
    loc = ...
    _data = ...
    iloc = ...
    dtypes = ...
    x: pandas.core.series.Series = ...
    empty = ...
    id = ...
    amount = ...
    path = ...
    _constructor_sliced = ...
    fruit = ...
    Date: pandas.core.series.Series = ...
    a: pandas.core.series.Series = ...
    dt_col = ...
    str_col = ...
    string_col = ...
    b = ...
    T = ...
    A = ...
    div = ...
    divide = ...
    rdiv = ...
    X = ...
    c = ...
    __class__ = ...
    y: pandas.core.series.Series = ...
    z = ...
    w: pandas.core.series.Series = ...
    tz = ...
    ndim = ...
    B = ...
    size = ...
    d = ...
    col2 = ...
    col1 = ...
    C = ...
    F = ...
    A_a = ...
    i32 = ...
    _partitions = ...
    e = ...
    f = ...

    def reset_index(self, /, level: int = ..., drop: bool = ...):
        "usage.xarray: 3, usage.dask: 28"

    def set_index(self, /, keys=...):
        "usage.xarray: 10, usage.dask: 115"

    def __getitem__(self, _0, /):
        ""

    def stack(self=..., /):
        "usage.xarray: 1, usage.dask: 1"

    def __setitem__(
        self,
        _0: Union[
            (
                pandas.core.indexes.numeric.Int64Index,
                pandas.core.frame.DataFrame,
                pandas.core.indexes.base.Index,
                List[Literal[("b", "a")]],
                str,
            )
        ],
        _1,
        /,
    ):
        ""

    def equals(self, /, other: pandas.core.frame.DataFrame):
        "usage.xarray: 8, usage.dask: 2"

    def reindex(
        self=...,
        /,
        labels: Union[
            (
                List[str],
                pandas.core.indexes.numeric.Int64Index,
                pandas.core.indexes.multi.MultiIndex,
                pandas.core.indexes.datetimes.DatetimeIndex,
                reversed,
            )
        ] = ...,
        fill_value: Union[(int, float)] = ...,
    ):
        "usage.xarray: 2, usage.dask: 12"

    def items(self, /):
        "usage.xarray: 1"

    def iteritems(self, /):
        "usage.xarray: 1, usage.dask: 2"

    def to_xarray(self, /):
        "usage.xarray: 5"

    def apply(
        self,
        /,
        func: Callable = ...,
        raw: bool = ...,
        result_type: None = ...,
        args: Tuple[(None, ...)] = ...,
    ):
        "usage.xarray: 1, usage.dask: 10"

    def rolling(
        self,
        /,
        window: Union[(pandas.tseries.offsets.Second, float, int, str)],
        min_periods: Union[(int, None)] = ...,
        center: bool = ...,
        win_type: None = ...,
        axis: Union[(int, Literal[("rows", "columns", "coulombs")])] = ...,
    ):
        "usage.xarray: 3, usage.dask: 85"

    def rename(
        self,
        /,
        columns: Union[
            (Dict[(str, Union[(int, str)])], collections.OrderedDict, Callable)
        ] = ...,
    ):
        "usage.dask: 18"

    def astype(
        self,
        /,
        dtype: Union[
            (
                Dict[
                    (
                        Union[(int, str)],
                        Union[
                            (
                                Literal[("category", "f8")],
                                numpy.dtype,
                                pandas.core.dtypes.dtypes.CategoricalDtype,
                                Type[float],
                            )
                        ],
                    )
                ],
                pandas.core.series.Series,
                Literal[("float", "float64")],
                type,
            )
        ] = ...,
    ):
        "usage.dask: 32"

    def itertuples(
        self, /, index: bool = ..., name: Union[(None, Literal[("Pandas",)])] = ...
    ):
        "usage.dask: 9"

    def sort_values(
        self,
        /,
        by: Union[
            (
                List[
                    Union[
                        (Tuple[(Literal[("a", "A", "B", "b")], str)], float, int, str)
                    ]
                ],
                Literal[("KEY",)],
            )
        ],
    ):
        "usage.dask: 179"

    def sort_index(self=..., /):
        "usage.dask: 8"

    def select_dtypes(
        self,
        /,
        include: Union[
            (
                List[
                    Union[
                        (
                            type,
                            Literal[
                                ("category", "bool", "number", "object", "datetime")
                            ],
                        )
                    ]
                ],
                None,
            )
        ] = ...,
    ):
        "usage.dask: 20"

    def fillna(
        self,
        /,
        value: Union[(pandas.core.series.Series, int, None, Literal[("-",)])] = ...,
        method: Union[(None, Literal[("ffill", "pad", "bfill")])] = ...,
        axis: int = ...,
        limit: Union[(None, int)] = ...,
    ):
        "usage.dask: 31"

    def head(self=..., /):
        "usage.dask: 18"

    def assign(self, /):
        "usage.dask: 16"

    def drop(
        self,
        /,
        columns: Union[(List[str], Literal[("category_2", "dt")])] = ...,
        inplace: bool = ...,
        labels: Union[
            (
                Literal[("a", "_index", "y", "timedelta", "_partitions")],
                List[Union[(int, Literal[("z", "y", "x", "a")])]],
                int,
            )
        ] = ...,
        axis: int = ...,
        errors: Literal[("raise", "ignore")] = ...,
    ):
        "usage.dask: 32"

    def copy(self=..., /):
        "usage.dask: 16"

    def groupby(
        self=...,
        /,
        by=...,
        group_keys: bool = ...,
        level: Union[(List[int], int)] = ...,
        sort: bool = ...,
        *,
        dropna: bool = ...,
    ):
        "usage.dask: 448"

    def get(self, /, key: str):
        "usage.dask: 10"

    def to_csv(
        self,
        /,
        path_or_buf: Union[
            (
                _io.TextIOWrapper,
                Literal[("/var/folders/xn/05ktz3056kqd9n8frgd6236h0000gn/T/t",)],
            )
        ] = ...,
        index: bool = ...,
    ):
        "usage.dask: 5"

    def __eq__(
        self,
        _0: Union[(dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame, int)],
        /,
    ):
        ""

    def all(self, /, axis: int = ..., skipna: bool = ...):
        "usage.dask: 11"

    def to_records(self=..., /):
        "usage.dask: 4"

    def to_json(
        self,
        /,
        path_or_buf: Literal[
            (
                "/private/var/folders/xn/05ktz3056kqd9n8frgd6236h00",
                "/var/folders/xn/05ktz3056kqd9n8frgd6236h0000gn/T/t",
            )
        ],
        orient: Literal[("values", "columns", "index", "records", "split")],
        lines: bool,
    ):
        "usage.dask: 24"

    def __add__(
        self,
        _0: Union[
            (
                numpy.ndarray,
                dask.dataframe.core.Scalar,
                pandas.core.frame.DataFrame,
                int,
                float,
            )
        ],
        /,
    ):
        ""

    def __radd__(
        self,
        _0: Union[
            (
                dask.dataframe.core.Scalar,
                int,
                pandas.core.frame.DataFrame,
                dask.dataframe.core.DataFrame,
            )
        ],
        /,
    ):
        ""

    def __mul__(self, _0: Union[(int, pandas.core.frame.DataFrame)], /):
        ""

    def __rmul__(
        self,
        _0: Union[(dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame, int)],
        /,
    ):
        ""

    def __sub__(
        self,
        _0: Union[(pandas.core.series.Series, pandas.core.frame.DataFrame, int)],
        /,
    ):
        ""

    def __rsub__(
        self,
        _0: Union[(dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame, int)],
        /,
    ):
        ""

    def __truediv__(self, _0: Union[(int, pandas.core.frame.DataFrame)], /):
        ""

    def __rtruediv__(
        self,
        _0: Union[(dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame, int)],
        /,
    ):
        ""

    def __floordiv__(self, _0: Union[(int, pandas.core.frame.DataFrame)], /):
        ""

    def __rfloordiv__(
        self,
        _0: Union[(dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame, int)],
        /,
    ):
        ""

    def __pow__(self, _0: Union[(int, pandas.core.frame.DataFrame)], /):
        ""

    def __rpow__(
        self,
        _0: Union[(dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame, int)],
        /,
    ):
        ""

    def __mod__(self, _0: Union[(int, pandas.core.frame.DataFrame)], /):
        ""

    def __rmod__(
        self,
        _0: Union[(dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame, int)],
        /,
    ):
        ""

    def __and__(self, _0: Union[(bool, pandas.core.frame.DataFrame)], /):
        ""

    def __rand__(
        self,
        _0: Union[(dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame, bool)],
        /,
    ):
        ""

    def __or__(self, _0: Union[(bool, pandas.core.frame.DataFrame)], /):
        ""

    def __ror__(
        self,
        _0: Union[(dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame, bool)],
        /,
    ):
        ""

    def __xor__(self, _0: Union[(bool, pandas.core.frame.DataFrame)], /):
        ""

    def __rxor__(
        self,
        _0: Union[(dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame, bool)],
        /,
    ):
        ""

    def __gt__(
        self,
        _0: Union[(pandas.core.series.Series, pandas.core.frame.DataFrame, int)],
        /,
    ):
        ""

    def __lt__(
        self,
        _0: Union[(dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame, int)],
        /,
    ):
        ""

    def __le__(self, _0, /):
        ""

    def __ge__(
        self,
        _0: Union[(dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame, int)],
        /,
    ):
        ""

    def __ne__(
        self,
        _0: Union[(dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame, int)],
        /,
    ):
        ""

    def lt(self, /, other: Union[(int, pandas.core.frame.DataFrame)]):
        "usage.dask: 2"

    def gt(self, /, other: Union[(int, pandas.core.frame.DataFrame)]):
        "usage.dask: 2"

    def le(self, /, other: Union[(int, pandas.core.frame.DataFrame)]):
        "usage.dask: 2"

    def ge(self, /, other: Union[(int, pandas.core.frame.DataFrame)]):
        "usage.dask: 2"

    def ne(self, /, other: Union[(int, pandas.core.frame.DataFrame)]):
        "usage.dask: 2"

    def eq(self, /, other: Union[(int, pandas.core.frame.DataFrame)]):
        "usage.dask: 2"

    def __neg__(self, /):
        ""

    def __invert__(self, /):
        ""

    def any(self, /, axis: int = ..., skipna: bool = ...):
        "usage.dask: 9"

    def add(
        self=...,
        /,
        other: Union[
            (pandas.core.frame.DataFrame, int, pandas.core.series.Series)
        ] = ...,
    ):
        "usage.dask: 11"

    def sub(
        self=...,
        /,
        other: Union[
            (pandas.core.series.Series, pandas.core.frame.DataFrame, int)
        ] = ...,
    ):
        "usage.dask: 9"

    def mul(
        self=...,
        /,
        other: Union[
            (pandas.core.frame.DataFrame, int, pandas.core.series.Series)
        ] = ...,
    ):
        "usage.dask: 11"

    def truediv(
        self=...,
        /,
        other: Union[
            (pandas.core.series.Series, pandas.core.frame.DataFrame, int)
        ] = ...,
    ):
        "usage.dask: 27"

    def floordiv(
        self=...,
        /,
        other: Union[
            (pandas.core.series.Series, pandas.core.frame.DataFrame, int)
        ] = ...,
    ):
        "usage.dask: 9"

    def pow(
        self=...,
        /,
        other: Union[
            (pandas.core.series.Series, pandas.core.frame.DataFrame, int)
        ] = ...,
    ):
        "usage.dask: 9"

    def mod(
        self=...,
        /,
        other: Union[
            (pandas.core.series.Series, pandas.core.frame.DataFrame, int)
        ] = ...,
    ):
        "usage.dask: 9"

    def radd(
        self=...,
        /,
        other: Union[
            (pandas.core.series.Series, pandas.core.frame.DataFrame, int)
        ] = ...,
    ):
        "usage.dask: 9"

    def rsub(
        self=...,
        /,
        other: Union[
            (pandas.core.series.Series, pandas.core.frame.DataFrame, int)
        ] = ...,
    ):
        "usage.dask: 9"

    def rmul(
        self=...,
        /,
        other: Union[
            (pandas.core.series.Series, pandas.core.frame.DataFrame, int)
        ] = ...,
    ):
        "usage.dask: 9"

    def rtruediv(
        self=...,
        /,
        other: Union[
            (pandas.core.series.Series, pandas.core.frame.DataFrame, int)
        ] = ...,
    ):
        "usage.dask: 18"

    def rpow(
        self=...,
        /,
        other: Union[
            (pandas.core.series.Series, pandas.core.frame.DataFrame, int)
        ] = ...,
    ):
        "usage.dask: 9"

    def rmod(
        self=...,
        /,
        other: Union[
            (pandas.core.series.Series, pandas.core.frame.DataFrame, int)
        ] = ...,
    ):
        "usage.dask: 9"

    def sum(
        self=...,
        /,
        axis: Union[(int, Literal[("columns", "index")])] = ...,
        min_count: int = ...,
    ):
        "usage.dask: 33"

    def prod(
        self=...,
        /,
        axis: Union[(int, Literal[("columns", "index")])] = ...,
        min_count: int = ...,
    ):
        "usage.dask: 15"

    def min(self=..., /):
        "usage.dask: 15"

    def max(self=..., /):
        "usage.dask: 15"

    def mean(self=..., /):
        "usage.dask: 20"

    def _get_numeric_data(self, /):
        "usage.dask: 4"

    def count(self=..., /):
        "usage.dask: 17"

    def var(
        self,
        /,
        axis: Union[(Literal[("columns", "index")], int)] = ...,
        skipna: Union[(bool, None)] = ...,
        ddof: int = ...,
    ):
        "usage.dask: 31"

    def std(
        self,
        /,
        axis: Union[(Literal[("columns", "index")], int)] = ...,
        skipna: bool = ...,
        ddof: int = ...,
    ):
        "usage.dask: 23"

    def sem(
        self,
        /,
        axis: Union[(int, Literal[("columns", "index")])] = ...,
        skipna: Union[(bool, None)] = ...,
        ddof: int = ...,
    ):
        "usage.dask: 23"

    def drop_duplicates(
        self,
        /,
        subset: Union[
            (Literal[("ticker", "y")], None, List[Literal[("x", "y", "z")]])
        ] = ...,
        keep: Union[(Literal[("last", "first")], bool)] = ...,
    ):
        "usage.dask: 43"

    def take(self, /, indices: numpy.ndarray):
        "usage.dask: 1"

    def to_string(self, /, max_rows: int, show_dimensions: bool):
        "usage.dask: 2"

    def tail(self, /, n: int):
        "usage.dask: 5"

    def describe(
        self,
        /,
        percentiles: Union[(None, List[float])] = ...,
        include: Union[
            (
                List[
                    Union[
                        (
                            Type[numpy.timedelta64],
                            Literal[("number", "object", "bool", "datetime")],
                        )
                    ]
                ],
                None,
                Literal[("all",)],
            )
        ] = ...,
        exclude: Union[(None, List[Literal[("object", "number")]])] = ...,
    ):
        "usage.dask: 21"

    def quantile(
        self,
        /,
        q: Union[(List[Union[(float, numpy.float64)]], float)] = ...,
        axis: int = ...,
    ):
        "usage.dask: 7"

    def __iter__(self, /):
        ""

    def cumsum(self, /, axis: Union[(int, None)] = ..., skipna: bool = ...):
        "usage.dask: 11"

    def cumprod(self, /, axis: Union[(int, None)] = ..., skipna: bool = ...):
        "usage.dask: 11"

    def cummin(self, /, axis: Union[(int, None)] = ..., skipna: bool = ...):
        "usage.dask: 11"

    def isnull(self, /):
        "usage.dask: 6"

    def where(
        self=...,
        /,
        cond: Union[(pandas.core.series.Series, pandas.core.frame.DataFrame)] = ...,
    ):
        "usage.dask: 8"

    def cummax(self, /, axis: Union[(int, None)] = ..., skipna: bool = ...):
        "usage.dask: 11"

    def dropna(
        self,
        /,
        how: Literal[("any", "all")] = ...,
        thresh: Union[(int, None)] = ...,
        subset: Union[(None, List[Literal[("x", "z", "y")]])] = ...,
    ):
        "usage.dask: 21"

    def clip(
        self,
        /,
        lower: Union[(None, int, float)] = ...,
        upper: Union[(float, int, None)] = ...,
    ):
        "usage.dask: 12"

    def squeeze(self, /):
        "usage.dask: 3"

    def mask(
        self,
        /,
        cond: Union[(pandas.core.series.Series, pandas.core.frame.DataFrame)] = ...,
    ):
        "usage.dask: 6"

    def rename_axis(
        self, /, mapper: Union[(Literal[("myindex", "newindex")], List[None])] = ...
    ):
        "usage.dask: 5"

    def isin(
        self, /, values: Union[(Dict[(Literal[("b", "a")], List[int])], List[int])]
    ):
        "usage.dask: 6"

    def notnull(self, /):
        "usage.dask: 2"

    def align(
        self,
        /,
        other: pandas.core.frame.DataFrame,
        join: Literal[("right", "left", "outer", "inner")],
        axis: Union[(Literal[("XXX", "columns", "index")], None, int)] = ...,
        fill_value: Union[(None, int)] = ...,
    ):
        "usage.dask: 48"

    def combine(
        self, /, other: pandas.core.frame.DataFrame = ..., func: Callable = ...
    ):
        "usage.dask: 7"

    def combine_first(self, /, other: pandas.core.frame.DataFrame):
        "usage.dask: 3"

    def sample(
        self, /, frac: float, random_state: numpy.random.mtrand.RandomState = ...
    ):
        "usage.dask: 2"

    def memory_usage(self, /, index: bool = ...):
        "usage.dask: 5"

    def ffill(self=..., /):
        "usage.dask: 2"

    def bfill(self=..., /):
        "usage.dask: 2"

    def to_timestamp(
        self, /, freq: None = ..., how: Literal[("start",)] = ..., axis: int = ...
    ):
        "usage.dask: 2"

    def applymap(self, /, func: Callable):
        "usage.dask: 3"

    def abs(self, /):
        "usage.dask: 3"

    def round(self=..., /):
        "usage.dask: 3"

    def cov(self=..., /):
        "usage.dask: 6"

    def corr(self=..., /):
        "usage.dask: 5"

    def nlargest(
        self, /, n: int, columns: Union[(List[Literal[("c", "a")]], Literal[("a",)])]
    ):
        "usage.dask: 4"

    def nsmallest(
        self, /, n: int, columns: Union[(List[Literal[("c", "a")]], Literal[("a",)])]
    ):
        "usage.dask: 4"

    def iterrows(self, /):
        "usage.dask: 2"

    def info(self, /, buf: _io.StringIO, memory_usage: bool):
        "usage.dask: 1"

    def idxmax(self=..., /):
        "usage.dask: 7"

    def idxmin(self=..., /):
        "usage.dask: 5"

    def diff(self, /, periods: int = ..., axis: int = ...):
        "usage.dask: 7"

    def shift(
        self,
        /,
        periods: int = ...,
        freq: Union[
            (
                Literal[("H", "D", "B", "W", "S")],
                None,
                pandas._libs.tslibs.timedeltas.Timedelta,
            )
        ] = ...,
        axis: int = ...,
    ):
        "usage.dask: 29"

    def first(self, /, offset: str):
        "usage.dask: 24"

    def last(self, /, offset: str):
        "usage.dask: 8"

    def query(self, /, expr: Literal[("B != 9", "B != 0")]):
        "usage.dask: 4"

    def replace(
        self,
        /,
        to_replace: Union[(Dict[(int, int)], int)],
        value: Union[(None, int)] = ...,
        regex: bool = ...,
    ):
        "usage.dask: 4"

    def explode(self, /, column: Literal[("A",)]):
        "usage.dask: 2"

    def to_html(self, /, max_rows: int, show_dimensions: bool = ...):
        "usage.dask: 2"

    def __itruediv__(self, _0: pandas.core.frame.DataFrame, /):
        ""

    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: str,
        on: Union[
            (Literal[("KEY", "x", "emp_id", "idx")], List[Literal[("idx", "k")]], None)
        ] = ...,
        left_on: Union[(str, List[str], None)] = ...,
        right_on: Union[(str, List[str], None)] = ...,
        left_index: bool = ...,
        right_index: bool = ...,
        suffixes: Union[
            (
                Tuple[(Literal[("_x", "1")], Literal[("_y", "2")])],
                List[Literal[("_r", "_l", "", "r", "l")]],
            )
        ] = ...,
        indicator: bool = ...,
    ):
        "usage.dask: 365"

    def join(
        self,
        /,
        other: pandas.core.frame.DataFrame,
        how: Literal[("right", "left", "outer", "inner")] = ...,
        lsuffix: Literal[("l", "_l")] = ...,
        rsuffix: Literal[("r", "_r")] = ...,
    ):
        "usage.dask: 31"

    def __contains__(
        self, _0: Union[(pandas._libs.tslibs.timestamps.Timestamp, int, numpy.int64)], /
    ):
        ""

    def isna(self, /):
        "usage.dask: 1"

    def melt(
        self,
        /,
        id_vars: Union[(Literal[("B", "C")], None)] = ...,
        value_vars: Union[(List[Literal[("C", "A")]], Literal[("C",)], None)] = ...,
        var_name: Union[(Literal[("myvar",)], None)] = ...,
        value_name: Literal[("myval", "value")] = ...,
        col_level: None = ...,
    ):
        "usage.dask: 10"

    def append(
        self,
        /,
        other: Union[(pandas.core.frame.DataFrame, pandas.core.series.Series)] = ...,
    ):
        "usage.dask: 12"

    def pivot_table(
        self,
        /,
        values: Literal[("B",)],
        index: Literal[("A",)],
        columns: Literal[("C",)],
        aggfunc: Literal[("count", "sum", "mean")],
    ):
        "usage.dask: 3"

    def __array_wrap__(self, /, result: numpy.ndarray):
        "usage.dask: 2"

    def resample(
        self,
        /,
        rule,
        closed: Union[(None, Literal[("left", "right")])] = ...,
        label: Union[(None, Literal[("left", "right")])] = ...,
    ):
        "usage.dask: 63"


class Pandas:
    def __iter__(self, /):
        ""

    def __eq__(self, _0: pandas.core.frame.Pandas, /):
        ""
