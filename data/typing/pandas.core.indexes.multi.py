from typing import *


class MultiIndex:
    @classmethod
    def from_product(
        iterables: Union[(list, pandas.core.indexes.frozen.FrozenList)] = ...
    ):
        "usage.xarray: 39"

    @classmethod
    def from_arrays(
        arrays: List[
            Union[
                (
                    pandas.core.indexes.category.CategoricalIndex,
                    pandas.core.indexes.numeric.Int64Index,
                    pandas.core.indexes.datetimes.DatetimeIndex,
                    List[Union[(Literal[("b", "a", "z", "y", "c")], int)]],
                )
            ]
        ],
        names: Union[
            (
                pandas.core.indexes.frozen.FrozenList,
                Tuple[(Literal[("level_str",)], Literal[("level_date",)])],
                List[Literal[("y", "x", "y2", "y1")]],
            )
        ],
    ):
        "usage.xarray: 8"

    @classmethod
    def from_tuples(
        tuples: Union[
            (
                Tuple[
                    (
                        Tuple[(Literal[("a", "b")], int)],
                        Tuple[(Literal[("a", "b")], int)],
                        Tuple[(Literal[("b", "a")], int)],
                        Tuple[(Literal[("b", "a")], int)],
                    )
                ],
                List[List[int]],
            )
        ],
        names: List[Literal[("level1", "level0", "two", "one")]],
    ):
        "usage.xarray: 3"

    dtype = ...
    values = ...
    names = ...
    name = ...
    nlevels = ...
    levels = ...
    codes = ...
    is_unique = ...
    shape = ...
    rename = ...
    size = ...
    is_monotonic = ...

    def __getitem__(
        self,
        _0: Union[
            (
                slice[(Union[(None, int)], Union[(int, None)], Union[(int, None)])],
                numpy.ndarray,
                int,
            )
        ],
        /,
    ):
        ""

    def append(self, /, other: List[pandas.core.indexes.multi.MultiIndex]):
        "usage.xarray: 3"

    def equals(self, /, other: pandas.core.indexes.multi.MultiIndex):
        "usage.xarray: 8"

    def get_level_values(self, /, level: str):
        "usage.xarray: 27"

    def get_loc(self, /, key: Tuple[(Literal[("a", "b")], int, int)]):
        "usage.xarray: 3"

    def get_loc_level(
        self,
        /,
        key: Union[
            (Tuple[(Union[(int, Literal[("a", "b")])], ...)], Literal[("a",)], int)
        ],
        level: Union[(Tuple[(str, ...)], List[int], int)],
    ):
        "usage.xarray: 12"

    def get_indexer(self, /, target: numpy.ndarray, method: None, tolerance: None):
        "usage.xarray: 2"

    def remove_unused_levels(self, /):
        "usage.xarray: 1"

    def copy(self, /, deep: bool):
        "usage.xarray: 1"

    def reorder_levels(self, /, order: List[Literal[("level_1", "level_2")]]):
        "usage.xarray: 4"

    def set_names(self, /, names: List[Literal[("level1", "level0")]]):
        "usage.xarray: 1"

    def set_levels(
        self,
        /,
        levels: List[
            Union[
                (pandas.core.indexes.numeric.Int64Index, pandas.core.indexes.base.Index)
            ]
        ],
    ):
        "usage.xarray: 1"

    def _get_level_number(self, /, level: int):
        "usage.xarray: 1"

    def get_locs(
        self, /, seq: Tuple[(slice[(None, None, None)], int, Literal[("no_level",)])]
    ):
        "usage.xarray: 1"
