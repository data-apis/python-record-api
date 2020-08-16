from typing import *

# usage.dask: 1
__name__: object


def fft(
    a: Union[dask.array.core.Array, numpy.ndarray, pandas.core.series.Series] = ...,
    n: Union[None, int] = ...,
    axis: int = ...,
    *,
    axes: Tuple[int] = ...,
):
    """
    usage.dask: 40
    usage.matplotlib: 8
    usage.pandas: 1
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
    usage.dask: 1
    usage.matplotlib: 1
    usage.skimage: 2
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
    usage.dask: 4
    usage.skimage: 3
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


def ifftshift(x: numpy.ndarray, axes: Union[Tuple[int, ...], int, None]):
    """
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
    a: Union[numpy.ndarray, pandas.core.series.Series] = ...,
    n: Union[int, None] = ...,
    axis: int = ...,
    *,
    axes: Tuple[int] = ...,
):
    """
    usage.dask: 35
    usage.pandas: 1
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
