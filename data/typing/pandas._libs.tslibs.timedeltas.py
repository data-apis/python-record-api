from typing import *


class Timedelta:
    def __init__(self, /, value: Literal["1", "1 hours"], unit: Literal["ms"]):
        """
        usage.dask: 2
        """
        ...

    # usage.dask: 1
    __module__: ClassVar[object]

    # usage.xarray: 1
    __name__: ClassVar[object]

    def __add__(
        self,
        _0: Union[
            numpy.int64,
            numpy.float64,
            numpy.ndarray,
            pandas._libs.tslibs.timestamps.Timestamp,
        ],
        /,
    ):
        """
        usage.pandas: 17
        usage.xarray: 2
        """
        ...

    def __eq__(
        self,
        _0: Union[
            pandas._libs.tslibs.timedeltas.Timedelta,
            numpy.timedelta64,
            numpy.int64,
            numpy.float64,
            numpy.ndarray,
        ],
        /,
    ):
        """
        usage.dask: 6
        usage.pandas: 58
        """
        ...

    def __floordiv__(
        self,
        _0: Union[
            numpy.ndarray, numpy.uint8, numpy.float64, numpy.timedelta64, numpy.int32
        ],
        /,
    ):
        """
        usage.pandas: 14
        """
        ...

    def __ge__(self, _0: pandas._libs.tslibs.timedeltas.Timedelta, /):
        """
        usage.dask: 3
        """
        ...

    def __gt__(self, _0: Union[pandas.core.series.Series, numpy.ndarray], /):
        """
        usage.dask: 2
        usage.pandas: 1
        """
        ...

    def __le__(self, _0: pandas._libs.tslibs.timedeltas.Timedelta, /):
        """
        usage.dask: 3
        """
        ...

    def __mod__(self, _0: numpy.timedelta64, /):
        """
        usage.pandas: 2
        """
        ...

    def __mul__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 6
        """
        ...

    def __ne__(self, _0: Union[numpy.timedelta64, numpy.ndarray], /):
        """
        usage.pandas: 2
        """
        ...

    def __radd__(self, _0: object, /):
        """
        usage.dask: 1
        usage.pandas: 8
        """
        ...

    def __rfloordiv__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    def __rmod__(self, _0: Union[numpy.ndarray, numpy.timedelta64], /):
        """
        usage.pandas: 2
        """
        ...

    def __rmul__(self, _0: Union[numpy.float64, numpy.ndarray, numpy.timedelta64], /):
        """
        usage.pandas: 7
        """
        ...

    def __rsub__(self, _0: object, /):
        """
        usage.dask: 3
        usage.pandas: 10
        """
        ...

    def __rtruediv__(self, _0: Union[numpy.timedelta64, numpy.ndarray], /):
        """
        usage.pandas: 3
        """
        ...

    def __sub__(
        self, _0: Union[numpy.ndarray, numpy.float64, numpy.timedelta64, numpy.int64], /
    ):
        """
        usage.pandas: 18
        """
        ...

    def __truediv__(self, _0: object, /):
        """
        usage.pandas: 33
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
