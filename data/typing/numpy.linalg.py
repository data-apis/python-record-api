from typing import *

# usage.dask: 4
_umath_linalg: object


def svd(a: numpy.ndarray):
    "\n    usage.skimage: 7\n    usage.sklearn: 3\n    usage.dask: 5\n    "
    ...


def inv(a: numpy.ndarray):
    "\n    usage.skimage: 7\n    "
    ...


def eigvalsh(a: numpy.ndarray):
    "\n    usage.skimage: 2\n    "
    ...


def det(a: Union[dask.array.core.Array, numpy.ndarray]):
    "\n    usage.skimage: 5\n    usage.sklearn: 1\n    usage.dask: 2\n    "
    ...


def solve(a: numpy.ndarray, b: numpy.ndarray):
    "\n    usage.skimage: 2\n    "
    ...


def norm(
    x: object,
    ord: Union[None, int, float, Literal["nuc", "fro"]] = ...,
    axis: Union[None, int, Tuple[int, ...]] = ...,
    keepdims: bool = ...,
):
    "\n    usage.skimage: 8\n    usage.sklearn: 22\n    usage.dask: 32\n    "
    ...


def pinv(a: numpy.ndarray):
    "\n    usage.skimage: 1\n    "
    ...


def eig(a: numpy.ndarray):
    "\n    usage.skimage: 3\n    usage.sklearn: 2\n    "
    ...


def matrix_rank(M: numpy.ndarray):
    "\n    usage.skimage: 1\n    "
    ...


def slogdet(a: numpy.ndarray):
    "\n    usage.sklearn: 1\n    "
    ...


def lstsq(a: numpy.ndarray, b: numpy.ndarray):
    "\n    usage.sklearn: 2\n    usage.dask: 3\n    "
    ...


def eigvals(a: Union[numpy.ndarray, dask.array.core.Array]):
    "\n    usage.dask: 2\n    "
    ...


def qr(a: numpy.ndarray):
    "\n    usage.dask: 5\n    "
    ...


class LinAlgError:

    # usage.sklearn: 2
    args: Tuple[
        Literal["The kernel, DotProduct(sigma_0=1), is not returnin"],
        Literal["3-th leading minor of the array is not positive de"],
    ]
