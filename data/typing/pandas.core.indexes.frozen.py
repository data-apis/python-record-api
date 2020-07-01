from typing import *


class FrozenList:
    def __iter__(self: object, /):
        "\n    usage.xarray: 20\n    usage.dask: 8\n    "
        ...

    def __getitem__(self: object, _0: Union[int, slice[int, None, int]], /):
        "\n    usage.xarray: 11\n    usage.dask: 1\n    "
        ...

    def __eq__(
        self: object,
        _0: Union[
            pandas.core.indexes.frozen.FrozenList,
            Tuple[Literal["x_level_0"], Literal["x_level_1"]],
        ],
        /,
    ):
        "\n    usage.xarray: 3\n    usage.dask: 6\n    "
        ...
