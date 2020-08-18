from typing import *


@overload
def cholesky(a: numpy.ndarray):
    """
    usage.scipy: 3
    """
    ...


@overload
def cholesky(a: List[List[float]]):
    """
    usage.scipy: 2
    """
    ...


def cholesky(a: Union[List[List[float]], numpy.ndarray]):
    """
    usage.scipy: 5
    """
    ...


@overload
def cond(x: numpy.ndarray, p: int):
    """
    usage.scipy: 4
    """
    ...


@overload
def cond(x: numpy.ndarray):
    """
    usage.scipy: 4
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
    usage.dask: 1
    usage.matplotlib: 1
    usage.scipy: 18
    usage.skimage: 5
    usage.sklearn: 1
    """
    ...


@overload
def det(a: dask.array.core.Array):
    """
    usage.dask: 1
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
    usage.dask: 1
    usage.scipy: 2
    """
    ...


@overload
def eigvals(a: dask.array.core.Array):
    """
    usage.dask: 1
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
    usage.dask: 2
    usage.scipy: 9
    """
    ...


@overload
def lstsq(a: numpy.ndarray, b: numpy.ndarray, rcond: numpy.float64):
    """
    usage.dask: 1
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
    usage.scipy: 21
    usage.skimage: 1
    """
    ...


@overload
def matrix_rank(M: numpy.ndarray, tol: numpy.float64):
    """
    usage.scipy: 2
    """
    ...


@overload
def matrix_rank(M: numpy.ndarray, tol: float):
    """
    usage.scipy: 1
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
    usage.dask: 1
    usage.matplotlib: 3
    usage.scipy: 197
    usage.skimage: 8
    usage.sklearn: 30
    """
    ...


@overload
def norm(x: float):
    """
    usage.scipy: 3
    """
    ...


@overload
def norm(x: numpy.ndarray, axis: int):
    """
    usage.matplotlib: 1
    usage.scipy: 18
    usage.sklearn: 3
    """
    ...


@overload
def norm(x: numpy.ndarray, ord: None):
    """
    usage.scipy: 13
    """
    ...


@overload
def norm(x: numpy.ndarray, ord: int):
    """
    usage.scipy: 35
    usage.sklearn: 2
    """
    ...


@overload
def norm(x: numpy.ndarray, ord: None, axis: int):
    """
    usage.scipy: 2
    """
    ...


@overload
def norm(x: numpy.ndarray, ord: int, axis: int):
    """
    usage.scipy: 2
    usage.sklearn: 2
    """
    ...


@overload
def norm(x: numpy.ndarray, ord: None, axis: int, keepdims: bool):
    """
    usage.dask: 1
    usage.scipy: 1
    """
    ...


@overload
def norm(x: numpy.ndarray, ord: int, axis: int, keepdims: bool):
    """
    usage.dask: 2
    usage.scipy: 1
    """
    ...


@overload
def norm(x: numpy.ndarray, ord: Literal["fro"]):
    """
    usage.scipy: 13
    usage.sklearn: 4
    """
    ...


@overload
def norm(x: numpy.ndarray, ord: float):
    """
    usage.scipy: 30
    """
    ...


@overload
def norm(x: numpy.ndarray, ord: float, axis: Tuple[int, int]):
    """
    usage.scipy: 2
    """
    ...


@overload
def norm(x: numpy.ndarray, ord: int, axis: Tuple[int, int]):
    """
    usage.scipy: 2
    """
    ...


@overload
def norm(x: numpy.ndarray, ord: float, axis: Tuple[int, int], keepdims: bool):
    """
    usage.scipy: 1
    """
    ...


@overload
def norm(x: numpy.ndarray, ord: int, axis: Tuple[int, int], keepdims: bool):
    """
    usage.dask: 1
    usage.scipy: 1
    """
    ...


@overload
def norm(x: List[numpy.complex128]):
    """
    usage.scipy: 1
    """
    ...


@overload
def norm(x: complex):
    """
    usage.scipy: 1
    """
    ...


@overload
def norm(x: numpy.complex128):
    """
    usage.scipy: 1
    """
    ...


@overload
def norm(x: numpy.float64):
    """
    usage.scipy: 1
    """
    ...


@overload
def norm(x: List[numpy.float64]):
    """
    usage.scipy: 2
    """
    ...


@overload
def norm(x: List[List[int]]):
    """
    usage.scipy: 1
    """
    ...


