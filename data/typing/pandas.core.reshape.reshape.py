from typing import *


@overload
def get_dummies(data: pandas.core.series.Series):
    """
    usage.dask: 2
    """
    ...


@overload
def get_dummies(
    data: pandas.core.series.Series,
    prefix: None,
    prefix_sep: Literal["_"],
    dummy_na: bool,
    columns: None,
    sparse: bool,
    drop_first: bool,
    dtype: Type[numpy.uint8],
):
    """
    usage.dask: 2
    """
    ...


@overload
def get_dummies(data: pandas.core.frame.DataFrame):
    """
    usage.dask: 1
    """
    ...


@overload
def get_dummies(
    data: pandas.core.frame.DataFrame,
    prefix: None,
    prefix_sep: Literal["_"],
    dummy_na: bool,
    columns: pandas.core.indexes.base.Index,
    sparse: bool,
    drop_first: bool,
    dtype: Type[numpy.uint8],
):
    """
    usage.dask: 2
    """
    ...


@overload
def get_dummies(data: pandas.core.frame.DataFrame, columns: List[Literal["c", "a"]]):
    """
    usage.dask: 1
    """
    ...


@overload
def get_dummies(
    data: pandas.core.frame.DataFrame,
    prefix: None,
    prefix_sep: Literal["_"],
    dummy_na: bool,
    columns: List[Literal["c", "a"]],
    sparse: bool,
    drop_first: bool,
    dtype: Type[numpy.uint8],
):
    """
    usage.dask: 2
    """
    ...


@overload
def get_dummies(
    data: pandas.core.series.Series, prefix: Literal["X"], prefix_sep: Literal["-"]
):
    """
    usage.dask: 1
    """
    ...


@overload
def get_dummies(
    data: pandas.core.series.Series,
    prefix: Literal["X"],
    prefix_sep: Literal["-"],
    dummy_na: bool,
    columns: None,
    sparse: bool,
    drop_first: bool,
    dtype: Type[numpy.uint8],
):
    """
    usage.dask: 2
    """
    ...


@overload
def get_dummies(data: pandas.core.series.Series, drop_first: bool):
    """
    usage.dask: 1
    """
    ...


@overload
def get_dummies(data: pandas.core.series.Series, dummy_na: bool):
    """
    usage.dask: 1
    """
    ...


@overload
def get_dummies(data: pandas.core.series.Series, sparse: bool):
    """
    usage.dask: 1
    """
    ...


@overload
def get_dummies(data: pandas.core.frame.DataFrame, sparse: bool):
    """
    usage.dask: 2
    """
    ...


@overload
def get_dummies(data: pandas.core.frame.DataFrame, dtype: Literal["float64"]):
    """
    usage.dask: 1
    """
    ...


@overload
def get_dummies(
    data: pandas.core.frame.DataFrame,
    prefix: None,
    prefix_sep: Literal["_"],
    dummy_na: bool,
    columns: pandas.core.indexes.base.Index,
    sparse: bool,
    drop_first: bool,
    dtype: Literal["float64"],
):
    """
    usage.dask: 2
    """
    ...


@overload
def get_dummies(
    data: pandas.core.frame.DataFrame,
    prefix: None,
    prefix_sep: Literal["_"],
    dummy_na: bool,
    columns: None,
    sparse: bool,
    drop_first: bool,
    dtype: Literal["float64"],
):
    """
    usage.dask: 1
    """
    ...


def get_dummies(
    data: Union[pandas.core.frame.DataFrame, pandas.core.series.Series],
    prefix: Union[None, Literal["X"]] = ...,
    prefix_sep: Literal["_", "-"] = ...,
    dummy_na: bool = ...,
    columns: Union[None, List[Literal["c", "a"]], pandas.core.indexes.base.Index] = ...,
    sparse: bool = ...,
    drop_first: bool = ...,
    dtype: Union[Literal["float64"], Type[numpy.uint8]] = ...,
):
    """
    usage.dask: 22
    """
    ...
