from typing import *


class DataFrame:
    def __init__(
        self, /, data: Union[Dict[Literal["x"], List[Literal["a"]]], List[List[int]]]
    ):
        """
        usage.xarray: 1
        usage.dask: 1
        """
        ...

    # usage.dask: 4
    __module__: ClassVar[object]

    # usage.dask: 4
    __name__: ClassVar[object]

    # usage.dask: 6
    shape: ClassVar[object]

    @classmethod
    def __ne__(
        cls,
        _0: Union[
            type, int, pandas.core.frame.DataFrame, dask.dataframe.core.DataFrame
        ],
        /,
    ):
        """
        usage.dask: 8
        """
        ...

    @classmethod
    def from_dict(
        cls,
        /,
        data: List[Dict[Literal["y", "x"], Union[Literal["a", "b", "c", "d"], int]]],
    ):
        """
        usage.dask: 1
        """
        ...

    # usage.dask: 40
    A: object

    # usage.dask: 3
    A_a: object

    # usage.dask: 15
    B: object

    # usage.dask: 4
    C: object

    # usage.dask: 2
    Date: pandas.core.series.Series

    # usage.dask: 1
    F: object

    # usage.dask: 5
    T: object

    # usage.dask: 2
    X: object

    # usage.dask: 7
    __class__: object

    # usage.dask: 1
    _constructor_sliced: object

    # usage.dask: 1
    _data: object

    # usage.dask: 2
    _partitions: object

    # usage.dask: 116
    a: pandas.core.series.Series

    # usage.dask: 1
    amount: object

    # usage.dask: 66
    b: object

    # usage.dask: 1
    c: object

    # usage.dask: 1
    col1: object

    # usage.dask: 1
    col2: object

    # usage.xarray: 9
    # usage.dask: 141
    columns: object

    # usage.dask: 4
    d: object

    # usage.dask: 3
    div: object

    # usage.dask: 3
    divide: object

    # usage.dask: 2
    dt_col: object

    # usage.dask: 26
    dtypes: object

    # usage.dask: 2
    e: object

    # usage.dask: 7
    empty: object

    # usage.dask: 3
    f: object

    # usage.dask: 2
    fruit: object

    # usage.dask: 2
    i32: object

    # usage.dask: 2
    id: object

    # usage.dask: 41
    iloc: object

    # usage.xarray: 10
    # usage.dask: 189
    index: object

    # usage.xarray: 1
    # usage.dask: 68
    loc: object

    # usage.dask: 3
    ndim: object

    # usage.dask: 2
    path: object

    # usage.dask: 3
    rdiv: object

    # usage.dask: 2
    size: object

    # usage.dask: 12
    str_col: object

    # usage.dask: 4
    string_col: object

    # usage.dask: 1
    tz: object

    # usage.xarray: 2
    # usage.dask: 31
    values: object

    # usage.dask: 7
    w: pandas.core.series.Series

    # usage.dask: 81
    x: pandas.core.series.Series

    # usage.dask: 37
    y: pandas.core.series.Series

    # usage.dask: 4
    z: object

    def __add__(
        self,
        _0: Union[
            numpy.ndarray,
            dask.dataframe.core.Scalar,
            pandas.core.frame.DataFrame,
            int,
            float,
        ],
        /,
    ):
        """
        usage.dask: 26
        """
        ...

    def __and__(self, _0: Union[bool, pandas.core.frame.DataFrame], /):
        """
        usage.dask: 2
        """
        ...

    def __array_wrap__(self, /, result: numpy.ndarray):
        """
        usage.dask: 2
        """
        ...

    def __contains__(
        self, _0: Union[pandas._libs.tslibs.timestamps.Timestamp, int, numpy.int64], /
    ):
        """
        usage.dask: 6
        """
        ...

    def __eq__(
        self,
        _0: Union[dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame, int],
        /,
    ):
        """
        usage.dask: 17
        """
        ...

    def __floordiv__(self, _0: Union[int, pandas.core.frame.DataFrame], /):
        """
        usage.dask: 2
        """
        ...

    def __ge__(
        self,
        _0: Union[dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame, int],
        /,
    ):
        """
        usage.dask: 7
        """
        ...

    def __getitem__(self, _0: object, /):
        """
        usage.xarray: 8
        usage.dask: 520
        """
        ...

    def __gt__(
        self, _0: Union[pandas.core.series.Series, pandas.core.frame.DataFrame, int], /
    ):
        """
        usage.dask: 3
        """
        ...

    def __invert__(self, /):
        """
        usage.dask: 1
        """
        ...

    def __iter__(self, /):
        """
        usage.dask: 1
        """
        ...

    def __itruediv__(self, _0: pandas.core.frame.DataFrame, /):
        """
        usage.dask: 1
        """
        ...

    def __le__(self, _0: object, /):
        """
        usage.dask: 12
        """
        ...

    def __lt__(
        self,
        _0: Union[dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame, int],
        /,
    ):
        """
        usage.dask: 3
        """
        ...

    def __mod__(self, _0: Union[int, pandas.core.frame.DataFrame], /):
        """
        usage.dask: 2
        """
        ...

    def __mul__(self, _0: Union[int, pandas.core.frame.DataFrame], /):
        """
        usage.dask: 2
        """
        ...

    def __neg__(self, /):
        """
        usage.dask: 5
        """
        ...

    def __or__(self, _0: Union[bool, pandas.core.frame.DataFrame], /):
        """
        usage.dask: 4
        """
        ...

    def __pow__(self, _0: Union[int, pandas.core.frame.DataFrame], /):
        """
        usage.dask: 4
        """
        ...

    def __radd__(
        self,
        _0: Union[
            dask.dataframe.core.Scalar,
            int,
            pandas.core.frame.DataFrame,
            dask.dataframe.core.DataFrame,
        ],
        /,
    ):
        """
        usage.dask: 5
        """
        ...

    def __rand__(
        self,
        _0: Union[dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame, bool],
        /,
    ):
        """
        usage.dask: 3
        """
        ...

    def __rfloordiv__(
        self,
        _0: Union[dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame, int],
        /,
    ):
        """
        usage.dask: 3
        """
        ...

    def __rmod__(
        self,
        _0: Union[dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame, int],
        /,
    ):
        """
        usage.dask: 3
        """
        ...

    def __rmul__(
        self,
        _0: Union[dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame, int],
        /,
    ):
        """
        usage.dask: 3
        """
        ...

    def __ror__(
        self,
        _0: Union[dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame, bool],
        /,
    ):
        """
        usage.dask: 5
        """
        ...

    def __rpow__(
        self,
        _0: Union[dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame, int],
        /,
    ):
        """
        usage.dask: 3
        """
        ...

    def __rsub__(
        self,
        _0: Union[dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame, int],
        /,
    ):
        """
        usage.dask: 4
        """
        ...

    def __rtruediv__(
        self,
        _0: Union[dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame, int],
        /,
    ):
        """
        usage.dask: 4
        """
        ...

    def __rxor__(
        self,
        _0: Union[dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame, bool],
        /,
    ):
        """
        usage.dask: 3
        """
        ...

    def __setitem__(
        self,
        _0: Union[
            pandas.core.indexes.numeric.Int64Index,
            pandas.core.frame.DataFrame,
            pandas.core.indexes.base.Index,
            List[Literal["b", "a"]],
            str,
        ],
        _1: object,
        /,
    ):
        """
        usage.xarray: 1
        usage.dask: 128
        """
        ...

    def __sub__(
        self, _0: Union[pandas.core.series.Series, pandas.core.frame.DataFrame, int], /
    ):
        """
        usage.dask: 10
        """
        ...

    def __truediv__(self, _0: Union[int, pandas.core.frame.DataFrame], /):
        """
        usage.dask: 3
        """
        ...

    def __xor__(self, _0: Union[bool, pandas.core.frame.DataFrame], /):
        """
        usage.dask: 2
        """
        ...

    def _get_numeric_data(self, /):
        """
        usage.dask: 4
        """
        ...

    def abs(self, /):
        """
        usage.dask: 3
        """
        ...

    def add(
        self,
        /,
        other: Union[pandas.core.frame.DataFrame, int, pandas.core.series.Series],
    ):
        """
        usage.dask: 11
        """
        ...

    def align(
        self,
        /,
        other: pandas.core.frame.DataFrame,
        join: Literal["right", "left", "outer", "inner"],
        axis: Union[Literal["XXX", "columns", "index"], None, int] = ...,
        fill_value: Union[None, int] = ...,
    ):
        """
        usage.dask: 48
        """
        ...

    def all(self, /, axis: int = ..., skipna: bool = ...):
        """
        usage.dask: 11
        """
        ...

    def any(self, /, axis: int = ..., skipna: bool = ...):
        """
        usage.dask: 9
        """
        ...

    def append(
        self, /, other: Union[pandas.core.frame.DataFrame, pandas.core.series.Series]
    ):
        """
        usage.dask: 12
        """
        ...

    def apply(
        self,
        /,
        func: Callable,
        raw: bool = ...,
        result_type: None = ...,
        args: Tuple[None, ...] = ...,
    ):
        """
        usage.xarray: 1
        usage.dask: 10
        """
        ...

    def applymap(self, /, func: Callable):
        """
        usage.dask: 3
        """
        ...

    def assign(self, /):
        """
        usage.dask: 16
        """
        ...

    def astype(
        self,
        /,
        dtype: Union[
            Dict[
                Union[int, str],
                Union[
                    Literal["category", "f8"],
                    numpy.dtype,
                    pandas.core.dtypes.dtypes.CategoricalDtype,
                    Type[float],
                ],
            ],
            pandas.core.series.Series,
            Literal["float", "float64"],
            type,
        ],
    ):
        """
        usage.dask: 32
        """
        ...

    def bfill(self, /):
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
        usage.dask: 12
        """
        ...

    def combine(self, /, other: pandas.core.frame.DataFrame, func: Callable):
        """
        usage.dask: 7
        """
        ...

    def combine_first(self, /, other: pandas.core.frame.DataFrame):
        """
        usage.dask: 3
        """
        ...

    def copy(self, /):
        """
        usage.dask: 16
        """
        ...

    def corr(self, /):
        """
        usage.dask: 5
        """
        ...

    def count(self, /):
        """
        usage.dask: 17
        """
        ...

    def cov(self, /):
        """
        usage.dask: 6
        """
        ...

    def cummax(self, /, axis: Union[int, None] = ..., skipna: bool = ...):
        """
        usage.dask: 11
        """
        ...

    def cummin(self, /, axis: Union[int, None] = ..., skipna: bool = ...):
        """
        usage.dask: 11
        """
        ...

    def cumprod(self, /, axis: Union[int, None] = ..., skipna: bool = ...):
        """
        usage.dask: 11
        """
        ...

    def cumsum(self, /, axis: Union[int, None] = ..., skipna: bool = ...):
        """
        usage.dask: 11
        """
        ...

    def describe(
        self,
        /,
        percentiles: Union[None, List[float]] = ...,
        include: Union[
            List[
                Union[
                    Type[numpy.timedelta64],
                    Literal["number", "object", "bool", "datetime"],
                ]
            ],
            None,
            Literal["all"],
        ] = ...,
        exclude: Union[None, List[Literal["object", "number"]]] = ...,
    ):
        """
        usage.dask: 21
        """
        ...

    def diff(self, /, periods: int = ..., axis: int = ...):
        """
        usage.dask: 7
        """
        ...

    def drop(
        self,
        /,
        columns: Union[List[str], Literal["category_2", "dt"]] = ...,
        inplace: bool = ...,
        labels: Union[
            Literal["a", "_index", "y", "timedelta", "_partitions"],
            List[Union[int, Literal["z", "y", "x", "a"]]],
            int,
        ] = ...,
        axis: int = ...,
        errors: Literal["raise", "ignore"] = ...,
    ):
        """
        usage.dask: 32
        """
        ...

    def drop_duplicates(
        self,
        /,
        subset: Union[Literal["ticker", "y"], None, List[Literal["x", "y", "z"]]] = ...,
        keep: Union[Literal["last", "first"], bool] = ...,
    ):
        """
        usage.dask: 43
        """
        ...

    def dropna(
        self,
        /,
        how: Literal["any", "all"] = ...,
        thresh: Union[int, None] = ...,
        subset: Union[None, List[Literal["x", "z", "y"]]] = ...,
    ):
        """
        usage.dask: 21
        """
        ...

    def eq(self, /, other: Union[int, pandas.core.frame.DataFrame]):
        """
        usage.dask: 2
        """
        ...

    def equals(self, /, other: pandas.core.frame.DataFrame):
        """
        usage.xarray: 8
        usage.dask: 2
        """
        ...

    def explode(self, /, column: Literal["A"]):
        """
        usage.dask: 2
        """
        ...

    def ffill(self, /):
        """
        usage.dask: 2
        """
        ...

    def fillna(
        self,
        /,
        value: Union[pandas.core.series.Series, int, None, Literal["-"]] = ...,
        method: Union[None, Literal["ffill", "pad", "bfill"]] = ...,
        axis: int = ...,
        limit: Union[None, int] = ...,
    ):
        """
        usage.dask: 31
        """
        ...

    def first(self, /, offset: str):
        """
        usage.dask: 24
        """
        ...

    def floordiv(
        self,
        /,
        other: Union[pandas.core.series.Series, pandas.core.frame.DataFrame, int],
    ):
        """
        usage.dask: 9
        """
        ...

    def ge(self, /, other: Union[int, pandas.core.frame.DataFrame]):
        """
        usage.dask: 2
        """
        ...

    def get(self, /, key: str):
        """
        usage.dask: 10
        """
        ...

    def groupby(
        self,
        /,
        level: Union[List[int], int] = ...,
        by: object = ...,
        group_keys: bool = ...,
        sort: bool = ...,
        *,
        dropna: bool = ...,
    ):
        """
        usage.dask: 448
        """
        ...

    def gt(self, /, other: Union[int, pandas.core.frame.DataFrame]):
        """
        usage.dask: 2
        """
        ...

    def head(self, /):
        """
        usage.dask: 18
        """
        ...

    def idxmax(self, /):
        """
        usage.dask: 7
        """
        ...

    def idxmin(self, /):
        """
        usage.dask: 5
        """
        ...

    def info(self, /, buf: _io.StringIO, memory_usage: bool):
        """
        usage.dask: 1
        """
        ...

    def isin(self, /, values: Union[Dict[Literal["b", "a"], List[int]], List[int]]):
        """
        usage.dask: 6
        """
        ...

    def isna(self, /):
        """
        usage.dask: 1
        """
        ...

    def isnull(self, /):
        """
        usage.dask: 6
        """
        ...

    def items(self, /):
        """
        usage.xarray: 1
        """
        ...

    def iteritems(self, /):
        """
        usage.xarray: 1
        usage.dask: 2
        """
        ...

    def iterrows(self, /):
        """
        usage.dask: 2
        """
        ...

    def itertuples(
        self, /, index: bool = ..., name: Union[None, Literal["Pandas"]] = ...
    ):
        """
        usage.dask: 9
        """
        ...

    def join(
        self,
        /,
        other: pandas.core.frame.DataFrame,
        how: Literal["right", "left", "outer", "inner"] = ...,
        lsuffix: Literal["l", "_l"] = ...,
        rsuffix: Literal["r", "_r"] = ...,
    ):
        """
        usage.dask: 31
        """
        ...

    def last(self, /, offset: str):
        """
        usage.dask: 8
        """
        ...

    def le(self, /, other: Union[int, pandas.core.frame.DataFrame]):
        """
        usage.dask: 2
        """
        ...

    def lt(self, /, other: Union[int, pandas.core.frame.DataFrame]):
        """
        usage.dask: 2
        """
        ...

    def mask(
        self, /, cond: Union[pandas.core.series.Series, pandas.core.frame.DataFrame]
    ):
        """
        usage.dask: 6
        """
        ...

    def max(self, /):
        """
        usage.dask: 15
        """
        ...

    def mean(self, /):
        """
        usage.dask: 20
        """
        ...

    def melt(
        self,
        /,
        id_vars: Union[Literal["B", "C"], None] = ...,
        value_vars: Union[List[Literal["C", "A"]], Literal["C"], None] = ...,
        var_name: Union[Literal["myvar"], None] = ...,
        value_name: Literal["myval", "value"] = ...,
        col_level: None = ...,
    ):
        """
        usage.dask: 10
        """
        ...

    def memory_usage(self, /, index: bool):
        """
        usage.dask: 5
        """
        ...

    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: str,
        on: Union[
            Literal["KEY", "x", "emp_id", "idx"], List[Literal["idx", "k"]], None
        ] = ...,
        left_on: Union[str, List[str], None] = ...,
        right_on: Union[str, List[str], None] = ...,
        left_index: bool = ...,
        right_index: bool = ...,
        suffixes: Union[
            Tuple[Literal["_x", "1"], Literal["_y", "2"]],
            List[Literal["_r", "_l", "", "r", "l"]],
        ] = ...,
        indicator: bool = ...,
    ):
        """
        usage.dask: 365
        """
        ...

    def min(self, /):
        """
        usage.dask: 15
        """
        ...

    def mod(
        self,
        /,
        other: Union[pandas.core.series.Series, pandas.core.frame.DataFrame, int],
    ):
        """
        usage.dask: 9
        """
        ...

    def mul(
        self,
        /,
        other: Union[pandas.core.frame.DataFrame, int, pandas.core.series.Series],
    ):
        """
        usage.dask: 11
        """
        ...

    def ne(self, /, other: Union[int, pandas.core.frame.DataFrame]):
        """
        usage.dask: 2
        """
        ...

    def nlargest(
        self, /, n: int, columns: Union[List[Literal["c", "a"]], Literal["a"]]
    ):
        """
        usage.dask: 4
        """
        ...

    def notnull(self, /):
        """
        usage.dask: 2
        """
        ...

    def nsmallest(
        self, /, n: int, columns: Union[List[Literal["c", "a"]], Literal["a"]]
    ):
        """
        usage.dask: 4
        """
        ...

    def pivot_table(
        self,
        /,
        values: Literal["B"],
        index: Literal["A"],
        columns: Literal["C"],
        aggfunc: Literal["count", "sum", "mean"],
    ):
        """
        usage.dask: 3
        """
        ...

    def pow(
        self,
        /,
        other: Union[pandas.core.series.Series, pandas.core.frame.DataFrame, int],
    ):
        """
        usage.dask: 9
        """
        ...

    def prod(
        self,
        /,
        axis: Union[int, Literal["columns", "index"]] = ...,
        min_count: int = ...,
    ):
        """
        usage.dask: 15
        """
        ...

    def quantile(
        self,
        /,
        q: Union[List[Union[float, numpy.float64]], float] = ...,
        axis: int = ...,
    ):
        """
        usage.dask: 7
        """
        ...

    def query(self, /, expr: Literal["B != 9", "B != 0"]):
        """
        usage.dask: 4
        """
        ...

    def radd(
        self,
        /,
        other: Union[pandas.core.series.Series, pandas.core.frame.DataFrame, int],
    ):
        """
        usage.dask: 9
        """
        ...

    def reindex(
        self,
        /,
        labels: Union[
            List[str],
            pandas.core.indexes.numeric.Int64Index,
            pandas.core.indexes.multi.MultiIndex,
            pandas.core.indexes.datetimes.DatetimeIndex,
            reversed,
        ] = ...,
        fill_value: Union[int, float] = ...,
    ):
        """
        usage.xarray: 2
        usage.dask: 12
        """
        ...

    def rename(
        self,
        /,
        columns: Union[Dict[str, Union[int, str]], collections.OrderedDict, Callable],
    ):
        """
        usage.dask: 18
        """
        ...

    def rename_axis(self, /, mapper: Union[Literal["myindex", "newindex"], List[None]]):
        """
        usage.dask: 5
        """
        ...

    def replace(
        self,
        /,
        to_replace: Union[Dict[int, int], int],
        value: Union[None, int] = ...,
        regex: bool = ...,
    ):
        """
        usage.dask: 4
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
        usage.dask: 63
        """
        ...

    def reset_index(self, /, level: int = ..., drop: bool = ...):
        """
        usage.xarray: 3
        usage.dask: 28
        """
        ...

    def rmod(
        self,
        /,
        other: Union[pandas.core.series.Series, pandas.core.frame.DataFrame, int],
    ):
        """
        usage.dask: 9
        """
        ...

    def rmul(
        self,
        /,
        other: Union[pandas.core.series.Series, pandas.core.frame.DataFrame, int],
    ):
        """
        usage.dask: 9
        """
        ...

    def rolling(
        self,
        /,
        window: Union[pandas.tseries.offsets.Second, float, int, str],
        min_periods: Union[int, None] = ...,
        center: bool = ...,
        win_type: None = ...,
        axis: Union[int, Literal["rows", "columns", "coulombs"]] = ...,
    ):
        """
        usage.xarray: 3
        usage.dask: 85
        """
        ...

    def round(self, /):
        """
        usage.dask: 3
        """
        ...

    def rpow(
        self,
        /,
        other: Union[pandas.core.series.Series, pandas.core.frame.DataFrame, int],
    ):
        """
        usage.dask: 9
        """
        ...

    def rsub(
        self,
        /,
        other: Union[pandas.core.series.Series, pandas.core.frame.DataFrame, int],
    ):
        """
        usage.dask: 9
        """
        ...

    def rtruediv(
        self,
        /,
        other: Union[pandas.core.series.Series, pandas.core.frame.DataFrame, int],
    ):
        """
        usage.dask: 18
        """
        ...

    def sample(self, /, frac: float, random_state: numpy.random.mtrand.RandomState):
        """
        usage.dask: 2
        """
        ...

    def select_dtypes(
        self,
        /,
        include: Union[
            List[
                Union[type, Literal["category", "bool", "number", "object", "datetime"]]
            ],
            None,
        ],
    ):
        """
        usage.dask: 20
        """
        ...

    def sem(
        self,
        /,
        axis: Union[int, Literal["columns", "index"]] = ...,
        skipna: Union[bool, None] = ...,
        ddof: int = ...,
    ):
        """
        usage.dask: 23
        """
        ...

    def set_index(self, /, keys: object):
        """
        usage.xarray: 10
        usage.dask: 115
        """
        ...

    def shift(
        self,
        /,
        periods: int = ...,
        freq: Union[
            Literal["H", "D", "B", "W", "S"],
            None,
            pandas._libs.tslibs.timedeltas.Timedelta,
        ] = ...,
        axis: int = ...,
    ):
        """
        usage.dask: 29
        """
        ...

    def sort_index(self, /):
        """
        usage.dask: 8
        """
        ...

    def sort_values(
        self,
        /,
        by: Union[
            List[Union[Tuple[Literal["a", "A", "B", "b"], str], float, int, str]],
            Literal["KEY"],
        ],
    ):
        """
        usage.dask: 179
        """
        ...

    def squeeze(self, /):
        """
        usage.dask: 3
        """
        ...

    def stack(self, /):
        """
        usage.xarray: 1
        usage.dask: 1
        """
        ...

    def std(
        self,
        /,
        axis: Union[Literal["columns", "index"], int] = ...,
        skipna: bool = ...,
        ddof: int = ...,
    ):
        """
        usage.dask: 23
        """
        ...

    def sub(
        self,
        /,
        other: Union[pandas.core.series.Series, pandas.core.frame.DataFrame, int],
    ):
        """
        usage.dask: 9
        """
        ...

    def sum(
        self,
        /,
        axis: Union[int, Literal["columns", "index"]] = ...,
        min_count: int = ...,
    ):
        """
        usage.dask: 33
        """
        ...

    def tail(self, /, n: int):
        """
        usage.dask: 5
        """
        ...

    def take(self, /, indices: numpy.ndarray):
        """
        usage.dask: 1
        """
        ...

    def to_csv(
        self,
        /,
        path_or_buf: Union[
            _io.TextIOWrapper,
            Literal["/var/folders/xn/05ktz3056kqd9n8frgd6236h0000gn/T/t"],
        ],
        index: bool,
    ):
        """
        usage.dask: 5
        """
        ...

    def to_html(self, /, max_rows: int, show_dimensions: bool):
        """
        usage.dask: 2
        """
        ...

    def to_json(
        self,
        /,
        path_or_buf: Literal[
            "/private/var/folders/xn/05ktz3056kqd9n8frgd6236h00",
            "/var/folders/xn/05ktz3056kqd9n8frgd6236h0000gn/T/t",
        ],
        orient: Literal["values", "columns", "index", "records", "split"],
        lines: bool,
    ):
        """
        usage.dask: 24
        """
        ...

    def to_records(self, /):
        """
        usage.dask: 4
        """
        ...

    def to_string(self, /, max_rows: int, show_dimensions: bool):
        """
        usage.dask: 2
        """
        ...

    def to_timestamp(
        self, /, freq: None = ..., how: Literal["start"] = ..., axis: int = ...
    ):
        """
        usage.dask: 2
        """
        ...

    def to_xarray(self, /):
        """
        usage.xarray: 5
        """
        ...

    def truediv(
        self,
        /,
        other: Union[pandas.core.series.Series, pandas.core.frame.DataFrame, int],
    ):
        """
        usage.dask: 27
        """
        ...

    def var(
        self,
        /,
        axis: Union[Literal["columns", "index"], int] = ...,
        skipna: Union[bool, None] = ...,
        ddof: int = ...,
    ):
        """
        usage.dask: 31
        """
        ...

    def where(
        self, /, cond: Union[pandas.core.series.Series, pandas.core.frame.DataFrame]
    ):
        """
        usage.dask: 8
        """
        ...


class Pandas:
    def __eq__(self, _0: pandas.core.frame.Pandas, /):
        """
        usage.dask: 4
        """
        ...

    def __iter__(self, /):
        """
        usage.dask: 2
        """
        ...
