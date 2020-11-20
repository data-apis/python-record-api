from typing import *


class Rolling:

    # usage.dask: 1
    min_periods: object

    # usage.dask: 1
    win_type: object

    # usage.dask: 1
    window: object

    @overload
    def aggregate(self, /, func: List[Callable]):
        """
        usage.dask: 4
        """
        ...

    @overload
    def aggregate(self, /, func: Dict[Literal["B", "A"], Callable]):
        """
        usage.dask: 2
        """
        ...

    @overload
    def aggregate(self, /, func: Dict[Literal["A"], List[Callable]]):
        """
        usage.dask: 2
        """
        ...

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

    @overload
    def apply(self, /, func: Callable, raw: bool):
        """
        usage.dask: 2
        """
        ...

    @overload
    def apply(
        self,
        /,
        func: Callable,
        raw: bool,
        engine: Literal["cython"],
        engine_kwargs: None,
        args: Tuple[None, ...],
        kwargs: dict,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def apply(self, /, func: Callable, raw: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def apply(
        self,
        /,
        func: Callable,
        raw: bool,
        engine: Literal["cython"],
        engine_kwargs: None,
        args: Tuple[None, ...],
        kwargs: dict,
    ):
        """
        usage.dask: 1
        """
        ...

    def apply(
        self,
        /,
        func: Callable,
        raw: bool,
        engine: Literal["cython"] = ...,
        engine_kwargs: None = ...,
        args: Tuple[None, ...] = ...,
        kwargs: dict = ...,
    ):
        """
        usage.dask: 5
        """
        ...

    def count(self, /):
        """
        usage.dask: 7
        usage.koalas: 6
        """
        ...

    def cov(self, /):
        """
        usage.dask: 5
        """
        ...

    def kurt(self, /):
        """
        usage.dask: 3
        """
        ...

    def max(self, /):
        """
        usage.dask: 3
        usage.koalas: 6
        """
        ...

    def mean(self, /):
        """
        usage.alphalens: 2
        usage.dask: 12
        usage.koalas: 6
        usage.statsmodels: 3
        usage.xarray: 4
        """
        ...

    def median(self, /):
        """
        usage.dask: 3
        """
        ...

    def min(self, /):
        """
        usage.dask: 3
        usage.koalas: 6
        """
        ...

    def quantile(self, /, quantile: float):
        """
        usage.dask: 3
        """
        ...

    def skew(self, /):
        """
        usage.dask: 3
        """
        ...

    @overload
    def std(self, /):
        """
        usage.dask: 3
        usage.koalas: 6
        """
        ...

    @overload
    def std(self, /, ddof: int):
        """
        usage.dask: 1
        """
        ...

    def std(self, /, ddof: int = ...):
        """
        usage.dask: 4
        usage.koalas: 6
        """
        ...

    def sum(self, /):
        """
        usage.dask: 9
        usage.koalas: 6
        """
        ...

    @overload
    def var(self, /):
        """
        usage.dask: 2
        usage.koalas: 6
        """
        ...

    @overload
    def var(self, /, ddof: int):
        """
        usage.dask: 1
        """
        ...

    def var(self, /, ddof: int = ...):
        """
        usage.dask: 3
        usage.koalas: 6
        """
        ...


class RollingGroupby:
    def count(self, /):
        """
        usage.koalas: 15
        """
        ...

    def max(self, /):
        """
        usage.koalas: 15
        """
        ...

    def mean(self, /):
        """
        usage.koalas: 15
        """
        ...

    def min(self, /):
        """
        usage.koalas: 15
        """
        ...

    def std(self, /):
        """
        usage.koalas: 15
        """
        ...

    def sum(self, /):
        """
        usage.koalas: 15
        """
        ...

    def var(self, /):
        """
        usage.koalas: 15
        """
        ...
