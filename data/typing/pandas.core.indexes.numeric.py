from typing import *


class Float64Index:

    # usage.dask: 1
    __module__: ClassVar[object]

    # usage.dask: 2
    __name__: ClassVar[object]

    # usage.dask: 1
    array: object

    # usage.dask: 7
    # usage.xarray: 4
    dtype: object

    # usage.dask: 1
    # usage.xarray: 2
    is_monotonic: object

    # usage.xarray: 3
    is_unique: object

    # usage.dask: 9
    # usage.xarray: 1
    name: Union[Literal["x"], None]

    # usage.dask: 4
    names: List[str]

    # usage.xarray: 1
    nlevels: object

    # usage.xarray: 1
    shape: object

    # usage.xarray: 2
    size: object

    # usage.dask: 2
    # usage.xarray: 3
    values: object

    def __add__(self, _0: Union[numpy.float64, numpy.timedelta64, numpy.datetime64], /):
        """
        usage.pandas: 3
        """
        ...

    @overload
    def __contains__(self, _0: str, /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __contains__(self, _0: Literal["divisions"], /):
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

    def __contains__(self, _0: str, /):
        """
        usage.dask: 4
        """
        ...

    def __eq__(self, _0: Union[numpy.ndarray, numpy.float64], /):
        """
        usage.pandas: 9
        """
        ...

    def __floordiv__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 4
        """
        ...

    @overload
    def __getitem__(self, _0: numpy.ndarray, /):
        """
        usage.xarray: 3
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, int, None], /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[int, None, int], /):
        """
        usage.xarray: 2
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, None, None], /):
        """
        usage.xarray: 2
        """
        ...

    @overload
    def __getitem__(self, _0: int, /):
        """
        usage.dask: 4
        usage.xarray: 2
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
    def __getitem__(self, _0: slice[int, None, int], /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[int, int, int], /):
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

    @overload
    def __getitem__(self, _0: slice[None, int, None], /):
        """
        usage.xarray: 1
        """
        ...

    def __getitem__(
        self,
        _0: Union[
            int,
            numpy.ndarray,
            slice[Union[None, int], Union[int, None], Union[None, int]],
        ],
        /,
    ):
        """
        usage.dask: 5
        usage.xarray: 15
        """
        ...

    def __mod__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 3
        """
        ...

    def __mul__(self, _0: Union[numpy.ndarray, numpy.timedelta64], /):
        """
        usage.pandas: 5
        """
        ...

    def __radd__(self, _0: Union[numpy.datetime64, numpy.timedelta64], /):
        """
        usage.pandas: 2
        """
        ...

    def __rfloordiv__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    def __rmul__(self, _0: Union[numpy.timedelta64, numpy.ndarray], /):
        """
        usage.pandas: 2
        """
        ...

    def __rsub__(
        self, _0: Union[numpy.ndarray, numpy.timedelta64, numpy.datetime64], /
    ):
        """
        usage.pandas: 4
        """
        ...

    def __rtruediv__(self, _0: Union[numpy.timedelta64, numpy.ndarray], /):
        """
        usage.pandas: 2
        """
        ...

    def __sub__(
        self,
        _0: Union[numpy.ndarray, numpy.datetime64, numpy.timedelta64, numpy.float64],
        /,
    ):
        """
        usage.pandas: 5
        """
        ...

    def __truediv__(self, _0: Union[numpy.ndarray, numpy.timedelta64], /):
        """
        usage.pandas: 5
        """
        ...

    def astype(self, /, dtype: pandas.core.dtypes.dtypes.CategoricalDtype):
        """
        usage.dask: 1
        """
        ...

    def copy(self, /, deep: bool):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_indexer(self, /, target: numpy.ndarray, method: None, tolerance: None):
        """
        usage.xarray: 5
        """
        ...

    @overload
    def get_indexer(
        self, /, target: numpy.ndarray, method: Literal["pad"], tolerance: None
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_indexer(
        self, /, target: numpy.ndarray, method: Literal["backfill"], tolerance: None
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_indexer(
        self, /, target: numpy.ndarray, method: Literal["nearest"], tolerance: None
    ):
        """
        usage.xarray: 1
        """
        ...

    def get_indexer(
        self,
        /,
        target: numpy.ndarray,
        method: Union[Literal["nearest", "backfill", "pad"], None],
        tolerance: None,
    ):
        """
        usage.xarray: 8
        """
        ...

    @overload
    def get_loc(self, /, key: float, method: Literal["nearest"], tolerance: None):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_loc(self, /, key: float, method: None, tolerance: None):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_loc(self, /, key: float, method: Literal["nearest"], tolerance: int):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_loc(self, /, key: numpy.float64, method: Literal["nearest"]):
        """
        usage.xarray: 2
        """
        ...

    @overload
    def get_loc(self, /, key: numpy.int64, method: Literal["nearest"]):
        """
        usage.xarray: 2
        """
        ...

    def get_loc(
        self,
        /,
        key: Union[numpy.int64, float, numpy.float64],
        method: Union[Literal["nearest"], None],
        tolerance: Union[int, None] = ...,
    ):
        """
        usage.xarray: 7
        """
        ...

    def identical(self, /, other: pandas.core.indexes.numeric.Float64Index):
        """
        usage.xarray: 1
        """
        ...

    def set_names(self, /, names: List[Literal["b"]], inplace: bool):
        """
        usage.dask: 1
        """
        ...


class Int64Index:

    # usage.dask: 1
    __module__: ClassVar[object]

    # usage.dask: 3
    __name__: ClassVar[object]

    # usage.dask: 1
    __class__: object

    # usage.dask: 1
    array: object

    # usage.dask: 11
    # usage.xarray: 6
    dtype: object

    # usage.dask: 1
    # usage.xarray: 2
    is_monotonic: object

    # usage.dask: 1
    # usage.xarray: 5
    is_unique: object

    # usage.dask: 21
    # usage.xarray: 13
    name: Union[None, Literal["foo", "C", "b", "idx", "a"]]

    # usage.dask: 6
    names: Union[pandas.core.indexes.frozen.FrozenList, List[str]]

    # usage.dask: 2
    nbytes: object

    # usage.dask: 1
    # usage.xarray: 1
    nlevels: object

    # usage.xarray: 2
    shape: object

    # usage.dask: 2
    # usage.xarray: 10
    size: object

    # usage.dask: 3
    # usage.xarray: 3
    values: object

    def __add__(self, _0: Union[numpy.int64, numpy.timedelta64, numpy.datetime64], /):
        """
        usage.pandas: 3
        """
        ...

    @overload
    def __contains__(self, _0: Literal["divisions"], /):
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

    @overload
    def __contains__(self, _0: str, /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __contains__(self, _0: int, /):
        """
        usage.dask: 3
        """
        ...

    @overload
    def __contains__(self, _0: None, /):
        """
        usage.dask: 1
        """
        ...

    def __contains__(self, _0: Union[None, str, int], /):
        """
        usage.dask: 8
        """
        ...

    def __eq__(self, _0: Union[numpy.ndarray, numpy.int64], /):
        """
        usage.pandas: 9
        """
        ...

    def __floordiv__(
        self, _0: Union[numpy.float64, numpy.int64, numpy.ndarray, numpy.uint64], /
    ):
        """
        usage.pandas: 11
        """
        ...

    @overload
    def __ge__(self, _0: int, /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __ge__(self, _0: float, /):
        """
        usage.dask: 1
        """
        ...

    def __ge__(self, _0: Union[float, int], /):
        """
        usage.dask: 3
        """
        ...

    @overload
    def __getitem__(self, _0: numpy.ndarray, /):
        """
        usage.xarray: 4
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, None, None], /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def __getitem__(self, _0: int, /):
        """
        usage.dask: 8
        usage.xarray: 3
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, int, None], /):
        """
        usage.dask: 2
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
    def __getitem__(self, _0: slice[int, None, int], /):
        """
        usage.xarray: 3
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
            int,
            numpy.ndarray,
            slice[Union[int, None], Union[None, int], Union[int, None]],
        ],
        /,
    ):
        """
        usage.dask: 11
        usage.xarray: 16
        """
        ...

    @overload
    def __gt__(self, _0: int, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __gt__(self, _0: float, /):
        """
        usage.dask: 1
        """
        ...

    def __gt__(self, _0: Union[float, int], /):
        """
        usage.dask: 2
        """
        ...

    def __iter__(self, /):
        """
        usage.dask: 4
        usage.xarray: 2
        """
        ...

    @overload
    def __le__(self, _0: int, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __le__(self, _0: float, /):
        """
        usage.dask: 1
        """
        ...

    def __le__(self, _0: Union[float, int], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __lt__(self, _0: int, /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __lt__(self, _0: float, /):
        """
        usage.dask: 1
        """
        ...

    def __lt__(self, _0: Union[float, int], /):
        """
        usage.dask: 3
        """
        ...

    def __mod__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 3
        """
        ...

    def __mul__(self, _0: Union[numpy.ndarray, numpy.timedelta64], /):
        """
        usage.pandas: 6
        """
        ...

    def __radd__(self, _0: Union[numpy.datetime64, numpy.timedelta64], /):
        """
        usage.pandas: 4
        """
        ...

    def __rfloordiv__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    def __rmul__(self, _0: Union[numpy.timedelta64, numpy.ndarray], /):
        """
        usage.pandas: 5
        """
        ...

    def __rsub__(self, _0: Union[numpy.datetime64, numpy.timedelta64], /):
        """
        usage.pandas: 4
        """
        ...

    def __rtruediv__(self, _0: Union[numpy.timedelta64, numpy.ndarray], /):
        """
        usage.pandas: 4
        """
        ...

    def __sub__(self, _0: Union[numpy.int64, numpy.timedelta64, numpy.datetime64], /):
        """
        usage.pandas: 3
        """
        ...

    def __truediv__(self, _0: Union[numpy.ndarray, numpy.timedelta64], /):
        """
        usage.pandas: 5
        """
        ...

    def copy(self, /, deep: bool):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def drop(self, /, labels: numpy.ndarray, errors: Literal["raise"]):
        """
        usage.xarray: 2
        """
        ...

    @overload
    def drop(self, /, labels: numpy.ndarray, errors: Literal["ignore"]):
        """
        usage.xarray: 1
        """
        ...

    def drop(self, /, labels: numpy.ndarray, errors: Literal["raise", "ignore"]):
        """
        usage.xarray: 3
        """
        ...

    def drop_duplicates(self, /):
        """
        usage.dask: 2
        """
        ...

    def dropna(self, /):
        """
        usage.dask: 1
        """
        ...

    def equals(self, /, other: pandas.core.indexes.numeric.Int64Index):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_indexer(self, /, target: numpy.ndarray, method: None, tolerance: None):
        """
        usage.xarray: 3
        """
        ...

    @overload
    def get_indexer(
        self, /, target: numpy.ndarray, method: Literal["backfill"], tolerance: int
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_indexer(
        self, /, target: numpy.ndarray, method: Literal["backfill"], tolerance: float
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_indexer(
        self, /, target: numpy.ndarray, method: Literal["backfill"], tolerance: None
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_indexer(
        self, /, target: numpy.ndarray, method: Literal["pad"], tolerance: None
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_indexer(
        self, /, target: numpy.ndarray, method: Literal["pad"], tolerance: float
    ):
        """
        usage.xarray: 1
        """
        ...

    def get_indexer(
        self,
        /,
        target: numpy.ndarray,
        method: Union[Literal["pad", "backfill"], None],
        tolerance: Union[float, int, None],
    ):
        """
        usage.xarray: 8
        """
        ...

    @overload
    def get_loc(self, /, key: int, method: None, tolerance: None):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_loc(self, /, key: numpy.int64, method: Literal["nearest"]):
        """
        usage.xarray: 2
        """
        ...

    @overload
    def get_loc(self, /, key: numpy.float64, method: Literal["nearest"]):
        """
        usage.xarray: 2
        """
        ...

    @overload
    def get_loc(self, /, key: float, method: None, tolerance: None):
        """
        usage.xarray: 1
        """
        ...

    def get_loc(
        self,
        /,
        key: Union[float, numpy.int64, int, numpy.float64],
        method: Union[None, Literal["nearest"]],
        tolerance: None = ...,
    ):
        """
        usage.xarray: 6
        """
        ...

    @overload
    def isin(self, /, values: dask.delayed.Delayed):
        """
        usage.dask: 1
        """
        ...

    @overload
    def isin(self, /, values: List[int]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def isin(self, /, values: dask.delayed.DelayedLeaf):
        """
        usage.dask: 1
        """
        ...

    @overload
    def isin(self, /, values: pandas.core.series.Series):
        """
        usage.dask: 1
        """
        ...

    def isin(
        self,
        /,
        values: Union[
            pandas.core.series.Series,
            dask.delayed.Delayed,
            dask.delayed.DelayedLeaf,
            List[int],
        ],
    ):
        """
        usage.dask: 4
        """
        ...

    def max(self, /):
        """
        usage.dask: 1
        """
        ...

    def min(self, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def set_names(self, /, names: List[Literal["a"]], inplace: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def set_names(self, /, names: List[Literal["b"]], inplace: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def set_names(self, /, names: List[Literal["key"]], inplace: bool):
        """
        usage.dask: 1
        """
        ...

    def set_names(self, /, names: List[Literal["a", "b", "key"]], inplace: bool):
        """
        usage.dask: 3
        """
        ...

    @overload
    def to_frame(self, /, index: bool, name: None):
        """
        usage.dask: 1
        """
        ...

    @overload
    def to_frame(self, /, index: bool, name: Literal["bar"]):
        """
        usage.dask: 1
        """
        ...

    def to_frame(self, /, index: bool, name: Union[Literal["bar"], None]):
        """
        usage.dask: 2
        """
        ...

    def to_series(self, /):
        """
        usage.dask: 1
        """
        ...


class UInt64Index:

    # usage.dask: 1
    __module__: ClassVar[object]

    # usage.dask: 2
    name: object

    def __add__(self, _0: Union[numpy.datetime64, numpy.timedelta64], /):
        """
        usage.pandas: 2
        """
        ...

    def __eq__(self, _0: Union[numpy.ndarray, numpy.uint64], /):
        """
        usage.pandas: 7
        """
        ...

    def __floordiv__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 4
        """
        ...

    def __mod__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 3
        """
        ...

    def __mul__(self, _0: Union[numpy.ndarray, numpy.timedelta64], /):
        """
        usage.pandas: 5
        """
        ...

    def __radd__(self, _0: Union[numpy.datetime64, numpy.timedelta64], /):
        """
        usage.pandas: 2
        """
        ...

    def __rfloordiv__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    def __rmul__(self, _0: Union[numpy.timedelta64, numpy.ndarray], /):
        """
        usage.pandas: 2
        """
        ...

    def __rsub__(self, _0: Union[numpy.datetime64, numpy.timedelta64], /):
        """
        usage.pandas: 2
        """
        ...

    def __rtruediv__(self, _0: Union[numpy.timedelta64, numpy.ndarray], /):
        """
        usage.pandas: 2
        """
        ...

    def __sub__(self, _0: Union[numpy.datetime64, numpy.timedelta64], /):
        """
        usage.pandas: 2
        """
        ...

    def __truediv__(self, _0: Union[numpy.ndarray, numpy.timedelta64], /):
        """
        usage.pandas: 5
        """
        ...
