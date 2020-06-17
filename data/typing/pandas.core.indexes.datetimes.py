from typing import *


def date_range(
    start: Literal[
        (
            "2000/01/01",
            "20130101",
            "1970-01-01",
            "1/1/2011",
            "2010-08-01",
            "20100101",
            "2011-09-01",
            "2007-02-01",
            "15/12/1999",
            "2000-1-1",
            "20000101",
            "01-01-2001",
            "2016-01-01",
            "2000-01-01",
            "2000",
            "2014-01-01",
        )
    ],
    end: Literal[
        ("2010-08-15", "2007-03-01", "2014-05-01", "2016-03-31", "2000-01-10")
    ] = ...,
    periods: int = ...,
    freq: Literal[
        ("6H", "1h", "2MS", "M", "h", "24H", "1D", "3H", "7D", "15min", "H", "D")
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

    def floor(self, /, *args: Literal[("v", "t")]):
        "usage.xarray: 1"

    def ceil(self, /, *args: Literal[("v", "t")]):
        "usage.xarray: 1"

    def round(self, /, *args: Literal[("v", "t")]):
        "usage.xarray: 1"

    def __sub__(
        self,
        _0: Union[(pandas._libs.tslibs.timestamps.Timestamp, numpy.timedelta64)],
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
                Literal[("1999",)],
                Literal[("2001",)],
                numpy.datetime64,
                Literal[("2000-01-01",)],
            )
        ],
        end: Union[
            (
                Literal[("2000-01-10",)],
                numpy.datetime64,
                Literal[("2005",)],
                Literal[("2002",)],
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
        tolerance: Union[(None, Literal[("12H",)], Literal[("6H",)])],
    ):
        "usage.xarray: 7"

    def __add__(self, _0: pandas.tseries.offsets.Hour, /):
        ""

    def get_loc(
        self,
        /,
        key: Union[(numpy.datetime64, Literal[("2000-01-01",)])],
        method: Union[(Literal[("nearest",)], None)] = ...,
    ):
        "usage.xarray: 3"
