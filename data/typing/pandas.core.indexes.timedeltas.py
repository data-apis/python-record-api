from typing import *


def timedelta_range(
    start: Union[(int, Literal[("1 day",)])] = ...,
    end: Literal[("30 days",)] = ...,
    freq: Literal[("6H",)] = ...,
):
    "usage.xarray: 2"


class TimedeltaIndex:
    dtype = ...
    name = ...
    values = ...

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

    def __getitem__(self, _0: Union[(numpy.ndarray, int, slice[(int, int, None)])], /):
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
