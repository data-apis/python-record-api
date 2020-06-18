from typing import *


class TimeGrouper:
    loffset: None = ...
    closed = ...
    label = ...


class DatetimeIndexResampler:
    agg = ...

    def g(self, /):
        "usage.xarray: 4, usage.dask: 5"

    def pad(self, /):
        "usage.xarray: 2"

    def backfill(self, /):
        "usage.xarray: 1"

    def asfreq(self, /):
        "usage.xarray: 7"

    def count(self, /):
        "usage.dask: 5"

    def aggregate(
        self,
        /,
        func: Union[(Callable, Literal[("mean",)], List[Literal[("min", "mean")]])],
    ):
        "usage.dask: 9"

    def h(self, /):
        "usage.dask: 3"

    def size(self, /):
        "usage.dask: 3"

    def quantile(self, /):
        "usage.dask: 3"


class Resampler:
    __module__ = ...
    __name__ = ...
