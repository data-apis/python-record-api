from typing import *


@overload
def to_numeric(arg: numpy.ndarray):
    """
    usage.dask: 1
    """
    ...


@overload
def to_numeric(arg: pandas.core.series.Series):
    """
    usage.dask: 3
    """
    ...


def to_numeric(arg: Union[pandas.core.series.Series, numpy.ndarray]):
    """
    usage.dask: 4
    """
    ...
