from typing import *


def cut(
    x: Union[
        (
            numpy.flatiter,
            numpy.ndarray,
            range,
            pandas.core.indexes.datetimes.DatetimeIndex,
            xarray.core.dataarray.DataArray,
        )
    ],
    bins,
    right: bool = ...,
    labels: None = ...,
    precision: int = ...,
    include_lowest: bool = ...,
):
    "usage.xarray: 12"
