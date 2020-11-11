from typing import *


@overload
def cholesky(a: numpy.ndarray):
    """
    usage.scipy: 3
    usage.statsmodels: 46
    """
    ...


@overload
def cholesky(a: pandas.core.frame.DataFrame):
    """
    usage.statsmodels: 2
    """
    ...


@overload
def cholesky(a: List[List[float]]):
    """
    usage.scipy: 2
    """
    ...


def cholesky(a: Union[numpy.ndarray, pandas.core.frame.DataFrame, List[List[float]]]):
    """
    usage.scipy: 5
    usage.statsmodels: 48
    """
    ...


@overload
def cond(x: numpy.ndarray):
    """
    usage.scipy: 4
    usage.statsmodels: 1
    """
    ...


@overload
def cond(x: numpy.ndarray, p: int):
    """
    usage.scipy: 4
    """
    ...


def cond(x: numpy.ndarray, p: int = ...):
    """
    usage.scipy: 8
    usage.statsmodels: 1
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
    usage.statsmodels: 7
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
    usage.statsmodels: 7
    """
    ...


@overload
def eig(a: numpy.ndarray):
    """
    usage.networkx: 1
    usage.scipy: 15
    usage.skimage: 3
    usage.sklearn: 2
    usage.statsmodels: 7
    """
    ...


@overload
def eig(a: patsy.design_info.DesignMatrix):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def eig(a: numpy.matrix):
    """
    usage.networkx: 4
    """
    ...


def eig(a: Union[numpy.matrix, numpy.ndarray, patsy.design_info.DesignMatrix]):
    """
    usage.networkx: 5
    usage.scipy: 15
    usage.skimage: 3
    usage.sklearn: 2
    usage.statsmodels: 8
    """
    ...


@overload
def eigh(a: numpy.ndarray):
    """
    usage.networkx: 2
    usage.scipy: 1
    usage.statsmodels: 9
    """
    ...


@overload
def eigh(a: numpy.ndarray, UPLO: Literal["U"]):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def eigh(a: numpy.matrix):
    """
    usage.networkx: 1
    """
    ...


def eigh(a: Union[numpy.ndarray, numpy.matrix], UPLO: Literal["U"] = ...):
    """
    usage.networkx: 3
    usage.scipy: 1
    usage.statsmodels: 10
    """
    ...


@overload
def eigvals(a: numpy.ndarray):
    """
    usage.dask: 1
    usage.scipy: 2
    usage.statsmodels: 8
    """
    ...


@overload
def eigvals(a: dask.array.core.Array):
    """
    usage.dask: 1
    """
    ...


@overload
def eigvals(a: numpy.matrix):
    """
    usage.networkx: 2
    """
    ...


def eigvals(a: Union[numpy.matrix, numpy.ndarray, dask.array.core.Array]):
    """
    usage.dask: 2
    usage.networkx: 2
    usage.scipy: 2
    usage.statsmodels: 8
    """
    ...


def eigvalsh(a: numpy.ndarray):
    """
    usage.skimage: 2
    usage.statsmodels: 8
    """
    ...


@overload
def inv(a: numpy.ndarray):
    """
    usage.matplotlib: 2
    usage.scipy: 13
    usage.skimage: 7
    usage.sklearn: 6
    usage.statsmodels: 127
    """
    ...


@overload
def inv(a: pandas.core.frame.DataFrame):
    """
    usage.statsmodels: 2
    """
    ...


@overload
def inv(a: numpy.matrix):
    """
    usage.networkx: 1
    """
    ...


def inv(a: Union[numpy.matrix, pandas.core.frame.DataFrame, numpy.ndarray]):
    """
    usage.matplotlib: 2
    usage.networkx: 1
    usage.scipy: 13
    usage.skimage: 7
    usage.sklearn: 6
    usage.statsmodels: 129
    """
    ...


@overload
def lstsq(a: numpy.ndarray, b: numpy.ndarray, rcond: int):
    """
    usage.dask: 2
    usage.scipy: 9
    usage.statsmodels: 5
    """
    ...


@overload
def lstsq(a: numpy.ndarray, b: numpy.ndarray, rcond: None):
    """
    usage.sklearn: 1
    usage.statsmodels: 4
    """
    ...


@overload
def lstsq(a: numpy.ndarray, b: numpy.ndarray, rcond: float):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def lstsq(a: numpy.ndarray, b: pandas.core.series.Series, rcond: None):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def lstsq(a: numpy.ndarray, b: numpy.ndarray, rcond: numpy.float64):
    """
    usage.dask: 1
    """
    ...


@overload
def lstsq(a: numpy.ndarray, b: numpy.ndarray):
    """
    usage.sklearn: 1
    """
    ...


def lstsq(
    a: numpy.ndarray,
    b: Union[numpy.ndarray, pandas.core.series.Series],
    rcond: Union[None, float, numpy.float64, int] = ...,
):
    """
    usage.dask: 3
    usage.scipy: 9
    usage.sklearn: 2
    usage.statsmodels: 11
    """
    ...


def matrix_power(a: numpy.ndarray, n: int):
    """
    usage.scipy: 16
    usage.statsmodels: 2
    """
    ...


