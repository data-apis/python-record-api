from typing import *


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


def average(a: numpy.ma.core.MaskedArray, weights: Union[None, numpy.ndarray]):
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


def masked_all(shape: Union[Tuple[int, ...], int]):
    """
    usage.matplotlib: 1
    usage.pandas: 14
    usage.scipy: 3
    """
    ...


def median(a: Union[numpy.ma.core.MaskedArray, numpy.ndarray], axis: Union[int, None]):
    """
    usage.scipy: 2
    usage.sklearn: 1
    """
    ...
