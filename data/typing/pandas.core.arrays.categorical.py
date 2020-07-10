from typing import *


class Categorical:
    def __init__(
        self,
        /,
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
        """
        usage.xarray: 4
        usage.dask: 10
        """
        ...

    @classmethod
    def from_codes(
        cls,
        /,
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
        """
        usage.dask: 5
        """
        ...

    # usage.xarray: 6
    # usage.dask: 1
    categories: object

    # usage.xarray: 1
    # usage.dask: 4
    codes: object

    # usage.dask: 3
    dtype: object

    # usage.dask: 2
    name: Union[Literal["idx"], None]

    # usage.dask: 1
    ordered: object

    def __contains__(
        self, _0: Literal["2014-01-03.csv", "2014-01-02.csv", "2014-01-01.csv"], /
    ):
        """
        usage.dask: 6
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
