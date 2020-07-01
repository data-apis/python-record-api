from typing import *


class NaTType:
    def __add__(self: object, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        """
        usage.xarray: 2
        """
        ...

    def __ge__(self: object, _0: pandas._libs.tslibs.nattype.NaTType, /):
        """
        usage.dask: 2
        """
        ...

    def __le__(
        self: object,
        _0: Union[pandas.core.series.Series, pandas._libs.tslibs.nattype.NaTType],
        /,
    ):
        """
        usage.dask: 3
        """
        ...

    def __gt__(self: object, _0: pandas._libs.tslibs.nattype.NaTType, /):
        """
        usage.dask: 1
        """
        ...

    def __lt__(self: object, _0: pandas._libs.tslibs.nattype.NaTType, /):
        """
        usage.dask: 1
        """
        ...