@overload
def norm(x: List[List[int]], ord: Literal["fro"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def norm(x: List[List[int]], ord: float):
    """
    usage.scipy: 2
    """
    ...


@overload
def norm(x: List[List[int]], ord: int):
    """
    usage.scipy: 2
    """
    ...


@overload
def norm(x: List[List[Union[int, complex]]]):
    """
    usage.scipy: 1
    """
    ...


@overload
def norm(x: List[List[Union[int, complex]]], ord: Literal["fro"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def norm(x: List[List[Union[int, complex]]], ord: float):
    """
    usage.scipy: 2
    """
    ...


@overload
def norm(x: List[List[Union[int, complex]]], ord: int):
    """
    usage.scipy: 2
    """
    ...


@overload
def norm(x: numpy.ndarray, axis: None):
    """
    usage.scipy: 1
    """
    ...


@overload
def norm(x: numpy.ndarray, ord: Literal["fro"], axis: None):
    """
    usage.scipy: 1
    """
    ...


@overload
def norm(x: numpy.ndarray, ord: float, axis: None):
    """
    usage.scipy: 1
    usage.sklearn: 2
    """
    ...


@overload
def norm(x: numpy.ndarray, ord: int, axis: None):
    """
    usage.scipy: 1
    """
    ...


@overload
def norm(x: numpy.ndarray, axis: Tuple[int, int]):
    """
    usage.scipy: 2
    """
    ...


@overload
def norm(x: numpy.ndarray, ord: Literal["fro"], axis: Tuple[int, int]):
    """
    usage.scipy: 2
    """
    ...


@overload
def norm(x: numpy.ndarray, ord: Literal["f"], axis: Tuple[int, int]):
    """
    usage.scipy: 1
    """
    ...


@overload
def norm(x: List[List[int]], axis: None):
    """
    usage.scipy: 1
    """
    ...


@overload
def norm(x: List[List[int]], ord: Literal["fro"], axis: None):
    """
    usage.scipy: 1
    """
    ...


@overload
def norm(x: List[List[int]], ord: float, axis: None):
    """
    usage.scipy: 1
    """
    ...


@overload
def norm(x: List[List[int]], ord: int, axis: None):
    """
    usage.scipy: 1
    """
    ...


@overload
def norm(x: List[List[int]], axis: Tuple[int, int]):
    """
    usage.scipy: 2
    """
    ...


@overload
def norm(x: List[List[int]], ord: Literal["fro"], axis: Tuple[int, int]):
    """
    usage.scipy: 2
    """
    ...


@overload
def norm(x: List[List[int]], ord: float, axis: Tuple[int, int]):
    """
    usage.scipy: 1
    """
    ...


@overload
def norm(x: List[List[int]], ord: int, axis: Tuple[int, int]):
    """
    usage.scipy: 1
    """
    ...


@overload
def norm(x: List[List[int]], ord: Literal["f"], axis: Tuple[int, int]):
    """
    usage.scipy: 1
    """
    ...


@overload
def norm(x: List[List[Union[int, complex]]], axis: None):
    """
    usage.scipy: 1
    """
    ...


@overload
def norm(x: List[List[Union[int, complex]]], ord: Literal["fro"], axis: None):
    """
    usage.scipy: 1
    """
    ...


@overload
def norm(x: List[List[Union[int, complex]]], ord: float, axis: None):
    """
    usage.scipy: 1
    """
    ...


@overload
def norm(x: List[List[Union[int, complex]]], ord: int, axis: None):
    """
    usage.scipy: 1
    """
    ...


@overload
def norm(x: List[List[Union[int, complex]]], axis: Tuple[int, int]):
    """
    usage.scipy: 2
    """
    ...


@overload
def norm(
    x: List[List[Union[int, complex]]], ord: Literal["fro"], axis: Tuple[int, int]
):
    """
    usage.scipy: 2
    """
    ...


@overload
def norm(x: List[List[Union[int, complex]]], ord: float, axis: Tuple[int, int]):
    """
    usage.scipy: 1
    """
    ...


@overload
def norm(x: List[List[Union[int, complex]]], ord: int, axis: Tuple[int, int]):
    """
    usage.scipy: 1
    """
    ...


@overload
def norm(x: List[List[Union[int, complex]]], ord: Literal["f"], axis: Tuple[int, int]):
    """
    usage.scipy: 1
    """
    ...


@overload
def norm(x: numpy.ndarray, ord: float, axis: int):
    """
    usage.scipy: 1
    usage.sklearn: 2
    """
    ...


@overload
def norm(x: numpy.ndarray, axis: Tuple[int]):
    """
    usage.scipy: 1
    """
    ...


@overload
def norm(x: numpy.ndarray, ord: None, axis: Tuple[int]):
    """
    usage.scipy: 1
    """
    ...


@overload
def norm(x: numpy.ndarray, ord: int, axis: Tuple[int]):
    """
    usage.scipy: 1
    """
    ...


@overload
def norm(x: numpy.ndarray, ord: float, axis: Tuple[int]):
    """
    usage.scipy: 1
    """
    ...


@overload
def norm(x: List[List[int]], axis: int):
    """
    usage.scipy: 1
    """
    ...


@overload
def norm(x: List[List[int]], ord: None, axis: int):
    """
    usage.scipy: 1
    """
    ...


@overload
def norm(x: List[List[int]], ord: int, axis: int):
    """
    usage.scipy: 1
    """
    ...


@overload
def norm(x: List[List[int]], ord: float, axis: int):
    """
    usage.scipy: 1
    """
    ...


@overload
def norm(x: List[List[int]], axis: Tuple[int]):
    """
    usage.scipy: 1
    """
    ...


@overload
def norm(x: List[List[int]], ord: None, axis: Tuple[int]):
    """
    usage.scipy: 1
    """
    ...


@overload
def norm(x: List[List[int]], ord: int, axis: Tuple[int]):
    """
    usage.scipy: 1
    """
    ...


@overload
def norm(x: List[List[int]], ord: float, axis: Tuple[int]):
    """
    usage.scipy: 1
    """
    ...


@overload
def norm(x: List[List[Union[int, complex]]], axis: int):
    """
    usage.scipy: 1
    """
    ...


@overload
def norm(x: List[List[Union[int, complex]]], ord: None, axis: int):
    """
    usage.scipy: 1
    """
    ...


@overload
def norm(x: List[List[Union[int, complex]]], ord: int, axis: int):
    """
    usage.scipy: 1
    """
    ...


@overload
def norm(x: List[List[Union[int, complex]]], ord: float, axis: int):
    """
    usage.scipy: 1
    """
    ...


@overload
def norm(x: List[List[Union[int, complex]]], axis: Tuple[int]):
    """
    usage.scipy: 1
    """
    ...


@overload
def norm(x: List[List[Union[int, complex]]], ord: None, axis: Tuple[int]):
    """
    usage.scipy: 1
    """
    ...


@overload
def norm(x: List[List[Union[int, complex]]], ord: int, axis: Tuple[int]):
    """
    usage.scipy: 1
    """
    ...


@overload
def norm(x: List[List[Union[int, complex]]], ord: float, axis: Tuple[int]):
    """
    usage.scipy: 1
    """
    ...


@overload
def norm(x: numpy.ndarray, axis: int, keepdims: bool):
    """
    usage.scipy: 3
    """
    ...


@overload
def norm(x: dask.array.core.Array):
    """
    usage.dask: 2
    """
    ...


@overload
def norm(x: object):
    """
    usage.dask: 1
    """
    ...


@overload
def norm(x: numpy.ndarray, ord: None, axis: None, keepdims: bool):
    """
    usage.dask: 1
    """
    ...


@overload
def norm(x: numpy.ndarray, ord: None, axis: Tuple[int], keepdims: bool):
    """
    usage.dask: 1
    """
    ...


@overload
def norm(x: numpy.ndarray, ord: int, axis: None, keepdims: bool):
    """
    usage.dask: 3
    """
    ...


@overload
def norm(x: numpy.ndarray, ord: int, axis: Tuple[int], keepdims: bool):
    """
    usage.dask: 2
    """
    ...


@overload
def norm(x: numpy.ndarray, ord: float, axis: None, keepdims: bool):
    """
    usage.dask: 2
    """
    ...


@overload
def norm(x: numpy.ndarray, ord: float, axis: int, keepdims: bool):
    """
    usage.dask: 2
    """
    ...


@overload
def norm(x: numpy.ndarray, ord: float, axis: Tuple[int], keepdims: bool):
    """
    usage.dask: 2
    """
    ...


@overload
def norm(x: numpy.ndarray, ord: Literal["fro"], axis: None, keepdims: bool):
    """
    usage.dask: 1
    """
    ...


@overload
def norm(x: numpy.ndarray, ord: Literal["fro"], axis: Tuple[int, int], keepdims: bool):
    """
    usage.dask: 1
    """
    ...


@overload
def norm(x: numpy.ndarray, ord: Literal["nuc"], axis: None, keepdims: bool):
    """
    usage.dask: 1
    """
    ...


@overload
def norm(x: numpy.ndarray, ord: Literal["nuc"], axis: Tuple[int, int], keepdims: bool):
    """
    usage.dask: 1
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
    usage.scipy: 23
    usage.skimage: 2
    """
    ...


@overload
def solve(a: numpy.matrix, b: numpy.ndarray):
    """
    usage.scipy: 2
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
    usage.dask: 3
    usage.scipy: 4
    usage.skimage: 6
    usage.sklearn: 3
    """
    ...


@overload
def svd(a: numpy.ndarray, full_matrices: bool):
    """
    usage.scipy: 1
    usage.skimage: 1
    usage.sklearn: 3
    """
    ...


@overload
def svd(a: numpy.ndarray, compute_uv: bool):
    """
    usage.scipy: 5
    """
    ...


@overload
def svd(a: numpy.ndarray, full_matrices: int):
    """
    usage.dask: 1
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
