from typing import *

# usage.skimage: 2
# usage.sklearn: 3
LinAlgError: object

# usage.dask: 4
_umath_linalg: object


def det(a: Union[dask.array.core.Array, numpy.ndarray]):
    """
    usage.skimage: 5
    usage.sklearn: 1
    usage.dask: 2
    """
    ...


def eig(a: numpy.ndarray):
    """
    usage.skimage: 3
    usage.sklearn: 2
    """
    ...


def eigvals(a: Union[numpy.ndarray, dask.array.core.Array]):
    """
    usage.dask: 2
    """
    ...


def eigvalsh(a: numpy.ndarray):
    """
    usage.skimage: 2
    """
    ...


def inv(a: numpy.ndarray):
    """
    usage.skimage: 7
    """
    ...


def lstsq(a: numpy.ndarray, b: numpy.ndarray):
    """
    usage.sklearn: 2
    usage.dask: 3
    """
    ...


def matrix_rank(M: numpy.ndarray):
    """
    usage.skimage: 1
    """
    ...


def norm(
    x: object,
    ord: Union[None, int, float, Literal["nuc", "fro"]] = ...,
    axis: Union[None, int, Tuple[int, ...]] = ...,
    keepdims: bool = ...,
):
    """
    usage.skimage: 8
    usage.sklearn: 22
    usage.dask: 32
    """
    ...


def pinv(a: numpy.ndarray):
    """
    usage.skimage: 1
    """
    ...


def qr(a: numpy.ndarray):
    """
    usage.dask: 5
    """
    ...


def slogdet(a: numpy.ndarray):
    """
    usage.sklearn: 1
    """
    ...


def solve(a: numpy.ndarray, b: numpy.ndarray):
    """
    usage.skimage: 2
    """
    ...


def svd(a: numpy.ndarray):
    """
    usage.skimage: 7
    usage.sklearn: 3
    usage.dask: 5
    """
    ...


class LinAlgError:

    # usage.sklearn: 2
    args: Tuple[
        Literal["The kernel, DotProduct(sigma_0=1), is not returnin"],
        Literal["3-th leading minor of the array is not positive de"],
    ]
