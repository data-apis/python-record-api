from typing import *


def timedelta_range(
    start: Union[(Literal[("1 day", "1 days")], numpy.timedelta64, int)] = ...,
    periods: int = ...,
    end: Literal[("30 days",)] = ...,
    freq: Union[
        (
            pandas.tseries.offsets.Day,
            pandas.tseries.offsets.Minute,
            pandas.tseries.offsets.Hour,
            Literal[("H", "D", "T", "6H")],
            None,
        )
    ] = ...,
):
    "usage.xarray: 2, usage.dask: 9"


class TimedeltaIndex:
    def __init__(
        data: List[numpy.timedelta64], name: Literal[("timedelta", "foo")] = ...
    ):
        "usage.dask: 2"

    __module__ = ...
    __name__ = ...
    dtype = ...
    name = ...
    values = ...
    array = ...
    is_monotonic_increasing = ...
    freq = ...
    names = ...

    def copy(self, /, deep: bool):
        "usage.xarray: 1"

    def floor(self, /, *args: Literal[("v", "t")]):
        "usage.xarray: 1"

    def ceil(self, /, *args: Literal[("v", "t")]):
        "usage.xarray: 1"

    def round(self, /, *args: Literal[("v", "t")]):
        "usage.xarray: 1"

    def __truediv__(self, _0: numpy.timedelta64, /):
        ""

    def __add__(self, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        ""

    def __getitem__(self, _0: Union[(int, numpy.ndarray, slice[(int, int, None)])], /):
        ""

    def get_indexer(self, /, target: numpy.ndarray, method: None, tolerance: None):
        "usage.xarray: 1"

    def get_loc(
        self,
        /,
        key: pandas._libs.tslibs.timedeltas.Timedelta,
        method: None,
        tolerance: None,
    ):
        "usage.xarray: 1"

    def shift(
        self,
        /,
        periods: int,
        freq: Union[(None, Literal[("S",)], pandas._libs.tslibs.timedeltas.Timedelta)],
    ):
        "usage.dask: 8"
