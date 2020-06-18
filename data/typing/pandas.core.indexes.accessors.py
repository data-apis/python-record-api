from typing import *


class DatetimeProperties:
    month = ...
    date = ...

    def floor(self, /):
        "usage.xarray: 1"

    def ceil(self, /):
        "usage.xarray: 1"

    def round(self, /):
        "usage.xarray: 1"

    def to_pydatetime(self, /):
        "usage.dask: 2"


class TimedeltaProperties:
    def floor(self, /):
        "usage.xarray: 1"

    def ceil(self, /):
        "usage.xarray: 1"

    def round(self, /):
        "usage.xarray: 1"
