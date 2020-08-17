from typing import *

# usage.dask: 1
__name__: object


def fft(
    a: Union[
        List[float], numpy.ndarray, dask.array.core.Array, pandas.core.series.Series
    ] = ...,
    n: Union[int, None] = ...,
    axis: int = ...,
    *,
    axes: Tuple[int] = ...,
):
    """
    usage.dask: 40
    usage.matplotlib: 8
    usage.pandas: 1
    usage.scipy: 34
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
    usage.scipy: 29
    usage.skimage: 2
    """
    ...


def fftn(
    a: numpy.ndarray, s: Union[Tuple[int, int], None] = ..., axes: Tuple[int, ...] = ...
):
    """
    usage.dask: 33
    usage.scipy: 4
    """
    ...


def fftshift(x: Union[numpy.ndarray, List[int]]):
    """
    usage.dask: 4
    usage.scipy: 3
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
    a: Union[List[float], numpy.ndarray] = ...,
    n: Union[int, None] = ...,
    axis: int = ...,
    *,
    axes: Tuple[int] = ...,
):
    """
    usage.dask: 36
    usage.scipy: 23
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


def ifftshift(x: Union[List[int], numpy.ndarray]):
    """
    usage.dask: 4
    usage.scipy: 4
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
    usage.scipy: 6
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
    usage.scipy: 9
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
    usage.scipy: 1
    """
    ...


def rfftn(
    a: numpy.ndarray, s: Union[Tuple[int, int], None] = ..., axes: Tuple[int, ...] = ...
):
    """
    usage.dask: 33
    """
    ...
