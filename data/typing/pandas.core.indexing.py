from typing import *


class IndexingError:
    pass


class _AtIndexer:
    @overload
    def __getitem__(self, _0: Tuple[int, Literal["b"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["b"], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["ab"], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Tuple[int, int], Literal["a"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Tuple[int], Literal["a"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[Literal["B"], Tuple[Literal["bar"], Literal["one"]]], /
    ):
        """
        usage.koalas: 1
        """
        ...

    def __getitem__(
        self,
        _0: Union[
            Tuple[
                Union[int, Tuple[int, ...], Literal["B"]],
                Union[Literal["b", "a"], Tuple[Literal["bar"], Literal["one"]]],
            ],
            Literal["ab", "b"],
        ],
        /,
    ):
        """
        usage.koalas: 9
        """
        ...

    def __setitem__(
        self, _0: Tuple[Literal["C"], Tuple[Literal["A"], Literal["two"]]], _1: None, /
    ):
        """
        usage.koalas: 4
        """
        ...


class _LocIndexer:
    @overload
    def __getitem__(self, _0: Tuple[slice[None, None, None], Literal["A_75%"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, None, None], Literal["A_25%"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, None, None], Literal["A_iqr"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[Literal["__corr_arg1__"], Literal["__corr_arg2__"]], /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __getitem__(self, _0: int, /):
        """
        usage.geopandas: 1
        usage.koalas: 10
        usage.seaborn: 1
        usage.statsmodels: 3
        """
        ...

    @overload
    def __getitem__(self, _0: slice[int, int, int], /):
        """
        usage.dask: 16
        usage.koalas: 16
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, int, None], /):
        """
        usage.dask: 4
        usage.geopandas: 3
        usage.koalas: 6
        """
        ...

    @overload
    def __getitem__(self, _0: slice[int, None, int], /):
        """
        usage.dask: 5
        usage.geopandas: 8
        usage.koalas: 7
        """
        ...

    @overload
    def __getitem__(self, _0: List[int], /):
        """
        usage.dask: 8
        usage.geopandas: 3
        usage.koalas: 2
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, None, None], /):
        """
        usage.dask: 3
        usage.koalas: 7
        """
        ...

    @overload
    def __getitem__(self, _0: list, /):
        """
        usage.dask: 2
        usage.koalas: 1
        """
        ...

    @overload
    def __getitem__(self, _0: numpy.ndarray, /):
        """
        usage.dask: 3
        usage.geopandas: 1
        usage.koalas: 1
        usage.sklearn: 1
        usage.statsmodels: 7
        usage.xarray: 2
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["a"], Literal["z"], Literal["a"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[int, int, int], Literal["a"]], /):
        """
        usage.dask: 3
        usage.koalas: 3
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[int], Literal["a"]], /):
        """
        usage.dask: 2
        usage.koalas: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[int, int, int], List[Literal["a"]]], /):
        """
        usage.dask: 3
        usage.koalas: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[int], List[Literal["a"]]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[slice[None, None, None], slice[None, None, None]], /
    ):
        """
        usage.dask: 1
        usage.koalas: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, int, None], Literal["a"]], /):
        """
        usage.dask: 2
        usage.koalas: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[int, None, int], Literal["a"]], /):
        """
        usage.dask: 2
        usage.koalas: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, int, None], List[Literal["a"]]], /):
        """
        usage.dask: 2
        usage.koalas: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[int, None, int], List[Literal["a"]]], /):
        """
        usage.dask: 2
        usage.koalas: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, Literal["a"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, List[Literal["a"]]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            slice[None, None, None], slice[Literal["a"], Literal["a"], Literal["a"]]
        ],
        /,
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            slice[None, None, None], slice[Literal["a"], Literal["d"], Literal["a"]]
        ],
        /,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            slice[None, None, None], slice[Literal["c"], Literal["d"], Literal["c"]]
        ],
        /,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, None, None], Literal["a"]], /):
        """
        usage.dask: 2
        usage.koalas: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            slice[None, None, None], slice[Literal["a"], Literal["c"], Literal["a"]]
        ],
        /,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            slice[None, None, None], slice[Literal["b"], Literal["c"], Literal["b"]]
        ],
        /,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[slice[Literal["B"], Literal["B"], Literal["B"]], Literal["bar"]],
        /,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            slice[Literal["B"], Literal["B"], Literal["B"]], List[Literal["bar"]]
        ],
        /,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            slice[None, None, None],
            slice[Literal["bar"], Literal["bar"], Literal["bar"]],
        ],
        /,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            slice[None, None, None],
            slice[
                Literal["bar"], Tuple[Literal["baz"], Literal["one"]], Literal["bar"]
            ],
        ],
        /,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            slice[None, None, None],
            slice[
                Tuple[Literal["bar"], Literal["two"]],
                Tuple[Literal["baz"], Literal["one"]],
                Tuple[Literal["bar"], Literal["two"]],
            ],
        ],
        /,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            slice[None, None, None],
            slice[
                Tuple[Literal["bar"], Literal["two"]],
                Literal["bar"],
                Tuple[Literal["bar"], Literal["two"]],
            ],
        ],
        /,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            slice[None, None, None], slice[Literal["a"], Literal["bax"], Literal["a"]]
        ],
        /,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            slice[None, None, None],
            slice[
                Tuple[Literal["bar"], Literal["x"]],
                Tuple[Literal["baz"], Literal["a"]],
                Tuple[Literal["bar"], Literal["x"]],
            ],
        ],
        /,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            slice[None, None, None],
            slice[Literal["bar"], Literal["baz"], Literal["bar"]],
        ],
        /,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[Literal["a"]], Literal["A"]], /):
        """
        usage.dask: 3
        usage.koalas: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[Literal["a"]], List[Literal["A"]]], /):
        """
        usage.dask: 3
        usage.koalas: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[slice[Literal["a"], Literal["o"], Literal["a"]], Literal["A"]],
        /,
    ):
        """
        usage.dask: 4
        usage.koalas: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[slice[Literal["a"], Literal["o"], Literal["a"]], List[Literal["A"]]],
        /,
    ):
        """
        usage.dask: 4
        usage.koalas: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[Literal["n"]], List[Literal["A"]]], /):
        """
        usage.dask: 2
        usage.koalas: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[List[Literal["n", "c", "a"]], List[Literal["A"]]], /
    ):
        """
        usage.dask: 1
        usage.koalas: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, int], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["y"], None, Literal["y"]], /):
        """
        usage.koalas: 4
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, Literal["y"], None], /):
        """
        usage.koalas: 4
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: slice[
            Tuple[Literal["x"], Literal["b"]], None, Tuple[Literal["x"], Literal["b"]]
        ],
        /,
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, Tuple[Literal["y"], Literal["c"]], None], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: slice[
            Tuple[Literal["x"], Literal["b"]],
            Tuple[Literal["y"], Literal["c"]],
            Tuple[Literal["x"], Literal["b"]],
        ],
        /,
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: slice[Literal["x"], Tuple[Literal["y"], Literal["c"]], Literal["x"]],
        /,
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: slice[
            Tuple[Literal["x"], Literal["b"]],
            Literal["y"],
            Tuple[Literal["x"], Literal["b"]],
        ],
        /,
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def __getitem__(
        self, _0: slice[Literal["2014"], Literal["2015"], Literal["2014"]], /
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def __getitem__(self, _0: pandas.core.series.Series, /):
        """
        usage.dask: 5
        usage.geopandas: 1
        usage.koalas: 7
        usage.seaborn: 2
        usage.statsmodels: 4
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[pandas.core.series.Series, Literal["a"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[pandas.core.series.Series, List[Literal["a"]]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, None, None], Literal["a_75%"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, None, None], Literal["a_25%"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, None, None], Literal["a_iqr"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[pandas.core.indexes.datetimes.DatetimeIndex, set], /
    ):
        """
        usage.alphalens: 1
        """
        ...

    @overload
    def __getitem__(self, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        """
        usage.alphalens: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[slice[None, None, None], pandas.core.indexes.base.Index], /
    ):
        """
        usage.alphalens: 2
        """
        ...

    @overload
    def __getitem__(self, _0: pandas.core.indexes.datetimes.DatetimeIndex, /):
        """
        usage.alphalens: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, Literal["mean"]], /):
        """
        usage.alphalens: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, Literal["std"]], /):
        """
        usage.alphalens: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[slice[None, None, None], slice[None, None, None]], /
    ):
        """
        usage.alphalens: 1
        """
        ...

    @overload
    def __getitem__(self, _0: cftime._cftime.DatetimeNoLeap, /):
        """
        usage.xarray: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["0001"], /):
        """
        usage.xarray: 2
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: slice[Literal["0001-01-01"], Literal["0001-12-30"], Literal["0001-01-01"]],
        /,
    ):
        """
        usage.xarray: 2
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, Literal["0001-12-30"], None], /):
        """
        usage.xarray: 2
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
        usage.xarray: 2
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, cftime._cftime.DatetimeNoLeap, None], /):
        """
        usage.xarray: 2
        """
        ...

    @overload
    def __getitem__(self, _0: cftime._cftime.Datetime360Day, /):
        """
        usage.xarray: 2
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
        usage.xarray: 2
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, cftime._cftime.Datetime360Day, None], /):
        """
        usage.xarray: 2
        """
        ...

    @overload
    def __getitem__(self, _0: cftime._cftime.DatetimeJulian, /):
        """
        usage.xarray: 2
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
        usage.xarray: 2
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, cftime._cftime.DatetimeJulian, None], /):
        """
        usage.xarray: 2
        """
        ...

    @overload
    def __getitem__(self, _0: cftime._cftime.DatetimeAllLeap, /):
        """
        usage.xarray: 2
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
        usage.xarray: 2
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, cftime._cftime.DatetimeAllLeap, None], /):
        """
        usage.xarray: 2
        """
        ...

    @overload
    def __getitem__(self, _0: cftime._cftime.DatetimeGregorian, /):
        """
        usage.xarray: 2
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
        usage.xarray: 2
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, cftime._cftime.DatetimeGregorian, None], /):
        """
        usage.xarray: 2
        """
        ...

    @overload
    def __getitem__(self, _0: cftime._cftime.DatetimeProlepticGregorian, /):
        """
        usage.xarray: 2
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
        usage.xarray: 2
        """
        ...

    @overload
    def __getitem__(
        self, _0: slice[None, cftime._cftime.DatetimeProlepticGregorian, None], /
    ):
        """
        usage.xarray: 2
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[slice[None, None, None], List[Literal["x", "a"]]], /
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[int], Literal["y"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[int], List[Literal["X", "constant"]]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[slice[None, None, None], List[Literal["NBELOW", "NABOVE"]]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, None, None], Literal["[0.025"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, None, None], Literal["0.975]"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[pandas.core.series.Series, slice[None, None, None]], /
    ):
        """
        usage.dask: 1
        usage.pyjanitor: 1
        usage.statsmodels: 3
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[pandas.core.series.Series, Literal["conc"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[pandas.core.series.Series, Literal["obs"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[pandas.core.series.Series, Literal["res"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[pandas.core.series.Series, Literal["final"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[pandas.core.series.Series, Literal["value"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[pandas.core.series.Series, Literal["Coef."]], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    def __getitem__(
        self, _0: List[Literal["R-squared Adj.", "R-squared", "x1", "const"]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: List[Literal["R-squared Adj.", "R-squared", "x2", "const", "x1"]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: List[Literal["R-squared Adj.", "R-squared", "const", "b", "a"]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.ndarray, slice[None, None, None]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["Wilks' lambda"], Literal["Value"]], /):
        """
        usage.statsmodels: 4
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["Pillai's trace"], Literal["Value"]], /):
        """
        usage.statsmodels: 4
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[str, Literal["Value"]], /):
        """
        usage.statsmodels: 4
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[Literal["Roy's greatest root"], Literal["Value"]], /
    ):
        """
        usage.statsmodels: 4
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["Wilks' lambda"], Literal["F Value"]], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["Pillai's trace"], Literal["F Value"]], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[str, Literal["F Value"]], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[Literal["Roy's greatest root"], Literal["F Value"]], /
    ):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["Wilks' lambda"], Literal["Num DF"]], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["Pillai's trace"], Literal["Num DF"]], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[str, Literal["Num DF"]], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[Literal["Roy's greatest root"], Literal["Num DF"]], /
    ):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["Wilks' lambda"], Literal["Den DF"]], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["Pillai's trace"], Literal["Den DF"]], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[str, Literal["Den DF"]], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[Literal["Roy's greatest root"], Literal["Den DF"]], /
    ):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["Wilks' lambda"], Literal["Pr > F"]], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["Pillai's trace"], Literal["Pr > F"]], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[str, Literal["Pr > F"]], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[Literal["Roy's greatest root"], Literal["Pr > F"]], /
    ):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, Literal["Wilks' lambda"]], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, Literal["F Value"]], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, Literal["Num DF"]], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, Literal["Den DF"]], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, Literal["Pr > F"]], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[pandas.core.indexes.numeric.Int64Index, slice[None, None, None]],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["Intercept", "income"]], /):
        """
        usage.statsmodels: 5
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, Literal["homog_stat"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, Literal["homog_df"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, Literal["lbl_stat"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, Literal["lbl_expval"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, Literal["lbl_var"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, Literal["lbl_chi2"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, Literal["lbl_pvalue"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, Literal["lbl2_stat"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, Literal["lbl2_expval"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, Literal["lbl2_var"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, Literal["lbl2_chi2"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, Literal["lbl2_pvalue"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, Literal["bowker_stat"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, Literal["bowker_df"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, Literal["bowker_pvalue"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, Literal["homog_cont_p"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, Literal["homog_binom_p"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[pandas.core.indexes.numeric.Int64Index, int], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.ndarray, Literal["v1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.ndarray, Literal["v2"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[pandas.core.indexes.numeric.Int64Index, Literal["v1"]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[pandas.core.indexes.numeric.Int64Index, Literal["v2"]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, None, None], List[bool]], /):
        """
        usage.sklearn: 1
        usage.statsmodels: 10
        """
        ...

    @overload
    def __getitem__(self, _0: List[str], /):
        """
        usage.statsmodels: 6
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["lb_stat"], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["lb_pvalue"], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, Literal["bp_stat"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, Literal["bp_pvalue"]], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["x"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["z"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[str, Literal["Estimate"]], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __getitem__(self, _0: List[bool], /):
        """
        usage.sklearn: 2
        usage.statsmodels: 2
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: slice[Literal["1960-04-01"], Literal["1978-10-01"], Literal["1960-04-01"]],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            slice[Literal["1960-04-01"], Literal["1978-10-01"], Literal["1960-04-01"]],
            List[Literal["dln_inc", "dln_inv"]],
        ],
        /,
    ):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            slice[Literal["1960-04-01"], Literal["1978-10-01"], Literal["1960-04-01"]],
            List[Literal["dln_consump", "dln_inc", "dln_inv"]],
        ],
        /,
    ):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[numpy.str_], Literal["count"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: pandas.core.indexes.base.Index, /):
        """
        usage.dask: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[List[Literal["Q1", "Q0", "M1", "M0"]], pandas.core.series.Series],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, None, None], Tuple[numpy.str_]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["M0"], numpy.str_], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["M1"], numpy.str_], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["Q0"], numpy.str_], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["Q1"], numpy.str_], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[Literal["1", "0"]], Literal["count"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[slice[None, None, None], Tuple[Literal["0"], Literal["1"]]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["M0"], Literal["0"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["M0"], Literal["1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["M1"], Literal["0"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["M1"], Literal["1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["Q0"], Literal["0"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["Q0"], Literal["1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["Q1"], Literal["0"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["Q1"], Literal["1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[Literal["b", "a"]], Literal["count"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[Literal["b"]], Literal["count"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[int], pandas.core.series.Series], /):
        """
        usage.statsmodels: 4
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[List[Literal["y2", "y1"]], pandas.core.series.Series], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[List[Literal["global.2", "global.1"]], Literal["count"]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            slice[None, None, None], Tuple[Literal["global.1"], Literal["global.2"]]
        ],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, None, None], Literal["global.1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, None, None], Literal["global.2"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, Literal["global.1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, Literal["global.2"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[slice[None, None, None], List[Literal["global.2", "global.1"]]],
        /,
    ):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            Tuple[List[Literal["global.2", "global.1"]], slice[None, None, None]],
            List[Literal["global.2", "global.1"]],
        ],
        /,
    ):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, None, None], Literal["global"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, None, None], Literal["block"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, numpy.str_], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[slice[None, None, None], List[Literal["block", "global"]]], /
    ):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            Tuple[List[Literal["block", "global"]], slice[None, None, None]],
            List[Literal["block", "global"]],
        ],
        /,
    ):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, None, None], Literal["0"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            List[Literal["yQ2_f1", "yQ1_f1", "yM2_f1", "yM1_f1"]],
            pandas.core.series.Series,
        ],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["yM1_f1"], numpy.str_], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["yM2_f1"], numpy.str_], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["yQ1_f1"], numpy.str_], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["yQ2_f1"], numpy.str_], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[Literal["y"]], pandas.core.series.Series], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[Literal["y1"]], pandas.core.series.Series], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["y"], numpy.str_], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["y1"], numpy.str_], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["y2"], numpy.str_], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[Literal["f1"]], pandas.core.series.Series], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["f1"], numpy.str_], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[List[Literal["f2", "f1"]], pandas.core.series.Series], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["f2"], numpy.str_], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, Literal["1957-12"], None], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, Literal["1957Q4"], None], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["1958-01"], None, Literal["1958-01"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["1958Q1"], None, Literal["1958Q1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[Literal["b.2", "b.1"]], Literal["count"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[str], pandas.core.series.Series], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[slice[None, None, None], Tuple[Literal["b.1"], Literal["b.2"]]],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, None, None], Literal["b.1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, None, None], Literal["b.2"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["yM1_f1"], Literal["b.1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["yM1_f1"], Literal["b.2"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["yM2_f1"], Literal["b.1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["yM2_f1"], Literal["b.2"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["f1"], Literal["b.1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["f1"], Literal["b.2"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["f2"], Literal["b.1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["f2"], Literal["b.2"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["yM1_f2"], Literal["b.1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["yM1_f2"], Literal["b.2"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["yM1_f2"], numpy.str_], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["yM2_f2"], Literal["b.1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["yM2_f2"], Literal["b.2"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["yM2_f2"], numpy.str_], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["yQ1_f1"], Literal["b.1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["yQ1_f1"], Literal["b.2"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["yQ2_f1"], Literal["b.1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["yQ2_f1"], Literal["b.2"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["yQ1_f2"], Literal["b.1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["yQ1_f2"], Literal["b.2"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["yQ1_f2"], numpy.str_], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["yQ2_f2"], Literal["b.1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["yQ2_f2"], Literal["b.2"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["yQ2_f2"], numpy.str_], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            List[Literal["ULCNFB", "GDPC1", "PAYEMS", "UNRATE", "CPIAUCSL"]],
            pandas.core.series.Series,
        ],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["CPIAUCSL"], numpy.str_], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["UNRATE"], numpy.str_], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["PAYEMS"], numpy.str_], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["GDPC1"], numpy.str_], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["ULCNFB"], numpy.str_], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["CPIAUCSL"], Literal["0"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["CPIAUCSL"], Literal["1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["UNRATE"], Literal["0"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["UNRATE"], Literal["1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["PAYEMS"], Literal["0"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["PAYEMS"], Literal["1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["GDPC1"], Literal["0"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["GDPC1"], Literal["1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["ULCNFB"], Literal["0"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["ULCNFB"], Literal["1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[Literal["global"]], Literal["count"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[Literal["test1"]], Literal["count"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[Literal["test2"]], Literal["count"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[slice[None, None, None], Tuple[Literal["global"]]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[slice[None, None, None], Tuple[Literal["test1"]]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[slice[None, None, None], Tuple[Literal["test2"]]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["CPIAUCSL"], Literal["global"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["CPIAUCSL"], Literal["test1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["CPIAUCSL"], Literal["test2"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["UNRATE"], Literal["global"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["UNRATE"], Literal["test1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["UNRATE"], Literal["test2"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["PAYEMS"], Literal["global"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["PAYEMS"], Literal["test1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["PAYEMS"], Literal["test2"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["RSAFS"], Literal["global"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["RSAFS"], Literal["test1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["RSAFS"], Literal["test2"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["TTLCONS"], Literal["global"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["TTLCONS"], Literal["test1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["TTLCONS"], Literal["test2"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["TCU"], Literal["global"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["TCU"], Literal["test1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["TCU"], Literal["test2"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["GDPC1"], Literal["global"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["GDPC1"], Literal["test1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["GDPC1"], Literal["test2"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["ULCNFB"], Literal["global"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["ULCNFB"], Literal["test1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["ULCNFB"], Literal["test2"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[List[Literal["test1.2", "test1.1"]], Literal["count"]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[List[Literal["test2.2", "test2.1"]], Literal["count"]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            slice[None, None, None], Tuple[Literal["test1.1"], Literal["test1.2"]]
        ],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            slice[None, None, None], Tuple[Literal["test2.1"], Literal["test2.2"]]
        ],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["CPIAUCSL"], Literal["global.1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["CPIAUCSL"], Literal["global.2"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["CPIAUCSL"], Literal["test1.1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["CPIAUCSL"], Literal["test1.2"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["CPIAUCSL"], Literal["test2.1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["CPIAUCSL"], Literal["test2.2"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["UNRATE"], Literal["global.1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["UNRATE"], Literal["global.2"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["UNRATE"], Literal["test1.1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["UNRATE"], Literal["test1.2"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["UNRATE"], Literal["test2.1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["UNRATE"], Literal["test2.2"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["PAYEMS"], Literal["global.1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["PAYEMS"], Literal["global.2"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["PAYEMS"], Literal["test1.1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["PAYEMS"], Literal["test1.2"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["PAYEMS"], Literal["test2.1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["PAYEMS"], Literal["test2.2"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["RSAFS"], Literal["global.1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["RSAFS"], Literal["global.2"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["RSAFS"], Literal["test1.1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["RSAFS"], Literal["test1.2"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["RSAFS"], Literal["test2.1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["RSAFS"], Literal["test2.2"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["TTLCONS"], Literal["global.1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["TTLCONS"], Literal["global.2"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["TTLCONS"], Literal["test1.1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["TTLCONS"], Literal["test1.2"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["TTLCONS"], Literal["test2.1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["TTLCONS"], Literal["test2.2"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["TCU"], Literal["global.1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["TCU"], Literal["global.2"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["TCU"], Literal["test1.1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["TCU"], Literal["test1.2"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["TCU"], Literal["test2.1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["TCU"], Literal["test2.2"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["GDPC1"], Literal["global.1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["GDPC1"], Literal["global.2"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["GDPC1"], Literal["test1.1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["GDPC1"], Literal["test1.2"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["GDPC1"], Literal["test2.1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["GDPC1"], Literal["test2.2"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["ULCNFB"], Literal["global.1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["ULCNFB"], Literal["global.2"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["ULCNFB"], Literal["test1.1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["ULCNFB"], Literal["test1.2"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["ULCNFB"], Literal["test2.1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["ULCNFB"], Literal["test2.2"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, None, None], Literal["1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, None, None], Literal["2"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, None, None], Literal["test1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, None, None], Literal["test2"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, None, None], Literal["test1.1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, None, None], Literal["test1.2"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, None, None], Literal["test2.1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, None, None], Literal["test2.2"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[Literal["2", "1", "0"]], Literal["count"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            slice[None, None, None], Tuple[Literal["0"], Literal["1"], Literal["2"]]
        ],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["2016-09"], Literal["GDPC1"]], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["2016-06"], Literal["CPIAUCSL"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["2016-06"], Literal["UNRATE"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["2016-06"], Literal["PAYEMS"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["2016-06"], Literal["GDPC1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["2016-06"], Literal["RSAFS"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["2016-05"], Literal["TTLCONS"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["2016-06"], Literal["TCU"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[List[Literal["yQ_f1", "yM_f1"]], pandas.core.series.Series], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["yM_f1"], numpy.str_], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["yQ_f1"], numpy.str_], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, None, None], numpy.ndarray], /):
        """
        usage.seaborn: 1
        usage.sklearn: 3
        usage.statsmodels: 2
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, Literal["2009Q2"], None], /):
        """
        usage.statsmodels: 7
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, Literal["2009Q3"], None], /):
        """
        usage.statsmodels: 21
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["2009Q3"], /):
        """
        usage.statsmodels: 5
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["2009Q2"], /):
        """
        usage.statsmodels: 5
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[slice[None, None, None], Literal["estimate (prev)"]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[slice[None, None, None], Literal["impact of revisions"]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[slice[None, None, None], Literal["impact of news"]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[slice[None, None, None], Literal["total impact"]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[slice[None, None, None], Literal["estimate (new)"]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: slice[Literal["1960Q2"], Literal["1978"], Literal["1960Q2"]], /
    ):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __getitem__(
        self, _0: slice[Literal["1979Q1"], Literal["1981Q2"], Literal["1979Q1"]], /
    ):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[slice[None, None, None], pandas.core.series.Series], /
    ):
        """
        usage.seaborn: 2
        usage.statsmodels: 2
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: slice[
            pandas._libs.tslibs.timestamps.Timestamp,
            pandas._libs.tslibs.timestamps.Timestamp,
            pandas._libs.tslibs.timestamps.Timestamp,
        ],
        /,
    ):
        """
        usage.dask: 2
        usage.statsmodels: 3
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: slice[
            pandas._libs.tslibs.period.Period,
            pandas._libs.tslibs.period.Period,
            pandas._libs.tslibs.period.Period,
        ],
        /,
    ):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    def __getitem__(self, _0: pandas.core.indexes.range.RangeIndex, /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __getitem__(self, _0: pandas.core.indexes.numeric.Int64Index, /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["baseline"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["short"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["nljump-1"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["ntjump-1"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["nljump-1-ntjump-1"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, None, None], Literal["ds"]], /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[pandas.core.series.Series, Literal["x"]], /):
        """
        usage.seaborn: 3
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[pandas.core.series.Series, Literal["y"]], /):
        """
        usage.seaborn: 3
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.float64, numpy.float64], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["c"]], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["a"], /):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["b"], /):
        """
        usage.geopandas: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, Literal["A"]], /):
        """
        usage.geopandas: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, Literal["Shape_Leng"]], /):
        """
        usage.geopandas: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, Literal["geometry"]], /):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[int], Literal["geometry"]], /):
        """
        usage.geopandas: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.ndarray, Literal["geometry"]], /):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, None, None], int], /):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, None, None], Literal["DATE"]], /):
        """
        usage.pyjanitor: 6
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[int], slice[None, None, None]], /):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[List[Literal["lion", "leopard", "rabbit"]], slice[None, None, None]],
        /,
    ):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[List[Literal["leopard", "lion", "rabbit"]], slice[None, None, None]],
        /,
    ):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            slice[None, None, None],
            List[
                Literal[
                    "cities", "animals@#$%^", "Bell__Chart", "decorated-elephant", "a"
                ]
            ],
        ],
        /,
    ):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            slice[None, None, None],
            List[
                Literal[
                    "cities", "Bell__Chart", "animals@#$%^", "decorated-elephant", "a"
                ]
            ],
        ],
        /,
    ):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["E"], Literal["g"], Literal["E"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["g"], Literal["h"], Literal["g"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["a"], Literal["f"], Literal["a"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["f"], Literal["j"], Literal["f"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["j"], Literal["k"], Literal["j"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["a"], Literal["b"], Literal["a"]], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["b"], Literal["f"], Literal["b"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["f"], Literal["k"], Literal["f"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["b"], Literal["d"], Literal["b"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["d"], Literal["f"], Literal["d"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["f"], Literal["h"], Literal["f"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["h"], Literal["k"], Literal["h"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["h"], Literal["j"], Literal["h"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["A"], Literal["a"], Literal["A"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["a"], Literal["a"], Literal["a"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["e"], Literal["f"], Literal["e"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["a"], Literal["e"], Literal["a"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[slice[None, None, None], List[Literal["d", "c"]]], /
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[slice[None, None, None], List[Literal["f", "d", "c"]]], /
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[slice[None, None, None], List[Literal["g", "d", "c"]]], /
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[slice[None, None, None], List[Literal["g", "f", "d", "c"]]], /
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[slice[None, None, None], List[Literal["g", "f"]]], /
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[int, numpy.int64, int], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[numpy.int64, numpy.int64, numpy.int64], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[numpy.int64, int, numpy.int64], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: float, /):
        """
        usage.dask: 4
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["a"], Literal["d"], Literal["a"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["d"], Literal["g"], Literal["d"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[numpy.float64, float, numpy.float64], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[float, numpy.float64, float], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[float, float, float], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["A"], Literal["b"], Literal["A"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["b"], Literal["g"], Literal["b"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["g"], Literal["l"], Literal["g"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["l"], Literal["q"], Literal["l"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["q"], Literal["v"], Literal["q"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["v"], Literal["z"], Literal["v"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["x"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["z", "y"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: slice[None, pandas._libs.tslibs.timestamps.Timestamp, None], /
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: slice[
            pandas._libs.tslibs.timestamps.Timestamp,
            None,
            pandas._libs.tslibs.timestamps.Timestamp,
        ],
        /,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, Literal["02.02.2015"], None], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(
        self, _0: slice[Literal["02.02.2015"], None, Literal["02.02.2015"]], /
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Callable, slice[None, None, None]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, None, None], Callable], /):
        """
        usage.dask: 3
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["a"], Literal["g"], Literal["a"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["k"], Literal["o"], Literal["k"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["o"], Literal["t"], Literal["o"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, None, None], List[Literal["a"]]], /):
        """
        usage.dask: 2
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, None, None], Literal["A"]], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[slice[Literal["a"], Literal["a"], Literal["a"]], Literal["A"]],
        /,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, None, None], List[Literal["A"]]], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[slice[Literal["a"], Literal["a"], Literal["a"]], List[Literal["A"]]],
        /,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[slice[Literal["a"], None, Literal["a"]], Literal["A"]], /
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, Literal["o"], None], Literal["A"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[slice[Literal["a"], None, Literal["a"]], List[Literal["A"]]], /
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[slice[None, Literal["o"], None], List[Literal["A"]]], /
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[Literal["c", "a"]], List[Literal["A"]]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[Literal["b", "t"]], List[Literal["A"]]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[Literal["b"]], List[Literal["A"]]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[Literal["t"]], List[Literal["A"]]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[List[Literal["h", "g", "c", "r"]], List[Literal["A"]]], /
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[Literal["g", "c"]], List[Literal["A"]]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[Literal["h"]], List[Literal["A"]]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[Literal["r"]], List[Literal["A"]]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, None, None], Literal["B"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[Literal["j"]], Literal["B"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[slice[Literal["j"], Literal["j"], Literal["j"]], Literal["B"]],
        /,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, None, None], List[Literal["B"]]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[Literal["j"]], List[Literal["B"]]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[slice[Literal["j"], Literal["j"], Literal["j"]], List[Literal["B"]]],
        /,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[slice[Literal["j"], Literal["q"], Literal["j"]], Literal["B"]],
        /,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[slice[Literal["j"], None, Literal["j"]], Literal["B"]], /
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, Literal["q"], None], Literal["B"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[slice[Literal["j"], Literal["q"], Literal["j"]], List[Literal["B"]]],
        /,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[slice[Literal["j"], None, Literal["j"]], List[Literal["B"]]], /
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[slice[None, Literal["q"], None], List[Literal["B"]]], /
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            slice[None, None, None], slice[Literal["B"], Literal["D"], Literal["B"]]
        ],
        /,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            slice[Literal["a"], Literal["o"], Literal["a"]],
            slice[Literal["B"], Literal["D"], Literal["B"]],
        ],
        /,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            slice[Literal["a"], None, Literal["a"]],
            slice[Literal["B"], Literal["D"], Literal["B"]],
        ],
        /,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            slice[None, Literal["o"], None],
            slice[Literal["B"], Literal["D"], Literal["B"]],
        ],
        /,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            slice[None, None, None], slice[Literal["B"], Literal["A"], Literal["B"]]
        ],
        /,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            slice[Literal["j"], Literal["q"], Literal["j"]],
            slice[Literal["B"], Literal["A"], Literal["B"]],
        ],
        /,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            slice[Literal["j"], None, Literal["j"]],
            slice[Literal["B"], Literal["A"], Literal["B"]],
        ],
        /,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            slice[None, Literal["q"], None],
            slice[Literal["B"], Literal["A"], Literal["B"]],
        ],
        /,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[pandas.core.series.Series, Literal["B"]], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[slice[None, None, None], List[Literal["C", "A"]]], /
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[pandas.core.series.Series, List[Literal["C", "A"]]], /
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["a"], None, Literal["a"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, Literal["e"], None], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["f"], None, Literal["f"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            slice[Literal["2016-01-03"], Literal["2016-01-05"], Literal["2016-01-03"]],
            slice[None, None, None],
        ],
        /,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            slice[
                pandas._libs.tslibs.timestamps.Timestamp,
                pandas._libs.tslibs.timestamps.Timestamp,
                pandas._libs.tslibs.timestamps.Timestamp,
            ],
            slice[None, None, None],
        ],
        /,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["2011-01-02"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: slice[Literal["2011-01-02"], Literal["2011-01-10"], Literal["2011-01-02"]],
        /,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["2011-01-02 10:00"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: slice[
            pandas._libs.tslibs.period.Period, None, pandas._libs.tslibs.period.Period
        ],
        /,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, pandas._libs.tslibs.period.Period, None], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["f"], Literal["g"], Literal["f"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["f"], Literal["f"], Literal["f"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["g"], Literal["j"], Literal["g"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["j"], Literal["l"], Literal["j"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["f"], Literal["e"], Literal["f"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["g"], Literal["i"], Literal["g"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["i"], Literal["l"], Literal["i"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["f"], Literal["d"], Literal["f"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, numpy.int64, None], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[numpy.int64, None, numpy.int64], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["e"], Literal["g"], Literal["e"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["d"], Literal["e"], Literal["d"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["c"], Literal["d"], Literal["c"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["l"], Literal["l"], Literal["l"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["d"], Literal["l"], Literal["d"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["a"], Literal["c"], Literal["a"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["p"], Literal["r"], Literal["p"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["l"], Literal["p"], Literal["l"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["l"], Literal["c"], Literal["l"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["o"], Literal["r"], Literal["o"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["l"], Literal["o"], Literal["l"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["c"], Literal["c"], Literal["c"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["f"], Literal["i"], Literal["f"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["h"], Literal["i"], Literal["h"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["i"], Literal["j"], Literal["i"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["j"], Literal["n"], Literal["j"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["n"], Literal["o"], Literal["n"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["F"], Literal["J"], Literal["F"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["J"], Literal["a"], Literal["J"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["A"], Literal["F"], Literal["A"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["a"], Literal["F"], Literal["a"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["e"], Literal["i"], Literal["e"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["I"], Literal["J"], Literal["I"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["A"], Literal["E"], Literal["A"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["E"], Literal["I"], Literal["E"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["a"], Literal["E"], Literal["a"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["k"], Literal["p"], Literal["k"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["j"], Literal["m"], Literal["j"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["m"], Literal["r"], Literal["m"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["k"], Literal["m"], Literal["k"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["m"], Literal["p"], Literal["m"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["c"], Literal["e"], Literal["c"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["g"], Literal["m"], Literal["g"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["c"], Literal["g"], Literal["c"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["c"], Literal["f"], Literal["c"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["i"], Literal["m"], Literal["i"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["f"], Literal["c"], Literal["f"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["y"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, None, None], Literal["first"]], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[slice[None, None, None], List[Literal["first"]]], /
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[slice[None, None, None], List[Literal["second", "first"]]], /
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            slice[None, None, None],
            slice[Literal["first"], Literal["second"], Literal["first"]],
        ],
        /,
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[slice[None, None, None], List[Literal["second"]]], /
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, None, None], Literal["col1"]], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[slice[None, None, None], List[Literal["col1", "col0"]]], /
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, None, None], List[Literal["col1"]]], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[slice[None, None, None], slice[None, Literal["first"], None]], /
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            slice[None, None, None],
            slice[Literal["first"], Literal["first"], Literal["first"]],
        ],
        /,
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, None, None], Literal["second"]], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[slice[None, None, None], List[Literal["b", "a"]]], /
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[slice[None, None, None], List[Literal["col_str", "col_cat"]]], /
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[slice[None, None, None], List[Literal["col_float", "col_int"]]],
        /,
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[slice[None, None, None], List[Literal["col_int", "col_float"]]],
        /,
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[slice[None, None, None], List[Literal["col2", "col1"]]], /
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            slice[None, None, None],
            List[Literal["petal length (cm)", "sepal length (cm)"]],
        ],
        /,
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            slice[None, None, None],
            List[Literal["petal width (cm)", "sepal width (cm)"]],
        ],
        /,
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, None, None], List[Literal["col2"]]], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[slice[None, None, None], List[Literal["col_2", "col_1"]]], /
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            slice[None, None, None],
            slice[Literal["col_1"], Literal["col_2"], Literal["col_1"]],
        ],
        /,
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, None, None], Literal["col_2"]], /):
        """
        usage.sklearn: 1
        """
        ...

    def __getitem__(self, _0: object, /):
        """
        usage.alphalens: 9
        usage.dask: 250
        usage.geopandas: 28
        usage.koalas: 137
        usage.prophet: 1
        usage.pyjanitor: 13
        usage.seaborn: 14
        usage.sklearn: 30
        usage.statsmodels: 455
        usage.xarray: 45
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[slice[None, None, None], Literal["A_iqr"]],
        _1: pandas.core.series.Series,
        /,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[slice[None, None, None], Literal["A_lfence"]],
        _1: pandas.core.series.Series,
        /,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[slice[None, None, None], Literal["A_ufence"]],
        _1: pandas.core.series.Series,
        /,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[
            List[Literal["sidewinder", "viper"]], List[Literal["max_speed", "shield"]]
        ],
        _1: int,
        /,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[List[Literal["sidewinder", "viper"]], Literal["shield"]],
        _1: int,
        /,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["cobra"], Literal["max_speed"]], _1: int, /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[pandas.core.series.Series, Literal["max_speed"]],
        _1: pandas.core.series.Series,
        /,
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[slice[None, None, None], Literal["min_speed"]], _1: int, /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[slice[None, None, None], Tuple[Literal["y"], Literal["shield"]]],
        _1: pandas.core.series.Series,
        /,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[slice[None, None, None], Literal["z"]], _1: int, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[slice[None, None, None], Literal["max_speed"]],
        _1: pandas.core.frame.DataFrame,
        /,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: pandas.core.series.Series, _1: pandas.core.series.Series, /
    ):
        """
        usage.koalas: 5
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: List[Literal["sidewinder", "viper"]], _1: int, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["viper"], _1: int, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: slice[None, None, None], _1: int, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: slice[None, Literal["viper"], None], _1: int, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: slice[Literal["viper"], None, Literal["viper"]], _1: int, /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["x"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["y"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[List[Literal["sidewinder", "viper"]], List[Literal["shield"]]],
        _1: pandas.core.series.Series,
        /,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[pandas.core.series.Series, List[Literal["shield"]]],
        _1: pandas.core.series.Series,
        /,
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def __setitem__(
        self, _0: List[Literal["sidewinder", "viper"]], _1: pandas.core.series.Series, /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: pandas.core.series.Series, _1: int, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: int, _1: float, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[slice[None, None, None], Literal["a_iqr"]],
        _1: pandas.core.series.Series,
        /,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[slice[None, None, None], Literal["a_lfence"]],
        _1: pandas.core.series.Series,
        /,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[slice[None, None, None], Literal["a_ufence"]],
        _1: pandas.core.series.Series,
        /,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["Ann. alpha"], Literal["1D"]], _1: numpy.float64, /
    ):
        """
        usage.alphalens: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["beta"], Literal["1D"]], _1: numpy.float64, /
    ):
        """
        usage.alphalens: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["Ann. alpha"], Literal["5D"]], _1: numpy.float64, /
    ):
        """
        usage.alphalens: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["beta"], Literal["5D"]], _1: numpy.float64, /
    ):
        """
        usage.alphalens: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["Ann. alpha"], Literal["10D"]], _1: numpy.float64, /
    ):
        """
        usage.alphalens: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["beta"], Literal["10D"]], _1: numpy.float64, /
    ):
        """
        usage.alphalens: 1
        """
        ...

    @overload
    def __setitem__(self, _0: str, _1: pandas.core.series.Series, /):
        """
        usage.alphalens: 3
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["Ann. alpha"], Literal["2D"]], _1: numpy.float64, /
    ):
        """
        usage.alphalens: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["beta"], Literal["2D"]], _1: numpy.float64, /
    ):
        """
        usage.alphalens: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["Ann. alpha"], Literal["4D"]], _1: numpy.float64, /
    ):
        """
        usage.alphalens: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["beta"], Literal["4D"]], _1: numpy.float64, /
    ):
        """
        usage.alphalens: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["Ann. alpha"], Literal["6D"]], _1: numpy.float64, /
    ):
        """
        usage.alphalens: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["beta"], Literal["6D"]], _1: numpy.float64, /
    ):
        """
        usage.alphalens: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["Ann. alpha"], Literal["8D"]], _1: numpy.float64, /
    ):
        """
        usage.alphalens: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["beta"], Literal["8D"]], _1: numpy.float64, /
    ):
        """
        usage.alphalens: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["Ann. alpha"], Literal["3D"]], _1: numpy.float64, /
    ):
        """
        usage.alphalens: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["beta"], Literal["3D"]], _1: numpy.float64, /
    ):
        """
        usage.alphalens: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["Ann. alpha"], Literal["7D"]], _1: numpy.float64, /
    ):
        """
        usage.alphalens: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["beta"], Literal["7D"]], _1: numpy.float64, /
    ):
        """
        usage.alphalens: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[str, Literal["1D"]], _1: numpy.float64, /):
        """
        usage.alphalens: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[str, Literal["5D"]], _1: numpy.float64, /):
        """
        usage.alphalens: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[str, Literal["10D"]], _1: numpy.float64, /):
        """
        usage.alphalens: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[str, Literal["2D"]], _1: numpy.float64, /):
        """
        usage.alphalens: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[str, Literal["3D"]], _1: numpy.float64, /):
        """
        usage.alphalens: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[str, Literal["7D"]], _1: numpy.float64, /):
        """
        usage.alphalens: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[int, Literal["Bar"]], _1: int, /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[slice[None, None, None], Literal["[0.025"]],
        _1: pandas.core.series.Series,
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[slice[None, None, None], Literal["0.975]"]],
        _1: pandas.core.series.Series,
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: int, _1: None, /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[numpy.ndarray, Literal["SD"]], _1: Literal[""], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[numpy.ndarray, Literal["SD (LB)"]], _1: Literal[""], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[numpy.ndarray, Literal["SD (UB)"]], _1: Literal[""], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[pandas.core.series.Series, Literal["fake"]], _1: float, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[slice[int, int, int], Literal["time"]], _1: float, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[slice[int, int, int], Literal["status"]], _1: float, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[slice[int, int, int], Literal["x1"]], _1: float, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[slice[int, int, int], Literal["x2"]], _1: float, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[int, Literal["censored"]], _1: bool, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[slice[None, None, None], Literal["upper_dl"]],
        _1: pandas.core.series.Series,
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[slice[None, None, None], Literal["nuncen_above"]],
        _1: pandas.core.series.Series,
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[slice[None, None, None], Literal["nobs_below"]],
        _1: pandas.core.series.Series,
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[slice[None, None, None], Literal["ncen_equal"]],
        _1: pandas.core.series.Series,
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[slice[None, None, None], Literal["prob_exceedance"]],
        _1: numpy.ndarray,
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[slice[None, None, None], Literal["rank"]], _1: int, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[slice[None, None, None], Literal["estimated"]],
        _1: pandas.core.series.Series,
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[slice[None, None, None], Literal["final"]], _1: numpy.ndarray, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[slice[None, None, None], Literal["conc"]],
        _1: pandas.core.series.Series,
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[slice[None, None, None], Literal["censored"]],
        _1: pandas.core.series.Series,
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[slice[None, None, None], Literal["det_limit_index"]],
        _1: pandas.core.series.Series,
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[slice[None, None, None], Literal["rank"]],
        _1: pandas.core.series.Series,
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[slice[None, None, None], Literal["plot_pos"]],
        _1: pandas.core.series.Series,
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[slice[None, None, None], Literal["Zprelim"]],
        _1: numpy.ndarray,
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[slice[None, None, None], Literal["final"]],
        _1: pandas.core.series.Series,
        /,
    ):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[slice[None, None, None], Literal["upper_dl"]],
        _1: List[float],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[pandas.core.series.Series, Literal["final"]],
        _1: pandas.core.series.Series,
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[pandas.core.series.Series, Literal["Coef."]],
        _1: pandas.core.series.Series,
        /,
    ):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[int, str], _1: numpy.float64, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[int, Literal["Wilks' lambda"]], _1: numpy.float64, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[int, Literal["Num DF"]], _1: int, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[int, Literal["Den DF"]], _1: float, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[int, Literal["F Value"]], _1: numpy.float64, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[int, Literal["Pr > F"]], _1: numpy.float64, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[int, Literal["Den DF"]], _1: numpy.float64, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[Literal["Wilks' lambda"], Literal["Value"]],
        _1: numpy.float64,
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[Literal["Pillai's trace"], Literal["Value"]],
        _1: numpy.float64,
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[str, Literal["Value"]], _1: numpy.float64, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[Literal["Roy's greatest root"], Literal["Value"]],
        _1: numpy.float64,
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["Wilks' lambda"], Literal["Num DF"]], _1: int, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[Literal["Wilks' lambda"], Literal["Den DF"]],
        _1: numpy.float64,
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[Literal["Wilks' lambda"], Literal["F Value"]],
        _1: numpy.float64,
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[Literal["Wilks' lambda"], Literal["Pr > F"]],
        _1: numpy.float64,
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[Literal["Pillai's trace"], Literal["Num DF"]],
        _1: numpy.float64,
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[Literal["Pillai's trace"], Literal["Den DF"]],
        _1: numpy.float64,
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[Literal["Pillai's trace"], Literal["F Value"]],
        _1: numpy.float64,
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[Literal["Pillai's trace"], Literal["Pr > F"]],
        _1: numpy.float64,
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[str, Literal["Num DF"]], _1: int, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[str, Literal["Den DF"]], _1: float, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[str, Literal["F Value"]], _1: numpy.float64, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[str, Literal["Pr > F"]], _1: numpy.float64, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[Literal["Roy's greatest root"], Literal["Num DF"]],
        _1: numpy.int64,
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[Literal["Roy's greatest root"], Literal["Den DF"]],
        _1: numpy.int64,
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[Literal["Roy's greatest root"], Literal["F Value"]],
        _1: numpy.float64,
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[Literal["Roy's greatest root"], Literal["Pr > F"]],
        _1: numpy.float64,
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["Wilks' lambda"], Literal["Num DF"]], _1: numpy.int64, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[str, Literal["Num DF"]], _1: numpy.int64, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[str, Literal["Den DF"]], _1: numpy.float64, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[int, Literal["y"]], _1: float, /):
        """
        usage.prophet: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[int, Literal["g"]], _1: float, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[int, Literal["x1"]], _1: float, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[int, Literal["z1"]], _1: float, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[int, Literal["c1"]], _1: float, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[int, Literal["c2"]], _1: float, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[int, Literal["firm"]], _1: float, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[List[str], List[Literal["sum_sq", "df"]]], _1: numpy.ndarray, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[Literal["Residual"], List[Literal["df", "sum_sq"]]],
        _1: Tuple[numpy.float64, numpy.float64],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[Literal["Residual"], List[Literal["PR(>F)", "F"]]],
        _1: Tuple[float, float],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[pandas.core.indexes.range.RangeIndex, Literal["df_diff"]],
        _1: numpy.ndarray,
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[int, Literal["F"]], _1: numpy.ndarray, /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[int, Literal["PR(>F)"]], _1: numpy.ndarray, /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[int, Literal["df"]], _1: int, /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[Literal["Residual"], List[Literal["PR(>F)", "F", "df", "sum_sq"]]],
        _1: Tuple[numpy.float64, numpy.float64, float, float],
        /,
    ):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["B"], Literal["F Value"]], _1: numpy.float64, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["B"], Literal["Num DF"]], _1: numpy.float64, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["B"], Literal["Den DF"]], _1: numpy.float64, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["B"], Literal["Pr > F"]], _1: numpy.float64, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["A"], Literal["F Value"]], _1: numpy.float64, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["A"], Literal["Num DF"]], _1: numpy.float64, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["A"], Literal["Den DF"]], _1: numpy.float64, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["A"], Literal["Pr > F"]], _1: numpy.float64, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["A:B"], Literal["F Value"]], _1: numpy.float64, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["A:B"], Literal["Num DF"]], _1: numpy.float64, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["A:B"], Literal["Den DF"]], _1: numpy.float64, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["A:B"], Literal["Pr > F"]], _1: numpy.float64, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["D"], Literal["F Value"]], _1: numpy.float64, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["D"], Literal["Num DF"]], _1: numpy.float64, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["D"], Literal["Den DF"]], _1: numpy.float64, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["D"], Literal["Pr > F"]], _1: numpy.float64, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["A:D"], Literal["F Value"]], _1: numpy.float64, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["A:D"], Literal["Num DF"]], _1: numpy.float64, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["A:D"], Literal["Den DF"]], _1: numpy.float64, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["A:D"], Literal["Pr > F"]], _1: numpy.float64, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["B:D"], Literal["F Value"]], _1: numpy.float64, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["B:D"], Literal["Num DF"]], _1: numpy.float64, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["B:D"], Literal["Den DF"]], _1: numpy.float64, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["B:D"], Literal["Pr > F"]], _1: numpy.float64, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["A:B:D"], Literal["F Value"]], _1: numpy.float64, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["A:B:D"], Literal["Num DF"]], _1: numpy.float64, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["A:B:D"], Literal["Den DF"]], _1: numpy.float64, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["A:B:D"], Literal["Pr > F"]], _1: numpy.float64, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[slice[None, None, None], int], _1: numpy.ndarray, /
    ):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    def __setitem__(self, _0: pandas.core.series.Series, _1: float, /):
        """
        usage.seaborn: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[pandas.core.indexes.range.RangeIndex, Literal["c"]],
        _1: float,
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[pandas.core.indexes.range.RangeIndex, Literal["d"]],
        _1: pandas._libs.missing.NAType,
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[slice[None, None, None], Literal["treat"]], _1: int, /
    ):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[slice[None, None, None], Literal["emo"]], _1: numpy.ndarray, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[slice[None, None, None], Literal["age"]], _1: int, /
    ):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[slice[None, None, None], Literal["x"]], _1: int, /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[slice[None, None, None], Literal["med"]], _1: numpy.ndarray, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[slice[None, None, None], Literal["exp"]], _1: int, /
    ):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[slice[None, None, None], Literal["mtime"]], _1: numpy.ndarray, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[Literal["M0"], List[Literal["0"]]], _1: bool, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[Literal["M1"], List[Literal["0"]]], _1: bool, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[Literal["Q0"], List[Literal["0"]]], _1: bool, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[Literal["Q1"], List[Literal["0"]]], _1: bool, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["M0"], List[Literal["1", "0"]]], _1: bool, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["M1"], List[Literal["1", "0"]]], _1: bool, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["Q0"], List[Literal["1", "0"]]], _1: bool, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["Q1"], List[Literal["1", "0"]]], _1: bool, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["y1"], List[Literal["2", "1", "0"]]], _1: bool, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["y2"], List[Literal["2", "1", "0"]]], _1: bool, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["y1"], List[Literal["b", "a"]]], _1: bool, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["y2"], List[Literal["b", "a"]]], _1: bool, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[int, List[Literal["0"]]], _1: bool, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[Literal["y1"], List[Literal["0"]]], _1: bool, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[Literal["y2"], List[Literal["0"]]], _1: bool, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[int, List[Literal["global.2", "global.1"]]], _1: bool, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[int, List[Literal["block", "global"]]], _1: bool, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[int, List[Literal["global"]]], _1: bool, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["yM1_f1"], List[Literal["0"]]], _1: bool, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["yM2_f1"], List[Literal["0"]]], _1: bool, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["yQ1_f1"], List[Literal["0"]]], _1: bool, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["yQ2_f1"], List[Literal["0"]]], _1: bool, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[Literal["y"], List[Literal["0"]]], _1: bool, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[Literal["f1"], List[Literal["0"]]], _1: bool, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[Literal["f2"], List[Literal["0"]]], _1: bool, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["yM1_f1"], List[Literal["a"]]], _1: bool, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["yM2_f1"], List[Literal["a"]]], _1: bool, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["f1"], List[Literal["b.2", "b.1"]]], _1: bool, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["f2"], List[Literal["b.2", "b.1"]]], _1: bool, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["yM1_f2"], List[Literal["b.2", "b.1"]]], _1: bool, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["yM2_f2"], List[Literal["b.2", "b.1"]]], _1: bool, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["yQ1_f1"], List[Literal["a"]]], _1: bool, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["yQ2_f1"], List[Literal["a"]]], _1: bool, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["yQ1_f2"], List[Literal["b.2", "b.1"]]], _1: bool, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["yQ2_f2"], List[Literal["b.2", "b.1"]]], _1: bool, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["CPIAUCSL"], List[Literal["0"]]], _1: bool, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["UNRATE"], List[Literal["0"]]], _1: bool, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["PAYEMS"], List[Literal["0"]]], _1: bool, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[Literal["GDPC1"], List[Literal["0"]]], _1: bool, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["ULCNFB"], List[Literal["0"]]], _1: bool, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["CPIAUCSL"], List[Literal["1", "0"]]], _1: bool, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["UNRATE"], List[Literal["1", "0"]]], _1: bool, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["PAYEMS"], List[Literal["1", "0"]]], _1: bool, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["GDPC1"], List[Literal["1", "0"]]], _1: bool, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["ULCNFB"], List[Literal["1", "0"]]], _1: bool, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[Literal["CPIAUCSL"], List[Literal["test1", "global"]]],
        _1: bool,
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[Literal["UNRATE"], List[Literal["test2", "global"]]],
        _1: bool,
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[Literal["PAYEMS"], List[Literal["test2", "global"]]],
        _1: bool,
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[Literal["RSAFS"], List[Literal["test2", "test1", "global"]]],
        _1: bool,
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[Literal["TTLCONS"], List[Literal["test1", "global"]]],
        _1: bool,
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["TCU"], List[Literal["test2", "global"]]], _1: bool, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[Literal["GDPC1"], List[Literal["test2", "test1", "global"]]],
        _1: bool,
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["ULCNFB"], List[Literal["global"]]], _1: bool, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[
            Literal["CPIAUCSL"],
            List[Literal["test1.2", "test1.1", "global.2", "global.1"]],
        ],
        _1: bool,
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[
            Literal["UNRATE"],
            List[Literal["test2.2", "test2.1", "global.2", "global.1"]],
        ],
        _1: bool,
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[
            Literal["PAYEMS"],
            List[Literal["test2.2", "test2.1", "global.2", "global.1"]],
        ],
        _1: bool,
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[Literal["RSAFS"], List[str]], _1: bool, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[
            Literal["TTLCONS"],
            List[Literal["test1.2", "test1.1", "global.2", "global.1"]],
        ],
        _1: bool,
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[
            Literal["TCU"], List[Literal["test2.2", "test2.1", "global.2", "global.1"]]
        ],
        _1: bool,
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[Literal["GDPC1"], List[str]], _1: bool, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[Literal["ULCNFB"], List[Literal["global.2", "global.1"]]],
        _1: bool,
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[Literal["RSAFS"], List[Literal["0"]]], _1: bool, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["TTLCONS"], List[Literal["0"]]], _1: bool, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[Literal["TCU"], List[Literal["0"]]], _1: bool, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["CPIAUCSL"], List[Literal["2", "1", "0"]]], _1: bool, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["UNRATE"], List[Literal["2", "1", "0"]]], _1: bool, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["PAYEMS"], List[Literal["2", "1", "0"]]], _1: bool, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["RSAFS"], List[Literal["2", "1", "0"]]], _1: bool, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["TTLCONS"], List[Literal["2", "1", "0"]]], _1: bool, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["TCU"], List[Literal["2", "1", "0"]]], _1: bool, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["GDPC1"], List[Literal["2", "1", "0"]]], _1: bool, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["ULCNFB"], List[Literal["2", "1", "0"]]], _1: bool, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[Literal["yM_f1"], List[Literal["0"]]], _1: bool, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[Literal["yQ_f1"], List[Literal["0"]]], _1: bool, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[slice[None, None, None], Literal["2009Q2"]],
        _1: numpy.ndarray,
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[slice[None, None, None], Literal["2009Q3"]],
        _1: numpy.ndarray,
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[slice[None, None, None], Literal["2009Q4"]],
        _1: numpy.ndarray,
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[slice[None, None, None], Literal["2010Q1"]],
        _1: numpy.ndarray,
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[numpy.ndarray, Literal["x"]], _1: float, /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[pandas.core.series.Series, Literal["y"]], _1: float, /
    ):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[pandas.core.series.Series, Literal["Shape_Area"]], _1: float, /
    ):
        """
        usage.geopandas: 3
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[pandas.core.series.Series, Literal["Shape_Leng"]], _1: float, /
    ):
        """
        usage.geopandas: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[int, Literal["A"]], _1: int, /):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[int, Literal["BoroName"]], _1: float, /):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: int, _1: shapely.geometry.point.Point, /):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[int, Literal["geometry"]], _1: shapely.geometry.point.Point, /
    ):
        """
        usage.geopandas: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[int, Literal["value1"]], _1: int, /):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[int, Literal["value1"]], _1: float, /):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[int, Literal["values"]], _1: float, /):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[int, Literal["col1"]], _1: int, /):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[slice[None, None, None], Literal["DATE"]],
        _1: pandas.core.series.Series,
        /,
    ):
        """
        usage.pyjanitor: 2
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[pandas.core.series.Series, Literal["cities"]],
        _1: Literal["Durham"],
        /,
    ):
        """
        usage.pyjanitor: 1
        """
        ...

    def __setitem__(self, _0: object, _1: object, /):
        """
        usage.alphalens: 33
        usage.geopandas: 14
        usage.koalas: 33
        usage.prophet: 1
        usage.pyjanitor: 3
        usage.seaborn: 3
        usage.statsmodels: 210
        """
        ...


class _iAtIndexer:
    @overload
    def __getitem__(self, _0: Tuple[int, int], /):
        """
        usage.koalas: 3
        """
        ...

    @overload
    def __getitem__(self, _0: int, /):
        """
        usage.koalas: 1
        """
        ...

    def __getitem__(self, _0: Union[int, Tuple[int, int]], /):
        """
        usage.koalas: 4
        """
        ...


class _iLocIndexer:
    @overload
    def __getitem__(self, _0: slice[None, int, None], /):
        """
        usage.dask: 17
        usage.geopandas: 3
        usage.koalas: 11
        usage.prophet: 1
        usage.sklearn: 1
        usage.statsmodels: 72
        usage.xarray: 3
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, int], /):
        """
        usage.geopandas: 1
        usage.koalas: 2
        usage.sklearn: 1
        usage.statsmodels: 28
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, None, None], int], /):
        """
        usage.dask: 11
        usage.koalas: 3
        usage.sklearn: 8
        usage.statsmodels: 71
        """
        ...

    @overload
    def __getitem__(self, _0: int, /):
        """
        usage.alphalens: 2
        usage.dask: 9
        usage.geopandas: 3
        usage.koalas: 6
        usage.prophet: 10
        usage.seaborn: 2
        usage.sklearn: 1
        usage.statsmodels: 49
        usage.xarray: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, int, None], int], /):
        """
        usage.koalas: 4
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, None, None], List[int]], /):
        """
        usage.dask: 6
        usage.koalas: 4
        usage.modin: 1
        usage.pyjanitor: 1
        usage.seaborn: 4
        usage.sklearn: 2
        usage.statsmodels: 16
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, int, None], List[int]], /):
        """
        usage.koalas: 8
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, None, None], List[bool]], /):
        """
        usage.dask: 1
        usage.koalas: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, int, None], List[bool]], /):
        """
        usage.koalas: 4
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, None, None], slice[int, int, int]], /):
        """
        usage.koalas: 2
        usage.sklearn: 3
        usage.statsmodels: 13
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, int, None], slice[int, int, int]], /):
        """
        usage.koalas: 4
        """
        ...

    @overload
    def __getitem__(self, _0: list, /):
        """
        usage.koalas: 3
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[list, slice[None, None, None]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[list, slice[None, int, None]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __getitem__(self, _0: numpy.ndarray, /):
        """
        usage.dask: 1
        usage.koalas: 3
        usage.prophet: 2
        usage.sklearn: 1
        usage.statsmodels: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.ndarray, slice[None, None, None]], /):
        """
        usage.koalas: 1
        usage.statsmodels: 3
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.ndarray, slice[None, int, None]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[int], /):
        """
        usage.geopandas: 2
        usage.koalas: 9
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[int], slice[None, None, None]], /):
        """
        usage.geopandas: 1
        usage.koalas: 3
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[int], slice[None, int, None]], /):
        """
        usage.koalas: 3
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, None, None], /):
        """
        usage.dask: 1
        usage.koalas: 5
        """
        ...

    @overload
    def __getitem__(self, _0: slice[int, int, int], /):
        """
        usage.dask: 8
        usage.koalas: 3
        usage.sklearn: 1
        usage.statsmodels: 15
        """
        ...

    @overload
    def __getitem__(self, _0: slice[int, None, int], /):
        """
        usage.dask: 5
        usage.geopandas: 6
        usage.koalas: 3
        usage.statsmodels: 67
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, None, None], /):
        """
        usage.koalas: 3
        """
        ...

    @overload
    def __getitem__(self, _0: slice[int, int, int], /):
        """
        usage.koalas: 3
        usage.statsmodels: 9
        """
        ...

    @overload
    def __getitem__(self, _0: slice[int, None, int], /):
        """
        usage.koalas: 3
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, int, None], /):
        """
        usage.koalas: 3
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[slice[None, None, None], slice[None, int, None]], /
    ):
        """
        usage.statsmodels: 31
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[slice[None, int, None], slice[None, None, None]], /
    ):
        """
        usage.sklearn: 1
        usage.statsmodels: 6
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, slice[None, None, None]], /):
        """
        usage.pyjanitor: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, None, None], slice[int, None, int]], /):
        """
        usage.statsmodels: 19
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.ndarray, int], /):
        """
        usage.sklearn: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[int, int, int], slice[None, None, None]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, slice[None, int, None]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[int, None, int], slice[None, int, None]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[int, None, int], slice[int, None, int]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[slice[None, None, None], slice[None, None, None]], /
    ):
        """
        usage.prophet: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[int, int, int], slice[int, int, int]], /):
        """
        usage.modin: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, int, None], slice[None, int, None]], /):
        """
        usage.modin: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[int], List[int]], /):
        """
        usage.seaborn: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.ndarray, List[int]], /):
        """
        usage.seaborn: 2
        """
        ...

    @overload
    def __getitem__(self, _0: pandas.core.series.Series, /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[slice[None, None, None], slice[None, None, None]], /
    ):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[int], int], /):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, numpy.int64, None], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: slice[numpy.int64, numpy.int64, numpy.int64], /):
        """
        usage.dask: 3
        """
        ...

    @overload
    def __getitem__(self, _0: slice[numpy.int64, None, numpy.int64], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[int, int, int], int], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, None, None], slice[int, int, int]], /):
        """
        usage.dask: 4
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, None, None], numpy.ndarray], /):
        """
        usage.sklearn: 2
        """
        ...

    def __getitem__(self, _0: object, /):
        """
        usage.alphalens: 2
        usage.dask: 71
        usage.geopandas: 17
        usage.koalas: 98
        usage.modin: 3
        usage.prophet: 14
        usage.pyjanitor: 2
        usage.seaborn: 12
        usage.sklearn: 24
        usage.statsmodels: 407
        usage.xarray: 5
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[List[int], List[int]], _1: int, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[int, int], _1: int, /):
        """
        usage.koalas: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[slice[None, None, None], int],
        _1: pandas.core.frame.DataFrame,
        /,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: List[int], _1: int, /):
        """
        usage.koalas: 3
        """
        ...

    @overload
    def __setitem__(self, _0: int, _1: int, /):
        """
        usage.koalas: 5
        usage.statsmodels: 3
        """
        ...

    @overload
    def __setitem__(self, _0: slice[None, None, None], _1: int, /):
        """
        usage.koalas: 3
        """
        ...

    @overload
    def __setitem__(self, _0: slice[None, int, None], _1: int, /):
        """
        usage.koalas: 3
        """
        ...

    @overload
    def __setitem__(self, _0: slice[int, None, int], _1: int, /):
        """
        usage.koalas: 3
        """
        ...

    @overload
    def __setitem__(self, _0: List[int], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 6
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[List[int], List[int]], _1: pandas.core.series.Series, /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[List[int], int], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[slice[None, None, None], int], _1: List[str], /):
        """
        usage.statsmodels: 6
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[slice[None, None, None], int],
        _1: List[Literal["Kurtosis:", "Skew:", "Prob(Omnibus):", "Omnibus:"]],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[slice[None, None, None], int],
        _1: List[Literal["Kurtosis: ", "Skew: ", "Prob(Omnibus): ", "Omnibus: "]],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[slice[None, None, None], int],
        _1: List[Literal["Kurtosis:  ", "Skew:  ", "Prob(Omnibus):  ", "Omnibus:  "]],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[slice[None, None, None], int],
        _1: List[
            Literal[
                "Df Model:",
                "No. Observations:",
                "Date:",
                "Dependent Variable:",
                "Model:",
            ]
        ],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[int, int], _1: float, /):
        """
        usage.dask: 1
        usage.statsmodels: 14
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[slice[None, None, None], int],
        _1: List[
            Literal[
                "Num. events:", "Sample size:", "Ties:", "Dependent variable:", "Model:"
            ]
        ],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[slice[None, None, None], int],
        _1: List[
            Literal[
                "Num. events: ",
                "Sample size: ",
                "Ties: ",
                "Dependent variable: ",
                "Model: ",
            ]
        ],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[slice[None, None, None], int],
        _1: List[Literal["Ties:", "Dependent variable:", "Model:"]],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[numpy.ndarray, int], _1: numpy.ndarray, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[List[int], int], _1: float, /):
        """
        usage.dask: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[slice[None, None, None], int], _1: pandas.core.series.Series, /
    ):
        """
        usage.sklearn: 4
        usage.statsmodels: 3
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[slice[None, None, None], int], _1: List[Literal[""]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[slice[None, None, None], int], _1: List[Literal["  "]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[slice[None, None, None], int], _1: int, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[int, int], _1: numpy.float64, /):
        """
        usage.statsmodels: 11
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[slice[int, int, int], slice[None, None, None]], _1: float, /
    ):
        """
        usage.statsmodels: 4
        """
        ...

    @overload
    def __setitem__(self, _0: slice[int, None, int], _1: float, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: int, _1: float, /):
        """
        usage.dask: 2
        usage.geopandas: 2
        usage.statsmodels: 20
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[int, slice[int, int, int]], _1: float, /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __setitem__(self, _0: int, _1: numpy.float64, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[slice[None, None, None], slice[int, None, int]],
        _1: pandas.core.frame.DataFrame,
        /,
    ):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[int, list], _1: Literal["."], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: slice[int, int, int], _1: pandas.core.series.Series, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[slice[None, int, None], slice[None, None, None]], _1: float, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[slice[int, int, int], int], _1: float, /):
        """
        usage.statsmodels: 5
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[slice[None, None, None], List[int]],
        _1: pandas.core.frame.DataFrame,
        /,
    ):
        """
        usage.seaborn: 3
        """
        ...

    @overload
    def __setitem__(self, _0: int, _1: shapely.geometry.point.Point, /):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[int, int], _1: shapely.geometry.point.Point, /):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: int, _1: None, /):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[slice[None, int, None], int], _1: float, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[slice[None, None, None], numpy.int32], _1: numpy.float64, /
    ):
        """
        usage.sklearn: 1
        """
        ...

    def __setitem__(
        self,
        _0: Union[
            Tuple[
                Union[
                    int,
                    numpy.ndarray,
                    List[int],
                    slice[Union[None, int], Union[None, int], Union[None, int]],
                ],
                Union[
                    int,
                    numpy.int32,
                    List[int],
                    slice[Union[None, int], Union[None, int], Union[None, int]],
                ],
            ],
            slice[Union[int, None], Union[None, int], Union[int, None]],
            List[int],
            int,
        ],
        _1: object,
        /,
    ):
        """
        usage.dask: 5
        usage.geopandas: 5
        usage.koalas: 28
        usage.seaborn: 3
        usage.sklearn: 5
        usage.statsmodels: 88
        """
        ...
