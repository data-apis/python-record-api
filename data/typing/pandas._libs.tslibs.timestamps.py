from typing import *


class _Timestamp:
    @classmethod
    def to_datetime64(_0: pandas._libs.tslibs.timestamps.Timestamp, /):
        "usage.xarray: 1"

    @classmethod
    def to_pydatetime(_0: pandas._libs.tslibs.timestamps.Timestamp, /):
        "usage.xarray: 1"


class Timestamp:
    def __init__(
        ts_input: Union[
            (
                str,
                pandas._libs.tslibs.timestamps.Timestamp,
                pandas._libs.tslibs.nattype.NaTType,
            )
        ] = ...
    ):
        "usage.xarray: 25, usage.dask: 8"

    __module__ = ...
    __name__ = ...
    tz = ...
    value = ...
    dtype = ...
    freq = ...
    tzinfo = ...

    def __rsub__(self, _0: pandas.core.indexes.datetimes.DatetimeIndex, /):
        ""

    def __radd__(
        self,
        _0: Union[
            (
                pandas._libs.tslibs.nattype.NaTType,
                pandas._libs.tslibs.timedeltas.Timedelta,
                pandas.core.indexes.timedeltas.TimedeltaIndex,
            )
        ],
        /,
    ):
        ""

    def __ge__(
        self,
        _0: Union[
            (
                pandas.core.indexes.datetimes.DatetimeIndex,
                pandas._libs.tslibs.timestamps.Timestamp,
                numpy.datetime64,
            )
        ],
        /,
    ):
        ""

    def __le__(
        self,
        _0: Union[
            (pandas._libs.tslibs.timestamps.Timestamp, pandas.core.series.Series)
        ],
        /,
    ):
        ""

    def __eq__(
        self,
        _0: Union[(pandas._libs.tslibs.timestamps.Timestamp, Literal[("2000",)])],
        /,
    ):
        ""

    def tz_localize(self, /, tz: None):
        "usage.dask: 3"

    def __ne__(self, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        ""

    def __gt__(self, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        ""

    def __lt__(
        self,
        _0: Union[
            (
                pandas.core.indexes.datetimes.DatetimeIndex,
                pandas._libs.tslibs.timestamps.Timestamp,
            )
        ],
        /,
    ):
        ""

    def ceil(self, /, freq: str):
        "usage.dask: 6"

    def round(self, /, freq: Literal[("15s",)]):
        "usage.dask: 1"

    def __add__(self, _0, /):
        ""

    def __sub__(self, _0, /):
        ""
