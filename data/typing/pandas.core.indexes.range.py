from typing import *


class RangeIndex:

    # usage.dask: 1
    __module__: ClassVar[object]

    # usage.dask: 2
    __name__: ClassVar[object]

    # usage.dask: 1
    array: object

    # usage.xarray: 4
    # usage.dask: 11
    dtype: object

    # usage.dask: 1
    is_all_dates: object

    # usage.xarray: 1
    # usage.dask: 1
    is_monotonic: object

    # usage.dask: 1
    is_monotonic_increasing: object

    # usage.xarray: 5
    is_unique: object

    # usage.xarray: 4
    # usage.dask: 16
    name: Union[Literal["ix", "renamed"], None]

    # usage.dask: 1
    names: object

    # usage.xarray: 1
    shape: object

    # usage.xarray: 3
    size: object

    # usage.xarray: 2
    values: object

    def __add__(self, _0: int, /):
        """
        usage.dask: 1
        """
        ...

    def __contains__(self, _0: Union[int, Literal["dtype", "divisions"]], /):
        """
        usage.dask: 3
        """
        ...

    def __getitem__(
        self,
        _0: Union[
            int,
            numpy.ndarray,
            slice[Union[int, None], Union[None, int], Union[int, None]],
        ],
        /,
    ):
        """
        usage.xarray: 7
        usage.dask: 5
        """
        ...

    def __iter__(self, /):
        """
        usage.xarray: 1
        """
        ...

    def __mul__(self, _0: int, /):
        """
        usage.dask: 1
        """
        ...

    def __neg__(self, /):
        """
        usage.dask: 1
        """
        ...

    def __rmul__(self, _0: int, /):
        """
        usage.dask: 1
        """
        ...

    def copy(self, /, deep: bool):
        """
        usage.xarray: 1
        """
        ...

    def drop_duplicates(self, /):
        """
        usage.dask: 1
        """
        ...

    def equals(
        self,
        /,
        other: Union[
            pandas.core.indexes.range.RangeIndex, pandas.core.indexes.numeric.Int64Index
        ],
    ):
        """
        usage.xarray: 8
        usage.dask: 2
        """
        ...

    def get_indexer(self, /, target: numpy.ndarray, method: None, tolerance: None):
        """
        usage.xarray: 1
        """
        ...

    def get_loc(self, /, key: int, method: None, tolerance: None):
        """
        usage.xarray: 1
        """
        ...

    def max(self, /):
        """
        usage.dask: 6
        """
        ...

    def memory_usage(self, /):
        """
        usage.dask: 1
        """
        ...

    def min(self, /):
        """
        usage.dask: 6
        """
        ...

    def to_frame(self, /, name: Union[Literal["bar"], None]):
        """
        usage.dask: 3
        """
        ...

    def to_series(self, /):
        """
        usage.dask: 1
        """
        ...

    def tolist(self, /):
        """
        usage.dask: 1
        """
        ...
