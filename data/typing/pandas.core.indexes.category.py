from typing import *


class CategoricalIndex:
    def __init__(
        data: Union[
            pandas.core.arrays.categorical.Categorical,
            pandas.core.indexes.base.Index,
            List[Literal[("B", "A", "xyx")]],
        ],
        name: Literal[("b", "foo", "A", "B", "C")],
        categories: Union[
            List[Literal[("zzz", "xyx", "__UNKNOWN_CATEGORIES__")]],
            pandas.core.indexes.numeric.Float64Index,
            pandas.core.indexes.base.Index,
            pandas.core.indexes.datetimes.DatetimeIndex,
        ] = ...,
        ordered: bool = ...,
    ):
        "\n    usage.dask: 12\n    "
        ...

    # usage.dask: 2
    __name__: ClassVar[object]

    # usage.dask: 1
    __module__: ClassVar[object]

    # usage.xarray: 2
    # usage.dask: 16
    name: Literal["y"]

    # usage.xarray: 1
    # usage.dask: 3
    dtype: object

    # usage.xarray: 1
    # usage.dask: 11
    categories: object

    # usage.xarray: 1
    values: object

    # usage.xarray: 2
    size: object

    # usage.xarray: 1
    is_unique: object

    # usage.dask: 1
    array: object

    # usage.dask: 3
    names: List[Literal["-overlapped-index-name-0"]]

    # usage.dask: 7
    ordered: object

    # usage.dask: 2
    codes: object

    # usage.dask: 1
    is_monotonic_increasing: object

    def __getitem__(
        self: object,
        _0: Union[
            slice[Union[None, int], Union[int, None], Union[None, int]],
            int,
            numpy.ndarray,
        ],
        /,
    ):
        "\n    usage.xarray: 5\n    usage.dask: 5\n    "
        ...

    def equals(self: object, /, other: pandas.core.indexes.category.CategoricalIndex):
        "\n    usage.xarray: 2\n    usage.dask: 1\n    "
        ...

    def get_indexer(
        self: object, /, target: numpy.ndarray, method: None, tolerance: None
    ):
        "\n    usage.xarray: 1\n    "
        ...

    def add_categories(self: object, /):
        "\n    usage.dask: 1\n    "
        ...

    def as_ordered(self: object, /):
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

    def set_categories(self: object, /, *args: Literal[("v", "t")]):
        "\n    usage.dask: 3\n    "
        ...

    def reindex(self: object, /, target: pandas.core.indexes.base.Index):
        "\n    usage.dask: 1\n    "
        ...

    def dropna(self: object, /):
        "\n    usage.dask: 1\n    "
        ...

    def __eq__(self: object, _0: pandas.core.indexes.category.CategoricalIndex, /):
        "\n    usage.dask: 2\n    "
        ...

    def __contains__(self: object, _0: Literal[("dtype", "divisions")], /):
        "\n    usage.dask: 2\n    "
        ...
