from typing import *

# usage.dask: 1
__name__: object


def fft(
    a: Union[numpy.ndarray, dask.array.core.Array] = ...,
    n: Union[int, None] = ...,
    axis: int = ...,
    *,
    axes: Tuple[int] = ...,
):
    """
    usage.dask: 40
    """
    ...


def fft2(
    a: Union[numpy.ndarray, dask.array.core.Array],
    s: Union[Tuple[int, int], None] = ...,
    axes: Tuple[int, ...] = ...,
):
    """
    usage.dask: 35
    """
    ...


def fftfreq(n: int):
    """
    usage.skimage: 2
    usage.dask: 1
    """
    ...


def fftn(
    a: numpy.ndarray, s: Union[Tuple[int, int], None] = ..., axes: Tuple[int, ...] = ...
):
    """
    usage.dask: 33
    """
    ...


def fftshift(x: numpy.ndarray):
    """
    usage.skimage: 3
    usage.dask: 4
    """
    ...


def hfft(
    a: numpy.ndarray = ...,
    n: Union[int, None] = ...,
    axis: int = ...,
    *,
    axes: Tuple[int] = ...,
):
    """
    usage.dask: 35
    """
    ...


def ifft(
    a: numpy.ndarray = ...,
    n: Union[int, None] = ...,
    axis: int = ...,
    *,
    axes: Tuple[int] = ...,
):
    """
    usage.dask: 36
    """
    ...


def ifft2(
    a: numpy.ndarray, s: Union[Tuple[int, int], None] = ..., axes: Tuple[int, ...] = ...
):
    """
    usage.dask: 33
    """
    ...


def ifftn(
    a: numpy.ndarray, s: Union[Tuple[int, int], None] = ..., axes: Tuple[int, ...] = ...
):
    """
    usage.dask: 33
    """
    ...


def ifftshift(x: numpy.ndarray):
    """
    usage.skimage: 2
    usage.dask: 4
    """
    ...


def ihfft(
    a: numpy.ndarray = ...,
    n: Union[int, None] = ...,
    axis: int = ...,
    *,
    axes: Tuple[int] = ...,
):
    """
    usage.dask: 35
    """
    ...


def irfft(
    a: numpy.ndarray = ...,
    n: Union[int, None] = ...,
    axis: int = ...,
    *,
    axes: Tuple[int] = ...,
):
    """
    usage.dask: 35
    """
    ...


def irfft2(
    a: numpy.ndarray, s: Union[Tuple[int, int], None] = ..., axes: Tuple[int, ...] = ...
):
    """
    usage.dask: 33
    """
    ...


def irfftn(
    a: numpy.ndarray, s: Union[Tuple[int, int], None] = ..., axes: Tuple[int, ...] = ...
):
    """
    usage.dask: 33
    """
    ...


def rfft(
    a: numpy.ndarray = ...,
    n: Union[int, None] = ...,
    axis: int = ...,
    *,
    axes: Tuple[int] = ...,
):
    """
    usage.dask: 35
    """
    ...


def rfft2(
    a: numpy.ndarray, s: Union[Tuple[int, int], None] = ..., axes: Tuple[int, ...] = ...
):
    """
    usage.dask: 33
    """
    ...


def rfftfreq(n: int, d: float):
    """
    usage.dask: 1
    """
    ...


def rfftn(
    a: numpy.ndarray, s: Union[Tuple[int, int], None] = ..., axes: Tuple[int, ...] = ...
):
    """
    usage.dask: 33
    """
    ...
