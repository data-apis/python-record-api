from typing import *


class CFTimeIndex:
    def copy(self, /, deep: bool):
        """
        usage.xarray: 1
        """
        ...

    def equals(self, /, other: xarray.coding.cftimeindex.CFTimeIndex):
        """
        usage.xarray: 11
        """
        ...

    def get_indexer(
        self,
        /,
        target: Union[numpy.ndarray, pandas.core.indexes.base.Index],
        method: Union[Literal["backfill", "pad", "nearest"], None],
    ):
        """
        usage.xarray: 9
        """
        ...
