from typing import *


class DataFrame:
    def __init__(data: Union[Dict[Literal["x"], List[Literal["a"]]], List[List[int]]]):
        "\n    usage.xarray: 1\n    usage.dask: 1\n    "
        ...

    # usage.dask: 3
    __name__: ClassVar[object]

    # usage.dask: 1
    shape: ClassVar[object]

    # usage.dask: 4
    __module__: ClassVar[object]

    @classmethod
    def __ne__(_0: type, /):
        "\n    usage.dask: 3\n    "
        ...

    @classmethod
    def from_dict(
        data: List[Dict[Literal["y", "x"], Union[Literal["a", "b", "c", "d"], int]]]
    ):
        "\n    usage.dask: 1\n    "
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
        "\n    usage.xarray: 3\n    usage.dask: 28\n    "
        ...

    def set_index(self: object, /, keys: object):
        "\n    usage.xarray: 10\n    usage.dask: 115\n    "
        ...

    def __getitem__(self: object, _0: object, /):
        "\n    usage.xarray: 8\n    usage.dask: 520\n    "
        ...

    def stack(self: object, /):
        "\n    usage.xarray: 1\n    usage.dask: 1\n    "
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
        "\n    usage.xarray: 1\n    usage.dask: 128\n    "
        ...

    def equals(self: object, /, other: pandas.core.frame.DataFrame):
        "\n    usage.xarray: 8\n    usage.dask: 2\n    "
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
        "\n    usage.xarray: 2\n    usage.dask: 12\n    "
        ...

    def items(self: object, /):
        "\n    usage.xarray: 1\n    "
        ...

    def iteritems(self: object, /):
        "\n    usage.xarray: 1\n    usage.dask: 2\n    "
        ...

    def to_xarray(self: object, /):
        "\n    usage.xarray: 5\n    "
        ...

    def apply(
        self: object,
        /,
        func: Callable,
        raw: bool = ...,
        result_type: None = ...,
        args: Tuple[None, ...] = ...,
    ):
        "\n    usage.xarray: 1\n    usage.dask: 10\n    "
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
        "\n    usage.xarray: 3\n    usage.dask: 85\n    "
        ...

    def rename(
        self: object,
        /,
        columns: Union[Dict[str, Union[int, str]], collections.OrderedDict, Callable],
    ):
        "\n    usage.dask: 18\n    "
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
        "\n    usage.dask: 32\n    "
        ...

    def itertuples(
        self: object, /, index: bool = ..., name: Union[None, Literal["Pandas"]] = ...
    ):
        "\n    usage.dask: 9\n    "
        ...

    def sort_values(
        self: object,
        /,
        by: Union[
            List[Union[Tuple[Literal["a", "A", "B", "b"], str], float, int, str]],
            Literal["KEY"],
        ],
    ):
        "\n    usage.dask: 179\n    "
        ...

    def sort_index(self: object, /):
        "\n    usage.dask: 8\n    "
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
        "\n    usage.dask: 20\n    "
        ...

    def fillna(
        self: object,
        /,
        value: Union[pandas.core.series.Series, int, None, Literal["-"]] = ...,
        method: Union[None, Literal["ffill", "pad", "bfill"]] = ...,
        axis: int = ...,
        limit: Union[None, int] = ...,
    ):
        "\n    usage.dask: 31\n    "
        ...

    def head(self: object, /):
        "\n    usage.dask: 18\n    "
        ...

    def assign(self: object, /):
        "\n    usage.dask: 16\n    "
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
        "\n    usage.dask: 32\n    "
        ...

    def copy(self: object, /):
        "\n    usage.dask: 16\n    "
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
        "\n    usage.dask: 448\n    "
        ...

    def get(self: object, /, key: str):
        "\n    usage.dask: 10\n    "
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
        "\n    usage.dask: 5\n    "
        ...

    def __eq__(
        self: object,
        _0: Union[dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame, int],
        /,
    ):
        "\n    usage.dask: 17\n    "
        ...

    def all(self: object, /, axis: int = ..., skipna: bool = ...):
        "\n    usage.dask: 11\n    "
        ...

    def to_records(self: object, /):
        "\n    usage.dask: 4\n    "
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
        "\n    usage.dask: 24\n    "
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
        "\n    usage.dask: 26\n    "
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
        "\n    usage.dask: 5\n    "
        ...

    def __mul__(self: object, _0: Union[int, pandas.core.frame.DataFrame], /):
        "\n    usage.dask: 2\n    "
        ...

    def __rmul__(
        self: object,
        _0: Union[dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame, int],
        /,
    ):
        "\n    usage.dask: 3\n    "
        ...

    def __sub__(
        self: object,
        _0: Union[pandas.core.series.Series, pandas.core.frame.DataFrame, int],
        /,
    ):
        "\n    usage.dask: 10\n    "
        ...

    def __rsub__(
        self: object,
        _0: Union[dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame, int],
        /,
    ):
        "\n    usage.dask: 4\n    "
        ...

    def __truediv__(self: object, _0: Union[int, pandas.core.frame.DataFrame], /):
        "\n    usage.dask: 3\n    "
        ...

    def __rtruediv__(
        self: object,
        _0: Union[dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame, int],
        /,
    ):
        "\n    usage.dask: 4\n    "
        ...

    def __floordiv__(self: object, _0: Union[int, pandas.core.frame.DataFrame], /):
        "\n    usage.dask: 2\n    "
        ...

    def __rfloordiv__(
        self: object,
        _0: Union[dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame, int],
        /,
    ):
        "\n    usage.dask: 3\n    "
        ...

    def __pow__(self: object, _0: Union[int, pandas.core.frame.DataFrame], /):
        "\n    usage.dask: 4\n    "
        ...

    def __rpow__(
        self: object,
        _0: Union[dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame, int],
        /,
    ):
        "\n    usage.dask: 3\n    "
        ...

    def __mod__(self: object, _0: Union[int, pandas.core.frame.DataFrame], /):
        "\n    usage.dask: 2\n    "
        ...

    def __rmod__(
        self: object,
        _0: Union[dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame, int],
        /,
    ):
        "\n    usage.dask: 3\n    "
        ...

    def __and__(self: object, _0: Union[bool, pandas.core.frame.DataFrame], /):
        "\n    usage.dask: 2\n    "
        ...

    def __rand__(
        self: object,
        _0: Union[dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame, bool],
        /,
    ):
        "\n    usage.dask: 3\n    "
        ...

    def __or__(self: object, _0: Union[bool, pandas.core.frame.DataFrame], /):
        "\n    usage.dask: 4\n    "
        ...

    def __ror__(
        self: object,
        _0: Union[dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame, bool],
        /,
    ):
        "\n    usage.dask: 5\n    "
        ...

    def __xor__(self: object, _0: Union[bool, pandas.core.frame.DataFrame], /):
        "\n    usage.dask: 2\n    "
        ...

    def __rxor__(
        self: object,
        _0: Union[dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame, bool],
        /,
    ):
        "\n    usage.dask: 3\n    "
        ...

    def __gt__(
        self: object,
        _0: Union[pandas.core.series.Series, pandas.core.frame.DataFrame, int],
        /,
    ):
        "\n    usage.dask: 3\n    "
        ...

    def __lt__(
        self: object,
        _0: Union[dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame, int],
        /,
    ):
        "\n    usage.dask: 3\n    "
        ...

    def __le__(self: object, _0: object, /):
        "\n    usage.dask: 12\n    "
        ...

    def __ge__(
        self: object,
        _0: Union[dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame, int],
        /,
    ):
        "\n    usage.dask: 7\n    "
        ...

    def __ne__(
        self: object,
        _0: Union[dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame, int],
        /,
    ):
        "\n    usage.dask: 5\n    "
        ...

    def lt(self: object, /, other: Union[int, pandas.core.frame.DataFrame]):
        "\n    usage.dask: 2\n    "
        ...

    def gt(self: object, /, other: Union[int, pandas.core.frame.DataFrame]):
        "\n    usage.dask: 2\n    "
        ...

    def le(self: object, /, other: Union[int, pandas.core.frame.DataFrame]):
        "\n    usage.dask: 2\n    "
        ...

    def ge(self: object, /, other: Union[int, pandas.core.frame.DataFrame]):
        "\n    usage.dask: 2\n    "
        ...

    def ne(self: object, /, other: Union[int, pandas.core.frame.DataFrame]):
        "\n    usage.dask: 2\n    "
        ...

    def eq(self: object, /, other: Union[int, pandas.core.frame.DataFrame]):
        "\n    usage.dask: 2\n    "
        ...

    def __neg__(self: object, /):
        "\n    usage.dask: 5\n    "
        ...

    def __invert__(self: object, /):
        "\n    usage.dask: 1\n    "
        ...

    def any(self: object, /, axis: int = ..., skipna: bool = ...):
        "\n    usage.dask: 9\n    "
        ...

    def add(
        self: object,
        /,
        other: Union[pandas.core.frame.DataFrame, int, pandas.core.series.Series],
    ):
        "\n    usage.dask: 11\n    "
        ...

    def sub(
        self: object,
        /,
        other: Union[pandas.core.series.Series, pandas.core.frame.DataFrame, int],
    ):
        "\n    usage.dask: 9\n    "
        ...

    def mul(
        self: object,
        /,
        other: Union[pandas.core.frame.DataFrame, int, pandas.core.series.Series],
    ):
        "\n    usage.dask: 11\n    "
        ...

    def truediv(
        self: object,
        /,
        other: Union[pandas.core.series.Series, pandas.core.frame.DataFrame, int],
    ):
        "\n    usage.dask: 27\n    "
        ...

    def floordiv(
        self: object,
        /,
        other: Union[pandas.core.series.Series, pandas.core.frame.DataFrame, int],
    ):
        "\n    usage.dask: 9\n    "
        ...

    def pow(
        self: object,
        /,
        other: Union[pandas.core.series.Series, pandas.core.frame.DataFrame, int],
    ):
        "\n    usage.dask: 9\n    "
        ...

    def mod(
        self: object,
        /,
        other: Union[pandas.core.series.Series, pandas.core.frame.DataFrame, int],
    ):
        "\n    usage.dask: 9\n    "
        ...

    def radd(
        self: object,
        /,
        other: Union[pandas.core.series.Series, pandas.core.frame.DataFrame, int],
    ):
        "\n    usage.dask: 9\n    "
        ...

    def rsub(
        self: object,
        /,
        other: Union[pandas.core.series.Series, pandas.core.frame.DataFrame, int],
    ):
        "\n    usage.dask: 9\n    "
        ...

    def rmul(
        self: object,
        /,
        other: Union[pandas.core.series.Series, pandas.core.frame.DataFrame, int],
    ):
        "\n    usage.dask: 9\n    "
        ...

    def rtruediv(
        self: object,
        /,
        other: Union[pandas.core.series.Series, pandas.core.frame.DataFrame, int],
    ):
        "\n    usage.dask: 18\n    "
        ...

    def rpow(
        self: object,
        /,
        other: Union[pandas.core.series.Series, pandas.core.frame.DataFrame, int],
    ):
        "\n    usage.dask: 9\n    "
        ...

    def rmod(
        self: object,
        /,
        other: Union[pandas.core.series.Series, pandas.core.frame.DataFrame, int],
    ):
        "\n    usage.dask: 9\n    "
        ...

    def sum(
        self: object,
        /,
        axis: Union[int, Literal["columns", "index"]] = ...,
        min_count: int = ...,
    ):
        "\n    usage.dask: 33\n    "
        ...

    def prod(
        self: object,
        /,
        axis: Union[int, Literal["columns", "index"]] = ...,
        min_count: int = ...,
    ):
        "\n    usage.dask: 15\n    "
        ...

    def min(self: object, /):
        "\n    usage.dask: 15\n    "
        ...

    def max(self: object, /):
        "\n    usage.dask: 15\n    "
        ...

    def mean(self: object, /):
        "\n    usage.dask: 20\n    "
        ...

    def _get_numeric_data(self: object, /):
        "\n    usage.dask: 4\n    "
        ...

    def count(self: object, /):
        "\n    usage.dask: 17\n    "
        ...

    def var(
        self: object,
        /,
        axis: Union[Literal["columns", "index"], int] = ...,
        skipna: Union[bool, None] = ...,
        ddof: int = ...,
    ):
        "\n    usage.dask: 31\n    "
        ...

    def std(
        self: object,
        /,
        axis: Union[Literal["columns", "index"], int] = ...,
        skipna: bool = ...,
        ddof: int = ...,
    ):
        "\n    usage.dask: 23\n    "
        ...

    def sem(
        self: object,
        /,
        axis: Union[int, Literal["columns", "index"]] = ...,
        skipna: Union[bool, None] = ...,
        ddof: int = ...,
    ):
        "\n    usage.dask: 23\n    "
        ...

    def drop_duplicates(
        self: object,
        /,
        subset: Union[Literal["ticker", "y"], None, List[Literal["x", "y", "z"]]] = ...,
        keep: Union[Literal["last", "first"], bool] = ...,
    ):
        "\n    usage.dask: 43\n    "
        ...

    def take(self: object, /, indices: numpy.ndarray):
        "\n    usage.dask: 1\n    "
        ...

    def to_string(self: object, /, max_rows: int, show_dimensions: bool):
        "\n    usage.dask: 2\n    "
        ...

    def tail(self: object, /, n: int):
        "\n    usage.dask: 5\n    "
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
        "\n    usage.dask: 21\n    "
        ...

    def quantile(
        self: object,
        /,
        q: Union[List[Union[float, numpy.float64]], float] = ...,
        axis: int = ...,
    ):
        "\n    usage.dask: 7\n    "
        ...

    def __iter__(self: object, /):
        "\n    usage.dask: 1\n    "
        ...

    def cumsum(self: object, /, axis: Union[int, None] = ..., skipna: bool = ...):
        "\n    usage.dask: 11\n    "
        ...

    def cumprod(self: object, /, axis: Union[int, None] = ..., skipna: bool = ...):
        "\n    usage.dask: 11\n    "
        ...

    def cummin(self: object, /, axis: Union[int, None] = ..., skipna: bool = ...):
        "\n    usage.dask: 11\n    "
        ...

    def isnull(self: object, /):
        "\n    usage.dask: 6\n    "
        ...

    def where(
        self: object,
        /,
        cond: Union[pandas.core.series.Series, pandas.core.frame.DataFrame],
    ):
        "\n    usage.dask: 8\n    "
        ...

    def cummax(self: object, /, axis: Union[int, None] = ..., skipna: bool = ...):
        "\n    usage.dask: 11\n    "
        ...

    def dropna(
        self: object,
        /,
        how: Literal["any", "all"] = ...,
        thresh: Union[int, None] = ...,
        subset: Union[None, List[Literal["x", "z", "y"]]] = ...,
    ):
        "\n    usage.dask: 21\n    "
        ...

    def clip(
        self: object,
        /,
        lower: Union[None, int, float] = ...,
        upper: Union[float, int, None] = ...,
    ):
        "\n    usage.dask: 12\n    "
        ...

    def squeeze(self: object, /):
        "\n    usage.dask: 3\n    "
        ...

    def mask(
        self: object,
        /,
        cond: Union[pandas.core.series.Series, pandas.core.frame.DataFrame],
    ):
        "\n    usage.dask: 6\n    "
        ...

    def rename_axis(
        self: object, /, mapper: Union[Literal["myindex", "newindex"], List[None]]
    ):
        "\n    usage.dask: 5\n    "
        ...

    def isin(
        self: object, /, values: Union[Dict[Literal["b", "a"], List[int]], List[int]]
    ):
        "\n    usage.dask: 6\n    "
        ...

    def notnull(self: object, /):
        "\n    usage.dask: 2\n    "
        ...

    def align(
        self: object,
        /,
        other: pandas.core.frame.DataFrame,
        join: Literal["right", "left", "outer", "inner"],
        axis: Union[Literal["XXX", "columns", "index"], None, int] = ...,
        fill_value: Union[None, int] = ...,
    ):
        "\n    usage.dask: 48\n    "
        ...

    def combine(self: object, /, other: pandas.core.frame.DataFrame, func: Callable):
        "\n    usage.dask: 7\n    "
        ...

    def combine_first(self: object, /, other: pandas.core.frame.DataFrame):
        "\n    usage.dask: 3\n    "
        ...

    def sample(
        self: object, /, frac: float, random_state: numpy.random.mtrand.RandomState
    ):
        "\n    usage.dask: 2\n    "
        ...

    def memory_usage(self: object, /, index: bool):
        "\n    usage.dask: 5\n    "
        ...

    def ffill(self: object, /):
        "\n    usage.dask: 2\n    "
        ...

    def bfill(self: object, /):
        "\n    usage.dask: 2\n    "
        ...

    def to_timestamp(
        self: object, /, freq: None = ..., how: Literal["start"] = ..., axis: int = ...
    ):
        "\n    usage.dask: 2\n    "
        ...

    def applymap(self: object, /, func: Callable):
        "\n    usage.dask: 3\n    "
        ...

    def abs(self: object, /):
        "\n    usage.dask: 3\n    "
        ...

    def round(self: object, /):
        "\n    usage.dask: 3\n    "
        ...

    def cov(self: object, /):
        "\n    usage.dask: 6\n    "
        ...

    def corr(self: object, /):
        "\n    usage.dask: 5\n    "
        ...

    def nlargest(
        self: object, /, n: int, columns: Union[List[Literal["c", "a"]], Literal["a"]]
    ):
        "\n    usage.dask: 4\n    "
        ...

    def nsmallest(
        self: object, /, n: int, columns: Union[List[Literal["c", "a"]], Literal["a"]]
    ):
        "\n    usage.dask: 4\n    "
        ...

    def iterrows(self: object, /):
        "\n    usage.dask: 2\n    "
        ...

    def info(self: object, /, buf: _io.StringIO, memory_usage: bool):
        "\n    usage.dask: 1\n    "
        ...

    def idxmax(self: object, /):
        "\n    usage.dask: 7\n    "
        ...

    def idxmin(self: object, /):
        "\n    usage.dask: 5\n    "
        ...

    def diff(self: object, /, periods: int = ..., axis: int = ...):
        "\n    usage.dask: 7\n    "
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
        "\n    usage.dask: 29\n    "
        ...

    def first(self: object, /, offset: str):
        "\n    usage.dask: 24\n    "
        ...

    def last(self: object, /, offset: str):
        "\n    usage.dask: 8\n    "
        ...

    def query(self: object, /, expr: Literal["B != 9", "B != 0"]):
        "\n    usage.dask: 4\n    "
        ...

    def replace(
        self: object,
        /,
        to_replace: Union[Dict[int, int], int],
        value: Union[None, int] = ...,
        regex: bool = ...,
    ):
        "\n    usage.dask: 4\n    "
        ...

    def explode(self: object, /, column: Literal["A"]):
        "\n    usage.dask: 2\n    "
        ...

    def to_html(self: object, /, max_rows: int, show_dimensions: bool):
        "\n    usage.dask: 2\n    "
        ...

    def __itruediv__(self: object, _0: pandas.core.frame.DataFrame, /):
        "\n    usage.dask: 1\n    "
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
        "\n    usage.dask: 365\n    "
        ...

    def join(
        self: object,
        /,
        other: pandas.core.frame.DataFrame,
        how: Literal["right", "left", "outer", "inner"] = ...,
        lsuffix: Literal["l", "_l"] = ...,
        rsuffix: Literal["r", "_r"] = ...,
    ):
        "\n    usage.dask: 31\n    "
        ...

    def __contains__(
        self: object,
        _0: Union[pandas._libs.tslibs.timestamps.Timestamp, int, numpy.int64],
        /,
    ):
        "\n    usage.dask: 6\n    "
        ...

    def isna(self: object, /):
        "\n    usage.dask: 1\n    "
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
        "\n    usage.dask: 10\n    "
        ...

    def append(
        self: object,
        /,
        other: Union[pandas.core.frame.DataFrame, pandas.core.series.Series],
    ):
        "\n    usage.dask: 12\n    "
        ...

    def pivot_table(
        self: object,
        /,
        values: Literal["B"],
        index: Literal["A"],
        columns: Literal["C"],
        aggfunc: Literal["count", "sum", "mean"],
    ):
        "\n    usage.dask: 3\n    "
        ...

    def __array_wrap__(self: object, /, result: numpy.ndarray):
        "\n    usage.dask: 2\n    "
        ...

    def resample(
        self: object,
        /,
        rule: object,
        closed: Union[None, Literal["left", "right"]] = ...,
        label: Union[None, Literal["left", "right"]] = ...,
    ):
        "\n    usage.dask: 63\n    "
        ...


class Pandas:
    def __iter__(self: object, /):
        "\n    usage.dask: 2\n    "
        ...

    def __eq__(self: object, _0: pandas.core.frame.Pandas, /):
        "\n    usage.dask: 4\n    "
        ...
