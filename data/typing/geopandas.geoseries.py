from typing import *


class GeoSeries:
    @overload
    def __getitem__(self, /, key: int):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: Literal["A"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: Literal["B"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: Literal["C"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: slice[None, int, None]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: pandas.core.series.Series):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: List[bool]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: numpy.ndarray):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: slice[int, None, int]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: slice[None, None, None]):
        """
        usage.geopandas: 1
        """
        ...

    def __getitem__(self, /, key: object):
        """
        usage.geopandas: 10
        """
        ...

    @overload
    def __init__(
        self, /, data: pandas.core.internals.managers.SingleBlockManager, index: None
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(self, /, data: geopandas.geoseries.GeoSeries, index: None, name: None):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: geopandas.array.GeometryArray,
        index: pandas.core.indexes.range.RangeIndex,
        name: Literal["geometry"],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: geopandas.array.GeometryArray,
        index: pandas.core.indexes.range.RangeIndex,
        name: Literal["geom"],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: geopandas.array.GeometryArray,
        index: pandas.core.indexes.base.Index,
        name: None,
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(self, /, data: geopandas.array.GeometryArray, index: None, name: None):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: geopandas.array.GeometryArray,
        index: pandas.core.indexes.range.RangeIndex,
        name: None,
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: geopandas.array.GeometryArray,
        index: pandas.core.indexes.numeric.Int64Index,
        dtype: geopandas.array.GeometryDtype,
        name: None,
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: geopandas.array.GeometryArray,
        index: pandas.core.indexes.numeric.Int64Index,
        name: None,
        fastpath: bool,
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: pandas.core.internals.managers.SingleBlockManager,
        index: None,
        name: Literal["myshapes"],
        fastpath: bool,
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: geopandas.array.GeometryArray,
        index: pandas.core.indexes.numeric.Int64Index,
        name: Literal["myshapes"],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: geopandas.array.GeometryArray,
        index: pandas.core.indexes.multi.MultiIndex,
        name: Literal["myshapes"],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: geopandas.array.GeometryArray,
        index: pandas.core.indexes.numeric.Int64Index,
        name: None,
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: geopandas.array.GeometryArray,
        index: pandas.core.indexes.range.RangeIndex,
        name: Literal["my_geom"],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: geopandas.array.GeometryArray,
        index: pandas.core.indexes.multi.MultiIndex,
        name: None,
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: geopandas.array.GeometryArray,
        index: pandas.core.indexes.base.Index,
        name: Literal["foo"],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: geopandas.array.GeometryArray,
        index: pandas.core.indexes.numeric.Int64Index,
        dtype: geopandas.array.GeometryDtype,
        name: Literal["geometry"],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: geopandas.array.GeometryArray,
        index: pandas.core.indexes.numeric.Int64Index,
        name: Literal["tt"],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: pandas.core.internals.managers.SingleBlockManager,
        index: None,
        name: Literal["geometry"],
        fastpath: bool,
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: geopandas.array.GeometryArray,
        index: pandas.core.indexes.numeric.Int64Index,
        name: Literal["geometry"],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: pandas.core.internals.managers.SingleBlockManager,
        index: None,
        name: None,
        fastpath: bool,
    ):
        """
        usage.geopandas: 1
        """
        ...

    def __init__(
        self,
        /,
        data: Union[
            pandas.core.internals.managers.SingleBlockManager,
            geopandas.geoseries.GeoSeries,
            geopandas.array.GeometryArray,
        ],
        index: Union[
            None,
            pandas.core.indexes.multi.MultiIndex,
            pandas.core.indexes.range.RangeIndex,
            pandas.core.indexes.base.Index,
            pandas.core.indexes.numeric.Int64Index,
        ],
        dtype: geopandas.array.GeometryDtype = ...,
        name: Union[None, str] = ...,
        fastpath: bool = ...,
    ):
        """
        usage.geopandas: 21
        """
        ...

    @overload
    def align(self, /, other: geopandas.geoseries.GeoSeries):
        """
        usage.geopandas: 5
        """
        ...

    @overload
    def align(self, /, other: pandas.core.series.Series):
        """
        usage.geopandas: 1
        """
        ...

    def align(
        self, /, other: Union[pandas.core.series.Series, geopandas.geoseries.GeoSeries]
    ):
        """
        usage.geopandas: 6
        """
        ...

    def all(self, /):
        """
        usage.geopandas: 3
        """
        ...

    def any(self, /):
        """
        usage.geopandas: 3
        """
        ...

    def apply(self, /, func: Callable, args: Tuple[None, ...]):
        """
        usage.geopandas: 4
        """
        ...

    @overload
    def astype(self, /, dtype: Type[int]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def astype(self, /, dtype: Type[str]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def astype(self, /, dtype: Type[object]):
        """
        usage.geopandas: 1
        """
        ...

    def astype(self, /, dtype: type):
        """
        usage.geopandas: 3
        """
        ...

    def copy(self, /):
        """
        usage.geopandas: 17
        """
        ...

    def drop_duplicates(self, /):
        """
        usage.geopandas: 1
        """
        ...

    def dropna(self, /):
        """
        usage.geopandas: 3
        """
        ...

    @overload
    def fillna(
        self, /, value: shapely.geometry.base.BaseGeometry, method: None, inplace: bool
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def fillna(
        self, /, value: shapely.geometry.point.Point, method: None, inplace: bool
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def fillna(self, /, value: float, method: None, inplace: bool):
        """
        usage.geopandas: 1
        """
        ...

    def fillna(
        self,
        /,
        value: Union[
            float, shapely.geometry.base.BaseGeometry, shapely.geometry.point.Point
        ],
        method: None,
        inplace: bool,
    ):
        """
        usage.geopandas: 3
        """
        ...

    def groupby(self, /, by: Callable):
        """
        usage.geopandas: 1
        """
        ...

    def head(self, /):
        """
        usage.geopandas: 1
        """
        ...

    def idxmax(self, /):
        """
        usage.geopandas: 1
        """
        ...

    def isna(self, /):
        """
        usage.geopandas: 1
        """
        ...

    def iteritems(self, /):
        """
        usage.geopandas: 1
        """
        ...

    def max(self, /):
        """
        usage.geopandas: 1
        """
        ...

    def notna(self, /):
        """
        usage.geopandas: 1
        """
        ...

    def reindex(self, /, index: List[int]):
        """
        usage.geopandas: 2
        """
        ...

    @overload
    def reset_index(self, /, level: int):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def reset_index(self, /):
        """
        usage.geopandas: 1
        """
        ...

    def reset_index(self, /, level: int = ...):
        """
        usage.geopandas: 2
        """
        ...

    def sort_index(self, /):
        """
        usage.geopandas: 1
        """
        ...

    def sum(self, /):
        """
        usage.geopandas: 1
        """
        ...

    def tail(self, /):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def take(self, /, indices: numpy.ndarray, axis: int):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def take(self, /, indices: numpy.ndarray):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def take(self, /, indices: List[int]):
        """
        usage.geopandas: 1
        """
        ...

    def take(self, /, indices: Union[List[int], numpy.ndarray], axis: int = ...):
        """
        usage.geopandas: 3
        """
        ...

    def tolist(self, /):
        """
        usage.geopandas: 1
        """
        ...

    def unique(self, /):
        """
        usage.geopandas: 1
        """
        ...

    def value_counts(self, /):
        """
        usage.geopandas: 1
        """
        ...

    def where(self, /, cond: numpy.ndarray):
        """
        usage.geopandas: 1
        """
        ...
