from typing import *


@overload
def polyval(x: numpy.ndarray, c: numpy.ndarray, tensor: bool):
    """
    usage.scipy: 5
    """
    ...


@overload
def polyval(x: int, c: List[int]):
    """
    usage.scipy: 7
    """
    ...


@overload
def polyval(x: numpy.ndarray, c: List[Union[numpy.float64, int]]):
    """
    usage.scipy: 1
    """
    ...


@overload
def polyval(x: numpy.ndarray, c: List[numpy.float64]):
    """
    usage.scipy: 1
    """
    ...


@overload
def polyval(x: numpy.int64, c: List[int]):
    """
    usage.scipy: 7
    """
    ...


def polyval(
    x: Union[numpy.int64, int, numpy.ndarray],
    c: Union[List[Union[int, numpy.float64]], numpy.ndarray],
    tensor: bool = ...,
):
    """
    usage.scipy: 21
    """
    ...


@overload
def polyvalfromroots(x: numpy.ndarray, r: numpy.ndarray):
    """
    usage.scipy: 6
    """
    ...


@overload
def polyvalfromroots(x: numpy.ndarray, r: List[float]):
    """
    usage.scipy: 2
    """
    ...


@overload
def polyvalfromroots(x: numpy.ndarray, r: list):
    """
    usage.scipy: 2
    """
    ...


@overload
def polyvalfromroots(x: numpy.ndarray, r: List[int]):
    """
    usage.scipy: 1
    """
    ...


def polyvalfromroots(
    x: numpy.ndarray, r: Union[numpy.ndarray, List[Union[float, int]]]
):
    """
    usage.scipy: 11
    """
    ...
