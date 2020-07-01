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
        "\n    usage.xarray: 1\n    usage.dask: 14\n    "
        ...

    def sum(self: object, /):
        "\n    usage.dask: 20\n    "
        ...

    def nunique(self: object, /):
        "\n    usage.dask: 14\n    "
        ...

    def count(self: object, /):
        "\n    usage.dask: 15\n    "
        ...

    def apply(self: object, /, func: Union[Callable, Literal["sum"], Callable]):
        "\n    usage.dask: 21\n    "
        ...

    def mean(self: object, /):
        "\n    usage.dask: 13\n    "
        ...

    def min(self: object, /):
        "\n    usage.dask: 10\n    "
        ...

    def max(self: object, /):
        "\n    usage.dask: 11\n    "
        ...

    def size(self: object, /):
        "\n    usage.dask: 10\n    "
        ...

    def std(self: object, /):
        "\n    usage.dask: 10\n    "
        ...

    def var(self: object, /):
        "\n    usage.dask: 8\n    "
        ...

    def last(self: object, /):
        "\n    usage.dask: 10\n    "
        ...

    def prod(self: object, /):
        "\n    usage.dask: 9\n    "
        ...

    def get_group(self: object, /, name: int):
        "\n    usage.dask: 3\n    "
        ...

    def transform(self: object, /, func: Union[Callable, Literal["sum"], Callable]):
        "\n    usage.dask: 19\n    "
        ...

    def cumsum(self: object, /):
        "\n    usage.dask: 3\n    "
        ...

    def cumprod(self: object, /):
        "\n    usage.dask: 3\n    "
        ...

    def cumcount(self: object, /):
        "\n    usage.dask: 2\n    "
        ...

    def aggregate(
        self: object,
        /,
        func: Union[
            Literal[("var", "sum", "mean")],
            List[Literal[("max", "min", "mean", "sum")]],
        ],
    ):
        "\n    usage.dask: 10\n    "
        ...

    def __iter__(self: object, /):
        "\n    usage.dask: 2\n    "
        ...

    def value_counts(self: object, /):
        "\n    usage.dask: 2\n    "
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
        "\n    usage.dask: 5\n    "
        ...

    def sum(self: object, /):
        "\n    usage.dask: 26\n    "
        ...

    def __getitem__(self: object, _0: object, /):
        "\n    usage.dask: 219\n    "
        ...

    def apply(
        self: object,
        /,
        func: Union[
            Callable, Literal["sum"], numpy.int64, dask.utils.methodcaller, Callable
        ],
        *args: Literal[("v", "t")],
    ):
        "\n    usage.dask: 63\n    "
        ...

    def count(self: object, /):
        "\n    usage.dask: 12\n    "
        ...

    def mean(self: object, /):
        "\n    usage.dask: 15\n    "
        ...

    def min(self: object, /):
        "\n    usage.dask: 9\n    "
        ...

    def max(self: object, /):
        "\n    usage.dask: 10\n    "
        ...

    def size(self: object, /):
        "\n    usage.dask: 9\n    "
        ...

    def std(self: object, /):
        "\n    usage.dask: 9\n    "
        ...

    def var(self: object, /):
        "\n    usage.dask: 7\n    "
        ...

    def first(self: object, /):
        "\n    usage.dask: 12\n    "
        ...

    def last(self: object, /):
        "\n    usage.dask: 10\n    "
        ...

    def prod(self: object, /):
        "\n    usage.dask: 11\n    "
        ...

    def nunique(self: object, /):
        "\n    usage.dask: 1\n    "
        ...

    def transform(self: object, /, func: Union[Callable, Literal["sum"], Callable]):
        "\n    usage.dask: 19\n    "
        ...

    def aggregate(
        self: object,
        /,
        func: Union[
            Dict[
                Literal[("b", "c", "e")],
                Union[
                    Literal[("mean", "sum", "count", "std")],
                    List[Literal[("sum", "mean")]],
                ],
            ],
            str,
            List[Literal[("max", "min", "sum", "mean")]],
        ],
    ):
        "\n    usage.dask: 22\n    "
        ...

    def cumsum(self: object, /):
        "\n    usage.dask: 4\n    "
        ...

    def cumprod(self: object, /):
        "\n    usage.dask: 4\n    "
        ...

    def cumcount(self: object, /):
        "\n    usage.dask: 3\n    "
        ...
