from typing import *


class RangeIndex:
    dtype = ...
    values = ...
    name = ...
    size = ...
    is_unique = ...
    shape = ...
    is_monotonic = ...

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
        "usage.xarray: 8"

    def __getitem__(
        self,
        _0: Union[
            (
                numpy.ndarray,
                int,
                slice[(None, int, None)],
                slice[(int, int, None)],
                slice[(None, None, int)],
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
