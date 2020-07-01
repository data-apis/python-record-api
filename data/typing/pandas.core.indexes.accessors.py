from typing import *


class DatetimeProperties:

    # usage.xarray: 1
    month: object

    # usage.dask: 1
    date: object

    def floor(self: object, /):
        "\n    usage.xarray: 1\n    "
        ...

    def ceil(self: object, /):
        "\n    usage.xarray: 1\n    "
        ...

    def round(self: object, /):
        "\n    usage.xarray: 1\n    "
        ...

    def to_pydatetime(self: object, /):
        "\n    usage.dask: 2\n    "
        ...


class TimedeltaProperties:
    def floor(self: object, /):
        "\n    usage.xarray: 1\n    "
        ...

    def ceil(self: object, /):
        "\n    usage.xarray: 1\n    "
        ...

    def round(self: object, /):
        "\n    usage.xarray: 1\n    "
        ...
