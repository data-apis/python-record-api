from typing import *


class Period:
    def __eq__(
        self: object,
        _0: Union[
            pandas._libs.tslibs.period.Period,
            xarray.core.variable.Variable,
            numpy.ndarray,
        ],
        /,
    ):
        "\n    usage.xarray: 2\n    usage.dask: 2\n    "
        ...

    def __ge__(self: object, _0: pandas._libs.tslibs.period.Period, /):
        "\n    usage.dask: 3\n    "
        ...

    def __le__(self: object, _0: pandas._libs.tslibs.period.Period, /):
        "\n    usage.dask: 3\n    "
        ...
