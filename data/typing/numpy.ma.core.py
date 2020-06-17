from typing import *


def isMaskedArray(x: Union[(numpy.ndarray, numpy.ma.core.MaskedArray)]):
    "usage.skimage: 18"


def array(
    data: numpy.ndarray, mask: Union[(numpy.ndarray, bool, List[List[int]])] = ...
):
    "usage.skimage: 7, usage.sklearn: 4"


def getdata(a: Union[(numpy.ma.core.MaskedArray, numpy.ndarray)]):
    "usage.skimage: 3, usage.sklearn: 2"


def getmaskarray(arr: numpy.ma.core.MaskedArray):
    "usage.skimage: 1, usage.xarray: 2, usage.sklearn: 1"


def masked_where(condition: numpy.ndarray, a: numpy.ndarray):
    "usage.xarray: 1"


def masked_invalid(a: Union[(numpy.ndarray, List[float])]):
    "usage.xarray: 4, usage.sklearn: 4"


def concatenate(
    arrays: Tuple[(numpy.ma.core.MaskedArray, numpy.ma.core.MaskedArray)], axis: int
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

    def __sub__(self, _0: Union[(numpy.ma.core.MaskedArray, numpy.float64)], /):
        ""

    def __rsub__(self, _0: numpy.ma.core.MaskedArray, /):
        ""

    def __truediv__(self, _0: numpy.ma.core.MaskedArray, /):
        ""

    def __rtruediv__(self, _0: numpy.ma.core.MaskedArray, /):
        ""

    def __add__(self, _0: numpy.float64, /):
        ""

    def __getitem__(
        self, _0: Union[(Tuple[(Union[(slice[(None, None, None)], int)], ...)], int)], /
    ):
        ""

    def __isub__(self, _0: numpy.float64, /):
        ""

    def reshape(self, /, *s: Literal[("v", "t")]):
        "usage.skimage: 1"

    def __eq__(self, _0: int, /):
        ""

    def __setitem__(
        self,
        _0: Union[
            (
                int,
                slice[(None, None, None)],
                Tuple[(Union[(numpy.ndarray, numpy.bool_, int)], ...)],
            )
        ],
        _1,
        /,
    ):
        ""

    def filled(self, /, fill_value: float):
        "usage.xarray: 2"

    def __imul__(self, _0: int, /):
        ""

    def __mul__(self, _0: numpy.float64, /):
        ""

    def __radd__(self, _0: numpy.float64, /):
        ""
