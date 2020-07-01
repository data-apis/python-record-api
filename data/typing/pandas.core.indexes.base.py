from typing import *


class Index:

    # usage.dask: 2
    __name__: ClassVar[object]

    # usage.xarray: 6
    # usage.dask: 14
    dtype: object

    # usage.xarray: 3
    values: object

    # usage.xarray: 1
    # usage.dask: 2
    is_monotonic_increasing: object

    # usage.xarray: 7
    size: object

    # usage.xarray: 5
    is_unique: object

    # usage.xarray: 1
    # usage.dask: 1
    is_monotonic: object

    # usage.xarray: 1
    shape: object

    # usage.xarray: 11
    # usage.dask: 14
    name: Union[None, Literal["A"]]

    # usage.xarray: 1
    nlevels: object

    # usage.dask: 1
    array: object

    # usage.dask: 3
    names: List[Literal["-overlapped-index-name-0"]]

    # usage.dask: 1
    str: object

    def set_names(self: object, /, names: Union[str, numpy.str_, List[str]]):
        "\n    usage.xarray: 183\n    "
        ...

    def equals(
        self: object,
        /,
        other: Union[
            pandas.core.indexes.base.Index,
            pandas.core.indexes.numeric.Int64Index,
            pandas.core.indexes.range.RangeIndex,
            pandas.core.indexes.numeric.Float64Index,
            pandas.core.indexes.multi.MultiIndex,
        ],
    ):
        "\n    usage.xarray: 24\n    usage.dask: 3\n    "
        ...

    def __getitem__(
        self: object,
        _0: Union[
            int,
            numpy.ndarray,
            slice[Union[int, None], Union[int, None], Union[int, None]],
        ],
        /,
    ):
        "\n    usage.xarray: 14\n    usage.dask: 22\n    "
        ...

    def append(
        self: object,
        /,
        other: Union[
            pandas.core.indexes.category.CategoricalIndex,
            pandas.core.indexes.numeric.Int64Index,
            list,
        ],
    ):
        "\n    usage.xarray: 17\n    usage.dask: 16\n    "
        ...

    def to_series(self: object, /):
        "\n    usage.xarray: 3\n    usage.dask: 7\n    "
        ...

    def copy(self: object, /, deep: bool):
        "\n    usage.xarray: 1\n    "
        ...

    def rename(self: object, /, name: str):
        "\n    usage.xarray: 15\n    usage.dask: 1\n    "
        ...

    def slice_indexer(self: object, /, start: object, end: object, step: None):
        "\n    usage.xarray: 12\n    "
        ...

    def get_indexer(
        self: object,
        /,
        target: numpy.ndarray,
        method: Union[Literal["pad"], None],
        tolerance: None,
    ):
        "\n    usage.xarray: 3\n    "
        ...

    def get_loc(
        self: object,
        /,
        key: Union[str, bool],
        method: None = ...,
        tolerance: None = ...,
    ):
        "\n    usage.xarray: 26\n    "
        ...

    def droplevel(
        self: object, /, level: Union[List[Literal["level_1"]], Literal["level_1"]]
    ):
        "\n    usage.xarray: 2\n    "
        ...

    def __iter__(self: object, /):
        "\n    usage.xarray: 3\n    usage.dask: 22\n    "
        ...

    def drop(self: object, /, labels: numpy.ndarray):
        "\n    usage.xarray: 2\n    usage.dask: 1\n    "
        ...

    def astype(self: object, /, dtype: Union[numpy.dtype, Literal["int64"]]):
        "\n    usage.xarray: 1\n    usage.dask: 12\n    "
        ...

    def __contains__(self: object, _0: str, /):
        "\n    usage.dask: 135\n    "
        ...

    def difference(
        self: object,
        /,
        other: Union[List[Literal["A"]], pandas.core.indexes.base.Index],
    ):
        "\n    usage.dask: 6\n    "
        ...

    def __eq__(
        self: object,
        _0: Union[List[Literal[("x", "b", "c", "a")]], pandas.core.indexes.base.Index],
        /,
    ):
        "\n    usage.dask: 14\n    "
        ...

    def intersection(self: object, /, other: pandas.core.indexes.base.Index):
        "\n    usage.dask: 2\n    "
        ...

    def _get_level_values(self: object, /, level: int):
        "\n    usage.dask: 7\n    "
        ...

    def min(self: object, /):
        "\n    usage.dask: 1\n    "
        ...

    def max(self: object, /):
        "\n    usage.dask: 1\n    "
        ...

    def get_slice_bound(
        self: object,
        /,
        label: object,
        side: Literal[("left", "right")],
        kind: Literal["loc"],
    ):
        "\n    usage.dask: 32\n    "
        ...

    def memory_usage(self: object, /):
        "\n    usage.dask: 3\n    "
        ...

    def dropna(self: object, /):
        "\n    usage.dask: 1\n    "
        ...

    def drop_duplicates(self: object, /):
        "\n    usage.dask: 1\n    "
        ...

    def isin(self: object, /, values: Union[pandas.core.series.Series, List[int]]):
        "\n    usage.dask: 4\n    "
        ...

    def shift(self: object, /, periods: int, freq: None):
        "\n    usage.dask: 1\n    "
        ...

    def union(
        self: object,
        /,
        other: Union[
            pandas.core.indexes.datetimes.DatetimeIndex,
            pandas.core.indexes.numeric.Int64Index,
        ],
    ):
        "\n    usage.dask: 2\n    "
        ...

    def to_frame(
        self: object,
        /,
        index: bool = ...,
        name: Union[Literal[("bar", "foo")], None] = ...,
    ):
        "\n    usage.dask: 6\n    "
        ...
