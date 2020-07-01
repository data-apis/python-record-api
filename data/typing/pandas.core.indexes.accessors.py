from typing import *


class DatetimeProperties:

    # usage.xarray: 1
    month: object

    # usage.dask: 1
    date: object

    def floor(self: object, /):
        """
        usage.xarray: 1
        """
        ...

    def ceil(self: object, /):
        """
        usage.xarray: 1
        """
        ...

    def round(self: object, /):
        """
        usage.xarray: 1
        """
        ...

    def to_pydatetime(self: object, /):
        """
        usage.dask: 2
        """
        ...


class TimedeltaProperties:
    def floor(self: object, /):
        """
        usage.xarray: 1
        """
        ...

    def ceil(self: object, /):
        """
        usage.xarray: 1
        """
        ...

    def round(self: object, /):
        """
        usage.xarray: 1
        """
        ...
