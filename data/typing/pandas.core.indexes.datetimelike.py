from typing import *


class DatetimeIndexOpsMixin:
    def equals(
        self,
        /,
        other: Union[
            (
                pandas.core.indexes.timedeltas.TimedeltaIndex,
                pandas.core.indexes.datetimes.DatetimeIndex,
            )
        ],
    ):
        "usage.xarray: 8"

    def take(self, /, indices: numpy.ndarray):
        "usage.xarray: 1"
