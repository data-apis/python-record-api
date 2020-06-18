from typing import *


def date_range(
    start: Union[(int, pandas._libs.tslibs.timestamps.Timestamp, str)],
    end: Union[(pandas._libs.tslibs.timestamps.Timestamp, str)] = ...,
    periods: int = ...,
    freq=...,
    tz=...,
    name: Union[(None, str)] = ...,
    closed: Union[(Literal[("left",)], None)] = ...,
):
    "usage.xarray: 79, usage.dask: 89"


class DatetimeIndex:
    __module__ = ...
    __name__ = ...
    name: Union[(Literal[("index",)], None)] = ...
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
    array = ...
    freq: None = ...
    tz = ...
    names = ...
    day = ...
    is_all_dates = ...

    def __getitem__(
        self,
        _0: Union[
            (
                int,
                numpy.ndarray,
                slice[(Union[(None, int)], Union[(int, None)], Union[(int, None)])],
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
        "usage.xarray: 7, usage.dask: 4"

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

    def __add__(self, _0, /):
        ""

    def get_loc(
        self,
        /,
        key: Union[(Literal[("2000-01-01",)], numpy.datetime64)],
        method: Union[(None, Literal[("nearest",)])] = ...,
    ):
        "usage.xarray: 3"

    def min(self, /):
        "usage.dask: 1"

    def max(self, /):
        "usage.dask: 1"

    def shift(
        self,
        /,
        periods: int,
        freq: Union[
            (None, Literal[("W", "S")], pandas._libs.tslibs.timedeltas.Timedelta)
        ],
    ):
        "usage.dask: 11"

    def _maybe_cast_slice_bound(
        self, /, label: str, side: Literal[("right", "left")], kind: Literal[("loc",)]
    ):
        "usage.dask: 23"

    def to_frame(self, /, name: Union[(Literal[("foo",)], None)] = ...):
        "usage.dask: 3"

    def __gt__(self, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        ""

    def __le__(self, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        ""

    def tz_localize(self, /, *args: Literal[("v", "t")]):
        "usage.dask: 2"
