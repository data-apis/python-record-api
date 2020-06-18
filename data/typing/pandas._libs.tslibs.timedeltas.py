from typing import *


class Timedelta:
    def __init__(
        value: Union[
            (str, pandas._libs.tslibs.timedeltas.Timedelta, numpy.timedelta64)
        ] = ...
    ):
        "usage.xarray: 10, usage.dask: 2"

    __module__ = ...

    def __add__(self, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        ""

    def __eq__(self, _0: pandas._libs.tslibs.timedeltas.Timedelta, /):
        ""

    def __ge__(self, _0: pandas._libs.tslibs.timedeltas.Timedelta, /):
        ""

    def __le__(self, _0: pandas._libs.tslibs.timedeltas.Timedelta, /):
        ""

    def __gt__(self, _0: pandas.core.series.Series, /):
        ""

    def __rsub__(self, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        ""

    def __radd__(self, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        ""


class _Timedelta:
    @classmethod
    def to_numpy(_0: pandas._libs.tslibs.timedeltas.Timedelta, /):
        "usage.xarray: 1"

    @classmethod
    def to_timedelta64(_0: pandas._libs.tslibs.timedeltas.Timedelta, /):
        "usage.xarray: 1"
