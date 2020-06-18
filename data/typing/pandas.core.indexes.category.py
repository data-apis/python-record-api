from typing import *


class CategoricalIndex:
    def __init__(
        data: Union[
            (
                pandas.core.arrays.categorical.Categorical,
                pandas.core.indexes.base.Index,
                List[Literal[("B", "A", "xyx")]],
            )
        ],
        name: Literal[("b", "foo", "A", "B", "C")],
        categories: Union[
            (
                List[Literal[("zzz", "xyx", "__UNKNOWN_CATEGORIES__")]],
                pandas.core.indexes.numeric.Float64Index,
                pandas.core.indexes.base.Index,
                pandas.core.indexes.datetimes.DatetimeIndex,
            )
        ] = ...,
        ordered: bool = ...,
    ):
        "usage.dask: 12"

    __name__ = ...
    __module__ = ...
    name: Literal[("y",)] = ...
    dtype = ...
    categories = ...
    values = ...
    size = ...
    is_unique = ...
    array = ...
    names: List[Literal[("-overlapped-index-name-0",)]] = ...
    ordered = ...
    codes = ...
    is_monotonic_increasing = ...

    def __getitem__(
        self,
        _0: Union[
            (slice[(Union[(None, int)], Union[(int, None)], None)], int, numpy.ndarray)
        ],
        /,
    ):
        ""

    def equals(self, /, other: pandas.core.indexes.category.CategoricalIndex):
        "usage.xarray: 2, usage.dask: 1"

    def get_indexer(self, /, target: numpy.ndarray, method: None, tolerance: None):
        "usage.xarray: 1"

    def add_categories(self, /):
        "usage.dask: 1"

    def as_ordered(self, /):
        "usage.dask: 1"

    def as_unordered(self, /):
        "usage.dask: 1"

    def remove_categories(self, /):
        "usage.dask: 1"

    def rename_categories(self, /):
        "usage.dask: 1"

    def reorder_categories(self, /):
        "usage.dask: 1"

    def set_categories(self, /, *args: Literal[("v", "t")]):
        "usage.dask: 3"

    def reindex(self, /, target: pandas.core.indexes.base.Index):
        "usage.dask: 1"

    def dropna(self, /):
        "usage.dask: 1"

    def __eq__(self, _0: pandas.core.indexes.category.CategoricalIndex, /):
        ""

    def __contains__(self, _0: Literal[("dtype", "divisions")], /):
        ""
