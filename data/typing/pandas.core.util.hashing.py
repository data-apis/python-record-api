from typing import *


@overload
def hash_pandas_object(
    obj: pandas.core.series.Series,
    index: bool,
    encoding: Literal["utf8"],
    hash_key: None,
    categorize: bool,
):
    """
    usage.dask: 1
    """
    ...


@overload
def hash_pandas_object(
    obj: pandas.core.frame.DataFrame,
    index: bool,
    encoding: Literal["utf8"],
    hash_key: None,
    categorize: bool,
):
    """
    usage.dask: 1
    """
    ...


@overload
def hash_pandas_object(
    obj: pandas.core.indexes.numeric.Int64Index,
    index: bool,
    encoding: Literal["utf8"],
    hash_key: None,
    categorize: bool,
):
    """
    usage.dask: 1
    """
    ...


@overload
def hash_pandas_object(
    obj: pandas.core.indexes.base.Index,
    index: bool,
    encoding: Literal["utf8"],
    hash_key: None,
    categorize: bool,
):
    """
    usage.dask: 1
    """
    ...


@overload
def hash_pandas_object(obj: pandas.core.series.Series):
    """
    usage.dask: 5
    """
    ...


@overload
def hash_pandas_object(obj: pandas.core.indexes.numeric.Int64Index):
    """
    usage.dask: 3
    """
    ...


@overload
def hash_pandas_object(obj: pandas.core.indexes.base.Index):
    """
    usage.dask: 3
    """
    ...


@overload
def hash_pandas_object(obj: pandas.core.frame.DataFrame):
    """
    usage.dask: 3
    """
    ...


@overload
def hash_pandas_object(obj: pandas.core.indexes.timedeltas.TimedeltaIndex):
    """
    usage.dask: 2
    """
    ...


@overload
def hash_pandas_object(obj: pandas.core.series.Series, categorize: bool):
    """
    usage.dask: 3
    """
    ...


@overload
def hash_pandas_object(obj: pandas.core.frame.DataFrame, index: bool):
    """
    usage.dask: 1
    """
    ...


@overload
def hash_pandas_object(obj: pandas.core.series.Series, index: bool):
    """
    usage.dask: 1
    """
    ...


@overload
def hash_pandas_object(
    obj: pandas.core.indexes.range.RangeIndex,
    index: bool,
    encoding: Literal["utf8"],
    hash_key: None,
    categorize: bool,
):
    """
    usage.dask: 1
    """
    ...


def hash_pandas_object(
    obj: object,
    index: bool = ...,
    encoding: Literal["utf8"] = ...,
    hash_key: None = ...,
    categorize: bool = ...,
):
    """
    usage.dask: 26
    """
    ...
