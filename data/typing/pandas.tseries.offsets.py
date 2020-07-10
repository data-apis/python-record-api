from typing import *


class BusinessDay:

    # usage.dask: 1
    __module__: ClassVar[object]

    def __radd__(self, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        """
        usage.dask: 1
        """
        ...

    def __rsub__(self, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        """
        usage.dask: 1
        """
        ...


class DateOffset:
    def is_anchored(self, /):
        """
        usage.dask: 3
        """
        ...


class Day:

    # usage.dask: 1
    __module__: ClassVar[object]

    # usage.dask: 2
    nanos: object

    def __eq__(self, _0: pandas.tseries.offsets.Day, /):
        """
        usage.dask: 8
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
        usage.dask: 3
        """
        ...

    def __rsub__(self, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        """
        usage.dask: 1
        """
        ...


class Hour:

    # usage.dask: 1
    __module__: ClassVar[object]

    # usage.dask: 1
    nanos: object

    def __radd__(
        self,
        _0: Union[
            pandas._libs.tslibs.timestamps.Timestamp,
            pandas.core.indexes.datetimes.DatetimeIndex,
        ],
        /,
    ):
        """
        usage.xarray: 1
        usage.dask: 2
        """
        ...

    def __rsub__(self, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        """
        usage.dask: 1
        """
        ...


class Minute:

    # usage.dask: 1
    __module__: ClassVar[object]

    # usage.dask: 1
    nanos: object

    def __radd__(self, _0: pandas.core.indexes.datetimes.DatetimeIndex, /):
        """
        usage.dask: 1
        """
        ...

    def __rmod__(
        self, _0: Literal["Resampling frequency %s that does not evenly divid"], /
    ):
        """
        usage.dask: 1
        """
        ...


class MonthEnd:

    # usage.dask: 1
    __module__: ClassVar[object]

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

    def __rsub__(self, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        """
        usage.dask: 1
        """
        ...


class Nano:
    def __radd__(self, _0: pandas.core.indexes.datetimes.DatetimeIndex, /):
        """
        usage.dask: 1
        """
        ...


class Second:

    # usage.dask: 1
    __module__: ClassVar[object]


class Tick:
    def is_anchored(self, /):
        """
        usage.dask: 6
        """
        ...


class Week:

    # usage.dask: 1
    __module__: ClassVar[object]

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
