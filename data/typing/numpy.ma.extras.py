from typing import *


@overload
def apply_along_axis(
    func1d: Callable,
    axis: int,
    arr: numpy.ma.core.MaskedArray,
    *args: Literal["v", "t"],
):
    """
    usage.scipy: 6
    """
    ...


@overload
def apply_along_axis(func1d: Callable, axis: int, arr: numpy.ma.core.MaskedArray):
    """
    usage.scipy: 3
    """
    ...


def apply_along_axis(
    func1d: Callable,
    axis: int,
    arr: numpy.ma.core.MaskedArray,
    *args: Literal["v", "t"],
):
    """
    usage.scipy: 9
    """
    ...


@overload
def average(a: numpy.ma.core.MaskedArray, axis: int, weights: numpy.ndarray):
    """
    usage.dask: 1
    usage.sklearn: 1
    """
    ...


@overload
def average(a: numpy.ma.core.MaskedArray, axis: int, weights: None):
    """
    usage.sklearn: 1
    """
    ...


@overload
def average(a: numpy.ma.core.MaskedArray, weights: numpy.ndarray):
    """
    usage.sklearn: 6
    """
    ...


def average(
    a: numpy.ma.core.MaskedArray, weights: Union[None, numpy.ndarray], axis: int = ...
):
    """
    usage.dask: 1
    usage.sklearn: 8
    """
    ...


def corrcoef(x: numpy.ndarray, rowvar: bool):
    """
    usage.scipy: 1
    """
    ...


def mask_cols(a: numpy.ma.core.MaskedArray):
    """
    usage.scipy: 1
    """
    ...


@overload
def masked_all(shape: Tuple[int, ...], dtype: Union[Literal["M8[ns]"], type] = ...):
    """
    usage.pandas: 14
    """
    ...


@overload
def masked_all(shape: int):
    """
    usage.scipy: 3
    """
    ...


@overload
def masked_all(shape: Tuple[int, int]):
    """
    usage.matplotlib: 1
    """
    ...


def masked_all(
    shape: Union[Tuple[int, ...], int], dtype: Union[Literal["M8[ns]"], type] = ...
):
    """
    usage.matplotlib: 1
    usage.pandas: 14
    usage.scipy: 3
    """
    ...


@overload
def median(a: numpy.ndarray, axis: None):
    """
    usage.scipy: 2
    """
    ...


@overload
def median(a: numpy.ma.core.MaskedArray, axis: int):
    """
    usage.sklearn: 1
    """
    ...


def median(a: Union[numpy.ma.core.MaskedArray, numpy.ndarray], axis: Union[int, None]):
    """
    usage.scipy: 2
    usage.sklearn: 1
    """
    ...
