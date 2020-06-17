from typing import *


def date_range(
    start: Literal[
        (
            "2016-01-01",
            "01-01-2001",
            "2011-09-01",
            "20000101",
            "1970-01-01",
            "2014-01-01",
            "2010-08-01",
            "15/12/1999",
            "2000-1-1",
            "2000/01/01",
            "2000",
            "1/1/2011",
            "2007-02-01",
            "20100101",
            "20130101",
            "2000-01-01",
        )
    ],
    end: Literal[
        ("2014-05-01", "2010-08-15", "2000-01-10", "2007-03-01", "2016-03-31")
    ] = ...,
    periods: int = ...,
    freq: Literal[
        ("2MS", "H", "M", "1h", "15min", "1D", "h", "D", "24H", "6H", "7D", "3H")
    ] = ...,
    tz: Union[(Literal[("US/Eastern",)], pytz.tzfile.America / New_York)] = ...,
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
                Literal[("1999",)],
                Literal[("2001",)],
                Literal[("2000-01-01",)],
                numpy.datetime64,
            )
        ],
        end: Union[
            (
                Literal[("2000-01-10",)],
                Literal[("2005",)],
                numpy.datetime64,
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
            (Literal[("pad",)], Literal[("nearest",)], None, Literal[("backfill",)])
        ],
        tolerance: Union[(Literal[("6H",)], None, Literal[("12H",)])],
    ):
        "usage.xarray: 7"

    def __add__(self, _0: pandas.tseries.offsets.Hour, /):
        ""

    def get_loc(
        self,
        /,
        key: Union[(Literal[("2000-01-01",)], numpy.datetime64)],
        method: Union[(Literal[("nearest",)], None)] = ...,
    ):
        "usage.xarray: 3"
