

class RandomState():

    @classmethod
    def random(_0: numpy.random.mtrand.RandomState, /):
        'usage.sample_usage: 1'

    @classmethod
    def rand(_0: numpy.random.mtrand.RandomState, _1: int, _0: numpy.random.mtrand.RandomState=..., _1: int=..., /):
        'usage.skimage: 4'

    @classmethod
    def randint(_0: numpy.random.mtrand.RandomState, _1: Union[(float, int)], _0: numpy.random.mtrand.RandomState=..., _1: Union[(float, int)]=..., /):
        'usage.skimage: 8'

    @classmethod
    def choice(_0: numpy.random.mtrand.RandomState, _1: list[Callable], /):
        'usage.skimage: 1'

    @classmethod
    def uniform(_0: numpy.random.mtrand.RandomState, _1: float, _2: Union[(float, int)], _0: numpy.random.mtrand.RandomState=..., _1: float=..., _2: Union[(float, int)]=..., /):
        'usage.skimage: 3'

    @classmethod
    def seed(_0: numpy.random.mtrand.RandomState, _1: int, /):
        'usage.skimage: 1'

    @classmethod
    def randn(_0: numpy.random.mtrand.RandomState, _1: int, /):
        'usage.skimage: 1'

    @classmethod
    def random_sample(_0: numpy.random.mtrand.RandomState, _1: tuple[(int, int)], /):
        'usage.skimage: 1'

    @classmethod
    def permutation(_0: numpy.random.mtrand.RandomState, _1: numpy.ndarray, /):
        'usage.skimage: 1'

    @classmethod
    def standard_normal(_0: numpy.random.mtrand.RandomState, _1: tuple[(int, ...)], _0: numpy.random.mtrand.RandomState=..., _1: tuple[(int, ...)]=..., /):
        'usage.skimage: 4'

    def random(self, _0, _0=..., /):
        'usage.skimage: 29'

    def rand(self, _0: int=..., _1: int=..., /):
        'usage.skimage: 90'

    def uniform(self, /, *, size: tuple[(int, int)]=..., low: float=..., high: float=...):
        'usage.skimage: 29'

    def randint(self, _0: int, _0: int=..., _1: int=..., /, *, size: Union[(tuple[(int, int, int)], tuple[(int, int)], int)]=..., dtype: list[numpy.uint8]=...):
        'usage.skimage: 15'

    def seed(self, /, *, seed: int=...):
        'usage.skimage: 25'

    def choice(self, _0: Union[(numpy.ndarray, list[bool], int)], _0: Union[(numpy.ndarray, list[bool], int)]=..., /, *, size: Union[(tuple[(int, int)], int)]=..., replace: bool=..., p: list[Union[(float, int)]]=...):
        'usage.skimage: 7'

    def normal(self, /, *, size: tuple[(int, ...)]=...):
        'usage.skimage: 32'

    def randn(self, _0: int, _0: int=..., _1: int=..., /):
        'usage.skimage: 44'

    def standard_normal(self, _0: tuple[(int, ...)], _0: tuple[(int, ...)]=..., /):
        'usage.skimage: 6'

    def gamma(self, _0: float, _1: numpy.float64, /):
        'usage.skimage: 2'

    def poisson(self, _0: numpy.ndarray, /):
        'usage.skimage: 2'
_rand = ...
