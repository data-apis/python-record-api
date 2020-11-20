from typing import *


@overload
def check_array_indexer(array: geopandas.array.GeometryArray, indexer: numpy.ndarray):
    """
    usage.geopandas: 4
    """
    ...


@overload
def check_array_indexer(
    array: geopandas.array.GeometryArray, indexer: slice[None, int, None]
):
    """
    usage.geopandas: 2
    """
    ...


@overload
def check_array_indexer(
    array: geopandas.array.GeometryArray, indexer: slice[int, int, int]
):
    """
    usage.geopandas: 2
    """
    ...


@overload
def check_array_indexer(
    array: geopandas.array.GeometryArray, indexer: slice[None, None, None]
):
    """
    usage.geopandas: 1
    """
    ...


@overload
def check_array_indexer(array: geopandas.array.GeometryArray, indexer: List[int]):
    """
    usage.geopandas: 5
    """
    ...


@overload
def check_array_indexer(
    array: geopandas.array.GeometryArray, indexer: slice[int, None, int]
):
    """
    usage.geopandas: 1
    """
    ...


@overload
def check_array_indexer(array: geopandas.array.GeometryArray, indexer: int):
    """
    usage.geopandas: 1
    """
    ...


@overload
def check_array_indexer(
    array: geopandas.array.GeometryArray, indexer: slice[int, None, int]
):
    """
    usage.geopandas: 1
    """
    ...


@overload
def check_array_indexer(
    array: geopandas.array.GeometryArray,
    indexer: slice[numpy.int64, numpy.int64, numpy.int64],
):
    """
    usage.geopandas: 1
    """
    ...


@overload
def check_array_indexer(
    array: geopandas.array.GeometryArray, indexer: slice[None, None, None]
):
    """
    usage.geopandas: 1
    """
    ...


@overload
def check_array_indexer(array: geopandas.array.GeometryArray, indexer: list):
    """
    usage.geopandas: 1
    """
    ...


@overload
def check_array_indexer(
    array: geopandas.array.GeometryArray,
    indexer: pandas.core.arrays.boolean.BooleanArray,
):
    """
    usage.geopandas: 2
    """
    ...


@overload
def check_array_indexer(
    array: geopandas.array.GeometryArray,
    indexer: pandas.core.arrays.integer.IntegerArray,
):
    """
    usage.geopandas: 2
    """
    ...


@overload
def check_array_indexer(
    array: geopandas.array.GeometryArray,
    indexer: List[Union[pandas._libs.missing.NAType, int]],
):
    """
    usage.geopandas: 2
    """
    ...


@overload
def check_array_indexer(
    array: geopandas.array.GeometryArray, indexer: slice[int, int, int]
):
    """
    usage.geopandas: 1
    """
    ...


def check_array_indexer(array: geopandas.array.GeometryArray, indexer: object):
    """
    usage.geopandas: 27
    """
    ...
