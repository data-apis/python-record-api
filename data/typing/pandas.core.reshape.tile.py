from typing import *


def cut(
    x: Union[
        (
            pandas.core.indexes.datetimes.DatetimeIndex,
            numpy.flatiter,
            numpy.ndarray,
            xarray.core.dataarray.DataArray,
            range,
        )
    ],
    bins,
    right: bool = ...,
    labels: None = ...,
    precision: int = ...,
    include_lowest: bool = ...,
):
    "usage.xarray: 12"
