from typing import *


class NaTType:
    def __add__(self, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        """
        usage.xarray: 2
        """
        ...

    def __ge__(self, _0: pandas._libs.tslibs.nattype.NaTType, /):
        """
        usage.dask: 2
        """
        ...

    def __gt__(self, _0: pandas._libs.tslibs.nattype.NaTType, /):
        """
        usage.dask: 1
        """
        ...

    def __le__(
        self,
        _0: Union[pandas.core.series.Series, pandas._libs.tslibs.nattype.NaTType],
        /,
    ):
        """
        usage.dask: 3
        """
        ...

    def __lt__(self, _0: pandas._libs.tslibs.nattype.NaTType, /):
        """
        usage.dask: 1
        """
        ...
