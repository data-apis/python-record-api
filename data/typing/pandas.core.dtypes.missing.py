from typing import *


@overload
def isna(obj: None):
    """
    usage.xarray: 1
    """
    ...


@overload
def isna(obj: numpy.float64):
    """
    usage.xarray: 3
    """
    ...


@overload
def isna(obj: numpy.ndarray):
    """
    usage.xarray: 22
    """
    ...


@overload
def isna(obj: numpy.float32):
    """
    usage.xarray: 1
    """
    ...


@overload
def isna(obj: numpy.bytes_):
    """
    usage.xarray: 2
    """
    ...


@overload
def isna(obj: bytes):
    """
    usage.xarray: 1
    """
    ...


@overload
def isna(obj: numpy.int8):
    """
    usage.xarray: 2
    """
    ...


@overload
def isna(obj: numpy.uint8):
    """
    usage.xarray: 1
    """
    ...


@overload
def isna(obj: numpy.int16):
    """
    usage.xarray: 2
    """
    ...


@overload
def isna(obj: Literal["XXX"]):
    """
    usage.xarray: 1
    """
    ...


@overload
def isna(obj: Literal[""]):
    """
    usage.xarray: 1
    """
    ...


@overload
def isna(obj: numpy.int32):
    """
    usage.xarray: 1
    """
    ...


@overload
def isna(obj: numpy.int64):
    """
    usage.xarray: 2
    """
    ...


@overload
def isna(obj: numpy.timedelta64):
    """
    usage.xarray: 1
    """
    ...


@overload
def isna(obj: sparse._coo.core.COO):
    """
    usage.xarray: 1
    """
    ...


@overload
def isna(obj: Literal["Z"]):
    """
    usage.xarray: 1
    """
    ...


@overload
def isna(obj: Literal["A"]):
    """
    usage.xarray: 1
    """
    ...


@overload
def isna(obj: object):
    """
    usage.dask: 116
    """
    ...


def isna(obj: object):
    """
    usage.dask: 116
    usage.xarray: 44
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
