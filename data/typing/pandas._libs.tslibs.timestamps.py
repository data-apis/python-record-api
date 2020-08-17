from typing import *


class Timestamp:
    def __init__(self, /, ts_input: Literal["2000-01-03", "2000-01-01T00"]):
        """
        usage.xarray: 2
        """
        ...

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

    def __add__(self, _0: object, /):
        """
        usage.dask: 8
        usage.pandas: 23
        usage.xarray: 1
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

    def __ge__(
        self,
        _0: Union[
            numpy.ndarray,
            numpy.datetime64,
            pandas._libs.tslibs.timestamps.Timestamp,
            pandas.core.indexes.datetimes.DatetimeIndex,
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

    def __lt__(
        self,
        _0: Union[
            numpy.ndarray,
            pandas._libs.tslibs.timestamps.Timestamp,
            pandas.core.indexes.datetimes.DatetimeIndex,
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

    def __ne__(
        self,
        _0: Union[
            numpy.float64,
            numpy.datetime64,
            numpy.ndarray,
            numpy.int64,
            pandas._libs.tslibs.timestamps.Timestamp,
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

    def __radd__(self, _0: object, /):
        """
        usage.pandas: 7
        usage.xarray: 5
        """
        ...

    def __rsub__(
        self,
        _0: Union[
            pandas.core.indexes.datetimes.DatetimeIndex,
            numpy.datetime64,
            numpy.int64,
            numpy.ndarray,
        ],
        /,
    ):
        """
        usage.pandas: 8
        usage.xarray: 3
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
