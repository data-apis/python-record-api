from typing import *


class Rolling:

    # usage.dask: 1
    window: object

    # usage.dask: 1
    win_type: object

    # usage.dask: 1
    min_periods: object

    def mean(self: object, /):
        "\n    usage.xarray: 4\n    usage.dask: 14\n    "
        ...

    def sum(self: object, /):
        "\n    usage.dask: 9\n    "
        ...

    def count(self: object, /):
        "\n    usage.dask: 9\n    "
        ...

    def median(self: object, /):
        "\n    usage.dask: 5\n    "
        ...

    def min(self: object, /):
        "\n    usage.dask: 5\n    "
        ...

    def max(self: object, /):
        "\n    usage.dask: 5\n    "
        ...

    def std(self: object, /):
        "\n    usage.dask: 6\n    "
        ...

    def var(self: object, /):
        "\n    usage.dask: 5\n    "
        ...

    def skew(self: object, /):
        "\n    usage.dask: 5\n    "
        ...

    def kurt(self: object, /):
        "\n    usage.dask: 5\n    "
        ...

    def quantile(self: object, /, quantile: float):
        "\n    usage.dask: 5\n    "
        ...

    def apply(
        self: object,
        /,
        func: Callable,
        raw: bool,
        engine: Literal[("numba", "cython")] = ...,
        engine_kwargs: None = ...,
        args: Tuple[None, ...] = ...,
        kwargs: dict = ...,
    ):
        "\n    usage.dask: 9\n    "
        ...

    def cov(self: object, /):
        "\n    usage.dask: 5\n    "
        ...

    def aggregate(
        self: object,
        /,
        func: Union[
            Dict[Literal[("B", "A")], Union[Callable, List[Callable]]], List[Callable]
        ],
    ):
        "\n    usage.dask: 8\n    "
        ...
