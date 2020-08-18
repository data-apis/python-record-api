from typing import *


@overload
def date_range(start: Literal["2000-01-01"], periods: int):
    """
    usage.xarray: 27
    """
    ...


@overload
def date_range(start: Literal["1999-01-05"], periods: int):
    """
    usage.xarray: 1
    """
    ...


@overload
def date_range(start: Literal["2000-02-01"], periods: int):
    """
    usage.xarray: 1
    """
    ...


@overload
def date_range(start: Literal["2010-01-01"], periods: int, freq: Literal["1D"]):
    """
    usage.xarray: 1
    """
    ...


@overload
def date_range(start: Literal["2000-02-01"], periods: int, freq: Literal["A"]):
    """
    usage.xarray: 2
    """
    ...


@overload
def date_range(start: Literal["2000-02-01"], periods: int, freq: Literal["M"]):
    """
    usage.xarray: 2
    """
    ...


@overload
def date_range(start: Literal["2000-02-01"], periods: int, freq: Literal["D"]):
    """
    usage.xarray: 2
    """
    ...


@overload
def date_range(start: Literal["2000"], periods: int):
    """
    usage.dask: 1
    usage.xarray: 5
    """
    ...


@overload
def date_range(
    start: Literal["2000-01-02T01:03:51"], periods: int, freq: Literal["1777S"]
):
    """
    usage.xarray: 1
    """
    ...


@overload
def date_range(
    start: Literal["2000-01-01T12:07:01"], periods: int, freq: Literal["8003D"]
):
    """
    usage.xarray: 1
    """
    ...


@overload
def date_range(
    start: Literal["2000-01-01T12:07:01"], periods: int, freq: Literal["6H"]
):
    """
    usage.xarray: 1
    """
    ...


@overload
def date_range(
    start: Literal["2000-01-01T12:07:01"], periods: int, freq: Literal["3D"]
):
    """
    usage.xarray: 1
    """
    ...


@overload
def date_range(
    start: Literal["2000-01-01T12:07:01"], periods: int, freq: Literal["11D"]
):
    """
    usage.xarray: 1
    """
    ...


@overload
def date_range(
    start: Literal["2000-01-01T12:07:01"], periods: int, freq: Literal["3MS"]
):
    """
    usage.xarray: 1
    """
    ...


@overload
def date_range(
    start: Literal["2000-01-01T12:07:01"], periods: int, freq: Literal["7M"]
):
    """
    usage.xarray: 1
    """
    ...


@overload
def date_range(
    start: Literal["2000-01-01T12:07:01"], periods: int, freq: Literal["43QS-AUG"]
):
    """
    usage.xarray: 1
    """
    ...


@overload
def date_range(
    start: Literal["2000-01-01T12:07:01"], periods: int, freq: Literal["11Q-JUN"]
):
    """
    usage.xarray: 1
    """
    ...


@overload
def date_range(
    start: Literal["2000-01-01T12:07:01"], periods: int, freq: Literal["3AS-MAR"]
):
    """
    usage.xarray: 1
    """
    ...


@overload
def date_range(
    start: Literal["2000-01-01T12:07:01"], periods: int, freq: Literal["7A-MAY"]
):
    """
    usage.xarray: 1
    """
    ...


@overload
def date_range(
    start: Literal["2004-01-01T12:07:01"], periods: int, freq: Literal["3D"]
):
    """
    usage.xarray: 1
    """
    ...


@overload
def date_range(start: Literal["1970-01-01"], periods: int, freq: Literal["h"]):
    """
    usage.xarray: 1
    """
    ...


@overload
def date_range(start: Literal["2000-01-01"], periods: int, freq: Literal["h"]):
    """
    usage.xarray: 1
    """
    ...


@overload
def date_range(
    start: Literal["2001-04-01-00"], end: Literal["2001-04-30-23"], freq: Literal["H"]
):
    """
    usage.xarray: 2
    """
    ...


@overload
def date_range(
    start: Literal["2001-04-01"], end: Literal["2001-04-05"], freq: Literal["D"]
):
    """
    usage.xarray: 2
    """
    ...


@overload
def date_range(
    start: Literal["2001-05-01"], end: Literal["2001-05-05"], freq: Literal["D"]
):
    """
    usage.xarray: 2
    """
    ...


