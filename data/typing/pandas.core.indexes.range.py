from typing import *


class RangeIndex:
    __module__ = ...
    __name__ = ...
    dtype = ...
    values = ...
    name: Union[(Literal[("ix", "renamed")], None)] = ...
    size = ...
    is_unique = ...
    shape = ...
    is_monotonic = ...
    array = ...
    is_monotonic_increasing = ...
    names = ...
    is_all_dates = ...

    def equals(
        self,
        /,
        other: Union[
            (
                pandas.core.indexes.range.RangeIndex,
                pandas.core.indexes.numeric.Int64Index,
            )
        ],
    ):
        "usage.xarray: 8, usage.dask: 2"

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

    def __iter__(self, /):
        ""

    def get_indexer(self, /, target: numpy.ndarray, method: None, tolerance: None):
        "usage.xarray: 1"

    def get_loc(self, /, key: int, method: None, tolerance: None):
        "usage.xarray: 1"

    def copy(self, /, deep: bool):
        "usage.xarray: 1"

    def __contains__(self, _0: Union[(int, Literal[("dtype", "divisions")])], /):
        ""

    def min(self, /):
        "usage.dask: 6"

    def max(self, /):
        "usage.dask: 6"

    def tolist(self, /):
        "usage.dask: 1"

    def drop_duplicates(self, /):
        "usage.dask: 1"

    def __mul__(self, _0: int, /):
        ""

    def __add__(self, _0: int, /):
        ""

    def __rmul__(self, _0: int, /):
        ""

    def __neg__(self, /):
        ""

    def to_series(self, /):
        "usage.dask: 1"

    def to_frame(self, /, name: Union[(Literal[("bar",)], None)] = ...):
        "usage.dask: 3"

    def memory_usage(self, /):
        "usage.dask: 1"
