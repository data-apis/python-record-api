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
        usage.dask: 6
        usage.xarray: 3
        """
        ...

    def __getitem__(self, _0: Union[int, slice[int, None, int]], /):
        """
        usage.dask: 1
        usage.xarray: 11
        """
        ...

    def __iter__(self, /):
        """
        usage.dask: 8
        usage.xarray: 22
        """
        ...
