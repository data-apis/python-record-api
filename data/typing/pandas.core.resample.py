from typing import *


class DatetimeIndexResampler:

    # usage.dask: 1
    agg: object

    @overload
    def aggregate(self, /, func: Literal["mean"]):
        """
        usage.dask: 3
        """
        ...

    @overload
    def aggregate(self, /, func: List[Literal["min", "mean"]]):
        """
        usage.dask: 3
        """
        ...

    @overload
    def aggregate(self, /, func: Callable):
        """
        usage.dask: 3
        """
        ...

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
        usage.dask: 7
        """
        ...

    def f(self, /):
        """
        usage.dask: 3
        """
        ...

    def g(self, /):
        """
        usage.dask: 6
        usage.xarray: 4
        """
        ...

    def h(self, /):
        """
        usage.dask: 4
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
        usage.dask: 5
        """
        ...


class TimeGrouper:

    # usage.dask: 1
    closed: object

    # usage.dask: 1
    label: object

    # usage.xarray: 3
    loffset: None
