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

    def __eq__(
        self, _0: Union[List[str], numpy.ndarray, pandas.core.indexes.base.Index], /
    ):
        """
        usage.dask: 14
        usage.pandas: 4
        usage.sklearn: 6
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
        self,
        /,
        other: Union[
            pandas.core.indexes.category.CategoricalIndex,
            pandas.core.indexes.numeric.Int64Index,
            pandas.core.indexes.datetimes.DatetimeIndex,
            list,
        ],
    ):
        """
        usage.dask: 16
        usage.xarray: 21
        """
        ...

    def astype(
        self,
        /,
        dtype: Union[
            numpy.dtype, pandas.core.dtypes.dtypes.CategoricalDtype, Literal["int64"]
        ],
    ):
        """
        usage.dask: 12
        usage.xarray: 1
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

    def drop(self, /, labels: numpy.ndarray):
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

    def droplevel(self, /, level: Union[List[Literal["level_1"]], Literal["level_1"]]):
        """
        usage.xarray: 2
        """
        ...

    def dropna(self, /):
        """
        usage.dask: 1
        """
        ...

    def equals(self, /, other: object):
        """
        usage.dask: 3
        usage.xarray: 38
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

    def get_loc(
        self,
        /,
        key: object,
        method: Union[None, Literal["backfill", "pad", "nearest"]] = ...,
        tolerance: Union[None, datetime.timedelta] = ...,
    ):
        """
        usage.sklearn: 20
        usage.xarray: 66
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

    def rename(self, /, name: str):
        """
        usage.dask: 1
        usage.xarray: 15
        """
        ...

    def set_names(self, /, names: Union[str, numpy.str_, List[str]]):
        """
        usage.xarray: 197
        """
        ...

    def shift(self, /, periods: int, freq: None):
        """
        usage.dask: 1
        """
        ...

    def slice_indexer(self, /, start: object, end: object, step: None):
        """
        usage.xarray: 11
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
        usage.xarray: 3
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
