from typing import *


class Series:

    # usage.dask: 4
    __module__: ClassVar[object]

    # usage.dask: 7
    # usage.sklearn: 1
    __name__: ClassVar[object]

    @overload
    @classmethod
    def __ne__(cls, _0: Type[pandas.core.series.Series], /):
        """
        usage.dask: 4
        """
        ...

    @overload
    @classmethod
    def __ne__(cls, _0: numpy.ndarray, /):
        """
        usage.pandas: 6
        """
        ...

    @classmethod
    def __ne__(cls, _0: Union[numpy.ndarray, Type[pandas.core.series.Series]], /):
        """
        usage.dask: 4
        usage.pandas: 6
        """
        ...

    @classmethod
    def __rmod__(cls, _0: Union[numpy.timedelta64, numpy.float64, str], /):
        """
        usage.pandas: 2
        usage.sklearn: 1
        """
        ...

    # usage.dask: 6
    # usage.sklearn: 1
    __class__: object

    # usage.dask: 2
    _constructor: object

    # usage.dask: 1
    _data: object

    # usage.dask: 3
    _values: object

    # usage.dask: 28
    cat: object

    # usage.dask: 1
    div: object

    # usage.dask: 1
    divide: object

    # usage.dask: 2
    # usage.xarray: 2
    dt: object

    # usage.dask: 65
    # usage.sklearn: 9
    dtype: object

    # usage.sklearn: 2
    dtypes: object

    # usage.dask: 1
    empty: object

    # usage.dask: 31
    # usage.sklearn: 1
    # usage.xarray: 3
    iloc: object

    # usage.dask: 83
    # usage.sklearn: 3
    # usage.xarray: 23
    index: object

    # usage.dask: 25
    # usage.sklearn: 1
    # usage.xarray: 3
    loc: object

    # usage.dask: 48
    # usage.sklearn: 6
    # usage.xarray: 5
    name: Union[str, None]

    # usage.dask: 2
    nbytes: object

    # usage.dask: 6
    # usage.sklearn: 4
    ndim: object

    # usage.dask: 1
    rdiv: object

    # usage.dask: 7
    # usage.sklearn: 12
    shape: object

    # usage.dask: 2
    size: object

    # usage.dask: 26
    str: object

    # usage.dask: 40
    # usage.xarray: 16
    values: object

    @overload
    def __add__(self, _0: Union[numpy.ndarray, numpy.timedelta64, numpy.datetime64], /):
        """
        usage.pandas: 39
        """
        ...

    @overload
    def __add__(self, _0: object, /):
        """
        usage.dask: 55
        """
        ...

    def __add__(self, _0: object, /):
        """
        usage.dask: 55
        usage.pandas: 39
        """
        ...

    @overload
    def __and__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 3
        """
        ...

    @overload
    def __and__(self, _0: pandas.core.series.Series, /):
        """
        usage.dask: 5
        """
        ...

    def __and__(self, _0: Union[pandas.core.series.Series, numpy.ndarray], /):
        """
        usage.dask: 5
        usage.pandas: 3
        """
        ...

    def __array_wrap__(self, /, result: numpy.ndarray):
        """
        usage.dask: 3
        """
        ...

    def __contains__(self, _0: Literal["bool"], /):
        """
        usage.pandas: 1
        """
        ...

    @overload
    def __eq__(self, _0: object, /):
        """
        usage.dask: 43
        usage.pandas: 52
        """
        ...

    @overload
    def __eq__(
        self,
        _0: Union[
            List[Union[type, pandas.core.dtypes.dtypes.CategoricalDtype]],
            Type[numpy.float64],
        ],
        /,
    ):
        """
        usage.sklearn: 10
        """
        ...

    def __eq__(self, _0: object, /):
        """
        usage.dask: 43
        usage.pandas: 52
        usage.sklearn: 10
        """
        ...

    @overload
    def __floordiv__(self, _0: Union[numpy.timedelta64, numpy.ndarray], /):
        """
        usage.pandas: 6
        """
        ...

    @overload
    def __floordiv__(self, _0: Union[float, int], /):
        """
        usage.dask: 3
        """
        ...

    def __floordiv__(self, _0: Union[int, float, numpy.ndarray, numpy.timedelta64], /):
        """
        usage.dask: 3
        usage.pandas: 6
        """
        ...

    @overload
    def __ge__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 7
        """
        ...

    @overload
    def __ge__(self, _0: object, /):
        """
        usage.dask: 17
        """
        ...

    def __ge__(self, _0: object, /):
        """
        usage.dask: 17
        usage.pandas: 7
        """
        ...

    @overload
    def __getitem__(self, _0: cftime._cftime.DatetimeNoLeap, /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["0001"], /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: slice[Literal["0001-01-01"], Literal["0001-12-30"], Literal["0001-01-01"]],
        /,
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, Literal["0001-12-30"], None], /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: slice[
            cftime._cftime.DatetimeNoLeap,
            cftime._cftime.DatetimeNoLeap,
            cftime._cftime.DatetimeNoLeap,
        ],
        /,
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, cftime._cftime.DatetimeNoLeap, None], /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def __getitem__(self, _0: cftime._cftime.Datetime360Day, /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: slice[
            cftime._cftime.Datetime360Day,
            cftime._cftime.Datetime360Day,
            cftime._cftime.Datetime360Day,
        ],
        /,
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, cftime._cftime.Datetime360Day, None], /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def __getitem__(self, _0: cftime._cftime.DatetimeJulian, /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: slice[
            cftime._cftime.DatetimeJulian,
            cftime._cftime.DatetimeJulian,
            cftime._cftime.DatetimeJulian,
        ],
        /,
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, cftime._cftime.DatetimeJulian, None], /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def __getitem__(self, _0: cftime._cftime.DatetimeAllLeap, /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: slice[
            cftime._cftime.DatetimeAllLeap,
            cftime._cftime.DatetimeAllLeap,
            cftime._cftime.DatetimeAllLeap,
        ],
        /,
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, cftime._cftime.DatetimeAllLeap, None], /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def __getitem__(self, _0: cftime._cftime.DatetimeGregorian, /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: slice[
            cftime._cftime.DatetimeGregorian,
            cftime._cftime.DatetimeGregorian,
            cftime._cftime.DatetimeGregorian,
        ],
        /,
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, cftime._cftime.DatetimeGregorian, None], /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def __getitem__(self, _0: cftime._cftime.DatetimeProlepticGregorian, /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: slice[
            cftime._cftime.DatetimeProlepticGregorian,
            cftime._cftime.DatetimeProlepticGregorian,
            cftime._cftime.DatetimeProlepticGregorian,
        ],
        /,
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: slice[None, cftime._cftime.DatetimeProlepticGregorian, None], /
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def __getitem__(self, _0: int, /):
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
    def __getitem__(self, _0: object, /):
        """
        usage.dask: 84
        """
        ...

    def __getitem__(self, _0: object, /):
        """
        usage.dask: 84
        usage.xarray: 23
        """
        ...

    @overload
    def __gt__(self, _0: Union[numpy.timedelta64, numpy.ndarray], /):
        """
        usage.pandas: 5
        """
        ...

    @overload
    def __gt__(
        self, _0: Union[numpy.int64, pandas.core.series.Series, int, numpy.float64], /
    ):
        """
        usage.dask: 59
        """
        ...

    def __gt__(self, _0: object, /):
        """
        usage.dask: 59
        usage.pandas: 5
        """
        ...

    def __iadd__(self, _0: Union[numpy.ndarray, numpy.timedelta64], /):
        """
        usage.pandas: 2
        """
        ...

    def __invert__(self, /):
        """
        usage.dask: 1
        usage.xarray: 1
        """
        ...

    def __isub__(self, _0: Union[numpy.ndarray, numpy.timedelta64], /):
        """
        usage.pandas: 2
        """
        ...

    def __iter__(self, /):
        """
        usage.dask: 4
        usage.sklearn: 12
        """
        ...

    def __itruediv__(self, _0: pandas.core.series.Series, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __le__(self, _0: Union[numpy.ndarray, numpy.float64], /):
        """
        usage.pandas: 7
        """
        ...

    @overload
    def __le__(
        self,
        _0: Union[numpy.float64, float, pandas.core.series.Series, int, numpy.int64],
        /,
    ):
        """
        usage.dask: 16
        """
        ...

    def __le__(self, _0: object, /):
        """
        usage.dask: 16
        usage.pandas: 7
        """
        ...

    @overload
    def __lt__(self, _0: Union[numpy.ndarray, numpy.int64, numpy.float64], /):
        """
        usage.pandas: 4
        """
        ...

    @overload
    def __lt__(
        self,
        _0: Union[
            pandas._libs.tslibs.timedeltas.Timedelta,
            pandas.core.frame.DataFrame,
            pandas.core.series.Series,
        ],
        /,
    ):
        """
        usage.dask: 4
        """
        ...

    def __lt__(self, _0: object, /):
        """
        usage.dask: 4
        usage.pandas: 4
        """
        ...

    @overload
    def __mod__(self, _0: Union[numpy.timedelta64, numpy.ndarray], /):
        """
        usage.pandas: 57
        """
        ...

    @overload
    def __mod__(self, _0: int, /):
        """
        usage.dask: 5
        """
        ...

    def __mod__(self, _0: Union[int, numpy.ndarray, numpy.timedelta64], /):
        """
        usage.dask: 5
        usage.pandas: 57
        """
        ...

    @overload
    def __mul__(
        self,
        _0: Union[
            numpy.float32, numpy.ndarray, numpy.timedelta64, numpy.int64, numpy.float64
        ],
        /,
    ):
        """
        usage.pandas: 29
        """
        ...

    @overload
    def __mul__(self, _0: Union[pandas.core.series.Series, float, int], /):
        """
        usage.dask: 6
        """
        ...

    def __mul__(self, _0: object, /):
        """
        usage.dask: 6
        usage.pandas: 29
        """
        ...

    def __neg__(self, /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __or__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 3
        """
        ...

    @overload
    def __or__(self, _0: pandas.core.series.Series, /):
        """
        usage.dask: 3
        """
        ...

    def __or__(self, _0: Union[pandas.core.series.Series, numpy.ndarray], /):
        """
        usage.dask: 3
        usage.pandas: 3
        """
        ...

    @overload
    def __pow__(self, _0: numpy.timedelta64, /):
        """
        usage.pandas: 1
        """
        ...

    @overload
    def __pow__(self, _0: Union[int, float], /):
        """
        usage.dask: 5
        """
        ...

    def __pow__(self, _0: Union[float, int, numpy.timedelta64], /):
        """
        usage.dask: 5
        usage.pandas: 1
        """
        ...

    @overload
    def __radd__(self, _0: object, /):
        """
        usage.pandas: 46
        """
        ...

    @overload
    def __radd__(
        self,
        _0: Union[
            numpy.ndarray, pandas.core.series.Series, dask.dataframe.core.Scalar, int
        ],
        /,
    ):
        """
        usage.dask: 17
        """
        ...

    def __radd__(self, _0: object, /):
        """
        usage.dask: 17
        usage.pandas: 46
        """
        ...

    def __rand__(self, _0: pandas.core.series.Series, /):
        """
        usage.dask: 5
        """
        ...

    def __rfloordiv__(
        self, _0: Union[numpy.float64, numpy.int64, numpy.ndarray, numpy.timedelta64], /
    ):
        """
        usage.pandas: 6
        """
        ...

    @overload
    def __rmul__(self, _0: object, /):
        """
        usage.pandas: 30
        """
        ...

    @overload
    def __rmul__(self, _0: pandas.core.series.Series, /):
        """
        usage.dask: 3
        """
        ...

    @overload
    def __rmul__(self, _0: Union[int, float], /):
        """
        usage.sklearn: 2
        """
        ...

    def __rmul__(self, _0: object, /):
        """
        usage.dask: 3
        usage.pandas: 30
        usage.sklearn: 2
        """
        ...

    @overload
    def __ror__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    @overload
    def __ror__(self, _0: pandas.core.series.Series, /):
        """
        usage.dask: 3
        """
        ...

    def __ror__(self, _0: Union[pandas.core.series.Series, numpy.ndarray], /):
        """
        usage.dask: 3
        usage.pandas: 1
        """
        ...

    def __rpow__(self, _0: Union[numpy.float64, numpy.int64, numpy.timedelta64], /):
        """
        usage.pandas: 10
        """
        ...

    @overload
    def __rsub__(self, _0: object, /):
        """
        usage.pandas: 44
        """
        ...

    @overload
    def __rsub__(
        self, _0: Union[pandas.core.series.Series, pandas.core.frame.DataFrame], /
    ):
        """
        usage.dask: 10
        """
        ...

    def __rsub__(self, _0: object, /):
        """
        usage.dask: 10
        usage.pandas: 44
        """
        ...

    @overload
    def __rtruediv__(self, _0: object, /):
        """
        usage.pandas: 37
        """
        ...

    @overload
    def __rtruediv__(self, _0: pandas.core.series.Series, /):
        """
        usage.dask: 8
        """
        ...

    def __rtruediv__(self, _0: object, /):
        """
        usage.dask: 8
        usage.pandas: 37
        """
        ...

    def __rxor__(self, _0: pandas.core.series.Series, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(self, _0: int, _1: float, /):
        """
        usage.xarray: 2
        """
        ...

    @overload
    def __setitem__(self, _0: pandas.core.series.Series, _1: Union[float, int], /):
        """
        usage.dask: 3
        """
        ...

    def __setitem__(
        self, _0: Union[pandas.core.series.Series, int], _1: Union[int, float], /
    ):
        """
        usage.dask: 3
        usage.xarray: 2
        """
        ...

    @overload
    def __sub__(self, _0: Union[numpy.ndarray, numpy.datetime64, numpy.timedelta64], /):
        """
        usage.pandas: 35
        """
        ...

    @overload
    def __sub__(self, _0: Union[pandas.core.series.Series, int, numpy.float64], /):
        """
        usage.dask: 18
        """
        ...

    def __sub__(self, _0: object, /):
        """
        usage.dask: 18
        usage.pandas: 35
        """
        ...

    @overload
    def __truediv__(
        self, _0: Union[numpy.float64, numpy.timedelta64, numpy.ndarray], /
    ):
        """
        usage.pandas: 29
        """
        ...

    @overload
    def __truediv__(self, _0: Union[int, float, pandas.core.series.Series], /):
        """
        usage.dask: 10
        """
        ...

    def __truediv__(self, _0: object, /):
        """
        usage.dask: 10
        usage.pandas: 29
        """
        ...

    @overload
    def __xor__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    @overload
    def __xor__(self, _0: pandas.core.series.Series, /):
        """
        usage.dask: 1
        """
        ...

    def __xor__(self, _0: Union[pandas.core.series.Series, numpy.ndarray], /):
        """
        usage.dask: 1
        usage.pandas: 1
        """
        ...

    def abs(self, /):
        """
        usage.dask: 3
        """
        ...

    def add(
        self,
        /,
        other: Union[pandas.core.series.Series, int],
        fill_value: Union[None, int] = ...,
    ):
        """
        usage.dask: 7
        """
        ...

    def align(
        self,
        /,
        other: pandas.core.series.Series,
        join: Literal["right", "left", "outer", "inner"],
        axis: Union[int, None] = ...,
        fill_value: Union[None, int] = ...,
    ):
        """
        usage.dask: 20
        """
        ...

    def all(self, /, axis: int = ..., skipna: bool = ...):
        """
        usage.dask: 24
        """
        ...

    @overload
    def any(self, /):
        """
        usage.sklearn: 2
        usage.xarray: 1
        """
        ...

    @overload
    def any(self, /, axis: int = ..., skipna: bool = ...):
        """
        usage.dask: 8
        """
        ...

    def any(self, /, axis: int = ..., skipna: bool = ...):
        """
        usage.dask: 8
        usage.sklearn: 2
        usage.xarray: 1
        """
        ...

    def append(self, /, to_append: pandas.core.series.Series):
        """
        usage.dask: 2
        """
        ...

    @overload
    def apply(
        self, /, func: Callable, convert_dtype: bool = ..., args: Tuple[None, ...] = ...
    ):
        """
        usage.dask: 9
        """
        ...

    @overload
    def apply(self, /, func: Callable):
        """
        usage.sklearn: 1
        """
        ...

    def apply(
        self, /, func: Callable, convert_dtype: bool = ..., args: Tuple[None, ...] = ...
    ):
        """
        usage.dask: 9
        usage.sklearn: 1
        """
        ...

    @overload
    def astype(self, /, dtype: Type[int]):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def astype(
        self,
        /,
        dtype: Union[
            type, str, pandas.core.dtypes.dtypes.CategoricalDtype, numpy.dtype
        ],
    ):
        """
        usage.dask: 53
        """
        ...

    @overload
    def astype(
        self,
        /,
        dtype: Union[
            type,
            Literal["float", "int", "category"],
            pandas.core.dtypes.dtypes.CategoricalDtype,
        ],
        copy: bool = ...,
    ):
        """
        usage.sklearn: 10
        """
        ...

    def astype(
        self,
        /,
        dtype: Union[
            pandas.core.dtypes.dtypes.CategoricalDtype, numpy.dtype, str, type
        ],
        copy: bool = ...,
    ):
        """
        usage.dask: 53
        usage.sklearn: 10
        usage.xarray: 1
        """
        ...

    def autocorr(self, /, lag: int):
        """
        usage.dask: 4
        """
        ...

    def between(self, /, left: int, right: int, inclusive: bool = ...):
        """
        usage.dask: 2
        """
        ...

    def clip(
        self,
        /,
        lower: Union[None, int, float] = ...,
        upper: Union[float, int, None] = ...,
    ):
        """
        usage.dask: 13
        """
        ...

    def combine(
        self,
        /,
        other: pandas.core.series.Series,
        func: Callable,
        fill_value: Union[None, int],
    ):
        """
        usage.dask: 6
        """
        ...

    def combine_first(self, /, other: pandas.core.series.Series):
        """
        usage.dask: 5
        """
        ...

    def copy(self, /):
        """
        usage.dask: 3
        """
        ...

    def count(self, /, *, axis: Union[Literal["columns"], int] = ...):
        """
        usage.dask: 10
        """
        ...

    def cov(self, /, other: pandas.core.series.Series, min_periods: int = ...):
        """
        usage.dask: 2
        """
        ...

    def cummax(self, /, axis: None = ..., skipna: bool = ...):
        """
        usage.dask: 4
        """
        ...

    def cummin(self, /, axis: None = ..., skipna: bool = ...):
        """
        usage.dask: 4
        """
        ...

    def cumprod(self, /, axis: None = ..., skipna: bool = ...):
        """
        usage.dask: 4
        """
        ...

    def cumsum(self, /, axis: None = ..., skipna: bool = ...):
        """
        usage.dask: 5
        """
        ...

    def describe(
        self,
        /,
        include: Union[
            List[
                Union[
                    Type[numpy.timedelta64],
                    Literal["number", "object", "bool", "datetime"],
                ]
            ],
            Literal["all"],
            None,
        ] = ...,
        exclude: Union[None, List[Literal["object", "number"]]] = ...,
    ):
        """
        usage.dask: 10
        """
        ...

    def diff(self, /, periods: int = ...):
        """
        usage.dask: 7
        """
        ...

    def drop_duplicates(self, /, keep: Literal["last", "first"] = ...):
        """
        usage.dask: 12
        """
        ...

    def dropna(self, /):
        """
        usage.dask: 7
        usage.xarray: 2
        """
        ...

    def duplicated(self, /, keep: Literal["last"]):
        """
        usage.xarray: 1
        """
        ...

    def eq(self, /, other: pandas.core.series.Series, fill_value: int):
        """
        usage.dask: 1
        """
        ...

    def equals(self, /, other: pandas.core.series.Series):
        """
        usage.dask: 3
        usage.xarray: 8
        """
        ...

    def explode(self, /):
        """
        usage.dask: 5
        """
        ...

    def fillna(
        self,
        /,
        value: Union[pandas.core.series.Series, numpy.float64, int, None] = ...,
        method: Union[None, Literal["bfill", "ffill", "pad"]] = ...,
        axis: int = ...,
        limit: Union[None, int] = ...,
    ):
        """
        usage.dask: 23
        """
        ...

    def first(self, /, offset: str):
        """
        usage.dask: 24
        """
        ...

    def floordiv(
        self, /, other: Union[int, pandas.core.series.Series], fill_value: int
    ):
        """
        usage.dask: 2
        """
        ...

    def ge(self, /, other: pandas.core.series.Series, fill_value: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def groupby(self, /, by: pandas.core.resample.TimeGrouper):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def groupby(
        self,
        /,
        level: Union[List[int], int] = ...,
        sort: bool = ...,
        by: object = ...,
        group_keys: bool = ...,
    ):
        """
        usage.dask: 64
        """
        ...

    def groupby(
        self,
        /,
        level: Union[List[int], int] = ...,
        sort: bool = ...,
        by: object = ...,
        group_keys: bool = ...,
    ):
        """
        usage.dask: 64
        usage.xarray: 1
        """
        ...

    def gt(self, /, other: pandas.core.series.Series, fill_value: int):
        """
        usage.dask: 1
        """
        ...

    def head(self, /, n: int):
        """
        usage.dask: 7
        """
        ...

    def idxmax(self, /, axis: int = ..., skipna: bool = ...):
        """
        usage.dask: 8
        """
        ...

    def idxmin(self, /, skipna: bool):
        """
        usage.dask: 4
        """
        ...

    def isin(self, /, values: Union[pandas.core.series.Series, List[int]]):
        """
        usage.dask: 6
        """
        ...

    def isnull(self, /):
        """
        usage.dask: 5
        usage.xarray: 1
        """
        ...

    def items(self, /):
        """
        usage.dask: 1
        """
        ...

    def iteritems(self, /):
        """
        usage.dask: 4
        usage.xarray: 1
        """
        ...

    def last(self, /, offset: str):
        """
        usage.dask: 8
        """
        ...

    def le(self, /, other: pandas.core.series.Series, fill_value: int):
        """
        usage.dask: 1
        """
        ...

    def lt(self, /, other: pandas.core.series.Series, fill_value: int):
        """
        usage.dask: 1
        """
        ...

    def map(
        self,
        /,
        arg: Union[Callable, Dict[numpy.int64, numpy.int64], pandas.core.series.Series],
        na_action: None = ...,
    ):
        """
        usage.dask: 16
        """
        ...

    def mask(
        self,
        /,
        cond: pandas.core.series.Series,
        other: Union[pandas.core.series.Series, float] = ...,
    ):
        """
        usage.dask: 4
        """
        ...

    @overload
    def max(self, /, skipna: bool):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def max(
        self, /, axis: Union[Literal["columns"], None, int] = ..., skipna: bool = ...
    ):
        """
        usage.dask: 22
        """
        ...

    def max(
        self, /, axis: Union[Literal["columns"], None, int] = ..., skipna: bool = ...
    ):
        """
        usage.dask: 22
        usage.xarray: 1
        """
        ...

    @overload
    def mean(self, /, skipna: bool):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def mean(
        self, /, axis: Union[Literal["columns"], None, int] = ..., skipna: bool = ...
    ):
        """
        usage.dask: 25
        """
        ...

    def mean(
        self, /, axis: Union[Literal["columns"], None, int] = ..., skipna: bool = ...
    ):
        """
        usage.dask: 25
        usage.xarray: 1
        """
        ...

    def median(self, /):
        """
        usage.xarray: 1
        """
        ...

    def memory_usage(self, /, index: bool, deep: bool = ...):
        """
        usage.dask: 6
        """
        ...

    @overload
    def min(self, /, skipna: bool):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def min(
        self, /, axis: Union[Literal["columns"], None, int] = ..., skipna: bool = ...
    ):
        """
        usage.dask: 17
        """
        ...

    def min(
        self, /, axis: Union[Literal["columns"], None, int] = ..., skipna: bool = ...
    ):
        """
        usage.dask: 17
        usage.xarray: 1
        """
        ...

    def mod(self, /, other: Union[int, pandas.core.series.Series], fill_value: int):
        """
        usage.dask: 2
        """
        ...

    def mode(self, /):
        """
        usage.dask: 1
        """
        ...

    def mul(
        self, /, other: Union[pandas.core.series.Series, int], fill_value: int = ...
    ):
        """
        usage.dask: 4
        """
        ...

    def ne(self, /, other: pandas.core.series.Series, fill_value: int):
        """
        usage.dask: 1
        """
        ...

    def nlargest(self, /, n: int):
        """
        usage.dask: 4
        """
        ...

    def notna(self, /):
        """
        usage.dask: 1
        """
        ...

    def notnull(self, /):
        """
        usage.dask: 3
        """
        ...

    def nsmallest(self, /, n: int):
        """
        usage.dask: 2
        """
        ...

    def nunique(self, /):
        """
        usage.dask: 5
        """
        ...

    def pow(
        self, /, other: Union[int, pandas.core.series.Series], fill_value: int = ...
    ):
        """
        usage.dask: 3
        """
        ...

    @overload
    def prod(self, /, skipna: bool, min_count: int):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def prod(
        self, /, axis: Union[Literal["columns"], None, int] = ..., skipna: bool = ...
    ):
        """
        usage.dask: 10
        """
        ...

    def prod(
        self,
        /,
        axis: Union[Literal["columns"], None, int] = ...,
        skipna: bool = ...,
        min_count: int = ...,
    ):
        """
        usage.dask: 10
        usage.xarray: 1
        """
        ...

    def quantile(self, /, q: Union[List[float], numpy.ndarray, float] = ...):
        """
        usage.dask: 7
        """
        ...

    def radd(self, /, other: Union[int, pandas.core.series.Series], fill_value: int):
        """
        usage.dask: 2
        """
        ...

    def rank(self, /, method: Literal["dense"], ascending: bool):
        """
        usage.xarray: 1
        """
        ...

    def reindex(
        self,
        /,
        index: Union[
            pandas.core.indexes.datetimes.DatetimeIndex,
            pandas.core.indexes.multi.MultiIndex,
            pandas.core.indexes.numeric.Int64Index,
            numpy.ndarray,
        ],
    ):
        """
        usage.dask: 8
        """
        ...

    def rename(
        self,
        /,
        index: Union[str, pandas.core.series.Series, None, Callable] = ...,
        *,
        inplace: bool = ...,
    ):
        """
        usage.dask: 25
        """
        ...

    def replace(
        self,
        /,
        to_replace: Union[Dict[int, int], int, Literal["c"]],
        value: Union[None, float, int] = ...,
        regex: bool = ...,
    ):
        """
        usage.dask: 5
        """
        ...

    @overload
    def resample(self, /, rule: Literal["24H"]):
        """
        usage.xarray: 2
        """
        ...

    @overload
    def resample(self, /, rule: Literal["24H"], loffset: Literal["-12H"]):
        """
        usage.xarray: 2
        """
        ...

    @overload
    def resample(self, /, rule: Literal["3H"]):
        """
        usage.xarray: 8
        """
        ...

    @overload
    def resample(self, /, rule: Literal["1H"]):
        """
        usage.xarray: 2
        """
        ...

    @overload
    def resample(
        self,
        /,
        rule: object,
        closed: Union[None, Literal["left", "right"]] = ...,
        label: Union[None, Literal["left", "right"]] = ...,
    ):
        """
        usage.dask: 88
        """
        ...

    def resample(
        self,
        /,
        rule: object,
        closed: Union[None, Literal["left", "right"]] = ...,
        label: Union[None, Literal["left", "right"]] = ...,
    ):
        """
        usage.dask: 88
        usage.xarray: 14
        """
        ...

    def reset_index(self, /, drop: bool = ...):
        """
        usage.dask: 7
        """
        ...

    def rmod(self, /, other: Union[int, pandas.core.series.Series], fill_value: int):
        """
        usage.dask: 2
        """
        ...

    def rmul(self, /, other: Union[int, pandas.core.series.Series], fill_value: int):
        """
        usage.dask: 2
        """
        ...

    @overload
    def rolling(self, /, window: int, min_periods: None, center: bool):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def rolling(self, /, window: int, min_periods: int, center: bool):
        """
        usage.xarray: 2
        """
        ...

    @overload
    def rolling(
        self,
        /,
        window: Union[pandas.tseries.offsets.Second, int, Literal["3S", "2S", "1S"]],
        min_periods: None = ...,
        center: bool = ...,
        win_type: None = ...,
        axis: int = ...,
    ):
        """
        usage.dask: 24
        """
        ...

    def rolling(
        self,
        /,
        window: Union[Literal["3S", "2S", "1S"], int, pandas.tseries.offsets.Second],
        min_periods: Union[None, int] = ...,
        center: bool = ...,
        win_type: None = ...,
        axis: int = ...,
    ):
        """
        usage.dask: 24
        usage.xarray: 3
        """
        ...

    def round(self, /, decimals: int = ...):
        """
        usage.dask: 2
        """
        ...

    def rpow(self, /, other: Union[int, pandas.core.series.Series], fill_value: int):
        """
        usage.dask: 2
        """
        ...

    def rsub(self, /, other: Union[int, pandas.core.series.Series], fill_value: int):
        """
        usage.dask: 2
        """
        ...

    def rtruediv(
        self, /, other: Union[int, pandas.core.series.Series], fill_value: int
    ):
        """
        usage.dask: 4
        """
        ...

    def searchsorted(self, /, value: pandas.core.series.Series, side: Literal["right"]):
        """
        usage.dask: 1
        """
        ...

    def sem(
        self,
        /,
        axis: Union[Literal["columns"], int] = ...,
        skipna: Union[bool, None] = ...,
        ddof: int = ...,
    ):
        """
        usage.dask: 9
        """
        ...

    @overload
    def shift(self, /, periods: int):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def shift(self, /, periods: int = ..., freq: object = ...):
        """
        usage.dask: 32
        """
        ...

    def shift(self, /, periods: int = ..., freq: object = ...):
        """
        usage.dask: 32
        usage.xarray: 1
        """
        ...

    def sort_index(self, /, ascending: bool = ...):
        """
        usage.dask: 4
        """
        ...

    def sort_values(self, /, ascending: bool = ...):
        """
        usage.dask: 5
        """
        ...

    def squeeze(self, /):
        """
        usage.dask: 1
        """
        ...

    def std(
        self,
        /,
        axis: Union[Literal["columns"], None, int] = ...,
        skipna: bool = ...,
        ddof: int = ...,
    ):
        """
        usage.dask: 12
        """
        ...

    def sub(self, /, other: Union[int, pandas.core.series.Series], fill_value: int):
        """
        usage.dask: 2
        """
        ...

    @overload
    def sum(self, /, skipna: bool):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def sum(self, /, skipna: bool, min_count: int):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def sum(
        self, /, axis: Union[Literal["columns"], None, int] = ..., skipna: bool = ...
    ):
        """
        usage.dask: 41
        """
        ...

    @overload
    def sum(self, /):
        """
        usage.sklearn: 1
        """
        ...

    def sum(
        self, /, axis: Union[Literal["columns"], None, int] = ..., skipna: bool = ...
    ):
        """
        usage.dask: 41
        usage.sklearn: 1
        usage.xarray: 2
        """
        ...

    def tail(self, /, n: int):
        """
        usage.dask: 4
        """
        ...

    def take(self, /, indices: numpy.ndarray):
        """
        usage.dask: 1
        """
        ...

    def to_dict(self, /):
        """
        usage.dask: 5
        """
        ...

    @overload
    def to_frame(self, /):
        """
        usage.sklearn: 2
        usage.xarray: 2
        """
        ...

    @overload
    def to_frame(
        self, /, name: Union[Literal["a", "A", "__series__", "bar", "s"], None] = ...
    ):
        """
        usage.dask: 29
        """
        ...

    def to_frame(
        self, /, name: Union[Literal["a", "A", "__series__", "bar", "s"], None] = ...
    ):
        """
        usage.dask: 29
        usage.sklearn: 2
        usage.xarray: 2
        """
        ...

    def to_string(self, /, max_rows: int):
        """
        usage.dask: 1
        """
        ...

    def to_timestamp(
        self,
        /,
        freq: Union[Literal["M"], None] = ...,
        how: Literal["s", "start"] = ...,
        copy: int = ...,
    ):
        """
        usage.dask: 4
        """
        ...

    def tolist(self, /):
        """
        usage.dask: 4
        """
        ...

    def truediv(self, /, other: Union[int, pandas.core.series.Series], fill_value: int):
        """
        usage.dask: 6
        """
        ...

    def unique(self, /):
        """
        usage.dask: 9
        """
        ...

    def unstack(self, /):
        """
        usage.xarray: 1
        """
        ...

    def value_counts(
        self, /, ascending: bool = ..., sort: bool = ..., dropna: bool = ...
    ):
        """
        usage.dask: 11
        """
        ...

    @overload
    def var(self, /, skipna: bool, ddof: int):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def var(
        self,
        /,
        axis: Union[Literal["columns"], None, int] = ...,
        skipna: Union[bool, None] = ...,
        ddof: int = ...,
    ):
        """
        usage.dask: 14
        """
        ...

    def var(
        self,
        /,
        axis: Union[Literal["columns"], None, int] = ...,
        skipna: Union[None, bool] = ...,
        ddof: int = ...,
    ):
        """
        usage.dask: 14
        usage.xarray: 1
        """
        ...

    @overload
    def where(self, /, cond: pandas.core.series.Series):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def where(
        self,
        /,
        cond: pandas.core.series.Series,
        axis: int = ...,
        other: Union[pandas.core.series.Series, numpy.float64, float] = ...,
    ):
        """
        usage.dask: 8
        """
        ...

    def where(
        self,
        /,
        cond: pandas.core.series.Series,
        axis: int = ...,
        other: Union[pandas.core.series.Series, numpy.float64, float] = ...,
    ):
        """
        usage.dask: 8
        usage.xarray: 1
        """
        ...
