from typing import *


class CategoricalIndex:
    def __init__(
        data: Union[
            pandas.core.arrays.categorical.Categorical,
            pandas.core.indexes.base.Index,
            List[Literal["B", "A", "xyx"]],
        ],
        name: Literal["b", "foo", "A", "B", "C"],
        categories: Union[
            List[Literal["zzz", "xyx", "__UNKNOWN_CATEGORIES__"]],
            pandas.core.indexes.numeric.Float64Index,
            pandas.core.indexes.base.Index,
            pandas.core.indexes.datetimes.DatetimeIndex,
        ] = ...,
        ordered: bool = ...,
    ):
        """
        usage.dask: 12
        """
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
        """
        usage.xarray: 5
        usage.dask: 5
        """
        ...

    def equals(self: object, /, other: pandas.core.indexes.category.CategoricalIndex):
        """
        usage.xarray: 2
        usage.dask: 1
        """
        ...

    def get_indexer(
        self: object, /, target: numpy.ndarray, method: None, tolerance: None
    ):
        """
        usage.xarray: 1
        """
        ...

    def add_categories(self: object, /):
        """
        usage.dask: 1
        """
        ...

    def as_ordered(self: object, /):
        """
        usage.dask: 1
        """
        ...

    def as_unordered(self: object, /):
        """
        usage.dask: 1
        """
        ...

    def remove_categories(self: object, /):
        """
        usage.dask: 1
        """
        ...

    def rename_categories(self: object, /):
        """
        usage.dask: 1
        """
        ...

    def reorder_categories(self: object, /):
        """
        usage.dask: 1
        """
        ...

    def set_categories(self: object, /, *args: Literal["v", "t"]):
        """
        usage.dask: 3
        """
        ...

    def reindex(self: object, /, target: pandas.core.indexes.base.Index):
        """
        usage.dask: 1
        """
        ...

    def dropna(self: object, /):
        """
        usage.dask: 1
        """
        ...

    def __eq__(self: object, _0: pandas.core.indexes.category.CategoricalIndex, /):
        """
        usage.dask: 2
        """
        ...

    def __contains__(self: object, _0: Literal["dtype", "divisions"], /):
        """
        usage.dask: 2
        """
        ...
