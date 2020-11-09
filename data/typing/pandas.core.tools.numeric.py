from typing import *


@overload
def to_numeric(arg: List[Literal["-3", "2", "1.0"]]):
    """
    usage.koalas: 1
    """
    ...


@overload
def to_numeric(arg: Tuple[Literal["1.0"], Literal["2"], Literal["-3"]]):
    """
    usage.koalas: 1
    """
    ...


@overload
def to_numeric(arg: numpy.ndarray):
    """
    usage.dask: 1
    usage.koalas: 1
    """
    ...


@overload
def to_numeric(arg: Literal["1.0"]):
    """
    usage.koalas: 1
    """
    ...


@overload
def to_numeric(arg: pandas.core.series.Series):
    """
    usage.dask: 3
    usage.seaborn: 1
    """
    ...


def to_numeric(
    arg: Union[
        numpy.ndarray,
        pandas.core.series.Series,
        Literal["1.0"],
        Tuple[Literal["1.0"], Literal["2"], Literal["-3"]],
        List[Literal["-3", "2", "1.0"]],
    ]
):
    """
    usage.dask: 4
    usage.koalas: 4
    usage.seaborn: 1
    """
    ...
