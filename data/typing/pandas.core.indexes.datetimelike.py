from typing import *


class DatetimeIndexOpsMixin:
    def equals(
        self: object,
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

    def take(self: object, /, indices: numpy.ndarray):
        """
        usage.xarray: 1
        """
        ...

    def min(self: object, /):
        """
        usage.dask: 9
        """
        ...

    def max(self: object, /):
        """
        usage.dask: 9
        """
        ...

    def tolist(self: object, /):
        """
        usage.dask: 4
        """
        ...

    def shift(self: object, /, periods: int):
        """
        usage.dask: 4
        """
        ...
