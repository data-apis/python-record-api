from typing import *


class CClass:
    @overload
    def __getitem__(self, _0: Tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray], /):
        """
        usage.scipy: 9
        usage.skimage: 1
        usage.sklearn: 1
        usage.statsmodels: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.ndarray, numpy.ndarray], /):
        """
        usage.matplotlib: 1
        usage.pandas: 3
        usage.scipy: 12
        usage.seaborn: 5
        usage.sklearn: 38
        usage.statsmodels: 107
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[pandas.core.series.Series, pandas.core.frame.DataFrame], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[float], List[float], numpy.ndarray], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.recarray, numpy.recarray], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[int], numpy.ndarray], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[numpy.float64], List[numpy.float64]], /):
        """
        usage.statsmodels: 5
        """
        ...

    @overload
    def __getitem__(self, _0: List[Tuple[numpy.ndarray, numpy.ndarray]], /):
        """
        usage.statsmodels: 5
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[List[Union[float, int]], List[Union[float, int]]], /
    ):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[float], List[float]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[Union[float, int]], List[float]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray, numpy.ndarray], /
    ):
        """
        usage.scipy: 1
        usage.statsmodels: 10
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[pandas.core.series.Series, pandas.core.series.Series], /
    ):
        """
        usage.seaborn: 2
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[int], List[int]], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    def __getitem__(self, _0: numpy.float64, /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __getitem__(self, _0: numpy.ndarray, /):
        """
        usage.seaborn: 1
        usage.sklearn: 1
        usage.statsmodels: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.ndarray, List[complex]], /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.ndarray, pandas.core.series.Series], /):
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

    def __getitem__(
        self,
        _0: Union[
            numpy.ndarray,
            numpy.float64,
            pandas.core.series.Series,
            Tuple[
                Union[
                    List[Union[int, numpy.float64, float, complex]],
                    numpy.recarray,
                    pandas.core.series.Series,
                    pandas.core.frame.DataFrame,
                    numpy.ndarray,
                ],
                ...,
            ],
            List[Tuple[numpy.ndarray, numpy.ndarray]],
        ],
        /,
    ):
        """
        usage.matplotlib: 1
        usage.pandas: 3
        usage.scipy: 23
        usage.seaborn: 11
        usage.skimage: 1
        usage.sklearn: 40
        usage.statsmodels: 145
        """
        ...


class IndexExpression:
    @overload
    def __getitem__(self, _0: Tuple[slice[int, int, int], slice[int, int, int]], /):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[Literal["transition"], slice[int, int, int], int], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[Literal["selection"], slice[int, int, int], int], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: ellipsis, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[int, numpy.int64, int], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[numpy.int64, numpy.int64, numpy.int64], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __getitem__(self, _0: slice[int, int, int], /):
        """
        usage.matplotlib: 1
        usage.scipy: 5
        usage.statsmodels: 13
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[Literal["design"], slice[None, None, None], slice[None, int, None]],
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
            Literal["obs_intercept"], slice[None, int, None], slice[None, None, None]
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
            Literal["transition"], slice[None, int, None], slice[None, int, None]
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
        _0: Tuple[Literal["transition"], slice[int, int, int], slice[int, int, int]],
        /,
    ):
        """
        usage.statsmodels: 4
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, int, None], /):
        """
        usage.scipy: 3
        usage.statsmodels: 2
        """
        ...

    @overload
    def __getitem__(self, _0: slice[int, None, int], /):
        """
        usage.scipy: 2
        usage.statsmodels: 2
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            Literal["state_intercept"], slice[None, int, None], slice[None, None, None]
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
            Literal["transition"], slice[None, int, None], slice[None, None, None]
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
            Literal["state_intercept"], slice[None, int, None], slice[None, int, None]
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
        _0: Tuple[Literal["obs_cov"], slice[None, None, None], slice[None, None, None]],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[Literal["selection"], slice[int, int, int], slice[int, int, int]],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[Literal["transition"], numpy.ndarray, numpy.ndarray], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, None, None], /):
        """
        usage.scipy: 3
        usage.sklearn: 1
        usage.statsmodels: 3
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[slice[None, None, None], slice[None, None, None]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[List[Literal["global.2", "global.1"]], slice[None, None, None]],
        /,
    ):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[List[Literal["block", "global"]], slice[None, None, None]], /
    ):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[Literal["transition"], int, slice[int, int, int]], /
    ):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[Literal["transition"], slice[None, int, None], slice[int, None, int]],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: int, /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["design"], int, slice[int, int, int]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[numpy.ndarray, numpy.ndarray, slice[None, None, None]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, None, None], /):
        """
        usage.pandas: 2
        """
        ...

    @overload
    def __getitem__(self, _0: slice[int, None, int], /):
        """
        usage.scipy: 4
        """
        ...

    @overload
    def __getitem__(self, _0: slice[int, int, int], /):
        """
        usage.matplotlib: 1
        usage.scipy: 2
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, int, None], /):
        """
        usage.scipy: 2
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, None, None], /):
        """
        usage.sklearn: 1
        """
        ...

    def __getitem__(
        self,
        _0: Union[
            slice[
                Union[None, numpy.int64, int],
                Union[numpy.int64, int, None],
                Union[None, numpy.int64, int],
            ],
            ellipsis,
            int,
            Tuple[
                Union[
                    slice[Union[int, None], Union[int, None], Union[int, None]],
                    List[Literal["block", "global", "global.2", "global.1"]],
                    int,
                    numpy.ndarray,
                    str,
                ],
                ...,
            ],
        ],
        /,
    ):
        """
        usage.matplotlib: 2
        usage.pandas: 2
        usage.scipy: 21
        usage.skimage: 1
        usage.sklearn: 2
        usage.statsmodels: 51
        """
        ...


