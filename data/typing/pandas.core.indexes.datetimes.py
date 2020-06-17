from typing import *


def date_range(
    start: Literal[
        (
            "20130101",
            "20000101",
            "2000",
            "2011-09-01",
            "2014-01-01",
            "1/1/2011",
            "2016-01-01",
            "2000-1-1",
            "2007-02-01",
            "15/12/1999",
            "2010-08-01",
            "2000/01/01",
            "20100101",
            "2000-01-01",
            "1970-01-01",
            "01-01-2001",
        )
    ],
    end: Literal[
        ("2014-05-01", "2000-01-10", "2010-08-15", "2016-03-31", "2007-03-01")
    ] = ...,
    periods: int = ...,
    freq: Literal[
        ("M", "6H", "24H", "D", "7D", "h", "1D", "15min", "1h", "H", "3H", "2MS")
    ] = ...,
    tz: Union[(pytz.tzfile.America / New_York, Literal[("US/Eastern",)])] = ...,
):
    "usage.xarray: 79"


class DatetimeIndex:
    name = ...
    dtype = ...
    values = ...
    is_monotonic_increasing = ...
    size = ...
    is_monotonic = ...
    is_unique = ...
    shape = ...
    month = ...
    time = ...
    hour = ...
    ndim = ...

    def __getitem__(self, _0, /):
        ""

    def copy(self, /, deep: bool):
        "usage.xarray: 1"

    def floor(self, /, *args: Literal[("t", "v")]):
        "usage.xarray: 1"

    def ceil(self, /, *args: Literal[("t", "v")]):
        "usage.xarray: 1"

    def round(self, /, *args: Literal[("t", "v")]):
        "usage.xarray: 1"

    def __sub__(
        self,
        _0: Union[(numpy.timedelta64, pandas._libs.tslibs.timestamps.Timestamp)],
        /,
    ):
        ""

    def to_series(self, /):
        "usage.xarray: 7"

    def slice_indexer(
        self,
        /,
        start: Union[
            (
                numpy.datetime64,
                Literal[("2001",)],
                Literal[("1999",)],
                Literal[("2000-01-01",)],
            )
        ],
        end: Union[
            (
                Literal[("2002",)],
                numpy.datetime64,
                Literal[("2000-01-10",)],
                Literal[("2005",)],
            )
        ],
        step: None,
    ):
        "usage.xarray: 4"

    def get_indexer(
        self,
        /,
        target: numpy.ndarray,
        method: Union[
            (None, Literal[("backfill",)], Literal[("nearest",)], Literal[("pad",)])
        ],
        tolerance: Union[(None, Literal[("6H",)], Literal[("12H",)])],
    ):
        "usage.xarray: 7"

    def __add__(self, _0: pandas.tseries.offsets.Hour, /):
        ""

    def get_loc(
        self,
        /,
        key: Union[(numpy.datetime64, Literal[("2000-01-01",)])],
        method: Union[(None, Literal[("nearest",)])] = ...,
    ):
        "usage.xarray: 3"
