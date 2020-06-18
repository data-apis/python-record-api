from typing import *


class Categorical:
    def __init__(
        values: Union[
            (
                pandas.core.indexes.datetimes.DatetimeIndex,
                pandas.core.indexes.numeric.Float64Index,
                pandas.core.indexes.base.Index,
                numpy.ndarray,
                List[str],
            )
        ],
        categories: Union[(None, pandas.core.indexes.base.Index)] = ...,
        ordered: bool = ...,
    ):
        "usage.xarray: 4, usage.dask: 10"

    @classmethod
    def from_codes(
        codes: Union[(numpy.ndarray, List[int])],
        categories: Union[
            (
                pandas.core.indexes.base.Index,
                List[
                    Literal[
                        (
                            "2014-01-03.csv",
                            "2014-01-02.csv",
                            "2014-01-01.csv",
                            "/private/var/folders/xn/05ktz3056kqd9n8frgd6236h00",
                        )
                    ]
                ],
            )
        ] = ...,
    ):
        "usage.dask: 5"

    codes = ...
    categories = ...
    dtype = ...
    name: Union[(Literal[("idx",)], None)] = ...
    ordered = ...

    def __contains__(
        self, _0: Literal[("2014-01-03.csv", "2014-01-02.csv", "2014-01-01.csv")], /
    ):
        ""

    def sort_values(self, /):
        "usage.dask: 1"


class CategoricalAccessor:
    categories = ...
    ordered = ...
    codes = ...

    def set_categories(self, /, *args: Literal[("v", "t")]):
        "usage.dask: 9"

    def as_ordered(self, /):
        "usage.dask: 1"

    def add_categories(self, /):
        "usage.dask: 1"

    def as_unordered(self, /):
        "usage.dask: 1"

    def remove_categories(self, /):
        "usage.dask: 1"

    def rename_categories(self, /):
        "usage.dask: 1"

    def reorder_categories(self, /):
        "usage.dask: 1"
