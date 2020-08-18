from typing import *


class Index:

    # usage.dask: 2
    __name__: ClassVar[object]

    # usage.xarray: 2
    get_loc: ClassVar[object]

    # usage.dask: 1
    array: object

    # usage.dask: 13
    # usage.sklearn: 2
    # usage.xarray: 6
    dtype: object

    # usage.dask: 1
    # usage.xarray: 2
    is_monotonic: object

    # usage.dask: 1
    # usage.xarray: 6
    is_unique: object

    # usage.dask: 16
    # usage.xarray: 13
    name: Union[None, Literal["A", "a"]]

    # usage.dask: 3
    names: List[str]

    # usage.xarray: 1
    nlevels: object

    # usage.xarray: 1
    shape: object

    # usage.xarray: 10
    size: object

    # usage.dask: 2
    # usage.sklearn: 1
    str: object

    # usage.dask: 1
    # usage.xarray: 6
    values: object

    def __contains__(self, _0: str, /):
        """
        usage.dask: 131
        """
        ...

    @overload
    def __eq__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 4
        """
        ...

    @overload
    def __eq__(
        self,
        _0: Union[List[Literal["x", "b", "c", "a"]], pandas.core.indexes.base.Index],
        /,
    ):
        """
        usage.dask: 14
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
        usage.pandas: 4
        usage.sklearn: 6
        """
        ...

    @overload
    def __getitem__(self, _0: int, /):
        """
        usage.xarray: 3
        """
        ...

    @overload
    def __getitem__(self, _0: numpy.ndarray, /):
        """
        usage.sklearn: 2
        usage.xarray: 2
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, int, None], /):
        """
        usage.sklearn: 1
        usage.xarray: 2
        """
        ...

    @overload
    def __getitem__(self, _0: slice[int, int, int], /):
        """
        usage.xarray: 2
        """
        ...

    @overload
    def __getitem__(self, _0: slice[int, None, int], /):
        """
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
    def __getitem__(
        self,
        _0: Union[
            slice[Union[None, int], Union[int, None], Union[None, int]],
            numpy.ndarray,
            int,
            List[Union[bool, int]],
        ],
        /,
    ):
        """
        usage.dask: 27
        """
        ...

    @overload
    def __getitem__(self, _0: List[int], /):
        """
        usage.sklearn: 2
        """
        ...

    def __getitem__(
        self,
        _0: Union[
            numpy.ndarray,
            int,
            List[Union[bool, int]],
            slice[Union[None, int], Union[None, int], Union[None, int]],
        ],
        /,
    ):
        """
        usage.dask: 27
        usage.sklearn: 6
        usage.xarray: 15
        """
        ...

    def __iter__(self, /):
        """
        usage.dask: 22
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

    def _get_level_values(self, /, level: int):
        """
        usage.dask: 7
        """
        ...

    def append(
        self, /, other: Union[list, pandas.core.indexes.category.CategoricalIndex]
    ):
        """
        usage.dask: 16
        """
        ...

    def astype(
        self,
        /,
        dtype: Union[
            Literal["int64"], pandas.core.dtypes.dtypes.CategoricalDtype, numpy.dtype
        ],
    ):
        """
        usage.dask: 12
        """
        ...

    def copy(self, /, deep: bool):
        """
        usage.xarray: 1
        """
        ...

    def difference(
        self, /, other: Union[List[Literal["A"]], pandas.core.indexes.base.Index]
    ):
        """
        usage.dask: 6
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

    @overload
    def drop(self, /, labels: numpy.ndarray):
        """
        usage.dask: 1
        """
        ...

    def drop(self, /, labels: numpy.ndarray, errors: Literal["ignore", "raise"] = ...):
        """
        usage.dask: 1
        usage.xarray: 2
        """
        ...

    def drop_duplicates(self, /):
        """
        usage.dask: 1
        """
        ...

    def dropna(self, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def equals(self, /, other: pandas.core.indexes.base.Index):
        """
        usage.xarray: 7
        """
        ...

    @overload
    def equals(
        self,
        /,
        other: Union[
            pandas.core.indexes.numeric.Int64Index, pandas.core.indexes.base.Index
        ],
    ):
        """
        usage.dask: 3
        """
        ...

    def equals(
        self,
        /,
        other: Union[
            pandas.core.indexes.base.Index, pandas.core.indexes.numeric.Int64Index
        ],
    ):
        """
        usage.dask: 3
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

    def get_slice_bound(
        self, /, label: object, side: Literal["left", "right"], kind: Literal["loc"]
    ):
        """
        usage.dask: 30
        """
        ...

    def intersection(self, /, other: pandas.core.indexes.base.Index):
        """
        usage.dask: 2
        """
        ...

    def isin(self, /, values: Union[pandas.core.series.Series, List[int]]):
        """
        usage.dask: 4
        """
        ...

    def max(self, /):
        """
        usage.dask: 1
        """
        ...

    def memory_usage(self, /):
        """
        usage.dask: 3
        """
        ...

    def min(self, /):
        """
        usage.dask: 1
        """
        ...

    def rename(self, /, name: Literal["renamed"]):
        """
        usage.dask: 1
        """
        ...

    def shift(self, /, periods: int, freq: None):
        """
        usage.dask: 1
        """
        ...

    def to_frame(
        self, /, index: bool = ..., name: Union[Literal["bar", "foo"], None] = ...
    ):
        """
        usage.dask: 6
        """
        ...

    def to_series(self, /):
        """
        usage.dask: 11
        """
        ...

    def union(
        self,
        /,
        other: Union[
            pandas.core.indexes.datetimes.DatetimeIndex,
            pandas.core.indexes.numeric.Int64Index,
        ],
    ):
        """
        usage.dask: 6
        """
        ...

    def unique(self, /):
        """
        usage.dask: 3
        """
        ...
