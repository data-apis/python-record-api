from typing import *


class RangeIndex:

    # usage.dask: 1
    __module__: ClassVar[object]

    # usage.dask: 2
    __name__: ClassVar[object]

    # usage.dask: 1
    array: object

    # usage.dask: 11
    # usage.xarray: 4
    dtype: object

    # usage.dask: 1
    is_all_dates: object

    # usage.dask: 1
    # usage.xarray: 2
    is_monotonic: object

    # usage.sklearn: 2
    # usage.xarray: 6
    is_unique: object

    # usage.dask: 16
    # usage.xarray: 4
    name: Union[Literal["ix", "renamed"], None]

    # usage.dask: 1
    names: object

    # usage.xarray: 1
    shape: object

    # usage.xarray: 3
    size: object

    # usage.xarray: 3
    values: object

    def __add__(self, _0: Union[int, numpy.timedelta64, numpy.datetime64], /):
        """
        usage.dask: 1
        usage.pandas: 2
        """
        ...

    def __contains__(self, _0: Union[int, Literal["dtype", "divisions"]], /):
        """
        usage.dask: 3
        """
        ...

    def __eq__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 4
        """
        ...

    def __floordiv__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 4
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
        usage.dask: 5
        usage.xarray: 7
        """
        ...

    def __iter__(self, /):
        """
        usage.xarray: 1
        """
        ...

    def __mod__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 3
        """
        ...

    def __mul__(self, _0: Union[int, numpy.timedelta64, numpy.ndarray], /):
        """
        usage.dask: 1
        usage.pandas: 5
        """
        ...

    def __neg__(self, /):
        """
        usage.dask: 1
        """
        ...

    def __radd__(self, _0: Union[numpy.datetime64, numpy.timedelta64], /):
        """
        usage.pandas: 2
        """
        ...

    def __rfloordiv__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    def __rmul__(self, _0: Union[int, numpy.ndarray, numpy.timedelta64], /):
        """
        usage.dask: 1
        usage.pandas: 2
        """
        ...

    def __rsub__(self, _0: Union[numpy.datetime64, numpy.timedelta64], /):
        """
        usage.pandas: 2
        """
        ...

    def __rtruediv__(self, _0: Union[numpy.timedelta64, numpy.ndarray], /):
        """
        usage.pandas: 2
        """
        ...

    def __sub__(self, _0: Union[numpy.datetime64, numpy.timedelta64], /):
        """
        usage.pandas: 2
        """
        ...

    def __truediv__(self, _0: Union[numpy.ndarray, numpy.timedelta64], /):
        """
        usage.pandas: 5
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
        usage.dask: 2
        usage.xarray: 8
        """
        ...

    def get_indexer(self, /, target: numpy.ndarray, method: None, tolerance: None):
        """
        usage.xarray: 1
        """
        ...

    def get_loc(
        self,
        /,
        key: Union[Literal["random"], int],
        method: None = ...,
        tolerance: None = ...,
    ):
        """
        usage.sklearn: 1
        usage.xarray: 1
        """
        ...

    def map(self, /, mapper: Callable, na_action: None):
        """
        usage.dask: 1
        """
        ...

    def max(self, /):
        """
        usage.dask: 5
        """
        ...

    def memory_usage(self, /):
        """
        usage.dask: 1
        """
        ...

    def min(self, /):
        """
        usage.dask: 5
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
