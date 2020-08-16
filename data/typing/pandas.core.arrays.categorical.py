from typing import *


class Categorical:
    def __init__(
        self,
        /,
        values: Union[
            List[Union[str, int]],
            pandas.core.indexes.datetimes.DatetimeIndex,
            pandas.core.indexes.numeric.Float64Index,
            pandas.core.indexes.base.Index,
        ],
        categories: Union[None, pandas.core.indexes.base.Index] = ...,
        ordered: bool = ...,
    ):
        """
        usage.dask: 10
        usage.sklearn: 1
        """
        ...

    @classmethod
    def from_codes(
        cls,
        /,
        codes: Union[numpy.ndarray, List[int]],
        categories: Union[pandas.core.indexes.base.Index, List[str]],
    ):
        """
        usage.dask: 5
        """
        ...

    # usage.dask: 1
    # usage.xarray: 6
    categories: object

    # usage.dask: 4
    # usage.xarray: 1
    codes: object

    # usage.dask: 3
    # usage.sklearn: 1
    dtype: object

    # usage.dask: 1
    ordered: object

    def __contains__(
        self, _0: Literal["2014-01-03.csv", "2014-01-02.csv", "2014-01-01.csv"], /
    ):
        """
        usage.dask: 6
        """
        ...

    def __gt__(self, _0: numpy.int64, /):
        """
        usage.pandas: 10
        """
        ...

    def sort_values(self, /):
        """
        usage.dask: 1
        """
        ...


class CategoricalAccessor:

    # usage.dask: 18
    categories: object

    # usage.dask: 2
    codes: object

    # usage.dask: 6
    ordered: object

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
        usage.dask: 9
        """
        ...
