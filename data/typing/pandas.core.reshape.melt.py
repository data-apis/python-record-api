from typing import *


@overload
def melt(frame: pandas.core.frame.DataFrame):
    """
    usage.dask: 1
    """
    ...


@overload
def melt(frame: pandas.core.frame.DataFrame, id_vars: Literal["C"]):
    """
    usage.dask: 1
    """
    ...


@overload
def melt(frame: pandas.core.frame.DataFrame, value_vars: Literal["C"]):
    """
    usage.dask: 1
    """
    ...


@overload
def melt(
    frame: pandas.core.frame.DataFrame,
    value_vars: List[Literal["C", "A"]],
    var_name: Literal["myvar"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def melt(
    frame: pandas.core.frame.DataFrame,
    id_vars: Literal["B"],
    value_vars: List[Literal["C", "A"]],
    value_name: Literal["myval"],
):
    """
    usage.dask: 1
    """
    ...


def melt(
    frame: pandas.core.frame.DataFrame,
    id_vars: Literal["B", "C"] = ...,
    value_vars: Union[List[Literal["C", "A"]], Literal["C"]] = ...,
    value_name: Literal["myval"] = ...,
    var_name: Literal["myvar"] = ...,
):
    """
    usage.dask: 5
    """
    ...
