from typing import *


class RangeIndex:

    # usage.dask: 1
    __module__: ClassVar[object]

    # usage.dask: 2
    # usage.statsmodels: 1
    __name__: ClassVar[object]

    # usage.dask: 1
    array: object

    # usage.dask: 11
    # usage.xarray: 4
    dtype: object

    # usage.dask: 1
    # usage.statsmodels: 2
    is_all_dates: object

    # usage.dask: 1
    # usage.xarray: 2
    is_monotonic: object

    # usage.sklearn: 2
    # usage.xarray: 6
    is_unique: object

    # usage.dask: 16
    # usage.geopandas: 7
    # usage.koalas: 2
    # usage.prophet: 1
    # usage.seaborn: 2
    # usage.statsmodels: 2
    # usage.xarray: 4
    name: Union[str, None]

    # usage.dask: 1
    # usage.geopandas: 6
    # usage.koalas: 3
    names: List[Literal["__index_level_0__"]]

    # usage.statsmodels: 21
    # usage.xarray: 1
    shape: object

    # usage.xarray: 3
    size: object

    # usage.statsmodels: 2
    start: object

    # usage.statsmodels: 4
    step: object

    # usage.statsmodels: 2
    stop: object

    # usage.modin: 1
    # usage.seaborn: 1
    # usage.statsmodels: 5
    # usage.xarray: 3
    values: object

    @overload
    def __add__(self, _0: Union[numpy.datetime64, numpy.timedelta64], /):
        """
        usage.pandas: 2
        """
        ...

    @overload
    def __add__(self, _0: int, /):
        """
        usage.dask: 1
        """
        ...

    def __add__(self, _0: Union[int, numpy.timedelta64, numpy.datetime64], /):
        """
        usage.dask: 1
        usage.pandas: 2
        """
        ...

    @overload
    def __contains__(self, _0: Literal["geometry"], /):
        """
        usage.geopandas: 1
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
    def __contains__(self, _0: int, /):
        """
        usage.dask: 1
        """
        ...

    def __contains__(
        self, _0: Union[Literal["dtype", "divisions", "geometry"], int], /
    ):
        """
        usage.dask: 3
        usage.geopandas: 1
        """
        ...

    @overload
    def __eq__(self, _0: pandas.core.indexes.range.RangeIndex, /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __eq__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 4
        """
        ...

    def __eq__(self, _0: Union[numpy.ndarray, pandas.core.indexes.range.RangeIndex], /):
        """
        usage.pandas: 4
        usage.statsmodels: 2
        """
        ...

    def __floordiv__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 4
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, int, None], /):
        """
        usage.statsmodels: 8
        usage.xarray: 1
        """
        ...

    @overload
    def __getitem__(self, _0: int, /):
        """
        usage.dask: 4
        usage.statsmodels: 26
        usage.xarray: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, None, None], /):
        """
        usage.statsmodels: 2
        usage.xarray: 3
        """
        ...

    @overload
    def __getitem__(self, _0: numpy.ndarray, /):
        """
        usage.modin: 1
        usage.statsmodels: 4
        usage.xarray: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[int, int, int], /):
        """
        usage.dask: 1
        usage.statsmodels: 10
        usage.xarray: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[int, None, int], /):
        """
        usage.modin: 1
        usage.statsmodels: 12
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[pandas.core.series.Series, ellipsis], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["c"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["aa"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["string"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: pandas.core.series.Series, /):
        """
        usage.prophet: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[numpy.int64, int, numpy.int64], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["2010-1-9"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["2010-1-4"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["2010-1-10"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["2010-1-7"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[numpy.int64, None, numpy.int64], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["2010-1-6"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["2010-1-13"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[numpy.int64, numpy.int64, numpy.int64], /):
        """
        usage.modin: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[numpy.int64], /):
        """
        usage.modin: 1
        """
        ...

    def __getitem__(self, _0: object, /):
        """
        usage.dask: 5
        usage.modin: 4
        usage.prophet: 1
        usage.statsmodels: 75
        usage.xarray: 7
        """
        ...

    def __iadd__(self, _0: int, /):
        """
        usage.geopandas: 1
        """
        ...

    def __iter__(self, /):
        """
        usage.koalas: 1
        usage.networkx: 1
        usage.statsmodels: 3
        usage.xarray: 1
        """
        ...

    def __le__(self, _0: int, /):
        """
        usage.statsmodels: 1
        """
        ...

    def __lt__(self, _0: int, /):
        """
        usage.statsmodels: 3
        """
        ...

    def __mod__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 3
        """
        ...

    @overload
    def __mul__(self, _0: Union[numpy.ndarray, numpy.timedelta64], /):
        """
        usage.pandas: 5
        """
        ...

    @overload
    def __mul__(self, _0: int, /):
        """
        usage.dask: 1
        """
        ...

    def __mul__(self, _0: Union[int, numpy.timedelta64, numpy.ndarray], /):
        """
        usage.dask: 1
        usage.pandas: 5
        """
        ...

    def __neg__(self, /):
        """
        usage.dask: 1
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

    @overload
    def __rmul__(self, _0: Union[numpy.timedelta64, numpy.ndarray], /):
        """
        usage.pandas: 2
        """
        ...

    @overload
    def __rmul__(self, _0: int, /):
        """
        usage.dask: 1
        """
        ...

    def __rmul__(self, _0: Union[int, numpy.ndarray, numpy.timedelta64], /):
        """
        usage.dask: 1
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

    def copy(self, /, deep: bool):
        """
        usage.xarray: 1
        """
        ...

    def drop_duplicates(self, /):
        """
        usage.dask: 1
        """
        ...

    def equals(self, /, other: pandas.core.indexes.numeric.Int64Index):
        """
        usage.statsmodels: 2
        usage.xarray: 3
        """
        ...

    def get_indexer(self, /, target: numpy.ndarray, method: None, tolerance: None):
        """
        usage.xarray: 1
        """
        ...

    def get_loc(self, /, key: int, method: None, tolerance: None):
        """
        usage.xarray: 1
        """
        ...

    def map(self, /, mapper: Callable, na_action: None):
        """
        usage.dask: 1
        """
        ...

    @overload
    def to_frame(self, /, index: bool, name: None):
        """
        usage.dask: 1
        """
        ...

    @overload
    def to_frame(self, /, name: Literal["bar"]):
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

    def to_frame(self, /, name: Union[Literal["bar"], None], index: bool = ...):
        """
        usage.dask: 3
        """
        ...

    def to_series(self, /):
        """
        usage.dask: 1
        """
        ...