class MGridClass:
    @overload
    def __getitem__(
        self,
        _0: Tuple[
            slice[numpy.float64, numpy.float64, numpy.float64],
            slice[numpy.float64, numpy.float64, numpy.float64],
            slice[numpy.float64, numpy.float64, numpy.float64],
        ],
        /,
    ):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[int, int, int], slice[int, int, int]], /):
        """
        usage.matplotlib: 1
        usage.scipy: 1
        usage.skimage: 47
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            slice[numpy.float64, numpy.float64, numpy.float64],
            slice[numpy.float64, numpy.float64, numpy.float64],
        ],
        /,
    ):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[slice[int, float, int]], /):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, int, None], slice[None, int, None]], /):
        """
        usage.skimage: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, int, None], slice[None, int, None]], /):
        """
        usage.matplotlib: 1
        usage.skimage: 2
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            slice[None, int, None], slice[None, int, None], slice[None, int, None]
        ],
        /,
    ):
        """
        usage.skimage: 2
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            slice[numpy.float64, numpy.float64, numpy.float64],
            slice[numpy.float64, numpy.float64, numpy.float64],
            slice[numpy.float64, numpy.float64, numpy.float64],
        ],
        /,
    ):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[slice[numpy.int64, numpy.int64, numpy.int64]], /):
        """
        usage.skimage: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, int, None], slice[None, int, None]], /):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[slice[int, int, int], slice[int, int, int], slice[int, int, int]],
        /,
    ):
        """
        usage.skimage: 2
        """
        ...

    @overload
    def __getitem__(self, _0: List[slice[None, int, None]], /):
        """
        usage.skimage: 3
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            slice[None, numpy.int64, None],
            slice[None, numpy.int64, None],
            slice[None, numpy.int64, None],
        ],
        /,
    ):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[int, int, int], slice[int, int, int]], /):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[slice[int, int, int], slice[int, int, int], slice[int, int, int]],
        /,
    ):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            slice[int, int, int],
            slice[int, int, int],
            slice[int, int, int],
            slice[int, int, int],
        ],
        /,
    ):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            slice[int, int, int],
            slice[int, int, int],
            slice[int, int, int],
            slice[int, int, int],
            slice[int, int, int],
        ],
        /,
    ):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            slice[int, int, int],
            slice[int, int, int],
            slice[int, int, int],
            slice[int, int, int],
            slice[int, int, int],
            slice[int, int, int],
        ],
        /,
    ):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            slice[int, int, int],
            slice[int, int, int],
            slice[int, int, int],
            slice[int, int, int],
            slice[int, int, int],
            slice[int, int, int],
            slice[int, int, int],
        ],
        /,
    ):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[int, int, int], slice[int, float, int]], /):
        """
        usage.scipy: 2
        """
        ...

    @overload
    def __getitem__(self, _0: List[slice[int, int, int]], /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[int, int, int], /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[int, float, int], slice[int, float, int]], /):
        """
        usage.matplotlib: 3
        usage.scipy: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[int, int, int], slice[int, int, int]], /):
        """
        usage.matplotlib: 2
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[slice[float, float, float], slice[float, float, float]], /
    ):
        """
        usage.matplotlib: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[int, int, int], slice[None, int, None]], /):
        """
        usage.matplotlib: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[int, float, int], slice[int, float, int]], /):
        """
        usage.matplotlib: 1
        """
        ...

    def __getitem__(
        self,
        _0: Union[
            Tuple[
                slice[
                    Union[None, numpy.float64, int, float],
                    Union[int, numpy.float64, numpy.int64, float],
                    Union[None, numpy.float64, int, float],
                ],
                ...,
            ],
            List[
                slice[
                    Union[int, numpy.int64, None],
                    Union[int, numpy.int64, float],
                    Union[int, numpy.int64, None],
                ]
            ],
            slice[int, int, int],
        ],
        /,
    ):
        """
        usage.matplotlib: 12
        usage.scipy: 6
        usage.skimage: 72
        usage.sklearn: 1
        """
        ...


