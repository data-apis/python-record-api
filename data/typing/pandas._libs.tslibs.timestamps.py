from typing import *


class _Timestamp:
    @classmethod
    def to_datetime64(_0: pandas._libs.tslibs.timestamps.Timestamp, /):
        """
        usage.xarray: 1
        """
        ...

    @classmethod
    def to_pydatetime(_0: pandas._libs.tslibs.timestamps.Timestamp, /):
        """
        usage.xarray: 1
        """
        ...


class Timestamp:
    def __init__(
        ts_input: Union[
            str,
            pandas._libs.tslibs.timestamps.Timestamp,
            pandas._libs.tslibs.nattype.NaTType,
        ]
    ):
        """
        usage.xarray: 25
        usage.dask: 8
        """
        ...

    # usage.dask: 1
    __module__: ClassVar[object]

    # usage.dask: 1
    __name__: ClassVar[object]

    # usage.xarray: 1
    # usage.dask: 5
    tz: object

    # usage.xarray: 1
    # usage.dask: 1
    value: object

    # usage.dask: 1
    dtype: object

    # usage.dask: 1
    freq: object

    # usage.dask: 1
    tzinfo: object

    def __rsub__(self: object, _0: pandas.core.indexes.datetimes.DatetimeIndex, /):
        """
        usage.xarray: 2
        """
        ...

    def __radd__(
        self: object,
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

    def __ge__(
        self: object,
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

    def __le__(
        self: object,
        _0: Union[pandas._libs.tslibs.timestamps.Timestamp, pandas.core.series.Series],
        /,
    ):
        """
        usage.dask: 19
        """
        ...

    def __eq__(
        self: object,
        _0: Union[pandas._libs.tslibs.timestamps.Timestamp, Literal["2000"]],
        /,
    ):
        """
        usage.dask: 45
        """
        ...

    def tz_localize(self: object, /, tz: None):
        """
        usage.dask: 3
        """
        ...

    def __ne__(self: object, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        """
        usage.dask: 10
        """
        ...

    def __gt__(self: object, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        """
        usage.dask: 6
        """
        ...

    def __lt__(
        self: object,
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

    def ceil(self: object, /, freq: str):
        """
        usage.dask: 6
        """
        ...

    def round(self: object, /, freq: Literal["15s"]):
        """
        usage.dask: 1
        """
        ...

    def __add__(self: object, _0: object, /):
        """
        usage.dask: 6
        """
        ...

    def __sub__(self: object, _0: object, /):
        """
        usage.dask: 8
        """
        ...
