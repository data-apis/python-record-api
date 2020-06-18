from typing import *


class MultiIndex:
    __module__ = ...
    __name__ = ...

    @classmethod
    def from_product(
        iterables: Union[(list, pandas.core.indexes.frozen.FrozenList)] = ...
    ):
        "usage.xarray: 39, usage.dask: 3"

    @classmethod
    def from_arrays(
        arrays: List[
            Union[
                (
                    List[Union[(int, Literal[("b", "a", "z", "y", "c")])]],
                    pandas.core.indexes.datetimes.DatetimeIndex,
                    pandas.core.indexes.numeric.Int64Index,
                    pandas.core.indexes.category.CategoricalIndex,
                    pandas.core.indexes.base.Index,
                )
            ]
        ] = ...
    ):
        "usage.xarray: 8, usage.dask: 7"

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
    names: List[
        Literal[
            (
                "-overlapped-index-name-1",
                "-overlapped-index-name-0",
                "-overlapped-index-name-2",
            )
        ]
    ] = ...
    name = ...
    nlevels = ...
    levels = ...
    codes = ...
    is_unique = ...
    shape = ...
    rename = ...
    size = ...
    is_monotonic = ...
    __class__ = ...

    def __getitem__(
        self,
        _0: Union[
            (
                slice[(Union[(int, None)], Union[(None, int)], Union[(None, int)])],
                int,
                numpy.ndarray,
            )
        ],
        /,
    ):
        ""

    def append(self, /, other: List[pandas.core.indexes.multi.MultiIndex]):
        "usage.xarray: 3"

    def equals(self, /, other: pandas.core.indexes.multi.MultiIndex):
        "usage.xarray: 8"

    def get_level_values(self, /, level: Union[(int, str)]):
        "usage.xarray: 27, usage.dask: 5"

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

    def set_names(
        self, /, names: List[Literal[("level1", "level0", "b", "a", "c")]] = ...
    ):
        "usage.xarray: 1, usage.dask: 2"

    def set_levels(
        self,
        /,
        levels: List[
            Union[
                (
                    pandas.core.indexes.base.Index,
                    pandas.core.indexes.numeric.Int64Index,
                    float,
                    str,
                )
            ]
        ],
        level: int = ...,
        inplace: bool = ...,
    ):
        "usage.xarray: 1, usage.dask: 11"

    def _get_level_number(self, /, level: int):
        "usage.xarray: 1"

    def get_locs(
        self, /, seq: Tuple[(slice[(None, None, None)], int, Literal[("no_level",)])]
    ):
        "usage.xarray: 1"

    def _get_level_values(self, /, level: int):
        "usage.dask: 1"

    def __contains__(self, _0: Literal[("dtype", "_meta", "columns", "divisions")], /):
        ""

    def __iter__(self, /):
        ""

    def union(self, /, other: pandas.core.indexes.multi.MultiIndex):
        "usage.dask: 1"
