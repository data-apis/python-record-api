from typing import *


def period_range(start: Literal[("2000-01-01", "2000")], periods: int = ...):
    "usage.xarray: 4"


class PeriodIndex:
    name = ...
    dtype = ...

    def __getitem__(
        self, _0: Union[(int, slice[(Union[(None, int)], Union[(None, int)], None)])], /
    ):
        ""

    def astype(self, /, dtype: Literal[("object",)]):
        "usage.xarray: 1"
