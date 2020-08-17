from typing import *


@overload
def to_datetime(arg: Union[List[str], numpy.ndarray]):
    """
    usage.xarray: 8
    """
    ...


@overload
def to_datetime(
    arg: object,
    infer_datetime_format: bool = ...,
    unit: Literal["ns"] = ...,
    utc: bool = ...,
):
    """
    usage.dask: 21
    """
    ...


def to_datetime(
    arg: object,
    infer_datetime_format: bool = ...,
    unit: Literal["ns"] = ...,
    utc: bool = ...,
):
    """
    usage.dask: 21
    usage.xarray: 8
    """
    ...
