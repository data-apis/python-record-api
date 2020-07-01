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
        "\n    usage.xarray: 8\n    "
        ...

    def take(self: object, /, indices: numpy.ndarray):
        "\n    usage.xarray: 1\n    "
        ...

    def min(self: object, /):
        "\n    usage.dask: 9\n    "
        ...

    def max(self: object, /):
        "\n    usage.dask: 9\n    "
        ...

    def tolist(self: object, /):
        "\n    usage.dask: 4\n    "
        ...

    def shift(self: object, /, periods: int):
        "\n    usage.dask: 4\n    "
        ...
