from typing import *


def merge(
    _0: Union[dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame] = ...,
    _1: Union[dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame] = ...,
    /,
    left: Union[dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame] = ...,
    right: Union[dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame] = ...,
    how: Literal["outer", "left", "inner", "right"] = ...,
    on: Union[
        None, List[Literal["idx", "k", "A"]], Literal["B", "x", "y", "idx"]
    ] = ...,
    left_on: Union[
        None,
        dask.dataframe.core.Series,
        List[Literal["y", "b", "a"]],
        Literal["x", "e", "d", "b", "a"],
    ] = ...,
    right_on: Union[
        None, List[Literal["y", "e", "d"]], str, dask.dataframe.core.Series
    ] = ...,
    left_index: bool = ...,
    right_index: bool = ...,
    suffixes: Union[
        Tuple[Literal["1", "_x"], Literal["2", "_y"]],
        List[Literal["_r", "_l", "", "r", "l"]],
    ] = ...,
    indicator: bool = ...,
    *,
    npartitions: None = ...,
    shuffle: Union[None, Literal["tasks", "disk"]] = ...,
):
    """
    usage.dask: 291
    """
    ...


def merge_asof(
    left: Union[dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame],
    right: Union[dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame],
    left_index: bool = ...,
    on: Literal["time", "a"] = ...,
    by: Literal["ticker"] = ...,
    left_on: Literal["a"] = ...,
    right_index: bool = ...,
    left_by: Union[Literal["ticker"], None] = ...,
    right_by: Union[Literal["ticker"], None] = ...,
    suffixes: Tuple[Literal["_x"], Literal["_y"]] = ...,
    tolerance: Union[pandas._libs.tslibs.timedeltas.Timedelta, None] = ...,
    allow_exact_matches: bool = ...,
    direction: Literal["backward", "nearest", "forward"] = ...,
):
    """
    usage.dask: 41
    """
    ...
