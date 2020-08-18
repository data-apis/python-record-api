from typing import *


class IndexingError:
    pass


class _LocIndexer:
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
    def __getitem__(self, _0: numpy.ndarray, /):
        """
        usage.sklearn: 1
        usage.xarray: 2
        """
        ...

    @overload
    def __getitem__(self, _0: object, /):
        """
        usage.dask: 263
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
    def __getitem__(self, _0: Tuple[slice[None, None, None], numpy.ndarray], /):
        """
        usage.sklearn: 3
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
    def __getitem__(self, _0: Tuple[slice[None, None, None], List[Literal["a"]]], /):
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
        usage.dask: 263
        usage.sklearn: 30
        usage.xarray: 45
        """
        ...


class _iLocIndexer:
    @overload
    def __getitem__(self, _0: int, /):
        """
        usage.sklearn: 1
        usage.xarray: 2
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, int, None], /):
        """
        usage.sklearn: 1
        usage.xarray: 3
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Union[
            Tuple[
                slice[Union[None, int], Union[None, int], Union[None, int]],
                Union[List[Union[int, bool]], int, slice[int, int, int]],
            ],
            slice[
                Union[None, numpy.int64, int],
                Union[None, int, numpy.int64],
                Union[None, numpy.int64, int],
            ],
            int,
            numpy.ndarray,
        ],
        /,
    ):
        """
        usage.dask: 72
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, None, None], int], /):
        """
        usage.sklearn: 8
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, None, None], List[int]], /):
        """
        usage.sklearn: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, None, None], numpy.ndarray], /):
        """
        usage.sklearn: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, None, None], slice[int, int, int]], /):
        """
        usage.sklearn: 3
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, None, None], slice[int, int, int]], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: numpy.ndarray, /):
        """
        usage.sklearn: 1
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

    @overload
    def __getitem__(self, _0: Tuple[int, int], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[int], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[int, int, int], /):
        """
        usage.sklearn: 1
        """
        ...

    def __getitem__(
        self,
        _0: Union[
            slice[
                Union[numpy.int64, int, None],
                Union[None, numpy.int64, int],
                Union[numpy.int64, int, None],
            ],
            Tuple[
                Union[
                    slice[Union[None, int], Union[None, int], Union[None, int]],
                    numpy.ndarray,
                    int,
                ],
                Union[
                    List[Union[int, bool]],
                    int,
                    numpy.ndarray,
                    slice[Union[int, None], Union[int, None], Union[int, None]],
                ],
            ],
            List[int],
            numpy.ndarray,
            int,
        ],
        /,
    ):
        """
        usage.dask: 72
        usage.sklearn: 24
        usage.xarray: 5
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Union[Tuple[Union[List[int], slice[None, int, None], int], int], int],
        _1: float,
        /,
    ):
        """
        usage.dask: 5
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
                Union[int, slice[None, Union[None, int], None], List[int]],
                Union[int, numpy.int32],
            ],
            int,
        ],
        _1: Union[numpy.float64, pandas.core.series.Series, float],
        /,
    ):
        """
        usage.dask: 5
        usage.sklearn: 5
        """
        ...
