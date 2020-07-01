from typing import *


class _Timestamp:
    @classmethod
    def to_datetime64(_0: pandas._libs.tslibs.timestamps.Timestamp, /):
        "\n    usage.xarray: 1\n    "
        ...

    @classmethod
    def to_pydatetime(_0: pandas._libs.tslibs.timestamps.Timestamp, /):
        "\n    usage.xarray: 1\n    "
        ...


class Timestamp:
    def __init__(
        ts_input: Union[
            str,
            pandas._libs.tslibs.timestamps.Timestamp,
            pandas._libs.tslibs.nattype.NaTType,
        ]
    ):
        "\n    usage.xarray: 25\n    usage.dask: 8\n    "
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
        "\n    usage.xarray: 2\n    "
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
        "\n    usage.xarray: 5\n    "
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
        "\n    usage.dask: 20\n    "
        ...

    def __le__(
        self: object,
        _0: Union[pandas._libs.tslibs.timestamps.Timestamp, pandas.core.series.Series],
        /,
    ):
        "\n    usage.dask: 19\n    "
        ...

    def __eq__(
        self: object,
        _0: Union[pandas._libs.tslibs.timestamps.Timestamp, Literal["2000"]],
        /,
    ):
        "\n    usage.dask: 45\n    "
        ...

    def tz_localize(self: object, /, tz: None):
        "\n    usage.dask: 3\n    "
        ...

    def __ne__(self: object, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        "\n    usage.dask: 10\n    "
        ...

    def __gt__(self: object, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        "\n    usage.dask: 6\n    "
        ...

    def __lt__(
        self: object,
        _0: Union[
            pandas.core.indexes.datetimes.DatetimeIndex,
            pandas._libs.tslibs.timestamps.Timestamp,
        ],
        /,
    ):
        "\n    usage.dask: 7\n    "
        ...

    def ceil(self: object, /, freq: str):
        "\n    usage.dask: 6\n    "
        ...

    def round(self: object, /, freq: Literal["15s"]):
        "\n    usage.dask: 1\n    "
        ...

    def __add__(self: object, _0: object, /):
        "\n    usage.dask: 6\n    "
        ...

    def __sub__(self: object, _0: object, /):
        "\n    usage.dask: 8\n    "
        ...
