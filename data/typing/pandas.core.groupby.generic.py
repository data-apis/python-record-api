from typing import *


class SeriesGroupBy:
    __name__ = ...
    obj = ...
    idxmin = ...
    idxmax = ...

    def first(self, /):
        "usage.xarray: 1, usage.dask: 14"

    def sum(self, /):
        "usage.dask: 20"

    def nunique(self, /):
        "usage.dask: 14"

    def count(self, /):
        "usage.dask: 15"

    def apply(self, /, func: Union[(Callable, Literal[("sum",)], Callable)]):
        "usage.dask: 21"

    def mean(self, /):
        "usage.dask: 13"

    def min(self, /):
        "usage.dask: 10"

    def max(self, /):
        "usage.dask: 11"

    def size(self, /):
        "usage.dask: 10"

    def std(self=..., /):
        "usage.dask: 10"

    def var(self=..., /):
        "usage.dask: 8"

    def last(self, /):
        "usage.dask: 10"

    def prod(self, /):
        "usage.dask: 9"

    def get_group(self, /, name: int):
        "usage.dask: 3"

    def transform(self, /, func: Union[(Callable, Literal[("sum",)], Callable)]):
        "usage.dask: 19"

    def cumsum(self, /):
        "usage.dask: 3"

    def cumprod(self, /):
        "usage.dask: 3"

    def cumcount(self, /):
        "usage.dask: 2"

    def aggregate(
        self,
        /,
        func: Union[
            (
                Literal[("var", "sum", "mean")],
                List[Literal[("max", "min", "mean", "sum")]],
            )
        ],
    ):
        "usage.dask: 10"

    def __iter__(self, /):
        ""

    def value_counts(self, /):
        "usage.dask: 2"


class DataFrameGroupBy:
    __name__ = ...
    groups = ...
    y = ...
    obj = ...
    a = ...
    A = ...
    b = ...
    B = ...
    z = ...
    _selected_obj = ...
    idxmin = ...
    idxmax = ...
    x = ...
    e = ...

    def get_group(self, /, name: Union[(float, int)]):
        "usage.dask: 5"

    def sum(self=..., /):
        "usage.dask: 26"

    def __getitem__(self, _0, /):
        ""

    def apply(
        self,
        /,
        func: Union[
            (
                Callable,
                Literal[("sum",)],
                numpy.int64,
                dask.utils.methodcaller,
                Callable,
            )
        ],
        *args: Literal[("v", "t")],
    ):
        "usage.dask: 63"

    def count(self, /):
        "usage.dask: 12"

    def mean(self, /):
        "usage.dask: 15"

    def min(self, /):
        "usage.dask: 9"

    def max(self, /):
        "usage.dask: 10"

    def size(self, /):
        "usage.dask: 9"

    def std(self=..., /):
        "usage.dask: 9"

    def var(self=..., /):
        "usage.dask: 7"

    def first(self, /):
        "usage.dask: 12"

    def last(self, /):
        "usage.dask: 10"

    def prod(self=..., /):
        "usage.dask: 11"

    def nunique(self, /):
        "usage.dask: 1"

    def transform(self, /, func: Union[(Callable, Literal[("sum",)], Callable)]):
        "usage.dask: 19"

    def aggregate(
        self,
        /,
        func: Union[
            (
                Dict[
                    (
                        Literal[("b", "c", "e")],
                        Union[
                            (
                                Literal[("mean", "sum", "count", "std")],
                                List[Literal[("sum", "mean")]],
                            )
                        ],
                    )
                ],
                str,
                List[Literal[("max", "min", "sum", "mean")]],
            )
        ],
    ):
        "usage.dask: 22"

    def cumsum(self=..., /):
        "usage.dask: 4"

    def cumprod(self=..., /):
        "usage.dask: 4"

    def cumcount(self, /):
        "usage.dask: 3"