@overload
def date_range(start: Literal["2000-01-16"], periods: int):
    """
    usage.xarray: 1
    """
    ...


@overload
def date_range(start: Literal["2000-01-01"], periods: int, freq: Literal["MS"]):
    """
    usage.xarray: 1
    """
    ...


@overload
def date_range(start: Literal["2100"], periods: int):
    """
    usage.xarray: 1
    """
    ...


@overload
def date_range(start: Literal["2000-01-01"], periods: int, freq: Literal["D"]):
    """
    usage.xarray: 2
    """
    ...


@overload
def date_range(start: Literal["2000-01-01"], periods: int, freq: Literal["6H"]):
    """
    usage.xarray: 20
    """
    ...


@overload
def date_range(start: Literal["2000"], periods: int, freq: Literal["D"]):
    """
    usage.dask: 1
    usage.xarray: 2
    """
    ...


@overload
def date_range(start: Literal["2000-01-01"], periods: int, freq: Literal["1D"]):
    """
    usage.xarray: 1
    """
    ...


@overload
def date_range(
    start: Literal["2007-02-01"], end: Literal["2007-03-01"], freq: Literal["D"]
):
    """
    usage.xarray: 1
    """
    ...


@overload
def date_range(
    start: Literal["2016-01-01"], end: Literal["2016-03-31"], freq: Literal["1D"]
):
    """
    usage.xarray: 1
    """
    ...


@overload
def date_range(start: Literal["20130101"], periods: int):
    """
    usage.dask: 2
    usage.xarray: 5
    """
    ...


@overload
def date_range(start: Literal["2000"], periods: int, freq: Literal["2MS"]):
    """
    usage.xarray: 1
    """
    ...


@overload
def date_range(start: Literal["2000-01-01"], periods: int, freq: Literal["H"]):
    """
    usage.xarray: 1
    """
    ...


@overload
def date_range(start: Literal["1/1/2011"], periods: int, freq: Literal["H"]):
    """
    usage.xarray: 1
    """
    ...


@overload
def date_range(start: Literal["2000-01-01"], periods: int, freq: Literal["M"]):
    """
    usage.xarray: 1
    """
    ...


@overload
def date_range(start: Literal["20100101"], periods: int):
    """
    usage.dask: 2
    usage.xarray: 1
    """
    ...


@overload
def date_range(start: Literal["2000-01-01"], periods: int, freq: Literal["3H"]):
    """
    usage.xarray: 1
    """
    ...


@overload
def date_range(start: Literal["20130101"], periods: int, tz: Literal["US/Eastern"]):
    """
    usage.dask: 2
    usage.xarray: 1
    """
    ...


@overload
def date_range(start: Literal["15/12/1999"], periods: int):
    """
    usage.xarray: 1
    """
    ...


@overload
def date_range(start: Literal["2000"], periods: int, freq: Literal["7D"]):
    """
    usage.xarray: 2
    """
    ...


@overload
def date_range(
    start: Literal["2010-08-01"], end: Literal["2010-08-15"], freq: Literal["15min"]
):
    """
    usage.xarray: 1
    """
    ...


@overload
def date_range(
    start: Literal["2010-08-01"], end: Literal["2010-08-15"], freq: Literal["24H"]
):
    """
    usage.xarray: 1
    """
    ...


@overload
def date_range(start: Literal["01-01-2001"], periods: int, freq: Literal["D"]):
    """
    usage.xarray: 1
    """
    ...


@overload
def date_range(start: Literal["01-01-2001"], periods: int, freq: Literal["H"]):
    """
    usage.xarray: 1
    """
    ...


@overload
def date_range(start: Literal["2001-01-01"], periods: int, freq: Literal["H"]):
    """
    usage.xarray: 2
    """
    ...


@overload
def date_range(start: Literal["20000101"], periods: int):
    """
    usage.xarray: 2
    """
    ...


@overload
def date_range(start: Literal["2000-01-01"], end: Literal["2000-01-10"]):
    """
    usage.xarray: 2
    """
    ...


@overload
def date_range(start: Literal["2000-1-1"], periods: int):
    """
    usage.xarray: 1
    """
    ...


@overload
def date_range(
    start: Literal["15/12/1999"],
    periods: int,
    freq: pandas._libs.tslibs.offsets.DateOffset,
):
    """
    usage.xarray: 1
    """
    ...


