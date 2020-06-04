def isMaskedArray(x: Union[(numpy.ma.core.MaskedArray, numpy.ndarray)]):
    "usage.skimage: 18"


def array(
    data: numpy.ndarray,
    mask: Union[(list[list[int]], bool, numpy.ndarray)],
    fill_value: Union[(numpy.float64, float)] = ...,
):
    "usage.skimage: 7"


def getdata(a: Union[(numpy.ma.core.MaskedArray, numpy.ndarray)]):
    "usage.skimage: 3"


def getmaskarray(arr: numpy.ma.core.MaskedArray):
    "usage.skimage: 1"


class MaskedArray:
    ndim = ...
    shape = ...
    fill_value = ...
    mask = ...

    def mean(self, /):
        "usage.skimage: 1"

    def reshape(self, /, *s: Literal[("v", "t")]):
        "usage.skimage: 1"
