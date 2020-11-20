from typing import *


@overload
def cut(x: pandas.core.series.Series, bins: int, labels: bool):
    """
    usage.alphalens: 3
    """
    ...


@overload
def cut(x: pandas.core.series.Series, bins: List[int], labels: bool):
    """
    usage.alphalens: 2
    """
    ...


@overload
def cut(x: pandas.core.series.Series, bins: List[float], labels: bool):
    """
    usage.alphalens: 2
    """
    ...


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


@overload
def cut(x: pandas.core.series.Series, bins: int):
    """
    usage.pyjanitor: 1
    """
    ...


def cut(
    x: object,
    bins: Union[
        int, range, pandas.core.indexes.datetimes.DatetimeIndex, List[Union[float, int]]
    ],
    right: bool = ...,
    labels: Union[None, bool] = ...,
    precision: int = ...,
    include_lowest: bool = ...,
):
    """
    usage.alphalens: 7
    usage.pyjanitor: 1
    usage.xarray: 14
    """
    ...


@overload
def qcut(x: pandas.core.series.Series, q: int, labels: bool):
    """
    usage.alphalens: 3
    """
    ...


@overload
def qcut(x: pandas.core.series.Series, q: List[Union[float, int]], labels: bool):
    """
    usage.alphalens: 4
    """
    ...


@overload
def qcut(x: pandas.core.series.Series, q: List[float], labels: bool):
    """
    usage.alphalens: 2
    """
    ...


def qcut(
    x: pandas.core.series.Series, q: Union[List[Union[float, int]], int], labels: bool
):
    """
    usage.alphalens: 9
    """
    ...
