from typing import *


class Timedelta:
    def __init__(self, /, value: Union[str, pandas._libs.tslibs.timedeltas.Timedelta]):
        """
        usage.xarray: 6
        usage.dask: 2
        """
        ...

    # usage.dask: 1
    __module__: ClassVar[object]

    def __add__(self, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        """
        usage.xarray: 2
        """
        ...

    def __eq__(self, _0: pandas._libs.tslibs.timedeltas.Timedelta, /):
        """
        usage.dask: 6
        """
        ...

    def __ge__(self, _0: pandas._libs.tslibs.timedeltas.Timedelta, /):
        """
        usage.dask: 3
        """
        ...

    def __gt__(self, _0: pandas.core.series.Series, /):
        """
        usage.dask: 2
        """
        ...

    def __le__(self, _0: pandas._libs.tslibs.timedeltas.Timedelta, /):
        """
        usage.dask: 3
        """
        ...

    def __radd__(self, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        """
        usage.dask: 1
        """
        ...

    def __rsub__(self, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        """
        usage.dask: 3
        """
        ...

    def to_numpy(self, /):
        """
        usage.xarray: 1
        """
        ...

    def to_timedelta64(self, /):
        """
        usage.xarray: 1
        """
        ...

    def total_seconds(self, /):
        """
        usage.xarray: 1
        """
        ...
