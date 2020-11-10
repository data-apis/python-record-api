from typing import *


class DatetimeProperties:

    # usage.dask: 1
    # usage.koalas: 3
    date: object

    # usage.koalas: 1
    day: object

    # usage.koalas: 1
    dayofweek: object

    # usage.koalas: 2
    dayofyear: object

    # usage.koalas: 1
    days_in_month: object

    # usage.koalas: 1
    daysinmonth: object

    # usage.koalas: 1
    hour: object

    # usage.koalas: 1
    is_leap_year: object

    # usage.koalas: 1
    is_month_end: object

    # usage.koalas: 1
    is_month_start: object

    # usage.koalas: 1
    is_quarter_end: object

    # usage.koalas: 1
    is_quarter_start: object

    # usage.koalas: 1
    is_year_end: object

    # usage.koalas: 1
    is_year_start: object

    # usage.koalas: 1
    microsecond: object

    # usage.koalas: 1
    minute: object

    # usage.koalas: 1
    # usage.xarray: 1
    month: object

    # usage.koalas: 1
    second: object

    # usage.prophet: 1
    tz: object

    # usage.koalas: 1
    week: object

    # usage.koalas: 1
    weekday: object

    # usage.koalas: 1
    weekofyear: object

    # usage.koalas: 1
    year: object

    def floor(self, /):
        """
        usage.koalas: 4
        """
        ...

    def round(self, /):
        """
        usage.koalas: 2
        """
        ...

    def to_pydatetime(self, /):
        """
        usage.dask: 1
        """
        ...


class TimedeltaProperties:

    # usage.koalas: 3
    days: object
