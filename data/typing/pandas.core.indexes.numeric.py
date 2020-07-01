from typing import *


class Int64Index:

    # usage.dask: 3
    __name__: ClassVar[object]

    # usage.dask: 1
    __module__: ClassVar[object]

    # usage.xarray: 6
    # usage.dask: 11
    dtype: object

    # usage.xarray: 2
    # usage.dask: 3
    values: object

    # usage.xarray: 2
    # usage.dask: 2
    is_monotonic_increasing: object

    # usage.xarray: 6
    # usage.dask: 2
    size: object

    # usage.xarray: 2
    is_monotonic_decreasing: object

    # usage.xarray: 4
    is_unique: object

    # usage.xarray: 2
    shape: object

    # usage.xarray: 1
    # usage.dask: 1
    is_monotonic: object

    # usage.xarray: 11
    # usage.dask: 19
    name: Union[None, Literal[("foo", "C", "b", "idx", "a")]]

    # usage.xarray: 1
    # usage.dask: 1
    nlevels: object

    # usage.dask: 6
    names: Union[
        pandas.core.indexes.frozen.FrozenList, List[Literal["-overlapped-index-name-0"]]
    ]

    # usage.dask: 1
    array: object

    # usage.dask: 2
    nbytes: object

    # usage.dask: 1
    __class__: object

    def __getitem__(
        self: object,
        _0: Union[
            int,
            numpy.ndarray,
            slice[Union[int, None], Union[None, int], Union[int, None]],
        ],
        /,
    ):
        "\n    usage.xarray: 16\n    usage.dask: 11\n    "
        ...

    def get_indexer(
        self: object,
        /,
        target: numpy.ndarray,
        method: Union[Literal[("pad", "backfill")], None],
        tolerance: Union[float, int, None],
    ):
        "\n    usage.xarray: 8\n    "
        ...

    def get_loc(
        self: object,
        /,
        key: Union[numpy.float64, int, numpy.int64],
        method: Union[Literal["nearest"], None],
    ):
        "\n    usage.xarray: 5\n    "
        ...

    def copy(self: object, /, deep: bool):
        "\n    usage.xarray: 1\n    "
        ...

    def __iter__(self: object, /):
        "\n    usage.xarray: 1\n    usage.dask: 4\n    "
        ...

    def equals(self: object, /, other: pandas.core.indexes.numeric.Int64Index):
        "\n    usage.xarray: 1\n    "
        ...

    def drop(
        self: object, /, labels: numpy.ndarray, errors: Literal[("ignore", "raise")]
    ):
        "\n    usage.xarray: 2\n    "
        ...

    def __contains__(
        self: object,
        _0: Union[None, Literal[("__UNKNOWN_CATEGORIES__", "dtype", "divisions")], int],
        /,
    ):
        "\n    usage.dask: 6\n    "
        ...

    def __le__(self: object, _0: Union[float, int], /):
        "\n    usage.dask: 3\n    "
        ...

    def __ge__(self: object, _0: Union[float, int], /):
        "\n    usage.dask: 3\n    "
        ...

    def min(self: object, /):
        "\n    usage.dask: 1\n    "
        ...

    def max(self: object, /):
        "\n    usage.dask: 1\n    "
        ...

    def drop_duplicates(self: object, /):
        "\n    usage.dask: 2\n    "
        ...

    def isin(
        self: object,
        /,
        values: Union[
            pandas.core.series.Series,
            dask.delayed.Delayed,
            dask.delayed.DelayedLeaf,
            List[int],
        ],
    ):
        "\n    usage.dask: 4\n    "
        ...

    def dropna(self: object, /):
        "\n    usage.dask: 1\n    "
        ...

    def __gt__(self: object, _0: Union[float, int], /):
        "\n    usage.dask: 2\n    "
        ...

    def set_names(
        self: object, /, names: List[Literal[("a", "b", "key")]], inplace: bool
    ):
        "\n    usage.dask: 3\n    "
        ...

    def to_series(self: object, /):
        "\n    usage.dask: 1\n    "
        ...

    def to_frame(self: object, /, index: bool, name: Union[Literal["bar"], None]):
        "\n    usage.dask: 2\n    "
        ...


class Float64Index:
    def __init__(data: List[float], name: Literal["b"]):
        "\n    usage.dask: 1\n    "
        ...

    # usage.dask: 1
    __module__: ClassVar[object]

    # usage.dask: 2
    __name__: ClassVar[object]

    # usage.xarray: 3
    # usage.dask: 7
    dtype: object

    # usage.xarray: 3
    # usage.dask: 2
    values: object

    # usage.xarray: 2
    # usage.dask: 1
    is_monotonic_increasing: object

    # usage.xarray: 2
    size: object

    # usage.xarray: 3
    is_unique: object

    # usage.xarray: 2
    # usage.dask: 1
    is_monotonic: object

    # usage.xarray: 1
    shape: object

    # usage.xarray: 1
    # usage.dask: 9
    name: Union[Literal["x"], None]

    # usage.dask: 1
    array: object

    # usage.dask: 4
    names: List[Literal["-overlapped-index-name-0"]]

    def copy(self: object, /, deep: bool):
        "\n    usage.xarray: 1\n    "
        ...

    def equals(
        self: object,
        /,
        other: Union[
            pandas.core.indexes.numeric.Float64Index,
            pandas.core.indexes.numeric.Int64Index,
            pandas.core.indexes.base.Index,
        ],
    ):
        "\n    usage.xarray: 10\n    usage.dask: 1\n    "
        ...

    def __getitem__(
        self: object,
        _0: Union[
            int,
            numpy.ndarray,
            slice[Union[None, int], Union[int, None], Union[None, int]],
        ],
        /,
    ):
        "\n    usage.xarray: 13\n    usage.dask: 5\n    "
        ...

    def get_indexer(
        self: object,
        /,
        target: numpy.ndarray,
        method: Union[Literal[("nearest", "backfill", "pad")], None],
        tolerance: None,
    ):
        "\n    usage.xarray: 8\n    "
        ...

    def get_loc(
        self: object,
        /,
        key: Union[numpy.int64, float, numpy.float64],
        method: Union[Literal["nearest"], None],
    ):
        "\n    usage.xarray: 7\n    "
        ...

    def astype(self: object, /, dtype: numpy.dtype):
        "\n    usage.xarray: 1\n    usage.dask: 1\n    "
        ...

    def identical(self: object, /, other: pandas.core.indexes.numeric.Float64Index):
        "\n    usage.xarray: 1\n    "
        ...

    def __contains__(
        self: object, _0: Literal[("dtype", "divisions", "__UNKNOWN_CATEGORIES__")], /
    ):
        "\n    usage.dask: 4\n    "
        ...

    def set_names(self: object, /, names: List[Literal["b"]], inplace: bool):
        "\n    usage.dask: 1\n    "
        ...


class UInt64Index:
    def __init__(data: List[int], name: Literal["foo"]):
        "\n    usage.dask: 1\n    "
        ...

    # usage.dask: 1
    __module__: ClassVar[object]

    # usage.dask: 2
    name: object
