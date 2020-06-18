from typing import *

_rand = ...


class RandomState:
    __module__ = ...

    @classmethod
    def random(_0: numpy.random.mtrand.RandomState, /):
        "usage.sample_usage: 1"

    @classmethod
    def rand(
        _0: numpy.random.mtrand.RandomState,
        _1: Union[(int, numpy.int64)] = ...,
        _2: int = ...,
        _3: int = ...,
        /,
    ):
        "usage.skimage: 4, usage.sklearn: 114, usage.dask: 4"

    @classmethod
    def randint(
        _0: numpy.random.mtrand.RandomState,
        _1: Union[(numpy.float64, int, float)],
        _2: int = ...,
        _3: Union[(Tuple[(int, int)], int, List[int])] = ...,
        /,
    ):
        "usage.skimage: 8, usage.sklearn: 33"

    @classmethod
    def choice(
        _0: numpy.random.mtrand.RandomState,
        _1: Union[(List[Union[(Callable, int)]], range)] = ...,
        /,
    ):
        "usage.skimage: 1, usage.xarray: 1, usage.sklearn: 1"

    @classmethod
    def uniform(
        _0: numpy.random.mtrand.RandomState,
        _1: Union[(numpy.ndarray, int, float)],
        _2: Union[(numpy.ndarray, int, float)] = ...,
        /,
    ):
        "usage.skimage: 3, usage.sklearn: 9"

    @classmethod
    def seed(_0: numpy.random.mtrand.RandomState, _1: int, /):
        "usage.skimage: 1, usage.dask: 1"

    @classmethod
    def randn(
        _0: numpy.random.mtrand.RandomState,
        _1: Union[(numpy.int64, int)],
        _2: Union[(numpy.int64, int)] = ...,
        _3: int = ...,
        /,
    ):
        "usage.skimage: 1, usage.xarray: 13, usage.sklearn: 238"

    @classmethod
    def random_sample(
        _0: numpy.random.mtrand.RandomState, _1: Union[(int, Tuple[(int, int)])], /
    ):
        "usage.skimage: 1, usage.sklearn: 20, usage.dask: 1"

    @classmethod
    def permutation(
        _0: numpy.random.mtrand.RandomState,
        _1: Union[(numpy.int64, int, numpy.ndarray, List[numpy.int64])],
        /,
    ):
        "usage.skimage: 1, usage.sklearn: 18"

    @classmethod
    def standard_normal(_0: numpy.random.mtrand.RandomState, _1: Tuple[(int, ...)], /):
        "usage.skimage: 4, usage.sklearn: 2"

    @classmethod
    def multinomial(_0: numpy.random.mtrand.RandomState, _1: int, _2: numpy.ndarray, /):
        "usage.sklearn: 4"

    @classmethod
    def shuffle(_0: numpy.random.mtrand.RandomState, _1: numpy.ndarray, /):
        "usage.sklearn: 18, usage.dask: 4"

    @classmethod
    def poisson(_0: numpy.random.mtrand.RandomState, _1: int, /):
        "usage.sklearn: 2"

    @classmethod
    def gamma(
        _0: numpy.random.mtrand.RandomState,
        _1: float,
        _2: float,
        _3: Tuple[(int, int)],
        /,
    ):
        "usage.sklearn: 2"

    @classmethod
    def binomial(
        _0: numpy.random.mtrand.RandomState,
        _1: int,
        _2: Union[(float, numpy.float64)] = ...,
        /,
    ):
        "usage.sklearn: 3"

    @classmethod
    def multivariate_normal(
        _0: numpy.random.mtrand.RandomState,
        _1: numpy.ndarray,
        _2: numpy.ndarray,
        _3: int,
        /,
    ):
        "usage.sklearn: 2"

    @classmethod
    def normal(
        _0: numpy.random.mtrand.RandomState, _1: int, _2: int, _3: Tuple[(int, int)], /
    ):
        "usage.sklearn: 3"

    @classmethod
    def chisquare(_0: numpy.random.mtrand.RandomState, _1: int, _2: int, /):
        "usage.sklearn: 2"

    @classmethod
    def bytes(_0: numpy.random.mtrand.RandomState, _1: int, /):
        "usage.dask: 1"

    def random(self=..., /, *, size: Union[(int, Tuple[(int, ...)])] = ...):
        "usage.skimage: 29, usage.xarray: 25, usage.sklearn: 2, usage.dask: 158"

    def rand(
        self,
        _0: int = ...,
        _1: int = ...,
        _2: int = ...,
        _3: int = ...,
        _4: int = ...,
        /,
    ):
        "usage.skimage: 90, usage.xarray: 16, usage.sklearn: 5, usage.dask: 26"

    def uniform(
        self,
        _0: Union[(float, int)] = ...,
        _1: Union[(float, int)] = ...,
        _2: Union[(int, Tuple[(int, int)])] = ...,
        /,
        *,
        size: Union[(Tuple[(int, ...)], int, numpy.int64, List[int])] = ...,
        low: Union[(float, int)] = ...,
        high: Union[(float, int)] = ...,
    ):
        "usage.skimage: 29, usage.xarray: 1, usage.sklearn: 33, usage.dask: 10"

    def randint(
        self,
        _0: Union[(numpy.int64, int)] = ...,
        _1: int = ...,
        _2: Union[(int, numpy.ndarray, List[int], Tuple[(int, ...)])] = ...,
        /,
        *,
        size: Union[
            (Tuple[(Union[(int, None)], ...)], int, numpy.int64, List[int])
        ] = ...,
        dtype: Union[(Literal[("l", "uint8", "u8")], type)] = ...,
        low: int = ...,
        high: int = ...,
    ):
        "usage.skimage: 15, usage.xarray: 14, usage.sklearn: 62, usage.dask: 133"

    def seed(self=..., /, *, seed: int = ...):
        "usage.skimage: 25, usage.dask: 18"

    def choice(
        self,
        _0: Union[
            (
                List[Union[(bool, float, int, str)]],
                numpy.ndarray,
                int,
                pandas.core.indexes.base.Index,
                pandas.core.indexes.numeric.Int64Index,
            )
        ] = ...,
        /,
        *,
        size: Union[
            (Tuple[(Union[(int, None)], ...)], int, numpy.int64, List[int])
        ] = ...,
        replace: bool = ...,
        p: Union[(None, numpy.ndarray, List[Union[(float, int)]])] = ...,
    ):
        "usage.skimage: 7, usage.xarray: 5, usage.sklearn: 10, usage.dask: 32"

    def normal(
        self,
        _0: Union[
            (numpy.float64, numpy.int64, float, dask.array.core.Array, int)
        ] = ...,
        _1: Union[
            (dask.array.core.Array, numpy.float64, float, int, numpy.ndarray)
        ] = ...,
        _2: Tuple[(int, int)] = ...,
        /,
        *,
        size: Union[(Tuple[(Union[(numpy.int64, int, None)], ...)], int)] = ...,
        scale: Union[(int, numpy.ndarray, numpy.float64, float)] = ...,
        loc: Union[(int, numpy.ndarray)] = ...,
    ):
        "usage.skimage: 32, usage.xarray: 1, usage.sklearn: 72, usage.dask: 23"

    def randn(
        self, _0: int, _1: int = ..., _2: int = ..., _3: int = ..., _4: int = ..., /
    ):
        "usage.skimage: 44, usage.xarray: 178, usage.sklearn: 13, usage.dask: 90"

    def standard_normal(
        self=...,
        /,
        *,
        size: Tuple[(int, ...)] = ...,
        dtype: Literal[("float64",)] = ...,
    ):
        "usage.skimage: 6, usage.dask: 3"

    def gamma(
        self,
        _0: Union[(int, float)] = ...,
        /,
        *,
        size: Union[(Tuple[(int,)], int)] = ...,
    ):
        "usage.skimage: 2, usage.sklearn: 1, usage.dask: 1"

    def poisson(
        self,
        _0: Union[(numpy.int64, float, int, numpy.ndarray)],
        /,
        *,
        size: Union[(int, Tuple[(int, ...)])] = ...,
    ):
        "usage.skimage: 2, usage.dask: 3"

    def random_sample(self=..., /, *, size: Tuple[(int, ...)] = ...):
        "usage.xarray: 1, usage.sklearn: 2, usage.dask: 4"

    def multivariate_normal(
        self, _0: numpy.ndarray, _1: numpy.ndarray, /, *, size: int = None
    ):
        "usage.sklearn: 4"

    def binomial(
        self, _0: int, _1: float, /, *, size: Union[(Tuple[(int, ...)], int)] = None
    ):
        "usage.sklearn: 4, usage.dask: 1"

    def exponential(self=..., /, *, size: Union[(Tuple[(int, ...)], int)] = None):
        "usage.sklearn: 1, usage.dask: 2"

    def lognormal(
        self,
        _0: float = ...,
        _1: float = ...,
        /,
        *,
        size: Union[(Tuple[(int,)], int)] = None,
    ):
        "usage.sklearn: 3, usage.dask: 1"

    def multinomial(
        self,
        _0: int,
        _1: Union[(List[float], numpy.ndarray)],
        /,
        *,
        size: Union[(int, Tuple[(int, ...)])] = None,
    ):
        "usage.sklearn: 1, usage.dask: 4"

    def beta(self, _0: int, _1: int, /, *, size: Tuple[(int,)] = None):
        "usage.dask: 1"

    def chisquare(self, _0: int, /, *, size: Tuple[(int,)] = None):
        "usage.dask: 1"

    def f(self, _0: int, _1: int, /, *, size: Tuple[(int,)] = None):
        "usage.dask: 1"

    def geometric(self, _0: int, /, *, size: Tuple[(int,)] = None):
        "usage.dask: 1"

    def gumbel(self, _0: int, _1: float, /, *, size: Tuple[(int,)] = None):
        "usage.dask: 1"

    def hypergeometric(
        self, _0: int, _1: int, _2: int, /, *, size: Tuple[(int,)] = None
    ):
        "usage.dask: 1"

    def laplace(self, _0: float, _1: float, /, *, size: Tuple[(int,)] = None):
        "usage.dask: 1"

    def logistic(self, _0: float, _1: float, /, *, size: Tuple[(int,)] = None):
        "usage.dask: 1"

    def logseries(self, _0: float, /, *, size: Tuple[(int,)] = None):
        "usage.dask: 1"

    def negative_binomial(self, _0: int, _1: float, /, *, size: Tuple[(int,)] = None):
        "usage.dask: 1"

    def noncentral_chisquare(self, _0: int, _1: int, /, *, size: Tuple[(int,)] = None):
        "usage.dask: 1"

    def noncentral_f(self, _0: int, _1: int, _2: int, /, *, size: Tuple[(int,)] = None):
        "usage.dask: 1"

    def pareto(self, _0: int, /, *, size: Tuple[(int,)] = None):
        "usage.dask: 1"

    def power(self, _0: int, /, *, size: Tuple[(int,)] = None):
        "usage.dask: 1"

    def rayleigh(self, _0: float, /, *, size: Tuple[(int,)] = None):
        "usage.dask: 1"

    def triangular(self, _0: int, _1: int, _2: int, /, *, size: Tuple[(int,)] = None):
        "usage.dask: 1"

    def vonmises(self, _0: int, _1: int, /, *, size: Tuple[(int,)] = None):
        "usage.dask: 1"

    def wald(self, _0: int, _1: int, /, *, size: Tuple[(int,)] = None):
        "usage.dask: 1"

    def weibull(self, _0: int, /, *, size: Tuple[(int,)] = None):
        "usage.dask: 1"

    def zipf(self, _0: int, /, *, size: Tuple[(int,)] = None):
        "usage.dask: 1"

    def standard_cauchy(self, /, *, size: Tuple[(int,)] = None):
        "usage.dask: 1"

    def standard_exponential(self, /, *, size: Tuple[(int,)] = None):
        "usage.dask: 1"

    def standard_gamma(self, _0: int, /, *, size: Tuple[(int,)] = None):
        "usage.dask: 1"

    def standard_t(self, _0: int, /, *, size: Tuple[(int,)] = None):
        "usage.dask: 1"

    def shuffle(self, _0: Union[(numpy.ndarray, List[int])], /):
        "usage.dask: 6"

    def permutation(self, _0: Union[(numpy.ndarray, int)], /):
        "usage.dask: 4"
