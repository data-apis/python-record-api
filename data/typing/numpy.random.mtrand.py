from typing import *

# usage.skimage: 1
# usage.sklearn: 1
_rand: object


class RandomState:

    # usage.dask: 1
    __module__: ClassVar[object]

    def beta(self, _0: int, _1: int, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    def binomial(
        self,
        _0: int,
        _1: Union[float, numpy.float64],
        /,
        *,
        size: Union[Tuple[int, ...], int] = ...,
    ):
        """
        usage.sklearn: 7
        usage.dask: 1
        """
        ...

    def bytes(self, _0: int, /):
        """
        usage.dask: 1
        """
        ...

    def chisquare(self, _0: int, /, *, size: Tuple[int] = ...):
        """
        usage.sklearn: 2
        usage.dask: 1
        """
        ...

    def choice(
        self,
        _0: object,
        /,
        *,
        size: Union[Tuple[Union[int, None], ...], int, numpy.int64, List[int]] = ...,
        replace: bool = ...,
        p: Union[None, numpy.ndarray, List[Union[float, int]]] = ...,
    ):
        """
        usage.skimage: 8
        usage.xarray: 6
        usage.sklearn: 11
        usage.dask: 32
        """
        ...

    def exponential(self, /, *, size: Union[Tuple[int, ...], int]):
        """
        usage.sklearn: 1
        usage.dask: 2
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
        _1: Union[int, numpy.float64, float] = ...,
        _2: Tuple[int, int] = ...,
        /,
        *,
        size: Union[Tuple[int], int] = ...,
    ):
        """
        usage.skimage: 2
        usage.sklearn: 3
        usage.dask: 1
        """
        ...

    def geometric(self, _0: int, /, *, size: Tuple[int]):
        """
        usage.dask: 1
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
        self, _0: float = ..., _1: float = ..., /, *, size: Union[Tuple[int], int]
    ):
        """
        usage.sklearn: 3
        usage.dask: 1
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
        _1: Union[List[float], numpy.ndarray],
        /,
        *,
        size: Union[int, Tuple[int, ...]] = ...,
    ):
        """
        usage.sklearn: 5
        usage.dask: 4
        """
        ...

    def multivariate_normal(
        self, _0: numpy.ndarray, _1: numpy.ndarray, /, *, size: int = ...
    ):
        """
        usage.sklearn: 6
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
        _0: Union[numpy.float64, numpy.int64, float, dask.array.core.Array, int] = ...,
        _1: Union[
            dask.array.core.Array, numpy.float64, float, int, numpy.ndarray
        ] = ...,
        _2: Tuple[int, int] = ...,
        /,
        *,
        size: Union[Tuple[Union[numpy.int64, int, None], ...], int] = ...,
        scale: Union[int, numpy.ndarray, numpy.float64, float] = ...,
        loc: Union[int, numpy.ndarray] = ...,
    ):
        """
        usage.skimage: 32
        usage.xarray: 1
        usage.sklearn: 75
        usage.dask: 23
        """
        ...

    def pareto(self, _0: int, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    def permutation(
        self, _0: Union[int, numpy.ndarray, numpy.int64, List[numpy.int64]], /
    ):
        """
        usage.skimage: 1
        usage.sklearn: 18
        usage.dask: 4
        """
        ...

    def poisson(
        self,
        _0: Union[numpy.int64, float, int, numpy.ndarray],
        /,
        *,
        size: Union[int, Tuple[int, ...]] = ...,
    ):
        """
        usage.skimage: 2
        usage.sklearn: 2
        usage.dask: 3
        """
        ...

    def power(self, _0: int, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    def rand(
        self,
        _0: Union[int, numpy.int64] = ...,
        _1: int = ...,
        _2: int = ...,
        _3: int = ...,
        _4: int = ...,
        /,
    ):
        """
        usage.skimage: 94
        usage.xarray: 16
        usage.sklearn: 119
        usage.dask: 30
        """
        ...

    def randint(
        self,
        _0: Union[numpy.int64, int, float, numpy.float64] = ...,
        _1: int = ...,
        _2: Union[int, numpy.ndarray, List[int], Tuple[int, ...]] = ...,
        /,
        *,
        size: Union[Tuple[Union[int, None], ...], int, numpy.int64, List[int]] = ...,
        dtype: Union[Literal["l", "uint8", "u8"], type] = ...,
        low: int = ...,
        high: int = ...,
    ):
        """
        usage.skimage: 23
        usage.xarray: 14
        usage.sklearn: 95
        usage.dask: 133
        """
        ...

    def randn(
        self,
        _0: Union[int, numpy.int64],
        _1: Union[int, numpy.int64] = ...,
        _2: int = ...,
        _3: int = ...,
        _4: int = ...,
        /,
    ):
        """
        usage.skimage: 45
        usage.xarray: 191
        usage.sklearn: 251
        usage.dask: 90
        """
        ...

    def random(self, /, *, size: Union[int, Tuple[int, ...]] = ...):
        """
        usage.sample_usage: 1
        usage.skimage: 29
        usage.xarray: 25
        usage.sklearn: 2
        usage.dask: 158
        """
        ...

    def random_sample(self, /, *, size: Tuple[int, ...] = ...):
        """
        usage.skimage: 1
        usage.xarray: 1
        usage.sklearn: 22
        usage.dask: 5
        """
        ...

    def rayleigh(self, _0: float, /, *, size: Tuple[int]):
        """
        usage.dask: 1
        """
        ...

    def seed(self, /, *, seed: int = ...):
        """
        usage.skimage: 26
        usage.dask: 19
        """
        ...

    def shuffle(self, _0: Union[List[int], numpy.ndarray], /):
        """
        usage.sklearn: 18
        usage.dask: 10
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
        usage.skimage: 10
        usage.sklearn: 2
        usage.dask: 3
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
        _0: Union[float, int, numpy.ndarray] = ...,
        _1: Union[float, int, numpy.ndarray] = ...,
        _2: Union[int, Tuple[int, int]] = ...,
        /,
        *,
        size: Union[Tuple[int, ...], int, numpy.int64, List[int]] = ...,
        low: Union[float, int] = ...,
        high: Union[float, int] = ...,
    ):
        """
        usage.skimage: 32
        usage.xarray: 1
        usage.sklearn: 42
        usage.dask: 10
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
