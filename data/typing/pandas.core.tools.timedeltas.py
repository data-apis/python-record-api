from typing import *


@overload
def to_timedelta(arg: object, unit: str = ...):
    """
    usage.xarray: 54
    """
    ...


@overload
def to_timedelta(
    arg: object,
    unit: Literal["ns", "h"] = ...,
    errors: Literal["coerce", "raise"] = ...,
):
    """
    usage.dask: 16
    """
    ...


def to_timedelta(
    arg: object, unit: str = ..., errors: Literal["coerce", "raise"] = ...
):
    """
    usage.dask: 16
    usage.xarray: 54
    """
    ...
