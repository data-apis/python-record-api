from typing import *


class Series:
    dt = ...
    values = ...
    index: pandas.core.indexes.datetimes.DatetimeIndex = ...
    name: None = ...
    loc = ...

    def rank(self, /, method: Literal[("dense",)], ascending: bool):
        "usage.xarray: 1"

    def astype(self, /, dtype: Type[int]):
        "usage.xarray: 1"

    def median(self, /):
        "usage.xarray: 1"

    def reset_index(self, /):
        "usage.xarray: 2"

    def unstack(self, /):
        "usage.xarray: 1"

    def groupby(self, /, by: pandas.core.resample.TimeGrouper):
        "usage.xarray: 1"

    def isnull(self, /):
        "usage.xarray: 1"

    def any(self, /):
        "usage.xarray: 1"

    def resample(self, /, rule: Literal[("1H", "3H", "24H")] = ...):
        "usage.xarray: 14"

    def dropna(self, /):
        "usage.xarray: 1"

    def to_frame(self, /):
        "usage.xarray: 2"

    def equals(self, /, other: pandas.core.series.Series):
        "usage.xarray: 1"

    def __setitem__(self, _0: int, _1: float, /):
        ""

    def shift(self, /, periods: int):
        "usage.xarray: 1"

    def rolling(self, /, window: int, min_periods: Union[(int, None)], center: bool):
        "usage.xarray: 3"

    def iteritems(self, /):
        "usage.xarray: 1"

    def __getitem__(self, _0: Union[(slice[(None, None, int)], int)], /):
        ""

    def sum(self, /, skipna: bool = ...):
        "usage.xarray: 2"

    def min(self, /, skipna: bool):
        "usage.xarray: 1"

    def max(self, /, skipna: bool):
        "usage.xarray: 1"

    def mean(self, /, skipna: bool):
        "usage.xarray: 1"

    def var(self, /, skipna: bool, ddof: int):
        "usage.xarray: 1"

    def prod(self, /, skipna: bool, min_count: int):
        "usage.xarray: 1"

    def __eq__(self, _0: Type[numpy.float64], /):
        ""
