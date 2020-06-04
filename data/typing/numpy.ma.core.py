def isMaskedArray(x: Union[(numpy.ndarray, numpy.ma.core.MaskedArray)]):
    "usage.skimage: 18"


def array(
    data: numpy.ndarray, mask: Union[(numpy.ndarray, bool, list[list[int]])] = ...
):
    "usage.skimage: 7, usage.sklearn: 4"


def getdata(a: Union[(numpy.ma.core.MaskedArray, numpy.ndarray)]):
    "usage.skimage: 3, usage.sklearn: 2"


def getmaskarray(arr: numpy.ma.core.MaskedArray):
    "usage.skimage: 1, usage.xarray: 1, usage.sklearn: 1"


def masked_where(condition: numpy.ndarray, a: numpy.ndarray):
    "usage.xarray: 1"


def masked_invalid(a: Union[(numpy.ndarray, list[float])]):
    "usage.xarray: 4, usage.sklearn: 4"


def concatenate(
    arrays: tuple[(numpy.ma.core.MaskedArray, numpy.ma.core.MaskedArray)], axis: int
):
    "usage.xarray: 3"


def getmask(a: numpy.ma.core.MaskedArray):
    "usage.sklearn: 1"


class MaskedArray:
    ndim = ...
    shape = ...
    fill_value = ...
    mask = ...
    dtype = ...
    base = ...
    data = ...

    def mean(self, /):
        "usage.skimage: 1, usage.sklearn: 1"

    def __getitem__(
        self,
        _0: Union[
            (
                tuple[(int, int)],
                int,
                tuple[(Union[(slice[(None, None, None)], int)], ...)],
            )
        ],
        /,
    ):
        ""

    def reshape(self, /, *s: Literal[("t", "v")]):
        "usage.skimage: 1"

    def __setitem__(
        self,
        _0: Union[
            (
                tuple[(Union[(numpy.ndarray, int, numpy.bool_)], int)],
                int,
                tuple[(int, int)],
                slice[(None, None, None)],
                tuple[(int, int, int)],
            )
        ],
        _1,
        /,
    ):
        ""

    def filled(self, /, fill_value: float):
        "usage.xarray: 2"
