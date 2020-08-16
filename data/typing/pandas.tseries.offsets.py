from typing import *


class BQuarterBegin:
    def __mul__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    def __rmul__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...


class BQuarterEnd:
    def __mul__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    def __rmul__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...


class BYearBegin:
    def __mul__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    def __rmul__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...


class BYearEnd:
    def __mul__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    def __rmul__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...


class BusinessDay:

    # usage.dask: 1
    __module__: ClassVar[object]

    def __mul__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    def __radd__(self, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        """
        usage.dask: 1
        """
        ...

    def __rmul__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    def __rsub__(self, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        """
        usage.dask: 1
        """
        ...


class BusinessHour:
    def __mul__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    def __radd__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    def __rmul__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...


class BusinessMonthBegin:
    def __mul__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    def __rmul__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...


class BusinessMonthEnd:
    def __mul__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    def __rmul__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...


class CustomBusinessDay:
    def __mul__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    def __radd__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    def __rmul__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...


class CustomBusinessHour:
    def __mul__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    def __radd__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    def __rmul__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...


class CustomBusinessMonthBegin:
    def __mul__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    def __radd__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    def __rmul__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...


class CustomBusinessMonthEnd:
    def __mul__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    def __radd__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    def __rmul__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...


class DateOffset:
    def __mul__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    def __radd__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    def __rmul__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    def is_anchored(self, /):
        """
        usage.dask: 3
        """
        ...


class Day:
    def __init__(self, /):
        """
        usage.dask: 1
        """
        ...

    # usage.dask: 1
    __module__: ClassVar[object]

    def __eq__(self, _0: Union[None, pandas.tseries.offsets.Day], /):
        """
        usage.dask: 9
        """
        ...

    def __mul__(self, _0: Union[numpy.ndarray, numpy.int64], /):
        """
        usage.pandas: 3
        """
        ...

    def __radd__(
        self,
        _0: Union[
            pandas.core.indexes.datetimes.DatetimeIndex,
            pandas._libs.tslibs.timestamps.Timestamp,
        ],
        /,
    ):
        """
        usage.dask: 4
        """
        ...

    def __rmul__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    def __rsub__(self, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        """
        usage.dask: 1
        """
        ...

    def __truediv__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 3
        """
        ...


class Easter:
    def __mul__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    def __radd__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    def __rmul__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...


class FY5253:
    def __mul__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    def __radd__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    def __rmul__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...


class FY5253Quarter:
    def __mul__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    def __radd__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    def __rmul__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...


class Hour:

    # usage.dask: 1
    __module__: ClassVar[object]

    def __mul__(self, _0: Union[numpy.ndarray, numpy.int64], /):
        """
        usage.pandas: 2
        """
        ...

    def __radd__(
        self,
        _0: Union[
            pandas.core.indexes.datetimes.DatetimeIndex,
            pandas._libs.tslibs.timestamps.Timestamp,
        ],
        /,
    ):
        """
        usage.dask: 2
        """
        ...

    def __rmul__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 2
        """
        ...

    def __rsub__(self, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        """
        usage.dask: 1
        """
        ...

    def __rtruediv__(self, _0: Union[numpy.ndarray, numpy.timedelta64], /):
        """
        usage.pandas: 2
        """
        ...

    def __truediv__(self, _0: Union[numpy.timedelta64, numpy.ndarray], /):
        """
        usage.pandas: 4
        """
        ...


class LastWeekOfMonth:
    def __mul__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    def __radd__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    def __rmul__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...


class Micro:
    def __mul__(self, _0: Union[numpy.ndarray, numpy.int64], /):
        """
        usage.pandas: 2
        """
        ...

    def __rmul__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    def __rtruediv__(self, _0: Union[numpy.ndarray, numpy.timedelta64], /):
        """
        usage.pandas: 2
        """
        ...

    def __truediv__(self, _0: numpy.timedelta64, /):
        """
        usage.pandas: 1
        """
        ...


class Milli:
    def __mul__(self, _0: Union[numpy.ndarray, numpy.int64], /):
        """
        usage.pandas: 2
        """
        ...

    def __rmul__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    def __rtruediv__(self, _0: Union[numpy.ndarray, numpy.timedelta64], /):
        """
        usage.pandas: 2
        """
        ...

    def __truediv__(self, _0: numpy.timedelta64, /):
        """
        usage.pandas: 1
        """
        ...


class Minute:

    # usage.dask: 1
    __module__: ClassVar[object]

    def __add__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 3
        """
        ...

    def __mul__(self, _0: Union[numpy.ndarray, numpy.int64], /):
        """
        usage.pandas: 2
        """
        ...

    def __radd__(self, _0: pandas.core.indexes.datetimes.DatetimeIndex, /):
        """
        usage.dask: 1
        """
        ...

    def __rmul__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 2
        """
        ...

    def __rtruediv__(self, _0: Union[numpy.ndarray, numpy.timedelta64], /):
        """
        usage.pandas: 2
        """
        ...

    def __sub__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 3
        """
        ...

    def __truediv__(self, _0: numpy.timedelta64, /):
        """
        usage.pandas: 1
        """
        ...


class MonthBegin:
    def __mul__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    def __rmul__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...


class MonthEnd:

    # usage.dask: 1
    __module__: ClassVar[object]

    def __mul__(self, _0: Union[numpy.ndarray, numpy.int64], /):
        """
        usage.pandas: 3
        """
        ...

    def __radd__(
        self,
        _0: Union[
            pandas.core.indexes.datetimes.DatetimeIndex,
            pandas._libs.tslibs.timestamps.Timestamp,
        ],
        /,
    ):
        """
        usage.dask: 2
        """
        ...

    def __rmul__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    def __rsub__(self, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        """
        usage.dask: 1
        """
        ...


class Nano:
    def __mul__(self, _0: Union[numpy.ndarray, numpy.int64], /):
        """
        usage.pandas: 2
        """
        ...

    def __radd__(
        self,
        _0: Union[
            pandas._libs.tslibs.timestamps.Timestamp,
            pandas.core.indexes.datetimes.DatetimeIndex,
        ],
        /,
    ):
        """
        usage.dask: 2
        """
        ...

    def __rmul__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    def __rtruediv__(self, _0: Union[numpy.ndarray, numpy.timedelta64], /):
        """
        usage.pandas: 2
        """
        ...

    def __truediv__(self, _0: numpy.timedelta64, /):
        """
        usage.pandas: 1
        """
        ...


class QuarterBegin:
    def __mul__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    def __rmul__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...


class QuarterEnd:

    # usage.dask: 1
    __module__: ClassVar[object]

    def __mul__(self, _0: Union[numpy.ndarray, numpy.int64], /):
        """
        usage.pandas: 2
        """
        ...

    def __radd__(self, _0: pandas.core.indexes.datetimes.DatetimeIndex, /):
        """
        usage.dask: 1
        """
        ...

    def __rmul__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...


class Second:

    # usage.dask: 1
    __module__: ClassVar[object]

    def __add__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 3
        """
        ...

    def __mul__(self, _0: Union[numpy.ndarray, numpy.int64], /):
        """
        usage.pandas: 2
        """
        ...

    def __rmul__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    def __rtruediv__(self, _0: Union[numpy.ndarray, numpy.timedelta64], /):
        """
        usage.pandas: 2
        """
        ...

    def __sub__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 3
        """
        ...

    def __truediv__(self, _0: numpy.timedelta64, /):
        """
        usage.pandas: 1
        """
        ...


class SemiMonthBegin:
    def __mul__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    def __rmul__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...


class SemiMonthEnd:
    def __mul__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    def __rmul__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...


class Tick:
    def is_anchored(self, /):
        """
        usage.dask: 6
        """
        ...


class Week:

    # usage.dask: 1
    __module__: ClassVar[object]

    def __mul__(self, _0: Union[numpy.ndarray, numpy.int64], /):
        """
        usage.pandas: 2
        """
        ...

    def __radd__(
        self,
        _0: Union[
            pandas.core.indexes.datetimes.DatetimeIndex,
            pandas._libs.tslibs.timestamps.Timestamp,
        ],
        /,
    ):
        """
        usage.dask: 2
        """
        ...

    def __rmul__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    def __rsub__(self, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        """
        usage.dask: 1
        """
        ...

    def is_anchored(self, /):
        """
        usage.dask: 2
        """
        ...


class WeekOfMonth:
    def __mul__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    def __radd__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    def __rmul__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...


class YearBegin:
    def __mul__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    def __rmul__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...


class YearEnd:
    def __mul__(self, _0: Union[numpy.ndarray, numpy.int64], /):
        """
        usage.pandas: 2
        """
        ...

    def __rmul__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...
