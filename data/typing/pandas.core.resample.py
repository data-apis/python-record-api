from typing import *


class DatetimeIndexResampler:

    # usage.dask: 1
    agg: object

    def aggregate(
        self, /, func: Union[Callable, Literal["mean"], List[Literal["min", "mean"]]]
    ):
        """
        usage.dask: 9
        """
        ...

    def asfreq(self, /):
        """
        usage.xarray: 7
        """
        ...

    def backfill(self, /):
        """
        usage.xarray: 1
        """
        ...

    def count(self, /):
        """
        usage.dask: 5
        """
        ...

    def g(self, /):
        """
        usage.xarray: 4
        usage.dask: 5
        """
        ...

    def h(self, /):
        """
        usage.dask: 3
        """
        ...

    def pad(self, /):
        """
        usage.xarray: 2
        """
        ...

    def quantile(self, /):
        """
        usage.dask: 3
        """
        ...

    def size(self, /):
        """
        usage.dask: 3
        """
        ...


class Resampler:

    # usage.dask: 1
    __module__: ClassVar[object]

    # usage.dask: 1
    __name__: ClassVar[object]


class TimeGrouper:

    # usage.dask: 1
    closed: object

    # usage.dask: 1
    label: object

    # usage.xarray: 3
    loffset: None
