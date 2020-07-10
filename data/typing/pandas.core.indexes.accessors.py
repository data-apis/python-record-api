from typing import *


class DatetimeProperties:

    # usage.dask: 1
    date: object

    # usage.xarray: 1
    month: object

    def ceil(self, /):
        """
        usage.xarray: 1
        """
        ...

    def floor(self, /):
        """
        usage.xarray: 1
        """
        ...

    def round(self, /):
        """
        usage.xarray: 1
        """
        ...

    def to_pydatetime(self, /):
        """
        usage.dask: 2
        """
        ...


class TimedeltaProperties:
    def ceil(self, /):
        """
        usage.xarray: 1
        """
        ...

    def floor(self, /):
        """
        usage.xarray: 1
        """
        ...

    def round(self, /):
        """
        usage.xarray: 1
        """
        ...
