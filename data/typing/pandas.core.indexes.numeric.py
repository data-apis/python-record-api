from typing import *


class Float64Index:
    def __init__(self, /, data: List[float], name: Literal["b"]):
        """
        usage.dask: 1
        """
        ...

    # usage.dask: 1
    __module__: ClassVar[object]

    # usage.dask: 2
    __name__: ClassVar[object]

    # usage.dask: 1
    array: object

    # usage.xarray: 3
    # usage.dask: 7
    dtype: object

    # usage.xarray: 2
    # usage.dask: 1
    is_monotonic: object

    # usage.xarray: 2
    # usage.dask: 1
    is_monotonic_increasing: object

    # usage.xarray: 3
    is_unique: object

    # usage.xarray: 1
    # usage.dask: 9
    name: Union[Literal["x"], None]

    # usage.dask: 4
    names: List[Literal["-overlapped-index-name-0"]]

    # usage.xarray: 1
    shape: object

    # usage.xarray: 2
    size: object

    # usage.xarray: 3
    # usage.dask: 2
    values: object

    def __contains__(
        self, _0: Literal["dtype", "divisions", "__UNKNOWN_CATEGORIES__"], /
    ):
        """
        usage.dask: 4
        """
        ...

    def __getitem__(
        self,
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

    def astype(self, /, dtype: numpy.dtype):
        """
        usage.xarray: 1
        usage.dask: 1
        """
        ...

    def copy(self, /, deep: bool):
        """
        usage.xarray: 1
        """
        ...

    def equals(
        self,
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

    def get_indexer(
        self,
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
        self,
        /,
        key: Union[numpy.int64, float, numpy.float64],
        method: Union[Literal["nearest"], None],
    ):
        """
        usage.xarray: 7
        """
        ...

    def identical(self, /, other: pandas.core.indexes.numeric.Float64Index):
        """
        usage.xarray: 1
        """
        ...

    def set_names(self, /, names: List[Literal["b"]], inplace: bool):
        """
        usage.dask: 1
        """
        ...


class Int64Index:

    # usage.dask: 1
    __module__: ClassVar[object]

    # usage.dask: 3
    __name__: ClassVar[object]

    # usage.dask: 1
    __class__: object

    # usage.dask: 1
    array: object

    # usage.xarray: 6
    # usage.dask: 11
    dtype: object

    # usage.xarray: 1
    # usage.dask: 1
    is_monotonic: object

    # usage.xarray: 2
    is_monotonic_decreasing: object

    # usage.xarray: 2
    # usage.dask: 2
    is_monotonic_increasing: object

    # usage.xarray: 4
    is_unique: object

    # usage.xarray: 11
    # usage.dask: 19
    name: Union[None, Literal["foo", "C", "b", "idx", "a"]]

    # usage.dask: 6
    names: Union[
        pandas.core.indexes.frozen.FrozenList, List[Literal["-overlapped-index-name-0"]]
    ]

    # usage.dask: 2
    nbytes: object

    # usage.xarray: 1
    # usage.dask: 1
    nlevels: object

    # usage.xarray: 2
    shape: object

    # usage.xarray: 6
    # usage.dask: 2
    size: object

    # usage.xarray: 2
    # usage.dask: 3
    values: object

    def __contains__(
        self,
        _0: Union[None, Literal["__UNKNOWN_CATEGORIES__", "dtype", "divisions"], int],
        /,
    ):
        """
        usage.dask: 6
        """
        ...

    def __ge__(self, _0: Union[float, int], /):
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
        usage.xarray: 16
        usage.dask: 11
        """
        ...

    def __gt__(self, _0: Union[float, int], /):
        """
        usage.dask: 2
        """
        ...

    def __iter__(self, /):
        """
        usage.xarray: 1
        usage.dask: 4
        """
        ...

    def __le__(self, _0: Union[float, int], /):
        """
        usage.dask: 3
        """
        ...

    def copy(self, /, deep: bool):
        """
        usage.xarray: 1
        """
        ...

    def drop(self, /, labels: numpy.ndarray, errors: Literal["ignore", "raise"]):
        """
        usage.xarray: 2
        """
        ...

    def drop_duplicates(self, /):
        """
        usage.dask: 2
        """
        ...

    def dropna(self, /):
        """
        usage.dask: 1
        """
        ...

    def equals(self, /, other: pandas.core.indexes.numeric.Int64Index):
        """
        usage.xarray: 1
        """
        ...

    def get_indexer(
        self,
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
        self,
        /,
        key: Union[numpy.float64, int, numpy.int64],
        method: Union[Literal["nearest"], None],
    ):
        """
        usage.xarray: 5
        """
        ...

    def isin(
        self,
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

    def set_names(self, /, names: List[Literal["a", "b", "key"]], inplace: bool):
        """
        usage.dask: 3
        """
        ...

    def to_frame(self, /, index: bool, name: Union[Literal["bar"], None]):
        """
        usage.dask: 2
        """
        ...

    def to_series(self, /):
        """
        usage.dask: 1
        """
        ...


class UInt64Index:
    def __init__(self, /, data: List[int], name: Literal["foo"]):
        """
        usage.dask: 1
        """
        ...

    # usage.dask: 1
    __module__: ClassVar[object]

    # usage.dask: 2
    name: object
