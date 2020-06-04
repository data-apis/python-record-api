from typing import *


def svd(a: numpy.ndarray = ...):
    "usage.skimage: 7, usage.sklearn: 3"


def inv(a: numpy.ndarray):
    "usage.skimage: 7"


def eigvalsh(a: numpy.ndarray):
    "usage.skimage: 2"


def det(a: numpy.ndarray):
    "usage.skimage: 5, usage.sklearn: 1"


def solve(a: numpy.ndarray, b: numpy.ndarray):
    "usage.skimage: 2"


def norm(
    x: numpy.ndarray,
    ord: Union[(float, int, Literal[("fro",)])] = ...,
    axis: Union[(None, int)] = ...,
):
    "usage.skimage: 8, usage.sklearn: 22"


def pinv(a: numpy.ndarray):
    "usage.skimage: 1"


def eig(a: numpy.ndarray):
    "usage.skimage: 3, usage.sklearn: 2"


def matrix_rank(M: numpy.ndarray):
    "usage.skimage: 1"


def slogdet(a: numpy.ndarray):
    "usage.sklearn: 1"


def lstsq(a: numpy.ndarray, b: numpy.ndarray = ...):
    "usage.sklearn: 2"


class LinAlgError:
    args: Tuple[
        (
            Literal[("The kernel, DotProduct(sigma_0=1), is not returnin",)],
            Literal[("3-th leading minor of the array is not positive de",)],
        )
    ] = ...
