from typing import *


@overload
def concat(
    objs: Union[
        List[Union[pandas.core.series.Series, pandas.core.frame.DataFrame]],
        Dict[int, pandas.core.series.Series],
    ],
    axis: int = ...,
    join: Literal["outer", "inner"] = ...,
    sort: bool = ...,
):
    """
    usage.dask: 149
    """
    ...


@overload
def concat(
    objs: List[pandas.core.frame.DataFrame], ignore_index: bool = ..., axis: int = ...
):
    """
    usage.sklearn: 3
    """
    ...


def concat(
    objs: Union[
        List[Union[pandas.core.frame.DataFrame, pandas.core.series.Series]],
        Dict[int, pandas.core.series.Series],
    ],
    axis: int = ...,
    join: Literal["outer", "inner"] = ...,
    sort: bool = ...,
):
    """
    usage.dask: 149
    usage.sklearn: 3
    """
    ...
