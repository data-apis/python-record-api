from typing import *

# usage.skimage: 1
# usage.sklearn: 3
_rand: object


class RandomState:
    def beta(self, _0: float, _1: float, /, *, size: int):
        """
        usage.pandas: 4
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
        usage.sklearn: 11
        """
        ...

    def chisquare(self, _0: int, _1: int, /):
        """
        usage.sklearn: 2
        """
        ...

    def choice(
        self,
        _0: Union[
            List[
                Union[
                    Dict[
                        str,
                        Union[
                            List[Union[str, int]],
                            scipy.stats._distn_infrastructure.rv_frozen,
                        ],
                    ],
                    int,
                    bool,
                    str,
                    Callable,
                ]
            ],
            range,
            int,
            pandas.core.indexes.datetimes.DatetimeIndex,
            numpy.ndarray,
        ],
        /,
        *,
        p: Union[numpy.ndarray, None, List[Union[float, int]]] = ...,
        replace: bool = ...,
        size: Union[List[int], Tuple[int, int], int, numpy.int64] = ...,
    ):
        """
        usage.pandas: 36
        usage.skimage: 8
        usage.sklearn: 23
        usage.xarray: 6
        """
        ...

    def exponential(self, /, *, size: int):
        """
        usage.sklearn: 1
        """
        ...

    def gamma(
        self,
        _0: Union[int, float],
        _1: Union[float, numpy.float64] = ...,
        _2: Tuple[int, int] = ...,
        /,
        *,
        size: int = ...,
    ):
        """
        usage.skimage: 2
        usage.sklearn: 3
        """
        ...

    def get_state(self, /):
        """
        usage.pandas: 1
        """
        ...

    def lognormal(
        self, _0: float = ..., _1: float = ..., _2: int = ..., /, *, size: int = ...
    ):
        """
        usage.pandas: 1
        usage.sklearn: 3
        """
        ...

    def multinomial(self, _0: int, _1: numpy.ndarray, /, *, size: int = ...):
        """
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

    def normal(
        self,
        _0: Union[numpy.ndarray, int, float] = ...,
        _1: Union[int, float, numpy.ndarray] = ...,
        _2: Union[int, Tuple[int, int]] = ...,
        /,
        *,
        size: Union[Tuple[Union[numpy.int64, int], ...], int] = ...,
        loc: Union[float, numpy.ndarray, int] = ...,
        scale: Union[int, numpy.ndarray, float, numpy.int64, numpy.float64] = ...,
    ):
        """
        usage.pandas: 7
        usage.skimage: 32
        usage.sklearn: 141
        usage.xarray: 3
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
        usage.pandas: 17
        usage.skimage: 1
        usage.sklearn: 39
        """
        ...

    def poisson(self, /, *, lam: numpy.ndarray = ..., size: int = ...):
        """
        usage.skimage: 2
        usage.sklearn: 6
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
        usage.pandas: 110
        usage.skimage: 85
        usage.sklearn: 269
        usage.xarray: 19
        """
        ...

    def randint(
        self,
        _0: Union[int, float, numpy.float64] = ...,
        _1: int = ...,
        _2: Union[Tuple[int, ...], int, numpy.int64, List[int]] = ...,
        /,
        *,
        size: Union[Tuple[int, ...], List[int], int, numpy.int64] = ...,
        dtype: Union[Literal["u8", "int64"], type] = ...,
        high: int = ...,
        low: int = ...,
    ):
        """
        usage.pandas: 160
        usage.skimage: 24
        usage.sklearn: 213
        usage.xarray: 14
        """
        ...

    def randn(
        self,
        _0: Union[int, numpy.int64] = ...,
        _1: Union[int, numpy.int64] = ...,
        _2: int = ...,
        _3: int = ...,
        _4: int = ...,
        /,
    ):
        """
        usage.pandas: 749
        usage.skimage: 46
        usage.sklearn: 419
        usage.xarray: 210
        """
        ...

    def random(self, /, *, size: Tuple[int, ...] = ...):
        """
        usage.pandas: 35
        usage.sample-usage: 1
        usage.skimage: 29
        usage.sklearn: 26
        usage.xarray: 26
        """
        ...

    def random_sample(self, /, *, size: Tuple[int, ...] = ...):
        """
        usage.pandas: 4
        usage.skimage: 1
        usage.sklearn: 156
        usage.xarray: 1
        """
        ...

    def seed(self, /, *, seed: int = ...):
        """
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

    def shuffle(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 3
        usage.sklearn: 26
        usage.xarray: 2
        """
        ...

    def standard_normal(self, _0: Tuple[int, ...], /):
        """
        usage.skimage: 10
        usage.sklearn: 2
        """
        ...

    def uniform(
        self,
        _0: Union[float, numpy.float64, numpy.ndarray, int] = ...,
        _1: Union[numpy.float64, numpy.ndarray, int, float] = ...,
        _2: Union[int, Tuple[int, int], List[int]] = ...,
        /,
        *,
        size: Union[List[int], int, numpy.int64, Tuple[int, ...]] = ...,
        high: Union[int, float] = ...,
        low: Union[float, int] = ...,
    ):
        """
        usage.pandas: 6
        usage.skimage: 29
        usage.sklearn: 84
        usage.xarray: 1
        """
        ...
