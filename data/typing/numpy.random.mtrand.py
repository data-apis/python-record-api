from typing import *

# usage.scipy: 1
# usage.skimage: 1
# usage.sklearn: 3
_rand: object


class RandomState:

    # usage.dask: 1
    __module__: ClassVar[object]

    def beta(
        self,
        _0: Union[int, float, numpy.float64, numpy.ndarray],
        _1: Union[int, float, numpy.float64, numpy.ndarray],
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

    def binomial(
        self,
        _0: Union[int, numpy.ndarray],
        _1: Union[numpy.float64, float, numpy.ndarray],
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

    def chisquare(
        self,
        _0: Union[int, numpy.ndarray, numpy.float64],
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

    def choice(
        self,
        _0: object,
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

    def exponential(self, /, *, size: Union[int, Tuple[int, ...]]):
        """
        usage.dask: 2
        usage.scipy: 3
        usage.sklearn: 1
        """
        ...

    def f(
        self,
        _0: Union[int, numpy.ndarray],
        _1: Union[int, numpy.ndarray],
        /,
        *,
        size: Tuple[int] = ...,
    ):
        """
        usage.dask: 1
        usage.scipy: 3
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

    def gumbel(
        self, _0: int = ..., _1: float = ..., /, *, size: Union[Tuple[int], int]
    ):
        """
        usage.dask: 1
        usage.scipy: 2
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

    def lognormal(
        self,
        _0: float = ...,
        _1: float = ...,
        _2: int = ...,
        /,
        *,
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

    def multinomial(
        self,
        _0: Union[int, numpy.ndarray],
        _1: Union[numpy.ndarray, List[float]],
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
        self, _0: numpy.ndarray, _1: numpy.ndarray, /, *, size: int = ...
    ):
        """
        usage.scipy: 5
        usage.sklearn: 13
        """
        ...

    def negative_binomial(
        self,
        _0: Union[int, numpy.ndarray],
        _1: Union[float, numpy.ndarray],
        /,
        *,
        size: Tuple[int] = ...,
    ):
        """
        usage.dask: 1
        usage.scipy: 7
        """
        ...

    def noncentral_chisquare(
        self,
        _0: Union[int, numpy.ndarray],
        _1: Union[int, numpy.ndarray],
        /,
        *,
        size: Tuple[int] = ...,
    ):
        """
        usage.dask: 1
        usage.scipy: 4
        """
        ...

    def noncentral_f(
        self,
        _0: Union[int, numpy.ndarray],
        _1: Union[int, numpy.ndarray],
        _2: Union[int, numpy.ndarray],
        /,
        *,
        size: Tuple[int] = ...,
    ):
        """
        usage.dask: 1
        usage.scipy: 3
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

    def pareto(self, _0: Union[int, float], /, *, size: Union[Tuple[int], int] = ...):
        """
        usage.dask: 1
        usage.scipy: 7
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

    def rand(
        self,
        _0: Union[numpy.int64, int] = ...,
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
        usage.dask: 30
        usage.matplotlib: 39
        usage.pandas: 110
        usage.scipy: 488
        usage.skimage: 85
        usage.sklearn: 269
        usage.xarray: 19
        """
        ...

    def randint(
        self,
        _0: Union[numpy.float64, int, float, numpy.ndarray, numpy.int64] = ...,
        _1: Union[int, float] = ...,
        _2: Union[numpy.int64, int, numpy.ndarray, List[int], Tuple[int, ...]] = ...,
        /,
        *,
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
        usage.scipy: 330
        usage.skimage: 46
        usage.sklearn: 419
        usage.xarray: 210
        """
        ...

    def random(self, /, *, size: Union[int, Tuple[int, ...], List[int]] = ...):
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

    def random_sample(self, /, *, size: Tuple[int, ...] = ...):
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

    def rayleigh(self, _0: Union[float, int], /, *, size: Tuple[int] = ...):
        """
        usage.dask: 1
        usage.scipy: 1
        """
        ...

    def seed(self, /, *, seed: int = ...):
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

    def standard_cauchy(self, /, *, size: Tuple[int, ...]):
        """
        usage.dask: 1
        usage.scipy: 2
        """
        ...

    def standard_exponential(self, /, *, size: Union[Tuple[int], int] = ...):
        """
        usage.dask: 1
        usage.scipy: 13
        """
        ...

    def standard_gamma(
        self, _0: Union[int, numpy.ndarray], /, *, size: Tuple[int] = ...
    ):
        """
        usage.dask: 1
        usage.scipy: 8
        """
        ...

    def standard_normal(
        self,
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

    def triangular(
        self,
        _0: int,
        _1: Union[int, numpy.ndarray],
        _2: int,
        /,
        *,
        size: Tuple[int] = ...,
    ):
        """
        usage.dask: 1
        usage.scipy: 3
        """
        ...

    def uniform(
        self,
        _0: Union[float, numpy.float64, numpy.ndarray, int] = ...,
        _1: Union[numpy.float64, numpy.ndarray, int, float] = ...,
        _2: Union[int, Tuple[Union[int, numpy.int64, None], ...], List[int]] = ...,
        /,
        *,
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
