from typing import *


@overload
def to_timedelta(arg: numpy.int64, unit: Literal["D"]):
    """
    usage.xarray: 2
    """
    ...


@overload
def to_timedelta(arg: numpy.ndarray, unit: Literal["ns"]):
    """
    usage.xarray: 1
    """
    ...


@overload
def to_timedelta(arg: numpy.float64, unit: Literal["D"]):
    """
    usage.xarray: 2
    """
    ...


@overload
def to_timedelta(arg: numpy.ndarray):
    """
    usage.xarray: 2
    """
    ...


@overload
def to_timedelta(arg: List[Literal["NaT", "2h", "1h"]]):
    """
    usage.xarray: 1
    """
    ...


@overload
def to_timedelta(arg: numpy.ndarray, unit: Literal["h"]):
    """
    usage.xarray: 3
    """
    ...


@overload
def to_timedelta(arg: numpy.int64, unit: Literal["h"]):
    """
    usage.xarray: 2
    """
    ...


@overload
def to_timedelta(arg: numpy.int16, unit: Literal["h"]):
    """
    usage.xarray: 2
    """
    ...


@overload
def to_timedelta(arg: numpy.int32, unit: Literal["D"]):
    """
    usage.xarray: 2
    """
    ...


@overload
def to_timedelta(arg: List[int]):
    """
    usage.xarray: 4
    """
    ...


@overload
def to_timedelta(arg: numpy.float32, unit: Literal["D"]):
    """
    usage.xarray: 2
    """
    ...


@overload
def to_timedelta(arg: List[datetime.timedelta]):
    """
    usage.xarray: 3
    """
    ...


@overload
def to_timedelta(arg: numpy.float64, unit: Literal["h"]):
    """
    usage.xarray: 2
    """
    ...


@overload
def to_timedelta(arg: numpy.int64, unit: Literal["ms"]):
    """
    usage.xarray: 2
    """
    ...


@overload
def to_timedelta(arg: numpy.int64, unit: Literal["us"]):
    """
    usage.xarray: 2
    """
    ...


@overload
def to_timedelta(arg: numpy.int32, unit: Literal["s"]):
    """
    usage.xarray: 2
    """
    ...


@overload
def to_timedelta(arg: Literal["1D"]):
    """
    usage.xarray: 1
    """
    ...


@overload
def to_timedelta(arg: numpy.ndarray, unit: Literal["D"]):
    """
    usage.xarray: 2
    """
    ...


@overload
def to_timedelta(arg: List[Literal["3D", "2D", "1D"]]):
    """
    usage.xarray: 1
    """
    ...


@overload
def to_timedelta(arg: Literal["1h"]):
    """
    usage.xarray: 1
    """
    ...


@overload
def to_timedelta(arg: Literal["1ms"]):
    """
    usage.xarray: 1
    """
    ...


@overload
def to_timedelta(arg: numpy.ndarray, unit: Literal["ms"]):
    """
    usage.xarray: 1
    """
    ...


@overload
def to_timedelta(arg: Literal["1us"]):
    """
    usage.xarray: 1
    """
    ...


@overload
def to_timedelta(arg: numpy.ndarray, unit: Literal["us"]):
    """
    usage.xarray: 1
    """
    ...


@overload
def to_timedelta(arg: List[Literal["1s", "0s", "NaT"]]):
    """
    usage.xarray: 1
    """
    ...


@overload
def to_timedelta(arg: List[Literal["60m", "30m"]]):
    """
    usage.xarray: 1
    """
    ...


@overload
def to_timedelta(arg: List[Literal["NaT"]]):
    """
    usage.xarray: 1
    """
    ...


@overload
def to_timedelta(arg: List[Literal["1 day"]]):
    """
    usage.xarray: 1
    """
    ...


@overload
def to_timedelta(arg: numpy.ndarray, unit: Literal["days"]):
    """
    usage.xarray: 1
    """
    ...


@overload
def to_timedelta(arg: Literal["1 day"]):
    """
    usage.xarray: 1
    """
    ...


@overload
def to_timedelta(arg: List[Literal["NaT", "1s", "0s"]]):
    """
    usage.xarray: 1
    """
    ...


@overload
def to_timedelta(arg: List[Literal["0 hours", "1 day", "1 day 1 hour"]]):
    """
    usage.xarray: 1
    """
    ...


@overload
def to_timedelta(arg: Literal["huh"]):
    """
    usage.xarray: 1
    """
    ...


@overload
def to_timedelta(arg: Literal["3H"]):
    """
    usage.xarray: 1
    """
    ...


@overload
def to_timedelta(arg: Literal["1s"]):
    """
    usage.xarray: 1
    """
    ...


@overload
def to_timedelta(arg: List[Union[int, float]]):
    """
    usage.dask: 1
    """
    ...


@overload
def to_timedelta(arg: List[Union[float, int]]):
    """
    usage.dask: 1
    """
    ...


@overload
def to_timedelta(arg: numpy.float64):
    """
    usage.dask: 2
    """
    ...


@overload
def to_timedelta(arg: numpy.int64):
    """
    usage.dask: 2
    """
    ...


@overload
def to_timedelta(arg: float):
    """
    usage.dask: 1
    """
    ...


@overload
def to_timedelta(arg: pandas.core.series.Series):
    """
    usage.dask: 1
    """
    ...


@overload
def to_timedelta(arg: dask.dataframe.core.Series):
    """
    usage.dask: 1
    """
    ...


@overload
def to_timedelta(
    arg: pandas.core.series.Series, unit: Literal["ns"], errors: Literal["raise"]
):
    """
    usage.dask: 1
    """
    ...


@overload
def to_timedelta(arg: pandas.core.series.Series, unit: Literal["h"]):
    """
    usage.dask: 1
    """
    ...


@overload
def to_timedelta(arg: dask.dataframe.core.Series, unit: Literal["h"]):
    """
    usage.dask: 1
    """
    ...


@overload
def to_timedelta(
    arg: pandas.core.series.Series, unit: Literal["h"], errors: Literal["raise"]
):
    """
    usage.dask: 1
    """
    ...


@overload
def to_timedelta(arg: pandas.core.series.Series, errors: Literal["coerce"]):
    """
    usage.dask: 1
    """
    ...


@overload
def to_timedelta(arg: dask.dataframe.core.Series, errors: Literal["coerce"]):
    """
    usage.dask: 1
    """
    ...


@overload
def to_timedelta(
    arg: pandas.core.series.Series, unit: Literal["ns"], errors: Literal["coerce"]
):
    """
    usage.dask: 1
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
