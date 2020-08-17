from typing import *

# usage.dask: 1
__name__: object


@overload
def fft(a: pandas.core.series.Series):
    """
    usage.pandas: 1
    """
    ...


@overload
def fft(a: Union[numpy.ndarray, List[float]], n: int = ..., axis: int = ...):
    """
    usage.scipy: 34
    """
    ...


@overload
def fft(a: numpy.ndarray, n: int = ..., axis: int = ...):
    """
    usage.matplotlib: 8
    """
    ...


@overload
def fft(
    _0: numpy.ndarray = ...,
    /,
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


def fft(
    _0: numpy.ndarray = ...,
    /,
    a: Union[
        dask.array.core.Array, numpy.ndarray, pandas.core.series.Series, List[float]
    ] = ...,
    n: Union[None, int] = ...,
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


@overload
def fftfreq(n: int, d: numpy.ndarray):
    """
    usage.skimage: 1
    """
    ...


@overload
def fftfreq(n: int):
    """
    usage.skimage: 1
    """
    ...


@overload
def fftfreq(n: int, d: float = ...):
    """
    usage.scipy: 29
    """
    ...


@overload
def fftfreq(n: int, d: float):
    """
    usage.dask: 1
    usage.matplotlib: 1
    """
    ...


def fftfreq(n: int, d: Union[float, numpy.ndarray] = ...):
    """
    usage.dask: 1
    usage.matplotlib: 1
    usage.scipy: 29
    usage.skimage: 2
    """
    ...


@overload
def fftn(a: numpy.ndarray, s: Tuple[int, int], axes: Tuple[int, int]):
    """
    usage.scipy: 4
    """
    ...


@overload
def fftn(
    a: numpy.ndarray, s: Union[Tuple[int, int], None] = ..., axes: Tuple[int, ...] = ...
):
    """
    usage.dask: 33
    """
    ...


def fftn(
    a: numpy.ndarray, s: Union[None, Tuple[int, int]] = ..., axes: Tuple[int, ...] = ...
):
    """
    usage.dask: 33
    usage.scipy: 4
    """
    ...


@overload
def fftshift(x: numpy.ndarray):
    """
    usage.skimage: 3
    """
    ...


@overload
def fftshift(x: Union[numpy.ndarray, List[int]]):
    """
    usage.scipy: 3
    """
    ...


@overload
def fftshift(x: numpy.ndarray, axes: Union[Tuple[int, ...], int, None]):
    """
    usage.dask: 4
    """
    ...


def fftshift(
    x: Union[numpy.ndarray, List[int]], axes: Union[Tuple[int, ...], int, None] = ...
):
    """
    usage.dask: 4
    usage.scipy: 3
    usage.skimage: 3
    """
    ...


def hfft(
    _0: numpy.ndarray = ...,
    /,
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


@overload
def ifft(a: Union[numpy.ndarray, List[float]], n: int = ..., axis: int = ...):
    """
    usage.scipy: 23
    """
    ...


@overload
def ifft(
    _0: numpy.ndarray = ...,
    /,
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


def ifft(
    _0: numpy.ndarray = ...,
    /,
    a: Union[numpy.ndarray, List[float]] = ...,
    n: Union[None, int] = ...,
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


@overload
def ifftshift(x: Union[numpy.ndarray, List[int]]):
    """
    usage.scipy: 4
    """
    ...


@overload
def ifftshift(x: numpy.ndarray, axes: Union[Tuple[int, ...], int, None]):
    """
    usage.dask: 4
    """
    ...


def ifftshift(
    x: Union[numpy.ndarray, List[int]], axes: Union[Tuple[int, ...], int, None] = ...
):
    """
    usage.dask: 4
    usage.scipy: 4
    """
    ...


def ihfft(
    _0: numpy.ndarray = ...,
    /,
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


@overload
def irfft(a: numpy.ndarray, n: int = ..., axis: int = ...):
    """
    usage.scipy: 6
    """
    ...


@overload
def irfft(
    _0: numpy.ndarray = ...,
    /,
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
    _0: numpy.ndarray = ...,
    /,
    a: numpy.ndarray = ...,
    n: Union[None, int] = ...,
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


@overload
def rfft(a: pandas.core.series.Series):
    """
    usage.pandas: 1
    """
    ...


@overload
def rfft(a: numpy.ndarray, n: int = ..., axis: int = ...):
    """
    usage.scipy: 9
    """
    ...


@overload
def rfft(
    _0: numpy.ndarray = ...,
    /,
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


def rfft(
    _0: numpy.ndarray = ...,
    /,
    a: Union[numpy.ndarray, pandas.core.series.Series] = ...,
    n: Union[None, int] = ...,
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
