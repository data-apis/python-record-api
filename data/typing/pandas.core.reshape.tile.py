from typing import *


def cut(
    x: Union[
        numpy.ndarray,
        pandas.core.indexes.datetimes.DatetimeIndex,
        xarray.core.dataarray.DataArray,
        numpy.flatiter,
        range,
    ],
    bins: Union[
        int, range, pandas.core.indexes.datetimes.DatetimeIndex, List[Union[float, int]]
    ],
    right: bool = ...,
    labels: None = ...,
    precision: int = ...,
    include_lowest: bool = ...,
):
    """
    usage.xarray: 14
    """
    ...
