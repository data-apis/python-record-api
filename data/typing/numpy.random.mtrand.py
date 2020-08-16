from typing import *

# usage.skimage: 1
# usage.sklearn: 3
_rand: object


class RandomState:

    # usage.dask: 1
    __module__: ClassVar[object]

    def beta(
        self,
        _0: Union[int, float],
        _1: Union[int, float],
        /,
        *,
        size: Union[Tuple[int], int],
    ):
        """
        usage.dask: 1
        usage.pandas: 4
        """
        ...

    def binomial(
        self,
        _0: int,
        _1: Union[numpy.float64, float],
        /,
        *,
        size: Union[int, Tuple[int, ...]] = ...,
    ):
        """
        usage.dask: 1
        usage.sklearn: 11
        """
        ...

    def bytes(self, _0: int, /):
        """
        usage.dask: 1
        """
        ...

    def chisquare(self, _0: int, /, *, size: Tuple[int] = ...):
        """
        usage.dask: 1
        usage.sklearn: 2
        """
        ...

    def choice(
        self,
        _0: object,
        /,
        *,
        replace: bool = ...,
        size: Union[numpy.int64, int, List[int], Tuple[Union[None, int], ...]] = ...,
        p: Union[numpy.ndarray, List[Union[int, float]], None] = ...,
    ):
        """
        usage.dask: 32
        usage.pandas: 36
        usage.skimage: 8
        usage.sklearn: 23
        usage.xarray: 6
        """
        ...

    def exponential(self, /, *, size: Union[int, Tuple[int, ...]]):
        """
        usage.dask: 2
        usage.sklearn: 1
        """
        ...

    def f(self, _0: int, _1: int, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    def gamma(
        self,
        _0: Union[int, float],
        _1: Union[float, numpy.float64, int] = ...,
        _2: Tuple[int, int] = ...,
        /,
        *,
        size: Union[int, Tuple[int]] = ...,
    ):
        """
        usage.dask: 1
        usage.skimage: 2
        usage.sklearn: 3
        """
        ...

    def geometric(self, _0: int, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    def get_state(self, /):
        """
        usage.pandas: 1
        """
        ...

    def gumbel(self, _0: int, _1: float, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    def hypergeometric(self, _0: int, _1: int, _2: int, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    def laplace(self, _0: float, _1: float, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    def logistic(self, _0: float, _1: float, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    def lognormal(
        self,
        _0: float = ...,
        _1: float = ...,
        _2: int = ...,
        /,
        *,
        mean: float = ...,
        sigma: float = ...,
        size: Union[int, Tuple[int, ...]] = ...,
    ):
        """
        usage.dask: 1
        usage.matplotlib: 1
        usage.pandas: 1
        usage.sklearn: 3
        """
        ...

    def logseries(self, _0: float, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    def multinomial(
        self,
        _0: int,
        _1: Union[numpy.ndarray, List[float]],
        /,
        *,
        size: Union[int, Tuple[int, ...]] = ...,
    ):
        """
        usage.dask: 4
        usage.sklearn: 6
        """
        ...

    def multivariate_normal(
        self, _0: numpy.ndarray, _1: numpy.ndarray, /, *, size: int = ...
    ):
        """
        usage.sklearn: 13
        """
        ...

    def negative_binomial(self, _0: int, _1: float, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    def noncentral_chisquare(self, _0: int, _1: int, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    def noncentral_f(self, _0: int, _1: int, _2: int, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    def normal(
        self,
        _0: object = ...,
        _1: Union[
            int, float, numpy.ndarray, numpy.float64, dask.array.core.Array
        ] = ...,
        _2: Union[int, Tuple[int, int]] = ...,
        /,
        *,
        size: Union[int, Tuple[Union[None, int, numpy.int64], ...]] = ...,
        scale: Union[int, numpy.ndarray, float, numpy.int64, numpy.float64] = ...,
        loc: Union[float, numpy.ndarray, int] = ...,
    ):
        """
        usage.dask: 23
        usage.matplotlib: 25
        usage.pandas: 7
        usage.skimage: 32
        usage.sklearn: 141
        usage.xarray: 3
        """
        ...

    def pareto(self, _0: int, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    def permutation(
        self,
        _0: Union[
            List[Union[Tuple[int, int], numpy.int64]], numpy.ndarray, numpy.int64, int
        ],
        /,
    ):
        """
        usage.dask: 4
        usage.pandas: 17
        usage.skimage: 1
        usage.sklearn: 39
        """
        ...

    def poisson(
        self, /, *, size: Union[int, Tuple[int, ...]] = ..., lam: numpy.ndarray = ...
    ):
        """
        usage.dask: 3
        usage.skimage: 2
        usage.sklearn: 6
        """
        ...

    def power(self, _0: int, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    def rand(
        self,
        _0: Union[numpy.int64, int] = ...,
        _1: int = ...,
        _2: int = ...,
        _3: int = ...,
        _4: int = ...,
        /,
    ):
        """
        usage.dask: 30
        usage.matplotlib: 39
        usage.pandas: 110
        usage.skimage: 85
        usage.sklearn: 269
        usage.xarray: 19
        """
        ...

    def randint(
        self,
        _0: Union[numpy.float64, int, float, numpy.int64] = ...,
        _1: int = ...,
        _2: Union[numpy.int64, int, numpy.ndarray, List[int], Tuple[int, ...]] = ...,
        /,
        *,
        dtype: Union[Literal["u8", "l", "uint8", "int64"], type] = ...,
        size: Union[numpy.int64, int, Tuple[Union[None, int], ...], List[int]] = ...,
        high: int = ...,
        low: int = ...,
    ):
        """
        usage.dask: 133
        usage.matplotlib: 3
        usage.pandas: 160
        usage.skimage: 24
        usage.sklearn: 213
        usage.xarray: 14
        """
        ...

    def randn(
        self,
        _0: Union[int, numpy.int64] = ...,
        _1: Union[numpy.int64, int] = ...,
        _2: int = ...,
        _3: int = ...,
        _4: int = ...,
        /,
    ):
        """
        usage.dask: 88
        usage.matplotlib: 17
        usage.pandas: 749
        usage.skimage: 46
        usage.sklearn: 419
        usage.xarray: 210
        """
        ...

    def random(self, /, *, size: Union[int, Tuple[int, ...]] = ...):
        """
        usage.dask: 157
        usage.matplotlib: 24
        usage.pandas: 35
        usage.sample-usage: 1
        usage.skimage: 29
        usage.sklearn: 26
        usage.xarray: 26
        """
        ...

    def random_sample(self, /, *, size: Tuple[int, ...] = ...):
        """
        usage.dask: 5
        usage.matplotlib: 1
        usage.pandas: 4
        usage.skimage: 1
        usage.sklearn: 156
        usage.xarray: 1
        """
        ...

    def rayleigh(self, _0: float, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    def seed(self, /, *, seed: int = ...):
        """
        usage.dask: 15
        usage.matplotlib: 83
        usage.pandas: 21
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

    def shuffle(self, _0: Union[numpy.ndarray, List[int]], /):
        """
        usage.dask: 10
        usage.matplotlib: 1
        usage.pandas: 3
        usage.sklearn: 26
        usage.xarray: 2
        """
        ...

    def standard_cauchy(self, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    def standard_exponential(self, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    def standard_gamma(self, _0: int, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    def standard_normal(
        self, /, *, size: Tuple[int, ...] = ..., dtype: Literal["float64"] = ...
    ):
        """
        usage.dask: 3
        usage.matplotlib: 20
        usage.skimage: 10
        usage.sklearn: 2
        """
        ...

    def standard_t(self, _0: int, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    def triangular(self, _0: int, _1: int, _2: int, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    def uniform(
        self,
        _0: Union[float, numpy.float64, numpy.ndarray, int] = ...,
        _1: Union[numpy.float64, numpy.ndarray, int, float] = ...,
        _2: Union[int, Tuple[int, int], List[int]] = ...,
        /,
        *,
        size: Union[Tuple[int, ...], numpy.int64, int, List[int]] = ...,
        high: Union[int, float] = ...,
        low: Union[float, int] = ...,
    ):
        """
        usage.dask: 9
        usage.matplotlib: 3
        usage.pandas: 6
        usage.skimage: 29
        usage.sklearn: 84
        usage.xarray: 1
        """
        ...

    def vonmises(self, _0: int, _1: int, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    def wald(self, _0: int, _1: int, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    def weibull(self, _0: int, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    def zipf(self, _0: int, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...
