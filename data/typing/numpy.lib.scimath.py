from typing import *


def arccos(x: List[float]):
    """
    usage.scipy: 2
    """
    ...


@overload
def sqrt(x: numpy.matrix):
    """
    usage.networkx: 2
    """
    ...


@overload
def sqrt(x: numpy.ndarray):
    """
    usage.networkx: 1
    """
    ...


def sqrt(x: Union[numpy.ndarray, numpy.matrix]):
    """
    usage.networkx: 3
    """
    ...
