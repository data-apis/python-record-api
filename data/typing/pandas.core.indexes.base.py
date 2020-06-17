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

    def set_names(self, /, names: Union[(int, numpy.str_, List[int])]):
        "usage.xarray: 183"

    def equals(
        self,
        /,
        other: Union[
            (
                pandas.core.indexes.base.Index,
                pandas.core.indexes.multi.MultiIndex,
                pandas.core.indexes.numeric.Float64Index,
                pandas.core.indexes.numeric.Int64Index,
                pandas.core.indexes.range.RangeIndex,
            )
        ],
    ):
        "usage.xarray: 24"

    def __getitem__(
        self,
        _0: Union[
            (
                slice[(Union[(None, int)], Union[(None, int)], Union[(None, int)])],
                numpy.ndarray,
                int,
            )
        ],
        /,
    ):
        ""

    def append(self, /, other: Union[(list, pandas.core.indexes.numeric.Int64Index)]):
        "usage.xarray: 17"

    def to_series(self, /):
        "usage.xarray: 3"

    def copy(self, /, deep: bool):
        "usage.xarray: 1"

    def rename(self, /, name: int):
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

    def get_loc(
        self, /, key: Union[(int, bool)], method: None = ..., tolerance: None = ...
    ):
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
