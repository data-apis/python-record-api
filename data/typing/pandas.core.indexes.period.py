from typing import *


@overload
def period_range(start: Literal["2000-01-01"], periods: int, freq: Literal["B"]):
    """
    usage.dask: 1
    usage.xarray: 1
    """
    ...


@overload
def period_range(start: Literal["2000-01-01"], periods: int):
    """
    usage.xarray: 2
    """
    ...


@overload
def period_range(start: Literal["2000"], periods: int, freq: Literal["B"]):
    """
    usage.xarray: 1
    """
    ...


@overload
def period_range(start: Literal["1/1/1990"], periods: int, freq: Literal["M"]):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def period_range(start: int, end: int, freq: Literal["A"]):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def period_range(
    start: pandas._libs.tslibs.period.Period,
    periods: int,
    freq: pandas._libs.tslibs.offsets.MonthEnd,
):
    """
    usage.statsmodels: 5
    """
    ...


@overload
def period_range(start: Literal["2000-1-1"], periods: int, freq: Literal["M"]):
    """
    usage.statsmodels: 2
    """
    ...


@overload
def period_range(
    start: pandas._libs.tslibs.period.Period,
    end: pandas._libs.tslibs.period.Period,
    freq: pandas._libs.tslibs.offsets.MonthEnd,
):
    """
    usage.statsmodels: 2
    """
    ...


@overload
def period_range(start: Literal["2000"], periods: int, freq: Literal["M"]):
    """
    usage.statsmodels: 10
    """
    ...


@overload
def period_range(start: Literal["2000"], periods: int, freq: Literal["Q"]):
    """
    usage.statsmodels: 8
    """
    ...


@overload
def period_range(start: Literal["2000"], periods: int, freq: Literal["W"]):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def period_range(start: Literal["1950-01"], periods: int, freq: Literal["M"]):
    """
    usage.statsmodels: 4
    """
    ...


@overload
def period_range(
    start: pandas._libs.tslibs.period.Period,
    end: pandas._libs.tslibs.period.Period,
    freq: Literal["M"],
):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def period_range(
    start: pandas._libs.tslibs.period.Period,
    periods: int,
    freq: pandas._libs.tslibs.offsets.QuarterEnd,
):
    """
    usage.statsmodels: 2
    """
    ...


@overload
def period_range(
    start: pandas._libs.tslibs.period.Period,
    periods: int,
    freq: pandas._libs.tslibs.offsets.YearEnd,
):
    """
    usage.statsmodels: 2
    """
    ...


@overload
def period_range(start: Literal["2000-01"], periods: int, freq: Literal["M"]):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def period_range(
    start: pandas._libs.tslibs.period.Period, periods: int, freq: Literal["M"]
):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def period_range(
    start: pandas._libs.tslibs.period.Period,
    end: pandas._libs.tslibs.period.Period,
    freq: pandas._libs.tslibs.offsets.QuarterEnd,
):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def period_range(start: Literal["2009Q2"], end: Literal["2010Q1"], freq: Literal["Q"]):
    """
    usage.statsmodels: 2
    """
    ...


@overload
def period_range(start: Literal["2009Q3"], periods: int, freq: Literal["Q"]):
    """
    usage.statsmodels: 2
    """
    ...


@overload
def period_range(start: Literal["2009Q2"], periods: int, freq: Literal["Q"]):
    """
    usage.statsmodels: 3
    """
    ...


@overload
def period_range(start: Literal["2009Q1"], periods: int, freq: Literal["Q"]):
    """
    usage.statsmodels: 4
    """
    ...


@overload
def period_range(end: Literal["2009Q1"], periods: int, freq: Literal["Q"]):
    """
    usage.statsmodels: 4
    """
    ...


@overload
def period_range(end: Literal["2009Q2"], periods: int, freq: Literal["Q"]):
    """
    usage.statsmodels: 2
    """
    ...


@overload
def period_range(start: Literal["2009Q1"], end: Literal["2009Q1"], freq: Literal["Q"]):
    """
    usage.statsmodels: 6
    """
    ...


