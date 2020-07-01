from typing import *


class Categorical:
    def __init__(
        values: Union[
            pandas.core.indexes.datetimes.DatetimeIndex,
            pandas.core.indexes.numeric.Float64Index,
            pandas.core.indexes.base.Index,
            numpy.ndarray,
            List[str],
        ],
        categories: Union[None, pandas.core.indexes.base.Index] = ...,
        ordered: bool = ...,
    ):
        "\n    usage.xarray: 4\n    usage.dask: 10\n    "
        ...

    @classmethod
    def from_codes(
        codes: Union[numpy.ndarray, List[int]],
        categories: Union[
            pandas.core.indexes.base.Index,
            List[
                Literal[
                    "2014-01-03.csv",
                    "2014-01-02.csv",
                    "2014-01-01.csv",
                    "/private/var/folders/xn/05ktz3056kqd9n8frgd6236h00",
                ]
            ],
        ],
    ):
        "\n    usage.dask: 5\n    "
        ...

    # usage.xarray: 1
    # usage.dask: 4
    codes: object

    # usage.xarray: 6
    # usage.dask: 1
    categories: object

    # usage.dask: 3
    dtype: object

    # usage.dask: 2
    name: Union[Literal["idx"], None]

    # usage.dask: 1
    ordered: object

    def __contains__(
        self: object,
        _0: Literal["2014-01-03.csv", "2014-01-02.csv", "2014-01-01.csv"],
        /,
    ):
        "\n    usage.dask: 6\n    "
        ...

    def sort_values(self: object, /):
        "\n    usage.dask: 1\n    "
        ...


class CategoricalAccessor:

    # usage.dask: 18
    categories: object

    # usage.dask: 6
    ordered: object

    # usage.dask: 2
    codes: object

    def set_categories(self: object, /, *args: Literal["v", "t"]):
        "\n    usage.dask: 9\n    "
        ...

    def as_ordered(self: object, /):
        "\n    usage.dask: 1\n    "
        ...

    def add_categories(self: object, /):
        "\n    usage.dask: 1\n    "
        ...

    def as_unordered(self: object, /):
        "\n    usage.dask: 1\n    "
        ...

    def remove_categories(self: object, /):
        "\n    usage.dask: 1\n    "
        ...

    def rename_categories(self: object, /):
        "\n    usage.dask: 1\n    "
        ...

    def reorder_categories(self: object, /):
        "\n    usage.dask: 1\n    "
        ...
