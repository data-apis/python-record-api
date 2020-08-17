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

    @overload
    def get_indexer(self, /, target: numpy.ndarray, method: None, tolerance: None):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_indexer(
        self,
        /,
        target: pandas.core.indexes.base.Index,
        method: Literal["pad"],
        limit: None,
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_indexer(
        self,
        /,
        target: pandas.core.indexes.base.Index,
        method: Literal["backfill"],
        limit: None,
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_indexer(
        self, /, target: numpy.ndarray, method: Literal["nearest"], tolerance: None
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_indexer(
        self,
        /,
        target: numpy.ndarray,
        method: Literal["nearest"],
        tolerance: datetime.timedelta,
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_indexer(
        self, /, target: numpy.ndarray, method: Literal["pad"], tolerance: None
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_indexer(
        self,
        /,
        target: numpy.ndarray,
        method: Literal["pad"],
        tolerance: datetime.timedelta,
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_indexer(
        self, /, target: numpy.ndarray, method: Literal["backfill"], tolerance: None
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_indexer(
        self,
        /,
        target: numpy.ndarray,
        method: Literal["backfill"],
        tolerance: datetime.timedelta,
    ):
        """
        usage.xarray: 1
        """
        ...

    def get_indexer(
        self,
        /,
        target: Union[numpy.ndarray, pandas.core.indexes.base.Index],
        method: Union[Literal["backfill", "pad", "nearest"], None],
        limit: None = ...,
        tolerance: Union[datetime.timedelta, None] = ...,
    ):
        """
        usage.xarray: 9
        """
        ...
