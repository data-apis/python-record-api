from typing import *


class StringMethods:
    def upper(self: object, /):
        """
        usage.dask: 1
        """
        ...

    def contains(self: object, /, pat: Literal["a", "d"]):
        """
        usage.dask: 9
        """
        ...

    def __getitem__(self: object, _0: Union[int, slice[None, int, None]], /):
        """
        usage.dask: 4
        """
        ...

    def extractall(self: object, /, pat: Literal["(.*)b(.*)"]):
        """
        usage.dask: 3
        """
        ...

    def cat(
        self: object,
        /,
        others: Union[
            Tuple[pandas.core.series.Series, ...],
            pandas.core.series.Series,
            List[pandas.core.series.Series],
        ],
        sep: Literal[":"],
    ):
        """
        usage.dask: 4
        """
        ...

    def split(self: object, /, n: int, expand: bool):
        """
        usage.dask: 5
        """
        ...

    def count(self: object, /, pat: Literal["A"]):
        """
        usage.dask: 1
        """
        ...

    def isalpha(self: object, /):
        """
        usage.dask: 1
        """
        ...
