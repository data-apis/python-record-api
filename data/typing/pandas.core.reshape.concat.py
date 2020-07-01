from typing import *


def concat(
    objs: Union[
        List[Union[pandas.core.series.Series, pandas.core.frame.DataFrame]],
        Dict[int, pandas.core.series.Series],
    ],
    axis: int = ...,
    join: Literal["inner", "outer"] = ...,
    sort: bool = ...,
):
    """
    usage.dask: 141
    """
    ...
