from typing import *


class NaTType:
    def __add__(self: object, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        "\n    usage.xarray: 2\n    "
        ...

    def __ge__(self: object, _0: pandas._libs.tslibs.nattype.NaTType, /):
        "\n    usage.dask: 2\n    "
        ...

    def __le__(
        self: object,
        _0: Union[pandas.core.series.Series, pandas._libs.tslibs.nattype.NaTType],
        /,
    ):
        "\n    usage.dask: 3\n    "
        ...

    def __gt__(self: object, _0: pandas._libs.tslibs.nattype.NaTType, /):
        "\n    usage.dask: 1\n    "
        ...

    def __lt__(self: object, _0: pandas._libs.tslibs.nattype.NaTType, /):
        "\n    usage.dask: 1\n    "
        ...
