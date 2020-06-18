from typing import *


class Int64Index:
    __name__ = ...
    __module__ = ...
    dtype = ...
    values = ...
    is_monotonic_increasing = ...
    size = ...
    is_monotonic_decreasing = ...
    is_unique = ...
    shape = ...
    is_monotonic = ...
    name: Union[(None, Literal[("foo", "C", "b", "idx", "a")])] = ...
    nlevels = ...
    names: Union[
        (
            pandas.core.indexes.frozen.FrozenList,
            List[Literal[("-overlapped-index-name-0",)]],
        )
    ] = ...
    array = ...
    nbytes = ...
    __class__ = ...

    def __getitem__(
        self,
        _0: Union[
            (
                int,
                numpy.ndarray,
                slice[(Union[(int, None)], Union[(None, int)], Union[(int, None)])],
            )
        ],
        /,
    ):
        ""

    def get_indexer(
        self,
        /,
        target: numpy.ndarray,
        method: Union[(Literal[("pad", "backfill")], None)],
        tolerance: Union[(float, int, None)],
    ):
        "usage.xarray: 8"

    def get_loc(
        self,
        /,
        key: Union[(numpy.float64, int, numpy.int64)],
        method: Union[(Literal[("nearest",)], None)] = ...,
    ):
        "usage.xarray: 5"

    def copy(self, /, deep: bool):
        "usage.xarray: 1"

    def __iter__(self, /):
        ""

    def equals(self, /, other: pandas.core.indexes.numeric.Int64Index):
        "usage.xarray: 1"

    def drop(self, /, labels: numpy.ndarray, errors: Literal[("ignore", "raise")]):
        "usage.xarray: 2"

    def __contains__(
        self,
        _0: Union[
            (None, Literal[("__UNKNOWN_CATEGORIES__", "dtype", "divisions")], int)
        ],
        /,
    ):
        ""

    def __le__(self, _0: Union[(float, int)], /):
        ""

    def __ge__(self, _0: Union[(float, int)], /):
        ""

    def min(self, /):
        "usage.dask: 1"

    def max(self, /):
        "usage.dask: 1"

    def drop_duplicates(self, /):
        "usage.dask: 2"

    def isin(
        self,
        /,
        values: Union[
            (
                pandas.core.series.Series,
                dask.delayed.Delayed,
                dask.delayed.DelayedLeaf,
                List[int],
            )
        ],
    ):
        "usage.dask: 4"

    def dropna(self, /):
        "usage.dask: 1"

    def __gt__(self, _0: Union[(float, int)], /):
        ""

    def set_names(self, /, names: List[Literal[("a", "b", "key")]], inplace: bool):
        "usage.dask: 3"

    def to_series(self, /):
        "usage.dask: 1"

    def to_frame(self, /, index: bool, name: Union[(Literal[("bar",)], None)]):
        "usage.dask: 2"


class Float64Index:
    def __init__(data: List[float], name: Literal[("b",)]):
        "usage.dask: 1"

    __module__ = ...
    __name__ = ...
    dtype = ...
    values = ...
    is_monotonic_increasing = ...
    size = ...
    is_unique = ...
    is_monotonic = ...
    shape = ...
    name: Union[(Literal[("x",)], None)] = ...
    array = ...
    names: List[Literal[("-overlapped-index-name-0",)]] = ...

    def copy(self, /, deep: bool):
        "usage.xarray: 1"

    def equals(
        self,
        /,
        other: Union[
            (
                pandas.core.indexes.numeric.Float64Index,
                pandas.core.indexes.numeric.Int64Index,
                pandas.core.indexes.base.Index,
            )
        ],
    ):
        "usage.xarray: 10, usage.dask: 1"

    def __getitem__(
        self,
        _0: Union[
            (
                int,
                numpy.ndarray,
                slice[(Union[(None, int)], Union[(int, None)], Union[(None, int)])],
            )
        ],
        /,
    ):
        ""

    def get_indexer(
        self,
        /,
        target: numpy.ndarray,
        method: Union[(Literal[("nearest", "backfill", "pad")], None)],
        tolerance: None,
    ):
        "usage.xarray: 8"

    def get_loc(
        self,
        /,
        key: Union[(numpy.int64, float, numpy.float64)],
        method: Union[(Literal[("nearest",)], None)] = ...,
    ):
        "usage.xarray: 7"

    def astype(self, /, dtype: numpy.dtype):
        "usage.xarray: 1, usage.dask: 1"

    def identical(self, /, other: pandas.core.indexes.numeric.Float64Index):
        "usage.xarray: 1"

    def __contains__(
        self, _0: Literal[("dtype", "divisions", "__UNKNOWN_CATEGORIES__")], /
    ):
        ""

    def set_names(self, /, names: List[Literal[("b",)]], inplace: bool):
        "usage.dask: 1"


class UInt64Index:
    def __init__(data: List[int], name: Literal[("foo",)]):
        "usage.dask: 1"

    __module__ = ...
    name = ...