class OGridClass:
    @overload
    def __getitem__(self, _0: Tuple[slice[int, float, int], slice[int, float, int]], /):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[int, int, int], slice[int, int, int]], /):
        """
        usage.skimage: 5
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[slice[int, int, int], slice[int, int, int], slice[int, int, int]],
        /,
    ):
        """
        usage.skimage: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[int, int, int], slice[int, int, int]], /):
        """
        usage.matplotlib: 3
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, int, None], slice[None, int, None]], /):
        """
        usage.dask: 1
        usage.scipy: 2
        usage.skimage: 2
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            slice[None, int, None], slice[None, int, None], slice[None, int, None]
        ],
        /,
    ):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[int, int, int], slice[int, float, int]], /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[slice[int, int, int]], /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[int, int, int], slice[int, int, int]], /):
        """
        usage.matplotlib: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, int, None]], /):
        """
        usage.dask: 1
        """
        ...

    def __getitem__(
        self,
        _0: Union[
            Tuple[slice[Union[None, int], Union[int, float], Union[None, int]], ...],
            List[slice[int, int, int]],
        ],
        /,
    ):
        """
        usage.dask: 2
        usage.matplotlib: 4
        usage.scipy: 4
        usage.skimage: 12
        """
        ...


class RClass:
    @overload
    def __getitem__(self, _0: Tuple[float, float], /):
        """
        usage.skimage: 2
        usage.statsmodels: 31
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, int, int, int, int], /):
        """
        usage.skimage: 1
        usage.statsmodels: 6
        """
        ...

    @overload
    def __getitem__(self, _0: List[List[Union[int, float]]], /):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[List[int]], /):
        """
        usage.skimage: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, int, int], /):
        """
        usage.scipy: 2
        usage.skimage: 3
        usage.statsmodels: 18
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[float, float, float], /):
        """
        usage.scipy: 2
        usage.skimage: 2
        usage.statsmodels: 7
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[float, int, int], /):
        """
        usage.skimage: 2
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: numpy.ndarray, /):
        """
        usage.scipy: 6
        usage.skimage: 3
        usage.statsmodels: 3
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Tuple[float, float], float], /):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, numpy.ndarray], /):
        """
        usage.scipy: 5
        usage.seaborn: 2
        usage.sklearn: 3
        usage.statsmodels: 69
        usage.xarray: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, int, None], /):
        """
        usage.xarray: 2
        """
        ...

    @overload
    def __getitem__(self, _0: numpy.float64, /):
        """
        usage.statsmodels: 7
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.ndarray, numpy.float64], /):
        """
        usage.scipy: 1
        usage.sklearn: 1
        usage.statsmodels: 6
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[int, int, int, int, int, int, int, int, int, int], /
    ):
        """
        usage.statsmodels: 57
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, int], /):
        """
        usage.scipy: 2
        usage.statsmodels: 48
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int], /):
        """
        usage.statsmodels: 13
        """
        ...

    @overload
    def __getitem__(self, _0: float, /):
        """
        usage.statsmodels: 17
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, float], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, int, int, int], /):
        """
        usage.statsmodels: 12
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, int, float, int], /):
        """
        usage.statsmodels: 4
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[float, numpy.ndarray], /):
        """
        usage.scipy: 4
        usage.seaborn: 2
        usage.statsmodels: 8
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, int, int, int, int, int, int, int, int], /):
        """
        usage.statsmodels: 12
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[float, numpy.ndarray, float], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.float64, numpy.ndarray, numpy.float64], /):
        """
        usage.scipy: 3
        usage.sklearn: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[float, float, float, float], /):
        """
        usage.scipy: 1
        usage.statsmodels: 21
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.int64, numpy.int64], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[float, float, float, float, float], /):
        """
        usage.statsmodels: 20
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[float, float, float, float, float, float, float, float], /
    ):
        """
        usage.statsmodels: 5
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, int, int, int, int, int, int], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[float, float, float, float, float, float, float], /
    ):
        """
        usage.statsmodels: 8
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, int, int, int, int, int, int, int], /):
        """
        usage.statsmodels: 10
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.ndarray, numpy.ndarray], /):
        """
        usage.matplotlib: 4
        usage.scipy: 38
        usage.sklearn: 16
        usage.statsmodels: 47
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, int, int, float], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.float64, numpy.ndarray], /):
        """
        usage.scipy: 1
        usage.sklearn: 2
        usage.statsmodels: 5
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, float, float], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[int], int, int], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[float, float, float, float, float, float, float, float, int, float],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[float, float, float, float, float, float], /):
        """
        usage.statsmodels: 4
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, numpy.ndarray, int], /):
        """
        usage.scipy: 10
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, int, int, int, float], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    def __getitem__(self, _0: int, /):
        """
        usage.scipy: 2
        usage.statsmodels: 6
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[list, list, List[int], List[int]], /):
        """
        usage.statsmodels: 8
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[list, List[int], List[int], list], /):
        """
        usage.statsmodels: 8
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            list,
            numpy.ndarray,
            numpy.ndarray,
            list,
            list,
            list,
            list,
            list,
            numpy.ndarray,
        ],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[bool], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[int], /):
        """
        usage.sklearn: 1
        usage.statsmodels: 7
        """
        ...

    @overload
    def __getitem__(self, _0: List[numpy.float64], /):
        """
        usage.statsmodels: 10
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, float, int], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[float], numpy.ndarray, List[float]], /):
        """
        usage.statsmodels: 6
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.ndarray, numpy.ndarray, numpy.float64], /):
        """
        usage.statsmodels: 4
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, int, numpy.ndarray], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray, numpy.ndarray, float],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, pandas.core.series.Series], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            list,
            list,
            numpy.ndarray,
            numpy.ndarray,
            list,
            list,
            list,
            list,
            numpy.ndarray,
        ],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[list, list, List[int], list], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[list, List[int], list, list], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            list, numpy.ndarray, numpy.ndarray, list, list, list, list, list, list
        ],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[int], list, List[int], list], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[int], List[int], list, list], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            list,
            numpy.ndarray,
            numpy.ndarray,
            numpy.ndarray,
            list,
            list,
            list,
            list,
            numpy.ndarray,
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
            list,
            list,
            numpy.ndarray,
            list,
            numpy.ndarray,
            list,
            list,
            list,
            numpy.ndarray,
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
            list, numpy.ndarray, list, list, list, list, list, list, numpy.ndarray
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
        _0: Tuple[list, numpy.ndarray, list, list, list, list, list, list, list],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[int], List[int], List[int], List[int]], /):
        """
        usage.statsmodels: 6
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[int], List[int], List[int], list], /):
        """
        usage.statsmodels: 9
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            list,
            numpy.ndarray,
            numpy.ndarray,
            numpy.ndarray,
            numpy.ndarray,
            numpy.ndarray,
            list,
            list,
            list,
        ],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, List[float]], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, int, int, int, int, int], /):
        """
        usage.statsmodels: 4
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[list, numpy.ndarray, numpy.ndarray, list, list, numpy.float64],
        /,
    ):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[list, numpy.ndarray, numpy.ndarray, list, list, float], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[list, numpy.ndarray, numpy.ndarray, list, list, int], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            list, numpy.ndarray, numpy.ndarray, numpy.ndarray, list, numpy.float64
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
            list, numpy.ndarray, numpy.ndarray, list, numpy.ndarray, numpy.float64
        ],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.ndarray, list, list, list, list, float], /):
        """
        usage.statsmodels: 4
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.ndarray, list, list, list, list, int], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray, list, list, float],
        /,
    ):
        """
        usage.statsmodels: 4
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            numpy.ndarray, numpy.ndarray, numpy.ndarray, numpy.ndarray, list, float
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
            numpy.ndarray, numpy.ndarray, numpy.ndarray, list, numpy.ndarray, float
        ],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray, list, list, int], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[numpy.ndarray, numpy.ndarray, list, list, list, float], /
    ):
        """
        usage.statsmodels: 4
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[numpy.ndarray, numpy.ndarray, list, numpy.ndarray, list, float],
        /,
    ):
        """
        usage.statsmodels: 7
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[numpy.ndarray, numpy.ndarray, list, list, list, int], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[numpy.ndarray, list, list, numpy.ndarray, numpy.ndarray, float],
        /,
    ):
        """
        usage.statsmodels: 4
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            numpy.ndarray, numpy.ndarray, list, numpy.ndarray, numpy.ndarray, float
        ],
        /,
    ):
        """
        usage.statsmodels: 6
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            numpy.ndarray, list, numpy.ndarray, numpy.ndarray, numpy.ndarray, float
        ],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[numpy.ndarray, list, list, numpy.ndarray, numpy.ndarray, int], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[numpy.ndarray, numpy.ndarray, list, numpy.ndarray, list, int], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            numpy.ndarray,
            numpy.ndarray,
            numpy.ndarray,
            numpy.ndarray,
            numpy.ndarray,
            float,
        ],
        /,
    ):
        """
        usage.statsmodels: 8
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            numpy.ndarray, numpy.ndarray, list, numpy.ndarray, numpy.ndarray, int
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
            numpy.ndarray,
            numpy.ndarray,
            numpy.ndarray,
            numpy.ndarray,
            numpy.ndarray,
            int,
        ],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[numpy.ndarray, list, list, list, numpy.ndarray, float], /
    ):
        """
        usage.statsmodels: 4
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[numpy.ndarray, list, numpy.ndarray, list, numpy.ndarray, float],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[numpy.ndarray, list, list, list, numpy.ndarray, int], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            numpy.ndarray,
            numpy.ndarray,
            numpy.ndarray,
            numpy.ndarray,
            numpy.ndarray,
            list,
        ],
        /,
    ):
        """
        usage.statsmodels: 8
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[Literal["1959"]], List[int]], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.ndarray, List[Literal["1962"]]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.ndarray, List[Literal["1961"]]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.ndarray, List[float]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[float], numpy.ndarray], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.ndarray, List[List[float]]], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[List[float]], numpy.ndarray], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[int], list, List[int], List[int]], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            numpy.ndarray,
            list,
            list,
            numpy.ndarray,
            list,
            list,
            list,
            list,
            numpy.ndarray,
        ],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.float64, pandas.core.series.Series], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.ndarray, numpy.ndarray, int], /):
        """
        usage.statsmodels: 7
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.ndarray, numpy.ndarray, float], /):
        """
        usage.statsmodels: 6
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray, int], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray, float], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[list, list], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: list, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[bool], list], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            List[float], float, float, int, float, float, float, float, float, float
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
        _0: Tuple[float, int, float, float, float, float, float, float, float, float],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[bool], List[bool]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            List[float], float, float, float, float, float, float, float, float, float
        ],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[int], List[float], float], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[int], List[int]], /):
        """
        usage.scipy: 19
        usage.sklearn: 2
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            list, list, numpy.ndarray, list, list, list, list, list, numpy.ndarray
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
        _0: Tuple[list, list, numpy.ndarray, list, list, list, list, list, list],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, numpy.float64], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[list, List[int], List[int], List[int]], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            list,
            list,
            numpy.ndarray,
            list,
            numpy.ndarray,
            numpy.ndarray,
            list,
            list,
            numpy.ndarray,
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
            numpy.ndarray,
            numpy.ndarray,
            numpy.ndarray,
            list,
            numpy.ndarray,
            numpy.ndarray,
            list,
            list,
            numpy.ndarray,
        ],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[float], /):
        """
        usage.statsmodels: 4
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[int], float, float, int, float, float], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[float], List[float], float], /):
        """
        usage.statsmodels: 4
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[bool, pandas.core.series.Series], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[bool, pandas.core.series.Series, List[bool]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[bool, pandas.core.series.Series, list], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            numpy.ndarray,
            list,
            numpy.ndarray,
            list,
            list,
            list,
            list,
            list,
            numpy.ndarray,
        ],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[float], float, float, List[float]], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, numpy.ndarray, float], /):
        """
        usage.scipy: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[List[float], float, float, List[int], List[float]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[float, List[int]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.ndarray, numpy.complex128], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.ndarray, float], /):
        """
        usage.scipy: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[numpy.float64, int, int, pandas.core.series.Series], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[pandas.core.series.Series, int], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[pandas.core.series.Series, pandas.core.series.Series, numpy.float64],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.ndarray, int, numpy.ndarray], /):
        """
        usage.scipy: 2
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, float, List[int]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, List[int]], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, List[float], List[float]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, List[float], float], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[float, List[float], float], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[float], float], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[float], numpy.ndarray, numpy.ndarray], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[list, list, list, list], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            numpy.ndarray,
            list,
            numpy.ndarray,
            numpy.ndarray,
            list,
            list,
            list,
            list,
            numpy.ndarray,
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
        _0: Tuple[list, list, list, list, list, list, List[int], int, numpy.ndarray],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[float, int], /):
        """
        usage.seaborn: 2
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.float64, numpy.float64], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[float, float, float, float, float, float, float, float, float],
        /,
    ):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[float, float, int], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[float], List[float]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            list,
            list,
            list,
            numpy.ndarray,
            list,
            numpy.ndarray,
            list,
            list,
            numpy.ndarray,
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
            list, list, list, numpy.ndarray, list, list, list, list, numpy.ndarray
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
            list,
            numpy.ndarray,
            list,
            numpy.ndarray,
            list,
            list,
            list,
            list,
            numpy.ndarray,
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
            list, list, list, list, numpy.ndarray, list, list, list, numpy.ndarray
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
            numpy.ndarray,
            list,
            list,
            list,
            numpy.ndarray,
            list,
            list,
            list,
            numpy.ndarray,
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
            list,
            numpy.ndarray,
            list,
            list,
            numpy.ndarray,
            list,
            list,
            list,
            numpy.ndarray,
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
            list, list, list, list, list, numpy.ndarray, list, list, numpy.ndarray
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
            numpy.ndarray,
            list,
            list,
            list,
            list,
            numpy.ndarray,
            list,
            list,
            numpy.ndarray,
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
            list,
            numpy.ndarray,
            list,
            list,
            list,
            numpy.ndarray,
            list,
            list,
            numpy.ndarray,
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
            list,
            list,
            list,
            list,
            numpy.ndarray,
            numpy.ndarray,
            list,
            list,
            numpy.ndarray,
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
            numpy.ndarray,
            list,
            list,
            list,
            numpy.ndarray,
            numpy.ndarray,
            list,
            list,
            numpy.ndarray,
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
            list,
            numpy.ndarray,
            list,
            list,
            numpy.ndarray,
            numpy.ndarray,
            list,
            list,
            numpy.ndarray,
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
            list,
            numpy.ndarray,
            numpy.ndarray,
            numpy.ndarray,
            numpy.ndarray,
            numpy.ndarray,
            list,
            list,
            numpy.ndarray,
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
            numpy.ndarray,
            numpy.ndarray,
            numpy.ndarray,
            numpy.ndarray,
            list,
            list,
            list,
            list,
            numpy.ndarray,
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
        _0: Tuple[list, list, list, list, list, list, list, list, numpy.ndarray],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[list, List[int], list, List[int]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[list, list, numpy.ndarray, list, list, list, list, int, list], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.ndarray, int], /):
        """
        usage.scipy: 6
        usage.sklearn: 2
        usage.statsmodels: 10
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            numpy.ndarray, list, numpy.ndarray, list, list, list, list, int, list
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
            numpy.ndarray, list, numpy.ndarray, list, list, list, list, list, list
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
            list,
            list,
            numpy.ndarray,
            list,
            numpy.ndarray,
            numpy.ndarray,
            list,
            int,
            list,
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
            list,
            list,
            numpy.ndarray,
            list,
            numpy.ndarray,
            numpy.ndarray,
            list,
            list,
            list,
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
            numpy.ndarray,
            list,
            numpy.ndarray,
            list,
            numpy.ndarray,
            numpy.ndarray,
            list,
            int,
            list,
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
            numpy.ndarray,
            list,
            numpy.ndarray,
            list,
            numpy.ndarray,
            numpy.ndarray,
            list,
            list,
            list,
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
            list, list, numpy.ndarray, numpy.ndarray, list, list, list, int, list
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
            list, list, numpy.ndarray, numpy.ndarray, list, list, list, list, list
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
            numpy.ndarray,
            list,
            numpy.ndarray,
            numpy.ndarray,
            list,
            list,
            list,
            int,
            list,
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
            numpy.ndarray,
            list,
            numpy.ndarray,
            numpy.ndarray,
            list,
            list,
            list,
            list,
            list,
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
            list,
            list,
            numpy.ndarray,
            numpy.ndarray,
            numpy.ndarray,
            numpy.ndarray,
            list,
            int,
            list,
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
            list,
            list,
            numpy.ndarray,
            numpy.ndarray,
            numpy.ndarray,
            numpy.ndarray,
            list,
            list,
            list,
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
            numpy.ndarray,
            list,
            numpy.ndarray,
            numpy.ndarray,
            numpy.ndarray,
            numpy.ndarray,
            list,
            int,
            list,
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
            numpy.ndarray,
            list,
            numpy.ndarray,
            numpy.ndarray,
            numpy.ndarray,
            numpy.ndarray,
            list,
            list,
            list,
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
        _0: Tuple[list, list, numpy.ndarray, list, list, list, List[int], int, list],
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
            list, numpy.ndarray, numpy.ndarray, list, list, list, list, int, list
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
        _0: Tuple[list, list, numpy.ndarray, list, list, list, List[int], list, list],
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
            numpy.ndarray, list, numpy.ndarray, list, list, list, List[int], int, list
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
            numpy.ndarray,
            numpy.ndarray,
            numpy.ndarray,
            list,
            list,
            list,
            list,
            int,
            list,
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
            numpy.ndarray, list, numpy.ndarray, list, list, list, List[int], list, list
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
            numpy.ndarray,
            numpy.ndarray,
            numpy.ndarray,
            list,
            list,
            list,
            list,
            list,
            list,
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
            list,
            list,
            numpy.ndarray,
            list,
            numpy.ndarray,
            numpy.ndarray,
            List[int],
            int,
            list,
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
            list,
            numpy.ndarray,
            numpy.ndarray,
            list,
            numpy.ndarray,
            numpy.ndarray,
            list,
            int,
            list,
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
            list,
            list,
            numpy.ndarray,
            list,
            numpy.ndarray,
            numpy.ndarray,
            List[int],
            list,
            list,
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
            list,
            numpy.ndarray,
            numpy.ndarray,
            list,
            numpy.ndarray,
            numpy.ndarray,
            list,
            list,
            list,
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
            numpy.ndarray,
            list,
            numpy.ndarray,
            list,
            numpy.ndarray,
            numpy.ndarray,
            List[int],
            int,
            list,
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
            numpy.ndarray,
            numpy.ndarray,
            numpy.ndarray,
            list,
            numpy.ndarray,
            numpy.ndarray,
            list,
            int,
            list,
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
            numpy.ndarray,
            list,
            numpy.ndarray,
            list,
            numpy.ndarray,
            numpy.ndarray,
            List[int],
            list,
            list,
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
            numpy.ndarray,
            numpy.ndarray,
            numpy.ndarray,
            list,
            numpy.ndarray,
            numpy.ndarray,
            list,
            list,
            list,
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
            list, list, numpy.ndarray, numpy.ndarray, list, list, List[int], int, list
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
            list,
            numpy.ndarray,
            numpy.ndarray,
            numpy.ndarray,
            list,
            list,
            list,
            int,
            list,
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
            list, list, numpy.ndarray, numpy.ndarray, list, list, List[int], list, list
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
            list,
            numpy.ndarray,
            numpy.ndarray,
            numpy.ndarray,
            list,
            list,
            list,
            list,
            list,
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
            numpy.ndarray,
            list,
            numpy.ndarray,
            numpy.ndarray,
            list,
            list,
            List[int],
            int,
            list,
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
            numpy.ndarray,
            numpy.ndarray,
            numpy.ndarray,
            numpy.ndarray,
            list,
            list,
            list,
            int,
            list,
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
            numpy.ndarray,
            list,
            numpy.ndarray,
            numpy.ndarray,
            list,
            list,
            List[int],
            list,
            list,
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
            numpy.ndarray,
            numpy.ndarray,
            numpy.ndarray,
            numpy.ndarray,
            list,
            list,
            list,
            list,
            list,
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
            list,
            list,
            numpy.ndarray,
            numpy.ndarray,
            numpy.ndarray,
            numpy.ndarray,
            List[int],
            int,
            list,
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
            list,
            numpy.ndarray,
            numpy.ndarray,
            numpy.ndarray,
            numpy.ndarray,
            numpy.ndarray,
            list,
            int,
            list,
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
            list,
            list,
            numpy.ndarray,
            numpy.ndarray,
            numpy.ndarray,
            numpy.ndarray,
            List[int],
            list,
            list,
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
            numpy.ndarray,
            list,
            numpy.ndarray,
            numpy.ndarray,
            numpy.ndarray,
            numpy.ndarray,
            List[int],
            int,
            list,
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
            numpy.ndarray,
            numpy.ndarray,
            numpy.ndarray,
            numpy.ndarray,
            numpy.ndarray,
            numpy.ndarray,
            list,
            int,
            list,
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
            numpy.ndarray,
            list,
            numpy.ndarray,
            numpy.ndarray,
            numpy.ndarray,
            numpy.ndarray,
            List[int],
            list,
            list,
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
            numpy.ndarray,
            numpy.ndarray,
            numpy.ndarray,
            numpy.ndarray,
            numpy.ndarray,
            numpy.ndarray,
            list,
            list,
            list,
        ],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.ndarray, float, int, float], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.ndarray, float, int, float, float, float], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.ndarray, int, int, float, int, float], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.ndarray, List[int]], /):
        """
        usage.scipy: 4
        usage.statsmodels: 3
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[float], List[float], List[float]], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[int], float, float, int, int, int], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[list, float, float, float, float, float, float, float], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[List[float], float, float, float, float, float, float, float], /
    ):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[int], numpy.float64], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[List[List[float]], numpy.ndarray, List[List[float]]], /
    ):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[int], numpy.ndarray], /):
        """
        usage.scipy: 2
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Union[
            Tuple[Union[bool, int, numpy.ndarray], Union[bool, numpy.ndarray, int]],
            slice[int, int, int],
        ],
        /,
    ):
        """
        usage.pandas: 13
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.ndarray, int, int], /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, int, numpy.ndarray, int, int], /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            Tuple[numpy.float64, numpy.float64],
            numpy.ndarray,
            Tuple[numpy.float64, numpy.float64],
        ],
        /,
    ):
        """
        usage.scipy: 2
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            Tuple[numpy.float64, numpy.float64, numpy.float64],
            numpy.ndarray,
            Tuple[numpy.float64, numpy.float64, numpy.float64],
        ],
        /,
    ):
        """
        usage.scipy: 4
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[numpy.ndarray, numpy.ndarray, List[numpy.float64]], /
    ):
        """
        usage.scipy: 8
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[numpy.ndarray, numpy.ndarray, List[numpy.ndarray]], /
    ):
        """
        usage.scipy: 2
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[Tuple[numpy.float64], numpy.ndarray, Tuple[numpy.float64]], /
    ):
        """
        usage.scipy: 2
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            Tuple[numpy.float64, numpy.float64, numpy.float64, numpy.float64],
            numpy.ndarray,
            Tuple[numpy.float64, numpy.float64, numpy.float64, numpy.float64],
        ],
        /,
    ):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            Tuple[
                numpy.float64,
                numpy.float64,
                numpy.float64,
                numpy.float64,
                numpy.float64,
                numpy.float64,
            ],
            numpy.ndarray,
            Tuple[
                numpy.float64,
                numpy.float64,
                numpy.float64,
                numpy.float64,
                numpy.float64,
                numpy.float64,
            ],
        ],
        /,
    ):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            Tuple[
                numpy.float64,
                numpy.float64,
                numpy.float64,
                numpy.float64,
                numpy.float64,
            ],
            numpy.ndarray,
            Tuple[
                numpy.float64,
                numpy.float64,
                numpy.float64,
                numpy.float64,
                numpy.float64,
            ],
        ],
        /,
    ):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[Tuple[numpy.int64], numpy.ndarray, Tuple[numpy.int64]], /
    ):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["-1"], numpy.ndarray, numpy.ndarray], /):
        """
        usage.scipy: 3
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray], /):
        """
        usage.matplotlib: 2
        usage.scipy: 6
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[int, slice[int, int, int], slice[int, int, int]], /
    ):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[int, int, int], /):
        """
        usage.scipy: 5
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.bool_, numpy.ndarray], /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.int32, numpy.ndarray], /):
        """
        usage.scipy: 3
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.float32, numpy.ndarray], /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.complex64, numpy.ndarray], /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.complex128, numpy.ndarray], /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.int64, numpy.ndarray], /):
        """
        usage.scipy: 1
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.uint32, numpy.ndarray], /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.ulonglong, numpy.ndarray], /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.longlong, numpy.ndarray], /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.uint16, numpy.ndarray], /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.int16, numpy.ndarray], /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.complex256, numpy.ndarray], /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.float128, numpy.ndarray], /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.uint64, numpy.ndarray], /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.uint8, numpy.ndarray], /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.int8, numpy.ndarray], /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.ndarray, List[Tuple[int, complex]]], /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[int, int, int], /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[int, numpy.int64, int], /):
        """
        usage.scipy: 2
        """
        ...

    @overload
    def __getitem__(self, _0: slice[numpy.int64, numpy.int64, numpy.int64], /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[bool, numpy.ndarray], /):
        """
        usage.scipy: 3
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, List[int], int], /):
        """
        usage.scipy: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[float, numpy.ndarray, int], /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[bool, List[bool], bool], /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[bool, numpy.ndarray, bool], /):
        """
        usage.scipy: 2
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[list, List[int]], /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[int], list], /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[numpy.ndarray], /):
        """
        usage.scipy: 2
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            List[int], List[int], List[int], List[int], List[int], int, List[int]
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
            List[int], List[int], List[int], List[int], List[int], int, int, List[int]
        ],
        /,
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[int], List[int], List[int]], /):
        """
        usage.sklearn: 3
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            numpy.ndarray, numpy.ndarray, numpy.ndarray, numpy.ndarray, numpy.ndarray
        ],
        /,
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.int64, numpy.ndarray, numpy.int64], /):
        """
        usage.sklearn: 1
        """
        ...

    def __getitem__(self, _0: object, /):
        """
        usage.matplotlib: 6
        usage.pandas: 13
        usage.scipy: 187
        usage.seaborn: 6
        usage.skimage: 16
        usage.sklearn: 37
        usage.statsmodels: 802
        usage.xarray: 3
        """
        ...
