from typing import *


def isMaskedArray(x: Union[numpy.ndarray, numpy.ma.core.MaskedArray]):
    "\n    usage.skimage: 18\n    "
    ...


def array(data: numpy.ndarray, mask: Union[numpy.ndarray, bool, List[List[int]]]):
    "\n    usage.skimage: 7\n    usage.sklearn: 4\n    usage.dask: 2\n    "
    ...


def getdata(a: Union[numpy.ndarray, numpy.ma.core.MaskedArray]):
    "\n    usage.skimage: 3\n    usage.sklearn: 2\n    usage.dask: 9\n    "
    ...


def getmaskarray(arr: Union[numpy.ndarray, numpy.ma.core.MaskedArray]):
    "\n    usage.skimage: 1\n    usage.xarray: 2\n    usage.sklearn: 1\n    usage.dask: 9\n    "
    ...


def masked_where(condition: Union[numpy.ndarray, bool], a: numpy.ndarray):
    "\n    usage.xarray: 1\n    usage.dask: 3\n    "
    ...


def masked_invalid(a: Union[numpy.ndarray, List[float]]):
    "\n    usage.xarray: 4\n    usage.sklearn: 4\n    usage.dask: 3\n    "
    ...


def concatenate(
    arrays: Union[
        List[Union[numpy.ma.core.MaskedArray, numpy.ndarray]],
        Tuple[numpy.ma.core.MaskedArray, numpy.ma.core.MaskedArray],
    ],
    axis: int,
):
    "\n    usage.xarray: 3\n    usage.dask: 38\n    "
    ...


def getmask(a: numpy.ma.core.MaskedArray):
    "\n    usage.sklearn: 1\n    "
    ...


def masked_equal(x: numpy.ndarray, value: int):
    "\n    usage.dask: 5\n    "
    ...


def filled(a: Union[numpy.ma.core.MaskedArray, numpy.float64, numpy.ndarray]):
    "\n    usage.dask: 31\n    "
    ...


def dot(
    a: numpy.ma.core.MaskedArray, b: Union[numpy.ma.core.MaskedArray, numpy.ndarray]
):
    "\n    usage.dask: 3\n    "
    ...


def masked_greater(
    x: Union[numpy.ndarray, dask.array.core.Array],
    value: Union[numpy.ndarray, int, dask.array.core.Array, float],
):
    "\n    usage.dask: 23\n    "
    ...


def masked_greater_equal(
    x: Union[numpy.ndarray, dask.array.core.Array], value: Union[int, numpy.ndarray]
):
    "\n    usage.dask: 3\n    "
    ...


def masked_less(
    x: Union[numpy.ndarray, dask.array.core.Array], value: Union[int, numpy.ndarray]
):
    "\n    usage.dask: 3\n    "
    ...


def masked_less_equal(
    x: Union[numpy.ndarray, dask.array.core.Array], value: Union[int, numpy.ndarray]
):
    "\n    usage.dask: 3\n    "
    ...


def masked_not_equal(
    x: Union[numpy.ndarray, dask.array.core.Array], value: Union[int, numpy.ndarray]
):
    "\n    usage.dask: 3\n    "
    ...


def masked_inside(x: numpy.ndarray, v1: int, v2: int):
    "\n    usage.dask: 3\n    "
    ...


def masked_outside(x: numpy.ndarray, v1: int, v2: int):
    "\n    usage.dask: 3\n    "
    ...


def masked_values(
    x: numpy.ndarray,
    value: int,
    rtol: float = ...,
    atol: float = ...,
    shrink: bool = ...,
):
    "\n    usage.dask: 4\n    "
    ...


def fix_invalid(a: Union[numpy.ma.core.MaskedArray, numpy.ndarray], fill_value: int):
    "\n    usage.dask: 4\n    "
    ...


def minimum_fill_value(obj: numpy.ma.core.MaskedArray):
    "\n    usage.dask: 1\n    "
    ...


def maximum_fill_value(obj: numpy.ma.core.MaskedArray):
    "\n    usage.dask: 1\n    "
    ...


def _check_fill_value(fill_value: Union[float, int], ndtype: numpy.dtype):
    "\n    usage.dask: 2\n    "
    ...


def set_fill_value(
    a: Union[numpy.ndarray, numpy.ma.core.MaskedArray],
    fill_value: Union[int, numpy.ndarray],
):
    "\n    usage.dask: 3\n    "
    ...


