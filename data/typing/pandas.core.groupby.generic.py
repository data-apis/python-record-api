from typing import *


class SeriesGroupBy:

    # usage.dask: 1
    __name__: ClassVar[object]

    # usage.dask: 5
    obj: object

    # usage.dask: 1
    idxmin: object

    # usage.dask: 1
    idxmax: object

    def first(self: object, /):
        """
        usage.xarray: 1
        usage.dask: 14
        """
        ...

    def sum(self: object, /):
        """
        usage.dask: 20
        """
        ...

    def nunique(self: object, /):
        """
        usage.dask: 14
        """
        ...

    def count(self: object, /):
        """
        usage.dask: 15
        """
        ...

    def apply(self: object, /, func: Union[Callable, Literal["sum"], Callable]):
        """
        usage.dask: 21
        """
        ...

    def mean(self: object, /):
        """
        usage.dask: 13
        """
        ...

    def min(self: object, /):
        """
        usage.dask: 10
        """
        ...

    def max(self: object, /):
        """
        usage.dask: 11
        """
        ...

    def size(self: object, /):
        """
        usage.dask: 10
        """
        ...

    def std(self: object, /):
        """
        usage.dask: 10
        """
        ...

    def var(self: object, /):
        """
        usage.dask: 8
        """
        ...

    def last(self: object, /):
        """
        usage.dask: 10
        """
        ...

    def prod(self: object, /):
        """
        usage.dask: 9
        """
        ...

    def get_group(self: object, /, name: int):
        """
        usage.dask: 3
        """
        ...

    def transform(self: object, /, func: Union[Callable, Literal["sum"], Callable]):
        """
        usage.dask: 19
        """
        ...

    def cumsum(self: object, /):
        """
        usage.dask: 3
        """
        ...

    def cumprod(self: object, /):
        """
        usage.dask: 3
        """
        ...

    def cumcount(self: object, /):
        """
        usage.dask: 2
        """
        ...

    def aggregate(
        self: object,
        /,
        func: Union[
            Literal["var", "sum", "mean"], List[Literal["max", "min", "mean", "sum"]]
        ],
    ):
        """
        usage.dask: 10
        """
        ...

    def __iter__(self: object, /):
        """
        usage.dask: 2
        """
        ...

    def value_counts(self: object, /):
        """
        usage.dask: 2
        """
        ...


class DataFrameGroupBy:

    # usage.dask: 1
    __name__: ClassVar[object]

    # usage.dask: 2
    groups: object

    # usage.dask: 3
    y: object

    # usage.dask: 4
    obj: object

    # usage.dask: 24
    a: object

    # usage.dask: 1
    A: object

    # usage.dask: 20
    b: object

    # usage.dask: 1
    B: object

    # usage.dask: 2
    z: object

    # usage.dask: 1
    _selected_obj: object

    # usage.dask: 1
    idxmin: object

    # usage.dask: 1
    idxmax: object

    # usage.dask: 1
    x: object

    # usage.dask: 1
    e: object

    def get_group(self: object, /, name: Union[float, int]):
        """
        usage.dask: 5
        """
        ...

    def sum(self: object, /):
        """
        usage.dask: 26
        """
        ...

    def __getitem__(self: object, _0: object, /):
        """
        usage.dask: 219
        """
        ...

    def apply(
        self: object,
        /,
        func: Union[
            Callable, Literal["sum"], numpy.int64, dask.utils.methodcaller, Callable
        ],
        *args: Literal["v", "t"],
    ):
        """
        usage.dask: 63
        """
        ...

    def count(self: object, /):
        """
        usage.dask: 12
        """
        ...

    def mean(self: object, /):
        """
        usage.dask: 15
        """
        ...

    def min(self: object, /):
        """
        usage.dask: 9
        """
        ...

    def max(self: object, /):
        """
        usage.dask: 10
        """
        ...

    def size(self: object, /):
        """
        usage.dask: 9
        """
        ...

    def std(self: object, /):
        """
        usage.dask: 9
        """
        ...

    def var(self: object, /):
        """
        usage.dask: 7
        """
        ...

    def first(self: object, /):
        """
        usage.dask: 12
        """
        ...

    def last(self: object, /):
        """
        usage.dask: 10
        """
        ...

    def prod(self: object, /):
        """
        usage.dask: 11
        """
        ...

    def nunique(self: object, /):
        """
        usage.dask: 1
        """
        ...

    def transform(self: object, /, func: Union[Callable, Literal["sum"], Callable]):
        """
        usage.dask: 19
        """
        ...

    def aggregate(
        self: object,
        /,
        func: Union[
            Dict[
                Literal["b", "c", "e"],
                Union[
                    Literal["mean", "sum", "count", "std"], List[Literal["sum", "mean"]]
                ],
            ],
            str,
            List[Literal["max", "min", "sum", "mean"]],
        ],
    ):
        """
        usage.dask: 22
        """
        ...

    def cumsum(self: object, /):
        """
        usage.dask: 4
        """
        ...

    def cumprod(self: object, /):
        """
        usage.dask: 4
        """
        ...

    def cumcount(self: object, /):
        """
        usage.dask: 3
        """
        ...
