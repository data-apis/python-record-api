_rand = ...


class RandomState:
    @classmethod
    def random(_0: numpy.random.mtrand.RandomState, /):
        "usage.sample_usage: 1"

    @classmethod
    def rand(_0: numpy.random.mtrand.RandomState, _1: int = ..., /):
        "usage.skimage: 4"

    @classmethod
    def randint(
        _0: numpy.random.mtrand.RandomState,
        _1: Union[(int, float)],
        _2: int = ...,
        _3: tuple[(int, int)] = ...,
        /,
    ):
        "usage.skimage: 8"

    @classmethod
    def choice(
        _0: numpy.random.mtrand.RandomState, _1: Union[(list[Callable], range)] = ..., /
    ):
        "usage.skimage: 1\nusage.xarray: 1"

    @classmethod
    def uniform(
        _0: numpy.random.mtrand.RandomState, _1: float, _2: Union[(int, float)], /
    ):
        "usage.skimage: 3"

    @classmethod
    def seed(_0: numpy.random.mtrand.RandomState, _1: int, /):
        "usage.skimage: 1"

    @classmethod
    def randn(_0: numpy.random.mtrand.RandomState, _1: int = ..., /):
        "usage.skimage: 1\nusage.xarray: 13"

    @classmethod
    def random_sample(_0: numpy.random.mtrand.RandomState, _1: tuple[(int, int)], /):
        "usage.skimage: 1"

    @classmethod
    def permutation(_0: numpy.random.mtrand.RandomState, _1: numpy.ndarray, /):
        "usage.skimage: 1"

    @classmethod
    def standard_normal(_0: numpy.random.mtrand.RandomState, _1: tuple[(int, ...)], /):
        "usage.skimage: 4"

    def random(self=..., /, *, size: tuple[(int, ...)] = ...):
        "usage.skimage: 29\nusage.xarray: 25"

    def rand(
        self,
        _0: int = ...,
        _1: int = ...,
        _2: int = ...,
        _3: int = ...,
        _4: int = ...,
        /,
    ):
        "usage.skimage: 90\nusage.xarray: 16"

    def uniform(
        self,
        _0: int = ...,
        _1: int = ...,
        _2: Union[(int, tuple[(int, int)])] = ...,
        /,
        *,
        size: Union[(tuple[(int, int)], list[int])] = ...,
        low: float = ...,
        high: float = ...,
    ):
        "usage.skimage: 29\nusage.xarray: 1"

    def randint(
        self,
        _0: int,
        _1: int = ...,
        _2: Union[(tuple[(int, int, int)], int)] = ...,
        /,
        *,
        size: Union[(tuple[(int, int, int)], int, list[int], tuple[(int, int)])] = ...,
        dtype: list[numpy.uint8] = ...,
    ):
        "usage.skimage: 15\nusage.xarray: 14"

    def seed(self=..., /, *, seed: int = ...):
        "usage.skimage: 25"

    def choice(
        self,
        _0: Union[
            (int, list[Literal[("c", "d", "a", "b")]], list[bool], numpy.ndarray)
        ] = ...,
        /,
        *,
        size: Union[(int, list[int], tuple[(int, int)])] = ...,
        replace: bool = ...,
        p: list[Union[(int, float)]] = ...,
    ):
        "usage.skimage: 7\nusage.xarray: 3"

    def normal(
        self,
        _0: Union[(int, float)] = ...,
        _1: Union[(numpy.ndarray, float)] = ...,
        _2: tuple[(int, int)] = ...,
        /,
        *,
        size: tuple[(int, ...)] = ...,
    ):
        "usage.skimage: 32\nusage.xarray: 1"

    def randn(
        self, _0: int, _1: int = ..., _2: int = ..., _3: int = ..., _4: int = ..., /
    ):
        "usage.skimage: 44\nusage.xarray: 164"

    def standard_normal(self, _0: tuple[(int, ...)], /):
        "usage.skimage: 6"

    def gamma(self, _0: float, _1: numpy.float64, /):
        "usage.skimage: 2"

    def poisson(self, _0: numpy.ndarray, /):
        "usage.skimage: 2"

    def random_sample(self, /, *, size: tuple[(int, int)] = None):
        "usage.xarray: 1"
