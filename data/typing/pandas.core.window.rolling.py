from typing import *


class Rolling:

    # usage.dask: 1
    window: object

    # usage.dask: 1
    win_type: object

    # usage.dask: 1
    min_periods: object

    def mean(self: object, /):
        """
        usage.xarray: 4
        usage.dask: 14
        """
        ...

    def sum(self: object, /):
        """
        usage.dask: 9
        """
        ...

    def count(self: object, /):
        """
        usage.dask: 9
        """
        ...

    def median(self: object, /):
        """
        usage.dask: 5
        """
        ...

    def min(self: object, /):
        """
        usage.dask: 5
        """
        ...

    def max(self: object, /):
        """
        usage.dask: 5
        """
        ...

    def std(self: object, /):
        """
        usage.dask: 6
        """
        ...

    def var(self: object, /):
        """
        usage.dask: 5
        """
        ...

    def skew(self: object, /):
        """
        usage.dask: 5
        """
        ...

    def kurt(self: object, /):
        """
        usage.dask: 5
        """
        ...

    def quantile(self: object, /, quantile: float):
        """
        usage.dask: 5
        """
        ...

    def apply(
        self: object,
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

    def cov(self: object, /):
        """
        usage.dask: 5
        """
        ...

    def aggregate(
        self: object,
        /,
        func: Union[
            Dict[Literal["B", "A"], Union[Callable, List[Callable]]], List[Callable]
        ],
    ):
        """
        usage.dask: 8
        """
        ...
