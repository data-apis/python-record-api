from typing import *


@overload
def cut(x: xarray.core.dataarray.DataArray, bins: List[Union[int, float]]):
    """
    usage.xarray: 1
    """
    ...


@overload
def cut(
    x: range,
    bins: List[Union[int, float]],
    right: bool,
    labels: None,
    precision: int,
    include_lowest: bool,
):
    """
    usage.xarray: 1
    """
    ...


@overload
def cut(x: xarray.core.dataarray.DataArray, bins: List[int]):
    """
    usage.xarray: 1
    """
    ...


@overload
def cut(
    x: numpy.ndarray,
    bins: List[int],
    right: bool,
    labels: None,
    precision: int,
    include_lowest: bool,
):
    """
    usage.xarray: 3
    """
    ...


@overload
def cut(x: numpy.flatiter, bins: List[int]):
    """
    usage.xarray: 1
    """
    ...


@overload
def cut(
    x: numpy.ndarray,
    bins: int,
    right: bool,
    labels: None,
    precision: int,
    include_lowest: bool,
):
    """
    usage.xarray: 2
    """
    ...


@overload
def cut(
    x: numpy.ndarray,
    bins: List[float],
    right: bool,
    labels: None,
    precision: int,
    include_lowest: bool,
):
    """
    usage.xarray: 1
    """
    ...


@overload
def cut(
    x: numpy.ndarray,
    bins: pandas.core.indexes.datetimes.DatetimeIndex,
    right: bool,
    labels: None,
    precision: int,
    include_lowest: bool,
):
    """
    usage.xarray: 1
    """
    ...


@overload
def cut(
    x: pandas.core.indexes.datetimes.DatetimeIndex,
    bins: pandas.core.indexes.datetimes.DatetimeIndex,
):
    """
    usage.xarray: 1
    """
    ...


@overload
def cut(
    x: range,
    bins: List[int],
    right: bool,
    labels: None,
    precision: int,
    include_lowest: bool,
):
    """
    usage.xarray: 1
    """
    ...


@overload
def cut(
    x: numpy.ndarray,
    bins: range,
    right: bool,
    labels: None,
    precision: int,
    include_lowest: bool,
):
    """
    usage.xarray: 1
    """
    ...


def cut(
    x: Union[
        numpy.ndarray,
        pandas.core.indexes.datetimes.DatetimeIndex,
        xarray.core.dataarray.DataArray,
        numpy.flatiter,
        range,
    ],
    bins: Union[
        int, range, pandas.core.indexes.datetimes.DatetimeIndex, List[Union[float, int]]
    ],
    right: bool = ...,
    labels: None = ...,
    precision: int = ...,
    include_lowest: bool = ...,
):
    """
    usage.xarray: 14
    """
    ...
