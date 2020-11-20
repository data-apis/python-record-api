from typing import *


class Series:

    # usage.dask: 4
    __module__: ClassVar[object]

    # usage.dask: 7
    # usage.sklearn: 1
    __name__: ClassVar[object]

    # usage.koalas: 1
    to_dict: ClassVar[object]

    # usage.koalas: 1
    to_latex: ClassVar[object]

    # usage.koalas: 1
    to_markdown: ClassVar[object]

    # usage.koalas: 1
    to_string: ClassVar[object]

    @overload
    @classmethod
    def __getitem__(cls, _0: Type[int], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: int, /):
        """
        usage.dask: 16
        usage.geopandas: 3
        usage.koalas: 10
        usage.prophet: 20
        usage.statsmodels: 32
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["int"], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["max", "min"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: numpy.float64, /):
        """
        usage.koalas: 4
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: slice[None, int, None], /):
        """
        usage.koalas: 11
        usage.prophet: 1
        usage.statsmodels: 29
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: slice[int, None, int], /):
        """
        usage.koalas: 2
        usage.statsmodels: 23
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: slice[int, int, int], /):
        """
        usage.koalas: 3
        usage.prophet: 1
        usage.statsmodels: 24
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["2013-01-04T00:00:00"], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: slice[None, Literal["2013-01-04T00:00:00"], None], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls,
        _0: slice[Literal["2013-01-02T00:00:00"], None, Literal["2013-01-02T00:00:00"]],
        /,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls,
        _0: slice[
            Literal["2013-01-02T00:00:00"],
            Literal["2013-01-04T00:00:00"],
            Literal["2013-01-02T00:00:00"],
        ],
        /,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: pandas.core.series.Series, /):
        """
        usage.dask: 6
        usage.geopandas: 2
        usage.koalas: 4
        usage.prophet: 3
        usage.seaborn: 28
        usage.statsmodels: 11
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["A"], /):
        """
        usage.dask: 4
        usage.koalas: 1
        usage.modin: 4
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["B"], /):
        """
        usage.dask: 1
        usage.koalas: 1
        usage.modin: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["a"], /):
        """
        usage.dask: 3
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["a"], Literal["lama"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Type[float], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: cftime._cftime.DatetimeNoLeap, /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["0001"], /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls,
        _0: slice[Literal["0001-01-01"], Literal["0001-12-30"], Literal["0001-01-01"]],
        /,
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: slice[None, Literal["0001-12-30"], None], /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls,
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
    @classmethod
    def __getitem__(cls, _0: slice[None, cftime._cftime.DatetimeNoLeap, None], /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: cftime._cftime.Datetime360Day, /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls,
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
    @classmethod
    def __getitem__(cls, _0: slice[None, cftime._cftime.Datetime360Day, None], /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: cftime._cftime.DatetimeJulian, /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls,
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
    @classmethod
    def __getitem__(cls, _0: slice[None, cftime._cftime.DatetimeJulian, None], /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: cftime._cftime.DatetimeAllLeap, /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls,
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
    @classmethod
    def __getitem__(cls, _0: slice[None, cftime._cftime.DatetimeAllLeap, None], /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: cftime._cftime.DatetimeGregorian, /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls,
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
    @classmethod
    def __getitem__(cls, _0: slice[None, cftime._cftime.DatetimeGregorian, None], /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: cftime._cftime.DatetimeProlepticGregorian, /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls,
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
    @classmethod
    def __getitem__(
        cls, _0: slice[None, cftime._cftime.DatetimeProlepticGregorian, None], /
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: slice[None, None, None], /):
        """
        usage.seaborn: 1
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["lower_dl"], /):
        """
        usage.statsmodels: 4
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["upper_dl"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["prob_exceedance"], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["nuncen_above"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["ncen_equal"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["det_limit_index"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["rank"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["censored"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["cen"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["L1.0->0"], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["fb(0).cov.chol[1,1]"], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["llf"], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["sse"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["mse"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: slice[None, Literal["initial_level"], None], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[numpy.int64], /):
        """
        usage.statsmodels: 12
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[int], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["ds"], /):
        """
        usage.prophet: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["col2"], /):
        """
        usage.modin: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["col1"], /):
        """
        usage.modin: 4
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["C"], /):
        """
        usage.modin: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["idx"], /):
        """
        usage.modin: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: numpy.ndarray, /):
        """
        usage.dask: 1
        usage.geopandas: 5
        usage.seaborn: 8
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["edges"], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["widths"], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["heights"], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["geometry"], /):
        """
        usage.geopandas: 5
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["address"], /):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["amount"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["name"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["id"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["aa"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["bb"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["Edith"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["-500"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["numbers"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["names"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["more_numbers"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["integers"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["dates"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["Date"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["Close"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["b"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["c-d"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["x"], /):
        """
        usage.dask: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["y"], /):
        """
        usage.dask: 4
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[slice[int, int, int]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["25%"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["50%"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["75%"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: pandas.core.indexes.base.Index, /):
        """
        usage.dask: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["z"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["d"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["e"], /):
        """
        usage.dask: 1
        """
        ...

    @classmethod
    def __getitem__(cls, _0: object, /):
        """
        usage.dask: 72
        usage.geopandas: 16
        usage.koalas: 47
        usage.modin: 12
        usage.prophet: 28
        usage.seaborn: 40
        usage.statsmodels: 155
        usage.xarray: 23
        """
        ...

    @overload
    @classmethod
    def __ne__(cls, _0: Type[pandas.core.series.Series], /):
        """
        usage.dask: 4
        """
        ...

    @overload
    @classmethod
    def __ne__(cls, _0: pandas.core.series.Series, /):
        """
        usage.koalas: 4
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __ne__(cls, _0: Literal["ALL"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __ne__(cls, _0: int, /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def __ne__(cls, _0: float, /):
        """
        usage.statsmodels: 1
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
    def __ne__(cls, _0: object, /):
        """
        usage.dask: 4
        usage.koalas: 4
        usage.pandas: 6
        usage.statsmodels: 7
        """
        ...

    @classmethod
    def __rmod__(cls, _0: Union[numpy.timedelta64, numpy.float64, str], /):
        """
        usage.pandas: 2
        usage.sklearn: 1
        """
        ...

    # usage.statsmodels: 3
    T: object

    # usage.dask: 6
    # usage.geopandas: 1
    # usage.sklearn: 1
    __class__: Type[geopandas.geoseries.GeoSeries]

    # usage.dask: 2
    _constructor: object

    # usage.dask: 1
    _data: object

    # usage.dask: 3
    _values: object

    # usage.geopandas: 1
    array: object

    # usage.koalas: 2
    at: object

    # usage.koalas: 2
    axes: object

    # usage.dask: 28
    # usage.seaborn: 10
    cat: object

    # usage.dask: 1
    div: object

    # usage.dask: 1
    divide: object

    # usage.prophet: 1
    ds: object

    # usage.dask: 2
    # usage.koalas: 33
    # usage.prophet: 2
    # usage.xarray: 2
    dt: object

    # usage.dask: 64
    # usage.geopandas: 7
    # usage.koalas: 7
    # usage.prophet: 1
    # usage.seaborn: 2
    # usage.sklearn: 9
    # usage.statsmodels: 2
    dtype: object

    # usage.sklearn: 2
    dtypes: object

    # usage.dask: 1
    # usage.geopandas: 1
    empty: object

    # usage.koalas: 6
    hasnans: object

    # usage.prophet: 3
    holiday: object

    # usage.koalas: 1
    iat: object

    # usage.dask: 31
    # usage.geopandas: 1
    # usage.koalas: 27
    # usage.prophet: 9
    # usage.seaborn: 1
    # usage.sklearn: 1
    # usage.statsmodels: 102
    # usage.xarray: 3
    iloc: object

    # usage.dask: 83
    # usage.geopandas: 5
    # usage.koalas: 42
    # usage.modin: 7
    # usage.seaborn: 12
    # usage.sklearn: 3
    # usage.statsmodels: 252
    # usage.xarray: 23
    index: object

    # usage.koalas: 4
    is_unique: object

    # usage.dask: 19
    # usage.koalas: 30
    # usage.seaborn: 1
    # usage.sklearn: 1
    # usage.statsmodels: 43
    # usage.xarray: 3
    loc: object

    # usage.statsmodels: 1
    lower_ci: object

    # usage.statsmodels: 1
    multiply: object

    # usage.dask: 48
    # usage.geopandas: 3
    # usage.koalas: 16
    # usage.modin: 1
    # usage.seaborn: 9
    # usage.sklearn: 6
    # usage.statsmodels: 31
    # usage.xarray: 5
    name: Union[
        Tuple[Literal["X", "Y", "x", "y"], Literal["A", "B", "a", "z"]], int, str, None
    ]

    # usage.koalas: 1
    names: List[Literal["koalas", "hello"]]

    # usage.dask: 2
    nbytes: object

    # usage.dask: 6
    # usage.sklearn: 4
    # usage.statsmodels: 19
    ndim: object

    # usage.koalas: 13
    plot: object

    # usage.dask: 1
    rdiv: object

    # usage.dask: 7
    # usage.koalas: 2
    # usage.prophet: 1
    # usage.seaborn: 1
    # usage.sklearn: 12
    # usage.statsmodels: 53
    shape: object

    # usage.dask: 2
    # usage.seaborn: 25
    # usage.statsmodels: 9
    size: object

    # usage.dask: 26
    # usage.geopandas: 2
    # usage.koalas: 103
    # usage.seaborn: 2
    str: object

    # usage.statsmodels: 1
    upper_ci: object

    # usage.dask: 40
    # usage.geopandas: 15
    # usage.koalas: 11
    # usage.modin: 1
    # usage.prophet: 38
    # usage.seaborn: 22
    # usage.statsmodels: 280
    # usage.xarray: 16
    values: object

    @overload
    def __add__(self, _0: int, /):
        """
        usage.dask: 35
        usage.koalas: 65
        usage.modin: 1
        usage.statsmodels: 6
        """
        ...

    @overload
    def __add__(self, _0: numpy.int64, /):
        """
        usage.dask: 2
        usage.koalas: 49
        usage.statsmodels: 1
        """
        ...

    @overload
    def __add__(self, _0: pandas.core.series.Series, /):
        """
        usage.dask: 14
        usage.koalas: 6
        usage.prophet: 4
        usage.seaborn: 1
        usage.statsmodels: 17
        """
        ...

    @overload
    def __add__(self, _0: Literal["_lit"], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __add__(self, _0: numpy.ndarray, /):
        """
        usage.dask: 2
        usage.prophet: 1
        usage.seaborn: 1
        usage.statsmodels: 17
        """
        ...

    @overload
    def __add__(self, _0: float, /):
        """
        usage.dask: 2
        usage.seaborn: 1
        usage.statsmodels: 2
        """
        ...

    @overload
    def __add__(self, _0: numpy.float64, /):
        """
        usage.dask: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    def __add__(self, _0: Literal[")"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __add__(self, _0: Literal["*"], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    def __add__(self, _0: Literal[""], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __add__(self, _0: Literal["Q"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __add__(self, _0: Union[numpy.ndarray, numpy.timedelta64, numpy.datetime64], /):
        """
        usage.pandas: 39
        """
        ...

    @overload
    def __add__(self, _0: dask.dataframe.core.Scalar, /):
        """
        usage.dask: 1
        """
        ...

    def __add__(self, _0: object, /):
        """
        usage.dask: 57
        usage.koalas: 121
        usage.modin: 1
        usage.pandas: 39
        usage.prophet: 5
        usage.seaborn: 3
        usage.statsmodels: 50
        """
        ...

    @overload
    def __and__(self, _0: pandas.core.series.Series, /):
        """
        usage.dask: 5
        usage.geopandas: 4
        usage.koalas: 3
        usage.prophet: 3
        usage.seaborn: 2
        usage.statsmodels: 4
        """
        ...

    @overload
    def __and__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 3
        usage.seaborn: 1
        """
        ...

    @overload
    def __and__(self, _0: bool, /):
        """
        usage.geopandas: 2
        """
        ...

    def __and__(self, _0: Union[pandas.core.series.Series, numpy.ndarray, bool], /):
        """
        usage.dask: 5
        usage.geopandas: 6
        usage.koalas: 3
        usage.pandas: 3
        usage.prophet: 3
        usage.seaborn: 3
        usage.statsmodels: 4
        """
        ...

    def __array_wrap__(self, /, result: numpy.ndarray):
        """
        usage.dask: 3
        """
        ...

    @overload
    def __contains__(self, _0: Literal["missing"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["nobs"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["bool"], /):
        """
        usage.pandas: 1
        """
        ...

    def __contains__(self, _0: Literal["bool", "nobs", "missing"], /):
        """
        usage.pandas: 1
        usage.statsmodels: 2
        """
        ...

    @overload
    def __eq__(self, _0: Literal["c"], /):
        """
        usage.koalas: 2
        usage.seaborn: 20
        """
        ...

    @overload
    def __eq__(self, _0: Literal["a"], /):
        """
        usage.dask: 1
        usage.koalas: 2
        usage.seaborn: 24
        """
        ...

    @overload
    def __eq__(self, _0: Literal["b"], /):
        """
        usage.koalas: 2
        usage.seaborn: 22
        """
        ...

    @overload
    def __eq__(self, _0: pandas.core.series.Series, /):
        """
        usage.dask: 24
        usage.geopandas: 2
        usage.koalas: 4
        usage.statsmodels: 2
        """
        ...

    @overload
    def __eq__(self, _0: int, /):
        """
        usage.dask: 5
        usage.koalas: 32
        usage.prophet: 1
        usage.seaborn: 3
        usage.statsmodels: 4
        """
        ...

    @overload
    def __eq__(self, _0: numpy.int64, /):
        """
        usage.dask: 1
        usage.koalas: 1
        usage.seaborn: 3
        """
        ...

    @overload
    def __eq__(self, _0: Literal["Duncan"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __eq__(self, _0: Literal["carData"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __eq__(self, _0: Literal["Guerry"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __eq__(self, _0: Literal["HistData"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __eq__(self, _0: Literal["ALL"], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __eq__(self, _0: numpy.float64, /):
        """
        usage.dask: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    def __eq__(self, _0: Literal["ND"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __eq__(self, _0: float, /):
        """
        usage.dask: 1
        usage.statsmodels: 10
        """
        ...

    @overload
    def __eq__(self, _0: Literal["1"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __eq__(self, _0: Literal["iris"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __eq__(self, _0: Literal["datasets"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __eq__(self, _0: Literal["quakes"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __eq__(self, _0: pandas.core.frame.DataFrame, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __eq__(self, _0: object, /):
        """
        usage.pandas: 52
        """
        ...

    @overload
    def __eq__(self, _0: pandas._libs.tslibs.timedeltas.Timedelta, /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    def __eq__(self, _0: Literal["Yes"], /):
        """
        usage.seaborn: 2
        """
        ...

    @overload
    def __eq__(self, _0: Literal["No"], /):
        """
        usage.seaborn: 2
        """
        ...

    @overload
    def __eq__(self, _0: Literal["Lunch"], /):
        """
        usage.seaborn: 2
        """
        ...

    @overload
    def __eq__(self, _0: Literal["Dinner"], /):
        """
        usage.seaborn: 2
        """
        ...

    @overload
    def __eq__(self, _0: Literal["rest"], /):
        """
        usage.seaborn: 3
        """
        ...

    @overload
    def __eq__(self, _0: Literal["walking"], /):
        """
        usage.seaborn: 3
        """
        ...

    @overload
    def __eq__(self, _0: Literal["running"], /):
        """
        usage.seaborn: 3
        """
        ...

    @overload
    def __eq__(self, _0: Literal["no fat"], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def __eq__(self, _0: Literal["low fat"], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def __eq__(self, _0: Literal["A"], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def __eq__(self, _0: Literal["B"], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def __eq__(self, _0: Literal["C"], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def __eq__(self, _0: Literal["D"], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def __eq__(self, _0: Literal["E"], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def __eq__(self, _0: Literal["F"], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def __eq__(self, _0: Literal["G"], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def __eq__(self, _0: Literal["First"], /):
        """
        usage.seaborn: 2
        """
        ...

    @overload
    def __eq__(self, _0: Literal["Second"], /):
        """
        usage.seaborn: 2
        """
        ...

    @overload
    def __eq__(self, _0: Literal["Third"], /):
        """
        usage.seaborn: 2
        """
        ...

    @overload
    def __eq__(self, _0: Literal["male"], /):
        """
        usage.seaborn: 2
        """
        ...

    @overload
    def __eq__(self, _0: Literal["female"], /):
        """
        usage.seaborn: 2
        """
        ...

    @overload
    def __eq__(self, _0: Literal["Male"], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def __eq__(self, _0: Literal["Female"], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def __eq__(self, _0: Literal["II"], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def __eq__(self, _0: Literal["III"], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def __eq__(self, _0: Literal["j"], /):
        """
        usage.seaborn: 2
        """
        ...

    @overload
    def __eq__(self, _0: Literal["d"], /):
        """
        usage.seaborn: 7
        """
        ...

    @overload
    def __eq__(self, _0: Literal["e"], /):
        """
        usage.seaborn: 7
        """
        ...

    @overload
    def __eq__(self, _0: Literal["f"], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def __eq__(self, _0: Literal["g"], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def __eq__(self, _0: Literal["h"], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def __eq__(self, _0: Literal["i"], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def __eq__(self, _0: Literal["k"], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def __eq__(self, _0: Literal["l"], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def __eq__(self, _0: Literal["m"], /):
        """
        usage.seaborn: 17
        """
        ...

    @overload
    def __eq__(self, _0: numpy.bool_, /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def __eq__(self, _0: Literal["n"], /):
        """
        usage.seaborn: 13
        """
        ...

    @overload
    def __eq__(self, _0: Literal["t"], /):
        """
        usage.seaborn: 2
        """
        ...

    @overload
    def __eq__(self, _0: Literal["u"], /):
        """
        usage.seaborn: 2
        """
        ...

    @overload
    def __eq__(self, _0: Literal["v"], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def __eq__(self, _0: Literal["x"], /):
        """
        usage.seaborn: 3
        """
        ...

    @overload
    def __eq__(self, _0: Literal["y"], /):
        """
        usage.seaborn: 3
        """
        ...

    @overload
    def __eq__(self, _0: Literal["o"], /):
        """
        usage.seaborn: 3
        """
        ...

    @overload
    def __eq__(self, _0: Literal["numeric"], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def __eq__(self, _0: Literal["geometry"], /):
        """
        usage.geopandas: 2
        """
        ...

    @overload
    def __eq__(self, _0: numpy.ndarray, /):
        """
        usage.geopandas: 5
        """
        ...

    @overload
    def __eq__(self, _0: Literal["Africa"], /):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __eq__(self, _0: Literal["Queens"], /):
        """
        usage.geopandas: 3
        """
        ...

    @overload
    def __eq__(self, _0: Literal["Bronx"], /):
        """
        usage.geopandas: 2
        """
        ...

    @overload
    def __eq__(self, _0: Literal["Polygon"], /):
        """
        usage.geopandas: 2
        """
        ...

    @overload
    def __eq__(self, _0: Literal["MultiPolygon"], /):
        """
        usage.geopandas: 2
        """
        ...

    @overload
    def __eq__(self, _0: Literal["LineString"], /):
        """
        usage.geopandas: 2
        """
        ...

    @overload
    def __eq__(self, _0: Literal["MultiLineString"], /):
        """
        usage.geopandas: 2
        """
        ...

    @overload
    def __eq__(self, _0: Literal["LinearRing"], /):
        """
        usage.geopandas: 2
        """
        ...

    @overload
    def __eq__(self, _0: Literal["Point"], /):
        """
        usage.geopandas: 2
        """
        ...

    @overload
    def __eq__(self, _0: Literal["MultiPoint"], /):
        """
        usage.geopandas: 2
        """
        ...

    @overload
    def __eq__(self, _0: Literal["category"], /):
        """
        usage.dask: 4
        """
        ...

    @overload
    def __eq__(self, _0: Literal["i8"], /):
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
        usage.geopandas: 29
        usage.koalas: 43
        usage.pandas: 52
        usage.prophet: 2
        usage.seaborn: 180
        usage.sklearn: 10
        usage.statsmodels: 29
        """
        ...

    @overload
    def __floordiv__(self, _0: int, /):
        """
        usage.dask: 1
        usage.koalas: 36
        """
        ...

    @overload
    def __floordiv__(self, _0: numpy.timedelta64, /):
        """
        usage.koalas: 3
        """
        ...

    @overload
    def __floordiv__(self, _0: Union[numpy.timedelta64, numpy.ndarray], /):
        """
        usage.pandas: 6
        """
        ...

    @overload
    def __floordiv__(self, _0: float, /):
        """
        usage.dask: 2
        """
        ...

    def __floordiv__(self, _0: Union[int, float, numpy.timedelta64, numpy.ndarray], /):
        """
        usage.dask: 3
        usage.koalas: 39
        usage.pandas: 6
        """
        ...

    @overload
    def __ge__(self, _0: numpy.float64, /):
        """
        usage.dask: 1
        usage.seaborn: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    def __ge__(self, _0: numpy.int64, /):
        """
        usage.dask: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    def __ge__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 7
        """
        ...

    @overload
    def __ge__(self, _0: pandas.core.series.Series, /):
        """
        usage.prophet: 3
        """
        ...

    @overload
    def __ge__(self, _0: int, /):
        """
        usage.dask: 6
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
        usage.dask: 17
        usage.pandas: 7
        usage.prophet: 3
        usage.seaborn: 1
        usage.statsmodels: 2
        """
        ...

    @overload
    def __gt__(self, _0: int, /):
        """
        usage.dask: 55
        usage.geopandas: 1
        usage.koalas: 12
        usage.statsmodels: 4
        """
        ...

    @overload
    def __gt__(self, _0: float, /):
        """
        usage.koalas: 1
        usage.statsmodels: 2
        """
        ...

    @overload
    def __gt__(self, _0: numpy.ndarray, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __gt__(self, _0: Union[numpy.timedelta64, numpy.ndarray], /):
        """
        usage.pandas: 5
        """
        ...

    @overload
    def __gt__(self, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        """
        usage.prophet: 2
        """
        ...

    @overload
    def __gt__(self, _0: pandas._libs.tslibs.timedeltas.Timedelta, /):
        """
        usage.prophet: 2
        """
        ...

    @overload
    def __gt__(self, _0: pandas.core.series.Series, /):
        """
        usage.dask: 2
        usage.prophet: 3
        """
        ...

    @overload
    def __gt__(self, _0: Literal["2014-01-01"], /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    def __gt__(self, _0: pandas.core.frame.DataFrame, /):
        """
        usage.dask: 1
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
        usage.geopandas: 1
        usage.koalas: 13
        usage.pandas: 5
        usage.prophet: 8
        usage.statsmodels: 7
        """
        ...

    @overload
    def __iadd__(self, _0: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        usage.seaborn: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    def __iadd__(self, _0: numpy.ndarray, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __iadd__(self, _0: List[float], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __iadd__(self, _0: Union[numpy.ndarray, numpy.timedelta64], /):
        """
        usage.pandas: 2
        """
        ...

    @overload
    def __iadd__(self, _0: int, /):
        """
        usage.prophet: 1
        usage.seaborn: 1
        """
        ...

    @overload
    def __iadd__(self, _0: float, /):
        """
        usage.prophet: 5
        """
        ...

    def __iadd__(self, _0: object, /):
        """
        usage.koalas: 1
        usage.pandas: 2
        usage.prophet: 6
        usage.seaborn: 2
        usage.statsmodels: 3
        """
        ...

    @overload
    def __iand__(self, _0: numpy.ndarray, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __iand__(self, _0: pandas.core.series.Series, /):
        """
        usage.seaborn: 1
        """
        ...

    def __iand__(self, _0: Union[pandas.core.series.Series, numpy.ndarray], /):
        """
        usage.seaborn: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    def __imul__(self, _0: float, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __imul__(self, _0: numpy.ndarray, /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __imul__(self, _0: numpy.float64, /):
        """
        usage.seaborn: 1
        """
        ...

    def __imul__(self, _0: Union[numpy.float64, float, numpy.ndarray], /):
        """
        usage.seaborn: 1
        usage.statsmodels: 3
        """
        ...

    def __invert__(self, /):
        """
        usage.dask: 1
        usage.geopandas: 5
        usage.koalas: 1
        usage.prophet: 1
        usage.seaborn: 1
        usage.statsmodels: 22
        usage.xarray: 1
        """
        ...

    @overload
    def __ior__(self, _0: pandas.core.series.Series, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __ior__(self, _0: numpy.ndarray, /):
        """
        usage.statsmodels: 3
        """
        ...

    def __ior__(self, _0: Union[numpy.ndarray, pandas.core.series.Series], /):
        """
        usage.statsmodels: 4
        """
        ...

    @overload
    def __isub__(self, _0: numpy.float64, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __isub__(self, _0: Union[numpy.ndarray, numpy.timedelta64], /):
        """
        usage.pandas: 2
        """
        ...

    @overload
    def __isub__(self, _0: float, /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    def __isub__(self, _0: int, /):
        """
        usage.seaborn: 1
        """
        ...

    def __isub__(
        self, _0: Union[int, numpy.timedelta64, numpy.ndarray, numpy.float64, float], /
    ):
        """
        usage.pandas: 2
        usage.prophet: 1
        usage.seaborn: 1
        usage.statsmodels: 1
        """
        ...

    def __iter__(self, /):
        """
        usage.dask: 4
        usage.koalas: 2
        usage.modin: 2
        usage.prophet: 1
        usage.seaborn: 7
        usage.sklearn: 12
        usage.statsmodels: 16
        """
        ...

    @overload
    def __itruediv__(self, _0: pandas.core.series.Series, /):
        """
        usage.dask: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    def __itruediv__(self, _0: numpy.float64, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __itruediv__(self, _0: int, /):
        """
        usage.seaborn: 1
        """
        ...

    def __itruediv__(self, _0: Union[pandas.core.series.Series, numpy.float64, int], /):
        """
        usage.dask: 1
        usage.seaborn: 1
        usage.statsmodels: 2
        """
        ...

    @overload
    def __le__(self, _0: numpy.float64, /):
        """
        usage.dask: 1
        usage.seaborn: 1
        usage.statsmodels: 2
        """
        ...

    @overload
    def __le__(self, _0: float, /):
        """
        usage.dask: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    def __le__(self, _0: int, /):
        """
        usage.dask: 3
        usage.statsmodels: 1
        """
        ...

    @overload
    def __le__(self, _0: Union[numpy.ndarray, numpy.float64], /):
        """
        usage.pandas: 7
        """
        ...

    @overload
    def __le__(self, _0: pandas.core.series.Series, /):
        """
        usage.prophet: 3
        """
        ...

    @overload
    def __le__(self, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        """
        usage.prophet: 4
        """
        ...

    @overload
    def __le__(self, _0: numpy.int64, /):
        """
        usage.dask: 1
        """
        ...

    def __le__(self, _0: object, /):
        """
        usage.dask: 6
        usage.pandas: 7
        usage.prophet: 7
        usage.seaborn: 1
        usage.statsmodels: 4
        """
        ...

    @overload
    def __lt__(self, _0: int, /):
        """
        usage.dask: 9
        usage.koalas: 4
        usage.prophet: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    def __lt__(self, _0: numpy.float64, /):
        """
        usage.dask: 1
        usage.statsmodels: 2
        """
        ...

    @overload
    def __lt__(self, _0: float, /):
        """
        usage.dask: 1
        usage.statsmodels: 4
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
        usage.prophet: 3
        """
        ...

    @overload
    def __lt__(self, _0: Literal["2013-01-01"], /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    def __lt__(self, _0: pandas._libs.tslibs.timedeltas.Timedelta, /):
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

    def __lt__(self, _0: object, /):
        """
        usage.dask: 16
        usage.koalas: 4
        usage.pandas: 4
        usage.prophet: 5
        usage.statsmodels: 7
        """
        ...

    @overload
    def __mod__(self, _0: int, /):
        """
        usage.dask: 5
        usage.geopandas: 2
        usage.koalas: 16
        """
        ...

    @overload
    def __mod__(self, _0: Union[numpy.timedelta64, numpy.ndarray], /):
        """
        usage.pandas: 57
        """
        ...

    def __mod__(self, _0: Union[int, numpy.ndarray, numpy.timedelta64], /):
        """
        usage.dask: 5
        usage.geopandas: 2
        usage.koalas: 16
        usage.pandas: 57
        """
        ...

    @overload
    def __mul__(self, _0: int, /):
        """
        usage.dask: 2
        usage.koalas: 5
        usage.seaborn: 2
        usage.statsmodels: 4
        """
        ...

    @overload
    def __mul__(self, _0: pandas.core.series.Series, /):
        """
        usage.dask: 4
        usage.koalas: 6
        usage.prophet: 1
        usage.seaborn: 1
        usage.statsmodels: 5
        """
        ...

    @overload
    def __mul__(self, _0: float, /):
        """
        usage.dask: 1
        usage.statsmodels: 9
        """
        ...

    @overload
    def __mul__(self, _0: numpy.float64, /):
        """
        usage.prophet: 2
        usage.statsmodels: 4
        """
        ...

    @overload
    def __mul__(self, _0: numpy.ndarray, /):
        """
        usage.prophet: 1
        usage.statsmodels: 2
        """
        ...

    @overload
    def __mul__(self, _0: numpy.int64, /):
        """
        usage.statsmodels: 2
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

    def __mul__(self, _0: object, /):
        """
        usage.dask: 7
        usage.koalas: 11
        usage.pandas: 29
        usage.prophet: 4
        usage.seaborn: 3
        usage.statsmodels: 26
        """
        ...

    def __neg__(self, /):
        """
        usage.dask: 2
        usage.koalas: 17
        usage.statsmodels: 2
        """
        ...

    @overload
    def __or__(self, _0: pandas.core.series.Series, /):
        """
        usage.dask: 3
        usage.geopandas: 8
        usage.koalas: 3
        usage.prophet: 1
        """
        ...

    @overload
    def __or__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 3
        usage.seaborn: 1
        """
        ...

    def __or__(self, _0: Union[pandas.core.series.Series, numpy.ndarray], /):
        """
        usage.dask: 3
        usage.geopandas: 8
        usage.koalas: 3
        usage.pandas: 3
        usage.prophet: 1
        usage.seaborn: 1
        """
        ...

    @overload
    def __pow__(self, _0: int, /):
        """
        usage.dask: 3
        usage.koalas: 1
        usage.prophet: 7
        usage.statsmodels: 10
        """
        ...

    @overload
    def __pow__(self, _0: float, /):
        """
        usage.dask: 2
        usage.statsmodels: 1
        """
        ...

    @overload
    def __pow__(self, _0: numpy.timedelta64, /):
        """
        usage.pandas: 1
        """
        ...

    def __pow__(self, _0: Union[float, int, numpy.timedelta64], /):
        """
        usage.dask: 5
        usage.koalas: 1
        usage.pandas: 1
        usage.prophet: 7
        usage.statsmodels: 11
        """
        ...

    @overload
    def __radd__(self, _0: pandas.core.frame.DataFrame, /):
        """
        usage.koalas: 48
        usage.statsmodels: 2
        """
        ...

    @overload
    def __radd__(self, _0: pandas.core.series.Series, /):
        """
        usage.dask: 14
        usage.koalas: 6
        usage.prophet: 4
        usage.seaborn: 1
        usage.statsmodels: 17
        """
        ...

    @overload
    def __radd__(self, _0: Literal["_lit"], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __radd__(self, _0: numpy.ndarray, /):
        """
        usage.dask: 2
        usage.prophet: 2
        usage.statsmodels: 2
        """
        ...

    @overload
    def __radd__(self, _0: int, /):
        """
        usage.dask: 1
        usage.prophet: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    def __radd__(self, _0: Literal["("], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __radd__(self, _0: numpy.float64, /):
        """
        usage.statsmodels: 1
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

    def __radd__(self, _0: object, /):
        """
        usage.dask: 18
        usage.koalas: 55
        usage.pandas: 46
        usage.prophet: 7
        usage.seaborn: 1
        usage.statsmodels: 24
        """
        ...

    @overload
    def __rand__(self, _0: pandas.core.series.Series, /):
        """
        usage.dask: 5
        usage.geopandas: 4
        usage.koalas: 3
        usage.prophet: 3
        usage.seaborn: 2
        usage.statsmodels: 4
        """
        ...

    @overload
    def __rand__(self, _0: numpy.ndarray, /):
        """
        usage.seaborn: 1
        """
        ...

    def __rand__(self, _0: Union[pandas.core.series.Series, numpy.ndarray], /):
        """
        usage.dask: 5
        usage.geopandas: 4
        usage.koalas: 3
        usage.prophet: 3
        usage.seaborn: 3
        usage.statsmodels: 4
        """
        ...

    def __rfloordiv__(
        self, _0: Union[numpy.float64, numpy.int64, numpy.ndarray, numpy.timedelta64], /
    ):
        """
        usage.pandas: 6
        """
        ...

    def __rmatmul__(self, _0: numpy.ndarray, /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    def __rmul__(self, _0: float, /):
        """
        usage.koalas: 2
        usage.sklearn: 1
        usage.statsmodels: 2
        """
        ...

    @overload
    def __rmul__(self, _0: pandas.core.series.Series, /):
        """
        usage.dask: 4
        usage.koalas: 6
        usage.prophet: 1
        usage.seaborn: 1
        usage.statsmodels: 5
        """
        ...

    @overload
    def __rmul__(self, _0: int, /):
        """
        usage.koalas: 3
        usage.seaborn: 1
        usage.sklearn: 1
        usage.statsmodels: 11
        """
        ...

    @overload
    def __rmul__(self, _0: numpy.ndarray, /):
        """
        usage.prophet: 1
        usage.statsmodels: 6
        """
        ...

    @overload
    def __rmul__(self, _0: numpy.float64, /):
        """
        usage.statsmodels: 9
        """
        ...

    @overload
    def __rmul__(self, _0: pandas.core.frame.DataFrame, /):
        """
        usage.statsmodels: 4
        """
        ...

    @overload
    def __rmul__(self, _0: object, /):
        """
        usage.pandas: 30
        """
        ...

    def __rmul__(self, _0: object, /):
        """
        usage.dask: 4
        usage.koalas: 11
        usage.pandas: 30
        usage.prophet: 2
        usage.seaborn: 2
        usage.sklearn: 2
        usage.statsmodels: 37
        """
        ...

    @overload
    def __ror__(self, _0: pandas.core.series.Series, /):
        """
        usage.dask: 3
        usage.geopandas: 8
        usage.koalas: 3
        usage.prophet: 1
        """
        ...

    @overload
    def __ror__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    def __ror__(self, _0: Union[pandas.core.series.Series, numpy.ndarray], /):
        """
        usage.dask: 3
        usage.geopandas: 8
        usage.koalas: 3
        usage.pandas: 1
        usage.prophet: 1
        """
        ...

    def __rpow__(self, _0: Union[numpy.float64, numpy.int64, numpy.timedelta64], /):
        """
        usage.pandas: 10
        """
        ...

    @overload
    def __rsub__(self, _0: pandas.core.series.Series, /):
        """
        usage.dask: 5
        usage.geopandas: 1
        usage.koalas: 14
        usage.prophet: 16
        usage.seaborn: 2
        usage.statsmodels: 14
        """
        ...

    @overload
    def __rsub__(self, _0: Literal["2013-03-11"], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __rsub__(self, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __rsub__(self, _0: pandas.core.frame.DataFrame, /):
        """
        usage.dask: 5
        usage.seaborn: 2
        usage.statsmodels: 8
        """
        ...

    @overload
    def __rsub__(self, _0: numpy.ndarray, /):
        """
        usage.statsmodels: 7
        """
        ...

    @overload
    def __rsub__(self, _0: int, /):
        """
        usage.statsmodels: 6
        """
        ...

    @overload
    def __rsub__(self, _0: object, /):
        """
        usage.pandas: 44
        """
        ...

    def __rsub__(self, _0: object, /):
        """
        usage.dask: 10
        usage.geopandas: 1
        usage.koalas: 16
        usage.pandas: 44
        usage.prophet: 16
        usage.seaborn: 4
        usage.statsmodels: 35
        """
        ...

    @overload
    def __rtruediv__(self, _0: pandas.core.series.Series, /):
        """
        usage.dask: 8
        usage.koalas: 5
        usage.prophet: 2
        usage.statsmodels: 10
        """
        ...

    @overload
    def __rtruediv__(self, _0: pandas.core.frame.DataFrame, /):
        """
        usage.seaborn: 2
        usage.statsmodels: 5
        """
        ...

    @overload
    def __rtruediv__(self, _0: int, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __rtruediv__(self, _0: numpy.ndarray, /):
        """
        usage.statsmodels: 6
        """
        ...

    @overload
    def __rtruediv__(self, _0: object, /):
        """
        usage.pandas: 37
        """
        ...

    def __rtruediv__(self, _0: object, /):
        """
        usage.dask: 8
        usage.koalas: 5
        usage.pandas: 37
        usage.prophet: 2
        usage.seaborn: 2
        usage.statsmodels: 22
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
        usage.statsmodels: 8
        usage.xarray: 2
        """
        ...

    @overload
    def __setitem__(self, _0: slice[None, None, None], _1: int, /):
        """
        usage.seaborn: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: slice[int, int, int], _1: float, /):
        """
        usage.statsmodels: 4
        """
        ...

    @overload
    def __setitem__(self, _0: slice[int, int, int], _1: float, /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    def __setitem__(
        self, _0: pandas.core.series.Series, _1: pandas.core.series.Series, /
    ):
        """
        usage.seaborn: 2
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: int, _1: numpy.dtype, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: pandas.core.series.Series, _1: float, /):
        """
        usage.dask: 1
        usage.seaborn: 1
        usage.statsmodels: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["L1.0->0"], _1: numpy.float64, /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["fb(0).cov.chol[1,1]"], _1: numpy.float64, /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __setitem__(self, _0: numpy.ndarray, _1: bool, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: slice[None, int, None], _1: float, /):
        """
        usage.modin: 1
        """
        ...

    @overload
    def __setitem__(self, _0: slice[int, None, int], _1: float, /):
        """
        usage.modin: 1
        """
        ...

    @overload
    def __setitem__(self, _0: pandas.core.series.Series, _1: int, /):
        """
        usage.dask: 2
        usage.seaborn: 1
        """
        ...

    def __setitem__(
        self,
        _0: Union[
            pandas.core.series.Series,
            numpy.ndarray,
            int,
            Literal["fb(0).cov.chol[1,1]", "L1.0->0"],
            slice[Union[int, None], Union[int, None], Union[int, None]],
        ],
        _1: object,
        /,
    ):
        """
        usage.dask: 3
        usage.modin: 2
        usage.seaborn: 5
        usage.statsmodels: 25
        usage.xarray: 2
        """
        ...

    @overload
    def __sub__(self, _0: pandas.core.series.Series, /):
        """
        usage.dask: 5
        usage.geopandas: 1
        usage.koalas: 14
        usage.prophet: 16
        usage.seaborn: 2
        usage.statsmodels: 14
        """
        ...

    @overload
    def __sub__(self, _0: Literal["2012-01-01"], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __sub__(self, _0: int, /):
        """
        usage.dask: 4
        usage.koalas: 3
        usage.statsmodels: 2
        """
        ...

    @overload
    def __sub__(self, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        """
        usage.koalas: 1
        usage.prophet: 2
        """
        ...

    @overload
    def __sub__(self, _0: numpy.float64, /):
        """
        usage.dask: 9
        usage.prophet: 1
        usage.statsmodels: 10
        """
        ...

    @overload
    def __sub__(self, _0: numpy.ndarray, /):
        """
        usage.prophet: 1
        usage.seaborn: 3
        usage.statsmodels: 4
        """
        ...

    @overload
    def __sub__(self, _0: Union[numpy.ndarray, numpy.datetime64, numpy.timedelta64], /):
        """
        usage.pandas: 35
        """
        ...

    @overload
    def __sub__(self, _0: float, /):
        """
        usage.prophet: 2
        """
        ...

    @overload
    def __sub__(self, _0: Literal["1970-01-01T00:00:00"], /):
        """
        usage.prophet: 1
        """
        ...

    def __sub__(self, _0: object, /):
        """
        usage.dask: 18
        usage.geopandas: 1
        usage.koalas: 19
        usage.pandas: 35
        usage.prophet: 23
        usage.seaborn: 5
        usage.statsmodels: 30
        """
        ...

    @overload
    def __truediv__(self, _0: pandas.core.series.Series, /):
        """
        usage.dask: 8
        usage.koalas: 5
        usage.prophet: 2
        usage.statsmodels: 10
        """
        ...

    @overload
    def __truediv__(self, _0: int, /):
        """
        usage.dask: 1
        usage.koalas: 1
        usage.prophet: 1
        usage.statsmodels: 4
        """
        ...

    @overload
    def __truediv__(self, _0: float, /):
        """
        usage.dask: 1
        usage.koalas: 1
        usage.prophet: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    def __truediv__(self, _0: numpy.float64, /):
        """
        usage.prophet: 3
        usage.statsmodels: 10
        """
        ...

    @overload
    def __truediv__(self, _0: numpy.ndarray, /):
        """
        usage.prophet: 1
        usage.statsmodels: 5
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
    def __truediv__(self, _0: pandas._libs.tslibs.timedeltas.Timedelta, /):
        """
        usage.prophet: 2
        """
        ...

    def __truediv__(self, _0: object, /):
        """
        usage.dask: 10
        usage.koalas: 7
        usage.pandas: 29
        usage.prophet: 10
        usage.statsmodels: 30
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
        usage.koalas: 2
        usage.prophet: 2
        """
        ...

    @overload
    def add(self, /, other: pandas.core.series.Series, level: int):
        """
        usage.statsmodels: 1
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
        other: Union[int, pandas.core.series.Series],
        level: int = ...,
        fill_value: Union[None, int] = ...,
    ):
        """
        usage.dask: 7
        usage.statsmodels: 1
        """
        ...

    def add_prefix(self, /, prefix: Literal["item_"]):
        """
        usage.koalas: 2
        """
        ...

    def add_suffix(self, /, suffix: Literal["_item"]):
        """
        usage.koalas: 2
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
        usage.geopandas: 7
        usage.koalas: 8
        usage.prophet: 5
        usage.seaborn: 13
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
        usage.geopandas: 7
        usage.koalas: 8
        usage.prophet: 5
        usage.seaborn: 13
        """
        ...

    @overload
    def any(self, /):
        """
        usage.dask: 6
        usage.geopandas: 5
        usage.koalas: 3
        usage.prophet: 4
        usage.seaborn: 6
        usage.sklearn: 2
        usage.statsmodels: 3
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
        usage.geopandas: 5
        usage.koalas: 3
        usage.prophet: 4
        usage.seaborn: 6
        usage.sklearn: 2
        usage.statsmodels: 3
        usage.xarray: 1
        """
        ...

    @overload
    def append(self, /, to_append: pandas.core.series.Series):
        """
        usage.dask: 2
        usage.koalas: 2
        """
        ...

    @overload
    def append(self, /, to_append: pandas.core.series.Series, ignore_index: bool):
        """
        usage.koalas: 1
        """
        ...

    def append(self, /, to_append: pandas.core.series.Series, ignore_index: bool = ...):
        """
        usage.dask: 2
        usage.koalas: 3
        """
        ...

    @overload
    def apply(self, /, func: Callable):
        """
        usage.dask: 6
        usage.koalas: 1
        usage.prophet: 1
        usage.statsmodels: 2
        """
        ...

    @overload
    def apply(self, /, func: numpy.ufunc):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def apply(self, /, func: numpy.ufunc):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def apply(self, /, func: numpy.ufunc):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def apply(self, /, func: Type[str]):
        """
        usage.koalas: 11
        """
        ...

    @overload
    def apply(self, /, func: Callable, args: Tuple[pandas.core.frame.DataFrame]):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def apply(self, /, func: Callable, args: Tuple[Literal["%tc"]]):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def apply(self, /, func: Callable, args: Tuple[Literal["%tC"]]):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def apply(self, /, func: Callable, args: Tuple[Literal["%td"]]):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def apply(self, /, func: Callable, args: Tuple[Literal["%tw"]]):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def apply(self, /, func: Callable, args: Tuple[Literal["%tm"]]):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def apply(self, /, func: Callable, args: Tuple[Literal["%tq"]]):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def apply(self, /, func: Callable, args: Tuple[Literal["%th"]]):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def apply(self, /, func: Callable, args: Tuple[Literal["%ty"]]):
        """
        usage.statsmodels: 1
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
        self,
        /,
        func: Union[Callable, Type[str], numpy.ufunc],
        convert_dtype: bool = ...,
        args: Tuple[Union[pandas.core.frame.DataFrame, str, None], ...] = ...,
    ):
        """
        usage.dask: 9
        usage.koalas: 15
        usage.prophet: 1
        usage.sklearn: 1
        usage.statsmodels: 11
        """
        ...

    @overload
    def asof(self, /, where: int):
        """
        usage.koalas: 4
        """
        ...

    @overload
    def asof(self, /, where: List[int]):
        """
        usage.koalas: 2
        """
        ...

    def asof(self, /, where: Union[List[int], int]):
        """
        usage.koalas: 6
        """
        ...

    @overload
    def astype(self, /, dtype: Type[numpy.int32]):
        """
        usage.dask: 1
        usage.koalas: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    def astype(self, /, dtype: Type[bool]):
        """
        usage.geopandas: 2
        usage.koalas: 5
        """
        ...

    @overload
    def astype(self, /, dtype: Type[int]):
        """
        usage.dask: 3
        usage.seaborn: 1
        usage.statsmodels: 4
        usage.xarray: 1
        """
        ...

    @overload
    def astype(self, /, dtype: Type[float]):
        """
        usage.dask: 5
        usage.prophet: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    def astype(self, /, dtype: Literal["category"]):
        """
        usage.dask: 17
        usage.seaborn: 5
        usage.sklearn: 2
        usage.statsmodels: 1
        """
        ...

    @overload
    def astype(self, /, dtype: Literal["int32"]):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def astype(self, /, dtype: Type[numpy.int64]):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def astype(self, /, dtype: Literal["bool"]):
        """
        usage.prophet: 1
        """
        ...

    @overload
    def astype(self, /, dtype: Type[object]):
        """
        usage.geopandas: 1
        usage.seaborn: 2
        """
        ...

    @overload
    def astype(self, /, dtype: Type[str]):
        """
        usage.dask: 3
        usage.seaborn: 2
        """
        ...

    @overload
    def astype(self, /, dtype: Literal["int64"]):
        """
        usage.dask: 2
        usage.geopandas: 1
        """
        ...

    @overload
    def astype(self, /, dtype: Literal["geometry"]):
        """
        usage.geopandas: 1
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
    def astype(self, /, dtype: pandas.core.dtypes.dtypes.CategoricalDtype):
        """
        usage.dask: 2
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
            pandas.core.dtypes.dtypes.CategoricalDtype, numpy.dtype, str, type
        ],
        copy: bool = ...,
    ):
        """
        usage.dask: 53
        usage.geopandas: 5
        usage.koalas: 6
        usage.prophet: 2
        usage.seaborn: 10
        usage.sklearn: 10
        usage.statsmodels: 9
        usage.xarray: 1
        """
        ...

    def autocorr(self, /, lag: int):
        """
        usage.dask: 4
        """
        ...

    @overload
    def between(self, /, left: numpy.float64, right: numpy.float64):
        """
        usage.koalas: 1
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

    def between(
        self,
        /,
        left: Union[int, numpy.float64],
        right: Union[int, numpy.float64],
        inclusive: bool = ...,
    ):
        """
        usage.dask: 2
        usage.koalas: 1
        """
        ...

    @overload
    def bfill(self, /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def bfill(self, /, inplace: bool):
        """
        usage.koalas: 1
        """
        ...

    def bfill(self, /, inplace: bool = ...):
        """
        usage.koalas: 3
        """
        ...

    @overload
    def clip(self, /, lower: int, upper: int):
        """
        usage.dask: 3
        usage.koalas: 2
        """
        ...

    @overload
    def clip(self, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def clip(self, /, lower: int):
        """
        usage.dask: 1
        usage.koalas: 1
        """
        ...

    @overload
    def clip(self, /, upper: int):
        """
        usage.dask: 1
        usage.koalas: 1
        """
        ...

    @overload
    def clip(self, /, lower: int, upper: None):
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
        lower: Union[float, int, None] = ...,
        upper: Union[None, int, float] = ...,
    ):
        """
        usage.dask: 13
        usage.koalas: 5
        """
        ...

    @overload
    def combine(self, /, other: shapely.geometry.point.Point, func: Callable):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def combine(self, /, other: shapely.geometry.point.Point, func: Callable):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def combine(self, /, other: pandas.core.series.Series, func: Callable):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def combine(self, /, other: pandas.core.series.Series, func: Callable):
        """
        usage.geopandas: 1
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
        other: Union[pandas.core.series.Series, shapely.geometry.point.Point],
        func: Callable,
        fill_value: Union[None, int] = ...,
    ):
        """
        usage.dask: 6
        usage.geopandas: 4
        """
        ...

    def combine_first(self, /, other: pandas.core.series.Series):
        """
        usage.dask: 5
        usage.koalas: 5
        """
        ...

    def copy(self, /):
        """
        usage.dask: 3
        usage.koalas: 2
        usage.modin: 1
        usage.seaborn: 1
        usage.statsmodels: 94
        """
        ...

    def corr(self, /, other: pandas.core.series.Series):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def count(self, /):
        """
        usage.dask: 9
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
        usage.dask: 11
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
        usage.koalas: 3
        """
        ...

    @overload
    def cummax(self, /, skipna: bool):
        """
        usage.koalas: 2
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
        usage.koalas: 5
        """
        ...

    @overload
    def cummin(self, /):
        """
        usage.dask: 3
        usage.koalas: 3
        """
        ...

    @overload
    def cummin(self, /, skipna: bool):
        """
        usage.koalas: 2
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
        usage.koalas: 5
        """
        ...

    @overload
    def cumprod(self, /):
        """
        usage.dask: 3
        usage.koalas: 3
        """
        ...

    @overload
    def cumprod(self, /, skipna: bool):
        """
        usage.koalas: 2
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
        usage.koalas: 5
        """
        ...

    @overload
    def cumsum(self, /):
        """
        usage.dask: 4
        usage.koalas: 3
        usage.statsmodels: 1
        """
        ...

    @overload
    def cumsum(self, /, skipna: bool):
        """
        usage.koalas: 2
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
        usage.koalas: 5
        usage.statsmodels: 1
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
    def diff(self, /):
        """
        usage.dask: 3
        usage.prophet: 3
        usage.seaborn: 1
        usage.statsmodels: 33
        """
        ...

    @overload
    def diff(self, /, periods: int):
        """
        usage.dask: 4
        usage.statsmodels: 1
        """
        ...

    def diff(self, /, periods: int = ...):
        """
        usage.dask: 7
        usage.prophet: 3
        usage.seaborn: 1
        usage.statsmodels: 34
        """
        ...

    def divmod(self, /, other: int):
        """
        usage.koalas: 2
        """
        ...

    def dot(self, /, other: pandas.core.series.Series):
        """
        usage.koalas: 3
        """
        ...

    def drop(self, /, labels: Literal["initial_level"]):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def drop_duplicates(self, /):
        """
        usage.dask: 6
        usage.koalas: 1
        usage.statsmodels: 4
        """
        ...

    @overload
    def drop_duplicates(self, /, keep: Literal["last"]):
        """
        usage.dask: 3
        usage.koalas: 2
        """
        ...

    @overload
    def drop_duplicates(self, /, keep: bool, inplace: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def drop_duplicates(self, /, keep: Literal["first"]):
        """
        usage.dask: 3
        usage.koalas: 1
        """
        ...

    @overload
    def drop_duplicates(self, /, keep: bool):
        """
        usage.koalas: 1
        """
        ...

    def drop_duplicates(
        self, /, keep: Union[Literal["last", "first"], bool] = ..., inplace: bool = ...
    ):
        """
        usage.dask: 12
        usage.koalas: 6
        usage.statsmodels: 4
        """
        ...

    @overload
    def droplevel(self, /, level: int):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def droplevel(self, /, level: Literal["level_1"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def droplevel(self, /, level: List[int]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def droplevel(self, /, level: List[Literal["level_1"]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def droplevel(self, /, level: Tuple[int]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def droplevel(self, /, level: Tuple[Literal["level_1"]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def droplevel(self, /, level: List[Literal["level_3", "level_1"]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def droplevel(self, /, level: Tuple[int, int]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def droplevel(self, /, level: Tuple[Literal["level_2"], Literal["level_3"]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def droplevel(self, /, level: List[Tuple[Literal["a", "c"], Literal["1", "3"]]]):
        """
        usage.koalas: 1
        """
        ...

    def droplevel(
        self,
        /,
        level: Union[
            List[
                Union[
                    Literal["level_1", "level_3"],
                    int,
                    Tuple[Literal["a", "c"], Literal["1", "3"]],
                ]
            ],
            int,
            Literal["level_1"],
            Tuple[Union[Literal["level_1", "level_3", "level_2"], int], ...],
        ],
    ):
        """
        usage.koalas: 12
        """
        ...

    @overload
    def dropna(self, /):
        """
        usage.dask: 7
        usage.geopandas: 1
        usage.koalas: 3
        usage.seaborn: 1
        usage.statsmodels: 17
        usage.xarray: 2
        """
        ...

    @overload
    def dropna(self, /, inplace: bool):
        """
        usage.koalas: 1
        """
        ...

    def dropna(self, /, inplace: bool = ...):
        """
        usage.dask: 7
        usage.geopandas: 1
        usage.koalas: 4
        usage.seaborn: 1
        usage.statsmodels: 17
        usage.xarray: 2
        """
        ...

    @overload
    def duplicated(self, /, keep: Literal["last"]):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def duplicated(self, /):
        """
        usage.statsmodels: 1
        """
        ...

    def duplicated(self, /, keep: Literal["last"] = ...):
        """
        usage.statsmodels: 1
        usage.xarray: 1
        """
        ...

    @overload
    def eq(self, /, other: Literal["MultiPolygon"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def eq(self, /, other: pandas.core.series.Series, fill_value: int):
        """
        usage.dask: 1
        """
        ...

    def eq(
        self,
        /,
        other: Union[pandas.core.series.Series, Literal["MultiPolygon"]],
        fill_value: int = ...,
    ):
        """
        usage.dask: 1
        usage.geopandas: 1
        """
        ...

    def equals(self, /, other: pandas.core.series.Series):
        """
        usage.dask: 3
        usage.statsmodels: 1
        usage.xarray: 8
        """
        ...

    def expanding(self, /, min_periods: int):
        """
        usage.koalas: 3
        """
        ...

    def explode(self, /):
        """
        usage.dask: 5
        """
        ...

    @overload
    def ffill(self, /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def ffill(self, /, inplace: bool):
        """
        usage.koalas: 1
        """
        ...

    def ffill(self, /, inplace: bool = ...):
        """
        usage.koalas: 3
        """
        ...

    @overload
    def fillna(self, /, value: int):
        """
        usage.dask: 1
        usage.koalas: 3
        usage.statsmodels: 2
        """
        ...

    @overload
    def fillna(self, /, value: float):
        """
        usage.koalas: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    def fillna(self, /, value: int, inplace: bool):
        """
        usage.koalas: 3
        """
        ...

    @overload
    def fillna(self, /, method: Literal["ffill"]):
        """
        usage.dask: 1
        usage.koalas: 1
        """
        ...

    @overload
    def fillna(self, /, method: Literal["bfill"]):
        """
        usage.dask: 2
        usage.koalas: 1
        """
        ...

    @overload
    def fillna(self, /, value: numpy.float64, inplace: bool):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def fillna(self, /, value: numpy.int32, inplace: bool):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def fillna(self, /, value: Literal["white"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def fillna(self, /, value: shapely.geometry.point.Point):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def fillna(self, /, value: int, method: None, axis: int, limit: None):
        """
        usage.dask: 2
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
        value: object = ...,
        method: Union[Literal["bfill", "ffill", "pad"], None] = ...,
        axis: int = ...,
        limit: Union[None, int] = ...,
    ):
        """
        usage.dask: 23
        usage.geopandas: 1
        usage.koalas: 9
        usage.seaborn: 1
        usage.statsmodels: 5
        """
        ...

    @overload
    def filter(self, /, items: List[Literal["three", "one"]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def filter(self, /, regex: Literal["e$"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def filter(self, /, like: Literal["hre"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def filter(self, /, items: List[Tuple[Literal["one", "three"], Literal["x", "z"]]]):
        """
        usage.koalas: 1
        """
        ...

    def filter(
        self,
        /,
        regex: Literal["e$"] = ...,
        items: List[
            Union[
                Literal["three", "one"],
                Tuple[Literal["one", "three"], Literal["x", "z"]],
            ]
        ] = ...,
        like: Literal["hre"] = ...,
    ):
        """
        usage.koalas: 4
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

    def first_valid_index(self, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def floordiv(self, /, other: int):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def floordiv(self, /, other: float):
        """
        usage.koalas: 1
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
        self,
        /,
        other: Union[pandas.core.series.Series, int, float],
        fill_value: int = ...,
    ):
        """
        usage.dask: 2
        usage.koalas: 2
        """
        ...

    def ge(self, /, other: pandas.core.series.Series, fill_value: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def get(self, /, key: Literal["lower_window"], default: int):
        """
        usage.prophet: 1
        """
        ...

    @overload
    def get(self, /, key: Literal["upper_window"], default: int):
        """
        usage.prophet: 1
        """
        ...

    @overload
    def get(self, /, key: Literal["prior_scale"], default: float):
        """
        usage.prophet: 1
        """
        ...

    def get(
        self,
        /,
        key: Literal["prior_scale", "upper_window", "lower_window"],
        default: Union[float, int],
    ):
        """
        usage.prophet: 3
        """
        ...

    @overload
    def groupby(self, /, by: pandas.core.series.Series):
        """
        usage.dask: 20
        usage.koalas: 72
        usage.seaborn: 14
        """
        ...

    @overload
    def groupby(self, /, by: pandas.core.series.Series, axis: int):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def groupby(self, /, by: pandas.core.series.Series, axis: Literal["index"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def groupby(self, /, by: pandas.core.resample.TimeGrouper):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def groupby(self, /, by: numpy.ndarray):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["b", "a"]]):
        """
        usage.seaborn: 2
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["d", "c", "b", "a"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def groupby(self, /, by: pandas.core.series.Series, sort: bool):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def groupby(self, /, by: pandas.core.arrays.categorical.Categorical, sort: bool):
        """
        usage.seaborn: 1
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
        usage.koalas: 74
        usage.seaborn: 19
        usage.statsmodels: 1
        usage.xarray: 1
        """
        ...

    def gt(self, /, other: pandas.core.series.Series, fill_value: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def head(self, /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def head(self, /, n: int):
        """
        usage.dask: 7
        usage.koalas: 4
        """
        ...

    def head(self, /, n: int = ...):
        """
        usage.dask: 7
        usage.koalas: 6
        """
        ...

    @overload
    def idxmax(self, /):
        """
        usage.dask: 2
        usage.koalas: 3
        usage.prophet: 2
        usage.seaborn: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    def idxmax(self, /, skipna: bool):
        """
        usage.dask: 4
        usage.koalas: 3
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

    def idxmax(self, /, skipna: bool = ..., axis: int = ...):
        """
        usage.dask: 8
        usage.koalas: 6
        usage.prophet: 2
        usage.seaborn: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    def idxmin(self, /):
        """
        usage.koalas: 3
        usage.prophet: 2
        usage.statsmodels: 1
        """
        ...

    @overload
    def idxmin(self, /, skipna: bool):
        """
        usage.dask: 4
        usage.koalas: 3
        """
        ...

    def idxmin(self, /, skipna: bool = ...):
        """
        usage.dask: 4
        usage.koalas: 6
        usage.prophet: 2
        usage.statsmodels: 1
        """
        ...

    def infer_objects(self, /):
        """
        usage.seaborn: 2
        """
        ...

    @overload
    def isin(self, /, values: List[Literal["lama", "cow"]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def isin(self, /, values: set):
        """
        usage.koalas: 1
        usage.prophet: 1
        """
        ...

    @overload
    def isin(self, /, values: List[bool]):
        """
        usage.prophet: 1
        """
        ...

    @overload
    def isin(self, /, values: pandas.core.series.Series):
        """
        usage.dask: 3
        usage.prophet: 2
        """
        ...

    @overload
    def isin(self, /, values: List[int]):
        """
        usage.dask: 3
        """
        ...

    def isin(
        self,
        /,
        values: Union[
            List[Union[bool, int, Literal["lama", "cow"]]],
            pandas.core.series.Series,
            set,
        ],
    ):
        """
        usage.dask: 6
        usage.koalas: 2
        usage.prophet: 4
        """
        ...

    def isna(self, /):
        """
        usage.seaborn: 1
        """
        ...

    def isnull(self, /):
        """
        usage.dask: 5
        usage.koalas: 8
        usage.prophet: 2
        usage.seaborn: 3
        usage.statsmodels: 1
        usage.xarray: 1
        """
        ...

    def item(self, /):
        """
        usage.koalas: 1
        """
        ...

    def items(self, /):
        """
        usage.dask: 1
        usage.geopandas: 1
        usage.koalas: 1
        usage.statsmodels: 2
        """
        ...

    def iteritems(self, /):
        """
        usage.dask: 4
        usage.geopandas: 1
        usage.koalas: 1
        usage.xarray: 1
        """
        ...

    def keys(self, /):
        """
        usage.koalas: 1
        usage.statsmodels: 1
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

    def last_valid_index(self, /):
        """
        usage.koalas: 3
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

    def mad(self, /):
        """
        usage.koalas: 4
        """
        ...

    @overload
    def map(self, /, arg: dict):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def map(self, /, arg: collections.defaultdict):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def map(self, /, arg: Callable):
        """
        usage.dask: 2
        usage.koalas: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    def map(
        self,
        /,
        arg: Dict[Literal["virginica", "versicolor", "setosa"], Literal["g", "b", "r"]],
    ):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def map(self, /, arg: Callable, na_action: None):
        """
        usage.dask: 3
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
        arg: Union[pandas.core.series.Series, collections.defaultdict, dict, Callable],
        na_action: None = ...,
    ):
        """
        usage.dask: 16
        usage.koalas: 3
        usage.seaborn: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    def mask(self, /, cond: pandas.core.series.Series):
        """
        usage.dask: 1
        usage.koalas: 1
        """
        ...

    @overload
    def mask(self, /, cond: pandas.core.series.Series, other: float):
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
        usage.koalas: 1
        """
        ...

    @overload
    def max(self, /):
        """
        usage.dask: 11
        usage.geopandas: 2
        usage.koalas: 3
        usage.prophet: 11
        usage.seaborn: 8
        usage.statsmodels: 2
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
        usage.geopandas: 2
        usage.koalas: 3
        usage.prophet: 11
        usage.seaborn: 8
        usage.statsmodels: 2
        usage.xarray: 1
        """
        ...

    @overload
    def mean(self, /):
        """
        usage.dask: 17
        usage.koalas: 8
        usage.prophet: 2
        usage.seaborn: 2
        usage.statsmodels: 12
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
    def mean(self, /, axis: int):
        """
        usage.dask: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    def mean(self, /, axis: int, skipna: bool):
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

    def mean(self, /, axis: Union[int, Literal["columns"]] = ..., skipna: bool = ...):
        """
        usage.dask: 22
        usage.koalas: 8
        usage.prophet: 2
        usage.seaborn: 2
        usage.statsmodels: 13
        usage.xarray: 1
        """
        ...

    def median(self, /):
        """
        usage.koalas: 1
        usage.prophet: 1
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
    def min(self, /):
        """
        usage.dask: 7
        usage.geopandas: 2
        usage.koalas: 52
        usage.prophet: 12
        usage.seaborn: 11
        usage.statsmodels: 5
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
        usage.geopandas: 2
        usage.koalas: 52
        usage.prophet: 12
        usage.seaborn: 11
        usage.statsmodels: 5
        usage.xarray: 1
        """
        ...

    @overload
    def mod(self, /, other: pandas.core.series.Series):
        """
        usage.koalas: 4
        """
        ...

    @overload
    def mod(self, /, other: int):
        """
        usage.koalas: 3
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

    def mod(
        self, /, other: Union[pandas.core.series.Series, int], fill_value: int = ...
    ):
        """
        usage.dask: 2
        usage.koalas: 7
        """
        ...

    def mode(self, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def mul(self, /, other: pandas.core.series.Series, level: int):
        """
        usage.statsmodels: 1
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
        self,
        /,
        other: Union[int, pandas.core.series.Series],
        level: int = ...,
        fill_value: int = ...,
    ):
        """
        usage.dask: 4
        usage.statsmodels: 1
        """
        ...

    def ne(self, /, other: pandas.core.series.Series, fill_value: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def nlargest(self, /, n: int):
        """
        usage.dask: 4
        usage.koalas: 1
        """
        ...

    @overload
    def nlargest(self, /):
        """
        usage.koalas: 2
        """
        ...

    def nlargest(self, /, n: int = ...):
        """
        usage.dask: 4
        usage.koalas: 3
        """
        ...

    def notna(self, /):
        """
        usage.dask: 1
        usage.seaborn: 5
        """
        ...

    def notnull(self, /):
        """
        usage.dask: 3
        usage.koalas: 2
        usage.prophet: 1
        usage.seaborn: 5
        usage.statsmodels: 1
        """
        ...

    @overload
    def nsmallest(self, /, n: int):
        """
        usage.dask: 2
        usage.koalas: 1
        """
        ...

    @overload
    def nsmallest(self, /):
        """
        usage.koalas: 2
        """
        ...

    def nsmallest(self, /, n: int = ...):
        """
        usage.dask: 2
        usage.koalas: 3
        """
        ...

    @overload
    def nunique(self, /):
        """
        usage.dask: 5
        usage.koalas: 1
        """
        ...

    @overload
    def nunique(self, /, dropna: bool):
        """
        usage.koalas: 1
        """
        ...

    def nunique(self, /, dropna: bool = ...):
        """
        usage.dask: 5
        usage.koalas: 2
        """
        ...

    @overload
    def pct_change(self, /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def pct_change(self, /, periods: int):
        """
        usage.koalas: 8
        """
        ...

    def pct_change(self, /, periods: int = ...):
        """
        usage.koalas: 10
        """
        ...

    def pop(self, /, item: Tuple[Literal["lama"], Literal["speed"]]):
        """
        usage.koalas: 1
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
    def prod(self, /):
        """
        usage.dask: 2
        usage.koalas: 7
        """
        ...

    @overload
    def prod(self, /, min_count: int):
        """
        usage.koalas: 6
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
        usage.koalas: 13
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

    @overload
    def rank(self, /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def rank(self, /, ascending: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def rank(self, /, method: Literal["min"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def rank(self, /, method: Literal["max"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def rank(self, /, method: Literal["first"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def rank(self, /, method: Literal["dense"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def rank(self, /, method: Literal["dense"], ascending: bool):
        """
        usage.xarray: 1
        """
        ...

    def rank(
        self,
        /,
        method: Literal["dense", "first", "max", "min"] = ...,
        ascending: bool = ...,
    ):
        """
        usage.koalas: 7
        usage.xarray: 1
        """
        ...

    def ravel(self, /):
        """
        usage.statsmodels: 1
        """
        ...

    def rdivmod(self, /, other: int):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def reindex(self, /, index: pandas.core.indexes.range.RangeIndex):
        """
        usage.seaborn: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    def reindex(self, /, index: pandas.core.indexes.multi.MultiIndex):
        """
        usage.dask: 3
        usage.statsmodels: 1
        """
        ...

    @overload
    def reindex(self, /, index: pandas.core.indexes.base.Index):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def reindex(self, /, index: pandas.core.indexes.numeric.Int64Index):
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

    def reindex(self, /, index: object):
        """
        usage.dask: 8
        usage.seaborn: 1
        usage.statsmodels: 3
        """
        ...

    @overload
    def rename(self, /, index: Literal["A"]):
        """
        usage.dask: 1
        usage.koalas: 1
        """
        ...

    @overload
    def rename(self, /, index: Literal["b"]):
        """
        usage.dask: 1
        usage.koalas: 1
        """
        ...

    @overload
    def rename(self, /, index: Literal["a"]):
        """
        usage.dask: 1
        usage.koalas: 13
        usage.seaborn: 1
        """
        ...

    @overload
    def rename(self, /):
        """
        usage.dask: 1
        usage.koalas: 54
        """
        ...

    @overload
    def rename(self, /, index: None):
        """
        usage.dask: 1
        usage.koalas: 1
        usage.seaborn: 1
        """
        ...

    @overload
    def rename(self, /, index: Tuple[Literal["x"], Literal["b"]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def rename(self, /, index: Tuple[Literal["x"], Literal["a"]]):
        """
        usage.koalas: 5
        """
        ...

    @overload
    def rename(self, /, index: Literal["d"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def rename(self, /, index: Literal["car_id"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def rename(self, /, index: Literal["B"]):
        """
        usage.dask: 1
        usage.koalas: 1
        """
        ...

    @overload
    def rename(self, /, index: Literal["ABC"]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def rename(self, /, index: Literal["c"]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def rename(self, /, index: Literal["left"]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def rename(self, /, index: Literal["y"]):
        """
        usage.dask: 2
        usage.koalas: 3
        usage.seaborn: 1
        """
        ...

    @overload
    def rename(self, /, index: Literal["z"], *, inplace: bool):
        """
        usage.dask: 1
        usage.koalas: 1
        """
        ...

    @overload
    def rename(self, /, index: Literal["end_date"]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def rename(self, /, index: Literal["col1"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def rename(self, /, index: Literal["col2"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def rename(self, /, index: Literal["count"]):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def rename(self, /, index: Literal["weight"]):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def rename(self, /, index: Literal["estimate (prev)"]):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def rename(self, /, index: Literal["impact of revisions"]):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def rename(self, /, index: Literal["impact of news"]):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def rename(self, /, index: Literal["estimate (new)"]):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def rename(self, /, index: Literal["heights"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def rename(self, /, index: Literal["x"]):
        """
        usage.seaborn: 1
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
    def rename(self, /, index: Literal["AA"]):
        """
        usage.dask: 1
        """
        ...

    def rename(
        self,
        /,
        index: Union[
            Callable,
            None,
            pandas.core.series.Series,
            str,
            Tuple[Literal["x"], Literal["b", "a"]],
        ] = ...,
        *,
        inplace: bool = ...,
    ):
        """
        usage.dask: 25
        usage.koalas: 93
        usage.seaborn: 5
        usage.statsmodels: 7
        """
        ...

    @overload
    def repeat(self, /, repeats: pandas.core.series.Series):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def repeat(self, /, repeats: int):
        """
        usage.koalas: 2
        """
        ...

    def repeat(self, /, repeats: Union[int, pandas.core.series.Series]):
        """
        usage.koalas: 4
        """
        ...

    @overload
    def replace(self, /, to_replace: Dict[float, None]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def replace(self, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def replace(self, /, to_replace: dict):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def replace(self, /, to_replace: Dict[int, str]):
        """
        usage.statsmodels: 2
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

    def replace(self, /, value: Union[None, float, int] = ..., regex: bool = ...):
        """
        usage.dask: 5
        usage.koalas: 4
        usage.statsmodels: 2
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
    def resample(self, /, rule: Literal["M"], convention: Literal["end"]):
        """
        usage.statsmodels: 1
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
        usage.statsmodels: 1
        usage.xarray: 14
        """
        ...

    @overload
    def reset_index(self, /):
        """
        usage.dask: 1
        usage.koalas: 8
        usage.prophet: 1
        usage.seaborn: 1
        usage.statsmodels: 2
        """
        ...

    @overload
    def reset_index(self, /, name: Literal["values"]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def reset_index(self, /, drop: bool):
        """
        usage.dask: 6
        usage.koalas: 6
        """
        ...

    @overload
    def reset_index(self, /, drop: bool, inplace: bool):
        """
        usage.koalas: 3
        """
        ...

    @overload
    def reset_index(self, /, level: int):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def reset_index(self, /, level: List[int]):
        """
        usage.koalas: 1
        usage.statsmodels: 4
        """
        ...

    @overload
    def reset_index(self, /, name: Literal["s"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def reset_index(self, /, drop: bool, name: Literal["s"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def reset_index(self, /, inplace: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def reset_index(self, /, name: Literal["heights"]):
        """
        usage.seaborn: 1
        """
        ...

    def reset_index(
        self,
        /,
        drop: bool = ...,
        name: Literal["heights", "s", "values"] = ...,
        inplace: bool = ...,
    ):
        """
        usage.dask: 7
        usage.koalas: 24
        usage.prophet: 1
        usage.seaborn: 2
        usage.statsmodels: 6
        """
        ...

    @overload
    def rmod(self, /, other: pandas.core.series.Series):
        """
        usage.koalas: 4
        """
        ...

    @overload
    def rmod(self, /, other: int):
        """
        usage.koalas: 3
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

    def rmod(
        self, /, other: Union[pandas.core.series.Series, int], fill_value: int = ...
    ):
        """
        usage.dask: 2
        usage.koalas: 7
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
    def rolling(self, /, window: int):
        """
        usage.dask: 2
        usage.koalas: 3
        usage.statsmodels: 2
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
        usage.statsmodels: 1
        """
        ...

    @overload
    def rolling(self, /, window: Literal["2D"]):
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
            Literal["3S", "2S", "1S", "2D"], int, pandas._libs.tslibs.offsets.Second
        ],
        min_periods: Union[None, int] = ...,
        center: bool = ...,
        win_type: None = ...,
        axis: int = ...,
    ):
        """
        usage.dask: 19
        usage.koalas: 3
        usage.statsmodels: 3
        usage.xarray: 3
        """
        ...

    @overload
    def round(self, /, decimals: int):
        """
        usage.dask: 1
        usage.koalas: 1
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
        usage.koalas: 1
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
    def shift(self, /, periods: int, fill_value: int):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def shift(self, /, periods: int):
        """
        usage.dask: 6
        usage.statsmodels: 5
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
        usage.koalas: 1
        usage.statsmodels: 5
        usage.xarray: 1
        """
        ...

    @overload
    def sort_index(self, /):
        """
        usage.dask: 3
        usage.koalas: 247
        usage.seaborn: 1
        usage.statsmodels: 4
        """
        ...

    @overload
    def sort_index(self, /, ascending: bool):
        """
        usage.dask: 1
        usage.koalas: 1
        """
        ...

    @overload
    def sort_index(self, /, na_position: Literal["first"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def sort_index(self, /, inplace: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def sort_index(self, /, level: List[int]):
        """
        usage.koalas: 1
        """
        ...

    def sort_index(
        self,
        /,
        ascending: bool = ...,
        na_position: Literal["first"] = ...,
        inplace: bool = ...,
        level: List[int] = ...,
    ):
        """
        usage.dask: 4
        usage.koalas: 251
        usage.seaborn: 1
        usage.statsmodels: 4
        """
        ...

    @overload
    def sort_values(self, /):
        """
        usage.dask: 4
        usage.koalas: 11
        usage.prophet: 1
        """
        ...

    @overload
    def sort_values(self, /, ascending: bool):
        """
        usage.dask: 1
        usage.koalas: 1
        """
        ...

    @overload
    def sort_values(self, /, na_position: Literal["first"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def sort_values(self, /, inplace: bool):
        """
        usage.koalas: 1
        """
        ...

    def sort_values(
        self,
        /,
        ascending: bool = ...,
        na_position: Literal["first"] = ...,
        inplace: bool = ...,
    ):
        """
        usage.dask: 5
        usage.koalas: 14
        usage.prophet: 1
        """
        ...

    @overload
    def squeeze(self, /):
        """
        usage.dask: 1
        usage.koalas: 4
        usage.statsmodels: 4
        """
        ...

    @overload
    def squeeze(self, /, axis: int):
        """
        usage.modin: 1
        """
        ...

    def squeeze(self, /, axis: int = ...):
        """
        usage.dask: 1
        usage.koalas: 4
        usage.modin: 1
        usage.statsmodels: 4
        """
        ...

    @overload
    def std(self, /):
        """
        usage.dask: 3
        usage.koalas: 3
        usage.prophet: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    def std(self, /, ddof: int):
        """
        usage.dask: 1
        usage.seaborn: 1
        """
        ...

    @overload
    def std(self, /, axis: int, skipna: bool):
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
        usage.koalas: 3
        usage.prophet: 1
        usage.seaborn: 1
        usage.statsmodels: 1
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
    def sum(self, /):
        """
        usage.dask: 35
        usage.koalas: 11
        usage.prophet: 3
        usage.seaborn: 3
        usage.sklearn: 1
        usage.statsmodels: 5
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
        usage.dask: 41
        usage.koalas: 11
        usage.prophet: 3
        usage.seaborn: 3
        usage.sklearn: 1
        usage.statsmodels: 5
        usage.xarray: 2
        """
        ...

    @overload
    def tail(self, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def tail(self, /, n: int):
        """
        usage.dask: 4
        usage.koalas: 5
        usage.prophet: 4
        """
        ...

    def tail(self, /, n: int = ...):
        """
        usage.dask: 4
        usage.koalas: 6
        usage.prophet: 4
        """
        ...

    @overload
    def take(self, /, indices: List[int]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def take(self, /, indices: range):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def take(self, /, indices: numpy.ndarray):
        """
        usage.dask: 1
        """
        ...

    def take(self, /, indices: Union[numpy.ndarray, range, List[int]]):
        """
        usage.dask: 1
        usage.koalas: 4
        """
        ...

    @overload
    def to_csv(
        self,
        /,
        path_or_buf: None,
        sep: Literal[","],
        na_rep: Literal[""],
        columns: None,
        header: bool,
        index: bool,
        quotechar: Literal['"'],
        date_format: None,
        escapechar: None,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def to_csv(self, /, header: bool, index: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def to_csv(
        self,
        /,
        path_or_buf: None,
        sep: Literal[","],
        na_rep: Literal["null"],
        columns: None,
        header: bool,
        index: bool,
        quotechar: Literal['"'],
        date_format: None,
        escapechar: None,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def to_csv(self, /, na_rep: Literal["null"], header: bool, index: bool):
        """
        usage.koalas: 1
        """
        ...

    def to_csv(
        self,
        /,
        header: bool,
        index: bool,
        path_or_buf: None = ...,
        sep: Literal[","] = ...,
        na_rep: Literal["null", ""] = ...,
        columns: None = ...,
        quotechar: Literal['"'] = ...,
        date_format: None = ...,
        escapechar: None = ...,
    ):
        """
        usage.koalas: 4
        """
        ...

    def to_dict(self, /):
        """
        usage.dask: 5
        usage.koalas: 1
        usage.statsmodels: 3
        """
        ...

    @overload
    def to_frame(self, /):
        """
        usage.dask: 12
        usage.koalas: 5
        usage.sklearn: 2
        usage.statsmodels: 6
        usage.xarray: 2
        """
        ...

    @overload
    def to_frame(self, /, name: Literal["a"]):
        """
        usage.dask: 3
        usage.koalas: 2
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

    def to_frame(
        self, /, name: Union[None, Literal["a", "A", "__series__", "bar", "s"]] = ...
    ):
        """
        usage.dask: 27
        usage.koalas: 7
        usage.sklearn: 2
        usage.statsmodels: 6
        usage.xarray: 2
        """
        ...

    def to_markdown(self, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def to_string(self, /, dtype: numpy.dtype, name: None):
        """
        usage.koalas: 7
        """
        ...

    @overload
    def to_string(self, /, dtype: numpy.dtype, name: Literal["B"]):
        """
        usage.koalas: 3
        """
        ...

    @overload
    def to_string(self, /, dtype: numpy.dtype, name: Literal["A"]):
        """
        usage.koalas: 3
        """
        ...

    @overload
    def to_string(self, /, dtype: numpy.dtype, name: Literal["animal"]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def to_string(self, /, dtype: numpy.dtype, name: Literal["Col1"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def to_string(self, /, dtype: numpy.dtype, name: Literal["Col2"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def to_string(self, /, dtype: numpy.dtype, name: Literal["x"]):
        """
        usage.koalas: 3
        """
        ...

    @overload
    def to_string(self, /, dtype: numpy.dtype, name: Literal["koalas"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def to_string(self, /, dtype: numpy.dtype, name: Literal["dates"]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def to_string(self, /, dtype: numpy.dtype, name: Literal["id"]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def to_string(
        self, /, dtype: numpy.dtype, name: Tuple[Literal["num"], Literal["b"]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def to_string(self, /, dtype: numpy.dtype, name: Literal["numeric1"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def to_string(self, /, dtype: numpy.dtype, name: Literal["one"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def to_string(self, /, dtype: numpy.dtype, name: Literal["class"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def to_string(self, /, dtype: numpy.dtype, name: Literal["0.5"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def to_string(self, /, dtype: numpy.dtype, name: Literal["b"]):
        """
        usage.koalas: 3
        """
        ...

    @overload
    def to_string(self, /, dtype: numpy.dtype, name: Literal["shield"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def to_string(self, /, dtype: numpy.dtype, name: Literal["max_speed"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def to_string(self, /, dtype: numpy.dtype, name: Literal["value"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def to_string(self, /, dtype: numpy.dtype, name: Literal["a"]):
        """
        usage.koalas: 3
        """
        ...

    @overload
    def to_string(self, /, dtype: numpy.dtype, name: Literal["1"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def to_string(self, /, dtype: numpy.dtype, name: Literal["C"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def to_string(self, /, dtype: numpy.dtype, name: Literal["value1"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def to_string(self, /, dtype: numpy.dtype, name: Literal["c"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def to_string(self, /, dtype: numpy.dtype, name: Literal["my_name"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def to_string(self, /, dtype: numpy.dtype, name: Literal["0"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def to_string(self, /, dtype: numpy.dtype, name: Tuple[Literal["x"], Literal["a"]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def to_string(self, /, dtype: numpy.dtype, name: Literal["species"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def to_string(self, /, dtype: numpy.dtype, name: Literal["population"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def to_string(self, /, dtype: numpy.dtype, name: Literal["Koalas"]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def to_string(self, /, length: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def to_string(self, /, max_rows: int):
        """
        usage.dask: 1
        """
        ...

    def to_string(
        self,
        /,
        dtype: numpy.dtype = ...,
        name: Union[str, Tuple[Literal["num", "x"], Literal["b", "a"]], None] = ...,
    ):
        """
        usage.dask: 1
        usage.koalas: 51
        """
        ...

    def to_timestamp(self, /, freq: Literal["Q"]):
        """
        usage.statsmodels: 1
        """
        ...

    def tolist(self, /):
        """
        usage.dask: 4
        usage.geopandas: 5
        usage.koalas: 2
        usage.prophet: 1
        usage.seaborn: 6
        usage.statsmodels: 9
        """
        ...

    def transform(self, /, func: Callable):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def truediv(self, /, other: int):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def truediv(self, /, other: float):
        """
        usage.koalas: 2
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

    def truediv(
        self,
        /,
        other: Union[pandas.core.series.Series, int, float],
        fill_value: int = ...,
    ):
        """
        usage.dask: 6
        usage.koalas: 4
        """
        ...

    @overload
    def truncate(self, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def truncate(self, /, before: int):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def truncate(self, /, after: int):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def truncate(self, /, copy: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def truncate(self, /, before: int, after: int, copy: bool):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def truncate(self, /, before: int, after: int):
        """
        usage.koalas: 1
        """
        ...

    def truncate(self, /, before: int = ..., after: int = ..., copy: bool = ...):
        """
        usage.koalas: 7
        """
        ...

    def unique(self, /):
        """
        usage.dask: 9
        usage.geopandas: 2
        usage.prophet: 8
        usage.seaborn: 63
        usage.statsmodels: 1
        """
        ...

    @overload
    def unstack(self, /, level: int):
        """
        usage.koalas: 2
        usage.statsmodels: 2
        """
        ...

    @overload
    def unstack(self, /):
        """
        usage.seaborn: 1
        usage.xarray: 1
        """
        ...

    @overload
    def unstack(self, /, level: List[int]):
        """
        usage.statsmodels: 4
        """
        ...

    def unstack(self, /, level: Union[List[int], int] = ...):
        """
        usage.koalas: 2
        usage.seaborn: 1
        usage.statsmodels: 6
        usage.xarray: 1
        """
        ...

    def update(self, /, other: pandas.core.series.Series):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def value_counts(self, /):
        """
        usage.dask: 8
        usage.koalas: 2
        usage.statsmodels: 1
        """
        ...

    @overload
    def value_counts(self, /, normalize: bool):
        """
        usage.koalas: 6
        usage.statsmodels: 1
        """
        ...

    @overload
    def value_counts(self, /, ascending: bool):
        """
        usage.dask: 1
        usage.koalas: 6
        """
        ...

    @overload
    def value_counts(self, /, normalize: bool, dropna: bool):
        """
        usage.koalas: 6
        """
        ...

    @overload
    def value_counts(self, /, ascending: bool, dropna: bool):
        """
        usage.dask: 1
        usage.koalas: 6
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

    def value_counts(
        self, /, ascending: bool = ..., normalize: bool = ..., dropna: bool = ...
    ):
        """
        usage.dask: 13
        usage.koalas: 26
        usage.statsmodels: 2
        """
        ...

    @overload
    def var(self, /):
        """
        usage.dask: 4
        usage.koalas: 3
        usage.seaborn: 1
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
        usage.koalas: 3
        usage.seaborn: 1
        usage.xarray: 1
        """
        ...

    @overload
    def where(self, /, cond: pandas.core.series.Series):
        """
        usage.dask: 1
        usage.koalas: 1
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
        usage.koalas: 1
        usage.xarray: 1
        """
        ...

    def xs(self, /, key: Tuple[Literal["a"], Literal["lama"], Literal["speed"]]):
        """
        usage.koalas: 1
        """
        ...
