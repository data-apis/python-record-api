from typing import *


class IntervalIndex:

    # usage.xarray: 1
    name: object

    # usage.xarray: 2
    dtype: object

    # usage.xarray: 1
    shape: object

    # usage.xarray: 1
    values: object

    def equals(self: object, /, other: pandas.core.indexes.interval.IntervalIndex):
        """
        usage.xarray: 1
        """
        ...

    def __getitem__(self: object, _0: slice[None, None, None], /):
        """
        usage.xarray: 1
        """
        ...
