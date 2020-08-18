from typing import *


@overload
def pivot_table(
    data: pandas.core.frame.DataFrame,
    values: Literal["B"],
    index: Literal["A"],
    columns: Literal["C"],
    aggfunc: Literal["mean"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def pivot_table(
    data: pandas.core.frame.DataFrame,
    values: Literal["B"],
    index: Literal["A"],
    columns: Literal["C"],
    aggfunc: Literal["count"],
):
    """
    usage.dask: 2
    """
    ...


@overload
def pivot_table(
    data: pandas.core.frame.DataFrame,
    values: Literal["B"],
    index: Literal["A"],
    columns: Literal["C"],
    aggfunc: Literal["sum"],
):
    """
    usage.dask: 2
    """
    ...


@overload
def pivot_table(
    data: pandas.core.frame.DataFrame,
    values: Literal["C"],
    index: Literal["A"],
    columns: Literal["B"],
    aggfunc: Literal["count"],
):
    """
    usage.dask: 2
    """
    ...


def pivot_table(
    data: pandas.core.frame.DataFrame,
    values: Literal["C", "B"],
    index: Literal["A"],
    columns: Literal["B", "C"],
    aggfunc: Literal["count", "sum", "mean"],
):
    """
    usage.dask: 7
    """
    ...
