from typing import *


@overload
def to_datetime(
    arg: Literal["13000101"],
    errors: Literal["ignore"],
    format: Literal["%Y%m%d"],
    unit: None,
    infer_datetime_format: bool,
    origin: Literal["unix"],
):
    """
    usage.koalas: 1
    """
    ...


@overload
def to_datetime(
    arg: Literal["13000101"],
    errors: Literal["coerce"],
    format: Literal["%Y%m%d"],
    unit: None,
    infer_datetime_format: bool,
    origin: Literal["unix"],
):
    """
    usage.koalas: 1
    """
    ...


@overload
def to_datetime(
    arg: int,
    errors: Literal["raise"],
    format: None,
    unit: Literal["s"],
    infer_datetime_format: bool,
    origin: Literal["unix"],
):
    """
    usage.koalas: 1
    """
    ...


@overload
def to_datetime(
    arg: int,
    errors: Literal["raise"],
    format: None,
    unit: Literal["ns"],
    infer_datetime_format: bool,
    origin: Literal["unix"],
):
    """
    usage.koalas: 1
    """
    ...


@overload
def to_datetime(
    arg: List[int],
    errors: Literal["raise"],
    format: None,
    unit: Literal["D"],
    infer_datetime_format: bool,
    origin: pandas._libs.tslibs.timestamps.Timestamp,
):
    """
    usage.koalas: 1
    """
    ...


@overload
def to_datetime(arg: pandas.core.frame.DataFrame):
    """
    usage.dask: 2
    usage.koalas: 2
    """
    ...


@overload
def to_datetime(arg: Dict[Literal["day", "month", "year"], Dict[int, int]]):
    """
    usage.koalas: 1
    """
    ...


@overload
def to_datetime(
    arg: Dict[Literal["day", "month", "year"], Dict[int, int]],
    errors: Literal["raise"],
    format: None,
    unit: None,
    infer_datetime_format: bool,
    origin: Literal["unix"],
):
    """
    usage.koalas: 1
    """
    ...


@overload
def to_datetime(arg: int, unit: Literal["s"]):
    """
    usage.koalas: 1
    """
    ...


@overload
def to_datetime(arg: int, unit: Literal["ns"]):
    """
    usage.dask: 3
    usage.koalas: 1
    """
    ...


@overload
def to_datetime(
    arg: List[int], unit: Literal["D"], origin: pandas._libs.tslibs.timestamps.Timestamp
):
    """
    usage.koalas: 1
    """
    ...


@overload
def to_datetime(arg: pandas.core.series.Series, infer_datetime_format: bool):
    """
    usage.dask: 2
    usage.koalas: 1
    """
    ...


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
def to_datetime(arg: dask.dataframe.core.DataFrame):
    """
    usage.dask: 1
    """
    ...


@overload
def to_datetime(arg: dask.dataframe.core.Series, infer_datetime_format: bool):
    """
    usage.dask: 1
    """
    ...


@overload
def to_datetime(arg: pandas.core.indexes.base.Index, infer_datetime_format: bool):
    """
    usage.dask: 3
    """
    ...


@overload
def to_datetime(arg: dask.dataframe.core.Index, infer_datetime_format: bool):
    """
    usage.dask: 1
    """
    ...


@overload
def to_datetime(arg: str):
    """
    usage.dask: 6
    """
    ...


@overload
def to_datetime(arg: numpy.ndarray, unit: Literal["ns"]):
    """
    usage.dask: 1
    """
    ...


@overload
def to_datetime(arg: pandas.core.series.Series, utc: bool):
    """
    usage.dask: 1
    """
    ...


def to_datetime(
    arg: object,
    errors: Literal["raise", "coerce", "ignore"] = ...,
    format: Union[None, Literal["%Y%m%d"]] = ...,
    unit: Union[Literal["ns", "D", "s"], None] = ...,
    infer_datetime_format: bool = ...,
    origin: Union[pandas._libs.tslibs.timestamps.Timestamp, Literal["unix"]] = ...,
):
    """
    usage.dask: 21
    usage.koalas: 13
    usage.xarray: 8
    """
    ...
