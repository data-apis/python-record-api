from typing import *


class TimeGrouper:

    # usage.xarray: 3
    loffset: None

    # usage.dask: 1
    closed: object

    # usage.dask: 1
    label: object


class DatetimeIndexResampler:

    # usage.dask: 1
    agg: object

    def g(self: object, /):
        "\n    usage.xarray: 4\n    usage.dask: 5\n    "
        ...

    def pad(self: object, /):
        "\n    usage.xarray: 2\n    "
        ...

    def backfill(self: object, /):
        "\n    usage.xarray: 1\n    "
        ...

    def asfreq(self: object, /):
        "\n    usage.xarray: 7\n    "
        ...

    def count(self: object, /):
        "\n    usage.dask: 5\n    "
        ...

    def aggregate(
        self: object,
        /,
        func: Union[Callable, Literal["mean"], List[Literal[("min", "mean")]]],
    ):
        "\n    usage.dask: 9\n    "
        ...

    def h(self: object, /):
        "\n    usage.dask: 3\n    "
        ...

    def size(self: object, /):
        "\n    usage.dask: 3\n    "
        ...

    def quantile(self: object, /):
        "\n    usage.dask: 3\n    "
        ...


class Resampler:

    # usage.dask: 1
    __module__: ClassVar[object]

    # usage.dask: 1
    __name__: ClassVar[object]
