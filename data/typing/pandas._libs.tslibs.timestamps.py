from typing import *


class Timestamp:

    # usage.dask: 1
    __module__: ClassVar[object]

    # usage.dask: 1
    __name__: ClassVar[object]

    # usage.dask: 1
    dtype: object

    # usage.dask: 1
    freq: object

    # usage.dask: 5
    # usage.xarray: 1
    tz: object

    # usage.dask: 1
    tzinfo: object

    # usage.dask: 1
    # usage.xarray: 1
    value: object

    @overload
    def __add__(self, _0: pandas.core.indexes.timedeltas.TimedeltaIndex, /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def __add__(self, _0: Union[numpy.ndarray, numpy.timedelta64, numpy.int64], /):
        """
        usage.pandas: 23
        """
        ...

    @overload
    def __add__(self, _0: object, /):
        """
        usage.dask: 8
        """
        ...

    def __add__(self, _0: object, /):
        """
        usage.dask: 8
        usage.pandas: 23
        usage.xarray: 1
        """
        ...

    @overload
    def __eq__(
        self, _0: Union[numpy.datetime64, numpy.float64, numpy.ndarray, numpy.int64], /
    ):
        """
        usage.pandas: 8
        """
        ...

    @overload
    def __eq__(
        self, _0: Union[pandas._libs.tslibs.timestamps.Timestamp, Literal["2000"]], /
    ):
        """
        usage.dask: 43
        """
        ...

    def __eq__(self, _0: object, /):
        """
        usage.dask: 43
        usage.pandas: 8
        """
        ...

    def __floordiv__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    @overload
    def __ge__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 2
        """
        ...

    @overload
    def __ge__(
        self,
        _0: Union[
            pandas.core.indexes.datetimes.DatetimeIndex,
            pandas._libs.tslibs.timestamps.Timestamp,
            numpy.datetime64,
        ],
        /,
    ):
        """
        usage.dask: 21
        """
        ...

    def __ge__(
        self,
        _0: Union[
            numpy.datetime64,
            pandas._libs.tslibs.timestamps.Timestamp,
            pandas.core.indexes.datetimes.DatetimeIndex,
            numpy.ndarray,
        ],
        /,
    ):
        """
        usage.dask: 21
        usage.pandas: 2
        """
        ...

    def __gt__(self, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        """
        usage.dask: 8
        """
        ...

    def __le__(
        self,
        _0: Union[pandas._libs.tslibs.timestamps.Timestamp, pandas.core.series.Series],
        /,
    ):
        """
        usage.dask: 20
        """
        ...

    @overload
    def __lt__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    @overload
    def __lt__(
        self,
        _0: Union[
            pandas.core.indexes.datetimes.DatetimeIndex,
            pandas._libs.tslibs.timestamps.Timestamp,
        ],
        /,
    ):
        """
        usage.dask: 9
        """
        ...

    def __lt__(
        self,
        _0: Union[
            pandas._libs.tslibs.timestamps.Timestamp,
            pandas.core.indexes.datetimes.DatetimeIndex,
            numpy.ndarray,
        ],
        /,
    ):
        """
        usage.dask: 9
        usage.pandas: 1
        """
        ...

    def __mod__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    def __mul__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    @overload
    def __ne__(
        self, _0: Union[numpy.int64, numpy.ndarray, numpy.datetime64, numpy.float64], /
    ):
        """
        usage.pandas: 4
        """
        ...

    @overload
    def __ne__(self, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        """
        usage.dask: 10
        """
        ...

    def __ne__(
        self,
        _0: Union[
            pandas._libs.tslibs.timestamps.Timestamp,
            numpy.float64,
            numpy.datetime64,
            numpy.ndarray,
            numpy.int64,
        ],
        /,
    ):
        """
        usage.dask: 10
        usage.pandas: 4
        """
        ...

    def __pow__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    @overload
    def __radd__(
        self,
        _0: Union[
            pandas._libs.tslibs.nattype.NaTType,
            pandas._libs.tslibs.timedeltas.Timedelta,
            pandas.core.indexes.timedeltas.TimedeltaIndex,
        ],
        /,
    ):
        """
        usage.xarray: 5
        """
        ...

    @overload
    def __radd__(self, _0: Union[numpy.ndarray, numpy.int64, numpy.timedelta64], /):
        """
        usage.pandas: 7
        """
        ...

    def __radd__(self, _0: object, /):
        """
        usage.pandas: 7
        usage.xarray: 5
        """
        ...

    @overload
    def __rsub__(self, _0: pandas.core.indexes.datetimes.DatetimeIndex, /):
        """
        usage.xarray: 3
        """
        ...

    @overload
    def __rsub__(self, _0: Union[numpy.ndarray, numpy.int64, numpy.datetime64], /):
        """
        usage.pandas: 8
        """
        ...

    def __rsub__(
        self,
        _0: Union[
            numpy.datetime64,
            numpy.int64,
            numpy.ndarray,
            pandas.core.indexes.datetimes.DatetimeIndex,
        ],
        /,
    ):
        """
        usage.pandas: 8
        usage.xarray: 3
        """
        ...

    @overload
    def __sub__(self, _0: Union[numpy.ndarray, numpy.timedelta64, numpy.int64], /):
        """
        usage.pandas: 14
        """
        ...

    @overload
    def __sub__(self, _0: object, /):
        """
        usage.dask: 8
        """
        ...

    def __sub__(self, _0: object, /):
        """
        usage.dask: 8
        usage.pandas: 14
        """
        ...

    def __truediv__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    def ceil(self, /, freq: Literal["1M", "15s"]):
        """
        usage.dask: 2
        """
        ...

    def round(self, /, freq: Literal["15s"]):
        """
        usage.dask: 1
        """
        ...

    def to_datetime64(self, /):
        """
        usage.xarray: 1
        """
        ...

    def to_pydatetime(self, /):
        """
        usage.xarray: 1
        """
        ...

    def tz_convert(self, /, tz: None):
        """
        usage.xarray: 1
        """
        ...

    def tz_localize(self, /, tz: None):
        """
        usage.dask: 3
        """
        ...