@overload
def matrix_rank(M: numpy.ndarray):
    """
    usage.scipy: 25
    usage.skimage: 1
    usage.statsmodels: 49
    """
    ...


@overload
def matrix_rank(M: numpy.ndarray, tol: float):
    """
    usage.scipy: 1
    usage.statsmodels: 1
    """
    ...


@overload
def matrix_rank(M: numpy.ndarray, tol: numpy.float64):
    """
    usage.scipy: 2
    """
    ...


def matrix_rank(M: numpy.ndarray, tol: Union[numpy.float64, float] = ...):
    """
    usage.scipy: 28
    usage.skimage: 1
    usage.statsmodels: 50
    """
    ...


@overload
def norm(x: numpy.ndarray):
    """
    usage.dask: 1
    usage.matplotlib: 3
    usage.networkx: 6
    usage.scipy: 206
    usage.skimage: 8
    usage.sklearn: 30
    usage.statsmodels: 10
    """
    ...


@overload
def norm(x: numpy.ndarray, ord: int):
    """
    usage.networkx: 1
    usage.scipy: 35
    usage.sklearn: 2
    usage.statsmodels: 1
    """
    ...


@overload
def norm(x: numpy.ndarray, ord: Literal["fro"]):
    """
    usage.scipy: 13
    usage.sklearn: 4
    usage.statsmodels: 5
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
    usage.networkx: 3
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
def norm(x: List[float]):
    """
    usage.scipy: 1
    """
    ...


@overload
def norm(x: List[int]):
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
    ord: Union[int, float, None, Literal["fro", "nuc", "f"]] = ...,
    axis: Union[int, Tuple[int, ...], None] = ...,
    keepdims: bool = ...,
):
    """
    usage.dask: 25
    usage.matplotlib: 4
    usage.networkx: 10
    usage.scipy: 405
    usage.skimage: 8
    usage.sklearn: 45
    usage.statsmodels: 16
    """
    ...


@overload
def pinv(a: numpy.ndarray):
    """
    usage.scipy: 3
    usage.seaborn: 1
    usage.skimage: 1
    usage.statsmodels: 76
    """
    ...


@overload
def pinv(a: numpy.ndarray, rcond: float):
    """
    usage.statsmodels: 1
    """
    ...


def pinv(a: numpy.ndarray, rcond: float = ...):
    """
    usage.scipy: 3
    usage.seaborn: 1
    usage.skimage: 1
    usage.statsmodels: 77
    """
    ...


@overload
def qr(a: numpy.ndarray, mode: Literal["r"]):
    """
    usage.statsmodels: 2
    """
    ...


@overload
def qr(a: numpy.ndarray):
    """
    usage.dask: 5
    usage.scipy: 1
    usage.statsmodels: 7
    """
    ...


@overload
def qr(a: numpy.matrix):
    """
    usage.networkx: 1
    """
    ...


def qr(a: Union[numpy.matrix, numpy.ndarray], mode: Literal["r"] = ...):
    """
    usage.dask: 5
    usage.networkx: 1
    usage.scipy: 1
    usage.statsmodels: 9
    """
    ...


def slogdet(a: numpy.ndarray):
    """
    usage.scipy: 4
    usage.sklearn: 1
    usage.statsmodels: 18
    """
    ...


@overload
def solve(a: numpy.ndarray, b: numpy.ndarray):
    """
    usage.scipy: 23
    usage.skimage: 2
    usage.statsmodels: 96
    """
    ...


@overload
def solve(a: numpy.ndarray, b: List[float]):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def solve(a: numpy.matrix, b: numpy.ndarray):
    """
    usage.networkx: 2
    usage.scipy: 2
    """
    ...


def solve(a: Union[numpy.matrix, numpy.ndarray], b: Union[numpy.ndarray, List[float]]):
    """
    usage.networkx: 2
    usage.scipy: 25
    usage.skimage: 2
    usage.statsmodels: 97
    """
    ...


@overload
def svd(a: numpy.ndarray):
    """
    usage.dask: 3
    usage.scipy: 4
    usage.skimage: 6
    usage.sklearn: 3
    usage.statsmodels: 4
    """
    ...


@overload
def svd(a: numpy.ndarray, full_matrices: bool):
    """
    usage.scipy: 1
    usage.skimage: 1
    usage.sklearn: 3
    usage.statsmodels: 7
    """
    ...


@overload
def svd(a: numpy.ndarray, full_matrices: int):
    """
    usage.dask: 1
    usage.statsmodels: 19
    """
    ...


@overload
def svd(a: numpy.ndarray, full_matrices: int, compute_uv: int):
    """
    usage.statsmodels: 3
    """
    ...


@overload
def svd(a: numpy.ndarray, compute_uv: bool):
    """
    usage.scipy: 5
    """
    ...


def svd(
    a: numpy.ndarray,
    full_matrices: Union[bool, int] = ...,
    compute_uv: Union[bool, int] = ...,
):
    """
    usage.dask: 4
    usage.scipy: 10
    usage.skimage: 7
    usage.sklearn: 6
    usage.statsmodels: 33
    """
    ...


class LinAlgError:

    # usage.sklearn: 2
    args: Tuple[str, str]
