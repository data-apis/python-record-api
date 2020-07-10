from typing import *


class CategoricalIndex:
    def __init__(
        self,
        /,
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

    # usage.dask: 1
    __module__: ClassVar[object]

    # usage.dask: 2
    __name__: ClassVar[object]

    # usage.dask: 1
    array: object

    # usage.xarray: 1
    # usage.dask: 11
    categories: object

    # usage.dask: 2
    codes: object

    # usage.xarray: 1
    # usage.dask: 3
    dtype: object

    # usage.dask: 1
    is_monotonic_increasing: object

    # usage.xarray: 1
    is_unique: object

    # usage.xarray: 2
    # usage.dask: 16
    name: Literal["y"]

    # usage.dask: 3
    names: List[Literal["-overlapped-index-name-0"]]

    # usage.dask: 7
    ordered: object

    # usage.xarray: 2
    size: object

    # usage.xarray: 1
    values: object

    def __contains__(self, _0: Literal["dtype", "divisions"], /):
        """
        usage.dask: 2
        """
        ...

    def __eq__(self, _0: pandas.core.indexes.category.CategoricalIndex, /):
        """
        usage.dask: 2
        """
        ...

    def __getitem__(
        self,
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

    def add_categories(self, /):
        """
        usage.dask: 1
        """
        ...

    def as_ordered(self, /):
        """
        usage.dask: 1
        """
        ...

    def as_unordered(self, /):
        """
        usage.dask: 1
        """
        ...

    def dropna(self, /):
        """
        usage.dask: 1
        """
        ...

    def equals(self, /, other: pandas.core.indexes.category.CategoricalIndex):
        """
        usage.xarray: 2
        usage.dask: 1
        """
        ...

    def get_indexer(self, /, target: numpy.ndarray, method: None, tolerance: None):
        """
        usage.xarray: 1
        """
        ...

    def reindex(self, /, target: pandas.core.indexes.base.Index):
        """
        usage.dask: 1
        """
        ...

    def remove_categories(self, /):
        """
        usage.dask: 1
        """
        ...

    def rename_categories(self, /):
        """
        usage.dask: 1
        """
        ...

    def reorder_categories(self, /):
        """
        usage.dask: 1
        """
        ...

    def set_categories(self, /, *args: Literal["v", "t"]):
        """
        usage.dask: 3
        """
        ...
