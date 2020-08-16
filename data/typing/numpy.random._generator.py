from typing import *


class Generator:
    def beta(
        self,
        _0: Union[numpy.float64, numpy.ndarray],
        _1: Union[numpy.float64, numpy.ndarray],
        _2: Tuple[numpy.int64],
        /,
    ):
        """
        usage.scipy: 2
        """
        ...

    def binomial(
        self,
        _0: Union[numpy.ndarray, int],
        _1: numpy.ndarray,
        _2: Tuple[numpy.int64],
        /,
    ):
        """
        usage.scipy: 2
        """
        ...

    def chisquare(self, _0: Union[int, numpy.ndarray], /, *, size: numpy.int64 = ...):
        """
        usage.scipy: 3
        """
        ...

    def choice(
        self,
        _0: int,
        /,
        *,
        replace: bool = ...,
        size: int = ...,
        p: numpy.ndarray = ...,
    ):
        """
        usage.scipy: 3
        """
        ...

    def dirichlet(self, _0: numpy.ndarray, /, *, size: int):
        """
        usage.scipy: 1
        """
        ...

    def f(self, _0: numpy.ndarray, _1: numpy.ndarray, _2: Tuple[numpy.int64], /):
        """
        usage.scipy: 1
        """
        ...

    def gamma(self, _0: numpy.ndarray, /, *, size: Tuple[numpy.int64]):
        """
        usage.scipy: 1
        """
        ...

    def geometric(
        self, _0: Union[numpy.ndarray, numpy.float64], /, *, size: Tuple[numpy.int64]
    ):
        """
        usage.scipy: 4
        """
        ...

    def integers(
        self,
        _0: Union[numpy.ndarray, int],
        /,
        *,
        dtype: Literal["int64"],
        endpoint: bool,
        high: Union[numpy.ndarray, int, None],
        size: Union[Tuple[numpy.int64], int],
    ):
        """
        usage.scipy: 3
        """
        ...

    def laplace(self, _0: int, _1: int, /, *, size: Tuple[numpy.int64]):
        """
        usage.scipy: 1
        """
        ...

    def logistic(self, /, *, size: Tuple[numpy.int64]):
        """
        usage.scipy: 1
        """
        ...

    def multinomial(self, _0: numpy.ndarray, _1: numpy.ndarray, _2: int, /):
        """
        usage.scipy: 1
        """
        ...

    def multivariate_normal(
        self, _0: numpy.ndarray, _1: numpy.ndarray, /, *, size: int = ...
    ):
        """
        usage.scipy: 2
        """
        ...

    def negative_binomial(
        self, _0: numpy.ndarray, _1: numpy.ndarray, _2: Tuple[numpy.int64], /
    ):
        """
        usage.scipy: 1
        """
        ...

    def noncentral_chisquare(
        self, _0: numpy.ndarray, _1: numpy.ndarray, _2: Tuple[numpy.int64], /
    ):
        """
        usage.scipy: 1
        """
        ...

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

    def normal(
        self, /, *, size: Union[Tuple[Union[int, numpy.int64], ...], numpy.int64]
    ):
        """
        usage.scipy: 6
        """
        ...

    def permutation(self, _0: range, /):
        """
        usage.scipy: 1
        """
        ...

    def poisson(self, _0: numpy.ndarray, _1: Tuple[numpy.int64], /):
        """
        usage.scipy: 1
        """
        ...

    def shuffle(self, _0: List[int], /):
        """
        usage.scipy: 1
        """
        ...

    def standard_exponential(self, _0: Tuple[numpy.int64], /):
        """
        usage.scipy: 2
        """
        ...

    def standard_gamma(
        self, _0: numpy.ndarray, _1: Union[numpy.int64, Tuple[numpy.int64]], /
    ):
        """
        usage.scipy: 3
        """
        ...

    def standard_normal(self, /, *, size: Tuple[Union[numpy.int64, int], ...] = ...):
        """
        usage.scipy: 10
        """
        ...

    def standard_t(self, _0: numpy.ndarray, /, *, size: Tuple[numpy.int64]):
        """
        usage.scipy: 1
        """
        ...

    def triangular(
        self, _0: int, _1: numpy.ndarray, _2: int, _3: Tuple[numpy.int64], /
    ):
        """
        usage.scipy: 1
        """
        ...

    def uniform(
        self,
        _0: Union[float, numpy.ndarray] = ...,
        _1: Union[float, int, numpy.ndarray] = ...,
        _2: Tuple[Union[int, numpy.int64]] = ...,
        /,
        *,
        size: Union[numpy.int64, int, Tuple[Union[numpy.int64, int], ...]] = ...,
    ):
        """
        usage.scipy: 23
        """
        ...

    def wald(
        self, _0: Union[float, numpy.ndarray], _1: float, /, *, size: Tuple[numpy.int64]
    ):
        """
        usage.scipy: 2
        """
        ...
