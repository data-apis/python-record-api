from typing import *


class StringMethods:
    def __getitem__(self, _0: Union[int, slice[None, int, None]], /):
        """
        usage.dask: 4
        """
        ...

    def cat(
        self,
        /,
        others: Union[
            Tuple[pandas.core.series.Series, ...],
            pandas.core.series.Series,
            List[pandas.core.series.Series],
        ],
        sep: Literal[":"],
        na_rep: None = ...,
    ):
        """
        usage.dask: 4
        """
        ...

    @overload
    def contains(
        self,
        /,
        pat: Literal["b", "a", "d"],
        case: bool = ...,
        na: bool = ...,
        regex: bool = ...,
    ):
        """
        usage.dask: 10
        """
        ...

    @overload
    def contains(self, /, pat: Literal["at$"], regex: bool):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def contains(self, /, pat: Literal["^col_int"], regex: bool):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def contains(self, /, pat: Literal["float|str"], regex: bool):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def contains(self, /, pat: Literal["^col_s"], regex: bool):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def contains(self, /, pat: Literal["str$"], regex: bool):
        """
        usage.sklearn: 1
        """
        ...

    def contains(
        self, /, pat: str, case: bool = ..., na: bool = ..., regex: bool = ...
    ):
        """
        usage.dask: 10
        usage.sklearn: 5
        """
        ...

    def count(self, /, pat: Literal["A"]):
        """
        usage.dask: 1
        """
        ...

    def extractall(self, /, pat: Literal["(.*)b(.*)"], flags: int = ...):
        """
        usage.dask: 3
        """
        ...

    def isalpha(self, /):
        """
        usage.dask: 1
        """
        ...

    def split(self, /, n: int, expand: bool, pat: Union[Literal[","], None] = ...):
        """
        usage.dask: 8
        """
        ...

    def upper(self, /):
        """
        usage.dask: 1
        """
        ...
