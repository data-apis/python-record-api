from typing import *


class DataFrameGroupBy:

    # usage.dask: 1
    __name__: ClassVar[object]

    # usage.dask: 1
    A: object

    # usage.dask: 1
    B: object

    # usage.dask: 1
    _selected_obj: object

    # usage.dask: 24
    a: object

    # usage.dask: 20
    b: object

    # usage.dask: 1
    e: object

    # usage.dask: 2
    groups: object

    # usage.dask: 1
    idxmax: object

    # usage.dask: 1
    idxmin: object

    # usage.dask: 4
    obj: object

    # usage.dask: 1
    x: object

    # usage.dask: 3
    y: object

    # usage.dask: 2
    z: object

    def __getitem__(self, _0: object, /):
        """
        usage.dask: 219
        """
        ...

    def aggregate(
        self,
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

    def apply(
        self,
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

    def count(self, /):
        """
        usage.dask: 12
        """
        ...

    def cumcount(self, /):
        """
        usage.dask: 3
        """
        ...

    def cumprod(self, /):
        """
        usage.dask: 4
        """
        ...

    def cumsum(self, /):
        """
        usage.dask: 4
        """
        ...

    def first(self, /):
        """
        usage.dask: 12
        """
        ...

    def get_group(self, /, name: Union[float, int]):
        """
        usage.dask: 5
        """
        ...

    def last(self, /):
        """
        usage.dask: 10
        """
        ...

    def max(self, /):
        """
        usage.dask: 10
        """
        ...

    def mean(self, /):
        """
        usage.dask: 15
        """
        ...

    def min(self, /):
        """
        usage.dask: 9
        """
        ...

    def nunique(self, /):
        """
        usage.dask: 1
        """
        ...

    def prod(self, /):
        """
        usage.dask: 11
        """
        ...

    def size(self, /):
        """
        usage.dask: 9
        """
        ...

    def std(self, /):
        """
        usage.dask: 9
        """
        ...

    def sum(self, /):
        """
        usage.dask: 26
        """
        ...

    def transform(self, /, func: Union[Callable, Literal["sum"], Callable]):
        """
        usage.dask: 19
        """
        ...

    def var(self, /):
        """
        usage.dask: 7
        """
        ...


class SeriesGroupBy:

    # usage.dask: 1
    __name__: ClassVar[object]

    # usage.dask: 1
    idxmax: object

    # usage.dask: 1
    idxmin: object

    # usage.dask: 5
    obj: object

    def __iter__(self, /):
        """
        usage.dask: 2
        """
        ...

    def aggregate(
        self,
        /,
        func: Union[
            Literal["var", "sum", "mean"], List[Literal["max", "min", "mean", "sum"]]
        ],
    ):
        """
        usage.dask: 10
        """
        ...

    def apply(self, /, func: Union[Callable, Literal["sum"], Callable]):
        """
        usage.dask: 21
        """
        ...

    def count(self, /):
        """
        usage.dask: 15
        """
        ...

    def cumcount(self, /):
        """
        usage.dask: 2
        """
        ...

    def cumprod(self, /):
        """
        usage.dask: 3
        """
        ...

    def cumsum(self, /):
        """
        usage.dask: 3
        """
        ...

    def first(self, /):
        """
        usage.xarray: 1
        usage.dask: 14
        """
        ...

    def get_group(self, /, name: int):
        """
        usage.dask: 3
        """
        ...

    def last(self, /):
        """
        usage.dask: 10
        """
        ...

    def max(self, /):
        """
        usage.dask: 11
        """
        ...

    def mean(self, /):
        """
        usage.dask: 13
        """
        ...

    def min(self, /):
        """
        usage.dask: 10
        """
        ...

    def nunique(self, /):
        """
        usage.dask: 14
        """
        ...

    def prod(self, /):
        """
        usage.dask: 9
        """
        ...

    def size(self, /):
        """
        usage.dask: 10
        """
        ...

    def std(self, /):
        """
        usage.dask: 10
        """
        ...

    def sum(self, /):
        """
        usage.dask: 20
        """
        ...

    def transform(self, /, func: Union[Callable, Literal["sum"], Callable]):
        """
        usage.dask: 19
        """
        ...

    def value_counts(self, /):
        """
        usage.dask: 2
        """
        ...

    def var(self, /):
        """
        usage.dask: 8
        """
        ...
