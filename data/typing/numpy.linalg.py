from typing import *


def cholesky(a: Union[List[List[float]], numpy.ndarray]):
    """
    usage.scipy: 5
    """
    ...


def cond(x: numpy.ndarray, p: int = ...):
    """
    usage.scipy: 8
    """
    ...


@overload
def det(a: numpy.ndarray):
    """
    usage.matplotlib: 1
    usage.scipy: 18
    usage.skimage: 5
    usage.sklearn: 1
    """
    ...


@overload
def det(a: Union[numpy.ndarray, dask.array.core.Array]):
    """
    usage.dask: 2
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


@overload
def eigvals(a: numpy.ndarray):
    """
    usage.scipy: 2
    """
    ...


@overload
def eigvals(a: Union[numpy.ndarray, dask.array.core.Array]):
    """
    usage.dask: 2
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


@overload
def lstsq(a: numpy.ndarray, b: numpy.ndarray, rcond: int):
    """
    usage.scipy: 9
    """
    ...


@overload
def lstsq(a: numpy.ndarray, b: numpy.ndarray, rcond: Union[numpy.float64, int]):
    """
    usage.dask: 3
    """
    ...


@overload
def lstsq(a: numpy.ndarray, b: numpy.ndarray, rcond: None):
    """
    usage.sklearn: 1
    """
    ...


@overload
def lstsq(a: numpy.ndarray, b: numpy.ndarray):
    """
    usage.sklearn: 1
    """
    ...


def lstsq(
    a: numpy.ndarray, b: numpy.ndarray, rcond: Union[None, numpy.float64, int] = ...
):
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


@overload
def matrix_rank(M: numpy.ndarray):
    """
    usage.skimage: 1
    """
    ...


@overload
def matrix_rank(M: numpy.ndarray, tol: Union[float, numpy.float64] = ...):
    """
    usage.scipy: 24
    """
    ...


def matrix_rank(M: numpy.ndarray, tol: Union[float, numpy.float64] = ...):
    """
    usage.scipy: 24
    usage.skimage: 1
    """
    ...


@overload
def norm(x: numpy.ndarray):
    """
    usage.matplotlib: 3
    usage.skimage: 8
    usage.sklearn: 30
    """
    ...


@overload
def norm(
    x: object,
    ord: Union[int, float, Literal["f", "fro"], None] = ...,
    axis: Union[int, Tuple[int, ...], None] = ...,
    keepdims: bool = ...,
):
    """
    usage.scipy: 394
    """
    ...


@overload
def norm(x: numpy.ndarray, axis: int):
    """
    usage.matplotlib: 1
    usage.sklearn: 3
    """
    ...


@overload
def norm(
    x: object,
    ord: Union[int, float, None, Literal["nuc", "fro"]] = ...,
    axis: Union[Tuple[int, ...], None, int] = ...,
    keepdims: bool = ...,
):
    """
    usage.dask: 25
    """
    ...


@overload
def norm(x: numpy.ndarray, ord: Literal["fro"]):
    """
    usage.sklearn: 4
    """
    ...


@overload
def norm(x: numpy.ndarray, ord: int):
    """
    usage.sklearn: 2
    """
    ...


@overload
def norm(x: numpy.ndarray, ord: int, axis: int):
    """
    usage.sklearn: 2
    """
    ...


@overload
def norm(x: numpy.ndarray, ord: float, axis: int):
    """
    usage.sklearn: 2
    """
    ...


@overload
def norm(x: numpy.ndarray, ord: float, axis: None):
    """
    usage.sklearn: 2
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


@overload
def solve(a: numpy.ndarray, b: numpy.ndarray):
    """
    usage.skimage: 2
    """
    ...


@overload
def solve(a: Union[numpy.matrix, numpy.ndarray], b: numpy.ndarray):
    """
    usage.scipy: 25
    """
    ...


def solve(a: Union[numpy.ndarray, numpy.matrix], b: numpy.ndarray):
    """
    usage.scipy: 25
    usage.skimage: 2
    """
    ...


@overload
def svd(a: numpy.ndarray):
    """
    usage.skimage: 6
    usage.sklearn: 3
    """
    ...


@overload
def svd(a: numpy.ndarray, full_matrices: bool):
    """
    usage.skimage: 1
    usage.sklearn: 3
    """
    ...


@overload
def svd(a: numpy.ndarray, full_matrices: bool = ..., compute_uv: bool = ...):
    """
    usage.scipy: 10
    """
    ...


@overload
def svd(a: numpy.ndarray, full_matrices: int = ...):
    """
    usage.dask: 4
    """
    ...


def svd(
    a: numpy.ndarray, full_matrices: Union[bool, int] = ..., compute_uv: bool = ...
):
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
