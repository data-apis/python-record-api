from typing import *


class RangeIndex:

    # usage.dask: 1
    __module__: ClassVar[object]

    # usage.dask: 2
    __name__: ClassVar[object]

    # usage.xarray: 4
    # usage.dask: 11
    dtype: object

    # usage.xarray: 2
    values: object

    # usage.xarray: 4
    # usage.dask: 16
    name: Union[Literal["ix", "renamed"], None]

    # usage.xarray: 3
    size: object

    # usage.xarray: 5
    is_unique: object

    # usage.xarray: 1
    shape: object

    # usage.xarray: 1
    # usage.dask: 1
    is_monotonic: object

    # usage.dask: 1
    array: object

    # usage.dask: 1
    is_monotonic_increasing: object

    # usage.dask: 1
    names: object

    # usage.dask: 1
    is_all_dates: object

    def equals(
        self: object,
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

    def __getitem__(
        self: object,
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

    def __iter__(self: object, /):
        """
        usage.xarray: 1
        """
        ...

    def get_indexer(
        self: object, /, target: numpy.ndarray, method: None, tolerance: None
    ):
        """
        usage.xarray: 1
        """
        ...

    def get_loc(self: object, /, key: int, method: None, tolerance: None):
        """
        usage.xarray: 1
        """
        ...

    def copy(self: object, /, deep: bool):
        """
        usage.xarray: 1
        """
        ...

    def __contains__(self: object, _0: Union[int, Literal["dtype", "divisions"]], /):
        """
        usage.dask: 3
        """
        ...

    def min(self: object, /):
        """
        usage.dask: 6
        """
        ...

    def max(self: object, /):
        """
        usage.dask: 6
        """
        ...

    def tolist(self: object, /):
        """
        usage.dask: 1
        """
        ...

    def drop_duplicates(self: object, /):
        """
        usage.dask: 1
        """
        ...

    def __mul__(self: object, _0: int, /):
        """
        usage.dask: 1
        """
        ...

    def __add__(self: object, _0: int, /):
        """
        usage.dask: 1
        """
        ...

    def __rmul__(self: object, _0: int, /):
        """
        usage.dask: 1
        """
        ...

    def __neg__(self: object, /):
        """
        usage.dask: 1
        """
        ...

    def to_series(self: object, /):
        """
        usage.dask: 1
        """
        ...

    def to_frame(self: object, /, name: Union[Literal["bar"], None]):
        """
        usage.dask: 3
        """
        ...

    def memory_usage(self: object, /):
        """
        usage.dask: 1
        """
        ...