@overload
def period_range(start: Literal["2009Q1"], end: Literal["2009Q2"], freq: Literal["Q"]):
    """
    usage.statsmodels: 4
    """
    ...


@overload
def period_range(start: Literal["2011-1"], periods: int, freq: Literal["M"]):
    """
    usage.statsmodels: 2
    """
    ...


@overload
def period_range(start: Literal["1959Q1"], periods: int, freq: Literal["Q"]):
    """
    usage.statsmodels: 4
    """
    ...


@overload
def period_range(start: Literal["1990-1-1"], periods: int, freq: Literal["M"]):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def period_range(
    start: pandas._libs.tslibs.period.Period,
    end: pandas._libs.tslibs.period.Period,
    freq: pandas._libs.tslibs.offsets.YearEnd,
):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def period_range(start: Literal["1959Q1"], end: Literal["2009Q3"], freq: Literal["Q"]):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def period_range(start: Literal["2008Q2"], end: Literal["2009Q4"], freq: Literal["Q"]):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def period_range(
    start: pandas._libs.tslibs.period.Period,
    periods: int,
    freq: pandas._libs.tslibs.offsets.BusinessDay,
):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def period_range(
    start: Literal["1960-1-1"], periods: int, freq: pandas._libs.tslibs.offsets.MonthEnd
):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def period_range(
    start: pandas._libs.tslibs.timestamps.Timestamp,
    periods: int,
    freq: pandas._libs.tslibs.offsets.Day,
):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def period_range(
    start: Literal["1/1/2001"], end: Literal["12/1/2004"], freq: Literal["A"]
):
    """
    usage.dask: 1
    """
    ...


@overload
def period_range(
    start: Literal["1970-01-01"],
    periods: int,
    freq: pandas._libs.tslibs.offsets.YearEnd,
    name: None,
):
    """
    usage.dask: 1
    """
    ...


@overload
def period_range(
    start: Literal["1970-01-01"],
    periods: int,
    freq: pandas._libs.tslibs.offsets.BusinessDay,
    name: None,
):
    """
    usage.dask: 1
    """
    ...


@overload
def period_range(start: Literal["2000-01-01"], periods: int, freq: Literal["D"]):
    """
    usage.dask: 1
    """
    ...


@overload
def period_range(
    start: Literal["1970-01-01"],
    periods: int,
    freq: pandas._libs.tslibs.offsets.Day,
    name: None,
):
    """
    usage.dask: 1
    """
    ...


@overload
def period_range(start: Literal["2000-01-01"], periods: int, freq: Literal["H"]):
    """
    usage.dask: 1
    """
    ...


@overload
def period_range(
    start: Literal["1970-01-01"],
    periods: int,
    freq: pandas._libs.tslibs.offsets.Hour,
    name: None,
):
    """
    usage.dask: 1
    """
    ...


@overload
def period_range(start: Literal["2011-01-01"], periods: int, freq: Literal["H"]):
    """
    usage.dask: 1
    """
    ...


@overload
def period_range(start: Literal["2011-01-01"], periods: int, freq: Literal["D"]):
    """
    usage.dask: 1
    """
    ...


@overload
def period_range(
    start: Literal["1970-01-01"],
    periods: int,
    freq: pandas._libs.tslibs.offsets.Day,
    name: Literal["foo"],
):
    """
    usage.dask: 1
    """
    ...


def period_range(
    start: Union[
        str,
        pandas._libs.tslibs.timestamps.Timestamp,
        pandas._libs.tslibs.period.Period,
        int,
    ] = ...,
    freq: object = ...,
    end: Union[str, int, pandas._libs.tslibs.period.Period] = ...,
    periods: int = ...,
    name: Union[Literal["foo"], None] = ...,
):
    """
    usage.dask: 11
    usage.statsmodels: 82
    usage.xarray: 4
    """
    ...


