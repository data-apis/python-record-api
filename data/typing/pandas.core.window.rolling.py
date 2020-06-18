from typing import *


class Rolling:
    window = ...
    win_type = ...
    min_periods = ...

    def mean(self, /):
        "usage.xarray: 4, usage.dask: 14"

    def sum(self, /):
        "usage.dask: 9"

    def count(self, /):
        "usage.dask: 9"

    def median(self, /):
        "usage.dask: 5"

    def min(self, /):
        "usage.dask: 5"

    def max(self, /):
        "usage.dask: 5"

    def std(self=..., /):
        "usage.dask: 6"

    def var(self=..., /):
        "usage.dask: 5"

    def skew(self, /):
        "usage.dask: 5"

    def kurt(self, /):
        "usage.dask: 5"

    def quantile(self, /, quantile: float):
        "usage.dask: 5"

    def apply(
        self,
        /,
        func: Callable,
        raw: bool,
        engine: Literal[("numba", "cython")] = ...,
        engine_kwargs: None = ...,
        args: Tuple[(None, ...)] = ...,
        kwargs: dict = ...,
    ):
        "usage.dask: 9"

    def cov(self, /):
        "usage.dask: 5"

    def aggregate(
        self,
        /,
        func: Union[
            (
                Dict[(Literal[("B", "A")], Union[(Callable, List[Callable])])],
                List[Callable],
            )
        ],
    ):
        "usage.dask: 8"
