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
    usage.statsmodels: 2
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
def to_datetime(arg: List[int]):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def to_datetime(
    arg: List[
        Literal["2016-03-01 12:00:00", "2016-02-01 12:00:00", "2016-01-01 12:00:00"]
    ]
):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def to_datetime(arg: pandas.core.indexes.base.Index):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def to_datetime(
    arg: List[
        Literal[
            "1950-01-05 00:00:00",
            "1950-01-04 00:00:00",
            "1950-01-03 00:00:00",
            "1950-01-02 00:00:00",
            "1950-01-01 00:00:00",
        ]
    ]
):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def to_datetime(
    arg: List[
        Literal[
            "1950-01-29 00:00:00",
            "1950-01-22 00:00:00",
            "1950-01-15 00:00:00",
            "1950-01-08 00:00:00",
            "1950-01-01 00:00:00",
        ]
    ]
):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def to_datetime(
    arg: List[
        Literal[
            "1950-05-31 00:00:00",
            "1950-04-30 00:00:00",
            "1950-03-31 00:00:00",
            "1950-02-28 00:00:00",
            "1950-01-31 00:00:00",
        ]
    ]
):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def to_datetime(
    arg: List[
        Literal[
            "1951-03-31 00:00:00",
            "1950-12-31 00:00:00",
            "1950-09-30 00:00:00",
            "1950-06-30 00:00:00",
            "1950-03-31 00:00:00",
        ]
    ]
):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def to_datetime(
    arg: List[
        Literal[
            "1954-12-31 00:00:00",
            "1953-12-31 00:00:00",
            "1952-12-31 00:00:00",
            "1951-12-31 00:00:00",
            "1950-12-31 00:00:00",
        ]
    ]
):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def to_datetime(
    arg: List[
        Literal[
            "1952-03-31 00:00:00",
            "1951-09-30 00:00:00",
            "1951-03-31 00:00:00",
            "1950-09-30 00:00:00",
            "1950-03-31 00:00:00",
        ]
    ]
):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def to_datetime(
    arg: List[
        Literal[
            "1952-01-01 00:00:00",
            "1951-07-01 00:00:00",
            "1951-01-01 00:00:00",
            "1950-07-01 00:00:00",
            "1950-01-01 00:00:00",
        ]
    ]
):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def to_datetime(
    arg: List[
        Literal[
            "1950-01-01 00:00:20",
            "1950-01-01 00:00:15",
            "1950-01-01 00:00:10",
            "1950-01-01 00:00:05",
            "1950-01-01 00:00:00",
        ]
    ]
):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def to_datetime(
    arg: List[
        Literal[
            "1950-01-05 00:40:00",
            "1950-01-04 00:30:00",
            "1950-01-03 00:20:00",
            "1950-01-02 00:10:00",
            "1950-01-01 00:00:00",
        ]
    ]
):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def to_datetime(
    arg: List[
        Literal[
            "1950-01-05T00:00:00",
            "1950-01-04T00:00:00",
            "1950-01-03T00:00:00",
            "1950-01-02T00:00:00",
            "1950-01-01T00:00:00",
        ]
    ]
):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def to_datetime(
    arg: List[
        Literal[
            "1950-01-29T00:00:00",
            "1950-01-22T00:00:00",
            "1950-01-15T00:00:00",
            "1950-01-08T00:00:00",
            "1950-01-01T00:00:00",
        ]
    ]
):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def to_datetime(
    arg: List[
        Literal[
            "1950-05-31T00:00:00",
            "1950-04-30T00:00:00",
            "1950-03-31T00:00:00",
            "1950-02-28T00:00:00",
            "1950-01-31T00:00:00",
        ]
    ]
):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def to_datetime(
    arg: List[
        Literal[
            "1951-03-31T00:00:00",
            "1950-12-31T00:00:00",
            "1950-09-30T00:00:00",
            "1950-06-30T00:00:00",
            "1950-03-31T00:00:00",
        ]
    ]
):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def to_datetime(
    arg: List[
        Literal[
            "1954-12-31T00:00:00",
            "1953-12-31T00:00:00",
            "1952-12-31T00:00:00",
            "1951-12-31T00:00:00",
            "1950-12-31T00:00:00",
        ]
    ]
):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def to_datetime(
    arg: List[
        Literal[
            "1952-03-31T00:00:00",
            "1951-09-30T00:00:00",
            "1951-03-31T00:00:00",
            "1950-09-30T00:00:00",
            "1950-03-31T00:00:00",
        ]
    ]
):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def to_datetime(
    arg: List[
        Literal[
            "1952-01-01T00:00:00",
            "1951-07-01T00:00:00",
            "1951-01-01T00:00:00",
            "1950-07-01T00:00:00",
            "1950-01-01T00:00:00",
        ]
    ]
):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def to_datetime(
    arg: List[
        Literal[
            "1950-01-01T00:00:20",
            "1950-01-01T00:00:15",
            "1950-01-01T00:00:10",
            "1950-01-01T00:00:05",
            "1950-01-01T00:00:00",
        ]
    ]
):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def to_datetime(
    arg: List[
        Literal[
            "1950-01-05T00:40:00",
            "1950-01-04T00:30:00",
            "1950-01-03T00:20:00",
            "1950-01-02T00:10:00",
            "1950-01-01T00:00:00",
        ]
    ]
):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def to_datetime(arg: List[Literal["e", "d", "c", "b", "a"]]):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def to_datetime(arg: List[Union[dict, float, int, Literal["a"], Type[str]]]):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def to_datetime(arg: List[Literal["2016-12-25"]]):
    """
    usage.prophet: 4
    """
    ...


