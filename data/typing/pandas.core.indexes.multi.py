from typing import *


class MultiIndex:

    # usage.dask: 1
    __module__: ClassVar[object]

    # usage.dask: 3
    # usage.xarray: 1
    __name__: ClassVar[object]

    @classmethod
    def from_arrays(cls, /, arrays: list):
        """
        usage.dask: 7
        usage.xarray: 8
        """
        ...

    @classmethod
    def from_product(
        cls, /, iterables: Union[list, pandas.core.indexes.frozen.FrozenList]
    ):
        """
        usage.dask: 3
        usage.xarray: 38
        """
        ...

    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: Union[
            Tuple[
                Tuple[Literal["a", "b"], int],
                Tuple[Literal["a", "b"], int],
                Tuple[Literal["b", "a"], int],
                Tuple[Literal["b", "a"], int],
            ],
            List[List[int]],
        ],
        names: List[Literal["level1", "level0", "two", "one"]],
    ):
        """
        usage.xarray: 3
        """
        ...

    # usage.dask: 1
    __class__: object

    # usage.dask: 2
    # usage.xarray: 6
    codes: object

    # usage.dask: 2
    # usage.xarray: 3
    dtype: object

    # usage.xarray: 1
    is_lexsorted: object

    # usage.xarray: 2
    is_monotonic: object

    # usage.xarray: 3
    is_unique: object

    # usage.dask: 9
    # usage.xarray: 18
    levels: object

    # usage.dask: 4
    # usage.xarray: 3
    name: Literal["z"]

    # usage.dask: 11
    # usage.xarray: 23
    names: List[str]

    # usage.dask: 3
    # usage.xarray: 4
    nlevels: object

    # usage.xarray: 1
    rename: object

    # usage.xarray: 1
    shape: object

    # usage.xarray: 2
    size: object

    # usage.xarray: 6
    values: object

    def __contains__(self, _0: Literal["dtype", "_meta", "columns", "divisions"], /):
        """
        usage.dask: 4
        """
        ...

    def __eq__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 4
        """
        ...

    def __getitem__(
        self,
        _0: Union[
            slice[Union[None, int], Union[int, None], Union[None, int]],
            int,
            numpy.ndarray,
        ],
        /,
    ):
        """
        usage.dask: 3
        usage.xarray: 17
        """
        ...

    def __iter__(self, /):
        """
        usage.dask: 1
        """
        ...

    def _get_level_number(self, /, level: int):
        """
        usage.xarray: 1
        """
        ...

    def _get_level_values(self, /, level: int):
        """
        usage.dask: 1
        """
        ...

    def append(self, /, other: List[pandas.core.indexes.multi.MultiIndex]):
        """
        usage.xarray: 3
        """
        ...

    def copy(self, /, deep: bool):
        """
        usage.xarray: 1
        """
        ...

    def equals(
        self,
        /,
        other: Union[
            pandas.core.indexes.base.Index, pandas.core.indexes.multi.MultiIndex
        ],
    ):
        """
        usage.xarray: 9
        """
        ...

    def get_indexer(self, /, target: numpy.ndarray, method: None, tolerance: None):
        """
        usage.xarray: 2
        """
        ...

    def get_level_values(self, /, level: Union[int, str]):
        """
        usage.dask: 5
        usage.xarray: 27
        """
        ...

    def get_loc(
        self, /, key: Union[Tuple[Literal["a", "b"], int, int], Literal["2001-01"]]
    ):
        """
        usage.xarray: 4
        """
        ...

    def get_loc_level(
        self,
        /,
        key: Union[Tuple[Union[int, Literal["a", "b"]], ...], Literal["a"], int],
        level: Union[Tuple[str, ...], List[int], int],
    ):
        """
        usage.xarray: 12
        """
        ...

    def get_locs(
        self, /, seq: Tuple[slice[None, None, None], int, Literal["no_level"]]
    ):
        """
        usage.xarray: 1
        """
        ...

    def remove_unused_levels(self, /):
        """
        usage.xarray: 1
        """
        ...

    def reorder_levels(self, /, order: List[Literal["level_1", "level_2"]]):
        """
        usage.xarray: 4
        """
        ...

    def set_levels(
        self,
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
        """
        usage.dask: 11
        usage.xarray: 1
        """
        ...

    def set_names(self, /, names: List[Literal["level1", "level0", "b", "a", "c"]]):
        """
        usage.dask: 2
        usage.xarray: 1
        """
        ...

    def union(self, /, other: pandas.core.indexes.multi.MultiIndex):
        """
        usage.dask: 1
        """
        ...
