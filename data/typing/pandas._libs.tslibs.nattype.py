from typing import *


class NaTType:
    @overload
    def __add__(self, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        """
        usage.xarray: 2
        """
        ...

    @overload
    def __add__(self, _0: Union[numpy.timedelta64, numpy.ndarray], /):
        """
        usage.pandas: 9
        """
        ...

    def __add__(
        self,
        _0: Union[
            numpy.ndarray, numpy.timedelta64, pandas._libs.tslibs.timestamps.Timestamp
        ],
        /,
    ):
        """
        usage.pandas: 9
        usage.xarray: 2
        """
        ...

    def __ge__(self, _0: pandas._libs.tslibs.nattype.NaTType, /):
        """
        usage.dask: 1
        """
        ...

    def __gt__(self, _0: pandas._libs.tslibs.nattype.NaTType, /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __le__(self, _0: pandas._libs.tslibs.nattype.NaTType, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __le__(self, _0: pandas.core.series.Series, /):
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
        usage.dask: 2
        """
        ...

    def __lt__(self, _0: pandas._libs.tslibs.nattype.NaTType, /):
        """
        usage.dask: 2
        """
        ...

    def __ne__(self, _0: Union[numpy.datetime64, numpy.timedelta64], /):
        """
        usage.pandas: 3
        """
        ...

    def __radd__(self, _0: Union[numpy.timedelta64, numpy.ndarray], /):
        """
        usage.pandas: 8
        """
        ...

    def __rsub__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 2
        """
        ...

    def __rtruediv__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    def __sub__(self, _0: Union[numpy.timedelta64, numpy.ndarray], /):
        """
        usage.pandas: 9
        """
        ...

    def __truediv__(self, _0: object, /):
        """
        usage.pandas: 21
        """
        ...
