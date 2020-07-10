from typing import *


class IntervalIndex:

    # usage.xarray: 2
    dtype: object

    # usage.xarray: 1
    name: object

    # usage.xarray: 1
    shape: object

    # usage.xarray: 1
    values: object

    def __getitem__(self, _0: slice[None, None, None], /):
        """
        usage.xarray: 1
        """
        ...

    def equals(self, /, other: pandas.core.indexes.interval.IntervalIndex):
        """
        usage.xarray: 1
        """
        ...
