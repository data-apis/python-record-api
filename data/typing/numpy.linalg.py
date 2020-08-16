from typing import *

# usage.matplotlib: 2
# usage.skimage: 2
# usage.sklearn: 4
LinAlgError: object

# usage.dask: 4
_umath_linalg: object


def det(a: Union[numpy.ndarray, dask.array.core.Array]):
    """
    usage.dask: 2
    usage.matplotlib: 1
    usage.skimage: 5
    usage.sklearn: 1
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
    usage.matplotlib: 2
    usage.skimage: 7
    usage.sklearn: 6
    """
    ...


def lstsq(a: numpy.ndarray, b: numpy.ndarray):
    """
    usage.dask: 3
    usage.sklearn: 2
    """
    ...


def matrix_rank(M: numpy.ndarray):
    """
    usage.skimage: 1
    """
    ...


def norm(
    x: object,
    ord: Union[Literal["fro", "nuc"], int, float, None] = ...,
    axis: Union[int, None, Tuple[int, ...]] = ...,
    keepdims: bool = ...,
):
    """
    usage.dask: 25
    usage.matplotlib: 4
    usage.skimage: 8
    usage.sklearn: 45
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
    usage.dask: 4
    usage.skimage: 7
    usage.sklearn: 6
    """
    ...


class LinAlgError:

    # usage.sklearn: 2
    args: Tuple[str, str]
