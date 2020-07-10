from typing import *


class FrozenList:
    def __eq__(
        self,
        _0: Union[
            pandas.core.indexes.frozen.FrozenList,
            Tuple[Literal["x_level_0"], Literal["x_level_1"]],
        ],
        /,
    ):
        """
        usage.xarray: 3
        usage.dask: 6
        """
        ...

    def __getitem__(self, _0: Union[int, slice[int, None, int]], /):
        """
        usage.xarray: 11
        usage.dask: 1
        """
        ...

    def __iter__(self, /):
        """
        usage.xarray: 20
        usage.dask: 8
        """
        ...
