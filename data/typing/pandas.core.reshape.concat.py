from typing import *


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
