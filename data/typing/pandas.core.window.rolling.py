from typing import *


class Rolling:

    # usage.dask: 1
    min_periods: object

    # usage.dask: 1
    win_type: object

    # usage.dask: 1
    window: object

    def aggregate(
        self,
        /,
        func: Union[
            Dict[Literal["B", "A"], Union[Callable, List[Callable]]], List[Callable]
        ],
    ):
        """
        usage.dask: 8
        """
        ...

    def apply(
        self,
        /,
        func: Callable,
        raw: bool,
        engine: Literal["numba", "cython"] = ...,
        engine_kwargs: None = ...,
        args: Tuple[None, ...] = ...,
        kwargs: dict = ...,
    ):
        """
        usage.dask: 9
        """
        ...

    def count(self, /):
        """
        usage.dask: 9
        """
        ...

    def cov(self, /):
        """
        usage.dask: 5
        """
        ...

    def kurt(self, /):
        """
        usage.dask: 5
        """
        ...

    def max(self, /):
        """
        usage.dask: 5
        """
        ...

    def mean(self, /):
        """
        usage.xarray: 4
        usage.dask: 14
        """
        ...

    def median(self, /):
        """
        usage.dask: 5
        """
        ...

    def min(self, /):
        """
        usage.dask: 5
        """
        ...

    def quantile(self, /, quantile: float):
        """
        usage.dask: 5
        """
        ...

    def skew(self, /):
        """
        usage.dask: 5
        """
        ...

    def std(self, /):
        """
        usage.dask: 6
        """
        ...

    def sum(self, /):
        """
        usage.dask: 9
        """
        ...

    def var(self, /):
        """
        usage.dask: 5
        """
        ...
