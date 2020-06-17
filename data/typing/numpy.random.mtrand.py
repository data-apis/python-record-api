from typing import *

_rand = ...


class RandomState:
    @classmethod
    def random(_0: numpy.random.mtrand.RandomState, /):
        "usage.sample_usage: 1"

    @classmethod
    def rand(
        _0: numpy.random.mtrand.RandomState,
        _1: Union[(int, numpy.int64)] = ...,
        _2: int = ...,
        /,
    ):
        "usage.skimage: 4, usage.sklearn: 114"

    @classmethod
    def randint(
        _0: numpy.random.mtrand.RandomState,
        _1: Union[(int, numpy.float64, float)],
        _2: int = ...,
        _3: Union[(int, List[int], Tuple[(int, int)])] = ...,
        /,
    ):
        "usage.skimage: 8, usage.sklearn: 33"

    @classmethod
    def choice(
        _0: numpy.random.mtrand.RandomState,
        _1: Union[(range, List[int], List[Callable])] = ...,
        /,
    ):
        "usage.skimage: 1, usage.xarray: 1, usage.sklearn: 1"

    @classmethod
    def uniform(
        _0: numpy.random.mtrand.RandomState,
        _1: Union[(int, numpy.ndarray, float)],
        _2: Union[(int, numpy.ndarray, float)] = ...,
        /,
    ):
        "usage.skimage: 3, usage.sklearn: 9"

    @classmethod
    def seed(_0: numpy.random.mtrand.RandomState, _1: int, /):
        "usage.skimage: 1"

    @classmethod
    def randn(
        _0: numpy.random.mtrand.RandomState,
        _1: Union[(int, numpy.int64)],
        _2: Union[(int, numpy.int64)] = ...,
        _3: int = ...,
        /,
    ):
        "usage.skimage: 1, usage.xarray: 13, usage.sklearn: 238"

    @classmethod
    def random_sample(
        _0: numpy.random.mtrand.RandomState, _1: Union[(int, Tuple[(int, int)])], /
    ):
        "usage.skimage: 1, usage.sklearn: 20"

    @classmethod
    def permutation(
        _0: numpy.random.mtrand.RandomState,
        _1: Union[(numpy.ndarray, int, numpy.int64, List[numpy.int64])],
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
        "usage.sklearn: 18"

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

    def random(self=..., /, *, size: Tuple[(int, ...)] = ...):
        "usage.skimage: 29, usage.xarray: 25, usage.sklearn: 2"

    def rand(
        self,
        _0: int = ...,
        _1: int = ...,
        _2: int = ...,
        _3: int = ...,
        _4: int = ...,
        /,
    ):
        "usage.skimage: 90, usage.xarray: 16, usage.sklearn: 5"

    def uniform(
        self,
        _0: Union[(int, float)] = ...,
        _1: Union[(int, float)] = ...,
        _2: Union[(Tuple[(int, int)], int)] = ...,
        /,
        *,
        size: Union[
            (int, List[int], Tuple[(int,)], numpy.int64, Tuple[(int, int)])
        ] = ...,
        high: Union[(int, float)] = ...,
        low: Union[(int, float)] = ...,
    ):
        "usage.skimage: 29, usage.xarray: 1, usage.sklearn: 33"

    def randint(
        self,
        _0: int = ...,
        _1: int = ...,
        _2: Union[(int, Tuple[(int, int, int)])] = ...,
        /,
        *,
        size=...,
        dtype: Union[(Type[numpy.uint8], Literal[("u8",)], Type[bool])] = ...,
        low: int = ...,
        high: int = ...,
    ):
        "usage.skimage: 15, usage.xarray: 14, usage.sklearn: 62"

    def seed(self=..., /, *, seed: int = ...):
        "usage.skimage: 25"

    def choice(
        self,
        _0: Union[
            (List[Literal[("a", "d", "b", "c")]], int, List[bool], numpy.ndarray)
        ] = ...,
        /,
        *,
        size: Union[(int, List[int], Tuple[(int, int)], numpy.int64)] = ...,
        replace: bool = ...,
        p: Union[(numpy.ndarray, List[Union[(int, float)]])] = ...,
    ):
        "usage.skimage: 7, usage.xarray: 5, usage.sklearn: 10"

    def normal(
        self,
        _0: Union[(float, int)] = ...,
        _1: Union[(numpy.ndarray, float)] = ...,
        _2: Tuple[(int, int)] = ...,
        /,
        *,
        size: Union[
            (Tuple[(numpy.int64, int)], int, Tuple[(int, ...)], Tuple[(int, int)])
        ] = ...,
        scale: Union[(numpy.ndarray, float, numpy.float64, int)] = ...,
        loc: Union[(numpy.ndarray, int)] = ...,
    ):
        "usage.skimage: 32, usage.xarray: 1, usage.sklearn: 72"

    def randn(
        self, _0: int, _1: int = ..., _2: int = ..., _3: int = ..., _4: int = ..., /
    ):
        "usage.skimage: 44, usage.xarray: 178, usage.sklearn: 13"

    def standard_normal(self, _0: Tuple[(int, ...)], /):
        "usage.skimage: 6"

    def gamma(self, _0: Union[(int, float)] = ..., /, *, size: int = ...):
        "usage.skimage: 2, usage.sklearn: 1"

    def poisson(self, _0: numpy.ndarray, /):
        "usage.skimage: 2"

    def random_sample(self, /, *, size: Tuple[(int, int)] = None):
        "usage.xarray: 1, usage.sklearn: 2"

    def multivariate_normal(
        self, _0: numpy.ndarray, _1: numpy.ndarray, /, *, size: int = None
    ):
        "usage.sklearn: 4"

    def binomial(
        self, _0: int, _1: float, /, *, size: Union[(Tuple[(int, int)], int)] = None
    ):
        "usage.sklearn: 4"

    def exponential(self, /, *, size: int = None):
        "usage.sklearn: 1"

    def lognormal(self, /, *, size: int = None):
        "usage.sklearn: 3"

    def multinomial(self, _0: int, _1: numpy.ndarray, /, *, size: int = None):
        "usage.sklearn: 1"
