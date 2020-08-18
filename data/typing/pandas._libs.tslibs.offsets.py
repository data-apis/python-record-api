from typing import *


@overload
def to_offset(_0: Literal["S"], /):
    """
    usage.dask: 1
    """
    ...


@overload
def to_offset(_0: Literal["W"], /):
    """
    usage.dask: 1
    """
    ...


@overload
def to_offset(_0: Literal["B"], /):
    """
    usage.dask: 1
    """
    ...


@overload
def to_offset(_0: Literal["D"], /):
    """
    usage.dask: 2
    """
    ...


@overload
def to_offset(_0: Literal["H"], /):
    """
    usage.dask: 1
    """
    ...


@overload
def to_offset(_0: Literal["0d"], /):
    """
    usage.dask: 2
    """
    ...


@overload
def to_offset(_0: Literal["100h"], /):
    """
    usage.dask: 1
    """
    ...


@overload
def to_offset(_0: Literal["20d"], /):
    """
    usage.dask: 1
    """
    ...


@overload
def to_offset(_0: Literal["20B"], /):
    """
    usage.dask: 1
    """
    ...


@overload
def to_offset(_0: Literal["3W"], /):
    """
    usage.dask: 1
    """
    ...


@overload
def to_offset(_0: Literal["3M"], /):
    """
    usage.dask: 1
    """
    ...


@overload
def to_offset(_0: Literal["400d"], /):
    """
    usage.dask: 1
    """
    ...


@overload
def to_offset(_0: Literal["13M"], /):
    """
    usage.dask: 1
    """
    ...


@overload
def to_offset(_0: Literal["30T"], /):
    """
    usage.dask: 1
    """
    ...


@overload
def to_offset(_0: pandas._libs.tslibs.offsets.Minute, /):
    """
    usage.dask: 1
    """
    ...


@overload
def to_offset(_0: Literal["h"], /):
    """
    usage.dask: 1
    """
    ...


@overload
def to_offset(_0: pandas._libs.tslibs.offsets.Hour, /):
    """
    usage.dask: 1
    """
    ...


@overload
def to_offset(_0: Literal["d"], /):
    """
    usage.dask: 1
    """
    ...


@overload
def to_offset(_0: pandas._libs.tslibs.offsets.Day, /):
    """
    usage.dask: 1
    """
    ...


@overload
def to_offset(_0: Literal["w"], /):
    """
    usage.dask: 1
    """
    ...


@overload
def to_offset(_0: pandas._libs.tslibs.offsets.Week, /):
    """
    usage.dask: 1
    """
    ...


@overload
def to_offset(_0: Literal["M"], /):
    """
    usage.dask: 1
    """
    ...


@overload
def to_offset(_0: pandas._libs.tslibs.offsets.MonthEnd, /):
    """
    usage.dask: 1
    """
    ...


@overload
def to_offset(_0: Literal["30min"], /):
    """
    usage.dask: 1
    """
    ...


@overload
def to_offset(_0: Literal["10min"], /):
    """
    usage.dask: 1
    """
    ...


@overload
def to_offset(_0: Literal["2h"], /):
    """
    usage.dask: 1
    """
    ...


@overload
def to_offset(_0: Literal["2M"], /):
    """
    usage.dask: 1
    """
    ...


@overload
def to_offset(_0: Literal["1Q"], /):
    """
    usage.dask: 1
    """
    ...


@overload
def to_offset(_0: pandas._libs.tslibs.offsets.QuarterEnd, /):
    """
    usage.dask: 1
    """
    ...


@overload
def to_offset(_0: Literal["2D"], /):
    """
    usage.dask: 1
    """
    ...


@overload
def to_offset(_0: Literal["57T"], /):
    """
    usage.dask: 1
    """
    ...


@overload
def to_offset(_0: Literal["1D"], /):
    """
    usage.dask: 1
    """
    ...


@overload
def to_offset(_0: Literal["1d"], /):
    """
    usage.dask: 1
    """
    ...


def to_offset(_0: object, /):
    """
    usage.dask: 35
    """
    ...


class BusinessDay:

    # usage.dask: 1
    __module__: ClassVar[object]

    def __rsub__(self, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        """
        usage.dask: 1
        """
        ...

    def is_anchored(self, /):
        """
        usage.dask: 1
        """
        ...


class DateOffset:
    pass


class Day:

    # usage.dask: 1
    __module__: ClassVar[object]

    def __eq__(self, _0: pandas._libs.tslibs.offsets.Day, /):
        """
        usage.dask: 8
        """
        ...

    @overload
    def __radd__(self, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __radd__(self, _0: pandas.core.indexes.datetimes.DatetimeIndex, /):
        """
        usage.dask: 2
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


class Hour:

    # usage.dask: 1
    __module__: ClassVar[object]

    def __radd__(self, _0: pandas.core.indexes.datetimes.DatetimeIndex, /):
        """
        usage.dask: 1
        usage.xarray: 1
        """
        ...

    def __rsub__(self, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        """
        usage.dask: 1
        """
        ...

    def is_anchored(self, /):
        """
        usage.dask: 1
        """
        ...


class Minute:

    # usage.dask: 1
    __module__: ClassVar[object]

    def __radd__(self, _0: pandas.core.indexes.datetimes.DatetimeIndex, /):
        """
        usage.dask: 1
        """
        ...

    def is_anchored(self, /):
        """
        usage.dask: 1
        """
        ...


class MonthEnd:

    # usage.dask: 1
    __module__: ClassVar[object]

    def __radd__(self, _0: pandas.core.indexes.datetimes.DatetimeIndex, /):
        """
        usage.dask: 1
        """
        ...

    def __rsub__(self, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        """
        usage.dask: 1
        """
        ...


class Nano:
    @overload
    def __radd__(self, _0: pandas.core.indexes.datetimes.DatetimeIndex, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __radd__(self, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        """
        usage.dask: 1
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


class QuarterEnd:

    # usage.dask: 1
    __module__: ClassVar[object]

    def __radd__(self, _0: pandas.core.indexes.datetimes.DatetimeIndex, /):
        """
        usage.dask: 1
        """
        ...


class Second:

    # usage.dask: 1
    __module__: ClassVar[object]

    def is_anchored(self, /):
        """
        usage.dask: 1
        """
        ...


class Week:

    # usage.dask: 1
    __module__: ClassVar[object]

    def __radd__(self, _0: pandas.core.indexes.datetimes.DatetimeIndex, /):
        """
        usage.dask: 1
        """
        ...

    def __rsub__(self, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        """
        usage.dask: 1
        """
        ...

    def is_anchored(self, /):
        """
        usage.dask: 1
        """
        ...
