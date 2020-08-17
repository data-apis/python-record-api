from typing import *


@overload
def as_strided(
    x: numpy.ndarray,
    shape: Tuple[Union[numpy.int64, int], ...],
    strides: Tuple[Union[numpy.int64, int], ...],
):
    """
    usage.skimage: 11
    """
    ...


@overload
def as_strided(
    x: object, shape: Tuple[int, ...], strides: Tuple[int, ...], writeable: bool
):
    """
    usage.xarray: 10
    """
    ...


@overload
def as_strided(x: numpy.ndarray, shape: Tuple[int, ...], strides: Tuple[int, ...]):
    """
    usage.pandas: 3
    """
    ...


@overload
def as_strided(
    x: numpy.ndarray,
    shape: Tuple[int, ...],
    strides: Union[Tuple[int, ...], List[int]] = ...,
):
    """
    usage.scipy: 22
    """
    ...


@overload
def as_strided(x: numpy.ndarray, shape: Tuple[int, int], strides: Tuple[int, int]):
    """
    usage.matplotlib: 5
    """
    ...


@overload
def as_strided(
    x: numpy.ndarray,
    shape: Tuple[Union[int, numpy.int64], ...],
    strides: Tuple[int, ...],
):
    """
    usage.sklearn: 6
    """
    ...


def as_strided(
    x: object,
    shape: Tuple[Union[int, numpy.int64], ...],
    writeable: bool = ...,
    strides: Union[Tuple[Union[int, numpy.int64], ...], List[int]] = ...,
):
    """
    usage.matplotlib: 5
    usage.pandas: 3
    usage.scipy: 22
    usage.skimage: 11
    usage.sklearn: 6
    usage.xarray: 10
    """
    ...


class DummyArray:

    # usage.matplotlib: 2
    base: object
