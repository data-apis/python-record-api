from typing import *


def isMaskedArray(x: Union[(numpy.ndarray, numpy.ma.core.MaskedArray)]):
    "usage.skimage: 18"


def array(
    data: numpy.ndarray, mask: Union[(numpy.ndarray, bool, List[List[int]])] = ...
):
    "usage.skimage: 7, usage.sklearn: 4, usage.dask: 2"


def getdata(a: Union[(numpy.ndarray, numpy.ma.core.MaskedArray)]):
    "usage.skimage: 3, usage.sklearn: 2, usage.dask: 9"


def getmaskarray(arr: Union[(numpy.ndarray, numpy.ma.core.MaskedArray)]):
    "usage.skimage: 1, usage.xarray: 2, usage.sklearn: 1, usage.dask: 9"


def masked_where(condition: Union[(numpy.ndarray, bool)], a: numpy.ndarray):
    "usage.xarray: 1, usage.dask: 3"


def masked_invalid(a: Union[(numpy.ndarray, List[float])]):
    "usage.xarray: 4, usage.sklearn: 4, usage.dask: 3"


def concatenate(
    arrays: Union[
        (
            List[Union[(numpy.ma.core.MaskedArray, numpy.ndarray)]],
            Tuple[(numpy.ma.core.MaskedArray, numpy.ma.core.MaskedArray)],
        )
    ],
    axis: int,
):
    "usage.xarray: 3, usage.dask: 38"


def getmask(a: numpy.ma.core.MaskedArray):
    "usage.sklearn: 1"


def masked_equal(x: numpy.ndarray, value: int):
    "usage.dask: 5"


def filled(a: Union[(numpy.ma.core.MaskedArray, numpy.float64, numpy.ndarray)] = ...):
    "usage.dask: 31"


def dot(
    a: numpy.ma.core.MaskedArray, b: Union[(numpy.ma.core.MaskedArray, numpy.ndarray)]
):
    "usage.dask: 3"


def masked_greater(
    x: Union[(numpy.ndarray, dask.array.core.Array)],
    value: Union[(numpy.ndarray, int, dask.array.core.Array, float)],
):
    "usage.dask: 23"


def masked_greater_equal(
    x: Union[(numpy.ndarray, dask.array.core.Array)], value: Union[(int, numpy.ndarray)]
):
    "usage.dask: 3"


def masked_less(
    x: Union[(numpy.ndarray, dask.array.core.Array)], value: Union[(int, numpy.ndarray)]
):
    "usage.dask: 3"


def masked_less_equal(
    x: Union[(numpy.ndarray, dask.array.core.Array)], value: Union[(int, numpy.ndarray)]
):
    "usage.dask: 3"


def masked_not_equal(
    x: Union[(numpy.ndarray, dask.array.core.Array)], value: Union[(int, numpy.ndarray)]
):
    "usage.dask: 3"


def masked_inside(x: numpy.ndarray, v1: int, v2: int):
    "usage.dask: 3"


def masked_outside(x: numpy.ndarray, v1: int, v2: int):
    "usage.dask: 3"


def masked_values(
    x: numpy.ndarray,
    value: int,
    rtol: float = ...,
    atol: float = ...,
    shrink: bool = ...,
):
    "usage.dask: 4"


def fix_invalid(a: Union[(numpy.ma.core.MaskedArray, numpy.ndarray)], fill_value: int):
    "usage.dask: 4"


def minimum_fill_value(obj: numpy.ma.core.MaskedArray):
    "usage.dask: 1"


def maximum_fill_value(obj: numpy.ma.core.MaskedArray):
    "usage.dask: 1"


def _check_fill_value(fill_value: Union[(float, int)], ndtype: numpy.dtype):
    "usage.dask: 2"


def set_fill_value(
    a: Union[(numpy.ndarray, numpy.ma.core.MaskedArray)],
    fill_value: Union[(int, numpy.ndarray)],
):
    "usage.dask: 3"


class MaskedArray:
    __module__ = ...
    ndim = ...
    shape = ...
    fill_value: Union[
        (numpy.float64, numpy.bool_, numpy.int64, numpy.complex128, numpy.float32)
    ] = ...
    mask = ...
    dtype = ...
    base = ...
    data = ...
    __class__ = ...
    __array_priority__ = ...

    def mean(self, /):
        "usage.skimage: 1, usage.sklearn: 1"

    def __sub__(self, _0: Union[(numpy.ma.core.MaskedArray, int, numpy.float64)], /):
        ""

    def __rsub__(self, _0: numpy.ma.core.MaskedArray, /):
        ""

    def __truediv__(self, _0: numpy.ma.core.MaskedArray, /):
        ""

    def __rtruediv__(self, _0: numpy.ma.core.MaskedArray, /):
        ""

    def __add__(self, _0: Union[(numpy.ma.core.MaskedArray, numpy.float64)], /):
        ""

    def __getitem__(
        self,
        _0: Union[
            (
                Tuple[
                    (
                        Union[
                            (
                                int,
                                ellipsis,
                                slice[(Union[(None, int)], Union[(None, int)], None)],
                                None,
                            )
                        ],
                        ...,
                    )
                ],
                int,
            )
        ],
        /,
    ):
        ""

    def __isub__(self, _0: numpy.float64, /):
        ""

    def reshape(self, /, *s: Literal[("v", "t")]):
        "usage.skimage: 1, usage.dask: 9"

    def __eq__(self, _0: int, /):
        ""

    def __setitem__(
        self,
        _0: Union[
            (
                numpy.ma.core.MaskedArray,
                int,
                Tuple[(Union[(int, numpy.bool_, numpy.ndarray)], ...)],
                slice[(None, None, None)],
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

    def __mul__(self, _0: Union[(int, numpy.ma.core.MaskedArray, numpy.float64)], /):
        ""

    def __radd__(
        self,
        _0: Union[
            (
                dask.array.core.Array,
                numpy.ma.core.MaskedArray,
                numpy.ndarray,
                numpy.float64,
            )
        ],
        /,
    ):
        ""

    def copy(self, /):
        "usage.dask: 1"

    def astype(self, _0: numpy.dtype, /):
        "usage.dask: 1"

    def sum(
        self,
        /,
        axis: Tuple[(int, ...)] = ...,
        dtype: Union[(Literal[("f8",)], numpy.dtype)] = ...,
        keepdims: bool = ...,
    ):
        "usage.dask: 27"

    def __pow__(self, _0: int, /):
        ""

    def __rmul__(self, _0: numpy.ma.core.MaskedArray, /):
        ""

    def __le__(self, _0: int, /):
        ""

    def cumsum(self, /, axis: int):
        "usage.dask: 1"

    def cumprod(self, /, axis: int):
        "usage.dask: 1"


class MaskError:
    def __init__(
        _0: Literal[("Mask and data not compatible: data shape is (10, 1",)], /
    ):
        "usage.dask: 1"