class PeriodIndex:

    # usage.dask: 1
    __module__: ClassVar[object]

    # usage.dask: 2
    # usage.statsmodels: 2
    __name__: ClassVar[object]

    # usage.dask: 1
    array: object

    # usage.statsmodels: 2
    asi8: object

    # usage.statsmodels: 3
    dayofweek: object

    # usage.dask: 3
    # usage.xarray: 1
    dtype: object

    # usage.dask: 3
    # usage.statsmodels: 22
    freq: object

    # usage.statsmodels: 2
    freqstr: object

    # usage.statsmodels: 2
    hour: object

    # usage.statsmodels: 2
    is_all_dates: object

    # usage.statsmodels: 1
    is_monotonic: object

    # usage.statsmodels: 2
    month: object

    # usage.dask: 8
    # usage.xarray: 1
    name: object

    # usage.dask: 1
    names: object

    # usage.statsmodels: 1
    quarter: object

    # usage.statsmodels: 19
    shape: object

    @overload
    def __add__(self, _0: int, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __add__(
        self,
        _0: Union[numpy.timedelta64, numpy.ndarray, numpy.datetime64, numpy.int64],
        /,
    ):
        """
        usage.pandas: 20
        """
        ...

    def __add__(
        self,
        _0: Union[numpy.int64, numpy.datetime64, numpy.ndarray, numpy.timedelta64, int],
        /,
    ):
        """
        usage.pandas: 20
        usage.statsmodels: 1
        """
        ...

    def __eq__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 8
        """
        ...

    def __ge__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 8
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, int, None], /):
        """
        usage.statsmodels: 7
        usage.xarray: 2
        """
        ...

    @overload
    def __getitem__(self, _0: slice[int, None, int], /):
        """
        usage.statsmodels: 15
        usage.xarray: 2
        """
        ...

    @overload
    def __getitem__(self, _0: slice[int, int, int], /):
        """
        usage.dask: 1
        usage.statsmodels: 4
        usage.xarray: 1
        """
        ...

    @overload
    def __getitem__(self, _0: int, /):
        """
        usage.dask: 4
        usage.statsmodels: 45
        usage.xarray: 1
        """
        ...

    @overload
    def __getitem__(self, _0: pandas.core.series.Series, /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __getitem__(self, _0: numpy.ndarray, /):
        """
        usage.statsmodels: 1
        """
        ...

    def __getitem__(
        self,
        _0: Union[
            int,
            numpy.ndarray,
            pandas.core.series.Series,
            slice[Union[None, int], Union[int, None], Union[None, int]],
        ],
        /,
    ):
        """
        usage.dask: 5
        usage.statsmodels: 74
        usage.xarray: 6
        """
        ...

    @overload
    def __gt__(self, _0: pandas._libs.tslibs.period.Period, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __gt__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 6
        """
        ...

    def __gt__(self, _0: Union[numpy.ndarray, pandas._libs.tslibs.period.Period], /):
        """
        usage.pandas: 6
        usage.statsmodels: 1
        """
        ...

    def __iadd__(self, _0: Union[numpy.timedelta64, numpy.ndarray], /):
        """
        usage.pandas: 7
        """
        ...

    def __isub__(self, _0: Union[numpy.timedelta64, numpy.ndarray], /):
        """
        usage.pandas: 6
        """
        ...

    def __le__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 8
        """
        ...

    @overload
    def __lt__(self, _0: pandas._libs.tslibs.period.Period, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __lt__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 2
        """
        ...

    def __lt__(self, _0: Union[numpy.ndarray, pandas._libs.tslibs.period.Period], /):
        """
        usage.pandas: 2
        usage.statsmodels: 1
        """
        ...

    def __ne__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 6
        """
        ...

    def __radd__(
        self, _0: Union[numpy.timedelta64, numpy.datetime64, numpy.ndarray], /
    ):
        """
        usage.pandas: 11
        """
        ...

    def __rsub__(
        self, _0: Union[numpy.timedelta64, numpy.datetime64, numpy.ndarray], /
    ):
        """
        usage.pandas: 10
        """
        ...

    def __sub__(self, _0: Union[numpy.timedelta64, numpy.datetime64, numpy.ndarray], /):
        """
        usage.pandas: 18
        """
        ...

    def shift(self, /, periods: int):
        """
        usage.dask: 1
        """
        ...

    def to_timestamp(self, /):
        """
        usage.statsmodels: 1
        """
        ...