@overload
def to_datetime(arg: None):
    """
    usage.prophet: 1
    """
    ...


@overload
def to_datetime(arg: pandas.core.series.Series):
    """
    usage.prophet: 4
    usage.pyjanitor: 1
    """
    ...


@overload
def to_datetime(arg: pandas.core.indexes.datetimes.DatetimeIndex):
    """
    usage.prophet: 1
    """
    ...


@overload
def to_datetime(arg: List[Literal["2017-01-02"]]):
    """
    usage.prophet: 2
    """
    ...


@overload
def to_datetime(arg: List[Literal["2013-06-06"]]):
    """
    usage.prophet: 1
    """
    ...


@overload
def to_datetime(arg: List[Literal["2013-06-06", "2012-06-06"]]):
    """
    usage.prophet: 2
    """
    ...


@overload
def to_datetime(arg: Literal["02/01/19"], format: None):
    """
    usage.pyjanitor: 1
    """
    ...


@overload
def to_datetime(arg: Literal["02/02/19"], format: None):
    """
    usage.pyjanitor: 1
    """
    ...


@overload
def to_datetime(arg: Literal["01@@@@29@@@@19"], format: Literal["%m@@@@%d@@@@%y"]):
    """
    usage.pyjanitor: 1
    """
    ...


@overload
def to_datetime(arg: pandas.core.series.Series, dayfirst: bool):
    """
    usage.pyjanitor: 1
    """
    ...


@overload
def to_datetime(arg: Literal["01/29/19"], format: None):
    """
    usage.pyjanitor: 1
    """
    ...


@overload
def to_datetime(arg: pandas.core.series.Series, format: Literal["%Y%m%d"]):
    """
    usage.pyjanitor: 1
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
    format: Union[None, Literal["%Y%m%d", "%m@@@@%d@@@@%y"]] = ...,
    unit: Union[Literal["ns", "D", "s"], None] = ...,
    infer_datetime_format: bool = ...,
    origin: Union[pandas._libs.tslibs.timestamps.Timestamp, Literal["unix"]] = ...,
):
    """
    usage.dask: 21
    usage.koalas: 13
    usage.prophet: 15
    usage.pyjanitor: 7
    usage.statsmodels: 25
    usage.xarray: 8
    """
    ...
