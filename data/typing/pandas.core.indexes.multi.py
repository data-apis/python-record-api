from typing import *


class MultiIndex:

    # usage.dask: 1
    __module__: ClassVar[object]

    # usage.dask: 3
    __name__: ClassVar[object]

    @classmethod
    def from_product(iterables: Union[list, pandas.core.indexes.frozen.FrozenList]):
        "\n    usage.xarray: 39\n    usage.dask: 3\n    "
        ...

    @classmethod
    def from_arrays(
        arrays: List[
            Union[
                List[Union[int, Literal[("b", "a", "z", "y", "c")]]],
                pandas.core.indexes.datetimes.DatetimeIndex,
                pandas.core.indexes.numeric.Int64Index,
                pandas.core.indexes.category.CategoricalIndex,
                pandas.core.indexes.base.Index,
            ]
        ]
    ):
        "\n    usage.xarray: 8\n    usage.dask: 7\n    "
        ...

    @classmethod
    def from_tuples(
        tuples: Union[
            Tuple[
                Tuple[Literal[("a", "b")], int],
                Tuple[Literal[("a", "b")], int],
                Tuple[Literal[("b", "a")], int],
                Tuple[Literal[("b", "a")], int],
            ],
            List[List[int]],
        ],
        names: List[Literal[("level1", "level0", "two", "one")]],
    ):
        "\n    usage.xarray: 3\n    "
        ...

    # usage.xarray: 3
    # usage.dask: 2
    dtype: object

    # usage.xarray: 5
    values: object

    # usage.xarray: 23
    # usage.dask: 11
    names: List[
        Literal[
            (
                "-overlapped-index-name-1",
                "-overlapped-index-name-0",
                "-overlapped-index-name-2",
            )
        ]
    ]

    # usage.xarray: 1
    # usage.dask: 4
    name: object

    # usage.xarray: 4
    # usage.dask: 3
    nlevels: object

    # usage.xarray: 17
    # usage.dask: 9
    levels: object

    # usage.xarray: 5
    # usage.dask: 2
    codes: object

    # usage.xarray: 2
    is_unique: object

    # usage.xarray: 1
    shape: object

    # usage.xarray: 1
    rename: object

    # usage.xarray: 2
    size: object

    # usage.xarray: 1
    is_monotonic: object

    # usage.dask: 1
    __class__: object

    def __getitem__(
        self: object,
        _0: Union[
            slice[Union[int, None], Union[None, int], Union[int, None]],
            int,
            numpy.ndarray,
        ],
        /,
    ):
        "\n    usage.xarray: 16\n    usage.dask: 3\n    "
        ...

    def append(self: object, /, other: List[pandas.core.indexes.multi.MultiIndex]):
        "\n    usage.xarray: 3\n    "
        ...

    def equals(self: object, /, other: pandas.core.indexes.multi.MultiIndex):
        "\n    usage.xarray: 8\n    "
        ...

    def get_level_values(self: object, /, level: Union[int, str]):
        "\n    usage.xarray: 27\n    usage.dask: 5\n    "
        ...

    def get_loc(self: object, /, key: Tuple[Literal[("a", "b")], int, int]):
        "\n    usage.xarray: 3\n    "
        ...

    def get_loc_level(
        self: object,
        /,
        key: Union[Tuple[Union[int, Literal[("a", "b")]], ...], Literal["a"], int],
        level: Union[Tuple[str, ...], List[int], int],
    ):
        "\n    usage.xarray: 12\n    "
        ...

    def get_indexer(
        self: object, /, target: numpy.ndarray, method: None, tolerance: None
    ):
        "\n    usage.xarray: 2\n    "
        ...

    def remove_unused_levels(self: object, /):
        "\n    usage.xarray: 1\n    "
        ...

    def copy(self: object, /, deep: bool):
        "\n    usage.xarray: 1\n    "
        ...

    def reorder_levels(self: object, /, order: List[Literal[("level_1", "level_2")]]):
        "\n    usage.xarray: 4\n    "
        ...

    def set_names(
        self: object, /, names: List[Literal[("level1", "level0", "b", "a", "c")]]
    ):
        "\n    usage.xarray: 1\n    usage.dask: 2\n    "
        ...

    def set_levels(
        self: object,
        /,
        levels: List[
            Union[
                pandas.core.indexes.base.Index,
                pandas.core.indexes.numeric.Int64Index,
                float,
                str,
            ]
        ],
        level: int = ...,
        inplace: bool = ...,
    ):
        "\n    usage.xarray: 1\n    usage.dask: 11\n    "
        ...

    def _get_level_number(self: object, /, level: int):
        "\n    usage.xarray: 1\n    "
        ...

    def get_locs(
        self: object, /, seq: Tuple[slice[None, None, None], int, Literal["no_level"]]
    ):
        "\n    usage.xarray: 1\n    "
        ...

    def _get_level_values(self: object, /, level: int):
        "\n    usage.dask: 1\n    "
        ...

    def __contains__(
        self: object, _0: Literal[("dtype", "_meta", "columns", "divisions")], /
    ):
        "\n    usage.dask: 4\n    "
        ...

    def __iter__(self: object, /):
        "\n    usage.dask: 1\n    "
        ...

    def union(self: object, /, other: pandas.core.indexes.multi.MultiIndex):
        "\n    usage.dask: 1\n    "
        ...
