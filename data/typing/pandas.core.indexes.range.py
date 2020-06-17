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
                slice[(Union[(None, int)], Union[(int, None)], Union[(None, int)])],
                int,
                numpy.ndarray,
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
