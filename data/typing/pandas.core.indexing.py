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
        usage.koalas: 10
        usage.seaborn: 1
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
        usage.koalas: 6
        """
        ...

    @overload
    def __getitem__(self, _0: slice[int, None, int], /):
        """
        usage.dask: 5
        usage.koalas: 7
        """
        ...

    @overload
    def __getitem__(self, _0: List[int], /):
        """
        usage.dask: 8
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
        usage.koalas: 1
        usage.sklearn: 1
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
        usage.koalas: 7
        usage.seaborn: 2
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
    def __getitem__(
        self, _0: Tuple[slice[None, None, None], pandas.core.series.Series], /
    ):
        """
        usage.seaborn: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, None, None], numpy.ndarray], /):
        """
        usage.seaborn: 1
        usage.sklearn: 3
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
    def __getitem__(self, _0: pandas.core.indexes.base.Index, /):
        """
        usage.dask: 1
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
    def __getitem__(
        self, _0: Tuple[pandas.core.series.Series, slice[None, None, None]], /
    ):
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
    def __getitem__(self, _0: List[bool], /):
        """
        usage.sklearn: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, None, None], List[bool]], /):
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
        usage.dask: 250
        usage.koalas: 137
        usage.seaborn: 14
        usage.sklearn: 30
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
    def __setitem__(self, _0: pandas.core.series.Series, _1: float, /):
        """
        usage.seaborn: 1
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

    def __setitem__(
        self,
        _0: object,
        _1: Union[float, pandas.core.frame.DataFrame, int, pandas.core.series.Series],
        /,
    ):
        """
        usage.koalas: 33
        usage.seaborn: 3
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
        usage.koalas: 11
        usage.sklearn: 1
        usage.xarray: 3
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, int], /):
        """
        usage.koalas: 2
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, None, None], int], /):
        """
        usage.dask: 11
        usage.koalas: 3
        usage.sklearn: 8
        """
        ...

    @overload
    def __getitem__(self, _0: int, /):
        """
        usage.dask: 9
        usage.koalas: 6
        usage.seaborn: 2
        usage.sklearn: 1
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
        usage.seaborn: 4
        usage.sklearn: 2
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
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.ndarray, slice[None, None, None]], /):
        """
        usage.koalas: 1
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
        usage.koalas: 9
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[int], slice[None, None, None]], /):
        """
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
        """
        ...

    @overload
    def __getitem__(self, _0: slice[int, None, int], /):
        """
        usage.dask: 5
        usage.koalas: 3
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

    @overload
    def __getitem__(self, _0: Tuple[numpy.ndarray, int], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[slice[None, int, None], slice[None, None, None]], /
    ):
        """
        usage.sklearn: 1
        """
        ...

    def __getitem__(self, _0: object, /):
        """
        usage.dask: 71
        usage.koalas: 98
        usage.modin: 3
        usage.seaborn: 12
        usage.sklearn: 24
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
    def __setitem__(self, _0: Tuple[slice[None, int, None], int], _1: float, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(self, _0: int, _1: float, /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[List[int], int], _1: float, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[int, int], _1: float, /):
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

    @overload
    def __setitem__(
        self, _0: Tuple[slice[None, None, None], int], _1: pandas.core.series.Series, /
    ):
        """
        usage.sklearn: 4
        """
        ...

    def __setitem__(
        self,
        _0: Union[
            Tuple[
                Union[int, List[int], slice[None, Union[None, int], None]],
                Union[int, numpy.int32, List[int]],
            ],
            slice[Union[int, None], Union[None, int], Union[int, None]],
            List[int],
            int,
        ],
        _1: Union[
            numpy.float64,
            pandas.core.series.Series,
            pandas.core.frame.DataFrame,
            int,
            float,
        ],
        /,
    ):
        """
        usage.dask: 5
        usage.koalas: 28
        usage.seaborn: 3
        usage.sklearn: 5
        """
        ...