class MaskedArray:

    # usage.dask: 2
    __module__: ClassVar[object]

    # usage.skimage: 8
    # usage.xarray: 3
    # usage.dask: 44
    ndim: object

    # usage.skimage: 3
    # usage.xarray: 6
    # usage.dask: 35
    shape: object

    # usage.skimage: 2
    # usage.dask: 13
    fill_value: Union[
        numpy.float64, numpy.bool_, numpy.int64, numpy.complex128, numpy.float32
    ]

    # usage.skimage: 5
    # usage.xarray: 6
    # usage.dask: 4
    mask: object

    # usage.xarray: 8
    # usage.dask: 17
    dtype: object

    # usage.xarray: 1
    base: object

    # usage.xarray: 3
    # usage.sklearn: 1
    # usage.dask: 1
    data: object

    # usage.dask: 1
    __class__: object

    # usage.dask: 1
    __array_priority__: object

    def mean(self: object, /):
        "\n    usage.skimage: 1\n    usage.sklearn: 1\n    "
        ...

    def __sub__(
        self: object, _0: Union[numpy.ma.core.MaskedArray, int, numpy.float64], /
    ):
        "\n    usage.skimage: 4\n    usage.sklearn: 1\n    usage.dask: 5\n    "
        ...

    def __rsub__(self: object, _0: numpy.ma.core.MaskedArray, /):
        "\n    usage.skimage: 2\n    usage.sklearn: 1\n    usage.dask: 4\n    "
        ...

    def __truediv__(self: object, _0: numpy.ma.core.MaskedArray, /):
        "\n    usage.skimage: 1\n    usage.dask: 1\n    "
        ...

    def __rtruediv__(self: object, _0: numpy.ma.core.MaskedArray, /):
        "\n    usage.skimage: 1\n    usage.dask: 1\n    "
        ...

    def __add__(self: object, _0: Union[numpy.ma.core.MaskedArray, numpy.float64], /):
        "\n    usage.skimage: 1\n    usage.dask: 1\n    "
        ...

    def __getitem__(
        self: object,
        _0: Union[
            Tuple[
                Union[
                    int,
                    ellipsis,
                    slice[Union[None, int], Union[None, int], Union[None, int]],
                    None,
                ],
                ...,
            ],
            int,
        ],
        /,
    ):
        "\n    usage.skimage: 6\n    usage.xarray: 1\n    usage.sklearn: 8\n    usage.dask: 22\n    "
        ...

    def __isub__(self: object, _0: numpy.float64, /):
        "\n    usage.skimage: 2\n    "
        ...

    def reshape(self: object, /, *s: Literal["v", "t"]):
        "\n    usage.skimage: 1\n    usage.dask: 9\n    "
        ...

    def __eq__(self: object, _0: int, /):
        "\n    usage.skimage: 1\n    "
        ...

    def __setitem__(
        self: object,
        _0: Union[
            numpy.ma.core.MaskedArray,
            int,
            Tuple[Union[int, numpy.bool_, numpy.ndarray], ...],
            slice[None, None, None],
        ],
        _1: object,
        /,
    ):
        "\n    usage.skimage: 6\n    usage.xarray: 5\n    usage.sklearn: 17\n    usage.dask: 1\n    "
        ...

    def filled(self: object, /, fill_value: float):
        "\n    usage.xarray: 2\n    "
        ...

    def __imul__(self: object, _0: int, /):
        "\n    usage.xarray: 1\n    "
        ...

    def __mul__(
        self: object, _0: Union[int, numpy.ma.core.MaskedArray, numpy.float64], /
    ):
        "\n    usage.xarray: 1\n    usage.dask: 3\n    "
        ...

    def __radd__(
        self: object,
        _0: Union[
            dask.array.core.Array,
            numpy.ma.core.MaskedArray,
            numpy.ndarray,
            numpy.float64,
        ],
        /,
    ):
        "\n    usage.xarray: 1\n    usage.dask: 3\n    "
        ...

    def copy(self: object, /):
        "\n    usage.dask: 1\n    "
        ...

    def astype(self: object, _0: numpy.dtype, /):
        "\n    usage.dask: 1\n    "
        ...

    def sum(
        self: object,
        /,
        axis: Tuple[int, ...] = ...,
        dtype: Union[Literal["f8"], numpy.dtype] = ...,
        keepdims: bool = ...,
    ):
        "\n    usage.dask: 27\n    "
        ...

    def __pow__(self: object, _0: int, /):
        "\n    usage.dask: 2\n    "
        ...

    def __rmul__(self: object, _0: numpy.ma.core.MaskedArray, /):
        "\n    usage.dask: 2\n    "
        ...

    def __le__(self: object, _0: int, /):
        "\n    usage.dask: 1\n    "
        ...

    def cumsum(self: object, /, axis: int):
        "\n    usage.dask: 1\n    "
        ...

    def cumprod(self: object, /, axis: int):
        "\n    usage.dask: 1\n    "
        ...


class MaskError:
    def __init__(_0: Literal["Mask and data not compatible: data shape is (10, 1"], /):
        "\n    usage.dask: 1\n    "
        ...
