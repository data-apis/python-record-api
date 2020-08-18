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
def fft(a: List[float]):
    """
    usage.scipy: 3
    """
    ...


@overload
def fft(a: numpy.ndarray):
    """
    usage.dask: 11
    usage.matplotlib: 3
    usage.scipy: 6
    """
    ...


@overload
def fft(a: numpy.ndarray, axis: int):
    """
    usage.dask: 8
    usage.scipy: 6
    """
    ...


@overload
def fft(a: numpy.ndarray, n: int, axis: int):
    """
    usage.dask: 8
    usage.matplotlib: 5
    usage.scipy: 16
    """
    ...


@overload
def fft(a: numpy.ndarray, n: int):
    """
    usage.dask: 6
    usage.scipy: 3
    """
    ...


@overload
def fft(a: dask.array.core.Array):
    """
    usage.dask: 1
    """
    ...


@overload
def fft(_0: numpy.ndarray, /, *, axes: Tuple[int]):
    """
    usage.dask: 3
    """
    ...


@overload
def fft(a: numpy.ndarray, n: None, axis: int):
    """
    usage.dask: 3
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


@overload
def fft2(a: numpy.ndarray):
    """
    usage.dask: 8
    """
    ...


@overload
def fft2(a: dask.array.core.Array):
    """
    usage.dask: 1
    """
    ...


@overload
def fft2(a: numpy.ndarray, axes: Tuple[int, int]):
    """
    usage.dask: 9
    """
    ...


@overload
def fft2(a: numpy.ndarray, s: None, axes: Tuple[int, int]):
    """
    usage.dask: 3
    """
    ...


@overload
def fft2(a: numpy.ndarray, s: Tuple[int, int], axes: Tuple[int, int]):
    """
    usage.dask: 7
    """
    ...


@overload
def fft2(a: numpy.ndarray, s: Tuple[int, int]):
    """
    usage.dask: 1
    """
    ...


@overload
def fft2(a: numpy.ndarray, axes: Tuple[int]):
    """
    usage.dask: 4
    """
    ...


@overload
def fft2(a: numpy.ndarray, s: None, axes: Tuple[int]):
    """
    usage.dask: 2
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
    usage.scipy: 7
    usage.skimage: 1
    """
    ...


@overload
def fftfreq(n: int, d: float):
    """
    usage.dask: 1
    usage.matplotlib: 1
    usage.scipy: 22
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
    usage.dask: 7
    usage.scipy: 4
    """
    ...


@overload
def fftn(a: numpy.ndarray, axes: Tuple[int, int]):
    """
    usage.dask: 9
    """
    ...


@overload
def fftn(a: numpy.ndarray, s: None, axes: Tuple[int, int]):
    """
    usage.dask: 3
    """
    ...


@overload
def fftn(a: numpy.ndarray):
    """
    usage.dask: 7
    """
    ...


@overload
def fftn(a: numpy.ndarray, s: Tuple[int, int]):
    """
    usage.dask: 1
    """
    ...


@overload
def fftn(a: numpy.ndarray, axes: Tuple[int]):
    """
    usage.dask: 4
    """
    ...


@overload
def fftn(a: numpy.ndarray, s: None, axes: Tuple[int]):
    """
    usage.dask: 2
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
    usage.scipy: 1
    usage.skimage: 3
    """
    ...


@overload
def fftshift(x: List[int]):
    """
    usage.scipy: 2
    """
    ...


@overload
def fftshift(x: numpy.ndarray, axes: None):
    """
    usage.dask: 1
    """
    ...


@overload
def fftshift(x: numpy.ndarray, axes: int):
    """
    usage.dask: 1
    """
    ...


@overload
def fftshift(x: numpy.ndarray, axes: Tuple[int, int]):
    """
    usage.dask: 1
    """
    ...


@overload
def fftshift(x: numpy.ndarray, axes: Tuple[int, int, int]):
    """
    usage.dask: 1
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


@overload
def hfft(_0: numpy.ndarray, /, *, axes: Tuple[int]):
    """
    usage.dask: 3
    """
    ...


@overload
def hfft(a: numpy.ndarray):
    """
    usage.dask: 10
    """
    ...


@overload
def hfft(a: numpy.ndarray, n: None, axis: int):
    """
    usage.dask: 3
    """
    ...


@overload
def hfft(a: numpy.ndarray, n: int, axis: int):
    """
    usage.dask: 8
    """
    ...


@overload
def hfft(a: numpy.ndarray, n: int):
    """
    usage.dask: 6
    """
    ...


