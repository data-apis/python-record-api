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
        "\n    usage.xarray: 8\n    usage.dask: 2\n    "
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
        "\n    usage.xarray: 7\n    usage.dask: 5\n    "
        ...

    def __iter__(self: object, /):
        "\n    usage.xarray: 1\n    "
        ...

    def get_indexer(
        self: object, /, target: numpy.ndarray, method: None, tolerance: None
    ):
        "\n    usage.xarray: 1\n    "
        ...

    def get_loc(self: object, /, key: int, method: None, tolerance: None):
        "\n    usage.xarray: 1\n    "
        ...

    def copy(self: object, /, deep: bool):
        "\n    usage.xarray: 1\n    "
        ...

    def __contains__(self: object, _0: Union[int, Literal["dtype", "divisions"]], /):
        "\n    usage.dask: 3\n    "
        ...

    def min(self: object, /):
        "\n    usage.dask: 6\n    "
        ...

    def max(self: object, /):
        "\n    usage.dask: 6\n    "
        ...

    def tolist(self: object, /):
        "\n    usage.dask: 1\n    "
        ...

    def drop_duplicates(self: object, /):
        "\n    usage.dask: 1\n    "
        ...

    def __mul__(self: object, _0: int, /):
        "\n    usage.dask: 1\n    "
        ...

    def __add__(self: object, _0: int, /):
        "\n    usage.dask: 1\n    "
        ...

    def __rmul__(self: object, _0: int, /):
        "\n    usage.dask: 1\n    "
        ...

    def __neg__(self: object, /):
        "\n    usage.dask: 1\n    "
        ...

    def to_series(self: object, /):
        "\n    usage.dask: 1\n    "
        ...

    def to_frame(self: object, /, name: Union[Literal["bar"], None]):
        "\n    usage.dask: 3\n    "
        ...

    def memory_usage(self: object, /):
        "\n    usage.dask: 1\n    "
        ...
