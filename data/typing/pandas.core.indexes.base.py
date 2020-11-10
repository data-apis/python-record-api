from typing import *


@overload
def ensure_index(index_like: pandas.core.indexes.range.RangeIndex):
    """
    usage.modin: 2
    """
    ...


@overload
def ensure_index(index_like: pandas.core.indexes.base.Index):
    """
    usage.modin: 2
    """
    ...


@overload
def ensure_index(index_like: List[Literal["col2", "col1"]]):
    """
    usage.modin: 1
    """
    ...


@overload
def ensure_index(index_like: List[Literal["col1"]]):
    """
    usage.modin: 1
    """
    ...


@overload
def ensure_index(index_like: pandas.core.indexes.numeric.Int64Index):
    """
    usage.modin: 3
    """
    ...


@overload
def ensure_index(index_like: List[Literal["C", "B", "A"]]):
    """
    usage.modin: 1
    """
    ...


@overload
def ensure_index(index_like: pandas.core.indexes.multi.MultiIndex):
    """
    usage.modin: 2
    """
    ...


@overload
def ensure_index(index_like: pandas.core.indexes.numeric.Float64Index):
    """
    usage.modin: 1
    """
    ...


@overload
def ensure_index(index_like: pandas.core.indexes.datetimes.DatetimeIndex):
    """
    usage.modin: 1
    """
    ...


def ensure_index(index_like: object):
    """
    usage.modin: 14
    """
    ...


