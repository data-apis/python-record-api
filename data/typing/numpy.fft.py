from typing import *

# usage.dask: 1
__name__: object


def ifftshift(x: numpy.ndarray):
    "\n    usage.skimage: 2\n    usage.dask: 4\n    "
    ...


def fftfreq(n: int):
    "\n    usage.skimage: 2\n    usage.dask: 1\n    "
    ...


def fftshift(x: numpy.ndarray):
    "\n    usage.skimage: 3\n    usage.dask: 4\n    "
    ...


def fft(
    a: Union[numpy.ndarray, dask.array.core.Array] = ...,
    n: Union[int, None] = ...,
    axis: int = ...,
    *,
    axes: Tuple[int] = ...,
):
    "\n    usage.dask: 40\n    "
    ...


def fft2(
    a: Union[numpy.ndarray, dask.array.core.Array],
    s: Union[Tuple[int, int], None] = ...,
    axes: Tuple[int, ...] = ...,
):
    "\n    usage.dask: 35\n    "
    ...


def ifft(
    a: numpy.ndarray = ...,
    n: Union[int, None] = ...,
    axis: int = ...,
    *,
    axes: Tuple[int] = ...,
):
    "\n    usage.dask: 36\n    "
    ...


def rfft(
    a: numpy.ndarray = ...,
    n: Union[int, None] = ...,
    axis: int = ...,
    *,
    axes: Tuple[int] = ...,
):
    "\n    usage.dask: 35\n    "
    ...


def irfft(
    a: numpy.ndarray = ...,
    n: Union[int, None] = ...,
    axis: int = ...,
    *,
    axes: Tuple[int] = ...,
):
    "\n    usage.dask: 35\n    "
    ...


def hfft(
    a: numpy.ndarray = ...,
    n: Union[int, None] = ...,
    axis: int = ...,
    *,
    axes: Tuple[int] = ...,
):
    "\n    usage.dask: 35\n    "
    ...


def ihfft(
    a: numpy.ndarray = ...,
    n: Union[int, None] = ...,
    axis: int = ...,
    *,
    axes: Tuple[int] = ...,
):
    "\n    usage.dask: 35\n    "
    ...


def ifft2(
    a: numpy.ndarray, s: Union[Tuple[int, int], None] = ..., axes: Tuple[int, ...] = ...
):
    "\n    usage.dask: 33\n    "
    ...


def fftn(
    a: numpy.ndarray, s: Union[Tuple[int, int], None] = ..., axes: Tuple[int, ...] = ...
):
    "\n    usage.dask: 33\n    "
    ...


def ifftn(
    a: numpy.ndarray, s: Union[Tuple[int, int], None] = ..., axes: Tuple[int, ...] = ...
):
    "\n    usage.dask: 33\n    "
    ...


def rfft2(
    a: numpy.ndarray, s: Union[Tuple[int, int], None] = ..., axes: Tuple[int, ...] = ...
):
    "\n    usage.dask: 33\n    "
    ...


def irfft2(
    a: numpy.ndarray, s: Union[Tuple[int, int], None] = ..., axes: Tuple[int, ...] = ...
):
    "\n    usage.dask: 33\n    "
    ...


def rfftn(
    a: numpy.ndarray, s: Union[Tuple[int, int], None] = ..., axes: Tuple[int, ...] = ...
):
    "\n    usage.dask: 33\n    "
    ...


def irfftn(
    a: numpy.ndarray, s: Union[Tuple[int, int], None] = ..., axes: Tuple[int, ...] = ...
):
    "\n    usage.dask: 33\n    "
    ...


def rfftfreq(n: int, d: float):
    "\n    usage.dask: 1\n    "
    ...
