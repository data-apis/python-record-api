from typing import *


class Hour:
    __module__ = ...
    nanos = ...

    def __radd__(
        self,
        _0: Union[
            (
                pandas._libs.tslibs.timestamps.Timestamp,
                pandas.core.indexes.datetimes.DatetimeIndex,
            )
        ],
        /,
    ):
        ""

    def __rsub__(self, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        ""


class Day:
    __module__ = ...
    nanos = ...

    def __eq__(self, _0: pandas.tseries.offsets.Day, /):
        ""

    def __radd__(
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

    def __rsub__(self, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        ""


class Tick:
    def is_anchored(self, /):
        "usage.dask: 6"


class Week:
    __module__ = ...

    def is_anchored(self, /):
        "usage.dask: 2"

    def __radd__(
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

    def __rsub__(self, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        ""


class DateOffset:
    def is_anchored(self, /):
        "usage.dask: 3"


class BusinessDay:
    __module__ = ...

    def __radd__(self, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        ""

    def __rsub__(self, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        ""


class MonthEnd:
    __module__ = ...

    def __radd__(
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

    def __rsub__(self, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        ""


class Second:
    __module__ = ...


class Minute:
    __module__ = ...
    nanos = ...

    def __radd__(self, _0: pandas.core.indexes.datetimes.DatetimeIndex, /):
        ""

    def __rmod__(
        self, _0: Literal[("Resampling frequency %s that does not evenly divid",)], /
    ):
        ""


class Nano:
    def __radd__(self, _0: pandas.core.indexes.datetimes.DatetimeIndex, /):
        ""
