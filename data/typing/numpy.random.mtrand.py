from typing import *

# usage.networkx: 3
# usage.scipy: 1
# usage.skimage: 1
# usage.sklearn: 3
_rand: object


class RandomState:

    # usage.dask: 1
    __module__: ClassVar[object]

    @overload
    def beta(self, _0: float, _1: float, /, *, size: Tuple[int]):
        """
        usage.statsmodels: 4
        """
        ...

    @overload
    def beta(self, _0: float, _1: float, /, *, size: int):
        """
        usage.pandas: 4
        """
        ...

    @overload
    def beta(self, _0: numpy.ndarray, _1: numpy.ndarray, _2: Tuple[numpy.int64], /):
        """
        usage.scipy: 2
        """
        ...

    @overload
    def beta(self, _0: numpy.float64, _1: numpy.float64, _2: Tuple[numpy.int64], /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def beta(
        self, _0: numpy.ndarray, _1: numpy.ndarray, _2: Tuple[int, int, int, int], /
    ):
        """
        usage.scipy: 2
        """
        ...

    @overload
    def beta(self, _0: numpy.ndarray, _1: numpy.ndarray, _2: Tuple[None, ...], /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def beta(self, _0: numpy.ndarray, _1: numpy.ndarray, _2: Tuple[int, int, int], /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def beta(self, _0: numpy.float64, _1: numpy.float64, _2: Tuple[None, ...], /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def beta(self, _0: int, _1: int, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    def beta(
        self,
        _0: Union[int, float, numpy.float64, numpy.ndarray],
        _1: Union[int, float, numpy.float64, numpy.ndarray],
        _2: Tuple[Union[int, numpy.int64, None], ...] = ...,
        /,
        *,
        size: Union[Tuple[int], int] = ...,
    ):
        """
        usage.dask: 1
        usage.pandas: 4
        usage.scipy: 8
        usage.statsmodels: 4
        """
        ...

    @overload
    def binomial(self, _0: int, _1: float, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        usage.sklearn: 1
        usage.statsmodels: 3
        """
        ...

    @overload
    def binomial(self, _0: int, _1: float, /, *, size: int):
        """
        usage.sklearn: 2
        usage.statsmodels: 2
        """
        ...

    @overload
    def binomial(self, _0: int, _1: numpy.ndarray, _2: Tuple[numpy.int64], /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def binomial(self, _0: numpy.ndarray, _1: numpy.ndarray, _2: Tuple[numpy.int64], /):
        """
        usage.scipy: 2
        """
        ...

    @overload
    def binomial(self, _0: int, _1: numpy.ndarray, _2: Tuple[int, int], /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def binomial(self, _0: int, _1: numpy.ndarray, _2: Tuple[None, ...], /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def binomial(
        self, _0: numpy.ndarray, _1: numpy.ndarray, _2: Tuple[int, int, int, int], /
    ):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def binomial(
        self, _0: numpy.ndarray, _1: numpy.ndarray, _2: Tuple[int, int, int], /
    ):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def binomial(self, _0: numpy.ndarray, _1: numpy.ndarray, _2: Tuple[None, ...], /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def binomial(
        self,
        _0: numpy.ndarray,
        _1: numpy.ndarray,
        _2: Tuple[numpy.int64, numpy.int64],
        /,
    ):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def binomial(
        self, _0: int, _1: numpy.ndarray, _2: Tuple[numpy.int64, numpy.int64], /
    ):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def binomial(self, _0: int, _1: float, _2: int, /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def binomial(self, _0: int, _1: numpy.float64, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def binomial(self, _0: int, _1: float, /, *, size: Tuple[int, int]):
        """
        usage.sklearn: 3
        """
        ...

    @overload
    def binomial(self, _0: int, _1: float, /):
        """
        usage.sklearn: 2
        """
        ...

    @overload
    def binomial(self, _0: int, _1: float, _2: Tuple[int, int], /):
        """
        usage.sklearn: 2
        """
        ...

    def binomial(
        self,
        _0: Union[int, numpy.ndarray],
        _1: Union[numpy.float64, float, numpy.ndarray],
        _2: Union[Tuple[Union[None, numpy.int64, int], ...], int] = ...,
        /,
        *,
        size: Union[int, Tuple[int, ...]] = ...,
    ):
        """
        usage.dask: 1
        usage.scipy: 10
        usage.seaborn: 1
        usage.sklearn: 11
        usage.statsmodels: 5
        """
        ...

    def bytes(self, _0: int, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def chisquare(self, _0: int, _1: int, /):
        """
        usage.scipy: 1
        usage.sklearn: 2
        usage.statsmodels: 2
        """
        ...

    @overload
    def chisquare(self, _0: numpy.ndarray, _1: Tuple[numpy.int64], /):
        """
        usage.scipy: 2
        """
        ...

    @overload
    def chisquare(
        self, _0: numpy.ndarray, _1: Tuple[numpy.int64, numpy.int64, numpy.int64], /
    ):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def chisquare(self, _0: numpy.ndarray, _1: Tuple[None, ...], /):
        """
        usage.scipy: 2
        """
        ...

    @overload
    def chisquare(self, _0: numpy.ndarray, _1: Tuple[int, int, int], /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def chisquare(self, _0: numpy.ndarray, _1: Tuple[numpy.int64, numpy.int64], /):
        """
        usage.scipy: 2
        """
        ...

    @overload
    def chisquare(
        self,
        _0: numpy.ndarray,
        _1: Tuple[numpy.int64, numpy.int64, numpy.int64, numpy.int64],
        /,
    ):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def chisquare(self, _0: numpy.float64, /, *, size: numpy.int64):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def chisquare(self, _0: int, /, *, size: numpy.int64):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def chisquare(self, _0: int, /):
        """
        usage.scipy: 3
        """
        ...

    @overload
    def chisquare(self, _0: int, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    def chisquare(
        self,
        _0: Union[int, numpy.float64, numpy.ndarray],
        _1: Union[int, Tuple[Union[int, numpy.int64, None], ...]] = ...,
        /,
        *,
        size: Union[Tuple[int], numpy.int64] = ...,
    ):
        """
        usage.dask: 1
        usage.scipy: 15
        usage.sklearn: 2
        usage.statsmodels: 2
        """
        ...

    @overload
    def choice(self, _0: List[Literal["people", "yo", "hello"]], /, *, size: int):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def choice(self, _0: List[Callable], /):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def choice(self, _0: numpy.ndarray, /, *, replace: bool, size: int):
        """
        usage.dask: 1
        usage.skimage: 1
        usage.sklearn: 5
        """
        ...

    @overload
    def choice(self, _0: int, _1: int, /, *, replace: bool):
        """
        usage.skimage: 2
        usage.sklearn: 2
        usage.xarray: 2
        """
        ...

    @overload
    def choice(self, _0: numpy.ndarray, _1: int, /, *, replace: bool):
        """
        usage.skimage: 1
        usage.sklearn: 1
        """
        ...

    @overload
    def choice(self, _0: List[bool], /, *, p: List[float], size: Tuple[int, int]):
        """
        usage.skimage: 2
        """
        ...

    @overload
    def choice(self, _0: List[bool], /, *, p: List[int], size: Tuple[int, int]):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def choice(self, _0: range, _1: int, /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def choice(self, _0: List[Literal["d", "c", "b", "a"]], /, *, size: List[int]):
        """
        usage.xarray: 2
        """
        ...

    @overload
    def choice(self, _0: int, _1: int, /):
        """
        usage.sklearn: 1
        usage.xarray: 1
        """
        ...

    @overload
    def choice(self, _0: numpy.ndarray, /, *, replace: bool, size: Tuple[int, int]):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def choice(
        self, _0: pandas.core.series.Series, /, *, replace: bool, size: Tuple[int, int]
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def choice(
        self,
        _0: Union[
            range,
            int,
            numpy.ndarray,
            pandas.core.indexes.datetimes.DatetimeIndex,
            List[Union[str, int]],
        ],
        _1: Union[int, numpy.int64, Tuple[int, int]] = ...,
        /,
        *,
        p: Union[numpy.ndarray, None] = ...,
        replace: bool = ...,
        size: Union[int, numpy.int64] = ...,
    ):
        """
        usage.pandas: 36
        """
        ...

    @overload
    def choice(self, _0: int, /, *, replace: bool, size: int):
        """
        usage.scipy: 2
        usage.sklearn: 2
        """
        ...

    @overload
    def choice(self, _0: List[int], _1: int, /):
        """
        usage.dask: 2
        usage.modin: 4
        usage.scipy: 1
        usage.sklearn: 1
        """
        ...

    @overload
    def choice(self, _0: int, /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def choice(self, _0: List[int], /, *, size: int):
        """
        usage.dask: 2
        usage.scipy: 1
        """
        ...

    @overload
    def choice(self, _0: range, /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def choice(self, _0: numpy.ndarray, /, *, size: int):
        """
        usage.scipy: 1
        usage.sklearn: 1
        """
        ...

    @overload
    def choice(self, _0: List[Union[int, float]], /, *, size: int):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def choice(self, _0: int, /, *, p: numpy.ndarray, size: int):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def choice(self, _0: List[str], _1: int, /):
        """
        usage.scipy: 2
        """
        ...

    @overload
    def choice(self, _0: numpy.ndarray, _1: int, /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def choice(self, _0: List[str], /, *, size: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def choice(self, _0: int, /, *, size: Tuple[None, ...]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def choice(self, _0: int, /, *, p: None, size: Tuple[None, ...]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def choice(self, _0: int, /, *, p: numpy.ndarray, size: Tuple[None, ...]):
        """
        usage.dask: 2
        """
        ...

    @overload
    def choice(
        self, _0: pandas.core.indexes.base.Index, /, *, replace: bool, size: int
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def choice(self, _0: List[bool], /, *, size: Tuple[int, int]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def choice(self, _0: List[bool], /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def choice(self, _0: List[Union[float, int]], _1: int, /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def choice(self, _0: List[Union[float, Literal["b", "a"]]], _1: int, /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def choice(self, _0: List[Literal["c", "b", "a"]], _1: int, /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def choice(self, _0: List[Union[float, int]], /, *, size: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def choice(self, _0: List[float], /, *, size: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def choice(self, _0: List[Literal["b", "a"]], /, *, size: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def choice(self, _0: List[Literal["c", "b", "a"]], /, *, size: int):
        """
        usage.dask: 7
        """
        ...

    @overload
    def choice(self, _0: List[str], _1: int, /, *, replace: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def choice(self, _0: List[Literal["Z", "Y", "X"]], /, *, size: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def choice(
        self, _0: pandas.core.indexes.numeric.Int64Index, /, *, replace: bool, size: int
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def choice(self, _0: int, /, *, replace: bool, size: numpy.int64):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def choice(
        self, _0: numpy.ndarray, /, *, p: numpy.ndarray, replace: bool, size: int
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def choice(self, _0: numpy.ndarray, _1: numpy.int64, /, *, replace: bool):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def choice(self, _0: numpy.ndarray, _1: int, /, *, p: numpy.ndarray, replace: bool):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def choice(
        self,
        _0: List[
            Dict[
                Literal["b", "a"],
                Union[List[int], scipy.stats._distn_infrastructure.rv_frozen],
            ]
        ],
        /,
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def choice(
        self,
        _0: List[
            Dict[
                Literal["penalty", "C"],
                Union[
                    scipy.stats._distn_infrastructure.rv_frozen,
                    List[Literal["l1", "l2"]],
                ],
            ]
        ],
        /,
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def choice(
        self,
        _0: List[
            Dict[
                Literal["C", "kernel"],
                Union[
                    List[Literal["linear", "rbf"]],
                    scipy.stats._distn_infrastructure.rv_frozen,
                ],
            ]
        ],
        /,
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def choice(
        self,
        _0: List[Dict[Literal["C"], scipy.stats._distn_infrastructure.rv_frozen]],
        /,
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def choice(
        self,
        _0: List[
            Dict[
                Literal["gamma", "C", "kernel", "degree"],
                Union[
                    List[Union[int, Literal["poly", "rbf"]]],
                    scipy.stats._distn_infrastructure.rv_frozen,
                ],
            ]
        ],
        /,
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def choice(
        self,
        _0: List[
            Dict[
                Literal["second", "first"],
                Union[
                    scipy.stats._distn_infrastructure.rv_frozen,
                    List[Literal["c", "b", "a"]],
                ],
            ]
        ],
        /,
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def choice(
        self,
        _0: List[Dict[Literal["a"], scipy.stats._distn_infrastructure.rv_frozen]],
        /,
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def choice(
        self,
        _0: List[Dict[Literal["alpha"], scipy.stats._distn_infrastructure.rv_frozen]],
        /,
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def choice(self, _0: List[int], /, *, replace: bool, size: Tuple[int]):
        """
        usage.networkx: 6
        """
        ...

    @overload
    def choice(
        self,
        _0: List[Literal["REG4", "REG3", "REG2", "REG1", "REG0"]],
        /,
        *,
        replace: bool,
        size: Tuple[int],
    ):
        """
        usage.networkx: 1
        """
        ...

    @overload
    def choice(self, _0: List[int], /):
        """
        usage.networkx: 1
        """
        ...

    @overload
    def choice(self, _0: List[int], _1: Tuple[int], /, *, replace: bool):
        """
        usage.networkx: 1
        """
        ...

    def choice(
        self,
        _0: object,
        _1: Union[Tuple[int, ...], int, numpy.int64] = ...,
        /,
        *,
        size: Union[Tuple[Union[int, None], ...], List[int], int, numpy.int64] = ...,
        replace: bool = ...,
        p: Union[numpy.ndarray, List[Union[float, int]], None] = ...,
    ):
        """
        usage.dask: 32
        usage.koalas: 1
        usage.modin: 4
        usage.networkx: 9
        usage.pandas: 36
        usage.scipy: 12
        usage.skimage: 8
        usage.sklearn: 25
        usage.statsmodels: 2
        usage.xarray: 6
        """
        ...

    def dirichlet(self, _0: numpy.ndarray, /, *, size: int):
        """
        usage.scipy: 4
        """
        ...

    @overload
    def exponential(self, /, *, size: int):
        """
        usage.sklearn: 1
        usage.statsmodels: 2
        """
        ...

    @overload
    def exponential(self, /, *, size: Tuple[int, int]):
        """
        usage.scipy: 3
        """
        ...

    @overload
    def exponential(self, _0: int, /, *, size: Tuple[int, int]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def exponential(self, _0: int, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def exponential(self, _0: float, /):
        """
        usage.networkx: 2
        """
        ...

    def exponential(
        self, _0: Union[float, int] = ..., /, *, size: Union[int, Tuple[int, ...]] = ...
    ):
        """
        usage.dask: 2
        usage.networkx: 2
        usage.scipy: 3
        usage.sklearn: 1
        usage.statsmodels: 2
        """
        ...

    @overload
    def f(self, _0: numpy.ndarray, _1: numpy.ndarray, _2: Tuple[numpy.int64], /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def f(self, _0: numpy.ndarray, _1: numpy.ndarray, _2: Tuple[int, int, int, int], /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def f(self, _0: numpy.ndarray, _1: numpy.ndarray, _2: Tuple[None, ...], /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def f(self, _0: int, _1: int, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    def f(
        self,
        _0: Union[int, numpy.ndarray],
        _1: Union[int, numpy.ndarray],
        _2: Tuple[Union[int, numpy.int64, None], ...] = ...,
        /,
        *,
        size: Tuple[int] = ...,
    ):
        """
        usage.dask: 1
        usage.scipy: 3
        """
        ...

    @overload
    def gamma(self, _0: float, _1: numpy.float64, /):
        """
        usage.skimage: 2
        """
        ...

    @overload
    def gamma(self, _0: int, _1: int, /, *, size: int):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def gamma(self, _0: int, _1: numpy.ndarray, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def gamma(self, _0: float, _1: numpy.float64, _2: numpy.int64, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def gamma(self, _0: int, /, *, size: numpy.int64):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def gamma(self, _0: numpy.ndarray, /, *, size: Tuple[numpy.int64]):
        """
        usage.scipy: 2
        """
        ...

    @overload
    def gamma(self, _0: numpy.ndarray, /, *, size: Tuple[int, int, int]):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def gamma(self, _0: numpy.ndarray, /, *, size: Tuple[None, ...]):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def gamma(self, _0: int, _1: int, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def gamma(self, _0: float, _1: float, _2: Tuple[int, int], /):
        """
        usage.sklearn: 2
        """
        ...

    @overload
    def gamma(self, _0: int, /, *, size: int):
        """
        usage.sklearn: 1
        """
        ...

    def gamma(
        self,
        _0: Union[float, int, numpy.ndarray],
        _1: Union[float, numpy.ndarray, numpy.float64, int] = ...,
        _2: Union[Tuple[int, int], numpy.int64] = ...,
        /,
        *,
        size: Union[int, numpy.int64, Tuple[Union[int, numpy.int64, None], ...]] = ...,
    ):
        """
        usage.dask: 1
        usage.scipy: 4
        usage.skimage: 2
        usage.sklearn: 3
        usage.statsmodels: 4
        """
        ...

    @overload
    def geometric(self, _0: numpy.float64, /, *, size: Tuple[numpy.int64]):
        """
        usage.scipy: 3
        """
        ...

    @overload
    def geometric(self, _0: numpy.ndarray, /, *, size: Tuple[numpy.int64]):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def geometric(self, _0: numpy.ndarray, /, *, size: Tuple[int, int]):
        """
        usage.scipy: 4
        """
        ...

    @overload
    def geometric(self, _0: numpy.ndarray, /, *, size: Tuple[None, ...]):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def geometric(self, _0: numpy.float64, /, *, size: Tuple[None, ...]):
        """
        usage.scipy: 3
        """
        ...

    @overload
    def geometric(self, _0: numpy.ndarray, /, *, size: Tuple[numpy.int64, numpy.int64]):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def geometric(self, _0: numpy.float64, /, *, size: Tuple[numpy.int64, numpy.int64]):
        """
        usage.scipy: 2
        """
        ...

    @overload
    def geometric(self, _0: int, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    def geometric(
        self,
        _0: Union[int, numpy.ndarray, numpy.float64],
        /,
        *,
        size: Tuple[Union[int, numpy.int64, None], ...],
    ):
        """
        usage.dask: 1
        usage.scipy: 15
        """
        ...

    def get_state(self, /):
        """
        usage.networkx: 1
        usage.pandas: 1
        usage.scipy: 8
        """
        ...

    @overload
    def gumbel(self, /, *, size: int):
        """
        usage.scipy: 2
        """
        ...

    @overload
    def gumbel(self, _0: int, _1: float, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    def gumbel(
        self, _0: int = ..., _1: float = ..., /, *, size: Union[Tuple[int], int]
    ):
        """
        usage.dask: 1
        usage.scipy: 2
        """
        ...

    @overload
    def hypergeometric(
        self,
        _0: numpy.ndarray,
        _1: numpy.int64,
        _2: numpy.ndarray,
        /,
        *,
        size: Tuple[numpy.int64],
    ):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def hypergeometric(
        self,
        _0: numpy.ndarray,
        _1: numpy.ndarray,
        _2: numpy.ndarray,
        /,
        *,
        size: Tuple[int, int, int, int],
    ):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def hypergeometric(
        self,
        _0: numpy.ndarray,
        _1: numpy.int64,
        _2: numpy.ndarray,
        /,
        *,
        size: Tuple[None, ...],
    ):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def hypergeometric(
        self,
        _0: numpy.ndarray,
        _1: numpy.int64,
        _2: numpy.ndarray,
        /,
        *,
        size: Tuple[numpy.int64, numpy.int64],
    ):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def hypergeometric(self, _0: int, _1: int, _2: int, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    def hypergeometric(
        self,
        _0: Union[int, numpy.ndarray],
        _1: Union[int, numpy.ndarray, numpy.int64],
        _2: Union[int, numpy.ndarray],
        /,
        *,
        size: Tuple[Union[int, numpy.int64, None], ...],
    ):
        """
        usage.dask: 1
        usage.scipy: 4
        """
        ...

    @overload
    def laplace(self, _0: int, _1: int, /, *, size: Tuple[numpy.int64]):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def laplace(self, _0: int, _1: int, /, *, size: Tuple[int, int]):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def laplace(self, _0: int, _1: int, /, *, size: Tuple[None, ...]):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def laplace(self, _0: int, _1: numpy.float64, _2: int, /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    def laplace(self, _0: float, _1: float, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    def laplace(
        self,
        _0: Union[float, int],
        _1: Union[float, int, numpy.float64],
        _2: int = ...,
        /,
        *,
        size: Tuple[Union[None, numpy.int64, int], ...] = ...,
    ):
        """
        usage.dask: 1
        usage.prophet: 1
        usage.scipy: 3
        """
        ...

    @overload
    def logistic(self, /, *, size: Tuple[numpy.int64]):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def logistic(self, /, *, size: Tuple[int, int]):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def logistic(self, /, *, size: Tuple[None, ...]):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def logistic(self, _0: float, _1: float, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    def logistic(
        self,
        _0: float = ...,
        _1: float = ...,
        /,
        *,
        size: Tuple[Union[None, numpy.int64, int], ...],
    ):
        """
        usage.dask: 1
        usage.scipy: 3
        """
        ...

    @overload
    def lognormal(self, _0: float, _1: float, _2: int, /):
        """
        usage.pandas: 1
        """
        ...

    @overload
    def lognormal(self, /, *, size: int):
        """
        usage.scipy: 1
        usage.sklearn: 3
        """
        ...

    @overload
    def lognormal(self, /, *, mean: float, sigma: float, size: Tuple[int, int]):
        """
        usage.matplotlib: 1
        """
        ...

    @overload
    def lognormal(self, _0: float, _1: float, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    def lognormal(
        self,
        /,
        *_args: Union[int, float],
        size: Union[int, Tuple[int, ...]] = ...,
        mean: float = ...,
        sigma: float = ...,
    ):
        """
        usage.dask: 1
        usage.matplotlib: 1
        usage.pandas: 1
        usage.scipy: 1
        usage.sklearn: 3
        """
        ...

    @overload
    def logseries(self, _0: numpy.ndarray, /, *, size: Tuple[numpy.int64]):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def logseries(self, _0: numpy.ndarray, /, *, size: Tuple[int, int]):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def logseries(self, _0: numpy.ndarray, /, *, size: Tuple[None, ...]):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def logseries(self, _0: numpy.ndarray, /, *, size: Tuple[numpy.int64, numpy.int64]):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def logseries(self, _0: float, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    def logseries(
        self,
        _0: Union[float, numpy.ndarray],
        /,
        *,
        size: Tuple[Union[int, numpy.int64, None], ...],
    ):
        """
        usage.dask: 1
        usage.scipy: 4
        """
        ...

    @overload
    def multinomial(self, _0: numpy.ndarray, _1: numpy.ndarray, _2: int, /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def multinomial(self, _0: int, _1: List[float], /, *, size: int):
        """
        usage.dask: 1
        usage.scipy: 1
        """
        ...

    @overload
    def multinomial(self, _0: int, _1: List[float], /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def multinomial(self, _0: int, _1: List[float], /, *, size: Tuple[int, int]):
        """
        usage.dask: 2
        """
        ...

    @overload
    def multinomial(self, _0: int, _1: numpy.ndarray, /):
        """
        usage.sklearn: 5
        """
        ...

    @overload
    def multinomial(self, _0: int, _1: numpy.ndarray, /, *, size: int):
        """
        usage.sklearn: 1
        """
        ...

    def multinomial(
        self,
        _0: Union[int, numpy.ndarray],
        _1: Union[numpy.ndarray, List[float]],
        _2: int = ...,
        /,
        *,
        size: Union[int, Tuple[int, ...]] = ...,
    ):
        """
        usage.dask: 4
        usage.scipy: 2
        usage.sklearn: 6
        """
        ...

    @overload
    def multivariate_normal(
        self, _0: numpy.ndarray, _1: numpy.ndarray, /, *, size: int
    ):
        """
        usage.scipy: 4
        usage.sklearn: 5
        usage.statsmodels: 4
        """
        ...

    @overload
    def multivariate_normal(self, /, *, cov: numpy.ndarray, mean: numpy.ndarray):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    def multivariate_normal(
        self, _0: numpy.ndarray, _1: numpy.ndarray, _2: Tuple[int], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def multivariate_normal(self, _0: numpy.ndarray, _1: numpy.ndarray, /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    def multivariate_normal(
        self, /, *, cov: numpy.ndarray, mean: numpy.ndarray, size: int
    ):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def multivariate_normal(self, _0: numpy.ndarray, _1: numpy.ndarray, _2: int, /):
        """
        usage.scipy: 1
        usage.sklearn: 8
        usage.statsmodels: 1
        """
        ...

    @overload
    def multivariate_normal(
        self, _0: List[int], _1: List[Tuple[float, Union[float, int]]], _2: int, /
    ):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def multivariate_normal(self, /, *, cov: numpy.ndarray, mean: List[int], size: int):
        """
        usage.sklearn: 8
        """
        ...

    def multivariate_normal(
        self,
        /,
        *_args: Union[
            List[Union[int, Tuple[float, Union[int, float]]]],
            Tuple[int],
            numpy.ndarray,
            int,
        ],
        size: int = ...,
        cov: numpy.ndarray = ...,
        mean: Union[List[int], numpy.ndarray] = ...,
    ):
        """
        usage.scipy: 5
        usage.seaborn: 1
        usage.sklearn: 21
        usage.statsmodels: 14
        """
        ...

    @overload
    def negative_binomial(
        self, _0: numpy.ndarray, _1: numpy.ndarray, _2: Tuple[numpy.int64], /
    ):
        """
        usage.scipy: 2
        """
        ...

    @overload
    def negative_binomial(
        self, _0: numpy.ndarray, _1: numpy.ndarray, _2: Tuple[int, int, int], /
    ):
        """
        usage.scipy: 2
        """
        ...

    @overload
    def negative_binomial(
        self, _0: numpy.ndarray, _1: numpy.ndarray, _2: Tuple[None, ...], /
    ):
        """
        usage.scipy: 2
        """
        ...

    @overload
    def negative_binomial(
        self,
        _0: numpy.ndarray,
        _1: numpy.ndarray,
        _2: Tuple[numpy.int64, numpy.int64],
        /,
    ):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def negative_binomial(self, _0: int, _1: float, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    def negative_binomial(
        self,
        _0: Union[int, numpy.ndarray],
        _1: Union[float, numpy.ndarray],
        _2: Tuple[Union[None, numpy.int64, int], ...] = ...,
        /,
        *,
        size: Tuple[int] = ...,
    ):
        """
        usage.dask: 1
        usage.scipy: 7
        """
        ...

    @overload
    def noncentral_chisquare(
        self, _0: numpy.ndarray, _1: numpy.ndarray, _2: Tuple[numpy.int64], /
    ):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def noncentral_chisquare(
        self, _0: numpy.ndarray, _1: numpy.ndarray, _2: Tuple[int, int, int, int], /
    ):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def noncentral_chisquare(
        self, _0: numpy.ndarray, _1: numpy.ndarray, _2: Tuple[None, ...], /
    ):
        """
        usage.scipy: 2
        """
        ...

    @overload
    def noncentral_chisquare(self, _0: int, _1: int, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    def noncentral_chisquare(
        self,
        _0: Union[int, numpy.ndarray],
        _1: Union[int, numpy.ndarray],
        _2: Tuple[Union[None, numpy.int64, int], ...] = ...,
        /,
        *,
        size: Tuple[int] = ...,
    ):
        """
        usage.dask: 1
        usage.scipy: 4
        """
        ...

    @overload
    def noncentral_f(
        self,
        _0: numpy.ndarray,
        _1: numpy.ndarray,
        _2: numpy.ndarray,
        _3: Tuple[numpy.int64],
        /,
    ):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def noncentral_f(
        self,
        _0: numpy.ndarray,
        _1: numpy.ndarray,
        _2: numpy.ndarray,
        _3: Tuple[int, int, int, int, int],
        /,
    ):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def noncentral_f(
        self,
        _0: numpy.ndarray,
        _1: numpy.ndarray,
        _2: numpy.ndarray,
        _3: Tuple[None, ...],
        /,
    ):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def noncentral_f(self, _0: int, _1: int, _2: int, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    def noncentral_f(
        self,
        _0: Union[int, numpy.ndarray],
        _1: Union[int, numpy.ndarray],
        _2: Union[int, numpy.ndarray],
        _3: Tuple[Union[int, numpy.int64, None], ...] = ...,
        /,
        *,
        size: Tuple[int] = ...,
    ):
        """
        usage.dask: 1
        usage.scipy: 3
        """
        ...

    @overload
    def normal(self, /, *, size: Tuple[int, int]):
        """
        usage.dask: 3
        usage.networkx: 1
        usage.scipy: 22
        usage.skimage: 17
        usage.sklearn: 66
        usage.statsmodels: 203
        usage.xarray: 2
        """
        ...

    @overload
    def normal(self, /, *, size: Tuple[int, int, int]):
        """
        usage.matplotlib: 1
        usage.scipy: 2
        usage.skimage: 9
        usage.statsmodels: 6
        """
        ...

    @overload
    def normal(self, /, *, size: Tuple[int, int, int, int, int]):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def normal(self, /, *, size: Tuple[int, int, int, int]):
        """
        usage.skimage: 2
        """
        ...

    @overload
    def normal(self, _0: float, _1: float, _2: Tuple[int, int], /):
        """
        usage.scipy: 1
        usage.skimage: 3
        """
        ...

    @overload
    def normal(self, _0: int, _1: numpy.ndarray, /):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def normal(self, /, *, scale: int, size: int):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def normal(self, /, *, size: int):
        """
        usage.dask: 3
        usage.matplotlib: 21
        usage.scipy: 10
        usage.sklearn: 39
        usage.statsmodels: 225
        """
        ...

    @overload
    def normal(self, /, *, size: numpy.int64):
        """
        usage.scipy: 1
        usage.statsmodels: 2
        """
        ...

    @overload
    def normal(self, _0: int, _1: float, _2: int, /):
        """
        usage.statsmodels: 6
        """
        ...

    @overload
    def normal(self, _0: int, _1: int, _2: Tuple[int, int], /):
        """
        usage.seaborn: 3
        usage.sklearn: 3
        usage.statsmodels: 4
        """
        ...

    @overload
    def normal(self, _0: int, _1: int, _2: int, /):
        """
        usage.matplotlib: 3
        usage.scipy: 2
        usage.seaborn: 11
        usage.sklearn: 1
        usage.statsmodels: 5
        """
        ...

    @overload
    def normal(self, /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def normal(self, _0: numpy.ndarray, /, *, size: int):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def normal(self, /, *, size: Tuple[int]):
        """
        usage.scipy: 7
        usage.statsmodels: 25
        """
        ...

    @overload
    def normal(self, _0: int, _1: int, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        usage.statsmodels: 16
        """
        ...

    @overload
    def normal(self, /, *, scale: float):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def normal(self, _0: int, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def normal(self, /, *, scale: float, size: int):
        """
        usage.sklearn: 4
        usage.statsmodels: 2
        """
        ...

    @overload
    def normal(
        self,
        _0: int = ...,
        _1: int = ...,
        _2: int = ...,
        /,
        *,
        size: Union[int, Tuple[int, int]] = ...,
    ):
        """
        usage.pandas: 7
        """
        ...

    @overload
    def normal(self, /, *, scale: numpy.float64, size: Tuple[int, int]):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def normal(self, /, *, size: Tuple[numpy.int64]):
        """
        usage.scipy: 2
        """
        ...

    @overload
    def normal(self, /, *, size: Tuple[numpy.int64, numpy.int64, numpy.int64]):
        """
        usage.scipy: 2
        """
        ...

    @overload
    def normal(self, /, *, loc: int, scale: int, size: int):
        """
        usage.scipy: 5
        """
        ...

    @overload
    def normal(self, _0: int, _1: numpy.ndarray, _2: int, /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    def normal(self, _0: int, _1: numpy.float64, _2: int, /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    def normal(self, _0: float, _1: float, /, *, size: Tuple[int, int, int]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def normal(self, _0: float, _1: float, /, *, size: Tuple[int, int]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def normal(self, _0: int, _1: float, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def normal(self, _0: float, _1: float, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def normal(self, _0: int, _1: int, /, *, size: Tuple[int, int]):
        """
        usage.dask: 3
        usage.sklearn: 2
        """
        ...

    @overload
    def normal(self, _0: numpy.int64, _1: int, /, *, size: Tuple[int, int]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def normal(
        self, _0: dask.array.core.Array, _1: int, /, *, size: Tuple[int, int, int]
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def normal(
        self,
        _0: numpy.float64,
        _1: dask.array.core.Array,
        /,
        *,
        size: Tuple[int, int, int],
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def normal(
        self,
        _0: dask.array.core.Array,
        _1: numpy.float64,
        /,
        *,
        size: Tuple[int, int, int, int],
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def normal(self, _0: numpy.float64, _1: float, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def normal(self, _0: dask.array.core.Array, _1: float, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def normal(self, _0: int, _1: float, /, *, size: Tuple[None, ...]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def normal(self, _0: int, _1: float, /, *, size: Tuple[int, int]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def normal(self, _0: int, _1: int, /, *, size: Tuple[int, int, int]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def normal(self, _0: int, _1: int, /, *, size: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def normal(
        self, /, *, loc: float, scale: numpy.float64, size: Tuple[numpy.int64, int]
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def normal(
        self, /, *, loc: numpy.ndarray, scale: numpy.float64, size: Tuple[int, int]
    ):
        """
        usage.sklearn: 2
        """
        ...

    @overload
    def normal(self, /, *, scale: float, size: Tuple[int, int]):
        """
        usage.sklearn: 8
        """
        ...

    @overload
    def normal(
        self,
        /,
        *,
        loc: numpy.ndarray,
        scale: numpy.float64,
        size: Tuple[numpy.int64, int],
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def normal(self, /, *, loc: int, scale: int, size: Tuple[int, int]):
        """
        usage.sklearn: 3
        """
        ...

    @overload
    def normal(self, /, *, loc: numpy.ndarray, scale: numpy.ndarray):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def normal(self, /, *, loc: float, scale: float, size: int):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def normal(self, /, *, loc: int, size: Tuple[int, int]):
        """
        usage.sklearn: 3
        """
        ...

    @overload
    def normal(self, /, *, scale: int, size: Tuple[int, int]):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def normal(self, _0: numpy.ndarray, _1: float, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def normal(self, _0: int, _1: float, _2: Tuple[int, int], /):
        """
        usage.sklearn: 2
        """
        ...

    @overload
    def normal(self, /, *, loc: float, scale: float, size: Tuple[int, int]):
        """
        usage.sklearn: 2
        """
        ...

    @overload
    def normal(
        self, /, *, loc: numpy.ndarray, scale: numpy.int64, size: Tuple[int, int]
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def normal(self, /, *, loc: float, scale: numpy.float64, size: Tuple[int, int]):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def normal(self, _0: int, _1: float, /):
        """
        usage.networkx: 1
        """
        ...

    @overload
    def normal(self, _0: int, _1: int, /):
        """
        usage.networkx: 2
        """
        ...

    def normal(
        self,
        /,
        *_args: object,
        size: Union[Tuple[Union[int, numpy.int64, None], ...], numpy.int64, int] = ...,
        scale: Union[numpy.int64, int, numpy.ndarray, float, numpy.float64] = ...,
        loc: Union[numpy.ndarray, int, float] = ...,
    ):
        """
        usage.dask: 24
        usage.matplotlib: 25
        usage.networkx: 4
        usage.pandas: 7
        usage.prophet: 2
        usage.scipy: 55
        usage.seaborn: 14
        usage.skimage: 33
        usage.sklearn: 143
        usage.statsmodels: 499
        usage.xarray: 3
        """
        ...

    @overload
    def pareto(self, _0: float, _1: int, /):
        """
        usage.scipy: 2
        """
        ...

    @overload
    def pareto(self, _0: float, /, *, size: int):
        """
        usage.scipy: 5
        """
        ...

    @overload
    def pareto(self, _0: int, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def pareto(self, _0: int, /):
        """
        usage.networkx: 1
        """
        ...

    @overload
    def pareto(self, _0: float, /):
        """
        usage.networkx: 1
        """
        ...

    def pareto(
        self,
        _0: Union[int, float],
        _1: int = ...,
        /,
        *,
        size: Union[Tuple[int], int] = ...,
    ):
        """
        usage.dask: 1
        usage.networkx: 2
        usage.scipy: 7
        """
        ...

    @overload
    def permutation(self, _0: numpy.ndarray, /):
        """
        usage.dask: 2
        usage.scipy: 4
        usage.skimage: 1
        usage.sklearn: 3
        usage.statsmodels: 1
        """
        ...

    @overload
    def permutation(self, _0: int, /):
        """
        usage.dask: 2
        usage.scipy: 5
        usage.sklearn: 19
        usage.statsmodels: 2
        """
        ...

    @overload
    def permutation(self, _0: Union[List[Tuple[int, int]], int], /):
        """
        usage.pandas: 17
        """
        ...

    @overload
    def permutation(self, _0: range, /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def permutation(self, _0: List[float], /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def permutation(self, _0: numpy.int64, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def permutation(self, _0: List[numpy.int64], /):
        """
        usage.sklearn: 18
        """
        ...

    def permutation(
        self,
        _0: Union[
            List[Union[Tuple[int, int], float, numpy.int64]],
            numpy.ndarray,
            numpy.int64,
            int,
            range,
        ],
        /,
    ):
        """
        usage.dask: 4
        usage.pandas: 17
        usage.scipy: 11
        usage.skimage: 1
        usage.sklearn: 41
        usage.statsmodels: 3
        """
        ...

    @overload
    def poisson(self, _0: numpy.ndarray, /):
        """
        usage.skimage: 2
        usage.statsmodels: 17
        """
        ...

    @overload
    def poisson(self, _0: pandas.core.series.Series, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def poisson(self, _0: numpy.ndarray, /, *, size: int):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    def poisson(self, _0: numpy.float64, /, *, size: numpy.int64):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def poisson(self, _0: int, /, *, size: int):
        """
        usage.dask: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    def poisson(self, _0: numpy.ndarray, _1: Tuple[numpy.int64], /):
        """
        usage.scipy: 3
        """
        ...

    @overload
    def poisson(self, _0: numpy.ndarray, _1: Tuple[int, int], /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def poisson(self, _0: numpy.ndarray, _1: Tuple[None, ...], /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def poisson(self, _0: numpy.ndarray, _1: Tuple[int, int, int], /):
        """
        usage.scipy: 2
        """
        ...

    @overload
    def poisson(self, _0: numpy.ndarray, _1: Tuple[numpy.int64, numpy.int64], /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def poisson(self, _0: numpy.float64, /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    def poisson(self, _0: float, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def poisson(self, _0: numpy.int64, /, *, size: Tuple[int, int]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def poisson(self, _0: int, /):
        """
        usage.sklearn: 2
        """
        ...

    @overload
    def poisson(self, /, *, lam: numpy.ndarray):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def poisson(self, /, *, size: int):
        """
        usage.sklearn: 3
        """
        ...

    def poisson(
        self,
        _0: object = ...,
        _1: Tuple[Union[int, numpy.int64, None], ...] = ...,
        /,
        *,
        size: Union[int, numpy.int64, Tuple[int, ...]] = ...,
        lam: numpy.ndarray = ...,
    ):
        """
        usage.dask: 3
        usage.prophet: 1
        usage.scipy: 8
        usage.skimage: 2
        usage.sklearn: 6
        usage.statsmodels: 23
        """
        ...

    def power(self, _0: int, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rand(self, _0: int, /):
        """
        usage.dask: 6
        usage.koalas: 91
        usage.matplotlib: 18
        usage.networkx: 1
        usage.prophet: 1
        usage.scipy: 219
        usage.seaborn: 4
        usage.skimage: 9
        usage.sklearn: 96
        usage.statsmodels: 2
        usage.xarray: 1
        """
        ...

    @overload
    def rand(self, _0: int, _1: int, /):
        """
        usage.dask: 17
        usage.koalas: 5
        usage.matplotlib: 20
        usage.networkx: 4
        usage.scipy: 222
        usage.skimage: 61
        usage.sklearn: 171
        usage.statsmodels: 16
        usage.xarray: 11
        """
        ...

    @overload
    def rand(self, _0: int, _1: int, _2: int, /):
        """
        usage.dask: 6
        usage.matplotlib: 1
        usage.scipy: 17
        usage.skimage: 18
        usage.xarray: 6
        """
        ...

    @overload
    def rand(self, _0: int, _1: int, _2: int, _3: int, /):
        """
        usage.dask: 1
        usage.scipy: 12
        usage.skimage: 6
        """
        ...

    @overload
    def rand(self, _0: int, _1: int, _2: int, _3: int, _4: int, /):
        """
        usage.scipy: 4
        usage.skimage: 5
        usage.xarray: 1
        """
        ...

    @overload
    def rand(self, _0: numpy.int64, _1: numpy.int64, _2: numpy.int64, /):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def rand(self, /):
        """
        usage.networkx: 7
        usage.scipy: 7
        usage.skimage: 1
        usage.sklearn: 7
        """
        ...

    @overload
    def rand(self, _0: int = ..., _1: int = ..., _2: int = ..., /):
        """
        usage.pandas: 110
        """
        ...

    @overload
    def rand(self, _0: int, _1: int, _2: int, _3: int, _4: int, _5: int, /):
        """
        usage.scipy: 4
        """
        ...

    @overload
    def rand(
        self, _0: int, _1: int, _2: int, _3: int, _4: int, _5: int, _6: int, _7: int, /
    ):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def rand(self, _0: numpy.int64, /):
        """
        usage.scipy: 2
        usage.sklearn: 1
        """
        ...

    def rand(self, /, *_args: Union[int, numpy.int64]):
        """
        usage.dask: 30
        usage.koalas: 96
        usage.matplotlib: 39
        usage.networkx: 12
        usage.pandas: 110
        usage.prophet: 1
        usage.scipy: 488
        usage.seaborn: 4
        usage.skimage: 101
        usage.sklearn: 275
        usage.statsmodels: 18
        usage.xarray: 19
        """
        ...

    @overload
    def randint(self, /, *, high: int, low: int, size: Tuple[int, int]):
        """
        usage.koalas: 1
        usage.scipy: 1
        usage.sklearn: 2
        """
        ...

    @overload
    def randint(self, _0: int, /):
        """
        usage.koalas: 2
        usage.scipy: 11
        usage.skimage: 2
        usage.sklearn: 11
        usage.xarray: 1
        """
        ...

    @overload
    def randint(self, _0: int, _1: int, /, *, size: Tuple[int, int]):
        """
        usage.dask: 23
        usage.koalas: 4
        usage.modin: 12
        usage.scipy: 5
        usage.skimage: 8
        usage.sklearn: 19
        usage.statsmodels: 6
        usage.xarray: 2
        """
        ...

    @overload
    def randint(
        self, _0: int, _1: int, /, *, dtype: Type[numpy.uint16], size: Tuple[int, int]
    ):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def randint(
        self, _0: int, _1: int, _2: Tuple[int, int], /, *, dtype: Type[numpy.uint8]
    ):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def randint(self, _0: int, _1: int, /):
        """
        usage.networkx: 5
        usage.scipy: 9
        usage.skimage: 5
        usage.sklearn: 8
        """
        ...

    @overload
    def randint(self, _0: int, _1: int, /, *, size: int):
        """
        usage.dask: 6
        usage.matplotlib: 2
        usage.modin: 22
        usage.scipy: 6
        usage.skimage: 3
        usage.sklearn: 34
        usage.statsmodels: 38
        """
        ...

    @overload
    def randint(self, _0: float, _1: int, /):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def randint(self, _0: int, _1: int, _2: Tuple[int, int], /):
        """
        usage.dask: 21
        usage.scipy: 4
        usage.skimage: 1
        usage.sklearn: 6
        """
        ...

    @overload
    def randint(self, _0: int, /, *, size: int):
        """
        usage.dask: 15
        usage.scipy: 2
        usage.skimage: 2
        usage.sklearn: 23
        usage.statsmodels: 3
        """
        ...

    @overload
    def randint(
        self,
        _0: int,
        _1: int,
        /,
        *,
        dtype: Type[numpy.uint8],
        size: Tuple[int, int, int],
    ):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def randint(self, _0: int, _1: int, _2: Tuple[int, int, int], /):
        """
        usage.dask: 9
        usage.xarray: 1
        """
        ...

    @overload
    def randint(self, _0: int, _1: int, /, *, size: List[int]):
        """
        usage.xarray: 6
        """
        ...

    @overload
    def randint(self, _0: int, _1: int, _2: int, /):
        """
        usage.dask: 7
        usage.modin: 4
        usage.scipy: 8
        usage.sklearn: 30
        usage.statsmodels: 31
        usage.xarray: 4
        """
        ...

    @overload
    def randint(self, _0: int, _1: int, /, *, size: numpy.int64):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def randint(self, _0: int, _1: int, /, *, size: Tuple[int, int, int]):
        """
        usage.scipy: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    def randint(self, _0: int, /, *, size: Tuple[int, int, int, int]):
        """
        usage.dask: 1
        usage.scipy: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    def randint(
        self,
        _0: int,
        _1: int = ...,
        _2: Union[int, numpy.int64, Tuple[int, ...]] = ...,
        /,
        *,
        size: Union[int, Tuple[int, ...]] = ...,
        dtype: Literal["int64"] = ...,
        high: int = ...,
    ):
        """
        usage.pandas: 160
        """
        ...

    @overload
    def randint(self, _0: int, /, *, dtype: Literal["int64"], high: int, size: int):
        """
        usage.scipy: 2
        """
        ...

    @overload
    def randint(self, _0: int, /, *, dtype: Literal["int64"], size: int):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def randint(self, _0: int, /, *, dtype: Literal["int64"], high: None, size: int):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def randint(self, _0: int, /, *, size: List[int]):
        """
        usage.scipy: 3
        """
        ...

    @overload
    def randint(self, _0: int, _1: float, /):
        """
        usage.scipy: 4
        """
        ...

    @overload
    def randint(self, _0: int, /, *, dtype: numpy.dtype, high: int, size: int):
        """
        usage.scipy: 2
        """
        ...

    @overload
    def randint(
        self,
        _0: numpy.ndarray,
        /,
        *,
        dtype: Literal["int64"],
        high: numpy.ndarray,
        size: Tuple[numpy.int64],
    ):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def randint(self, _0: int, /, *, dtype: Literal["int64"], high: int, size: None):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def randint(
        self,
        _0: numpy.ndarray,
        /,
        *,
        dtype: Literal["int64"],
        high: numpy.ndarray,
        size: Tuple[None, ...],
    ):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def randint(
        self,
        _0: numpy.ndarray,
        /,
        *,
        dtype: Literal["int64"],
        high: numpy.ndarray,
        size: Tuple[numpy.int64, numpy.int64],
    ):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def randint(self, _0: int, /, *, dtype: Type[numpy.uint32], high: None, size: int):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def randint(self, _0: int, /, *, size: Tuple[int, int]):
        """
        usage.dask: 26
        usage.matplotlib: 1
        usage.sklearn: 27
        """
        ...

    @overload
    def randint(self, _0: int, /, *, size: Tuple[int, int, int]):
        """
        usage.dask: 6
        usage.sklearn: 1
        """
        ...

    @overload
    def randint(self, _0: int, /, *, size: Tuple[int]):
        """
        usage.dask: 6
        usage.sklearn: 3
        """
        ...

    @overload
    def randint(self, _0: int, /, *, size: Tuple[None, ...]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def randint(self, _0: int, _1: int, _2: List[int], /):
        """
        usage.dask: 1
        usage.sklearn: 2
        """
        ...

    @overload
    def randint(self, _0: int, _1: int, _2: numpy.ndarray, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def randint(self, _0: int, _1: int, _2: Tuple[int, int, int, int], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def randint(
        self, _0: int, _1: int, /, *, dtype: Literal["uint8"], size: Tuple[int]
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def randint(self, _0: int, _1: int, _2: Tuple[int], /):
        """
        usage.dask: 1
        usage.sklearn: 1
        """
        ...

    @overload
    def randint(self, _0: int, _1: int, /, *, size: Tuple[int]):
        """
        usage.dask: 3
        usage.sklearn: 28
        """
        ...

    @overload
    def randint(self, _0: numpy.int64, /, *, size: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def randint(
        self, _0: int, _1: int, /, *, dtype: Literal["l"], size: Tuple[int, int]
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def randint(self, _0: int, _1: int, /, *, dtype: Literal["l"], size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def randint(self, _0: int, /, *, high: int, size: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def randint(self, _0: int, /, *, size: numpy.int64):
        """
        usage.sklearn: 2
        """
        ...

    @overload
    def randint(self, _0: numpy.float64, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def randint(self, _0: int, /, *, dtype: Type[numpy.int32], size: int):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def randint(self, /, *, high: int, low: int, size: int):
        """
        usage.sklearn: 7
        """
        ...

    @overload
    def randint(self, _0: int, /, *, dtype: Literal["u8"]):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def randint(
        self, _0: int, _1: int, /, *, dtype: Type[numpy.uint8], size: Tuple[int, int]
    ):
        """
        usage.sklearn: 4
        """
        ...

    @overload
    def randint(self, _0: int, _1: int, /, *, dtype: Type[numpy.uint8], size: int):
        """
        usage.sklearn: 3
        """
        ...

    @overload
    def randint(self, _0: int, /, *, dtype: Type[bool], size: int):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def randint(self, _0: int, _1: int, _2: numpy.int64, /):
        """
        usage.sklearn: 2
        """
        ...

    @overload
    def randint(self, _0: int, _1: None, /):
        """
        usage.networkx: 1
        """
        ...

    @overload
    def randint(self, _0: float, _1: None, /):
        """
        usage.networkx: 1
        """
        ...

    def randint(
        self,
        /,
        *_args: object,
        high: Union[int, numpy.ndarray, None] = ...,
        low: int = ...,
        size: Union[
            numpy.int64, int, Tuple[Union[int, numpy.int64, None], ...], List[int], None
        ] = ...,
        dtype: Union[Literal["u8", "l", "uint8", "int64"], type, numpy.dtype] = ...,
    ):
        """
        usage.dask: 133
        usage.koalas: 7
        usage.matplotlib: 3
        usage.modin: 38
        usage.networkx: 7
        usage.pandas: 160
        usage.scipy: 66
        usage.skimage: 25
        usage.sklearn: 217
        usage.statsmodels: 81
        usage.xarray: 14
        """
        ...

    @overload
    def randn(self, _0: int, _1: int, /):
        """
        usage.dask: 39
        usage.koalas: 23
        usage.matplotlib: 4
        usage.modin: 2
        usage.scipy: 140
        usage.seaborn: 2
        usage.skimage: 22
        usage.sklearn: 351
        usage.statsmodels: 34
        usage.xarray: 97
        """
        ...

    @overload
    def randn(self, _0: int, /):
        """
        usage.dask: 43
        usage.matplotlib: 13
        usage.modin: 3
        usage.scipy: 159
        usage.seaborn: 13
        usage.skimage: 7
        usage.sklearn: 73
        usage.statsmodels: 42
        usage.xarray: 90
        """
        ...

    @overload
    def randn(self, _0: int, _1: int, _2: int, /):
        """
        usage.dask: 5
        usage.scipy: 24
        usage.skimage: 15
        usage.sklearn: 1
        usage.statsmodels: 2
        usage.xarray: 19
        """
        ...

    @overload
    def randn(self, _0: int, _1: int, _2: int, _3: int, /):
        """
        usage.skimage: 6
        usage.xarray: 2
        """
        ...

    @overload
    def randn(self, _0: int, _1: int, _2: int, _3: int, _4: int, /):
        """
        usage.skimage: 1
        usage.xarray: 2
        """
        ...

    @overload
    def randn(self, _0: numpy.int64, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def randn(
        self,
        _0: Union[numpy.int64, int] = ...,
        _1: int = ...,
        _2: int = ...,
        _3: int = ...,
        /,
    ):
        """
        usage.pandas: 749
        """
        ...

    @overload
    def randn(self, /):
        """
        usage.scipy: 7
        usage.sklearn: 4
        """
        ...

    @overload
    def randn(self, _0: int, _1: numpy.int64, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def randn(self, _0: numpy.int64, _1: int, /):
        """
        usage.sklearn: 1
        """
        ...

    def randn(self, /, *_args: Union[int, numpy.int64]):
        """
        usage.dask: 87
        usage.koalas: 23
        usage.matplotlib: 17
        usage.modin: 5
        usage.pandas: 749
        usage.scipy: 330
        usage.seaborn: 15
        usage.skimage: 51
        usage.sklearn: 431
        usage.statsmodels: 79
        usage.xarray: 210
        """
        ...

    @overload
    def random(self, _0: int, /):
        """
        usage.dask: 31
        usage.matplotlib: 7
        usage.scipy: 40
        usage.skimage: 5
        usage.sklearn: 1
        usage.statsmodels: 8
        usage.xarray: 1
        """
        ...

    @overload
    def random(self, _0: Tuple[int, int, int], /):
        """
        usage.dask: 26
        usage.matplotlib: 1
        usage.scipy: 11
        usage.skimage: 8
        usage.sklearn: 8
        usage.xarray: 2
        """
        ...

    @overload
    def random(self, _0: Tuple[int, int], /):
        """
        usage.dask: 42
        usage.matplotlib: 6
        usage.scipy: 60
        usage.skimage: 12
        usage.sklearn: 17
        usage.statsmodels: 10
        usage.xarray: 16
        """
        ...

    @overload
    def random(self, _0: Tuple[int, int, int, int], /):
        """
        usage.dask: 10
        usage.scipy: 6
        usage.skimage: 2
        """
        ...

    @overload
    def random(self, _0: Tuple[int], /):
        """
        usage.dask: 22
        usage.matplotlib: 1
        usage.scipy: 17
        usage.skimage: 4
        usage.statsmodels: 2
        usage.xarray: 3
        """
        ...

    @overload
    def random(self, _0: numpy.ndarray, /):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def random(self, /, *, size: Tuple[int, int]):
        """
        usage.dask: 8
        usage.xarray: 3
        """
        ...

    @overload
    def random(self, /, *, size: Tuple[int, int, int]):
        """
        usage.scipy: 1
        usage.xarray: 1
        """
        ...

    @overload
    def random(
        self,
        _0: Union[List[int], int, Tuple[int, int]] = ...,
        /,
        *,
        size: Tuple[int, int] = ...,
    ):
        """
        usage.pandas: 35
        """
        ...

    @overload
    def random(self, /, *, size: List[int]):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def random(self, /, *, size: int):
        """
        usage.dask: 5
        usage.scipy: 4
        """
        ...

    @overload
    def random(self, /, *, size: Tuple[int, int, int, int]):
        """
        usage.scipy: 3
        """
        ...

    @overload
    def random(self, /):
        """
        usage.matplotlib: 3
        usage.networkx: 1
        usage.sample-usage: 1
        usage.scipy: 6
        """
        ...

    @overload
    def random(self, _0: Tuple[int, int, int, int, int], /):
        """
        usage.dask: 1
        usage.scipy: 2
        """
        ...

    @overload
    def random(self, _0: List[int], /):
        """
        usage.matplotlib: 6
        usage.scipy: 69
        """
        ...

    @overload
    def random(self, _0: Tuple[None, ...], /):
        """
        usage.dask: 9
        """
        ...

    @overload
    def random(self, _0: Tuple[int, int, int, int, int, int], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def random(self, /, *, size: Tuple[int]):
        """
        usage.dask: 2
        """
        ...

    def random(
        self,
        _0: Union[int, numpy.ndarray, Tuple[Union[None, int], ...], List[int]] = ...,
        /,
        *,
        size: Union[int, Tuple[int, ...], List[int]] = ...,
    ):
        """
        usage.dask: 157
        usage.matplotlib: 24
        usage.networkx: 1
        usage.pandas: 35
        usage.sample-usage: 1
        usage.scipy: 220
        usage.skimage: 32
        usage.sklearn: 26
        usage.statsmodels: 20
        usage.xarray: 26
        """
        ...

    @overload
    def random_sample(self, _0: Tuple[int, int], /):
        """
        usage.matplotlib: 1
        usage.skimage: 1
        usage.sklearn: 120
        """
        ...

    @overload
    def random_sample(self, /, *, size: Tuple[int, int]):
        """
        usage.dask: 1
        usage.scipy: 1
        usage.sklearn: 7
        usage.xarray: 1
        """
        ...

    @overload
    def random_sample(self, _0: int, /):
        """
        usage.dask: 2
        usage.sklearn: 21
        usage.statsmodels: 2
        """
        ...

    @overload
    def random_sample(self, _0: Union[Tuple[int, int], int], /):
        """
        usage.pandas: 4
        """
        ...

    @overload
    def random_sample(self, _0: numpy.int64, /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def random_sample(self, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        usage.sklearn: 4
        """
        ...

    @overload
    def random_sample(self, /, *, size: Tuple[int, int, int]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def random_sample(self, _0: Tuple[int, int, int], /):
        """
        usage.sklearn: 2
        """
        ...

    @overload
    def random_sample(self, _0: Tuple[int], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def random_sample(self, _0: Tuple[int, int, int, int, int], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def random_sample(self, _0: Tuple[int, int, int, int], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def random_sample(self, /):
        """
        usage.networkx: 11
        """
        ...

    def random_sample(
        self,
        _0: Union[int, numpy.int64, Tuple[int, ...]] = ...,
        /,
        *,
        size: Tuple[int, ...] = ...,
    ):
        """
        usage.dask: 5
        usage.matplotlib: 1
        usage.networkx: 11
        usage.pandas: 4
        usage.scipy: 2
        usage.skimage: 1
        usage.sklearn: 157
        usage.statsmodels: 2
        usage.xarray: 1
        """
        ...

    @overload
    def rayleigh(self, _0: int, _1: int, /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def rayleigh(self, _0: float, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    def rayleigh(
        self, _0: Union[float, int], _1: int = ..., /, *, size: Tuple[int] = ...
    ):
        """
        usage.dask: 1
        usage.scipy: 1
        """
        ...

    @overload
    def seed(self, _0: int, /):
        """
        usage.dask: 14
        usage.matplotlib: 81
        usage.networkx: 14
        usage.pandas: 21
        usage.prophet: 2
        usage.scipy: 491
        usage.seaborn: 1
        usage.skimage: 25
        usage.sklearn: 4
        usage.statsmodels: 293
        """
        ...

    @overload
    def seed(self, /, *, seed: int):
        """
        usage.dask: 1
        usage.matplotlib: 1
        usage.skimage: 5
        """
        ...

    @overload
    def seed(self, _0: List[int], /):
        """
        usage.matplotlib: 1
        """
        ...

    def seed(self, _0: Union[int, List[int]] = ..., /, *, seed: int = ...):
        """
        usage.dask: 15
        usage.matplotlib: 83
        usage.networkx: 14
        usage.pandas: 21
        usage.prophet: 2
        usage.scipy: 491
        usage.seaborn: 1
        usage.skimage: 30
        usage.sklearn: 4
        usage.statsmodels: 293
        """
        ...

    def set_state(
        self, _0: Tuple[Literal["MT19937"], numpy.ndarray, int, int, float], /
    ):
        """
        usage.networkx: 1
        usage.pandas: 1
        """
        ...

    @overload
    def shuffle(self, _0: numpy.ndarray, /):
        """
        usage.dask: 7
        usage.matplotlib: 1
        usage.pandas: 3
        usage.scipy: 14
        usage.sklearn: 26
        usage.statsmodels: 5
        usage.xarray: 2
        """
        ...

    @overload
    def shuffle(self, _0: List[int], /):
        """
        usage.dask: 2
        usage.networkx: 7
        usage.scipy: 17
        """
        ...

    @overload
    def shuffle(self, _0: list, /):
        """
        usage.dask: 1
        """
        ...

    def shuffle(self, _0: Union[List[int], numpy.ndarray], /):
        """
        usage.dask: 10
        usage.matplotlib: 1
        usage.networkx: 7
        usage.pandas: 3
        usage.scipy: 31
        usage.sklearn: 26
        usage.statsmodels: 5
        usage.xarray: 2
        """
        ...

    @overload
    def standard_cauchy(self, /, *, size: Tuple[int, int]):
        """
        usage.scipy: 2
        """
        ...

    @overload
    def standard_cauchy(self, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    def standard_cauchy(self, /, *, size: Tuple[int, ...]):
        """
        usage.dask: 1
        usage.scipy: 2
        """
        ...

    @overload
    def standard_exponential(self, _0: Tuple[numpy.int64], /):
        """
        usage.scipy: 4
        """
        ...

    @overload
    def standard_exponential(self, _0: Tuple[int, int], /):
        """
        usage.scipy: 3
        """
        ...

    @overload
    def standard_exponential(self, _0: Tuple[None, ...], /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def standard_exponential(self, _0: Tuple[int, int, int], /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def standard_exponential(
        self, _0: Tuple[numpy.int64, numpy.int64, numpy.int64, numpy.int64], /
    ):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def standard_exponential(self, /, *, size: int):
        """
        usage.scipy: 3
        """
        ...

    @overload
    def standard_exponential(self, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    def standard_exponential(
        self,
        _0: Tuple[Union[int, numpy.int64, None], ...] = ...,
        /,
        *,
        size: Union[Tuple[int], int] = ...,
    ):
        """
        usage.dask: 1
        usage.scipy: 13
        """
        ...

    @overload
    def standard_gamma(self, _0: numpy.ndarray, _1: Tuple[numpy.int64], /):
        """
        usage.scipy: 2
        """
        ...

    @overload
    def standard_gamma(self, _0: numpy.ndarray, _1: numpy.int64, /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def standard_gamma(
        self,
        _0: numpy.ndarray,
        _1: Tuple[numpy.int64, numpy.int64, numpy.int64, numpy.int64],
        /,
    ):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def standard_gamma(
        self, _0: numpy.ndarray, _1: Tuple[numpy.int64, numpy.int64, numpy.int64], /
    ):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def standard_gamma(self, _0: numpy.ndarray, _1: Tuple[int, int, int], /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def standard_gamma(self, _0: numpy.ndarray, _1: Tuple[None, ...], /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def standard_gamma(self, _0: numpy.ndarray, _1: Tuple[numpy.int64, numpy.int64], /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def standard_gamma(self, _0: int, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    def standard_gamma(
        self,
        _0: Union[int, numpy.ndarray],
        _1: Union[Tuple[Union[None, numpy.int64, int], ...], numpy.int64] = ...,
        /,
        *,
        size: Tuple[int] = ...,
    ):
        """
        usage.dask: 1
        usage.scipy: 8
        """
        ...

    @overload
    def standard_normal(self, _0: Tuple[int, int], /):
        """
        usage.scipy: 2
        usage.skimage: 13
        usage.sklearn: 2
        usage.statsmodels: 43
        """
        ...

    @overload
    def standard_normal(self, _0: Tuple[int, int, int], /):
        """
        usage.scipy: 4
        usage.skimage: 2
        """
        ...

    @overload
    def standard_normal(self, _0: int, /):
        """
        usage.matplotlib: 12
        usage.scipy: 1
        usage.statsmodels: 51
        """
        ...

    @overload
    def standard_normal(self, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        usage.scipy: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    def standard_normal(self, /, *, size: Tuple[int, int]):
        """
        usage.dask: 1
        usage.scipy: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    def standard_normal(self, _0: Tuple[numpy.int64], /):
        """
        usage.scipy: 6
        """
        ...

    @overload
    def standard_normal(self, /, *, size: Tuple[numpy.int64]):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def standard_normal(self, _0: numpy.int64, /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def standard_normal(self, /, *, size: Tuple[int, numpy.int64]):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def standard_normal(self, _0: Tuple[None, ...], /):
        """
        usage.scipy: 5
        """
        ...

    @overload
    def standard_normal(self, /, *, size: Tuple[None, ...]):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def standard_normal(
        self, _0: Tuple[numpy.int64, numpy.int64, numpy.int64, numpy.int64], /
    ):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def standard_normal(self, /, *, size: Tuple[int, int, int, int]):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def standard_normal(self, _0: Tuple[int], /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def standard_normal(self, _0: Tuple[numpy.int64, numpy.int64], /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def standard_normal(self, /, *, size: Tuple[int, numpy.int64, numpy.int64]):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def standard_normal(self, /, *, size: int):
        """
        usage.scipy: 2
        """
        ...

    @overload
    def standard_normal(self, /, *, size: Tuple[int, int, int]):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def standard_normal(self, _0: Tuple[numpy.int64, numpy.int64, numpy.int64], /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def standard_normal(self, _0: List[int], /):
        """
        usage.matplotlib: 8
        """
        ...

    @overload
    def standard_normal(self, /, *, dtype: Literal["float64"], size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    def standard_normal(
        self,
        _0: Union[
            Tuple[Union[int, numpy.int64, None], ...], List[int], numpy.int64, int
        ] = ...,
        /,
        *,
        size: Union[Tuple[Union[None, numpy.int64, int], ...], int] = ...,
        dtype: Literal["float64"] = ...,
    ):
        """
        usage.dask: 3
        usage.matplotlib: 20
        usage.scipy: 33
        usage.skimage: 15
        usage.sklearn: 2
        usage.statsmodels: 96
        """
        ...

    @overload
    def standard_t(self, _0: numpy.ndarray, /, *, size: Tuple[numpy.int64]):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def standard_t(self, _0: numpy.ndarray, /, *, size: Tuple[int, int, int]):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def standard_t(self, _0: numpy.ndarray, /, *, size: Tuple[None, ...]):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def standard_t(self, _0: int, _1: int, /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def standard_t(self, _0: int, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    def standard_t(
        self,
        _0: Union[int, numpy.ndarray],
        _1: int = ...,
        /,
        *,
        size: Tuple[Union[None, numpy.int64, int], ...] = ...,
    ):
        """
        usage.dask: 1
        usage.scipy: 3
        usage.seaborn: 1
        """
        ...

    @overload
    def triangular(
        self, _0: int, _1: numpy.ndarray, _2: int, _3: Tuple[numpy.int64], /
    ):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def triangular(
        self, _0: int, _1: numpy.ndarray, _2: int, _3: Tuple[int, int, int], /
    ):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def triangular(self, _0: int, _1: numpy.ndarray, _2: int, _3: Tuple[None, ...], /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def triangular(self, _0: int, _1: int, _2: int, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    def triangular(
        self,
        _0: int,
        _1: Union[int, numpy.ndarray],
        _2: int,
        _3: Tuple[Union[int, numpy.int64, None], ...] = ...,
        /,
        *,
        size: Tuple[int] = ...,
    ):
        """
        usage.dask: 1
        usage.scipy: 3
        """
        ...

    @overload
    def uniform(self, /, *, size: Tuple[int, int]):
        """
        usage.scipy: 20
        usage.skimage: 23
        usage.sklearn: 33
        usage.statsmodels: 4
        """
        ...

    @overload
    def uniform(self, _0: float, _1: int, /):
        """
        usage.scipy: 1
        usage.skimage: 2
        """
        ...

    @overload
    def uniform(self, _0: float, _1: float, /):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def uniform(self, _0: int, _1: int, _2: Tuple[int, int], /):
        """
        usage.scipy: 3
        usage.skimage: 3
        usage.sklearn: 4
        usage.statsmodels: 3
        """
        ...

    @overload
    def uniform(self, /, *, high: float, low: float, size: Tuple[int, int]):
        """
        usage.skimage: 1
        usage.sklearn: 1
        """
        ...

    @overload
    def uniform(self, _0: int, _1: int, _2: int, /):
        """
        usage.dask: 7
        usage.scipy: 10
        usage.skimage: 2
        usage.sklearn: 5
        usage.statsmodels: 13
        """
        ...

    @overload
    def uniform(self, /, *, size: List[int]):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def uniform(self, /, *, size: int):
        """
        usage.dask: 1
        usage.matplotlib: 2
        usage.scipy: 11
        usage.sklearn: 10
        usage.statsmodels: 47
        """
        ...

    @overload
    def uniform(self, _0: int, _1: int, /, *, size: Tuple[int, int]):
        """
        usage.scipy: 2
        usage.sklearn: 3
        usage.statsmodels: 3
        """
        ...

    @overload
    def uniform(self, _0: int, _1: int, /, *, size: int):
        """
        usage.sklearn: 2
        usage.statsmodels: 9
        """
        ...

    @overload
    def uniform(self, _0: float, _1: float, _2: int, /):
        """
        usage.seaborn: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    def uniform(self, _0: int, _1: int, /):
        """
        usage.sklearn: 1
        usage.statsmodels: 4
        """
        ...

    @overload
    def uniform(self, /):
        """
        usage.scipy: 4
        usage.seaborn: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    def uniform(self, /, *, size: Tuple[int]):
        """
        usage.scipy: 2
        usage.sklearn: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    def uniform(self, _0: float, _1: float, /, *, size: int):
        """
        usage.sklearn: 2
        usage.statsmodels: 2
        """
        ...

    @overload
    def uniform(self, _0: float, _1: float, /, *, size: Tuple[int, int]):
        """
        usage.scipy: 1
        usage.sklearn: 4
        usage.statsmodels: 1
        """
        ...

    @overload
    def uniform(self, /, *, size: Union[Tuple[int, int], int] = ...):
        """
        usage.pandas: 6
        """
        ...

    @overload
    def uniform(self, _0: float, _1: float, _2: Tuple[int], /):
        """
        usage.scipy: 2
        """
        ...

    @overload
    def uniform(self, _0: float, _1: float, _2: Tuple[None, ...], /):
        """
        usage.scipy: 2
        """
        ...

    @overload
    def uniform(self, _0: numpy.ndarray, _1: numpy.ndarray, /, *, size: int):
        """
        usage.scipy: 2
        """
        ...

    @overload
    def uniform(self, _0: int, _1: int, /, *, size: Tuple[int]):
        """
        usage.scipy: 4
        """
        ...

    @overload
    def uniform(self, _0: int, _1: float, /, *, size: int):
        """
        usage.scipy: 1
        usage.sklearn: 2
        """
        ...

    @overload
    def uniform(self, /, *, high: float, low: float, size: Tuple[int]):
        """
        usage.scipy: 5
        """
        ...

    @overload
    def uniform(self, /, *, high: float, low: int, size: Tuple[int]):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def uniform(self, /, *, size: Tuple[numpy.int64]):
        """
        usage.scipy: 6
        """
        ...

    @overload
    def uniform(self, /, *, size: numpy.int64):
        """
        usage.scipy: 5
        """
        ...

    @overload
    def uniform(self, _0: float, _1: float, _2: Tuple[numpy.int64], /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def uniform(self, /, *, size: Tuple[int, int, int]):
        """
        usage.scipy: 3
        """
        ...

    @overload
    def uniform(self, /, *, size: Tuple[None, ...]):
        """
        usage.scipy: 2
        """
        ...

    @overload
    def uniform(self, /, *, size: Tuple[int, int, int, int]):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def uniform(self, /, *, size: Tuple[numpy.int64, numpy.int64, numpy.int64]):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def uniform(
        self,
        _0: float,
        _1: float,
        _2: Tuple[numpy.int64, numpy.int64, numpy.int64, numpy.int64],
        /,
    ):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def uniform(self, _0: float, _1: float, _2: Tuple[int, int], /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def uniform(self, _0: int, _1: numpy.float64, /, *, size: numpy.int64):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def uniform(self, _0: float, _1: int, _2: int, /):
        """
        usage.scipy: 8
        """
        ...

    @overload
    def uniform(self, _0: numpy.float64, _1: numpy.float64, /, *, size: numpy.int64):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def uniform(self, /, *, high: int, low: int, size: Tuple[int, int]):
        """
        usage.matplotlib: 1
        usage.sklearn: 4
        """
        ...

    @overload
    def uniform(self, _0: int, _1: float, _2: int, /):
        """
        usage.seaborn: 3
        """
        ...

    @overload
    def uniform(self, _0: float, _1: float, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def uniform(self, /, *, high: int, low: int, size: int):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def uniform(self, _0: int, _1: int, /, *, size: numpy.int64):
        """
        usage.sklearn: 4
        """
        ...

    @overload
    def uniform(self, _0: numpy.ndarray, _1: numpy.ndarray, /):
        """
        usage.sklearn: 4
        """
        ...

    @overload
    def uniform(self, /, *, high: float, size: int):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def uniform(self, _0: float, _1: int, /, *, size: int):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def uniform(self, _0: numpy.float64, _1: numpy.float64, _2: Tuple[int, int], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def uniform(self, _0: numpy.float64, _1: numpy.float64, _2: int, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def uniform(self, _0: int, _1: int, _2: List[int], /):
        """
        usage.sklearn: 1
        """
        ...

    def uniform(
        self,
        /,
        *_args: object,
        size: Union[
            Tuple[Union[None, numpy.int64, int], ...], numpy.int64, int, List[int]
        ] = ...,
        high: Union[int, float] = ...,
        low: Union[float, int] = ...,
    ):
        """
        usage.dask: 9
        usage.matplotlib: 3
        usage.pandas: 6
        usage.scipy: 102
        usage.seaborn: 5
        usage.skimage: 32
        usage.sklearn: 86
        usage.statsmodels: 89
        usage.xarray: 1
        """
        ...

    @overload
    def vonmises(self, _0: float, _1: numpy.ndarray, /, *, size: Tuple[int, int, int]):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def vonmises(self, _0: float, _1: numpy.ndarray, /, *, size: Tuple[None, ...]):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def vonmises(self, _0: int, _1: int, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    def vonmises(
        self,
        _0: Union[int, float],
        _1: Union[int, numpy.ndarray],
        /,
        *,
        size: Tuple[Union[None, int], ...],
    ):
        """
        usage.dask: 1
        usage.scipy: 2
        """
        ...

    @overload
    def wald(self, _0: numpy.ndarray, _1: float, /, *, size: Tuple[numpy.int64]):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def wald(self, _0: float, _1: float, /, *, size: Tuple[numpy.int64]):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def wald(self, _0: numpy.ndarray, _1: float, /, *, size: Tuple[int, int, int]):
        """
        usage.scipy: 2
        """
        ...

    @overload
    def wald(self, _0: numpy.ndarray, _1: float, /, *, size: Tuple[None, ...]):
        """
        usage.scipy: 2
        """
        ...

    @overload
    def wald(
        self,
        _0: numpy.ndarray,
        _1: float,
        /,
        *,
        size: Tuple[numpy.int64, numpy.int64, numpy.int64, numpy.int64],
    ):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def wald(self, _0: float, _1: float, /, *, size: Tuple[int, int]):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def wald(self, _0: float, _1: float, /, *, size: Tuple[None, ...]):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def wald(self, _0: int, _1: int, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    def wald(
        self,
        _0: Union[int, numpy.ndarray, float],
        _1: Union[int, float],
        /,
        *,
        size: Tuple[Union[int, numpy.int64, None], ...],
    ):
        """
        usage.dask: 1
        usage.scipy: 9
        """
        ...

    def weibull(self, _0: int, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def zipf(self, _0: numpy.ndarray, /, *, size: Tuple[numpy.int64]):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def zipf(self, _0: numpy.ndarray, /, *, size: Tuple[int, int]):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def zipf(self, _0: numpy.ndarray, /, *, size: Tuple[None, ...]):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def zipf(self, _0: numpy.ndarray, /, *, size: Tuple[numpy.int64, numpy.int64]):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def zipf(self, _0: int, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    def zipf(
        self,
        _0: Union[int, numpy.ndarray],
        /,
        *,
        size: Tuple[Union[int, numpy.int64, None], ...],
    ):
        """
        usage.dask: 1
        usage.scipy: 4
        """
        ...
