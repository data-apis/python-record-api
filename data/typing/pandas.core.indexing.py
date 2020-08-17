from typing import *


class IndexingError:
    pass


class _LocIndexer:
    @overload
    def __getitem__(self, _0: object, /):
        """
        usage.dask: 263
        usage.xarray: 45
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Union[
            Tuple[
                slice[None, None, None],
                Union[
                    numpy.ndarray,
                    Literal["first", "col1", "second", "col_2"],
                    List[Union[str, bool]],
                    slice[
                        Union[None, Literal["col_1", "first"]],
                        Literal["col_2", "first", "second"],
                        Union[None, Literal["col_1", "first"]],
                    ],
                ],
            ],
            List[bool],
            numpy.ndarray,
        ],
        /,
    ):
        """
        usage.sklearn: 30
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
    def __getitem__(self, _0: Union[slice[None, int, None], int], /):
        """
        usage.xarray: 5
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
    def __getitem__(
        self,
        _0: Union[
            int,
            numpy.ndarray,
            List[int],
            Tuple[
                Union[int, numpy.ndarray, slice[None, Union[int, None], None]],
                Union[
                    List[int],
                    numpy.ndarray,
                    int,
                    slice[Union[None, int], Union[None, int], Union[None, int]],
                ],
            ],
            slice[Union[int, None], int, Union[int, None]],
        ],
        /,
    ):
        """
        usage.sklearn: 24
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
        self,
        _0: Tuple[slice[None, None, None], Union[numpy.int32, int]],
        _1: Union[pandas.core.series.Series, numpy.float64],
        /,
    ):
        """
        usage.sklearn: 5
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