@overload
def date_range(start: Literal["2011-09-01"], periods: int):
    """
    usage.xarray: 1
    """
    ...


@overload
def date_range(start: Literal["10-09-2010"], periods: int, freq: Literal["1y"]):
    """
    usage.xarray: 2
    """
    ...


@overload
def date_range(
    start: Literal["2000-01-01"], periods: int, freq: Literal["1h"], tz: object
):
    """
    usage.xarray: 1
    """
    ...


@overload
def date_range(
    start: Literal["1970-01-01"],
    periods: int,
    freq: None,
    tz: None,
    name: Literal["Date"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(start: Literal["2000"], end: Literal["2015"], freq: Literal["6M"]):
    """
    usage.dask: 2
    """
    ...


@overload
def date_range(
    start: Literal["2000"],
    end: Literal["2000"],
    freq: Literal["1H"],
    name: Literal["timestamp"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(start: Literal["2000"], end: Literal["2015"], freq: Literal["3M"]):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(
    start: Literal["2000-01-01"], end: Literal["2000-12-31"], freq: Literal["1M"]
):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(start: Literal["2000"], end: Literal["2001"], freq: Literal["3M"]):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(
    start: Literal["1970-01-01"],
    periods: int,
    freq: pandas._libs.tslibs.offsets.Hour,
    tz: None,
    name: Literal["timestamp"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(start: Literal["2000"], end: Literal["2001"], freq: Literal["6M"]):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(
    start: pandas._libs.tslibs.timestamps.Timestamp,
    end: pandas._libs.tslibs.timestamps.Timestamp,
    freq: Literal["1D"],
    name: Literal["timestamp"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(start: Literal["20120101"], periods: int):
    """
    usage.dask: 2
    """
    ...


@overload
def date_range(start: Literal["2019-01-01"], periods: int, freq: Literal["1T"]):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(
    start: Literal["1970-01-01"],
    periods: int,
    freq: None,
    tz: None,
    name: Literal["date"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(start: Literal["2011-01-01"], periods: int, freq: Literal["D"]):
    """
    usage.dask: 3
    """
    ...


@overload
def date_range(
    start: Literal["1970-01-01"],
    periods: int,
    freq: pandas._libs.tslibs.offsets.Day,
    tz: None,
    name: None,
):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(start: Literal["2000"], periods: int, freq: Literal["B"]):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(
    start: Literal["1970-01-01"], periods: int, freq: None, tz: None, name: None
):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(
    start: Literal["1970-01-01"],
    periods: int,
    freq: pandas._libs.tslibs.offsets.BusinessDay,
    tz: None,
    name: None,
):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(
    start: pandas._libs.tslibs.timestamps.Timestamp,
    end: pandas._libs.tslibs.timestamps.Timestamp,
    freq: Literal["15s"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(
    start: Literal["2015-01-01 00:00"],
    end: Literal[" 2015-05-01 23:50"],
    freq: Literal["10min"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(
    start: pandas._libs.tslibs.timestamps.Timestamp,
    end: pandas._libs.tslibs.timestamps.Timestamp,
    freq: Literal["1M"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(start: Literal["2016-01-01"], periods: int):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(start: Literal["2015-01-01"], periods: int, freq: Literal["1T"]):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(start: Literal["2000"], periods: int, freq: Literal["H"]):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(
    start: Literal["1970-01-01"],
    periods: int,
    freq: pandas._libs.tslibs.offsets.Hour,
    tz: None,
    name: None,
):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(
    start: Literal["1/1/2000"], end: Literal["1/1/2001"], freq: Literal["12h"]
):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(
    start: Literal["1/1/2000"], end: Literal["1/1/2001"], freq: Literal["D"]
):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(start: Literal["01.01.2015"], end: Literal["05.05.2015"]):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(
    start: Literal["2000-01-01"], end: Literal["2000-01-31"], freq: Literal["1d"]
):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(
    start: pandas._libs.tslibs.timestamps.Timestamp,
    end: pandas._libs.tslibs.timestamps.Timestamp,
    freq: Literal["1s"],
    name: Literal["timestamp"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(start: int, periods: int):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(
    start: Literal["2000-01-01"], end: Literal["2000-04-01"], freq: Literal["1D"]
):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(
    start: Literal["2016-01-01"], end: Literal["2016-01-31"], freq: Literal["12h"]
):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(start: Literal["2011-01-01"], periods: int, freq: Literal["H"]):
    """
    usage.dask: 5
    """
    ...


@overload
def date_range(
    start: Literal["1970-01-01"],
    periods: int,
    freq: None,
    tz: None,
    name: Literal["time"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(
    start: Literal["1970-01-01"],
    periods: int,
    freq: pandas._libs.tslibs.offsets.Day,
    tz: None,
    name: Literal["time"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(start: Literal["2019-08-01"], periods: int, freq: Literal["1D"]):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(
    start: Literal["2016-01-01 00:00:00"], periods: int, freq: Literal["1s"]
):
    """
    usage.dask: 2
    """
    ...


@overload
def date_range(
    start: Literal["1970-01-01"], periods: int, freq: None, tz: None, name: Literal["a"]
):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(
    start: Literal["1970-01-01"],
    periods: int,
    freq: pandas._libs.tslibs.offsets.Day,
    tz: None,
    name: Literal["a"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(start: Literal["2000"], end: Literal["2004"], freq: Literal["1M"]):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(
    start: pandas._libs.tslibs.timestamps.Timestamp,
    end: pandas._libs.tslibs.timestamps.Timestamp,
    freq: Literal["2H"],
    name: Literal["timestamp"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(
    start: Literal["1970-01-01"],
    periods: int,
    freq: None,
    tz: None,
    name: Literal["timestamp"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(
    start: Literal["1970-01-01"],
    periods: int,
    freq: None,
    tz: None,
    name: Literal["notz"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(
    start: Literal["1970-01-01"],
    periods: int,
    freq: pandas._libs.tslibs.offsets.Day,
    tz: object,
    name: Literal["tz"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(
    start: Literal["1970-01-01"], periods: int, freq: None, tz: None, name: Literal["x"]
):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(start: Literal["2000"], periods: int, tz: Literal["US/Central"]):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(
    start: Literal["1970-01-01"],
    periods: int,
    freq: None,
    tz: object,
    name: Literal["A"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(start: Literal["2000"], end: Literal["2001"], freq: Literal["1M"]):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(
    start: Literal["2016-01-01"], periods: int, tz: Literal["America/New_York"]
):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(
    start: Literal["1970-01-01"],
    periods: int,
    freq: pandas._libs.tslibs.offsets.Day,
    tz: object,
    name: Literal["foo"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(
    start: Literal["1-1-2000"], end: Literal["2-15-2000"], freq: Literal["h"]
):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(
    start: Literal["4-15-2000"], end: Literal["5-15-2000"], freq: Literal["h"]
):
    """
    usage.dask: 2
    """
    ...


@overload
def date_range(
    start: pandas._libs.tslibs.timestamps.Timestamp,
    end: pandas._libs.tslibs.timestamps.Timestamp,
    freq: pandas._libs.tslibs.offsets.Minute,
    name: None,
    closed: Literal["left"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(
    start: pandas._libs.tslibs.timestamps.Timestamp,
    end: pandas._libs.tslibs.timestamps.Timestamp,
    freq: pandas._libs.tslibs.offsets.Minute,
    name: None,
    closed: None,
):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(
    start: pandas._libs.tslibs.timestamps.Timestamp,
    end: pandas._libs.tslibs.timestamps.Timestamp,
    freq: pandas._libs.tslibs.offsets.Hour,
    name: None,
    closed: Literal["left"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(
    start: pandas._libs.tslibs.timestamps.Timestamp,
    end: pandas._libs.tslibs.timestamps.Timestamp,
    freq: pandas._libs.tslibs.offsets.Hour,
    name: None,
    closed: None,
):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(
    start: pandas._libs.tslibs.timestamps.Timestamp,
    end: pandas._libs.tslibs.timestamps.Timestamp,
    freq: pandas._libs.tslibs.offsets.Day,
    name: None,
    closed: Literal["left"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(
    start: pandas._libs.tslibs.timestamps.Timestamp,
    end: pandas._libs.tslibs.timestamps.Timestamp,
    freq: pandas._libs.tslibs.offsets.Day,
    name: None,
    closed: None,
):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(
    start: pandas._libs.tslibs.timestamps.Timestamp,
    end: pandas._libs.tslibs.timestamps.Timestamp,
    freq: pandas._libs.tslibs.offsets.Week,
    name: None,
    closed: None,
):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(
    start: pandas._libs.tslibs.timestamps.Timestamp,
    end: pandas._libs.tslibs.timestamps.Timestamp,
    freq: pandas._libs.tslibs.offsets.Week,
    name: None,
    closed: Literal["left"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(
    start: pandas._libs.tslibs.timestamps.Timestamp,
    end: pandas._libs.tslibs.timestamps.Timestamp,
    freq: pandas._libs.tslibs.offsets.MonthEnd,
    name: None,
    closed: Literal["left"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(
    start: pandas._libs.tslibs.timestamps.Timestamp,
    end: pandas._libs.tslibs.timestamps.Timestamp,
    freq: pandas._libs.tslibs.offsets.MonthEnd,
    name: None,
    closed: None,
):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(
    start: Literal["2000-01-01"], end: Literal["2000-02-15"], freq: Literal["h"]
):
    """
    usage.dask: 4
    """
    ...


@overload
def date_range(
    start: Literal["1-1-2000"], end: Literal["2-15-2000"], freq: Literal["D"]
):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(
    start: Literal["4-15-2000"], end: Literal["5-15-2000"], freq: Literal["D"]
):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(
    start: Literal["1970-01-01"],
    periods: int,
    freq: None,
    tz: pytz.UTC,
    name: Literal["Time"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(
    start: Literal["1970-01-01"],
    periods: int,
    freq: pandas._libs.tslibs.offsets.Day,
    tz: pytz.UTC,
    name: Literal["Time"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(
    start: Literal["2012-01-02"], end: Literal["2012-02-02"], freq: Literal["H"]
):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(
    start: Literal["2012-03-02"], end: Literal["2012-04-02"], freq: Literal["H"]
):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(
    start: Literal["2012-01-02 00:00:00"],
    end: Literal["2012-01-02 01:00:00"],
    freq: Literal["T"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(
    start: Literal["2012-01-02 06:00:00"],
    end: Literal["2012-01-02 08:00:00"],
    freq: Literal["T"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(
    start: Literal["2020-08-17T23:31:00.596478"],
    end: Literal["2020-09-06T23:31:00.596478"],
    freq: Literal["D"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def date_range(
    start: Literal["1970-01-01"], periods: int, freq: None, tz: object, name: None
):
    """
    usage.dask: 1
    """
    ...


def date_range(
    start: Union[pandas._libs.tslibs.timestamps.Timestamp, int, str],
    periods: int = ...,
    end: Union[pandas._libs.tslibs.timestamps.Timestamp, str] = ...,
    freq: object = ...,
    tz: object = ...,
    name: Union[None, str] = ...,
    closed: Union[None, Literal["left"]] = ...,
):
    """
    usage.dask: 94
    usage.xarray: 122
    """
    ...


class DatetimeIndex:

    # usage.dask: 1
    __module__: ClassVar[object]

    # usage.dask: 2
    __name__: ClassVar[object]

    # usage.dask: 1
    array: object

    # usage.dask: 1
    day: object

    # usage.xarray: 1
    dayofweek: object

    # usage.xarray: 1
    dayofyear: object

    # usage.dask: 4
    # usage.xarray: 5
    dtype: object

    # usage.dask: 4
    freq: None

    # usage.xarray: 1
    hour: object

    # usage.dask: 1
    is_all_dates: object

    # usage.dask: 2
    # usage.xarray: 2
    is_monotonic: object

    # usage.xarray: 2
    is_unique: object

    # usage.dask: 4
    # usage.xarray: 1
    month: object

    # usage.dask: 17
    # usage.xarray: 5
    name: Union[None, Literal["timestamp", "index"]]

    # usage.dask: 1
    names: object

    # usage.xarray: 1
    ndim: object

    # usage.xarray: 1
    shape: object

    # usage.xarray: 5
    size: object

    # usage.xarray: 1
    time: object

    # usage.dask: 2
    tz: object

    # usage.xarray: 16
    values: object

    @overload
    def __add__(self, _0: pandas._libs.tslibs.offsets.Hour, /):
        """
        usage.dask: 1
        usage.xarray: 1
        """
        ...

    @overload
    def __add__(self, _0: datetime.timedelta, /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def __add__(self, _0: Union[numpy.ndarray, numpy.timedelta64, numpy.datetime64], /):
        """
        usage.pandas: 103
        """
        ...

    @overload
    def __add__(self, _0: pandas._libs.tslibs.offsets.Nano, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __add__(self, _0: pandas._libs.tslibs.offsets.Minute, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __add__(self, _0: pandas._libs.tslibs.offsets.Day, /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __add__(self, _0: pandas._libs.tslibs.offsets.Week, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __add__(self, _0: pandas._libs.tslibs.offsets.MonthEnd, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __add__(self, _0: pandas._libs.tslibs.offsets.QuarterEnd, /):
        """
        usage.dask: 1
        """
        ...

    def __add__(self, _0: object, /):
        """
        usage.dask: 8
        usage.pandas: 103
        usage.xarray: 2
        """
        ...

    def __contains__(self, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        """
        usage.dask: 2
        """
        ...

    def __eq__(self, _0: Union[numpy.ndarray, numpy.datetime64], /):
        """
        usage.pandas: 32
        """
        ...

    def __ge__(self, _0: Union[numpy.ndarray, numpy.datetime64], /):
        """
        usage.pandas: 3
        """
        ...

    @overload
    def __getitem__(self, _0: int, /):
        """
        usage.dask: 18
        usage.xarray: 6
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, int, None], /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[int, None, int], /):
        """
        usage.xarray: 2
        """
        ...

    @overload
    def __getitem__(self, _0: slice[int, int, int], /):
        """
        usage.dask: 2
        usage.xarray: 1
        """
        ...

    @overload
    def __getitem__(self, _0: numpy.ndarray, /):
        """
        usage.xarray: 2
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, None, None], /):
        """
        usage.dask: 1
        usage.xarray: 7
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, None, None], /):
        """
        usage.xarray: 1
        """
        ...

    def __getitem__(
        self,
        _0: Union[
            int,
            numpy.ndarray,
            slice[Union[None, int], Union[int, None], Union[None, int]],
        ],
        /,
    ):
        """
        usage.dask: 21
        usage.xarray: 20
        """
        ...

    @overload
    def __gt__(self, _0: Union[numpy.ndarray, numpy.datetime64], /):
        """
        usage.pandas: 2
        """
        ...

    @overload
    def __gt__(self, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        """
        usage.dask: 1
        """
        ...

    def __gt__(
        self,
        _0: Union[
            pandas._libs.tslibs.timestamps.Timestamp, numpy.datetime64, numpy.ndarray
        ],
        /,
    ):
        """
        usage.dask: 1
        usage.pandas: 2
        """
        ...

    def __iadd__(self, _0: Union[numpy.ndarray, numpy.timedelta64], /):
        """
        usage.pandas: 4
        """
        ...

    def __isub__(self, _0: Union[numpy.ndarray, numpy.timedelta64], /):
        """
        usage.pandas: 3
        """
        ...

    def __le__(self, _0: Union[numpy.ndarray, numpy.datetime64], /):
        """
        usage.pandas: 5
        """
        ...

    @overload
    def __lt__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    @overload
    def __lt__(self, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        """
        usage.dask: 1
        """
        ...

    def __lt__(
        self, _0: Union[pandas._libs.tslibs.timestamps.Timestamp, numpy.ndarray], /
    ):
        """
        usage.dask: 1
        usage.pandas: 1
        """
        ...

    def __ne__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 2
        """
        ...

    def __radd__(
        self, _0: Union[numpy.datetime64, numpy.timedelta64, numpy.ndarray], /
    ):
        """
        usage.pandas: 59
        """
        ...

    def __rsub__(
        self, _0: Union[numpy.ndarray, numpy.timedelta64, numpy.datetime64], /
    ):
        """
        usage.pandas: 32
        """
        ...

    @overload
    def __sub__(self, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        """
        usage.xarray: 3
        """
        ...

    @overload
    def __sub__(self, _0: numpy.timedelta64, /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def __sub__(self, _0: Union[numpy.ndarray, numpy.timedelta64, numpy.datetime64], /):
        """
        usage.pandas: 75
        """
        ...

    def __sub__(
        self,
        _0: Union[
            numpy.datetime64,
            numpy.timedelta64,
            numpy.ndarray,
            pandas._libs.tslibs.timestamps.Timestamp,
        ],
        /,
    ):
        """
        usage.pandas: 75
        usage.xarray: 4
        """
        ...

    def ceil(self, /, *args: Literal["v", "t"]):
        """
        usage.xarray: 3
        """
        ...

    def copy(self, /, deep: bool):
        """
        usage.xarray: 1
        """
        ...

    def equals(self, /, other: pandas.core.indexes.datetimes.DatetimeIndex):
        """
        usage.xarray: 2
        """
        ...

    def floor(self, /, *args: Literal["v", "t"]):
        """
        usage.xarray: 3
        """
        ...

    @overload
    def get_indexer(self, /, target: numpy.ndarray, method: None, tolerance: None):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_indexer(
        self, /, target: numpy.ndarray, method: Literal["pad"], tolerance: None
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_indexer(
        self, /, target: numpy.ndarray, method: Literal["backfill"], tolerance: None
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_indexer(
        self, /, target: numpy.ndarray, method: Literal["nearest"], tolerance: None
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_indexer(
        self,
        /,
        target: numpy.ndarray,
        method: Literal["pad"],
        tolerance: Literal["12H"],
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_indexer(
        self,
        /,
        target: numpy.ndarray,
        method: Literal["backfill"],
        tolerance: Literal["12H"],
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_indexer(
        self,
        /,
        target: numpy.ndarray,
        method: Literal["nearest"],
        tolerance: Literal["6H"],
    ):
        """
        usage.xarray: 1
        """
        ...

    def get_indexer(
        self,
        /,
        target: numpy.ndarray,
        method: Union[Literal["nearest", "backfill", "pad"], None],
        tolerance: Union[Literal["6H", "12H"], None],
    ):
        """
        usage.xarray: 7
        """
        ...

    @overload
    def get_loc(self, /, key: numpy.datetime64, method: Literal["nearest"]):
        """
        usage.xarray: 2
        """
        ...

    @overload
    def get_loc(self, /, key: Literal["2000-01-01"], method: None, tolerance: None):
        """
        usage.xarray: 1
        """
        ...

    def get_loc(
        self,
        /,
        key: Union[Literal["2000-01-01"], numpy.datetime64],
        method: Union[None, Literal["nearest"]],
        tolerance: None = ...,
    ):
        """
        usage.xarray: 3
        """
        ...

    def max(self, /):
        """
        usage.dask: 1
        """
        ...

    def min(self, /):
        """
        usage.dask: 1
        """
        ...

    def round(self, /, *args: Literal["v", "t"]):
        """
        usage.xarray: 3
        """
        ...

    @overload
    def shift(self, /, periods: int, freq: Literal["S"]):
        """
        usage.dask: 3
        """
        ...

    @overload
    def shift(self, /, periods: int, freq: Literal["W"]):
        """
        usage.dask: 3
        """
        ...

    @overload
    def shift(self, /, periods: int, freq: pandas._libs.tslibs.timedeltas.Timedelta):
        """
        usage.dask: 3
        """
        ...

    @overload
    def shift(self, /, periods: int, freq: None):
        """
        usage.dask: 2
        """
        ...

    def shift(
        self,
        /,
        periods: int,
        freq: Union[None, Literal["W", "S"], pandas._libs.tslibs.timedeltas.Timedelta],
    ):
        """
        usage.dask: 11
        """
        ...

    @overload
    def to_frame(self, /, index: bool, name: None):
        """
        usage.dask: 1
        """
        ...

    @overload
    def to_frame(self, /, name: Literal["foo"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def to_frame(self, /, index: bool, name: Literal["foo"]):
        """
        usage.dask: 1
        """
        ...

    def to_frame(self, /, name: Union[Literal["foo"], None], index: bool = ...):
        """
        usage.dask: 3
        """
        ...

    def to_numpy(self, /, dtype: Literal["datetime64[ns]"]):
        """
        usage.xarray: 1
        """
        ...

    def to_series(self, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def tz_localize(self, /, tz: None, nonexistent: Literal["shift_forward"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def tz_localize(self, /, tz: object, nonexistent: Literal["shift_forward"]):
        """
        usage.dask: 1
        """
        ...

    def tz_localize(self, /, tz: object, nonexistent: Literal["shift_forward"]):
        """
        usage.dask: 2
        """
        ...
