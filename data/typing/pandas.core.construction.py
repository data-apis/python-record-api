from typing import *


@overload
def array(data: List[Union[float, int]], dtype: pandas.core.arrays.integer.Int64Dtype):
    """
    usage.geopandas: 2
    """
    ...


@overload
def array(data: numpy.ndarray, dtype: Literal["string"]):
    """
    usage.geopandas: 1
    """
    ...


@overload
def array(
    data: List[Union[pandas._libs.missing.NAType, Literal["a"]]],
    dtype: pandas.core.arrays.string_.StringDtype,
):
    """
    usage.dask: 1
    """
    ...


@overload
def array(data: List[Union[None, int]], dtype: pandas.core.arrays.integer.Int32Dtype):
    """
    usage.dask: 1
    """
    ...


@overload
def array(data: List[Union[None, bool]], dtype: Literal["boolean"]):
    """
    usage.dask: 4
    """
    ...


@overload
def array(
    data: List[Union[pandas._libs.missing.NAType, bool]],
    dtype: pandas.core.arrays.boolean.BooleanDtype,
):
    """
    usage.dask: 1
    """
    ...


@overload
def array(
    data: List[Union[pandas._libs.missing.NAType, bool]], dtype: Literal["boolean"]
):
    """
    usage.dask: 1
    """
    ...


@overload
def array(data: List[Union[None, int]], dtype: Literal["Int64"]):
    """
    usage.dask: 1
    """
    ...


@overload
def array(data: List[Literal["2000"]], dtype: Literal["Period[D]"]):
    """
    usage.dask: 1
    """
    ...


@overload
def array(data: List[int], dtype: Literal["Sparse[int]"]):
    """
    usage.dask: 1
    """
    ...


@overload
def array(
    data: List[pandas._libs.tslibs.timestamps.Timestamp],
    dtype: Literal["datetime64[ns]"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def array(
    data: List[pandas._libs.tslibs.timestamps.Timestamp],
    dtype: Literal["datetime64[ns, CET]"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def array(
    data: List[Literal["b", "a"]], dtype: pandas.core.dtypes.dtypes.CategoricalDtype
):
    """
    usage.dask: 1
    """
    ...


@overload
def array(data: List[Union[None, Literal["b", "a"]]], dtype: Literal["string"]):
    """
    usage.dask: 1
    """
    ...


def array(data: Union[list, numpy.ndarray], dtype: object):
    """
    usage.dask: 15
    usage.geopandas: 3
    """
    ...
