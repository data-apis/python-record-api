from typing import *


class Timedelta:
    def __init__(
        value: Union[str, pandas._libs.tslibs.timedeltas.Timedelta, numpy.timedelta64]
    ):
        "\n    usage.xarray: 10\n    usage.dask: 2\n    "
        ...

    # usage.dask: 1
    __module__: ClassVar[object]

    def __add__(self: object, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        "\n    usage.xarray: 2\n    "
        ...

    def __eq__(self: object, _0: pandas._libs.tslibs.timedeltas.Timedelta, /):
        "\n    usage.dask: 6\n    "
        ...

    def __ge__(self: object, _0: pandas._libs.tslibs.timedeltas.Timedelta, /):
        "\n    usage.dask: 3\n    "
        ...

    def __le__(self: object, _0: pandas._libs.tslibs.timedeltas.Timedelta, /):
        "\n    usage.dask: 3\n    "
        ...

    def __gt__(self: object, _0: pandas.core.series.Series, /):
        "\n    usage.dask: 2\n    "
        ...

    def __rsub__(self: object, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        "\n    usage.dask: 3\n    "
        ...

    def __radd__(self: object, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        "\n    usage.dask: 1\n    "
        ...


class _Timedelta:
    @classmethod
    def to_numpy(_0: pandas._libs.tslibs.timedeltas.Timedelta, /):
        "\n    usage.xarray: 1\n    "
        ...

    @classmethod
    def to_timedelta64(_0: pandas._libs.tslibs.timedeltas.Timedelta, /):
        "\n    usage.xarray: 1\n    "
        ...
