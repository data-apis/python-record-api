from typing import *


class DatetimeIndexOpsMixin:
    def equals(
        self,
        /,
        other: Union[
            pandas.core.indexes.timedeltas.TimedeltaIndex,
            pandas.core.indexes.datetimes.DatetimeIndex,
        ],
    ):
        """
        usage.xarray: 8
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

    def take(self, /, indices: numpy.ndarray):
        """
        usage.xarray: 1
        """
        ...

    def tolist(self, /):
        """
        usage.dask: 4
        """
        ...
