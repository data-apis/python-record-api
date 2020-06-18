from typing import *


class IntervalDtype:
    def __eq__(self, _0: Literal[("O",)], /):
        ""


class CategoricalDtype:
    def __init__(categories: List[str] = ...):
        "usage.xarray: 2, usage.dask: 1"

    __module__ = ...
    categories = ...
    kind = ...
    ordered = ...

    def __eq__(
        self,
        _0: Union[
            (
                pandas.core.dtypes.dtypes.CategoricalDtype,
                Literal[("category", "O")],
                Type[object],
            )
        ],
        /,
    ):
        ""

    def __ne__(
        self,
        _0: Union[(pandas.core.dtypes.dtypes.CategoricalDtype, Literal[("category",)])],
        /,
    ):
        ""


class PeriodDtype:
    __module__ = ...
    name = ...
    kind = ...

    def __eq__(self, _0: Literal[("O",)], /):
        ""


class DatetimeTZDtype:
    __module__ = ...
    name = ...
    tz = ...
    kind = ...

    def __eq__(
        self,
        _0: Union[
            (Type[object], pandas.core.dtypes.dtypes.DatetimeTZDtype, Literal[("O",)])
        ],
        /,
    ):
        ""
