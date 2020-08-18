from typing import *


class Timedelta:

    # usage.dask: 1
    __module__: ClassVar[object]

    # usage.xarray: 1
    __name__: ClassVar[object]

    @overload
    def __add__(self, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        """
        usage.xarray: 2
        """
        ...

    @overload
    def __add__(self, _0: Union[numpy.ndarray, numpy.float64, numpy.int64], /):
        """
        usage.pandas: 17
        """
        ...

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

    @overload
    def __eq__(
        self, _0: Union[numpy.ndarray, numpy.float64, numpy.int64, numpy.timedelta64], /
    ):
        """
        usage.pandas: 58
        """
        ...

    @overload
    def __eq__(self, _0: pandas._libs.tslibs.timedeltas.Timedelta, /):
        """
        usage.dask: 4
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
        usage.dask: 4
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

    @overload
    def __gt__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    @overload
    def __gt__(self, _0: pandas._libs.tslibs.timedeltas.Timedelta, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __gt__(self, _0: pandas.core.series.Series, /):
        """
        usage.dask: 2
        """
        ...

    def __gt__(
        self,
        _0: Union[
            pandas._libs.tslibs.timedeltas.Timedelta,
            pandas.core.series.Series,
            numpy.ndarray,
        ],
        /,
    ):
        """
        usage.dask: 3
        usage.pandas: 1
        """
        ...

    def __le__(self, _0: pandas._libs.tslibs.timedeltas.Timedelta, /):
        """
        usage.dask: 3
        """
        ...

    def __lt__(self, _0: pandas._libs.tslibs.timedeltas.Timedelta, /):
        """
        usage.dask: 1
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

    @overload
    def __radd__(
        self,
        _0: Union[
            numpy.ndarray,
            numpy.int64,
            numpy.datetime64,
            numpy.timedelta64,
            numpy.float64,
        ],
        /,
    ):
        """
        usage.pandas: 8
        """
        ...

    @overload
    def __radd__(self, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        """
        usage.dask: 1
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

    @overload
    def __rsub__(
        self,
        _0: Union[
            numpy.ndarray,
            numpy.float64,
            numpy.timedelta64,
            numpy.int64,
            numpy.datetime64,
        ],
        /,
    ):
        """
        usage.pandas: 10
        """
        ...

    @overload
    def __rsub__(self, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        """
        usage.dask: 3
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
