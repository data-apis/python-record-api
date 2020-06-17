from typing import *


class Index:
    dtype = ...
    values = ...
    is_monotonic_increasing = ...
    size = ...
    is_unique = ...
    is_monotonic = ...
    shape = ...
    name = ...
    nlevels = ...

    def set_names(self, /, names):
        "usage.xarray: 183"

    def equals(
        self,
        /,
        other: Union[
            (
                pandas.core.indexes.numeric.Float64Index,
                pandas.core.indexes.numeric.Int64Index,
                pandas.core.indexes.base.Index,
                pandas.core.indexes.range.RangeIndex,
                pandas.core.indexes.multi.MultiIndex,
            )
        ],
    ):
        "usage.xarray: 24"

    def __getitem__(self, _0, /):
        ""

    def append(self, /, other):
        "usage.xarray: 17"

    def to_series(self, /):
        "usage.xarray: 3"

    def copy(self, /, deep: bool):
        "usage.xarray: 1"

    def rename(
        self,
        /,
        name: Literal[
            (
                "xnew",
                "z",
                "x",
                "dim3",
                "dim2",
                "renamed_dim2",
                "three",
                "new_dim",
                "abc",
                "time_new",
                "y",
                "time",
            )
        ],
    ):
        "usage.xarray: 15"

    def slice_indexer(self, /, start, end, step: None):
        "usage.xarray: 12"

    def get_indexer(
        self,
        /,
        target: numpy.ndarray,
        method: Union[(Literal[("pad",)], None)],
        tolerance: None,
    ):
        "usage.xarray: 3"

    def get_loc(self, /, key, method: None = ..., tolerance: None = ...):
        "usage.xarray: 26"

    def droplevel(
        self, /, level: Union[(List[Literal[("level_1",)]], Literal[("level_1",)])]
    ):
        "usage.xarray: 2"

    def __iter__(self, /):
        ""

    def drop(self, /, labels: numpy.ndarray, errors: Literal[("ignore", "raise")]):
        "usage.xarray: 2"

    def astype(self, /, dtype: numpy.dtype):
        "usage.xarray: 1"
