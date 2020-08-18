from typing import *


@overload
def as_strided(x: numpy.ndarray, shape: Tuple[int, int], strides: Tuple[int, int]):
    """
    usage.matplotlib: 5
    usage.scipy: 13
    usage.skimage: 1
    """
    ...


@overload
def as_strided(
    x: numpy.ndarray, shape: Tuple[int, int, int], strides: Tuple[int, int, int]
):
    """
    usage.skimage: 1
    """
    ...


@overload
def as_strided(x: numpy.ndarray, shape: Tuple[int], strides: Tuple[int]):
    """
    usage.skimage: 1
    """
    ...


@overload
def as_strided(
    x: numpy.ndarray,
    shape: Tuple[numpy.int64, numpy.int64, numpy.int64, numpy.int64],
    strides: Tuple[numpy.int64, numpy.int64, int, int],
):
    """
    usage.skimage: 3
    """
    ...


@overload
def as_strided(
    x: numpy.ndarray,
    shape: Tuple[numpy.int64, numpy.int64, numpy.int64, numpy.int64],
    strides: Tuple[int, int, numpy.int64, numpy.int64],
):
    """
    usage.skimage: 2
    """
    ...


@overload
def as_strided(
    x: numpy.ndarray,
    shape: Tuple[numpy.int64, numpy.int64],
    strides: Tuple[numpy.int64, int],
):
    """
    usage.skimage: 1
    """
    ...


@overload
def as_strided(
    x: numpy.ndarray,
    shape: Tuple[
        numpy.int64, numpy.int64, numpy.int64, numpy.int64, numpy.int64, numpy.int64
    ],
    strides: Tuple[numpy.int64, numpy.int64, numpy.int64, int, int, int],
):
    """
    usage.skimage: 1
    """
    ...


@overload
def as_strided(
    x: numpy.ndarray,
    shape: Tuple[numpy.int64, numpy.int64],
    strides: Tuple[int, numpy.int64],
):
    """
    usage.skimage: 1
    """
    ...


@overload
def as_strided(
    x: numpy.ndarray,
    shape: Tuple[int, int, int, int],
    strides: Tuple[int, int, int, int],
    writeable: bool,
):
    """
    usage.xarray: 2
    """
    ...


@overload
def as_strided(
    x: numpy.ndarray, shape: Tuple[int, int], strides: Tuple[int, int], writeable: bool
):
    """
    usage.xarray: 4
    """
    ...


@overload
def as_strided(
    x: numpy.ndarray,
    shape: Tuple[int, int, int],
    strides: Tuple[int, int, int],
    writeable: bool,
):
    """
    usage.xarray: 2
    """
    ...


@overload
def as_strided(
    x: object,
    shape: Tuple[int, int, int],
    strides: Tuple[int, int, int],
    writeable: bool,
):
    """
    usage.xarray: 1
    """
    ...


@overload
def as_strided(
    x: object,
    shape: Tuple[int, int, int, int],
    strides: Tuple[int, int, int, int],
    writeable: bool,
):
    """
    usage.xarray: 1
    """
    ...


@overload
def as_strided(x: numpy.ndarray, shape: Tuple[int, ...], strides: Tuple[int, ...]):
    """
    usage.pandas: 3
    """
    ...


@overload
def as_strided(x: numpy.ndarray, shape: Tuple[int]):
    """
    usage.scipy: 1
    """
    ...


@overload
def as_strided(x: numpy.ndarray, shape: Tuple[int, int, int], strides: List[int]):
    """
    usage.scipy: 7
    """
    ...


@overload
def as_strided(
    x: numpy.ndarray,
    shape: Tuple[int, int, int, int],
    strides: Tuple[int, int, int, int],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def as_strided(
    x: numpy.ndarray,
    shape: Tuple[numpy.int64, numpy.int64, numpy.int64, int, int, int],
    strides: Tuple[int, int, int, int, int, int],
):
    """
    usage.sklearn: 3
    """
    ...


@overload
def as_strided(
    x: numpy.ndarray, shape: Tuple[numpy.int64, int], strides: Tuple[int, int]
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def as_strided(
    x: numpy.ndarray,
    shape: Tuple[numpy.int64, numpy.int64, int, int],
    strides: Tuple[int, int, int, int],
):
    """
    usage.sklearn: 2
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
