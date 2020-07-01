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
        """
        usage.xarray: 4
        usage.dask: 5
        """
        ...

    def pad(self: object, /):
        """
        usage.xarray: 2
        """
        ...

    def backfill(self: object, /):
        """
        usage.xarray: 1
        """
        ...

    def asfreq(self: object, /):
        """
        usage.xarray: 7
        """
        ...

    def count(self: object, /):
        """
        usage.dask: 5
        """
        ...

    def aggregate(
        self: object,
        /,
        func: Union[Callable, Literal["mean"], List[Literal["min", "mean"]]],
    ):
        """
        usage.dask: 9
        """
        ...

    def h(self: object, /):
        """
        usage.dask: 3
        """
        ...

    def size(self: object, /):
        """
        usage.dask: 3
        """
        ...

    def quantile(self: object, /):
        """
        usage.dask: 3
        """
        ...


class Resampler:

    # usage.dask: 1
    __module__: ClassVar[object]

    # usage.dask: 1
    __name__: ClassVar[object]
