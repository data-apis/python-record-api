from typing import *


class MultiIndex:

    # usage.dask: 1
    __module__: ClassVar[object]

    # usage.dask: 3
    # usage.xarray: 1
    __name__: ClassVar[object]

    @overload
    @classmethod
    def from_arrays(cls, /, arrays: List[xarray.coding.cftimeindex.CFTimeIndex]):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def from_arrays(
        cls,
        /,
        arrays: List[List[Literal["b", "a", "z", "y"]]],
        names: List[Literal["y2", "y1"]],
    ):
        """
        usage.xarray: 2
        """
        ...

    @overload
    @classmethod
    def from_arrays(
        cls,
        /,
        arrays: List[
            Union[
                pandas.core.indexes.category.CategoricalIndex,
                pandas.core.indexes.numeric.Int64Index,
            ]
        ],
        names: pandas.core.indexes.frozen.FrozenList,
    ):
        """
        usage.dask: 1
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def from_arrays(
        cls,
        /,
        arrays: List[
            Union[pandas.core.indexes.datetimes.DatetimeIndex, List[Literal["b", "a"]]]
        ],
        names: Tuple[Literal["level_str"], Literal["level_date"]],
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def from_arrays(
        cls,
        /,
        arrays: List[List[Union[int, Literal["c", "b", "a"]]]],
        names: List[Literal["y", "x"]],
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def from_arrays(cls, /, arrays: List[List[int]], names: List[Literal["y", "x"]]):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def from_arrays(
        cls,
        /,
        arrays: List[pandas.core.indexes.category.CategoricalIndex],
        names: pandas.core.indexes.frozen.FrozenList,
    ):
        """
        usage.dask: 1
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def from_arrays(
        cls,
        /,
        arrays: List[
            Union[
                pandas.core.indexes.numeric.Int64Index,
                pandas.core.indexes.category.CategoricalIndex,
            ]
        ],
        names: pandas.core.indexes.frozen.FrozenList,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def from_arrays(cls, /, arrays: List[pandas.core.indexes.numeric.Int64Index]):
        """
        usage.dask: 2
        """
        ...

    @overload
    @classmethod
    def from_arrays(cls, /, arrays: List[pandas.core.indexes.base.Index]):
        """
        usage.dask: 2
        """
        ...

    @classmethod
    def from_arrays(
        cls,
        /,
        arrays: list,
        names: Union[
            pandas.core.indexes.frozen.FrozenList,
            List[Literal["y2", "y1", "y", "x"]],
            Tuple[Literal["level_str"], Literal["level_date"]],
        ] = ...,
    ):
        """
        usage.dask: 7
        usage.xarray: 8
        """
        ...

    @overload
    @classmethod
    def from_product(cls, /, iterables: List[List[Union[int, Literal["b", "a"]]]]):
        """
        usage.xarray: 2
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[List[Union[Literal["d", "c", "b", "a"], int]]],
        names: Tuple[Literal["level_1"], Literal["level_2"]],
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[List[Union[Literal["b", "a"], int]]],
        names: Tuple[Literal["one"], Literal["two"], Literal["three"]],
    ):
        """
        usage.xarray: 4
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: pandas.core.indexes.frozen.FrozenList,
        names: pandas.core.indexes.frozen.FrozenList,
    ):
        """
        usage.xarray: 2
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[List[Union[int, Literal["c", "b", "a"]]]],
        names: List[Literal["y", "x"]],
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[
                pandas.core.indexes.base.Index, pandas.core.indexes.numeric.Int64Index
            ]
        ],
        names: List[Literal["y", "x"]],
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[List[Union[Literal["c", "b", "a"], int]]],
        names: List[Literal["x", "y"]],
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[
                pandas.core.indexes.numeric.Int64Index, pandas.core.indexes.base.Index
            ]
        ],
        names: List[Literal["x", "y"]],
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[
                pandas.core.indexes.base.Index, pandas.core.indexes.numeric.Int64Index
            ]
        ],
        names: List[Literal["A", "B"]],
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[pandas.core.indexes.range.RangeIndex],
        names: List[Literal["y", "x"]],
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[List[Union[Literal["b", "a"], int]]],
        names: Tuple[Literal["level_1"], Literal["level_2"]],
    ):
        """
        usage.xarray: 2
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[List[Union[Literal["b", "a"], int]]],
        names: Tuple[str, Literal["level_2"]],
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[List[Union[Literal["c", "b", "a"], int]]],
        names: Tuple[Literal["one"], Literal["two"]],
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[List[Union[int, Literal["b", "a"]]]],
        names: List[Literal["y", "x"]],
    ):
        """
        usage.xarray: 2
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[List[Union[Literal["b", "a"], int]]],
        names: List[Literal["x", "y"]],
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[pandas.core.indexes.base.Index, pandas.core.indexes.range.RangeIndex]
        ],
        names: List[Literal["y", "x"]],
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[pandas.core.indexes.numeric.Int64Index],
        names: List[Literal["y", "x"]],
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[Union[range, List[Literal["a"]]]],
        names: List[Literal["two", "one"]],
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[
                pandas.core.indexes.numeric.Int64Index, pandas.core.indexes.base.Index
            ]
        ],
        names: List[Literal["two", "one"]],
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[
                pandas.core.indexes.range.RangeIndex,
                pandas.core.indexes.numeric.Int64Index,
            ]
        ],
        names: List[Literal["y", "x"]],
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[List[Union[Literal["b", "a"], int]]],
        names: Tuple[Literal["one"], Literal["two"]],
    ):
        """
        usage.xarray: 2
        """
        ...

    @overload
    @classmethod
    def from_product(cls, /, iterables: List[List[int]]):
        """
        usage.xarray: 3
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls, /, iterables: List[numpy.ndarray], names: List[Literal["y", "x"]]
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def from_product(cls, /, iterables: List[List[Union[Literal["a", "b"], int]]]):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def from_product(cls, /, iterables: List[List[Union[Literal["c", "b", "a"], int]]]):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def from_product(cls, /, iterables: List[List[Union[Literal["b", "a"], int]]]):
        """
        usage.dask: 1
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[List[Union[Literal["b", "a"], int]]],
        names: List[Literal["level_2", "level_1"]],
    ):
        """
        usage.xarray: 2
        """
        ...

    @overload
    @classmethod
    def from_product(cls, /, iterables: List[pandas.core.indexes.base.Index]):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls, /, iterables: List[Union[List[Literal["e", "d", "c", "b", "a"]], range]]
    ):
        """
        usage.dask: 1
        """
        ...

    @classmethod
    def from_product(
        cls,
        /,
        iterables: Union[list, pandas.core.indexes.frozen.FrozenList],
        names: Union[
            List[str], Tuple[str, ...], pandas.core.indexes.frozen.FrozenList
        ] = ...,
    ):
        """
        usage.dask: 3
        usage.xarray: 38
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[List[int]], names: List[Literal["level1", "level0"]]
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: Tuple[
            Tuple[Literal["b"], int],
            Tuple[Literal["b"], int],
            Tuple[Literal["a"], int],
            Tuple[Literal["a"], int],
        ],
        names: List[Literal["two", "one"]],
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: Tuple[
            Tuple[Literal["a"], int],
            Tuple[Literal["a"], int],
            Tuple[Literal["b"], int],
            Tuple[Literal["b"], int],
        ],
        names: List[Literal["two", "one"]],
    ):
        """
        usage.xarray: 1
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

    @overload
    def __contains__(self, _0: Literal["divisions"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["columns"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["_meta"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["dtype"], /):
        """
        usage.dask: 1
        """
        ...

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

    @overload
    def __getitem__(self, _0: int, /):
        """
        usage.dask: 2
        usage.xarray: 2
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, int, None], /):
        """
        usage.xarray: 6
        """
        ...

    @overload
    def __getitem__(self, _0: slice[int, None, int], /):
        """
        usage.xarray: 3
        """
        ...

    @overload
    def __getitem__(self, _0: numpy.ndarray, /):
        """
        usage.xarray: 3
        """
        ...

    @overload
    def __getitem__(self, _0: slice[int, int, int], /):
        """
        usage.dask: 1
        usage.xarray: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, None, None], /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, None, None], /):
        """
        usage.xarray: 1
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

    def copy(self, /, deep: bool):
        """
        usage.xarray: 1
        """
        ...

    def equals(self, /, other: pandas.core.indexes.multi.MultiIndex):
        """
        usage.xarray: 2
        """
        ...

    def get_indexer(self, /, target: numpy.ndarray, method: None, tolerance: None):
        """
        usage.xarray: 2
        """
        ...

    def get_level_values(self, /, level: int):
        """
        usage.dask: 4
        """
        ...

    def get_loc(self, /, key: Literal["2001-01"]):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_loc_level(self, /, key: Tuple[Literal["a"], int], level: List[int]):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_loc_level(self, /, key: Tuple[Literal["a"]], level: List[int]):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_loc_level(self, /, key: Literal["a"], level: int):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_loc_level(
        self,
        /,
        key: Tuple[Literal["a"], int],
        level: Tuple[Literal["one"], Literal["two"]],
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_loc_level(self, /, key: Tuple[Literal["a"]], level: Tuple[Literal["one"]]):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_loc_level(self, /, key: Tuple[int], level: Tuple[Literal["x"]]):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_loc_level(self, /, key: Tuple[Literal["a"]], level: Tuple[Literal["y"]]):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_loc_level(
        self, /, key: Tuple[Literal["a"]], level: Tuple[Literal["variable"]]
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_loc_level(
        self, /, key: Tuple[Literal["b"]], level: Tuple[Literal["variable"]]
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_loc_level(self, /, key: Tuple[int, int], level: int):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_loc_level(self, /, key: int, level: int):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_loc_level(
        self,
        /,
        key: Tuple[Literal["a"], int],
        level: Tuple[Literal["one"], Literal["three"]],
    ):
        """
        usage.xarray: 1
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

    @overload
    def set_levels(self, /, levels: List[Literal["d", "c"]], level: int, inplace: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def set_levels(self, /, levels: List[Literal["c", "b"]], level: int, inplace: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def set_levels(self, /, levels: List[Literal["b"]], level: int, inplace: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def set_levels(self, /, levels: List[Literal["d"]], level: int, inplace: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def set_levels(self, /, levels: List[Literal["a"]], level: int, inplace: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def set_levels(
        self, /, levels: List[Literal["d", "b", "c"]], level: int, inplace: bool
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def set_levels(
        self, /, levels: List[Literal["d", "a", "b", "c"]], level: int, inplace: bool
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def set_levels(
        self, /, levels: List[Literal["c", "b", "a"]], level: int, inplace: bool
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def set_levels(self, /, levels: List[float], level: int, inplace: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def set_levels(
        self, /, levels: List[Literal["3", "2", "1"]], level: int, inplace: bool
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def set_levels(
        self, /, levels: List[Literal["b", "a", ""]], level: int, inplace: bool
    ):
        """
        usage.dask: 1
        """
        ...

    def set_levels(self, /, levels: List[Union[str, float]], level: int, inplace: bool):
        """
        usage.dask: 11
        """
        ...

    @overload
    def set_names(self, /, names: List[Literal["level1", "level0"]]):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def set_names(self, /, names: List[Literal["b", "a"]], inplace: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def set_names(self, /, names: List[Literal["c", "b", "a"]], inplace: bool):
        """
        usage.dask: 1
        """
        ...

    def set_names(
        self,
        /,
        names: List[Literal["level1", "level0", "b", "a", "c"]],
        inplace: bool = ...,
    ):
        """
        usage.dask: 2
        usage.xarray: 1
        """
        ...
