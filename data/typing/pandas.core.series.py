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

    # usage.dask: 64
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

    # usage.dask: 19
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
    def __add__(self, _0: float, /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __add__(self, _0: dask.dataframe.core.Scalar, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __add__(self, _0: int, /):
        """
        usage.dask: 34
        """
        ...

    @overload
    def __add__(self, _0: pandas.core.series.Series, /):
        """
        usage.dask: 13
        """
        ...

    @overload
    def __add__(self, _0: numpy.ndarray, /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __add__(self, _0: numpy.int64, /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __add__(self, _0: numpy.float64, /):
        """
        usage.dask: 1
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
        usage.pandas: 52
        """
        ...

    @overload
    def __eq__(self, _0: Literal["category"], /):
        """
        usage.dask: 4
        """
        ...

    @overload
    def __eq__(self, _0: pandas.core.series.Series, /):
        """
        usage.dask: 24
        """
        ...

    @overload
    def __eq__(self, _0: Literal["i8"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __eq__(self, _0: int, /):
        """
        usage.dask: 5
        """
        ...

    @overload
    def __eq__(self, _0: Literal["a"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __eq__(self, _0: numpy.int64, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __eq__(self, _0: numpy.float64, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __eq__(self, _0: float, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __eq__(self, _0: Literal["object"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __eq__(self, _0: Type[numpy.float64], /):
        """
        usage.sklearn: 3
        """
        ...

    @overload
    def __eq__(self, _0: List[Type[numpy.float64]], /):
        """
        usage.sklearn: 2
        """
        ...

    @overload
    def __eq__(
        self,
        _0: List[
            Union[pandas.core.dtypes.dtypes.CategoricalDtype, Type[numpy.float64]]
        ],
        /,
    ):
        """
        usage.sklearn: 3
        """
        ...

    @overload
    def __eq__(
        self,
        _0: List[
            Union[Type[numpy.float64], pandas.core.dtypes.dtypes.CategoricalDtype]
        ],
        /,
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __eq__(
        self, _0: List[Union[type, pandas.core.dtypes.dtypes.CategoricalDtype]], /
    ):
        """
        usage.sklearn: 1
        """
        ...

    def __eq__(self, _0: object, /):
        """
        usage.dask: 39
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
    def __floordiv__(self, _0: int, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __floordiv__(self, _0: float, /):
        """
        usage.dask: 2
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
    def __ge__(self, _0: numpy.int64, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __ge__(self, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __ge__(self, _0: Literal["c"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __ge__(self, _0: int, /):
        """
        usage.dask: 5
        """
        ...

    @overload
    def __ge__(self, _0: numpy.float64, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __ge__(self, _0: Literal["Zelda"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __ge__(self, _0: Literal["d"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __ge__(self, _0: Literal["B"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __ge__(self, _0: Literal["3"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __ge__(self, _0: None, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __ge__(self, _0: pandas._libs.tslibs.nattype.NaTType, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __ge__(self, _0: Literal["2"], /):
        """
        usage.dask: 1
        """
        ...

    def __ge__(self, _0: object, /):
        """
        usage.dask: 16
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
        usage.dask: 16
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
    def __getitem__(self, _0: Literal["amount"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["name"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["id"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["aa"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["bb"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: pandas.core.series.Series, /):
        """
        usage.dask: 6
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["Edith"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["-500"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["A"], /):
        """
        usage.dask: 4
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["B"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["numbers"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["names"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["more_numbers"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["integers"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["dates"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["Date"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["Close"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["a"], /):
        """
        usage.dask: 3
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["b"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["c-d"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["x"], /):
        """
        usage.dask: 3
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["y"], /):
        """
        usage.dask: 4
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[int, int, int]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["25%"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["50%"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["75%"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: pandas.core.indexes.base.Index, /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["z"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["d"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["e"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: numpy.ndarray, /):
        """
        usage.dask: 1
        """
        ...

    def __getitem__(self, _0: object, /):
        """
        usage.dask: 72
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
    def __gt__(self, _0: int, /):
        """
        usage.dask: 55
        """
        ...

    @overload
    def __gt__(self, _0: pandas.core.frame.DataFrame, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __gt__(self, _0: pandas.core.series.Series, /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __gt__(self, _0: numpy.float64, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __gt__(self, _0: numpy.int64, /):
        """
        usage.dask: 2
        """
        ...

    def __gt__(self, _0: object, /):
        """
        usage.dask: 61
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
    def __le__(self, _0: int, /):
        """
        usage.dask: 3
        """
        ...

    @overload
    def __le__(self, _0: float, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __le__(self, _0: numpy.int64, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __le__(self, _0: numpy.float64, /):
        """
        usage.dask: 1
        """
        ...

    def __le__(
        self, _0: Union[numpy.int64, int, float, numpy.float64, numpy.ndarray], /
    ):
        """
        usage.dask: 6
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
    def __lt__(self, _0: pandas.core.series.Series, /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __lt__(self, _0: pandas.core.frame.DataFrame, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __lt__(self, _0: numpy.float64, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __lt__(self, _0: int, /):
        """
        usage.dask: 9
        """
        ...

    @overload
    def __lt__(self, _0: float, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __lt__(self, _0: pandas._libs.tslibs.timedeltas.Timedelta, /):
        """
        usage.dask: 2
        """
        ...

    def __lt__(self, _0: object, /):
        """
        usage.dask: 16
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
    def __mul__(self, _0: float, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __mul__(self, _0: int, /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __mul__(self, _0: pandas.core.series.Series, /):
        """
        usage.dask: 3
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
    def __pow__(self, _0: float, /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __pow__(self, _0: int, /):
        """
        usage.dask: 3
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
    def __radd__(self, _0: dask.dataframe.core.Scalar, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __radd__(self, _0: pandas.core.series.Series, /):
        """
        usage.dask: 13
        """
        ...

    @overload
    def __radd__(self, _0: int, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __radd__(self, _0: numpy.ndarray, /):
        """
        usage.dask: 2
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
    def __rmul__(self, _0: float, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __rmul__(self, _0: int, /):
        """
        usage.sklearn: 1
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
    def __rsub__(self, _0: pandas.core.frame.DataFrame, /):
        """
        usage.dask: 5
        """
        ...

    @overload
    def __rsub__(self, _0: pandas.core.series.Series, /):
        """
        usage.dask: 5
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
    def __setitem__(self, _0: pandas.core.series.Series, _1: int, /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __setitem__(self, _0: pandas.core.series.Series, _1: float, /):
        """
        usage.dask: 1
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
    def __sub__(self, _0: int, /):
        """
        usage.dask: 4
        """
        ...

    @overload
    def __sub__(self, _0: numpy.float64, /):
        """
        usage.dask: 9
        """
        ...

    @overload
    def __sub__(self, _0: pandas.core.series.Series, /):
        """
        usage.dask: 5
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
    def __truediv__(self, _0: float, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __truediv__(self, _0: pandas.core.series.Series, /):
        """
        usage.dask: 8
        """
        ...

    @overload
    def __truediv__(self, _0: int, /):
        """
        usage.dask: 1
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

    @overload
    def add(self, /, other: pandas.core.series.Series, fill_value: int):
        """
        usage.dask: 4
        """
        ...

    @overload
    def add(self, /, other: int, fill_value: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def add(self, /, other: pandas.core.series.Series):
        """
        usage.dask: 1
        """
        ...

    @overload
    def add(self, /, other: pandas.core.series.Series, fill_value: None):
        """
        usage.dask: 1
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

    @overload
    def align(
        self,
        /,
        other: pandas.core.series.Series,
        join: Literal["inner"],
        axis: None,
        fill_value: None,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def align(self, /, other: pandas.core.series.Series, join: Literal["inner"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def align(
        self,
        /,
        other: pandas.core.series.Series,
        join: Literal["inner"],
        axis: None,
        fill_value: int,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def align(
        self,
        /,
        other: pandas.core.series.Series,
        join: Literal["inner"],
        fill_value: int,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def align(
        self,
        /,
        other: pandas.core.series.Series,
        join: Literal["outer"],
        axis: None,
        fill_value: None,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def align(self, /, other: pandas.core.series.Series, join: Literal["outer"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def align(
        self,
        /,
        other: pandas.core.series.Series,
        join: Literal["outer"],
        axis: None,
        fill_value: int,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def align(
        self,
        /,
        other: pandas.core.series.Series,
        join: Literal["outer"],
        fill_value: int,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def align(
        self,
        /,
        other: pandas.core.series.Series,
        join: Literal["left"],
        axis: None,
        fill_value: None,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def align(self, /, other: pandas.core.series.Series, join: Literal["left"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def align(
        self,
        /,
        other: pandas.core.series.Series,
        join: Literal["left"],
        axis: None,
        fill_value: int,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def align(
        self,
        /,
        other: pandas.core.series.Series,
        join: Literal["left"],
        fill_value: int,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def align(
        self,
        /,
        other: pandas.core.series.Series,
        join: Literal["right"],
        axis: None,
        fill_value: None,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def align(self, /, other: pandas.core.series.Series, join: Literal["right"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def align(
        self,
        /,
        other: pandas.core.series.Series,
        join: Literal["right"],
        axis: None,
        fill_value: int,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def align(
        self,
        /,
        other: pandas.core.series.Series,
        join: Literal["right"],
        fill_value: int,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def align(
        self,
        /,
        other: pandas.core.series.Series,
        join: Literal["inner"],
        axis: int,
        fill_value: None,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def align(
        self,
        /,
        other: pandas.core.series.Series,
        join: Literal["outer"],
        axis: int,
        fill_value: None,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def align(
        self,
        /,
        other: pandas.core.series.Series,
        join: Literal["left"],
        axis: int,
        fill_value: None,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def align(
        self,
        /,
        other: pandas.core.series.Series,
        join: Literal["right"],
        axis: int,
        fill_value: None,
    ):
        """
        usage.dask: 1
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

    @overload
    def all(self, /):
        """
        usage.dask: 20
        """
        ...

    @overload
    def all(self, /, axis: int, skipna: bool):
        """
        usage.dask: 2
        """
        ...

    def all(self, /, axis: int = ..., skipna: bool = ...):
        """
        usage.dask: 22
        """
        ...

    @overload
    def any(self, /):
        """
        usage.dask: 6
        usage.sklearn: 2
        usage.xarray: 1
        """
        ...

    @overload
    def any(self, /, axis: int, skipna: bool):
        """
        usage.dask: 2
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
    def apply(self, /, func: Callable):
        """
        usage.dask: 6
        """
        ...

    @overload
    def apply(self, /, func: Callable, convert_dtype: bool, args: Tuple[None, ...]):
        """
        usage.dask: 3
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
        usage.dask: 3
        usage.xarray: 1
        """
        ...

    @overload
    def astype(self, /, dtype: Literal["float"]):
        """
        usage.dask: 2
        usage.sklearn: 1
        """
        ...

    @overload
    def astype(self, /, dtype: numpy.dtype):
        """
        usage.dask: 6
        """
        ...

    @overload
    def astype(self, /, dtype: Type[float]):
        """
        usage.dask: 5
        """
        ...

    @overload
    def astype(self, /, dtype: Literal["datetime64[ns]"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def astype(self, /, dtype: Literal["f8"]):
        """
        usage.dask: 5
        """
        ...

    @overload
    def astype(self, /, dtype: Literal["int64"]):
        """
        usage.dask: 2
        """
        ...

    @overload
    def astype(self, /, dtype: pandas.core.dtypes.dtypes.CategoricalDtype):
        """
        usage.dask: 2
        """
        ...

    @overload
    def astype(self, /, dtype: Literal["category"]):
        """
        usage.dask: 17
        usage.sklearn: 2
        """
        ...

    @overload
    def astype(self, /, dtype: Literal["i8"]):
        """
        usage.dask: 3
        """
        ...

    @overload
    def astype(self, /, dtype: Literal["float32"]):
        """
        usage.dask: 3
        """
        ...

    @overload
    def astype(self, /, dtype: Type[str]):
        """
        usage.dask: 3
        """
        ...

    @overload
    def astype(self, /, dtype: Type[numpy.int32]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def astype(self, /, dtype: Type[numpy.float64], copy: bool):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def astype(self, /, dtype: pandas.core.dtypes.dtypes.CategoricalDtype, copy: bool):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def astype(self, /, dtype: Type[object], copy: bool):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def astype(self, /, dtype: Literal["int"]):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def astype(self, /, dtype: Type[numpy.float16]):
        """
        usage.sklearn: 2
        """
        ...

    @overload
    def astype(self, /, dtype: Type[numpy.int16]):
        """
        usage.sklearn: 1
        """
        ...

    def astype(
        self,
        /,
        dtype: Union[
            pandas.core.dtypes.dtypes.CategoricalDtype,
            numpy.dtype,
            str,
            type,
            Type[int],
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

    @overload
    def between(self, /, left: int, right: int, inclusive: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def between(self, /, left: int, right: int):
        """
        usage.dask: 1
        """
        ...

    def between(self, /, left: int, right: int, inclusive: bool = ...):
        """
        usage.dask: 2
        """
        ...

    @overload
    def clip(self, /, lower: int, upper: int):
        """
        usage.dask: 3
        """
        ...

    @overload
    def clip(self, /, lower: int, upper: None):
        """
        usage.dask: 1
        """
        ...

    @overload
    def clip(self, /, lower: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def clip(self, /, lower: None, upper: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def clip(self, /, upper: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def clip(self, /, lower: float, upper: float):
        """
        usage.dask: 2
        """
        ...

    @overload
    def clip(self, /, lower: float, upper: None):
        """
        usage.dask: 1
        """
        ...

    @overload
    def clip(self, /, lower: float):
        """
        usage.dask: 1
        """
        ...

    @overload
    def clip(self, /, lower: None, upper: float):
        """
        usage.dask: 1
        """
        ...

    @overload
    def clip(self, /, upper: float):
        """
        usage.dask: 1
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

    @overload
    def combine(
        self, /, other: pandas.core.series.Series, func: Callable, fill_value: None
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def combine(
        self, /, other: pandas.core.series.Series, func: Callable, fill_value: int
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def combine(
        self, /, other: pandas.core.series.Series, func: Callable, fill_value: None
    ):
        """
        usage.dask: 2
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

    @overload
    def count(self, /):
        """
        usage.dask: 8
        """
        ...

    @overload
    def count(self, /, *, axis: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def count(self, /, *, axis: Literal["columns"]):
        """
        usage.dask: 1
        """
        ...

    def count(self, /, *, axis: Union[Literal["columns"], int] = ...):
        """
        usage.dask: 10
        """
        ...

    @overload
    def cov(self, /, other: pandas.core.series.Series):
        """
        usage.dask: 1
        """
        ...

    @overload
    def cov(self, /, other: pandas.core.series.Series, min_periods: int):
        """
        usage.dask: 1
        """
        ...

    def cov(self, /, other: pandas.core.series.Series, min_periods: int = ...):
        """
        usage.dask: 2
        """
        ...

    @overload
    def cummax(self, /):
        """
        usage.dask: 3
        """
        ...

    @overload
    def cummax(self, /, axis: None, skipna: bool):
        """
        usage.dask: 1
        """
        ...

    def cummax(self, /, axis: None = ..., skipna: bool = ...):
        """
        usage.dask: 4
        """
        ...

    @overload
    def cummin(self, /):
        """
        usage.dask: 3
        """
        ...

    @overload
    def cummin(self, /, axis: None, skipna: bool):
        """
        usage.dask: 1
        """
        ...

    def cummin(self, /, axis: None = ..., skipna: bool = ...):
        """
        usage.dask: 4
        """
        ...

    @overload
    def cumprod(self, /):
        """
        usage.dask: 3
        """
        ...

    @overload
    def cumprod(self, /, axis: None, skipna: bool):
        """
        usage.dask: 1
        """
        ...

    def cumprod(self, /, axis: None = ..., skipna: bool = ...):
        """
        usage.dask: 4
        """
        ...

    @overload
    def cumsum(self, /):
        """
        usage.dask: 4
        """
        ...

    @overload
    def cumsum(self, /, axis: None, skipna: bool):
        """
        usage.dask: 1
        """
        ...

    def cumsum(self, /, axis: None = ..., skipna: bool = ...):
        """
        usage.dask: 5
        """
        ...

    @overload
    def describe(self, /):
        """
        usage.dask: 4
        """
        ...

    @overload
    def describe(self, /, include: List[Literal["number"]], exclude: None):
        """
        usage.dask: 1
        """
        ...

    @overload
    def describe(self, /, include: List[Type[numpy.timedelta64]], exclude: None):
        """
        usage.dask: 1
        """
        ...

    @overload
    def describe(self, /, include: List[Literal["object", "number"]], exclude: None):
        """
        usage.dask: 1
        """
        ...

    def describe(
        self,
        /,
        include: List[
            Union[Type[numpy.timedelta64], Literal["number", "object"]]
        ] = ...,
        exclude: None = ...,
    ):
        """
        usage.dask: 7
        """
        ...

    @overload
    def diff(self, /, periods: int):
        """
        usage.dask: 4
        """
        ...

    @overload
    def diff(self, /):
        """
        usage.dask: 3
        """
        ...

    def diff(self, /, periods: int = ...):
        """
        usage.dask: 7
        """
        ...

    @overload
    def drop_duplicates(self, /):
        """
        usage.dask: 6
        """
        ...

    @overload
    def drop_duplicates(self, /, keep: Literal["first"]):
        """
        usage.dask: 3
        """
        ...

    @overload
    def drop_duplicates(self, /, keep: Literal["last"]):
        """
        usage.dask: 3
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

    @overload
    def fillna(self, /, value: int, method: None, axis: int, limit: None):
        """
        usage.dask: 2
        """
        ...

    @overload
    def fillna(self, /, value: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def fillna(self, /, value: numpy.float64, method: None, axis: int, limit: None):
        """
        usage.dask: 2
        """
        ...

    @overload
    def fillna(self, /, value: numpy.float64):
        """
        usage.dask: 1
        """
        ...

    @overload
    def fillna(self, /, value: None, method: Literal["pad"], axis: int, limit: None):
        """
        usage.dask: 1
        """
        ...

    @overload
    def fillna(self, /, method: Literal["pad"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def fillna(self, /, method: Literal["ffill"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def fillna(self, /, method: Literal["ffill"], limit: None):
        """
        usage.dask: 1
        """
        ...

    @overload
    def fillna(self, /, value: None, method: Literal["bfill"], axis: int, limit: None):
        """
        usage.dask: 1
        """
        ...

    @overload
    def fillna(self, /, method: Literal["bfill"]):
        """
        usage.dask: 2
        """
        ...

    @overload
    def fillna(self, /, method: Literal["bfill"], limit: None):
        """
        usage.dask: 1
        """
        ...

    @overload
    def fillna(self, /, value: None, method: Literal["pad"], axis: int, limit: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def fillna(self, /, method: Literal["pad"], limit: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def fillna(self, /, method: Literal["ffill"], limit: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def fillna(self, /, value: None, method: Literal["bfill"], axis: int, limit: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def fillna(self, /, method: Literal["bfill"], limit: int):
        """
        usage.dask: 2
        """
        ...

    @overload
    def fillna(self, /, value: pandas.core.series.Series):
        """
        usage.dask: 2
        """
        ...

    @overload
    def fillna(
        self, /, value: pandas.core.series.Series, method: None, axis: int, limit: None
    ):
        """
        usage.dask: 1
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

    @overload
    def first(self, /, offset: Literal["0d"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def first(self, /, offset: Literal["100h"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def first(self, /, offset: Literal["20d"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def first(self, /, offset: Literal["20B"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def first(self, /, offset: Literal["3W"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def first(self, /, offset: Literal["3M"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def first(self, /, offset: Literal["400d"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def first(self, /, offset: Literal["13M"]):
        """
        usage.dask: 1
        """
        ...

    def first(self, /, offset: str):
        """
        usage.dask: 8
        """
        ...

    @overload
    def floordiv(self, /, other: pandas.core.series.Series, fill_value: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def floordiv(self, /, other: int, fill_value: int):
        """
        usage.dask: 1
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
    def groupby(self, /, level: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def groupby(self, /, by: pandas.core.series.Series, group_keys: bool):
        """
        usage.dask: 4
        """
        ...

    @overload
    def groupby(self, /, by: pandas.core.series.Series):
        """
        usage.dask: 20
        """
        ...

    @overload
    def groupby(self, /, by: List[pandas.core.series.Series]):
        """
        usage.dask: 6
        """
        ...

    @overload
    def groupby(self, /, level: int, sort: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def groupby(self, /, level: int, dropna: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def groupby(self, /, by: Callable):
        """
        usage.dask: 2
        """
        ...

    @overload
    def groupby(self, /, by: Callable, group_keys: bool):
        """
        usage.dask: 2
        """
        ...

    @overload
    def groupby(self, /, by: List[Callable]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def groupby(self, /, by: pandas.core.indexes.base.Index, group_keys: bool):
        """
        usage.dask: 2
        """
        ...

    @overload
    def groupby(self, /, by: List[pandas.core.indexes.base.Index]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def groupby(self, /, by: Literal["a"]):
        """
        usage.dask: 2
        """
        ...

    @overload
    def groupby(self, /, by: Literal["a"], group_keys: bool):
        """
        usage.dask: 3
        """
        ...

    @overload
    def groupby(self, /, by: pandas.core.indexes.numeric.Int64Index, group_keys: bool):
        """
        usage.dask: 2
        """
        ...

    @overload
    def groupby(self, /, by: pandas.core.indexes.numeric.Int64Index):
        """
        usage.dask: 2
        """
        ...

    @overload
    def groupby(self, /, level: List[int], sort: bool):
        """
        usage.dask: 2
        """
        ...

    @overload
    def groupby(self, /, by: list):
        """
        usage.dask: 2
        """
        ...

    @overload
    def groupby(self, /, by: Literal["x"]):
        """
        usage.dask: 2
        """
        ...

    @overload
    def groupby(self, /, by: pandas.core.groupby.ops.BaseGrouper):
        """
        usage.dask: 1
        """
        ...

    @overload
    def groupby(self, /, by: List[pandas.core.series.Series], group_keys: bool):
        """
        usage.dask: 4
        """
        ...

    @overload
    def groupby(self, /, by: Literal["foo"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["foo"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def groupby(self, /, by: dask.dataframe.core.DataFrame):
        """
        usage.dask: 1
        """
        ...

    @overload
    def groupby(self, /, by: List[dask.dataframe.core.DataFrame]):
        """
        usage.dask: 1
        """
        ...

    def groupby(
        self,
        /,
        level: Union[List[int], int] = ...,
        dropna: bool = ...,
        sort: bool = ...,
        by: object = ...,
        group_keys: bool = ...,
    ):
        """
        usage.dask: 65
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

    @overload
    def idxmax(self, /, skipna: bool):
        """
        usage.dask: 4
        """
        ...

    @overload
    def idxmax(self, /, axis: int, skipna: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def idxmax(self, /, axis: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def idxmax(self, /):
        """
        usage.dask: 2
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

    @overload
    def isin(self, /, values: List[int]):
        """
        usage.dask: 3
        """
        ...

    @overload
    def isin(self, /, values: pandas.core.series.Series):
        """
        usage.dask: 3
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

    @overload
    def last(self, /, offset: Literal["0d"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def last(self, /, offset: Literal["100h"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def last(self, /, offset: Literal["20d"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def last(self, /, offset: Literal["20B"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def last(self, /, offset: Literal["3W"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def last(self, /, offset: Literal["3M"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def last(self, /, offset: Literal["400d"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def last(self, /, offset: Literal["13M"]):
        """
        usage.dask: 1
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

    @overload
    def map(self, /, arg: Callable, na_action: None):
        """
        usage.dask: 3
        """
        ...

    @overload
    def map(self, /, arg: Callable):
        """
        usage.dask: 2
        """
        ...

    @overload
    def map(self, /, arg: Dict[numpy.int64, numpy.int64], na_action: None):
        """
        usage.dask: 1
        """
        ...

    @overload
    def map(self, /, arg: Dict[numpy.int64, numpy.int64]):
        """
        usage.dask: 2
        """
        ...

    @overload
    def map(self, /, arg: pandas.core.series.Series, na_action: None):
        """
        usage.dask: 1
        """
        ...

    @overload
    def map(self, /, arg: pandas.core.series.Series):
        """
        usage.dask: 7
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

    @overload
    def mask(self, /, cond: pandas.core.series.Series, other: float):
        """
        usage.dask: 1
        """
        ...

    @overload
    def mask(self, /, cond: pandas.core.series.Series):
        """
        usage.dask: 1
        """
        ...

    @overload
    def mask(
        self, /, cond: pandas.core.series.Series, other: pandas.core.series.Series
    ):
        """
        usage.dask: 2
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
        usage.dask: 4
        usage.xarray: 1
        """
        ...

    @overload
    def max(self, /, axis: int, skipna: bool):
        """
        usage.dask: 2
        """
        ...

    @overload
    def max(self, /):
        """
        usage.dask: 11
        """
        ...

    @overload
    def max(self, /, axis: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def max(self, /, axis: Literal["columns"]):
        """
        usage.dask: 1
        """
        ...

    def max(self, /, axis: Union[Literal["columns"], int] = ..., skipna: bool = ...):
        """
        usage.dask: 19
        usage.xarray: 1
        """
        ...

    @overload
    def mean(self, /, skipna: bool):
        """
        usage.dask: 2
        usage.xarray: 1
        """
        ...

    @overload
    def mean(self, /, axis: int, skipna: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def mean(self, /):
        """
        usage.dask: 17
        """
        ...

    @overload
    def mean(self, /, axis: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def mean(self, /, axis: Literal["columns"]):
        """
        usage.dask: 1
        """
        ...

    def mean(self, /, axis: Union[Literal["columns"], int] = ..., skipna: bool = ...):
        """
        usage.dask: 22
        usage.xarray: 1
        """
        ...

    def median(self, /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def memory_usage(self, /, index: bool):
        """
        usage.dask: 2
        """
        ...

    @overload
    def memory_usage(self, /, index: bool, deep: bool):
        """
        usage.dask: 4
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
        usage.dask: 3
        usage.xarray: 1
        """
        ...

    @overload
    def min(self, /, axis: int, skipna: bool):
        """
        usage.dask: 2
        """
        ...

    @overload
    def min(self, /):
        """
        usage.dask: 7
        """
        ...

    @overload
    def min(self, /, axis: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def min(self, /, axis: Literal["columns"]):
        """
        usage.dask: 1
        """
        ...

    def min(self, /, axis: Union[Literal["columns"], int] = ..., skipna: bool = ...):
        """
        usage.dask: 14
        usage.xarray: 1
        """
        ...

    @overload
    def mod(self, /, other: pandas.core.series.Series, fill_value: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def mod(self, /, other: int, fill_value: int):
        """
        usage.dask: 1
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

    @overload
    def mul(self, /, other: pandas.core.series.Series, fill_value: int):
        """
        usage.dask: 2
        """
        ...

    @overload
    def mul(self, /, other: int, fill_value: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def mul(self, /, other: pandas.core.series.Series):
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

    @overload
    def pow(self, /, other: pandas.core.series.Series, fill_value: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def pow(self, /, other: int, fill_value: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def pow(self, /, other: int):
        """
        usage.dask: 1
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
    def prod(self, /, axis: int, skipna: bool):
        """
        usage.dask: 2
        """
        ...

    @overload
    def prod(self, /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def prod(self, /, skipna: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def prod(self, /, axis: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def prod(self, /, axis: Literal["columns"]):
        """
        usage.dask: 1
        """
        ...

    def prod(
        self,
        /,
        axis: Union[Literal["columns"], int] = ...,
        skipna: bool = ...,
        min_count: int = ...,
    ):
        """
        usage.dask: 7
        usage.xarray: 1
        """
        ...

    @overload
    def quantile(self, /, q: numpy.ndarray):
        """
        usage.dask: 2
        """
        ...

    @overload
    def quantile(self, /, q: List[float]):
        """
        usage.dask: 2
        """
        ...

    @overload
    def quantile(self, /, q: float):
        """
        usage.dask: 1
        """
        ...

    @overload
    def quantile(self, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def quantile(self, /, q: list):
        """
        usage.dask: 1
        """
        ...

    def quantile(self, /, q: Union[List[float], numpy.ndarray, float] = ...):
        """
        usage.dask: 7
        """
        ...

    @overload
    def radd(self, /, other: pandas.core.series.Series, fill_value: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def radd(self, /, other: int, fill_value: int):
        """
        usage.dask: 1
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

    @overload
    def reindex(self, /, index: pandas.core.indexes.numeric.Int64Index):
        """
        usage.dask: 3
        """
        ...

    @overload
    def reindex(self, /, index: pandas.core.indexes.multi.MultiIndex):
        """
        usage.dask: 3
        """
        ...

    @overload
    def reindex(self, /, index: numpy.ndarray):
        """
        usage.dask: 1
        """
        ...

    @overload
    def reindex(self, /, index: pandas.core.indexes.datetimes.DatetimeIndex):
        """
        usage.dask: 1
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

    @overload
    def rename(self, /, index: Literal["idx"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rename(self, /, index: Literal["renamed"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rename(self, /, index: Literal["y"]):
        """
        usage.dask: 2
        """
        ...

    @overload
    def rename(self, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rename(self, /, index: None):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rename(self, /, index: Literal["z"], *, inplace: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rename(self, /, index: Literal["z"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rename(self, /, index: Callable):
        """
        usage.dask: 5
        """
        ...

    @overload
    def rename(self, /, index: pandas.core.series.Series):
        """
        usage.dask: 4
        """
        ...

    @overload
    def rename(self, /, index: Callable, *, inplace: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rename(self, /, index: Literal["A"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rename(self, /, index: Literal["Name"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rename(self, /, index: Literal["Num"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rename(self, /, index: Literal["a"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rename(self, /, index: Literal["b"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rename(self, /, index: Literal["B"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rename(self, /, index: Literal["AA"]):
        """
        usage.dask: 1
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

    @overload
    def replace(self, /, to_replace: Literal["c"], value: float):
        """
        usage.dask: 1
        """
        ...

    @overload
    def replace(self, /, to_replace: int, value: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def replace(self, /, to_replace: int, value: int, regex: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def replace(self, /, to_replace: Dict[int, int]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def replace(self, /, to_replace: Dict[int, int], value: None, regex: bool):
        """
        usage.dask: 1
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
        rule: pandas._libs.tslibs.offsets.Minute,
        closed: Literal["right"],
        label: Literal["left"],
    ):
        """
        usage.dask: 3
        """
        ...

    @overload
    def resample(
        self,
        /,
        rule: pandas._libs.tslibs.offsets.Minute,
        closed: Literal["right"],
        label: Literal["right"],
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def resample(
        self, /, rule: Literal["30T"], closed: Literal["right"], label: Literal["right"]
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def resample(
        self, /, rule: Literal["30T"], closed: Literal["right"], label: Literal["left"]
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def resample(
        self,
        /,
        rule: pandas._libs.tslibs.offsets.Minute,
        closed: Literal["left"],
        label: Literal["left"],
    ):
        """
        usage.dask: 3
        """
        ...

    @overload
    def resample(
        self,
        /,
        rule: pandas._libs.tslibs.offsets.Minute,
        closed: Literal["left"],
        label: Literal["right"],
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def resample(
        self, /, rule: Literal["30T"], closed: Literal["left"], label: Literal["right"]
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def resample(
        self, /, rule: Literal["30T"], closed: Literal["left"], label: Literal["left"]
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def resample(
        self,
        /,
        rule: pandas._libs.tslibs.offsets.Hour,
        closed: Literal["right"],
        label: Literal["left"],
    ):
        """
        usage.dask: 3
        """
        ...

    @overload
    def resample(
        self,
        /,
        rule: pandas._libs.tslibs.offsets.Hour,
        closed: Literal["right"],
        label: Literal["right"],
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def resample(
        self, /, rule: Literal["h"], closed: Literal["right"], label: Literal["right"]
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def resample(
        self, /, rule: Literal["h"], closed: Literal["right"], label: Literal["left"]
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def resample(
        self,
        /,
        rule: pandas._libs.tslibs.offsets.Hour,
        closed: Literal["left"],
        label: Literal["left"],
    ):
        """
        usage.dask: 3
        """
        ...

    @overload
    def resample(
        self,
        /,
        rule: pandas._libs.tslibs.offsets.Hour,
        closed: Literal["left"],
        label: Literal["right"],
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def resample(
        self, /, rule: Literal["h"], closed: Literal["left"], label: Literal["right"]
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def resample(
        self, /, rule: Literal["h"], closed: Literal["left"], label: Literal["left"]
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def resample(
        self,
        /,
        rule: pandas._libs.tslibs.offsets.Day,
        closed: Literal["right"],
        label: Literal["left"],
    ):
        """
        usage.dask: 3
        """
        ...

    @overload
    def resample(
        self,
        /,
        rule: pandas._libs.tslibs.offsets.Day,
        closed: Literal["right"],
        label: Literal["right"],
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def resample(
        self, /, rule: Literal["d"], closed: Literal["right"], label: Literal["right"]
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def resample(
        self, /, rule: Literal["d"], closed: Literal["right"], label: Literal["left"]
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def resample(
        self,
        /,
        rule: pandas._libs.tslibs.offsets.Day,
        closed: Literal["left"],
        label: Literal["left"],
    ):
        """
        usage.dask: 3
        """
        ...

    @overload
    def resample(
        self,
        /,
        rule: pandas._libs.tslibs.offsets.Day,
        closed: Literal["left"],
        label: Literal["right"],
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def resample(
        self, /, rule: Literal["d"], closed: Literal["left"], label: Literal["right"]
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def resample(
        self, /, rule: Literal["d"], closed: Literal["left"], label: Literal["left"]
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def resample(
        self,
        /,
        rule: pandas._libs.tslibs.offsets.Week,
        closed: Literal["right"],
        label: Literal["left"],
    ):
        """
        usage.dask: 3
        """
        ...

    @overload
    def resample(
        self,
        /,
        rule: pandas._libs.tslibs.offsets.Week,
        closed: Literal["right"],
        label: Literal["right"],
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def resample(
        self, /, rule: Literal["w"], closed: Literal["right"], label: Literal["right"]
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def resample(
        self, /, rule: Literal["w"], closed: Literal["right"], label: Literal["left"]
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def resample(
        self,
        /,
        rule: pandas._libs.tslibs.offsets.Week,
        closed: Literal["left"],
        label: Literal["left"],
    ):
        """
        usage.dask: 3
        """
        ...

    @overload
    def resample(
        self,
        /,
        rule: pandas._libs.tslibs.offsets.Week,
        closed: Literal["left"],
        label: Literal["right"],
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def resample(
        self, /, rule: Literal["w"], closed: Literal["left"], label: Literal["right"]
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def resample(
        self, /, rule: Literal["w"], closed: Literal["left"], label: Literal["left"]
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def resample(
        self,
        /,
        rule: pandas._libs.tslibs.offsets.MonthEnd,
        closed: Literal["right"],
        label: Literal["left"],
    ):
        """
        usage.dask: 3
        """
        ...

    @overload
    def resample(
        self,
        /,
        rule: pandas._libs.tslibs.offsets.MonthEnd,
        closed: Literal["right"],
        label: Literal["right"],
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def resample(
        self, /, rule: Literal["M"], closed: Literal["right"], label: Literal["right"]
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def resample(
        self, /, rule: Literal["M"], closed: Literal["right"], label: Literal["left"]
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def resample(
        self,
        /,
        rule: pandas._libs.tslibs.offsets.MonthEnd,
        closed: Literal["left"],
        label: Literal["left"],
    ):
        """
        usage.dask: 3
        """
        ...

    @overload
    def resample(
        self,
        /,
        rule: pandas._libs.tslibs.offsets.MonthEnd,
        closed: Literal["left"],
        label: Literal["right"],
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def resample(
        self, /, rule: Literal["M"], closed: Literal["left"], label: Literal["right"]
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def resample(
        self, /, rule: Literal["M"], closed: Literal["left"], label: Literal["left"]
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def resample(
        self,
        /,
        rule: pandas._libs.tslibs.offsets.Minute,
        closed: None,
        label: Literal["left"],
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def resample(
        self, /, rule: pandas._libs.tslibs.offsets.Minute, closed: None, label: None
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def resample(self, /, rule: Literal["30min"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def resample(self, /, rule: Literal["10min"]):
        """
        usage.dask: 2
        """
        ...

    @overload
    def resample(
        self,
        /,
        rule: pandas._libs.tslibs.offsets.Hour,
        closed: None,
        label: Literal["left"],
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def resample(
        self, /, rule: pandas._libs.tslibs.offsets.Hour, closed: None, label: None
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def resample(self, /, rule: Literal["2h"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def resample(
        self,
        /,
        rule: pandas._libs.tslibs.offsets.MonthEnd,
        closed: None,
        label: Literal["left"],
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def resample(
        self, /, rule: pandas._libs.tslibs.offsets.MonthEnd, closed: None, label: None
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def resample(
        self,
        /,
        rule: pandas._libs.tslibs.offsets.QuarterEnd,
        closed: None,
        label: Literal["left"],
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def resample(
        self,
        /,
        rule: pandas._libs.tslibs.offsets.Day,
        closed: None,
        label: Literal["left"],
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def resample(self, /, rule: Literal["57T"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def resample(self, /, rule: Literal["1d"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def resample(
        self, /, rule: pandas._libs.tslibs.offsets.Day, closed: None, label: None
    ):
        """
        usage.dask: 2
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

    @overload
    def reset_index(self, /, drop: bool):
        """
        usage.dask: 6
        """
        ...

    @overload
    def reset_index(self, /):
        """
        usage.dask: 1
        """
        ...

    def reset_index(self, /, drop: bool = ...):
        """
        usage.dask: 7
        """
        ...

    @overload
    def rmod(self, /, other: pandas.core.series.Series, fill_value: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rmod(self, /, other: int, fill_value: int):
        """
        usage.dask: 1
        """
        ...

    def rmod(self, /, other: Union[int, pandas.core.series.Series], fill_value: int):
        """
        usage.dask: 2
        """
        ...

    @overload
    def rmul(self, /, other: pandas.core.series.Series, fill_value: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rmul(self, /, other: int, fill_value: int):
        """
        usage.dask: 1
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
    def rolling(self, /, window: int, center: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rolling(
        self, /, window: int, min_periods: None, center: bool, win_type: None, axis: int
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def rolling(self, /, window: int, axis: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rolling(self, /, window: int):
        """
        usage.dask: 2
        """
        ...

    @overload
    def rolling(self, /, window: Literal["1S"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rolling(
        self,
        /,
        window: Literal["1S"],
        min_periods: None,
        center: bool,
        win_type: None,
        axis: int,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def rolling(self, /, window: Literal["2S"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rolling(
        self,
        /,
        window: Literal["2S"],
        min_periods: None,
        center: bool,
        win_type: None,
        axis: int,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def rolling(self, /, window: Literal["3S"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rolling(
        self,
        /,
        window: Literal["3S"],
        min_periods: None,
        center: bool,
        win_type: None,
        axis: int,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def rolling(self, /, window: pandas._libs.tslibs.offsets.Second):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rolling(
        self,
        /,
        window: pandas._libs.tslibs.offsets.Second,
        min_periods: None,
        center: bool,
        win_type: None,
        axis: int,
    ):
        """
        usage.dask: 2
        """
        ...

    def rolling(
        self,
        /,
        window: Union[
            Literal["3S", "2S", "1S"], int, pandas._libs.tslibs.offsets.Second
        ],
        min_periods: Union[None, int] = ...,
        center: bool = ...,
        win_type: None = ...,
        axis: int = ...,
    ):
        """
        usage.dask: 18
        usage.xarray: 3
        """
        ...

    @overload
    def round(self, /, decimals: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def round(self, /):
        """
        usage.dask: 1
        """
        ...

    def round(self, /, decimals: int = ...):
        """
        usage.dask: 2
        """
        ...

    @overload
    def rpow(self, /, other: pandas.core.series.Series, fill_value: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rpow(self, /, other: int, fill_value: int):
        """
        usage.dask: 1
        """
        ...

    def rpow(self, /, other: Union[int, pandas.core.series.Series], fill_value: int):
        """
        usage.dask: 2
        """
        ...

    @overload
    def rsub(self, /, other: pandas.core.series.Series, fill_value: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rsub(self, /, other: int, fill_value: int):
        """
        usage.dask: 1
        """
        ...

    def rsub(self, /, other: Union[int, pandas.core.series.Series], fill_value: int):
        """
        usage.dask: 2
        """
        ...

    @overload
    def rtruediv(self, /, other: pandas.core.series.Series, fill_value: int):
        """
        usage.dask: 2
        """
        ...

    @overload
    def rtruediv(self, /, other: int, fill_value: int):
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

    @overload
    def sem(self, /, axis: int, skipna: None, ddof: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sem(self, /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def sem(self, /, ddof: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sem(self, /, axis: int, skipna: bool, ddof: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sem(self, /, skipna: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sem(self, /, skipna: bool, ddof: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sem(self, /, axis: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sem(self, /, axis: Literal["columns"]):
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
        usage.dask: 6
        usage.xarray: 1
        """
        ...

    @overload
    def shift(self, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def shift(self, /, periods: int, freq: pandas._libs.tslibs.offsets.Second):
        """
        usage.dask: 1
        """
        ...

    @overload
    def shift(self, /, periods: int, freq: Literal["S"]):
        """
        usage.dask: 4
        """
        ...

    @overload
    def shift(self, /, periods: int, freq: Literal["W"]):
        """
        usage.dask: 3
        """
        ...

    @overload
    def shift(self, /, periods: int, freq: pandas._libs.tslibs.timedeltas.Timedelta):
        """
        usage.dask: 5
        """
        ...

    @overload
    def shift(self, /, periods: int, freq: pandas._libs.tslibs.offsets.Day):
        """
        usage.dask: 1
        """
        ...

    @overload
    def shift(self, /, periods: int, freq: pandas._libs.tslibs.offsets.Hour):
        """
        usage.dask: 1
        """
        ...

    @overload
    def shift(self, /, periods: int, freq: Literal["B"]):
        """
        usage.dask: 3
        """
        ...

    @overload
    def shift(self, /, periods: int, freq: Literal["D"]):
        """
        usage.dask: 3
        """
        ...

    @overload
    def shift(self, /, periods: int, freq: Literal["H"]):
        """
        usage.dask: 3
        """
        ...

    @overload
    def shift(self, /, periods: int, freq: pandas._libs.tslibs.offsets.Minute):
        """
        usage.dask: 1
        """
        ...

    def shift(self, /, periods: int = ..., freq: object = ...):
        """
        usage.dask: 32
        usage.xarray: 1
        """
        ...

    @overload
    def sort_index(self, /):
        """
        usage.dask: 3
        """
        ...

    @overload
    def sort_index(self, /, ascending: bool):
        """
        usage.dask: 1
        """
        ...

    def sort_index(self, /, ascending: bool = ...):
        """
        usage.dask: 4
        """
        ...

    @overload
    def sort_values(self, /):
        """
        usage.dask: 4
        """
        ...

    @overload
    def sort_values(self, /, ascending: bool):
        """
        usage.dask: 1
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

    @overload
    def std(self, /, axis: int, skipna: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def std(self, /):
        """
        usage.dask: 3
        """
        ...

    @overload
    def std(self, /, ddof: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def std(self, /, skipna: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def std(self, /, skipna: bool, ddof: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def std(self, /, axis: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def std(self, /, axis: Literal["columns"]):
        """
        usage.dask: 1
        """
        ...

    def std(
        self,
        /,
        axis: Union[Literal["columns"], int] = ...,
        skipna: bool = ...,
        ddof: int = ...,
    ):
        """
        usage.dask: 9
        """
        ...

    @overload
    def sub(self, /, other: pandas.core.series.Series, fill_value: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sub(self, /, other: int, fill_value: int):
        """
        usage.dask: 1
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
        usage.dask: 1
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
    def sum(self, /):
        """
        usage.dask: 32
        usage.sklearn: 1
        """
        ...

    @overload
    def sum(self, /, axis: int, skipna: bool):
        """
        usage.dask: 2
        """
        ...

    @overload
    def sum(self, /, axis: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sum(self, /, axis: Literal["columns"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sum(self, /, level: int):
        """
        usage.dask: 1
        """
        ...

    def sum(self, /, axis: Union[Literal["columns"], int] = ..., skipna: bool = ...):
        """
        usage.dask: 38
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
        usage.dask: 12
        usage.sklearn: 2
        usage.xarray: 2
        """
        ...

    @overload
    def to_frame(self, /, name: Literal["s"]):
        """
        usage.dask: 2
        """
        ...

    @overload
    def to_frame(self, /, name: None):
        """
        usage.dask: 2
        """
        ...

    @overload
    def to_frame(self, /, name: Literal["bar"]):
        """
        usage.dask: 3
        """
        ...

    @overload
    def to_frame(self, /, name: Literal["__series__"]):
        """
        usage.dask: 2
        """
        ...

    @overload
    def to_frame(self, /, name: Literal["A"]):
        """
        usage.dask: 3
        """
        ...

    @overload
    def to_frame(self, /, name: Literal["a"]):
        """
        usage.dask: 3
        """
        ...

    def to_frame(
        self, /, name: Union[Literal["a", "A", "__series__", "bar", "s"], None] = ...
    ):
        """
        usage.dask: 27
        usage.sklearn: 2
        usage.xarray: 2
        """
        ...

    def to_string(self, /, max_rows: int):
        """
        usage.dask: 1
        """
        ...

    def tolist(self, /):
        """
        usage.dask: 4
        """
        ...

    @overload
    def truediv(self, /, other: pandas.core.series.Series, fill_value: int):
        """
        usage.dask: 3
        """
        ...

    @overload
    def truediv(self, /, other: int, fill_value: int):
        """
        usage.dask: 3
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

    @overload
    def value_counts(self, /):
        """
        usage.dask: 8
        """
        ...

    @overload
    def value_counts(self, /, ascending: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def value_counts(self, /, sort: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def value_counts(self, /, dropna: bool):
        """
        usage.dask: 2
        """
        ...

    @overload
    def value_counts(self, /, ascending: bool, dropna: bool):
        """
        usage.dask: 1
        """
        ...

    def value_counts(self, /, ascending: bool = ..., dropna: bool = ...):
        """
        usage.dask: 13
        """
        ...

    @overload
    def var(self, /, skipna: bool, ddof: int):
        """
        usage.dask: 1
        usage.xarray: 1
        """
        ...

    @overload
    def var(self, /, axis: int, skipna: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def var(self, /):
        """
        usage.dask: 4
        """
        ...

    @overload
    def var(self, /, axis: int, skipna: None):
        """
        usage.dask: 1
        """
        ...

    @overload
    def var(self, /, ddof: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def var(self, /, skipna: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def var(self, /, axis: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def var(self, /, axis: Literal["columns"]):
        """
        usage.dask: 1
        """
        ...

    def var(
        self,
        /,
        axis: Union[Literal["columns"], int] = ...,
        skipna: Union[None, bool] = ...,
        ddof: int = ...,
    ):
        """
        usage.dask: 11
        usage.xarray: 1
        """
        ...

    @overload
    def where(self, /, cond: pandas.core.series.Series):
        """
        usage.dask: 1
        usage.xarray: 1
        """
        ...

    @overload
    def where(
        self,
        /,
        cond: pandas.core.series.Series,
        other: pandas.core.series.Series,
        axis: int,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def where(
        self, /, cond: pandas.core.series.Series, other: numpy.float64, axis: int
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def where(self, /, cond: pandas.core.series.Series, other: float):
        """
        usage.dask: 1
        """
        ...

    @overload
    def where(
        self, /, cond: pandas.core.series.Series, other: pandas.core.series.Series
    ):
        """
        usage.dask: 2
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
