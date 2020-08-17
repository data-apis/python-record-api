from typing import *


class DatetimeIndexOpsMixin:
    def isin(self, /, values: pandas.core.indexes.datetimes.DatetimeIndex):
        """
        usage.dask: 1
        """
        ...

    def max(self, /):
        """
        usage.dask: 9
        """
        ...

    def min(self, /):
        """
        usage.dask: 9
        """
        ...

    def shift(self, /, periods: int):
        """
        usage.dask: 4
        """
        ...

    def tolist(self, /):
        """
        usage.dask: 4
        """
        ...