@overload
def hfft(a: numpy.ndarray, axis: int):
    """
    usage.dask: 5
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
def ifft(a: List[float]):
    """
    usage.scipy: 3
    """
    ...


@overload
def ifft(a: numpy.ndarray):
    """
    usage.dask: 10
    usage.scipy: 7
    """
    ...


@overload
def ifft(a: numpy.ndarray, axis: int):
    """
    usage.dask: 6
    usage.scipy: 1
    """
    ...


@overload
def ifft(a: numpy.ndarray, n: int, axis: int):
    """
    usage.dask: 8
    usage.scipy: 12
    """
    ...


@overload
def ifft(_0: numpy.ndarray, /, *, axes: Tuple[int]):
    """
    usage.dask: 3
    """
    ...


@overload
def ifft(a: numpy.ndarray, n: None, axis: int):
    """
    usage.dask: 3
    """
    ...


@overload
def ifft(a: numpy.ndarray, n: int):
    """
    usage.dask: 6
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


@overload
def ifft2(a: numpy.ndarray, axes: Tuple[int, int]):
    """
    usage.dask: 9
    """
    ...


@overload
def ifft2(a: numpy.ndarray, s: None, axes: Tuple[int, int]):
    """
    usage.dask: 3
    """
    ...


@overload
def ifft2(a: numpy.ndarray):
    """
    usage.dask: 7
    """
    ...


@overload
def ifft2(a: numpy.ndarray, s: Tuple[int, int], axes: Tuple[int, int]):
    """
    usage.dask: 7
    """
    ...


@overload
def ifft2(a: numpy.ndarray, s: Tuple[int, int]):
    """
    usage.dask: 1
    """
    ...


@overload
def ifft2(a: numpy.ndarray, axes: Tuple[int]):
    """
    usage.dask: 4
    """
    ...


@overload
def ifft2(a: numpy.ndarray, s: None, axes: Tuple[int]):
    """
    usage.dask: 2
    """
    ...


def ifft2(
    a: numpy.ndarray, s: Union[Tuple[int, int], None] = ..., axes: Tuple[int, ...] = ...
):
    """
    usage.dask: 33
    """
    ...


@overload
def ifftn(a: numpy.ndarray, axes: Tuple[int, int]):
    """
    usage.dask: 9
    """
    ...


@overload
def ifftn(a: numpy.ndarray, s: None, axes: Tuple[int, int]):
    """
    usage.dask: 3
    """
    ...


@overload
def ifftn(a: numpy.ndarray):
    """
    usage.dask: 7
    """
    ...


@overload
def ifftn(a: numpy.ndarray, s: Tuple[int, int], axes: Tuple[int, int]):
    """
    usage.dask: 7
    """
    ...


@overload
def ifftn(a: numpy.ndarray, s: Tuple[int, int]):
    """
    usage.dask: 1
    """
    ...


@overload
def ifftn(a: numpy.ndarray, axes: Tuple[int]):
    """
    usage.dask: 4
    """
    ...


@overload
def ifftn(a: numpy.ndarray, s: None, axes: Tuple[int]):
    """
    usage.dask: 2
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
def ifftshift(x: List[int]):
    """
    usage.scipy: 2
    """
    ...


@overload
def ifftshift(x: numpy.ndarray):
    """
    usage.scipy: 2
    """
    ...


@overload
def ifftshift(x: numpy.ndarray, axes: None):
    """
    usage.dask: 1
    """
    ...


@overload
def ifftshift(x: numpy.ndarray, axes: int):
    """
    usage.dask: 1
    """
    ...


@overload
def ifftshift(x: numpy.ndarray, axes: Tuple[int, int]):
    """
    usage.dask: 1
    """
    ...


@overload
def ifftshift(x: numpy.ndarray, axes: Tuple[int, int, int]):
    """
    usage.dask: 1
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


@overload
def ihfft(_0: numpy.ndarray, /, *, axes: Tuple[int]):
    """
    usage.dask: 3
    """
    ...


@overload
def ihfft(a: numpy.ndarray):
    """
    usage.dask: 10
    """
    ...


@overload
def ihfft(a: numpy.ndarray, n: None, axis: int):
    """
    usage.dask: 3
    """
    ...


@overload
def ihfft(a: numpy.ndarray, n: int, axis: int):
    """
    usage.dask: 8
    """
    ...


@overload
def ihfft(a: numpy.ndarray, n: int):
    """
    usage.dask: 6
    """
    ...


@overload
def ihfft(a: numpy.ndarray, axis: int):
    """
    usage.dask: 5
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
def irfft(a: numpy.ndarray):
    """
    usage.dask: 10
    usage.scipy: 2
    """
    ...


@overload
def irfft(a: numpy.ndarray, n: int, axis: int):
    """
    usage.dask: 8
    usage.scipy: 4
    """
    ...


@overload
def irfft(_0: numpy.ndarray, /, *, axes: Tuple[int]):
    """
    usage.dask: 3
    """
    ...


@overload
def irfft(a: numpy.ndarray, n: None, axis: int):
    """
    usage.dask: 3
    """
    ...


@overload
def irfft(a: numpy.ndarray, n: int):
    """
    usage.dask: 6
    """
    ...


@overload
def irfft(a: numpy.ndarray, axis: int):
    """
    usage.dask: 5
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


