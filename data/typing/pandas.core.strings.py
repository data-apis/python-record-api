from typing import *


class StringMethods:
    def upper(self: object, /):
        "\n    usage.dask: 1\n    "
        ...

    def contains(self: object, /, pat: Literal[("a", "d")]):
        "\n    usage.dask: 9\n    "
        ...

    def __getitem__(self: object, _0: Union[int, slice[None, int, None]], /):
        "\n    usage.dask: 4\n    "
        ...

    def extractall(self: object, /, pat: Literal["(.*)b(.*)"]):
        "\n    usage.dask: 3\n    "
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
        "\n    usage.dask: 4\n    "
        ...

    def split(self: object, /, n: int, expand: bool):
        "\n    usage.dask: 5\n    "
        ...

    def count(self: object, /, pat: Literal["A"]):
        "\n    usage.dask: 1\n    "
        ...

    def isalpha(self: object, /):
        "\n    usage.dask: 1\n    "
        ...
