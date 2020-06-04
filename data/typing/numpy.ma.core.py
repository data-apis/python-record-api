def isMaskedArray(x: Union[(numpy.ma.core.MaskedArray, numpy.ndarray)]):
    "usage.skimage: 18"


def array(
    data: numpy.ndarray, mask: Union[(bool, numpy.ndarray, list[list[int]])] = ...
):
    "usage.skimage: 7"


def getdata(a: Union[(numpy.ma.core.MaskedArray, numpy.ndarray)]):
    "usage.skimage: 3"


def getmaskarray(arr: numpy.ma.core.MaskedArray):
    "usage.skimage: 1\nusage.xarray: 1"


def masked_where(condition: numpy.ndarray, a: numpy.ndarray):
    "usage.xarray: 1"


def masked_invalid(a: list[float]):
    "usage.xarray: 4"


def concatenate(
    arrays: tuple[(numpy.ma.core.MaskedArray, numpy.ma.core.MaskedArray)], axis: int
):
    "usage.xarray: 3"


class MaskedArray:
    ndim = ...
    shape = ...
    fill_value = ...
    mask = ...
    dtype = ...
    base = ...
    data = ...

    def mean(self, /):
        "usage.skimage: 1"

    def __getitem__(self, _0: tuple[(Union[(int, slice[(None, None, None)])], ...)], /):
        ""

    def reshape(self, /, *s: Literal[("v", "t")]):
        "usage.skimage: 1"

    def __setitem__(
        self,
        _0: Union[
            (
                tuple[(int, int, int)],
                slice[(None, None, None)],
                tuple[(Union[(int, numpy.bool_, numpy.ndarray)], int)],
                tuple[(int, int)],
            )
        ],
        _1: Union[(int, float, numpy.ma.core.MaskedConstant)],
        /,
    ):
        ""

    def filled(self, /, fill_value: float):
        "usage.xarray: 2"