@overload
def irfft2(a: numpy.ndarray, axes: Tuple[int, int]):
    """
    usage.dask: 9
    """
    ...


@overload
def irfft2(a: numpy.ndarray, s: None, axes: Tuple[int, int]):
    """
    usage.dask: 3
    """
    ...


@overload
def irfft2(a: numpy.ndarray):
    """
    usage.dask: 7
    """
    ...


@overload
def irfft2(a: numpy.ndarray, s: Tuple[int, int], axes: Tuple[int, int]):
    """
    usage.dask: 7
    """
    ...


@overload
def irfft2(a: numpy.ndarray, s: Tuple[int, int]):
    """
    usage.dask: 1
    """
    ...


@overload
def irfft2(a: numpy.ndarray, axes: Tuple[int]):
    """
    usage.dask: 4
    """
    ...


@overload
def irfft2(a: numpy.ndarray, s: None, axes: Tuple[int]):
    """
    usage.dask: 2
    """
    ...


def irfft2(
    a: numpy.ndarray, s: Union[Tuple[int, int], None] = ..., axes: Tuple[int, ...] = ...
):
    """
    usage.dask: 33
    """
    ...


@overload
def irfftn(a: numpy.ndarray, axes: Tuple[int, int]):
    """
    usage.dask: 9
    """
    ...


@overload
def irfftn(a: numpy.ndarray, s: None, axes: Tuple[int, int]):
    """
    usage.dask: 3
    """
    ...


@overload
def irfftn(a: numpy.ndarray):
    """
    usage.dask: 7
    """
    ...


@overload
def irfftn(a: numpy.ndarray, s: Tuple[int, int], axes: Tuple[int, int]):
    """
    usage.dask: 7
    """
    ...


@overload
def irfftn(a: numpy.ndarray, s: Tuple[int, int]):
    """
    usage.dask: 1
    """
    ...


@overload
def irfftn(a: numpy.ndarray, axes: Tuple[int]):
    """
    usage.dask: 4
    """
    ...


@overload
def irfftn(a: numpy.ndarray, s: None, axes: Tuple[int]):
    """
    usage.dask: 2
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
def rfft(a: numpy.ndarray):
    """
    usage.dask: 10
    usage.scipy: 1
    """
    ...


@overload
def rfft(a: numpy.ndarray, n: int, axis: int):
    """
    usage.dask: 8
    usage.scipy: 8
    """
    ...


@overload
def rfft(_0: numpy.ndarray, /, *, axes: Tuple[int]):
    """
    usage.dask: 3
    """
    ...


@overload
def rfft(a: numpy.ndarray, n: None, axis: int):
    """
    usage.dask: 3
    """
    ...


@overload
def rfft(a: numpy.ndarray, n: int):
    """
    usage.dask: 6
    """
    ...


@overload
def rfft(a: numpy.ndarray, axis: int):
    """
    usage.dask: 5
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


@overload
def rfft2(a: numpy.ndarray, axes: Tuple[int, int]):
    """
    usage.dask: 9
    """
    ...


@overload
def rfft2(a: numpy.ndarray, s: None, axes: Tuple[int, int]):
    """
    usage.dask: 3
    """
    ...


@overload
def rfft2(a: numpy.ndarray):
    """
    usage.dask: 7
    """
    ...


@overload
def rfft2(a: numpy.ndarray, s: Tuple[int, int], axes: Tuple[int, int]):
    """
    usage.dask: 7
    """
    ...


@overload
def rfft2(a: numpy.ndarray, s: Tuple[int, int]):
    """
    usage.dask: 1
    """
    ...


@overload
def rfft2(a: numpy.ndarray, axes: Tuple[int]):
    """
    usage.dask: 4
    """
    ...


@overload
def rfft2(a: numpy.ndarray, s: None, axes: Tuple[int]):
    """
    usage.dask: 2
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


@overload
def rfftn(a: numpy.ndarray, axes: Tuple[int, int]):
    """
    usage.dask: 9
    """
    ...


@overload
def rfftn(a: numpy.ndarray, s: None, axes: Tuple[int, int]):
    """
    usage.dask: 3
    """
    ...


@overload
def rfftn(a: numpy.ndarray):
    """
    usage.dask: 7
    """
    ...


@overload
def rfftn(a: numpy.ndarray, s: Tuple[int, int], axes: Tuple[int, int]):
    """
    usage.dask: 7
    """
    ...


@overload
def rfftn(a: numpy.ndarray, s: Tuple[int, int]):
    """
    usage.dask: 1
    """
    ...


@overload
def rfftn(a: numpy.ndarray, axes: Tuple[int]):
    """
    usage.dask: 4
    """
    ...


@overload
def rfftn(a: numpy.ndarray, s: None, axes: Tuple[int]):
    """
    usage.dask: 2
    """
    ...


def rfftn(
    a: numpy.ndarray, s: Union[Tuple[int, int], None] = ..., axes: Tuple[int, ...] = ...
):
    """
    usage.dask: 33
    """
    ...
