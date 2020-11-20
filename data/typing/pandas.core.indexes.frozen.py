from typing import *


class FrozenList:
    def __add__(self, _0: List[None], /):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["level_2"], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["level_1"], /):
        """
        usage.koalas: 1
        """
        ...

    def __contains__(self, _0: Literal["level_1", "level_2"], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def __eq__(self, _0: Tuple[Literal["x_level_0"], Literal["x_level_1"]], /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def __eq__(self, _0: pandas.core.indexes.frozen.FrozenList, /):
        """
        usage.dask: 6
        usage.xarray: 2
        """
        ...

    @overload
    def __eq__(self, _0: List[None], /):
        """
        usage.hvplot: 1
        """
        ...

    def __eq__(
        self,
        _0: Union[
            pandas.core.indexes.frozen.FrozenList,
            Tuple[Literal["x_level_0"], Literal["x_level_1"]],
            List[None],
        ],
        /,
    ):
        """
        usage.dask: 6
        usage.hvplot: 1
        usage.xarray: 3
        """
        ...

    @overload
    def __getitem__(self, _0: int, /):
        """
        usage.alphalens: 9
        usage.dask: 1
        usage.koalas: 4
        usage.statsmodels: 8
        usage.xarray: 10
        """
        ...

    @overload
    def __getitem__(self, _0: slice[int, None, int], /):
        """
        usage.koalas: 1
        usage.xarray: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, int, None], /):
        """
        usage.koalas: 2
        """
        ...

    def __getitem__(
        self,
        _0: Union[int, slice[Union[int, None], Union[None, int], Union[int, None]]],
        /,
    ):
        """
        usage.alphalens: 9
        usage.dask: 1
        usage.koalas: 7
        usage.statsmodels: 8
        usage.xarray: 11
        """
        ...

    def __iter__(self, /):
        """
        usage.dask: 8
        usage.geopandas: 1
        usage.koalas: 3
        usage.xarray: 22
        """
        ...
