from typing import *


class Index:

    # usage.dask: 2
    __name__: ClassVar[object]

    # usage.dask: 1
    array: object

    # usage.xarray: 6
    # usage.dask: 14
    dtype: object

    # usage.xarray: 1
    # usage.dask: 1
    is_monotonic: object

    # usage.xarray: 1
    # usage.dask: 2
    is_monotonic_increasing: object

    # usage.xarray: 5
    is_unique: object

    # usage.xarray: 11
    # usage.dask: 14
    name: Union[None, Literal["A"]]

    # usage.dask: 3
    names: List[Literal["-overlapped-index-name-0"]]

    # usage.xarray: 1
    nlevels: object

    # usage.xarray: 1
    shape: object

    # usage.xarray: 7
    size: object

    # usage.dask: 1
    str: object

    # usage.xarray: 3
    values: object

    def __contains__(self, _0: str, /):
        """
        usage.dask: 135
        """
        ...

    def __eq__(
        self,
        _0: Union[List[Literal["x", "b", "c", "a"]], pandas.core.indexes.base.Index],
        /,
    ):
        """
        usage.dask: 14
        """
        ...

    def __getitem__(
        self,
        _0: Union[
            int,
            numpy.ndarray,
            slice[Union[int, None], Union[int, None], Union[int, None]],
        ],
        /,
    ):
        """
        usage.xarray: 14
        usage.dask: 22
        """
        ...

    def __iter__(self, /):
        """
        usage.xarray: 3
        usage.dask: 22
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
            list,
        ],
    ):
        """
        usage.xarray: 17
        usage.dask: 16
        """
        ...

    def astype(self, /, dtype: Union[numpy.dtype, Literal["int64"]]):
        """
        usage.xarray: 1
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

    def drop(self, /, labels: numpy.ndarray):
        """
        usage.xarray: 2
        usage.dask: 1
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

    def equals(
        self,
        /,
        other: Union[
            pandas.core.indexes.base.Index,
            pandas.core.indexes.numeric.Int64Index,
            pandas.core.indexes.range.RangeIndex,
            pandas.core.indexes.numeric.Float64Index,
            pandas.core.indexes.multi.MultiIndex,
        ],
    ):
        """
        usage.xarray: 24
        usage.dask: 3
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
        self, /, key: Union[str, bool], method: None = ..., tolerance: None = ...
    ):
        """
        usage.xarray: 26
        """
        ...

    def get_slice_bound(
        self, /, label: object, side: Literal["left", "right"], kind: Literal["loc"]
    ):
        """
        usage.dask: 32
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
        usage.xarray: 15
        usage.dask: 1
        """
        ...

    def set_names(self, /, names: Union[str, numpy.str_, List[str]]):
        """
        usage.xarray: 183
        """
        ...

    def shift(self, /, periods: int, freq: None):
        """
        usage.dask: 1
        """
        ...

    def slice_indexer(self, /, start: object, end: object, step: None):
        """
        usage.xarray: 12
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
        usage.xarray: 3
        usage.dask: 7
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
        usage.dask: 2
        """
        ...
