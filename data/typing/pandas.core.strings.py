from typing import *


class StringMethods:
    def upper(self, /):
        "usage.dask: 1"

    def contains(self=..., /, pat: Literal[("a", "d")] = ...):
        "usage.dask: 9"

    def __getitem__(self, _0: Union[(int, slice[(None, int, None)])], /):
        ""

    def extractall(self, /, pat: Literal[("(.*)b(.*)",)] = ...):
        "usage.dask: 3"

    def cat(
        self,
        /,
        others: Union[
            (
                Tuple[(pandas.core.series.Series, ...)],
                pandas.core.series.Series,
                List[pandas.core.series.Series],
            )
        ],
        sep: Literal[(":",)] = ...,
    ):
        "usage.dask: 4"

    def split(self, /, n: int, expand: bool = ...):
        "usage.dask: 5"

    def count(self, /, pat: Literal[("A",)]):
        "usage.dask: 1"

    def isalpha(self, /):
        "usage.dask: 1"
