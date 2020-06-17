from typing import *


class Int64Index:
    dtype = ...
    values = ...
    is_monotonic_increasing = ...
    size = ...
    is_monotonic_decreasing = ...
    is_unique = ...
    shape = ...
    is_monotonic = ...
    name = ...
    nlevels = ...

    def __getitem__(self, _0, /):
        ""

    def get_indexer(
        self,
        /,
        target: numpy.ndarray,
        method: Union[(None, Literal[("backfill",)], Literal[("pad",)])],
        tolerance: Union[(None, float, int)],
    ):
        "usage.xarray: 8"

    def get_loc(
        self,
        /,
        key: Union[(numpy.float64, numpy.int64, int)],
        method: Union[(None, Literal[("nearest",)])] = ...,
    ):
        "usage.xarray: 5"

    def copy(self, /, deep: bool):
        "usage.xarray: 1"

    def __iter__(self, /):
        ""

    def equals(self, /, other: pandas.core.indexes.numeric.Int64Index):
        "usage.xarray: 1"

    def drop(self, /, labels: numpy.ndarray, errors: Literal[("raise", "ignore")]):
        "usage.xarray: 2"


class Float64Index:
    dtype = ...
    values = ...
    is_monotonic_increasing = ...
    size = ...
    is_unique = ...
    is_monotonic = ...
    shape = ...
    name = ...

    def copy(self, /, deep: bool):
        "usage.xarray: 1"

    def equals(
        self,
        /,
        other: Union[
            (
                pandas.core.indexes.base.Index,
                pandas.core.indexes.numeric.Int64Index,
                pandas.core.indexes.numeric.Float64Index,
            )
        ],
    ):
        "usage.xarray: 10"

    def __getitem__(self, _0, /):
        ""

    def get_indexer(
        self,
        /,
        target: numpy.ndarray,
        method: Union[
            (Literal[("backfill",)], Literal[("pad",)], Literal[("nearest",)], None)
        ],
        tolerance: None,
    ):
        "usage.xarray: 8"

    def get_loc(
        self,
        /,
        key: Union[(float, numpy.int64, numpy.float64)],
        method: Union[(None, Literal[("nearest",)])] = ...,
    ):
        "usage.xarray: 7"

    def astype(self, /, dtype: numpy.dtype):
        "usage.xarray: 1"

    def identical(self, /, other: pandas.core.indexes.numeric.Float64Index):
        "usage.xarray: 1"
