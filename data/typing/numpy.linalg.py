from typing import *

# usage.skimage: 2
# usage.sklearn: 4
LinAlgError: object


def det(a: numpy.ndarray):
    """
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


def eigvalsh(a: numpy.ndarray):
    """
    usage.skimage: 2
    """
    ...


def inv(a: numpy.ndarray):
    """
    usage.skimage: 7
    usage.sklearn: 6
    """
    ...


def lstsq(a: numpy.ndarray, b: numpy.ndarray):
    """
    usage.sklearn: 2
    """
    ...


def matrix_rank(M: numpy.ndarray):
    """
    usage.skimage: 1
    """
    ...


def norm(
    x: numpy.ndarray,
    ord: Union[float, int, Literal["fro"]] = ...,
    axis: Union[None, int] = ...,
):
    """
    usage.skimage: 8
    usage.sklearn: 45
    """
    ...


def pinv(a: numpy.ndarray):
    """
    usage.skimage: 1
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
    usage.sklearn: 6
    """
    ...


class LinAlgError:

    # usage.sklearn: 2
    args: Tuple[str, str]
