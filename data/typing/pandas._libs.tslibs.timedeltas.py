from typing import *


class Timedelta:
    def __init__(
        value: Union[str, pandas._libs.tslibs.timedeltas.Timedelta, numpy.timedelta64]
    ):
        """
        usage.xarray: 10
        usage.dask: 2
        """
        ...

    # usage.dask: 1
    __module__: ClassVar[object]

    def __add__(self: object, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        """
        usage.xarray: 2
        """
        ...

    def __eq__(self: object, _0: pandas._libs.tslibs.timedeltas.Timedelta, /):
        """
        usage.dask: 6
        """
        ...

    def __ge__(self: object, _0: pandas._libs.tslibs.timedeltas.Timedelta, /):
        """
        usage.dask: 3
        """
        ...

    def __le__(self: object, _0: pandas._libs.tslibs.timedeltas.Timedelta, /):
        """
        usage.dask: 3
        """
        ...

    def __gt__(self: object, _0: pandas.core.series.Series, /):
        """
        usage.dask: 2
        """
        ...

    def __rsub__(self: object, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        """
        usage.dask: 3
        """
        ...

    def __radd__(self: object, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        """
        usage.dask: 1
        """
        ...


class _Timedelta:
    @classmethod
    def to_numpy(_0: pandas._libs.tslibs.timedeltas.Timedelta, /):
        """
        usage.xarray: 1
        """
        ...

    @classmethod
    def to_timedelta64(_0: pandas._libs.tslibs.timedeltas.Timedelta, /):
        """
        usage.xarray: 1
        """
        ...
