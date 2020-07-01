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
    name: Union[None, Literal["foo", "C", "b", "idx", "a"]]

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
        """
        usage.xarray: 16
        usage.dask: 11
        """
        ...

    def get_indexer(
        self: object,
        /,
        target: numpy.ndarray,
        method: Union[Literal["pad", "backfill"], None],
        tolerance: Union[float, int, None],
    ):
        """
        usage.xarray: 8
        """
        ...

    def get_loc(
        self: object,
        /,
        key: Union[numpy.float64, int, numpy.int64],
        method: Union[Literal["nearest"], None],
    ):
        """
        usage.xarray: 5
        """
        ...

    def copy(self: object, /, deep: bool):
        """
        usage.xarray: 1
        """
        ...

    def __iter__(self: object, /):
        """
        usage.xarray: 1
        usage.dask: 4
        """
        ...

    def equals(self: object, /, other: pandas.core.indexes.numeric.Int64Index):
        """
        usage.xarray: 1
        """
        ...

    def drop(
        self: object, /, labels: numpy.ndarray, errors: Literal["ignore", "raise"]
    ):
        """
        usage.xarray: 2
        """
        ...

    def __contains__(
        self: object,
        _0: Union[None, Literal["__UNKNOWN_CATEGORIES__", "dtype", "divisions"], int],
        /,
    ):
        """
        usage.dask: 6
        """
        ...

    def __le__(self: object, _0: Union[float, int], /):
        """
        usage.dask: 3
        """
        ...

    def __ge__(self: object, _0: Union[float, int], /):
        """
        usage.dask: 3
        """
        ...

    def min(self: object, /):
        """
        usage.dask: 1
        """
        ...

    def max(self: object, /):
        """
        usage.dask: 1
        """
        ...

    def drop_duplicates(self: object, /):
        """
        usage.dask: 2
        """
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
        """
        usage.dask: 4
        """
        ...

    def dropna(self: object, /):
        """
        usage.dask: 1
        """
        ...

    def __gt__(self: object, _0: Union[float, int], /):
        """
        usage.dask: 2
        """
        ...

    def set_names(
        self: object, /, names: List[Literal["a", "b", "key"]], inplace: bool
    ):
        """
        usage.dask: 3
        """
        ...

    def to_series(self: object, /):
        """
        usage.dask: 1
        """
        ...

    def to_frame(self: object, /, index: bool, name: Union[Literal["bar"], None]):
        """
        usage.dask: 2
        """
        ...


class Float64Index:
    def __init__(data: List[float], name: Literal["b"]):
        """
        usage.dask: 1
        """
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
        """
        usage.xarray: 1
        """
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
        """
        usage.xarray: 10
        usage.dask: 1
        """
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
        """
        usage.xarray: 13
        usage.dask: 5
        """
        ...

    def get_indexer(
        self: object,
        /,
        target: numpy.ndarray,
        method: Union[Literal["nearest", "backfill", "pad"], None],
        tolerance: None,
    ):
        """
        usage.xarray: 8
        """
        ...

    def get_loc(
        self: object,
        /,
        key: Union[numpy.int64, float, numpy.float64],
        method: Union[Literal["nearest"], None],
    ):
        """
        usage.xarray: 7
        """
        ...

    def astype(self: object, /, dtype: numpy.dtype):
        """
        usage.xarray: 1
        usage.dask: 1
        """
        ...

    def identical(self: object, /, other: pandas.core.indexes.numeric.Float64Index):
        """
        usage.xarray: 1
        """
        ...

    def __contains__(
        self: object, _0: Literal["dtype", "divisions", "__UNKNOWN_CATEGORIES__"], /
    ):
        """
        usage.dask: 4
        """
        ...

    def set_names(self: object, /, names: List[Literal["b"]], inplace: bool):
        """
        usage.dask: 1
        """
        ...


class UInt64Index:
    def __init__(data: List[int], name: Literal["foo"]):
        """
        usage.dask: 1
        """
        ...

    # usage.dask: 1
    __module__: ClassVar[object]

    # usage.dask: 2
    name: object
