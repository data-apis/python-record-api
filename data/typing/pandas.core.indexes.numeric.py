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
        method: Union[(Literal[("pad",)], None, Literal[("backfill",)])],
        tolerance: Union[(int, None, float)],
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
                pandas.core.indexes.numeric.Float64Index,
                pandas.core.indexes.numeric.Int64Index,
                pandas.core.indexes.base.Index,
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
            (Literal[("pad",)], Literal[("nearest",)], None, Literal[("backfill",)])
        ],
        tolerance: None,
    ):
        "usage.xarray: 8"

    def get_loc(
        self,
        /,
        key: Union[(numpy.float64, numpy.int64, float)],
        method: Union[(Literal[("nearest",)], None)] = ...,
    ):
        "usage.xarray: 7"

    def astype(self, /, dtype: numpy.dtype):
        "usage.xarray: 1"

    def identical(self, /, other: pandas.core.indexes.numeric.Float64Index):
        "usage.xarray: 1"
