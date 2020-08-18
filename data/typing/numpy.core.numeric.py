from typing import *


@overload
def normalize_axis_tuple(axis: int, ndim: int, argname: Literal["source"]):
    """
    usage.dask: 1
    """
    ...


@overload
def normalize_axis_tuple(axis: int, ndim: int, argname: Literal["destination"]):
    """
    usage.dask: 1
    """
    ...


def normalize_axis_tuple(
    axis: int, ndim: int, argname: Literal["destination", "source"]
):
    """
    usage.dask: 2
    """
    ...
