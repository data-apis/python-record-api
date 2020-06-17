from typing import *


def cut(
    x: Union[
        (
            range,
            xarray.core.dataarray.DataArray,
            pandas.core.indexes.datetimes.DatetimeIndex,
            numpy.ndarray,
            numpy.flatiter,
        )
    ],
    bins,
    right: bool = ...,
    labels: None = ...,
    precision: int = ...,
    include_lowest: bool = ...,
):
    "usage.xarray: 12"
