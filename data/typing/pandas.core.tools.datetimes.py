from typing import *


@overload
def to_datetime(arg: numpy.ndarray):
    """
    usage.xarray: 1
    """
    ...


@overload
def to_datetime(arg: List[Literal["NaT", "2000-01-02", "2000-01-01"]]):
    """
    usage.xarray: 2
    """
    ...


@overload
def to_datetime(arg: List[Literal["NaT"]]):
    """
    usage.xarray: 1
    """
    ...


@overload
def to_datetime(arg: List[Literal["2000-01-01T00:00:00Z", "NaT"]]):
    """
    usage.xarray: 1
    """
    ...


@overload
def to_datetime(
    arg: List[Literal["2000-01-02T00:00:00Z", "2000-01-01T00:00:00Z", "NaT"]]
):
    """
    usage.xarray: 1
    """
    ...


@overload
def to_datetime(arg: List[Literal["2000-01-03T06", "2000-01-02T18", "2000-01-01T18"]]):
    """
    usage.xarray: 1
    """
    ...


@overload
def to_datetime(arg: List[Literal["2002", "2000", "2001"]]):
    """
    usage.xarray: 1
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
