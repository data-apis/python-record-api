from typing import *

# usage.skimage: 1
# usage.sklearn: 1
_rand: object


class RandomState:

    # usage.dask: 1
    __module__: ClassVar[object]

    @classmethod
    def random(_0: numpy.random.mtrand.RandomState, /):
        "\n    usage.sample_usage: 1\n    "
        ...

    @classmethod
    def rand(
        _0: numpy.random.mtrand.RandomState,
        _1: Union[int, numpy.int64] = ...,
        _2: int = ...,
        _3: int = ...,
        /,
    ):
        "\n    usage.skimage: 4\n    usage.sklearn: 114\n    usage.dask: 4\n    "
        ...

    @classmethod
    def randint(
        _0: numpy.random.mtrand.RandomState,
        _1: Union[numpy.float64, int, float],
        _2: int = ...,
        _3: Union[Tuple[int, int], int, List[int]] = ...,
        /,
    ):
        "\n    usage.skimage: 8\n    usage.sklearn: 33\n    "
        ...

    @classmethod
    def choice(
        _0: numpy.random.mtrand.RandomState,
        _1: Union[List[Union[Callable, int]], range],
        /,
    ):
        "\n    usage.skimage: 1\n    usage.xarray: 1\n    usage.sklearn: 1\n    "
        ...

    @classmethod
    def uniform(
        _0: numpy.random.mtrand.RandomState,
        _1: Union[numpy.ndarray, int, float],
        _2: Union[numpy.ndarray, int, float],
        /,
    ):
        "\n    usage.skimage: 3\n    usage.sklearn: 9\n    "
        ...

    @classmethod
    def seed(_0: numpy.random.mtrand.RandomState, _1: int, /):
        "\n    usage.skimage: 1\n    usage.dask: 1\n    "
        ...

    @classmethod
    def randn(
        _0: numpy.random.mtrand.RandomState,
        _1: Union[numpy.int64, int],
        _2: Union[numpy.int64, int] = ...,
        _3: int = ...,
        /,
    ):
        "\n    usage.skimage: 1\n    usage.xarray: 13\n    usage.sklearn: 238\n    "
        ...

    @classmethod
    def random_sample(
        _0: numpy.random.mtrand.RandomState, _1: Union[int, Tuple[int, int]], /
    ):
        "\n    usage.skimage: 1\n    usage.sklearn: 20\n    usage.dask: 1\n    "
        ...

    @classmethod
    def permutation(
        _0: numpy.random.mtrand.RandomState,
        _1: Union[numpy.int64, int, numpy.ndarray, List[numpy.int64]],
        /,
    ):
        "\n    usage.skimage: 1\n    usage.sklearn: 18\n    "
        ...

    @classmethod
    def standard_normal(_0: numpy.random.mtrand.RandomState, _1: Tuple[int, ...], /):
        "\n    usage.skimage: 4\n    usage.sklearn: 2\n    "
        ...

    @classmethod
    def multinomial(_0: numpy.random.mtrand.RandomState, _1: int, _2: numpy.ndarray, /):
        "\n    usage.sklearn: 4\n    "
        ...

    @classmethod
    def shuffle(_0: numpy.random.mtrand.RandomState, _1: numpy.ndarray, /):
        "\n    usage.sklearn: 18\n    usage.dask: 4\n    "
        ...

    @classmethod
    def poisson(_0: numpy.random.mtrand.RandomState, _1: int, /):
        "\n    usage.sklearn: 2\n    "
        ...

    @classmethod
    def gamma(
        _0: numpy.random.mtrand.RandomState,
        _1: float,
        _2: float,
        _3: Tuple[int, int],
        /,
    ):
        "\n    usage.sklearn: 2\n    "
        ...

    @classmethod
    def binomial(
        _0: numpy.random.mtrand.RandomState, _1: int, _2: Union[float, numpy.float64], /
    ):
        "\n    usage.sklearn: 3\n    "
        ...

    @classmethod
    def multivariate_normal(
        _0: numpy.random.mtrand.RandomState,
        _1: numpy.ndarray,
        _2: numpy.ndarray,
        _3: int,
        /,
    ):
        "\n    usage.sklearn: 2\n    "
        ...

    @classmethod
    def normal(
        _0: numpy.random.mtrand.RandomState, _1: int, _2: int, _3: Tuple[int, int], /
    ):
        "\n    usage.sklearn: 3\n    "
        ...

    @classmethod
    def chisquare(_0: numpy.random.mtrand.RandomState, _1: int, _2: int, /):
        "\n    usage.sklearn: 2\n    "
        ...

    @classmethod
    def bytes(_0: numpy.random.mtrand.RandomState, _1: int, /):
        "\n    usage.dask: 1\n    "
        ...

    def random(self: object, /, *, size: Union[int, Tuple[int, ...]] = ...):
        "\n    usage.skimage: 29\n    usage.xarray: 25\n    usage.sklearn: 2\n    usage.dask: 158\n    "
        ...

    def rand(
        self: object,
        _0: int = ...,
        _1: int = ...,
        _2: int = ...,
        _3: int = ...,
        _4: int = ...,
        /,
    ):
        "\n    usage.skimage: 90\n    usage.xarray: 16\n    usage.sklearn: 5\n    usage.dask: 26\n    "
        ...

    def uniform(
        self: object,
        _0: Union[float, int] = ...,
        _1: Union[float, int] = ...,
        _2: Union[int, Tuple[int, int]] = ...,
        /,
        *,
        size: Union[Tuple[int, ...], int, numpy.int64, List[int]] = ...,
        low: Union[float, int] = ...,
        high: Union[float, int] = ...,
    ):
        "\n    usage.skimage: 29\n    usage.xarray: 1\n    usage.sklearn: 33\n    usage.dask: 10\n    "
        ...

    def randint(
        self: object,
        _0: Union[numpy.int64, int] = ...,
        _1: int = ...,
        _2: Union[int, numpy.ndarray, List[int], Tuple[int, ...]] = ...,
        /,
        *,
        size: Union[Tuple[Union[int, None], ...], int, numpy.int64, List[int]] = ...,
        dtype: Union[Literal[("l", "uint8", "u8")], type] = ...,
        low: int = ...,
        high: int = ...,
    ):
        "\n    usage.skimage: 15\n    usage.xarray: 14\n    usage.sklearn: 62\n    usage.dask: 133\n    "
        ...

    def seed(self: object, /, *, seed: int = ...):
        "\n    usage.skimage: 25\n    usage.dask: 18\n    "
        ...

    def choice(
        self: object,
        _0: Union[
            List[Union[bool, float, int, str]],
            numpy.ndarray,
            int,
            pandas.core.indexes.base.Index,
            pandas.core.indexes.numeric.Int64Index,
        ],
        /,
        *,
        size: Union[Tuple[Union[int, None], ...], int, numpy.int64, List[int]] = ...,
        replace: bool = ...,
        p: Union[None, numpy.ndarray, List[Union[float, int]]] = ...,
    ):
        "\n    usage.skimage: 7\n    usage.xarray: 5\n    usage.sklearn: 10\n    usage.dask: 32\n    "
        ...

    def normal(
        self: object,
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
        "\n    usage.skimage: 32\n    usage.xarray: 1\n    usage.sklearn: 72\n    usage.dask: 23\n    "
        ...

    def randn(
        self: object,
        _0: int,
        _1: int = ...,
        _2: int = ...,
        _3: int = ...,
        _4: int = ...,
        /,
    ):
        "\n    usage.skimage: 44\n    usage.xarray: 178\n    usage.sklearn: 13\n    usage.dask: 90\n    "
        ...

    def standard_normal(
        self: object, /, *, size: Tuple[int, ...] = ..., dtype: Literal["float64"] = ...
    ):
        "\n    usage.skimage: 6\n    usage.dask: 3\n    "
        ...

    def gamma(
        self: object, _0: Union[int, float], /, *, size: Union[Tuple[int], int] = ...
    ):
        "\n    usage.skimage: 2\n    usage.sklearn: 1\n    usage.dask: 1\n    "
        ...

    def poisson(
        self: object,
        _0: Union[numpy.int64, float, int, numpy.ndarray],
        /,
        *,
        size: Union[int, Tuple[int, ...]] = ...,
    ):
        "\n    usage.skimage: 2\n    usage.dask: 3\n    "
        ...

    def random_sample(self: object, /, *, size: Tuple[int, ...] = ...):
        "\n    usage.xarray: 1\n    usage.sklearn: 2\n    usage.dask: 4\n    "
        ...

    def multivariate_normal(
        self: object, _0: numpy.ndarray, _1: numpy.ndarray, /, *, size: int
    ):
        "\n    usage.sklearn: 4\n    "
        ...

    def binomial(
        self: object, _0: int, _1: float, /, *, size: Union[Tuple[int, ...], int]
    ):
        "\n    usage.sklearn: 4\n    usage.dask: 1\n    "
        ...

    def exponential(self: object, /, *, size: Union[Tuple[int, ...], int]):
        "\n    usage.sklearn: 1\n    usage.dask: 2\n    "
        ...

    def lognormal(
        self: object,
        _0: float = ...,
        _1: float = ...,
        /,
        *,
        size: Union[Tuple[int], int],
    ):
        "\n    usage.sklearn: 3\n    usage.dask: 1\n    "
        ...

    def multinomial(
        self: object,
        _0: int,
        _1: Union[List[float], numpy.ndarray],
        /,
        *,
        size: Union[int, Tuple[int, ...]],
    ):
        "\n    usage.sklearn: 1\n    usage.dask: 4\n    "
        ...

    def beta(self: object, _0: int, _1: int, /, *, size: Tuple[int]):
        "\n    usage.dask: 1\n    "
        ...

    def chisquare(self: object, _0: int, /, *, size: Tuple[int]):
        "\n    usage.dask: 1\n    "
        ...

    def f(self: object, _0: int, _1: int, /, *, size: Tuple[int]):
        "\n    usage.dask: 1\n    "
        ...

    def geometric(self: object, _0: int, /, *, size: Tuple[int]):
        "\n    usage.dask: 1\n    "
        ...

    def gumbel(self: object, _0: int, _1: float, /, *, size: Tuple[int]):
        "\n    usage.dask: 1\n    "
        ...

    def hypergeometric(self: object, _0: int, _1: int, _2: int, /, *, size: Tuple[int]):
        "\n    usage.dask: 1\n    "
        ...

    def laplace(self: object, _0: float, _1: float, /, *, size: Tuple[int]):
        "\n    usage.dask: 1\n    "
        ...

    def logistic(self: object, _0: float, _1: float, /, *, size: Tuple[int]):
        "\n    usage.dask: 1\n    "
        ...

    def logseries(self: object, _0: float, /, *, size: Tuple[int]):
        "\n    usage.dask: 1\n    "
        ...

    def negative_binomial(self: object, _0: int, _1: float, /, *, size: Tuple[int]):
        "\n    usage.dask: 1\n    "
        ...

    def noncentral_chisquare(self: object, _0: int, _1: int, /, *, size: Tuple[int]):
        "\n    usage.dask: 1\n    "
        ...

    def noncentral_f(self: object, _0: int, _1: int, _2: int, /, *, size: Tuple[int]):
        "\n    usage.dask: 1\n    "
        ...

    def pareto(self: object, _0: int, /, *, size: Tuple[int]):
        "\n    usage.dask: 1\n    "
        ...

    def power(self: object, _0: int, /, *, size: Tuple[int]):
        "\n    usage.dask: 1\n    "
        ...

    def rayleigh(self: object, _0: float, /, *, size: Tuple[int]):
        "\n    usage.dask: 1\n    "
        ...

    def triangular(self: object, _0: int, _1: int, _2: int, /, *, size: Tuple[int]):
        "\n    usage.dask: 1\n    "
        ...

    def vonmises(self: object, _0: int, _1: int, /, *, size: Tuple[int]):
        "\n    usage.dask: 1\n    "
        ...

    def wald(self: object, _0: int, _1: int, /, *, size: Tuple[int]):
        "\n    usage.dask: 1\n    "
        ...

    def weibull(self: object, _0: int, /, *, size: Tuple[int]):
        "\n    usage.dask: 1\n    "
        ...

    def zipf(self: object, _0: int, /, *, size: Tuple[int]):
        "\n    usage.dask: 1\n    "
        ...

    def standard_cauchy(self: object, /, *, size: Tuple[int]):
        "\n    usage.dask: 1\n    "
        ...

    def standard_exponential(self: object, /, *, size: Tuple[int]):
        "\n    usage.dask: 1\n    "
        ...

    def standard_gamma(self: object, _0: int, /, *, size: Tuple[int]):
        "\n    usage.dask: 1\n    "
        ...

    def standard_t(self: object, _0: int, /, *, size: Tuple[int]):
        "\n    usage.dask: 1\n    "
        ...

    def shuffle(self: object, _0: Union[numpy.ndarray, List[int]], /):
        "\n    usage.dask: 6\n    "
        ...

    def permutation(self: object, _0: Union[numpy.ndarray, int], /):
        "\n    usage.dask: 4\n    "
        ...
