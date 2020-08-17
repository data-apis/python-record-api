from typing import *


def isna(obj: object):
    """
    usage.dask: 116
    usage.xarray: 45
    """
    ...


@overload
def notna(obj: numpy.ndarray):
    """
    usage.xarray: 3
    """
    ...


@overload
def notna(obj: pandas.core.indexes.numeric.Int64Index):
    """
    usage.dask: 2
    """
    ...


def notna(obj: Union[pandas.core.indexes.numeric.Int64Index, numpy.ndarray]):
    """
    usage.dask: 2
    usage.xarray: 3
    """
    ...
