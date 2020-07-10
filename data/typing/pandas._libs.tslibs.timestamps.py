from typing import *


class Timestamp:
    def __init__(
        self,
        /,
        ts_input: Union[
            str,
            pandas._libs.tslibs.timestamps.Timestamp,
            pandas._libs.tslibs.nattype.NaTType,
        ],
    ):
        """
        usage.xarray: 7
        usage.dask: 8
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

    # usage.xarray: 1
    # usage.dask: 5
    tz: object

    # usage.dask: 1
    tzinfo: object

    # usage.xarray: 1
    # usage.dask: 1
    value: object

    def __add__(self, _0: object, /):
        """
        usage.dask: 6
        """
        ...

    def __eq__(
        self, _0: Union[pandas._libs.tslibs.timestamps.Timestamp, Literal["2000"]], /
    ):
        """
        usage.dask: 45
        """
        ...

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
        usage.dask: 20
        """
        ...

    def __gt__(self, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        """
        usage.dask: 6
        """
        ...

    def __le__(
        self,
        _0: Union[pandas._libs.tslibs.timestamps.Timestamp, pandas.core.series.Series],
        /,
    ):
        """
        usage.dask: 19
        """
        ...

    def __lt__(
        self,
        _0: Union[
            pandas.core.indexes.datetimes.DatetimeIndex,
            pandas._libs.tslibs.timestamps.Timestamp,
        ],
        /,
    ):
        """
        usage.dask: 7
        """
        ...

    def __ne__(self, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        """
        usage.dask: 10
        """
        ...

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

    def __rsub__(self, _0: pandas.core.indexes.datetimes.DatetimeIndex, /):
        """
        usage.xarray: 2
        """
        ...

    def __sub__(self, _0: object, /):
        """
        usage.dask: 8
        """
        ...

    def ceil(self, /, freq: str):
        """
        usage.dask: 6
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

    def tz_localize(self, /, tz: None):
        """
        usage.dask: 3
        """
        ...
