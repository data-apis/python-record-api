from typing import *


class Categorical:
    @overload
    @classmethod
    def from_codes(
        cls,
        /,
        codes: numpy.ndarray,
        categories: List[Literal["2014-01-03.csv", "2014-01-02.csv", "2014-01-01.csv"]],
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def from_codes(cls, /, codes: numpy.ndarray, categories: List[str]):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def from_codes(
        cls,
        /,
        codes: List[int],
        categories: pandas.core.indexes.base.Index,
        ordered: bool,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def from_codes(
        cls,
        /,
        codes: numpy.ndarray,
        categories: pandas.core.indexes.base.Index,
        ordered: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @classmethod
    def from_codes(
        cls,
        /,
        codes: Union[numpy.ndarray, List[int]],
        categories: Union[pandas.core.indexes.base.Index, List[str]],
        ordered: bool = ...,
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

    @overload
    def __contains__(self, _0: Literal["2014-01-01.csv"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __contains__(self, _0: Literal["2014-01-02.csv"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __contains__(self, _0: Literal["2014-01-03.csv"], /):
        """
        usage.dask: 2
        """
        ...

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

    @overload
    def set_categories(self, /, *args: Literal["v", "t"]):
        """
        usage.dask: 8
        """
        ...

    @overload
    def set_categories(self, /):
        """
        usage.dask: 1
        """
        ...

    def set_categories(self, /, *args: Literal["v", "t"]):
        """
        usage.dask: 9
        """
        ...
