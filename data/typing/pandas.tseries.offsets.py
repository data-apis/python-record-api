from typing import *


class Hour:

    # usage.dask: 1
    __module__: ClassVar[object]

    # usage.dask: 1
    nanos: object

    def __radd__(
        self: object,
        _0: Union[
            pandas._libs.tslibs.timestamps.Timestamp,
            pandas.core.indexes.datetimes.DatetimeIndex,
        ],
        /,
    ):
        "\n    usage.xarray: 1\n    usage.dask: 2\n    "
        ...

    def __rsub__(self: object, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        "\n    usage.dask: 1\n    "
        ...


class Day:

    # usage.dask: 1
    __module__: ClassVar[object]

    # usage.dask: 2
    nanos: object

    def __eq__(self: object, _0: pandas.tseries.offsets.Day, /):
        "\n    usage.dask: 8\n    "
        ...

    def __radd__(
        self: object,
        _0: Union[
            pandas.core.indexes.datetimes.DatetimeIndex,
            pandas._libs.tslibs.timestamps.Timestamp,
        ],
        /,
    ):
        "\n    usage.dask: 3\n    "
        ...

    def __rsub__(self: object, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        "\n    usage.dask: 1\n    "
        ...


class Tick:
    def is_anchored(self: object, /):
        "\n    usage.dask: 6\n    "
        ...


class Week:

    # usage.dask: 1
    __module__: ClassVar[object]

    def is_anchored(self: object, /):
        "\n    usage.dask: 2\n    "
        ...

    def __radd__(
        self: object,
        _0: Union[
            pandas.core.indexes.datetimes.DatetimeIndex,
            pandas._libs.tslibs.timestamps.Timestamp,
        ],
        /,
    ):
        "\n    usage.dask: 2\n    "
        ...

    def __rsub__(self: object, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        "\n    usage.dask: 1\n    "
        ...


class DateOffset:
    def is_anchored(self: object, /):
        "\n    usage.dask: 3\n    "
        ...


class BusinessDay:

    # usage.dask: 1
    __module__: ClassVar[object]

    def __radd__(self: object, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        "\n    usage.dask: 1\n    "
        ...

    def __rsub__(self: object, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        "\n    usage.dask: 1\n    "
        ...


class MonthEnd:

    # usage.dask: 1
    __module__: ClassVar[object]

    def __radd__(
        self: object,
        _0: Union[
            pandas.core.indexes.datetimes.DatetimeIndex,
            pandas._libs.tslibs.timestamps.Timestamp,
        ],
        /,
    ):
        "\n    usage.dask: 2\n    "
        ...

    def __rsub__(self: object, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        "\n    usage.dask: 1\n    "
        ...


class Second:

    # usage.dask: 1
    __module__: ClassVar[object]


class Minute:

    # usage.dask: 1
    __module__: ClassVar[object]

    # usage.dask: 1
    nanos: object

    def __radd__(self: object, _0: pandas.core.indexes.datetimes.DatetimeIndex, /):
        "\n    usage.dask: 1\n    "
        ...

    def __rmod__(
        self: object,
        _0: Literal["Resampling frequency %s that does not evenly divid"],
        /,
    ):
        "\n    usage.dask: 1\n    "
        ...


class Nano:
    def __radd__(self: object, _0: pandas.core.indexes.datetimes.DatetimeIndex, /):
        "\n    usage.dask: 1\n    "
        ...
