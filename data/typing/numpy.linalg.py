from typing import *

# usage.matplotlib: 2
# usage.scipy: 6
# usage.skimage: 2
# usage.sklearn: 4
LinAlgError: object

# usage.dask: 4
_umath_linalg: object

# usage.scipy: 1
linalg: object


def cholesky(a: Union[List[List[float]], numpy.ndarray]):
    """
    usage.scipy: 5
    """
    ...


def cond(x: numpy.ndarray):
    """
    usage.scipy: 8
    """
    ...


def det(a: Union[numpy.ndarray, dask.array.core.Array]):
    """
    usage.dask: 2
    usage.matplotlib: 1
    usage.scipy: 18
    usage.skimage: 5
    usage.sklearn: 1
    """
    ...


def eig(a: numpy.ndarray):
    """
    usage.scipy: 15
    usage.skimage: 3
    usage.sklearn: 2
    """
    ...


def eigh(a: numpy.ndarray):
    """
    usage.scipy: 1
    """
    ...


def eigvals(a: Union[dask.array.core.Array, numpy.ndarray]):
    """
    usage.dask: 2
    usage.scipy: 2
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
    usage.scipy: 12
    usage.skimage: 7
    usage.sklearn: 6
    """
    ...


def lstsq(a: numpy.ndarray, b: numpy.ndarray):
    """
    usage.dask: 3
    usage.scipy: 9
    usage.sklearn: 2
    """
    ...


def matrix_power(a: numpy.ndarray, n: int):
    """
    usage.scipy: 16
    """
    ...


def matrix_rank(M: numpy.ndarray):
    """
    usage.scipy: 24
    usage.skimage: 1
    """
    ...


def norm(
    x: object,
    ord: Union[Literal["fro", "nuc", "f"], int, float, None] = ...,
    axis: Union[int, None, Tuple[int, ...]] = ...,
    keepdims: bool = ...,
):
    """
    usage.dask: 25
    usage.matplotlib: 4
    usage.scipy: 394
    usage.skimage: 8
    usage.sklearn: 45
    """
    ...


def pinv(a: numpy.ndarray):
    """
    usage.scipy: 3
    usage.skimage: 1
    """
    ...


def qr(a: numpy.ndarray):
    """
    usage.dask: 5
    usage.scipy: 1
    """
    ...


def slogdet(a: numpy.ndarray):
    """
    usage.scipy: 4
    usage.sklearn: 1
    """
    ...


def solve(a: Union[numpy.ndarray, numpy.matrix], b: numpy.ndarray):
    """
    usage.scipy: 25
    usage.skimage: 2
    """
    ...


def svd(a: numpy.ndarray):
    """
    usage.dask: 4
    usage.scipy: 10
    usage.skimage: 7
    usage.sklearn: 6
    """
    ...


class LinAlgError:

    # usage.sklearn: 2
    args: Tuple[str, str]
