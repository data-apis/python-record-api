from typing import *


class CategoricalIndex:
    name = ...
    dtype = ...
    categories = ...
    values = ...
    size = ...
    is_unique = ...

    def __getitem__(
        self,
        _0: Union[
            (numpy.ndarray, int, slice[(Union[(None, int)], Union[(None, int)], None)])
        ],
        /,
    ):
        ""

    def equals(self, /, other: pandas.core.indexes.category.CategoricalIndex):
        "usage.xarray: 2"

    def get_indexer(self, /, target: numpy.ndarray, method: None, tolerance: None):
        "usage.xarray: 1"
