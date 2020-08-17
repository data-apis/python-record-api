from typing import *


@overload
def _as_pairs(x: Tuple[Tuple[int, int], Tuple[int, int]], ndim: int, as_index: bool):
    """
    usage.skimage: 1
    """
    ...


@overload
def _as_pairs(
    x: Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]],
    ndim: int,
    as_index: bool,
):
    """
    usage.skimage: 1
    """
    ...


@overload
def _as_pairs(x: int, ndim: int, as_index: bool):
    """
    usage.skimage: 1
    """
    ...


@overload
def _as_pairs(x: List[Tuple[numpy.int64, numpy.int64]], ndim: int, as_index: bool):
    """
    usage.skimage: 1
    """
    ...


@overload
def _as_pairs(x: Tuple[int, int], ndim: int, as_index: bool):
    """
    usage.skimage: 1
    """
    ...


def _as_pairs(
    x: Union[
        Tuple[Union[Tuple[int, int], int], ...],
        int,
        List[Tuple[numpy.int64, numpy.int64]],
    ],
    ndim: int,
    as_index: bool,
):
    """
    usage.skimage: 5
    """
    ...
