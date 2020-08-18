from typing import *

# usage.scipy: 1
# usage.skimage: 1
# usage.sklearn: 3
_rand: object


class RandomState:

    # usage.dask: 1
    __module__: ClassVar[object]

    @overload
    def beta(self, _0: float, _1: float, /, *, size: int):
        """
        usage.pandas: 4
        """
        ...

    @overload
    def beta(
        self,
        _0: Union[numpy.float64, numpy.ndarray],
        _1: Union[numpy.float64, numpy.ndarray],
        _2: Tuple[Union[int, numpy.int64, None], ...],
        /,
    ):
        """
        usage.scipy: 8
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
        """
        ...

    @overload
    def binomial(
        self,
        _0: Union[int, numpy.ndarray],
        _1: numpy.ndarray,
        _2: Tuple[Union[None, numpy.int64, int], ...],
        /,
    ):
        """
        usage.scipy: 10
        """
        ...

    @overload
    def binomial(self, _0: int, _1: float, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def binomial(
        self,
        _0: int,
        _1: Union[float, numpy.float64],
        _2: Tuple[int, int] = ...,
        /,
        *,
        size: Union[Tuple[int, ...], int] = ...,
    ):
        """
        usage.sklearn: 11
        """
        ...

    def binomial(
        self,
        _0: Union[int, numpy.ndarray],
        _1: Union[numpy.float64, float, numpy.ndarray],
        _2: Tuple[Union[int, numpy.int64, None], ...] = ...,
        /,
        *,
        size: Union[int, Tuple[int, ...]] = ...,
    ):
        """
        usage.dask: 1
        usage.scipy: 10
        usage.sklearn: 11
        """
        ...

    def bytes(self, _0: int, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def chisquare(
        self,
        _0: Union[int, numpy.ndarray, numpy.float64],
        _1: Union[int, Tuple[Union[int, numpy.int64, None], ...]] = ...,
        /,
        *,
        size: numpy.int64 = ...,
    ):
        """
        usage.scipy: 15
        """
        ...

    @overload
    def chisquare(self, _0: int, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def chisquare(self, _0: int, _1: int, /):
        """
        usage.sklearn: 2
        """
        ...

    def chisquare(
        self,
        _0: Union[int, numpy.ndarray, numpy.float64],
        _1: Union[int, Tuple[Union[None, numpy.int64, int], ...]] = ...,
        /,
        *,
        size: Union[Tuple[int], numpy.int64] = ...,
    ):
        """
        usage.dask: 1
        usage.scipy: 15
        usage.sklearn: 2
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
        usage.skimage: 1
        """
        ...

    @overload
    def choice(self, _0: int, _1: int, /, *, replace: bool):
        """
        usage.skimage: 2
        usage.xarray: 2
        """
        ...

    @overload
    def choice(self, _0: numpy.ndarray, _1: int, /, *, replace: bool):
        """
        usage.skimage: 1
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
        usage.xarray: 1
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
    def choice(
        self,
        _0: Union[numpy.ndarray, int, range, List[Union[str, float, int]]],
        _1: int = ...,
        /,
        *,
        replace: bool = ...,
        size: int = ...,
        p: numpy.ndarray = ...,
    ):
        """
        usage.scipy: 12
        """
        ...

    @overload
    def choice(
        self,
        _0: Union[
            pandas.core.indexes.numeric.Int64Index,
            pandas.core.indexes.base.Index,
            int,
            numpy.ndarray,
            List[Union[bool, int, float, str]],
        ],
        _1: int = ...,
        /,
        *,
        p: Union[numpy.ndarray, None] = ...,
        replace: bool = ...,
        size: Union[int, Tuple[Union[None, int], ...]] = ...,
    ):
        """
        usage.dask: 32
        """
        ...

    @overload
    def choice(
        self,
        _0: Union[
            numpy.ndarray,
            int,
            List[
                Union[
                    int,
                    Dict[
                        str,
                        Union[
                            List[Union[str, int]],
                            scipy.stats._distn_infrastructure.rv_frozen,
                        ],
                    ],
                ]
            ],
        ],
        _1: Union[int, numpy.int64] = ...,
        /,
        *,
        size: Union[int, numpy.int64] = ...,
        p: numpy.ndarray = ...,
        replace: bool = ...,
    ):
        """
        usage.sklearn: 23
        """
        ...

    def choice(
        self,
        _0: object,
        _1: Union[numpy.int64, int, Tuple[int, int]] = ...,
        /,
        *,
        replace: bool = ...,
        size: Union[numpy.int64, int, List[int], Tuple[Union[None, int], ...]] = ...,
        p: Union[numpy.ndarray, List[Union[float, int]], None] = ...,
    ):
        """
        usage.dask: 32
        usage.pandas: 36
        usage.scipy: 12
        usage.skimage: 8
        usage.sklearn: 23
        usage.xarray: 6
        """
        ...

    def dirichlet(self, _0: numpy.ndarray, /, *, size: int):
        """
        usage.scipy: 4
        """
        ...

    @overload
    def exponential(self, /, *, size: Tuple[int, int]):
        """
        usage.scipy: 3
        """
        ...

    @overload
    def exponential(self, _0: int, /, *, size: Tuple[int, ...]):
        """
        usage.dask: 2
        """
        ...

    @overload
    def exponential(self, /, *, size: int):
        """
        usage.sklearn: 1
        """
        ...

    def exponential(self, _0: int = ..., /, *, size: Union[int, Tuple[int, ...]]):
        """
        usage.dask: 2
        usage.scipy: 3
        usage.sklearn: 1
        """
        ...

    @overload
    def f(
        self,
        _0: numpy.ndarray,
        _1: numpy.ndarray,
        _2: Tuple[Union[int, numpy.int64, None], ...],
        /,
    ):
        """
        usage.scipy: 3
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
    def gamma(
        self, _0: numpy.ndarray, /, *, size: Tuple[Union[None, numpy.int64, int], ...]
    ):
        """
        usage.scipy: 4
        """
        ...

    @overload
    def gamma(self, _0: int, _1: int, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def gamma(
        self,
        _0: Union[float, int],
        _1: float = ...,
        _2: Tuple[int, int] = ...,
        /,
        *,
        size: int = ...,
    ):
        """
        usage.sklearn: 3
        """
        ...

    def gamma(
        self,
        _0: Union[int, float, numpy.ndarray],
        _1: Union[float, numpy.float64, int] = ...,
        _2: Tuple[int, int] = ...,
        /,
        *,
        size: Union[int, Tuple[Union[None, numpy.int64, int], ...]] = ...,
    ):
        """
        usage.dask: 1
        usage.scipy: 4
        usage.skimage: 2
        usage.sklearn: 3
        """
        ...

    @overload
    def geometric(
        self,
        _0: Union[numpy.float64, numpy.ndarray],
        /,
        *,
        size: Tuple[Union[None, numpy.int64, int], ...],
    ):
        """
        usage.scipy: 15
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
        _1: Union[numpy.int64, numpy.ndarray],
        _2: numpy.ndarray,
        /,
        *,
        size: Tuple[Union[None, numpy.int64, int], ...],
    ):
        """
        usage.scipy: 4
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
    def laplace(
        self, _0: int, _1: int, /, *, size: Tuple[Union[int, numpy.int64, None], ...]
    ):
        """
        usage.scipy: 3
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
        _1: Union[float, int],
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
    def logistic(self, /, *, size: Tuple[Union[int, numpy.int64, None], ...]):
        """
        usage.scipy: 3
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
    def logseries(
        self, _0: numpy.ndarray, /, *, size: Tuple[Union[None, numpy.int64, int], ...]
    ):
        """
        usage.scipy: 4
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
    def multinomial(
        self,
        _0: Union[int, numpy.ndarray],
        _1: Union[List[float], numpy.ndarray],
        _2: int = ...,
        /,
        *,
        size: int = ...,
    ):
        """
        usage.scipy: 2
        """
        ...

    @overload
    def multinomial(
        self, _0: int, _1: List[float], /, *, size: Union[Tuple[int, ...], int]
    ):
        """
        usage.dask: 4
        """
        ...

    @overload
    def multinomial(self, _0: int, _1: numpy.ndarray, /, *, size: int = ...):
        """
        usage.sklearn: 6
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

    def multivariate_normal(
        self, _0: numpy.ndarray, _1: numpy.ndarray, _2: int = ..., /, *, size: int = ...
    ):
        """
        usage.scipy: 5
        usage.sklearn: 13
        """
        ...

    @overload
    def negative_binomial(
        self,
        _0: numpy.ndarray,
        _1: numpy.ndarray,
        _2: Tuple[Union[None, numpy.int64, int], ...],
        /,
    ):
        """
        usage.scipy: 7
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
        self,
        _0: numpy.ndarray,
        _1: numpy.ndarray,
        _2: Tuple[Union[None, numpy.int64, int], ...],
        /,
    ):
        """
        usage.scipy: 4
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
        _3: Tuple[Union[int, numpy.int64, None], ...],
        /,
    ):
        """
        usage.scipy: 3
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
        usage.skimage: 16
        usage.xarray: 2
        """
        ...

    @overload
    def normal(self, /, *, size: Tuple[int, int, int]):
        """
        usage.matplotlib: 1
        usage.skimage: 9
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
    def normal(
        self,
        _0: Union[int, float] = ...,
        _1: Union[int, float] = ...,
        _2: Union[int, Tuple[int, int]] = ...,
        /,
        *,
        size: Union[numpy.int64, int, Tuple[Union[int, numpy.int64], ...]] = ...,
        scale: Union[int, numpy.float64] = ...,
        loc: int = ...,
    ):
        """
        usage.scipy: 51
        """
        ...

    @overload
    def normal(self, /, *, size: int):
        """
        usage.matplotlib: 21
        """
        ...

    @overload
    def normal(self, _0: int, _1: int, _2: int, /):
        """
        usage.matplotlib: 3
        """
        ...

    @overload
    def normal(
        self,
        _0: Union[int, dask.array.core.Array, float, numpy.int64, numpy.float64] = ...,
        _1: Union[int, float, numpy.float64, dask.array.core.Array] = ...,
        /,
        *,
        size: Union[int, Tuple[Union[None, int], ...]],
    ):
        """
        usage.dask: 23
        """
        ...

    @overload
    def normal(
        self,
        _0: Union[int, numpy.ndarray] = ...,
        _1: Union[float, int] = ...,
        _2: Union[Tuple[int, int], int] = ...,
        /,
        *,
        loc: Union[float, numpy.ndarray, int] = ...,
        scale: Union[numpy.float64, numpy.int64, float, numpy.ndarray, int] = ...,
        size: Union[Tuple[Union[numpy.int64, int], int], int] = ...,
    ):
        """
        usage.sklearn: 141
        """
        ...

    def normal(
        self,
        /,
        *_args: object,
        size: Union[int, numpy.int64, Tuple[Union[None, numpy.int64, int], ...]] = ...,
        scale: Union[int, numpy.ndarray, float, numpy.int64, numpy.float64] = ...,
        loc: Union[int, numpy.ndarray, float] = ...,
    ):
        """
        usage.dask: 23
        usage.matplotlib: 25
        usage.pandas: 7
        usage.scipy: 51
        usage.skimage: 32
        usage.sklearn: 141
        usage.xarray: 3
        """
        ...

    @overload
    def pareto(self, _0: float, _1: int = ..., /, *, size: int = ...):
        """
        usage.scipy: 7
        """
        ...

    @overload
    def pareto(self, _0: int, /, *, size: Tuple[int]):
        """
        usage.dask: 1
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
        usage.scipy: 7
        """
        ...

    @overload
    def permutation(self, _0: numpy.ndarray, /):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def permutation(self, _0: Union[List[Tuple[int, int]], int], /):
        """
        usage.pandas: 17
        """
        ...

    @overload
    def permutation(self, _0: Union[numpy.ndarray, int, range, List[float]], /):
        """
        usage.scipy: 11
        """
        ...

    @overload
    def permutation(self, _0: Union[numpy.ndarray, int], /):
        """
        usage.dask: 4
        """
        ...

    @overload
    def permutation(
        self, _0: Union[int, numpy.int64, numpy.ndarray, List[numpy.int64]], /
    ):
        """
        usage.sklearn: 39
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
        usage.sklearn: 39
        """
        ...

    @overload
    def poisson(self, _0: numpy.ndarray, /):
        """
        usage.skimage: 2
        """
        ...

    @overload
    def poisson(
        self, _0: numpy.ndarray, _1: Tuple[Union[int, numpy.int64, None], ...], /
    ):
        """
        usage.scipy: 8
        """
        ...

    @overload
    def poisson(
        self,
        _0: Union[int, float, numpy.int64],
        /,
        *,
        size: Union[int, Tuple[int, ...]],
    ):
        """
        usage.dask: 3
        """
        ...

    @overload
    def poisson(self, _0: int = ..., /, *, lam: numpy.ndarray = ..., size: int = ...):
        """
        usage.sklearn: 6
        """
        ...

    def poisson(
        self,
        _0: Union[int, numpy.ndarray, float, numpy.int64] = ...,
        _1: Tuple[Union[int, numpy.int64, None], ...] = ...,
        /,
        *,
        size: Union[int, Tuple[int, ...]] = ...,
        lam: numpy.ndarray = ...,
    ):
        """
        usage.dask: 3
        usage.scipy: 8
        usage.skimage: 2
        usage.sklearn: 6
        """
        ...

    def power(self, _0: int, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rand(self, _0: int, _1: int, _2: int, /):
        """
        usage.matplotlib: 1
        usage.skimage: 12
        usage.xarray: 6
        """
        ...

    @overload
    def rand(self, _0: int, /):
        """
        usage.matplotlib: 18
        usage.skimage: 9
        usage.xarray: 1
        """
        ...

    @overload
    def rand(self, _0: int, _1: int, /):
        """
        usage.matplotlib: 20
        usage.skimage: 53
        usage.xarray: 11
        """
        ...

    @overload
    def rand(self, _0: int, _1: int, _2: int, _3: int, /):
        """
        usage.skimage: 5
        """
        ...

    @overload
    def rand(self, _0: int, _1: int, _2: int, _3: int, _4: int, /):
        """
        usage.skimage: 5
        usage.xarray: 1
        """
        ...

    @overload
    def rand(self, /):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def rand(self, _0: int = ..., _1: int = ..., _2: int = ..., /):
        """
        usage.pandas: 110
        """
        ...

    @overload
    def rand(
        self,
        _0: Union[int, numpy.int64] = ...,
        _1: int = ...,
        _2: int = ...,
        _3: int = ...,
        _4: int = ...,
        _5: int = ...,
        _6: int = ...,
        _7: int = ...,
        /,
    ):
        """
        usage.scipy: 488
        """
        ...

    @overload
    def rand(self, _0: int, _1: int = ..., _2: int = ..., _3: int = ..., /):
        """
        usage.dask: 30
        """
        ...

    @overload
    def rand(self, _0: Union[int, numpy.int64] = ..., _1: int = ..., /):
        """
        usage.sklearn: 269
        """
        ...

    def rand(self, /, *_args: Union[numpy.int64, int]):
        """
        usage.dask: 30
        usage.matplotlib: 39
        usage.pandas: 110
        usage.scipy: 488
        usage.skimage: 85
        usage.sklearn: 269
        usage.xarray: 19
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
    def randint(self, _0: int, _1: int, /, *, size: Tuple[int, int]):
        """
        usage.skimage: 8
        usage.xarray: 2
        """
        ...

    @overload
    def randint(self, _0: int, _1: int, /):
        """
        usage.skimage: 5
        """
        ...

    @overload
    def randint(self, _0: int, _1: int, /, *, size: int):
        """
        usage.matplotlib: 2
        usage.skimage: 3
        """
        ...

    @overload
    def randint(self, _0: int, /):
        """
        usage.skimage: 2
        usage.xarray: 1
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
        usage.skimage: 1
        """
        ...

    @overload
    def randint(self, _0: int, /, *, size: int):
        """
        usage.skimage: 2
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
        usage.xarray: 4
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
    def randint(
        self,
        _0: Union[int, numpy.ndarray] = ...,
        _1: Union[int, float] = ...,
        _2: Union[Tuple[int, int], int] = ...,
        /,
        *,
        high: Union[None, int, numpy.ndarray] = ...,
        dtype: Union[Type[numpy.uint32], numpy.dtype, Literal["int64"]] = ...,
        size: Union[
            int, None, List[int], Tuple[Union[None, numpy.int64, int], ...]
        ] = ...,
        low: int = ...,
    ):
        """
        usage.scipy: 66
        """
        ...

    @overload
    def randint(self, _0: int, /, *, size: Tuple[int, int]):
        """
        usage.matplotlib: 1
        """
        ...

    @overload
    def randint(
        self,
        _0: Union[int, numpy.int64],
        _1: int = ...,
        _2: Union[Tuple[int, ...], List[int], numpy.ndarray, int] = ...,
        /,
        *,
        size: Union[int, Tuple[Union[None, int], ...]] = ...,
        dtype: Literal["l", "uint8"] = ...,
        high: int = ...,
    ):
        """
        usage.dask: 133
        """
        ...

    @overload
    def randint(
        self,
        _0: Union[int, numpy.float64] = ...,
        _1: int = ...,
        _2: Union[Tuple[int, ...], List[int], int, numpy.int64] = ...,
        /,
        *,
        size: Union[Tuple[int, ...], int, numpy.int64] = ...,
        dtype: Union[type, Literal["u8"]] = ...,
        high: int = ...,
        low: int = ...,
    ):
        """
        usage.sklearn: 213
        """
        ...

    def randint(
        self,
        /,
        *_args: object,
        dtype: Union[Literal["u8", "l", "uint8", "int64"], type, numpy.dtype] = ...,
        size: Union[
            numpy.int64, int, Tuple[Union[None, numpy.int64, int], ...], None, List[int]
        ] = ...,
        high: Union[int, numpy.ndarray, None] = ...,
        low: int = ...,
    ):
        """
        usage.dask: 133
        usage.matplotlib: 3
        usage.pandas: 160
        usage.scipy: 66
        usage.skimage: 24
        usage.sklearn: 213
        usage.xarray: 14
        """
        ...

    @overload
    def randn(self, _0: int, /):
        """
        usage.matplotlib: 13
        usage.skimage: 7
        usage.xarray: 90
        """
        ...

    @overload
    def randn(self, _0: int, _1: int, _2: int, /):
        """
        usage.skimage: 14
        usage.xarray: 19
        """
        ...

    @overload
    def randn(self, _0: int, _1: int, /):
        """
        usage.matplotlib: 4
        usage.skimage: 18
        usage.xarray: 97
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
    def randn(self, _0: int = ..., _1: int = ..., _2: int = ..., /):
        """
        usage.scipy: 330
        """
        ...

    @overload
    def randn(self, _0: int, _1: int = ..., _2: int = ..., /):
        """
        usage.dask: 88
        """
        ...

    @overload
    def randn(
        self,
        _0: Union[numpy.int64, int] = ...,
        _1: Union[int, numpy.int64] = ...,
        _2: int = ...,
        /,
    ):
        """
        usage.sklearn: 419
        """
        ...

    def randn(self, /, *_args: Union[int, numpy.int64]):
        """
        usage.dask: 88
        usage.matplotlib: 17
        usage.pandas: 749
        usage.scipy: 330
        usage.skimage: 46
        usage.sklearn: 419
        usage.xarray: 210
        """
        ...

    @overload
    def random(self, _0: int, /):
        """
        usage.matplotlib: 7
        usage.skimage: 4
        usage.xarray: 1
        """
        ...

    @overload
    def random(self, _0: Tuple[int, int, int], /):
        """
        usage.matplotlib: 1
        usage.skimage: 7
        usage.xarray: 2
        """
        ...

    @overload
    def random(self, _0: Tuple[int, int], /):
        """
        usage.matplotlib: 6
        usage.skimage: 11
        usage.xarray: 16
        """
        ...

    @overload
    def random(self, _0: Tuple[int, int, int, int], /):
        """
        usage.skimage: 2
        """
        ...

    @overload
    def random(self, _0: Tuple[int], /):
        """
        usage.matplotlib: 1
        usage.skimage: 4
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
        usage.xarray: 3
        """
        ...

    @overload
    def random(self, /, *, size: Tuple[int, int, int]):
        """
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
    def random(
        self,
        _0: Union[List[int], Tuple[int, ...], int] = ...,
        /,
        *,
        size: Union[Tuple[int, ...], List[int], int] = ...,
    ):
        """
        usage.scipy: 220
        """
        ...

    @overload
    def random(self, /):
        """
        usage.matplotlib: 3
        usage.sample-usage: 1
        """
        ...

    @overload
    def random(self, _0: List[int], /):
        """
        usage.matplotlib: 6
        """
        ...

    @overload
    def random(
        self,
        _0: Union[Tuple[Union[int, None], ...], int] = ...,
        /,
        *,
        size: Union[Tuple[int, ...], int] = ...,
    ):
        """
        usage.dask: 157
        """
        ...

    @overload
    def random(self, _0: Union[Tuple[int, ...], int], /):
        """
        usage.sklearn: 26
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
        usage.pandas: 35
        usage.sample-usage: 1
        usage.scipy: 220
        usage.skimage: 29
        usage.sklearn: 26
        usage.xarray: 26
        """
        ...

    @overload
    def random_sample(self, _0: Tuple[int, int], /):
        """
        usage.matplotlib: 1
        usage.skimage: 1
        """
        ...

    @overload
    def random_sample(self, /, *, size: Tuple[int, int]):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def random_sample(self, _0: Union[Tuple[int, int], int], /):
        """
        usage.pandas: 4
        """
        ...

    @overload
    def random_sample(self, _0: numpy.int64 = ..., /, *, size: Tuple[int, int] = ...):
        """
        usage.scipy: 2
        """
        ...

    @overload
    def random_sample(self, _0: int = ..., /, *, size: Tuple[int, ...] = ...):
        """
        usage.dask: 5
        """
        ...

    @overload
    def random_sample(
        self, _0: Union[Tuple[int, ...], int] = ..., /, *, size: Tuple[int, ...] = ...
    ):
        """
        usage.sklearn: 156
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
        usage.pandas: 4
        usage.scipy: 2
        usage.skimage: 1
        usage.sklearn: 156
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
        usage.matplotlib: 81
        usage.pandas: 21
        usage.scipy: 489
        usage.skimage: 21
        """
        ...

    @overload
    def seed(self, /, *, seed: int):
        """
        usage.matplotlib: 1
        usage.skimage: 4
        """
        ...

    @overload
    def seed(self, _0: List[int], /):
        """
        usage.matplotlib: 1
        """
        ...

    @overload
    def seed(self, _0: int = ..., /, *, seed: int = ...):
        """
        usage.dask: 15
        """
        ...

    def seed(self, _0: Union[int, List[int]] = ..., /, *, seed: int = ...):
        """
        usage.dask: 15
        usage.matplotlib: 83
        usage.pandas: 21
        usage.scipy: 489
        usage.skimage: 25
        """
        ...

    def set_state(
        self, _0: Tuple[Literal["MT19937"], numpy.ndarray, int, int, float], /
    ):
        """
        usage.pandas: 1
        """
        ...

    @overload
    def shuffle(self, _0: numpy.ndarray, /):
        """
        usage.matplotlib: 1
        usage.pandas: 3
        usage.sklearn: 26
        usage.xarray: 2
        """
        ...

    @overload
    def shuffle(self, _0: Union[List[int], numpy.ndarray], /):
        """
        usage.scipy: 31
        """
        ...

    @overload
    def shuffle(self, _0: Union[numpy.ndarray, List[int]], /):
        """
        usage.dask: 10
        """
        ...

    def shuffle(self, _0: Union[numpy.ndarray, List[int]], /):
        """
        usage.dask: 10
        usage.matplotlib: 1
        usage.pandas: 3
        usage.scipy: 31
        usage.sklearn: 26
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
    def standard_exponential(
        self, _0: Tuple[Union[int, numpy.int64, None], ...] = ..., /, *, size: int = ...
    ):
        """
        usage.scipy: 13
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
    def standard_gamma(
        self,
        _0: numpy.ndarray,
        _1: Union[Tuple[Union[None, numpy.int64, int], ...], numpy.int64],
        /,
    ):
        """
        usage.scipy: 8
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
        usage.skimage: 8
        usage.sklearn: 2
        """
        ...

    @overload
    def standard_normal(self, _0: Tuple[int, int, int], /):
        """
        usage.skimage: 2
        """
        ...

    @overload
    def standard_normal(
        self,
        _0: Union[Tuple[Union[None, numpy.int64, int], ...], int, numpy.int64] = ...,
        /,
        *,
        size: Union[Tuple[Union[None, int, numpy.int64], ...], int] = ...,
    ):
        """
        usage.scipy: 33
        """
        ...

    @overload
    def standard_normal(self, _0: int, /):
        """
        usage.matplotlib: 12
        """
        ...

    @overload
    def standard_normal(self, _0: List[int], /):
        """
        usage.matplotlib: 8
        """
        ...

    @overload
    def standard_normal(
        self, /, *, size: Tuple[int, ...], dtype: Literal["float64"] = ...
    ):
        """
        usage.dask: 3
        """
        ...

    def standard_normal(
        self,
        _0: Union[
            Tuple[Union[int, numpy.int64, None], ...], List[int], numpy.int64, int
        ] = ...,
        /,
        *,
        size: Union[Tuple[Union[numpy.int64, int, None], ...], int] = ...,
        dtype: Literal["float64"] = ...,
    ):
        """
        usage.dask: 3
        usage.matplotlib: 20
        usage.scipy: 33
        usage.skimage: 10
        usage.sklearn: 2
        """
        ...

    @overload
    def standard_t(
        self, _0: numpy.ndarray, /, *, size: Tuple[Union[int, numpy.int64, None], ...]
    ):
        """
        usage.scipy: 3
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
    def triangular(
        self,
        _0: int,
        _1: numpy.ndarray,
        _2: int,
        _3: Tuple[Union[int, numpy.int64, None], ...],
        /,
    ):
        """
        usage.scipy: 3
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
        usage.skimage: 21
        """
        ...

    @overload
    def uniform(self, _0: float, _1: int, /):
        """
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
        usage.skimage: 2
        """
        ...

    @overload
    def uniform(self, /, *, high: float, low: float, size: Tuple[int, int]):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def uniform(self, _0: int, _1: int, _2: int, /):
        """
        usage.skimage: 2
        """
        ...

    @overload
    def uniform(self, /, *, size: List[int]):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def uniform(self, /, *, size: Union[Tuple[int, int], int] = ...):
        """
        usage.pandas: 6
        """
        ...

    @overload
    def uniform(
        self,
        _0: Union[numpy.float64, int, numpy.ndarray, float] = ...,
        _1: Union[numpy.float64, numpy.ndarray, float, int] = ...,
        _2: Union[int, Tuple[Union[numpy.int64, int, None], ...]] = ...,
        /,
        *,
        size: Union[numpy.int64, int, Tuple[Union[numpy.int64, int, None], ...]] = ...,
        high: float = ...,
        low: Union[int, float] = ...,
    ):
        """
        usage.scipy: 100
        """
        ...

    @overload
    def uniform(self, /, *, high: int, low: int, size: Tuple[int, int]):
        """
        usage.matplotlib: 1
        """
        ...

    @overload
    def uniform(self, /, *, size: int):
        """
        usage.matplotlib: 2
        """
        ...

    @overload
    def uniform(
        self,
        _0: Union[int, float] = ...,
        _1: Union[int, float] = ...,
        _2: int = ...,
        /,
        *,
        size: Union[int, Tuple[int]] = ...,
    ):
        """
        usage.dask: 9
        """
        ...

    @overload
    def uniform(
        self,
        _0: Union[int, numpy.ndarray, numpy.float64, float] = ...,
        _1: Union[float, int, numpy.ndarray, numpy.float64] = ...,
        _2: Union[List[int], Tuple[int, int], int] = ...,
        /,
        *,
        size: Union[int, numpy.int64, Tuple[int, ...]] = ...,
        high: Union[float, int] = ...,
        low: Union[int, float] = ...,
    ):
        """
        usage.sklearn: 84
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
        usage.scipy: 100
        usage.skimage: 29
        usage.sklearn: 84
        usage.xarray: 1
        """
        ...

    @overload
    def vonmises(
        self, _0: float, _1: numpy.ndarray, /, *, size: Tuple[Union[int, None], ...]
    ):
        """
        usage.scipy: 2
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
    def wald(
        self,
        _0: Union[float, numpy.ndarray],
        _1: float,
        /,
        *,
        size: Tuple[Union[None, numpy.int64, int], ...],
    ):
        """
        usage.scipy: 9
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
    def zipf(
        self, _0: numpy.ndarray, /, *, size: Tuple[Union[None, numpy.int64, int], ...]
    ):
        """
        usage.scipy: 4
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
