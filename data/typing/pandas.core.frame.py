from typing import *


class DataFrame:
    def __init__(data: Union[Dict[Literal["x"], List[Literal["a"]]], List[List[int]]]):
        """
        usage.xarray: 1
        usage.dask: 1
        """
        ...

    # usage.dask: 3
    __name__: ClassVar[object]

    # usage.dask: 1
    shape: ClassVar[object]

    # usage.dask: 4
    __module__: ClassVar[object]

    @classmethod
    def __ne__(_0: type, /):
        """
        usage.dask: 3
        """
        ...

    @classmethod
    def from_dict(
        data: List[Dict[Literal["y", "x"], Union[Literal["a", "b", "c", "d"], int]]]
    ):
        """
        usage.dask: 1
        """
        ...

    # usage.xarray: 10
    # usage.dask: 189
    index: object

    # usage.xarray: 9
    # usage.dask: 141
    columns: object

    # usage.xarray: 2
    # usage.dask: 31
    values: object

    # usage.xarray: 1
    # usage.dask: 68
    loc: object

    # usage.dask: 1
    _data: object

    # usage.dask: 41
    iloc: object

    # usage.dask: 26
    dtypes: object

    # usage.dask: 81
    x: pandas.core.series.Series

    # usage.dask: 7
    empty: object

    # usage.dask: 2
    id: object

    # usage.dask: 1
    amount: object

    # usage.dask: 2
    path: object

    # usage.dask: 1
    _constructor_sliced: object

    # usage.dask: 2
    fruit: object

    # usage.dask: 2
    Date: pandas.core.series.Series

    # usage.dask: 116
    a: pandas.core.series.Series

    # usage.dask: 2
    dt_col: object

    # usage.dask: 12
    str_col: object

    # usage.dask: 4
    string_col: object

    # usage.dask: 66
    b: object

    # usage.dask: 5
    T: object

    # usage.dask: 40
    A: object

    # usage.dask: 3
    div: object

    # usage.dask: 3
    divide: object

    # usage.dask: 3
    rdiv: object

    # usage.dask: 2
    X: object

    # usage.dask: 1
    c: object

    # usage.dask: 7
    __class__: object

    # usage.dask: 37
    y: pandas.core.series.Series

    # usage.dask: 4
    z: object

    # usage.dask: 7
    w: pandas.core.series.Series

    # usage.dask: 1
    tz: object

    # usage.dask: 3
    ndim: object

    # usage.dask: 15
    B: object

    # usage.dask: 2
    size: object

    # usage.dask: 4
    d: object

    # usage.dask: 1
    col2: object

    # usage.dask: 1
    col1: object

    # usage.dask: 4
    C: object

    # usage.dask: 1
    F: object

    # usage.dask: 3
    A_a: object

    # usage.dask: 2
    i32: object

    # usage.dask: 2
    _partitions: object

    # usage.dask: 2
    e: object

    # usage.dask: 3
    f: object

    def reset_index(self: object, /, level: int = ..., drop: bool = ...):
        """
        usage.xarray: 3
        usage.dask: 28
        """
        ...

    def set_index(self: object, /, keys: object):
        """
        usage.xarray: 10
        usage.dask: 115
        """
        ...

    def __getitem__(self: object, _0: object, /):
        """
        usage.xarray: 8
        usage.dask: 520
        """
        ...

    def stack(self: object, /):
        """
        usage.xarray: 1
        usage.dask: 1
        """
        ...

    def __setitem__(
        self: object,
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

    def equals(self: object, /, other: pandas.core.frame.DataFrame):
        """
        usage.xarray: 8
        usage.dask: 2
        """
        ...

    def reindex(
        self: object,
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

    def items(self: object, /):
        """
        usage.xarray: 1
        """
        ...

    def iteritems(self: object, /):
        """
        usage.xarray: 1
        usage.dask: 2
        """
        ...

    def to_xarray(self: object, /):
        """
        usage.xarray: 5
        """
        ...

    def apply(
        self: object,
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

    def rolling(
        self: object,
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

    def rename(
        self: object,
        /,
        columns: Union[Dict[str, Union[int, str]], collections.OrderedDict, Callable],
    ):
        """
        usage.dask: 18
        """
        ...

    def astype(
        self: object,
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

    def itertuples(
        self: object, /, index: bool = ..., name: Union[None, Literal["Pandas"]] = ...
    ):
        """
        usage.dask: 9
        """
        ...

    def sort_values(
        self: object,
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

    def sort_index(self: object, /):
        """
        usage.dask: 8
        """
        ...

    def select_dtypes(
        self: object,
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

    def fillna(
        self: object,
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

    def head(self: object, /):
        """
        usage.dask: 18
        """
        ...

    def assign(self: object, /):
        """
        usage.dask: 16
        """
        ...

    def drop(
        self: object,
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

    def copy(self: object, /):
        """
        usage.dask: 16
        """
        ...

    def groupby(
        self: object,
        /,
        by: object = ...,
        group_keys: bool = ...,
        level: Union[List[int], int] = ...,
        sort: bool = ...,
        *,
        dropna: bool = ...,
    ):
        """
        usage.dask: 448
        """
        ...

    def get(self: object, /, key: str):
        """
        usage.dask: 10
        """
        ...

    def to_csv(
        self: object,
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

    def __eq__(
        self: object,
        _0: Union[dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame, int],
        /,
    ):
        """
        usage.dask: 17
        """
        ...

    def all(self: object, /, axis: int = ..., skipna: bool = ...):
        """
        usage.dask: 11
        """
        ...

    def to_records(self: object, /):
        """
        usage.dask: 4
        """
        ...

    def to_json(
        self: object,
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

    def __add__(
        self: object,
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

    def __radd__(
        self: object,
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

    def __mul__(self: object, _0: Union[int, pandas.core.frame.DataFrame], /):
        """
        usage.dask: 2
        """
        ...

    def __rmul__(
        self: object,
        _0: Union[dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame, int],
        /,
    ):
        """
        usage.dask: 3
        """
        ...

    def __sub__(
        self: object,
        _0: Union[pandas.core.series.Series, pandas.core.frame.DataFrame, int],
        /,
    ):
        """
        usage.dask: 10
        """
        ...

    def __rsub__(
        self: object,
        _0: Union[dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame, int],
        /,
    ):
        """
        usage.dask: 4
        """
        ...

    def __truediv__(self: object, _0: Union[int, pandas.core.frame.DataFrame], /):
        """
        usage.dask: 3
        """
        ...

    def __rtruediv__(
        self: object,
        _0: Union[dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame, int],
        /,
    ):
        """
        usage.dask: 4
        """
        ...

    def __floordiv__(self: object, _0: Union[int, pandas.core.frame.DataFrame], /):
        """
        usage.dask: 2
        """
        ...

    def __rfloordiv__(
        self: object,
        _0: Union[dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame, int],
        /,
    ):
        """
        usage.dask: 3
        """
        ...

    def __pow__(self: object, _0: Union[int, pandas.core.frame.DataFrame], /):
        """
        usage.dask: 4
        """
        ...

    def __rpow__(
        self: object,
        _0: Union[dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame, int],
        /,
    ):
        """
        usage.dask: 3
        """
        ...

    def __mod__(self: object, _0: Union[int, pandas.core.frame.DataFrame], /):
        """
        usage.dask: 2
        """
        ...

    def __rmod__(
        self: object,
        _0: Union[dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame, int],
        /,
    ):
        """
        usage.dask: 3
        """
        ...

    def __and__(self: object, _0: Union[bool, pandas.core.frame.DataFrame], /):
        """
        usage.dask: 2
        """
        ...

    def __rand__(
        self: object,
        _0: Union[dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame, bool],
        /,
    ):
        """
        usage.dask: 3
        """
        ...

    def __or__(self: object, _0: Union[bool, pandas.core.frame.DataFrame], /):
        """
        usage.dask: 4
        """
        ...

    def __ror__(
        self: object,
        _0: Union[dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame, bool],
        /,
    ):
        """
        usage.dask: 5
        """
        ...

    def __xor__(self: object, _0: Union[bool, pandas.core.frame.DataFrame], /):
        """
        usage.dask: 2
        """
        ...

    def __rxor__(
        self: object,
        _0: Union[dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame, bool],
        /,
    ):
        """
        usage.dask: 3
        """
        ...

    def __gt__(
        self: object,
        _0: Union[pandas.core.series.Series, pandas.core.frame.DataFrame, int],
        /,
    ):
        """
        usage.dask: 3
        """
        ...

    def __lt__(
        self: object,
        _0: Union[dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame, int],
        /,
    ):
        """
        usage.dask: 3
        """
        ...

    def __le__(self: object, _0: object, /):
        """
        usage.dask: 12
        """
        ...

    def __ge__(
        self: object,
        _0: Union[dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame, int],
        /,
    ):
        """
        usage.dask: 7
        """
        ...

    def __ne__(
        self: object,
        _0: Union[dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame, int],
        /,
    ):
        """
        usage.dask: 5
        """
        ...

    def lt(self: object, /, other: Union[int, pandas.core.frame.DataFrame]):
        """
        usage.dask: 2
        """
        ...

    def gt(self: object, /, other: Union[int, pandas.core.frame.DataFrame]):
        """
        usage.dask: 2
        """
        ...

    def le(self: object, /, other: Union[int, pandas.core.frame.DataFrame]):
        """
        usage.dask: 2
        """
        ...

    def ge(self: object, /, other: Union[int, pandas.core.frame.DataFrame]):
        """
        usage.dask: 2
        """
        ...

    def ne(self: object, /, other: Union[int, pandas.core.frame.DataFrame]):
        """
        usage.dask: 2
        """
        ...

    def eq(self: object, /, other: Union[int, pandas.core.frame.DataFrame]):
        """
        usage.dask: 2
        """
        ...

    def __neg__(self: object, /):
        """
        usage.dask: 5
        """
        ...

    def __invert__(self: object, /):
        """
        usage.dask: 1
        """
        ...

    def any(self: object, /, axis: int = ..., skipna: bool = ...):
        """
        usage.dask: 9
        """
        ...

    def add(
        self: object,
        /,
        other: Union[pandas.core.frame.DataFrame, int, pandas.core.series.Series],
    ):
        """
        usage.dask: 11
        """
        ...

    def sub(
        self: object,
        /,
        other: Union[pandas.core.series.Series, pandas.core.frame.DataFrame, int],
    ):
        """
        usage.dask: 9
        """
        ...

    def mul(
        self: object,
        /,
        other: Union[pandas.core.frame.DataFrame, int, pandas.core.series.Series],
    ):
        """
        usage.dask: 11
        """
        ...

    def truediv(
        self: object,
        /,
        other: Union[pandas.core.series.Series, pandas.core.frame.DataFrame, int],
    ):
        """
        usage.dask: 27
        """
        ...

    def floordiv(
        self: object,
        /,
        other: Union[pandas.core.series.Series, pandas.core.frame.DataFrame, int],
    ):
        """
        usage.dask: 9
        """
        ...

    def pow(
        self: object,
        /,
        other: Union[pandas.core.series.Series, pandas.core.frame.DataFrame, int],
    ):
        """
        usage.dask: 9
        """
        ...

    def mod(
        self: object,
        /,
        other: Union[pandas.core.series.Series, pandas.core.frame.DataFrame, int],
    ):
        """
        usage.dask: 9
        """
        ...

    def radd(
        self: object,
        /,
        other: Union[pandas.core.series.Series, pandas.core.frame.DataFrame, int],
    ):
        """
        usage.dask: 9
        """
        ...

    def rsub(
        self: object,
        /,
        other: Union[pandas.core.series.Series, pandas.core.frame.DataFrame, int],
    ):
        """
        usage.dask: 9
        """
        ...

    def rmul(
        self: object,
        /,
        other: Union[pandas.core.series.Series, pandas.core.frame.DataFrame, int],
    ):
        """
        usage.dask: 9
        """
        ...

    def rtruediv(
        self: object,
        /,
        other: Union[pandas.core.series.Series, pandas.core.frame.DataFrame, int],
    ):
        """
        usage.dask: 18
        """
        ...

    def rpow(
        self: object,
        /,
        other: Union[pandas.core.series.Series, pandas.core.frame.DataFrame, int],
    ):
        """
        usage.dask: 9
        """
        ...

    def rmod(
        self: object,
        /,
        other: Union[pandas.core.series.Series, pandas.core.frame.DataFrame, int],
    ):
        """
        usage.dask: 9
        """
        ...

    def sum(
        self: object,
        /,
        axis: Union[int, Literal["columns", "index"]] = ...,
        min_count: int = ...,
    ):
        """
        usage.dask: 33
        """
        ...

    def prod(
        self: object,
        /,
        axis: Union[int, Literal["columns", "index"]] = ...,
        min_count: int = ...,
    ):
        """
        usage.dask: 15
        """
        ...

    def min(self: object, /):
        """
        usage.dask: 15
        """
        ...

    def max(self: object, /):
        """
        usage.dask: 15
        """
        ...

    def mean(self: object, /):
        """
        usage.dask: 20
        """
        ...

    def _get_numeric_data(self: object, /):
        """
        usage.dask: 4
        """
        ...

    def count(self: object, /):
        """
        usage.dask: 17
        """
        ...

    def var(
        self: object,
        /,
        axis: Union[Literal["columns", "index"], int] = ...,
        skipna: Union[bool, None] = ...,
        ddof: int = ...,
    ):
        """
        usage.dask: 31
        """
        ...

    def std(
        self: object,
        /,
        axis: Union[Literal["columns", "index"], int] = ...,
        skipna: bool = ...,
        ddof: int = ...,
    ):
        """
        usage.dask: 23
        """
        ...

    def sem(
        self: object,
        /,
        axis: Union[int, Literal["columns", "index"]] = ...,
        skipna: Union[bool, None] = ...,
        ddof: int = ...,
    ):
        """
        usage.dask: 23
        """
        ...

    def drop_duplicates(
        self: object,
        /,
        subset: Union[Literal["ticker", "y"], None, List[Literal["x", "y", "z"]]] = ...,
        keep: Union[Literal["last", "first"], bool] = ...,
    ):
        """
        usage.dask: 43
        """
        ...

    def take(self: object, /, indices: numpy.ndarray):
        """
        usage.dask: 1
        """
        ...

    def to_string(self: object, /, max_rows: int, show_dimensions: bool):
        """
        usage.dask: 2
        """
        ...

    def tail(self: object, /, n: int):
        """
        usage.dask: 5
        """
        ...

    def describe(
        self: object,
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

    def quantile(
        self: object,
        /,
        q: Union[List[Union[float, numpy.float64]], float] = ...,
        axis: int = ...,
    ):
        """
        usage.dask: 7
        """
        ...

    def __iter__(self: object, /):
        """
        usage.dask: 1
        """
        ...

    def cumsum(self: object, /, axis: Union[int, None] = ..., skipna: bool = ...):
        """
        usage.dask: 11
        """
        ...

    def cumprod(self: object, /, axis: Union[int, None] = ..., skipna: bool = ...):
        """
        usage.dask: 11
        """
        ...

    def cummin(self: object, /, axis: Union[int, None] = ..., skipna: bool = ...):
        """
        usage.dask: 11
        """
        ...

    def isnull(self: object, /):
        """
        usage.dask: 6
        """
        ...

    def where(
        self: object,
        /,
        cond: Union[pandas.core.series.Series, pandas.core.frame.DataFrame],
    ):
        """
        usage.dask: 8
        """
        ...

    def cummax(self: object, /, axis: Union[int, None] = ..., skipna: bool = ...):
        """
        usage.dask: 11
        """
        ...

    def dropna(
        self: object,
        /,
        how: Literal["any", "all"] = ...,
        thresh: Union[int, None] = ...,
        subset: Union[None, List[Literal["x", "z", "y"]]] = ...,
    ):
        """
        usage.dask: 21
        """
        ...

    def clip(
        self: object,
        /,
        lower: Union[None, int, float] = ...,
        upper: Union[float, int, None] = ...,
    ):
        """
        usage.dask: 12
        """
        ...

    def squeeze(self: object, /):
        """
        usage.dask: 3
        """
        ...

    def mask(
        self: object,
        /,
        cond: Union[pandas.core.series.Series, pandas.core.frame.DataFrame],
    ):
        """
        usage.dask: 6
        """
        ...

    def rename_axis(
        self: object, /, mapper: Union[Literal["myindex", "newindex"], List[None]]
    ):
        """
        usage.dask: 5
        """
        ...

    def isin(
        self: object, /, values: Union[Dict[Literal["b", "a"], List[int]], List[int]]
    ):
        """
        usage.dask: 6
        """
        ...

    def notnull(self: object, /):
        """
        usage.dask: 2
        """
        ...

    def align(
        self: object,
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

    def combine(self: object, /, other: pandas.core.frame.DataFrame, func: Callable):
        """
        usage.dask: 7
        """
        ...

    def combine_first(self: object, /, other: pandas.core.frame.DataFrame):
        """
        usage.dask: 3
        """
        ...

    def sample(
        self: object, /, frac: float, random_state: numpy.random.mtrand.RandomState
    ):
        """
        usage.dask: 2
        """
        ...

    def memory_usage(self: object, /, index: bool):
        """
        usage.dask: 5
        """
        ...

    def ffill(self: object, /):
        """
        usage.dask: 2
        """
        ...

    def bfill(self: object, /):
        """
        usage.dask: 2
        """
        ...

    def to_timestamp(
        self: object, /, freq: None = ..., how: Literal["start"] = ..., axis: int = ...
    ):
        """
        usage.dask: 2
        """
        ...

    def applymap(self: object, /, func: Callable):
        """
        usage.dask: 3
        """
        ...

    def abs(self: object, /):
        """
        usage.dask: 3
        """
        ...

    def round(self: object, /):
        """
        usage.dask: 3
        """
        ...

    def cov(self: object, /):
        """
        usage.dask: 6
        """
        ...

    def corr(self: object, /):
        """
        usage.dask: 5
        """
        ...

    def nlargest(
        self: object, /, n: int, columns: Union[List[Literal["c", "a"]], Literal["a"]]
    ):
        """
        usage.dask: 4
        """
        ...

    def nsmallest(
        self: object, /, n: int, columns: Union[List[Literal["c", "a"]], Literal["a"]]
    ):
        """
        usage.dask: 4
        """
        ...

    def iterrows(self: object, /):
        """
        usage.dask: 2
        """
        ...

    def info(self: object, /, buf: _io.StringIO, memory_usage: bool):
        """
        usage.dask: 1
        """
        ...

    def idxmax(self: object, /):
        """
        usage.dask: 7
        """
        ...

    def idxmin(self: object, /):
        """
        usage.dask: 5
        """
        ...

    def diff(self: object, /, periods: int = ..., axis: int = ...):
        """
        usage.dask: 7
        """
        ...

    def shift(
        self: object,
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

    def query(self: object, /, expr: Literal["B != 9", "B != 0"]):
        """
        usage.dask: 4
        """
        ...

    def replace(
        self: object,
        /,
        to_replace: Union[Dict[int, int], int],
        value: Union[None, int] = ...,
        regex: bool = ...,
    ):
        """
        usage.dask: 4
        """
        ...

    def explode(self: object, /, column: Literal["A"]):
        """
        usage.dask: 2
        """
        ...

    def to_html(self: object, /, max_rows: int, show_dimensions: bool):
        """
        usage.dask: 2
        """
        ...

    def __itruediv__(self: object, _0: pandas.core.frame.DataFrame, /):
        """
        usage.dask: 1
        """
        ...

    def merge(
        self: object,
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

    def join(
        self: object,
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

    def __contains__(
        self: object,
        _0: Union[pandas._libs.tslibs.timestamps.Timestamp, int, numpy.int64],
        /,
    ):
        """
        usage.dask: 6
        """
        ...

    def isna(self: object, /):
        """
        usage.dask: 1
        """
        ...

    def melt(
        self: object,
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

    def append(
        self: object,
        /,
        other: Union[pandas.core.frame.DataFrame, pandas.core.series.Series],
    ):
        """
        usage.dask: 12
        """
        ...

    def pivot_table(
        self: object,
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

    def __array_wrap__(self: object, /, result: numpy.ndarray):
        """
        usage.dask: 2
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
        usage.dask: 63
        """
        ...


class Pandas:
    def __iter__(self: object, /):
        """
        usage.dask: 2
        """
        ...

    def __eq__(self: object, _0: pandas.core.frame.Pandas, /):
        """
        usage.dask: 4
        """
        ...
