from typing import *


class CategoricalIndex:

    # usage.dask: 1
    __module__: ClassVar[object]

    # usage.dask: 2
    __name__: ClassVar[object]

    # usage.dask: 1
    array: object

    # usage.dask: 11
    # usage.xarray: 1
    categories: object

    # usage.dask: 2
    codes: object

    # usage.dask: 4
    # usage.xarray: 1
    dtype: object

    # usage.xarray: 1
    is_unique: object

    # usage.dask: 18
    # usage.xarray: 2
    name: Union[None, Literal["idx", "y"]]

    # usage.dask: 3
    names: List[str]

    # usage.dask: 7
    ordered: object

    # usage.xarray: 2
    size: object

    # usage.xarray: 1
    values: object

    @overload
    def __contains__(self, _0: Literal["divisions"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["dtype"], /):
        """
        usage.dask: 1
        """
        ...

    def __contains__(self, _0: Literal["dtype", "divisions"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __eq__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 4
        """
        ...

    @overload
    def __eq__(self, _0: pandas.core.indexes.category.CategoricalIndex, /):
        """
        usage.dask: 2
        """
        ...

    def __eq__(
        self, _0: Union[pandas.core.indexes.category.CategoricalIndex, numpy.ndarray], /
    ):
        """
        usage.dask: 2
        usage.pandas: 4
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, int, None], /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[int, None, int], /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def __getitem__(self, _0: int, /):
        """
        usage.dask: 4
        usage.xarray: 1
        """
        ...

    @overload
    def __getitem__(self, _0: numpy.ndarray, /):
        """
        usage.xarray: 2
        """
        ...

    @overload
    def __getitem__(self, _0: slice[int, int, int], /):
        """
        usage.dask: 1
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
        usage.dask: 5
        usage.xarray: 5
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

    def get_indexer(self, /, target: numpy.ndarray, method: None, tolerance: None):
        """
        usage.xarray: 1
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

    @overload
    def set_categories(self, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def set_categories(self, /, *args: Literal["v", "t"]):
        """
        usage.dask: 2
        """
        ...

    def set_categories(self, /, *args: Literal["v", "t"]):
        """
        usage.dask: 3
        """
        ...
