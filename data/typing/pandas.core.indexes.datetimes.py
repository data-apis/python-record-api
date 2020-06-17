from typing import *


def date_range(
    start: str,
    end: Literal[
        ("2000-01-10", "2010-08-15", "2016-03-31", "2007-03-01", "2014-05-01")
    ] = ...,
    periods: int = ...,
    freq: str = ...,
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

    def __getitem__(
        self,
        _0: Union[
            (
                slice[(Union[(int, None)], Union[(None, int)], Union[(None, int)])],
                int,
                numpy.ndarray,
            )
        ],
        /,
    ):
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
        _0: Union[(numpy.timedelta64, pandas._libs.tslibs.timestamps.Timestamp)],
        /,
    ):
        ""

    def to_series(self, /):
        "usage.xarray: 7"

    def slice_indexer(
        self,
        /,
        start: Union[(Literal[("2001", "1999", "2000-01-01")], numpy.datetime64)],
        end: Union[(Literal[("2002", "2005", "2000-01-10")], numpy.datetime64)],
        step: None,
    ):
        "usage.xarray: 4"

    def get_indexer(
        self,
        /,
        target: numpy.ndarray,
        method: Union[(Literal[("nearest", "backfill", "pad")], None)],
        tolerance: Union[(Literal[("6H", "12H")], None)],
    ):
        "usage.xarray: 7"

    def __add__(self, _0: pandas.tseries.offsets.Hour, /):
        ""

    def get_loc(
        self,
        /,
        key: Union[(Literal[("2000-01-01",)], numpy.datetime64)],
        method: Union[(None, Literal[("nearest",)])] = ...,
    ):
        "usage.xarray: 3"