class Index:

    # usage.dask: 2
    __name__: ClassVar[object]

    # usage.modin: 2
    __new__: ClassVar[object]

    # usage.xarray: 2
    get_loc: ClassVar[object]

    # usage.dask: 1
    array: object

    # usage.seaborn: 1
    categories: object

    # usage.dask: 13
    # usage.koalas: 1
    # usage.sklearn: 2
    # usage.xarray: 6
    dtype: object

    # usage.koalas: 2
    hasnans: object

    # usage.dask: 1
    # usage.xarray: 2
    is_monotonic: object

    # usage.dask: 1
    # usage.xarray: 6
    is_unique: object

    # usage.dask: 16
    # usage.koalas: 4
    # usage.modin: 3
    # usage.seaborn: 2
    # usage.xarray: 13
    name: Union[None, Literal["A", "a", "id", "lvl_1", "columns"], int]

    # usage.dask: 3
    # usage.koalas: 56
    names: Union[
        List[
            Union[
                str,
                None,
                Tuple[Literal["b", "x", "a"], Literal["2", "group", "lkey", "aa"]],
            ]
        ],
        pandas.core.indexes.frozen.FrozenList,
    ]

    # usage.xarray: 1
    nlevels: object

    # usage.xarray: 1
    shape: object

    # usage.xarray: 10
    size: object

    # usage.dask: 2
    # usage.prophet: 1
    # usage.sklearn: 1
    str: object

    # usage.dask: 1
    # usage.modin: 1
    # usage.seaborn: 1
    # usage.xarray: 6
    values: object

    def __add__(self, _0: Literal["x"], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["a"], /):
        """
        usage.dask: 8
        usage.koalas: 2
        """
        ...

    @overload
    def __contains__(self, _0: Literal["bar"], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["C"], /):
        """
        usage.dask: 2
        usage.koalas: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["A"], /):
        """
        usage.dask: 7
        usage.koalas: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["id"], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["level_1"], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["i32"], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["i64"], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["coverage"], /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["divisions"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["dtype"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["x"], /):
        """
        usage.dask: 6
        """
        ...

    @overload
    def __contains__(self, _0: str, /):
        """
        usage.dask: 3
        """
        ...

    @overload
    def __contains__(self, _0: Literal["amount"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __contains__(self, _0: Literal["path"], /):
        """
        usage.dask: 3
        """
        ...

    @overload
    def __contains__(self, _0: Literal["filename"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __contains__(self, _0: Literal["name"], /):
        """
        usage.dask: 3
        """
        ...

    @overload
    def __contains__(self, _0: Literal["fruit"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __contains__(self, _0: Literal["B"], /):
        """
        usage.dask: 4
        """
        ...

    @overload
    def __contains__(self, _0: Literal["b"], /):
        """
        usage.dask: 8
        """
        ...

    @overload
    def __contains__(self, _0: Literal["numbers"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["A_B"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __contains__(self, _0: Literal["B_"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __contains__(self, _0: Literal["dt_col"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["str_col"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["string_col"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["int_col"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["y"], /):
        """
        usage.dask: 8
        """
        ...

    @overload
    def __contains__(self, _0: Literal["X"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["c"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __contains__(self, _0: Literal["w"], /):
        """
        usage.dask: 3
        """
        ...

    @overload
    def __contains__(self, _0: Literal["y_"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __contains__(self, _0: Literal["v"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __contains__(self, _0: Literal["_meta"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["_index"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["dask"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["_name"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["foo"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["tz"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["columns"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["z"], /):
        """
        usage.dask: 5
        """
        ...

    @overload
    def __contains__(self, _0: Literal["col2"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["col1"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["Name"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["index"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["D"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["AA"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __contains__(self, _0: Literal["AB"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __contains__(self, _0: Literal["_typ"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["idx"], /):
        """
        usage.dask: 4
        """
        ...

    @overload
    def __contains__(self, _0: Literal["group"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __contains__(self, _0: Literal["2011-01-02"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["2011-01"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["2011"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["k"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __contains__(self, _0: Literal["d"], /):
        """
        usage.dask: 3
        """
        ...

    @overload
    def __contains__(self, _0: Literal["e"], /):
        """
        usage.dask: 3
        """
        ...

    @overload
    def __contains__(self, _0: Literal["F"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["H"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["cluster"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["a_a"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["A_a"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["value"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["imag"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["__array_struct__"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["__array_interface__"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["_computed"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["real"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["__array_priority__"], /):
        """
        usage.dask: 1
        """
        ...

    def __contains__(self, _0: str, /):
        """
        usage.dask: 130
        usage.koalas: 9
        usage.prophet: 1
        """
        ...

    @overload
    def __eq__(self, _0: List[Literal["bhello", "f", "i64", "i32"]], /):
        """
        usage.koalas: 6
        """
        ...

    @overload
    def __eq__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 4
        """
        ...

    @overload
    def __eq__(self, _0: pandas.core.indexes.base.Index, /):
        """
        usage.dask: 12
        """
        ...

    @overload
    def __eq__(self, _0: List[Literal["x"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __eq__(self, _0: List[Literal["b", "c", "a"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __eq__(
        self,
        _0: List[Literal["petalwidth", "petallength", "sepalwidth", "sepallength"]],
        /,
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __eq__(self, _0: List[Literal["class", "sepalwidth", "sepallength"]], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __eq__(self, _0: List[Literal["petallength", "petalwidth"]], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __eq__(self, _0: List[str], /):
        """
        usage.sklearn: 3
        """
        ...

    def __eq__(
        self, _0: Union[List[str], numpy.ndarray, pandas.core.indexes.base.Index], /
    ):
        """
        usage.dask: 14
        usage.koalas: 6
        usage.pandas: 4
        usage.sklearn: 6
        """
        ...

    @overload
    def __getitem__(self, _0: int, /):
        """
        usage.dask: 17
        usage.koalas: 7
        usage.modin: 3
        usage.prophet: 1
        usage.xarray: 3
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, int, None], /):
        """
        usage.dask: 1
        usage.koalas: 3
        usage.seaborn: 2
        usage.sklearn: 1
        usage.xarray: 2
        """
        ...

    @overload
    def __getitem__(self, _0: numpy.ndarray, /):
        """
        usage.dask: 1
        usage.koalas: 1
        usage.prophet: 1
        usage.sklearn: 2
        usage.xarray: 2
        """
        ...

    @overload
    def __getitem__(self, _0: slice[int, int, int], /):
        """
        usage.dask: 1
        usage.xarray: 2
        """
        ...

    @overload
    def __getitem__(self, _0: slice[int, None, int], /):
        """
        usage.dask: 2
        usage.xarray: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, None, None], /):
        """
        usage.xarray: 2
        """
        ...

    @overload
    def __getitem__(self, _0: slice[int, int, int], /):
        """
        usage.dask: 2
        usage.sklearn: 1
        usage.xarray: 2
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, None, None], /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[int], /):
        """
        usage.dask: 2
        usage.sklearn: 2
        """
        ...

    @overload
    def __getitem__(self, _0: List[bool], /):
        """
        usage.dask: 1
        """
        ...

    def __getitem__(
        self,
        _0: Union[
            numpy.ndarray,
            int,
            List[Union[bool, int]],
            slice[Union[int, None], Union[None, int], Union[int, None]],
        ],
        /,
    ):
        """
        usage.dask: 27
        usage.koalas: 11
        usage.modin: 3
        usage.prophet: 2
        usage.seaborn: 2
        usage.sklearn: 6
        usage.xarray: 15
        """
        ...

    def __iter__(self, /):
        """
        usage.dask: 22
        usage.koalas: 5
        usage.modin: 1
        usage.networkx: 1
        usage.prophet: 3
        usage.sklearn: 1
        usage.xarray: 4
        """
        ...

    def __ne__(self, _0: pandas.core.indexes.base.Index, /):
        """
        usage.sklearn: 2
        """
        ...

    def __radd__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    @overload
    def __rsub__(self, _0: xarray.coding.cftimeindex.CFTimeIndex, /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def __rsub__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 4
        """
        ...

    def __rsub__(
        self, _0: Union[numpy.ndarray, xarray.coding.cftimeindex.CFTimeIndex], /
    ):
        """
        usage.pandas: 4
        usage.xarray: 1
        """
        ...

    def __sub__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    def astype(self, /, dtype: pandas.core.dtypes.dtypes.CategoricalDtype):
        """
        usage.dask: 1
        """
        ...

    def copy(self, /, deep: bool):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def drop(self, /, labels: numpy.ndarray, errors: Literal["raise"]):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def drop(self, /, labels: numpy.ndarray, errors: Literal["ignore"]):
        """
        usage.xarray: 1
        """
        ...

    def drop(self, /, labels: numpy.ndarray, errors: Literal["ignore", "raise"]):
        """
        usage.xarray: 2
        """
        ...

    def dropna(self, /):
        """
        usage.dask: 1
        """
        ...

    def equals(self, /, other: pandas.core.indexes.base.Index):
        """
        usage.xarray: 7
        """
        ...

    @overload
    def get_indexer(self, /, target: numpy.ndarray, method: None, tolerance: None):
        """
        usage.xarray: 2
        """
        ...

    @overload
    def get_indexer(
        self, /, target: numpy.ndarray, method: Literal["pad"], tolerance: None
    ):
        """
        usage.xarray: 1
        """
        ...

    def get_indexer(
        self,
        /,
        target: numpy.ndarray,
        method: Union[Literal["pad"], None],
        tolerance: None,
    ):
        """
        usage.xarray: 3
        """
        ...

    @overload
    def get_loc(self, /, key: Literal["b"], method: None, tolerance: None):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_loc(self, /, key: bool, method: None, tolerance: None):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_loc(self, /, key: Literal["a"], method: None, tolerance: None):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_loc(self, /, key: Literal["c"], method: None, tolerance: None):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_loc(self, /, key: Literal["2000-01-01"], method: None, tolerance: None):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_loc(self, /, key: Literal["2000-01-02"], method: None, tolerance: None):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_loc(self, /, key: Literal["2000-01-03"], method: None, tolerance: None):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_loc(self, /, key: Literal["d"], method: None, tolerance: None):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_loc(self, /, key: str, method: None, tolerance: None):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_loc(self, /, key: Literal["row0"], method: None, tolerance: None):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_loc(self, /, key: Literal["col0"], method: None, tolerance: None):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_loc(self, /, key: Literal["col1"], method: None, tolerance: None):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_loc(self, /, key: Literal["col2"], method: None, tolerance: None):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_loc(self, /, key: Literal["row1"], method: None, tolerance: None):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_loc(self, /, key: Literal["one"], method: None, tolerance: None):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_loc(self, /, key: Literal["two"], method: None, tolerance: None):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_loc(self, /, key: Literal["three"], method: None, tolerance: None):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_loc(self, /, key: Literal["five"], method: None, tolerance: None):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_loc(self, /, key: Literal["A"], method: None, tolerance: None):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_loc(self, /, key: Literal["B"], method: None, tolerance: None):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_loc(self, /, key: Literal["C"], method: None, tolerance: None):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_loc(self, /, key: Literal["C++"], method: None, tolerance: None):
        """
        usage.xarray: 1
        """
        ...

    def get_loc(self, /, key: Union[str, bool], method: None, tolerance: None):
        """
        usage.xarray: 22
        """
        ...

    def max(self, /):
        """
        usage.dask: 1
        """
        ...

    def min(self, /):
        """
        usage.dask: 1
        """
        ...

    def nunique(self, /, dropna: bool):
        """
        usage.koalas: 1
        """
        ...

    def shift(self, /, periods: int, freq: None):
        """
        usage.dask: 1
        """
        ...

    @overload
    def slice_locs(self, /, start: Literal["A"], end: Literal["B"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def slice_locs(self, /, start: Literal["B"], end: None):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def slice_locs(self, /, start: None, end: Literal["A"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def slice_locs(self, /, start: Literal["B"], end: Literal["C"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def slice_locs(self, /, start: Literal["a"], end: Literal["a"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def slice_locs(self, /, start: Literal["a"], end: Literal["d"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def slice_locs(self, /, start: Literal["c"], end: Literal["d"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def slice_locs(self, /, start: Literal["a"], end: Literal["c"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def slice_locs(self, /, start: Literal["b"], end: Literal["c"]):
        """
        usage.koalas: 1
        """
        ...

    def slice_locs(
        self,
        /,
        start: Union[Literal["b", "a", "c", "B", "A"], None],
        end: Union[str, None],
    ):
        """
        usage.koalas: 9
        """
        ...

    def tolist(self, /):
        """
        usage.seaborn: 4
        """
        ...

    @overload
    def value_counts(self, /, normalize: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def value_counts(self, /, ascending: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def value_counts(self, /, normalize: bool, dropna: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def value_counts(self, /, ascending: bool, dropna: bool):
        """
        usage.koalas: 1
        """
        ...

    def value_counts(
        self, /, ascending: bool = ..., normalize: bool = ..., dropna: bool = ...
    ):
        """
        usage.koalas: 4
        """
        ...
