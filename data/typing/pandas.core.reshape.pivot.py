from typing import *


@overload
def crosstab(index: pandas.core.series.Series, columns: pandas.core.series.Series):
    """
    usage.prophet: 1
    """
    ...


@overload
def crosstab(
    index: numpy.ndarray,
    columns: List[numpy.ndarray],
    values: None,
    rownames: List[Literal["a"]],
    colnames: List[Literal["c", "b"]],
    aggfunc: None,
    margins: bool,
    margins_name: Literal["All"],
    dropna: bool,
    normalize: bool,
):
    """
    usage.modin: 1
    """
    ...


def crosstab(
    index: Union[numpy.ndarray, pandas.core.series.Series],
    columns: Union[List[numpy.ndarray], pandas.core.series.Series],
    values: None = ...,
    rownames: List[Literal["a"]] = ...,
    colnames: List[Literal["c", "b"]] = ...,
    aggfunc: None = ...,
    margins: bool = ...,
    margins_name: Literal["All"] = ...,
    dropna: bool = ...,
    normalize: bool = ...,
):
    """
    usage.modin: 1
    usage.prophet: 1
    """
    ...


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
