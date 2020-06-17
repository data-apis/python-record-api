from typing import *


class IntervalIndex:
    name = ...
    dtype = ...
    shape = ...
    values = ...

    def equals(self, /, other: pandas.core.indexes.interval.IntervalIndex):
        "usage.xarray: 1"

    def __getitem__(self, _0: slice[(None, None, None)], /):
        ""
