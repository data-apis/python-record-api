from typing import *


class DatetimeIndexOpsMixin:
    def equals(
        self,
        /,
        other: Union[
            (
                pandas.core.indexes.datetimes.DatetimeIndex,
                pandas.core.indexes.timedeltas.TimedeltaIndex,
            )
        ],
    ):
        "usage.xarray: 8"

    def take(self, /, indices: numpy.ndarray):
        "usage.xarray: 1"
