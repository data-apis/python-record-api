from typing import *


class DataFrame:
    def __init__(data: List[List[int]]):
        "usage.xarray: 1"

    index: pandas.core.indexes.multi.MultiIndex = ...
    columns: List[Literal[("foo", "x", "C")]] = ...
    values = ...
    loc = ...

    def reset_index(self=..., /):
        "usage.xarray: 3"

    def set_index(self, /, keys):
        "usage.xarray: 10"

    def __getitem__(
        self,
        _0: Union[
            (Literal[("foo",)], List[Literal[("foo", "C")]], Literal[("x",)], int)
        ],
        /,
    ):
        ""

    def stack(self, /):
        "usage.xarray: 1"

    def __setitem__(self, _0: Literal[("C",)], _1: List[int], /):
        ""

    def equals(self, /, other: pandas.core.frame.DataFrame):
        "usage.xarray: 8"

    def reindex(
        self, /, labels: Union[(pandas.core.indexes.multi.MultiIndex, reversed)]
    ):
        "usage.xarray: 2"

    def items(self, /):
        "usage.xarray: 1"

    def iteritems(self, /):
        "usage.xarray: 1"

    def to_xarray(self, /):
        "usage.xarray: 5"

    def apply(self, /, func: Callable):
        "usage.xarray: 1"

    def rolling(self, /, window: int, min_periods: Union[(None, int)], center: bool):
        "usage.xarray: 3"
