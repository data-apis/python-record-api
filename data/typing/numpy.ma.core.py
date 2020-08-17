from typing import *

# usage.matplotlib: 2
MaskedArray: object


def _check_fill_value(fill_value: Union[float, int], ndtype: numpy.dtype):
    """
    usage.dask: 2
    """
    ...


def allclose(a: numpy.ma.core.MaskedArray, b: numpy.ma.core.MaskedArray):
    """
    usage.scipy: 1
    """
    ...


def array(
    data: Union[numpy.ndarray, numpy.ma.core.MaskedArray, list],
    dtype: Union[numpy.dtype, type] = ...,
    copy: Union[bool, numpy.bool_] = ...,
    subok: bool = ...,
    ndmin: int = ...,
    mask: Union[
        numpy.ndarray, numpy.bool_, bool, List[Union[int, bool, List[int]]]
    ] = ...,
):
    """
    usage.dask: 2
    usage.matplotlib: 45
    usage.pandas: 1
    usage.scipy: 92
    usage.skimage: 7
    usage.sklearn: 4
    usage.xarray: 1
    """
    ...


def asanyarray(
    a: Union[
        List[Union[float, int]],
        Tuple[float, float],
        numpy.float64,
        numpy.ma.core.MaskedArray,
        numpy.ndarray,
    ]
):
    """
    usage.scipy: 42
    """
    ...


def asarray(a: object):
    """
    usage.matplotlib: 48
    usage.scipy: 20
    """
    ...


def compressed(x: Union[list, numpy.ma.core.MaskedArray, numpy.ndarray]):
    """
    usage.scipy: 8
    """
    ...


def concatenate(
    arrays: Union[
        List[Union[numpy.ma.core.MaskedArray, numpy.ndarray]],
        Tuple[
            Union[numpy.ndarray, numpy.ma.core.MaskedArray],
            Union[numpy.ndarray, numpy.ma.core.MaskedArray],
        ],
    ],
    axis: int,
):
    """
    usage.dask: 36
    usage.matplotlib: 2
    usage.xarray: 3
    """
    ...


def dot(
    a: numpy.ma.core.MaskedArray, b: Union[numpy.ndarray, numpy.ma.core.MaskedArray]
):
    """
    usage.dask: 3
    usage.scipy: 1
    """
    ...


def filled(a: Union[numpy.ndarray, numpy.float64, numpy.ma.core.MaskedArray]):
    """
    usage.dask: 31
    usage.matplotlib: 23
    usage.scipy: 3
    """
    ...


def fix_invalid(
    a: Union[
        numpy.ndarray,
        numpy.ma.core.MaskedArray,
        List[Union[List[Union[int, float]], float, int]],
    ]
):
    """
    usage.dask: 4
    usage.scipy: 16
    """
    ...


def getdata(
    a: Union[numpy.ma.core.MaskedArray, numpy.ma.mrecords.MaskedRecords, numpy.ndarray]
):
    """
    usage.dask: 9
    usage.matplotlib: 20
    usage.pandas: 1
    usage.skimage: 3
    usage.sklearn: 2
    """
    ...


def getmask(a: object):
    """
    usage.matplotlib: 31
    usage.scipy: 33
    usage.sklearn: 1
    """
    ...


def getmaskarray(arr: Union[numpy.ma.core.MaskedArray, numpy.ndarray]):
    """
    usage.dask: 9
    usage.matplotlib: 8
    usage.pandas: 7
    usage.scipy: 5
    usage.skimage: 1
    usage.sklearn: 1
    usage.xarray: 2
    """
    ...


def isMaskedArray(x: object):
    """
    usage.scipy: 69
    usage.skimage: 18
    """
    ...


def is_masked(x: object):
    """
    usage.matplotlib: 32
    usage.scipy: 17
    """
    ...


def make_mask(m: numpy.ma.core.MaskedArray):
    """
    usage.scipy: 2
    """
    ...


def mask_or(
    m1: Union[numpy.ndarray, numpy.bool_],
    m2: Union[numpy.ndarray, numpy.bool_],
    copy: bool = ...,
    shrink: bool = ...,
):
    """
    usage.matplotlib: 2
    usage.scipy: 12
    """
    ...


def mask_rowcols(a: numpy.ma.core.MaskedArray, axis: int):
    """
    usage.scipy: 2
    """
    ...


def masked_equal(x: Union[numpy.ndarray, List[int]], value: int):
    """
    usage.dask: 5
    usage.matplotlib: 6
    usage.scipy: 4
    """
    ...


def masked_greater(
    x: Union[dask.array.core.Array, numpy.ndarray, numpy.ma.core.MaskedArray],
    value: Union[float, dask.array.core.Array, int, numpy.ndarray],
):
    """
    usage.dask: 23
    usage.matplotlib: 3
    usage.scipy: 6
    """
    ...


def masked_greater_equal(
    x: Union[dask.array.core.Array, numpy.ndarray, numpy.ma.core.MaskedArray],
    value: Union[numpy.ndarray, int],
):
    """
    usage.dask: 3
    usage.scipy: 2
    """
    ...


def masked_inside(x: numpy.ndarray, v1: int, v2: int):
    """
    usage.dask: 3
    """
    ...


def masked_invalid(a: object):
    """
    usage.dask: 3
    usage.matplotlib: 72
    usage.scipy: 25
    usage.sklearn: 4
    usage.xarray: 4
    """
    ...


def masked_less(
    x: Union[dask.array.core.Array, numpy.ndarray, numpy.ma.core.MaskedArray],
    value: Union[numpy.ndarray, int, float],
):
    """
    usage.dask: 3
    usage.scipy: 3
    """
    ...


def masked_less_equal(
    x: Union[dask.array.core.Array, numpy.ndarray, numpy.ma.core.MaskedArray],
    value: Union[numpy.ndarray, int],
):
    """
    usage.dask: 3
    usage.matplotlib: 7
    usage.scipy: 2
    """
    ...


def masked_not_equal(
    x: Union[numpy.ndarray, dask.array.core.Array], value: Union[int, numpy.ndarray]
):
    """
    usage.dask: 3
    """
    ...


def masked_outside(x: numpy.ndarray, v1: int, v2: int):
    """
    usage.dask: 3
    """
    ...


def masked_values(
    x: numpy.ndarray,
    value: int,
    rtol: float = ...,
    atol: float = ...,
    shrink: bool = ...,
):
    """
    usage.dask: 4
    usage.scipy: 1
    """
    ...


def masked_where(
    condition: Union[numpy.ndarray, bool, numpy.ma.core.MaskedArray],
    a: Union[numpy.ndarray, List[int]],
):
    """
    usage.dask: 3
    usage.matplotlib: 2
    usage.scipy: 12
    usage.xarray: 1
    """
    ...


def max(obj: numpy.ndarray):
    """
    usage.matplotlib: 2
    """
    ...


def maximum_fill_value(obj: numpy.ma.core.MaskedArray):
    """
    usage.dask: 1
    """
    ...


def min(obj: numpy.ndarray):
    """
    usage.matplotlib: 2
    """
    ...


def minimum_fill_value(obj: numpy.ma.core.MaskedArray):
    """
    usage.dask: 1
    """
    ...


def power(
    a: Union[numpy.float64, float, numpy.ma.core.MaskedArray],
    b: Union[numpy.ma.core.MaskedArray, numpy.ndarray, float],
):
    """
    usage.matplotlib: 4
    usage.scipy: 4
    """
    ...


def reshape(a: numpy.ndarray, new_shape: Tuple[int, int]):
    """
    usage.matplotlib: 1
    """
    ...


def set_fill_value(
    a: Union[numpy.ndarray, numpy.ma.core.MaskedArray],
    fill_value: Union[int, numpy.ndarray],
):
    """
    usage.dask: 3
    """
    ...


def sort(
    a: Union[List[int], numpy.ma.core.MaskedArray, numpy.ndarray],
    axis: Union[None, int],
):
    """
    usage.scipy: 4
    """
    ...


def where(
    condition: Union[
        numpy.ma.core.MaskedArray, numpy.ma.core.MaskedConstant, numpy.bool_
    ],
    x: Union[numpy.ma.core.MaskedArray, int, numpy.ndarray],
    y: Union[
        numpy.ma.core.MaskedArray, numpy.float64, float, numpy.ma.core.MaskedConstant
    ],
):
    """
    usage.scipy: 10
    """
    ...


class MaskError:
    def __init__(self, _0: str, /):
        """
        usage.dask: 1
        """
        ...


class MaskedArray:

    # usage.dask: 2
    __module__: ClassVar[object]

    # usage.matplotlib: 2
    # usage.scipy: 11
    T: object

    # usage.dask: 1
    __array_priority__: object

    # usage.dask: 1
    __class__: object

    # usage.scipy: 2
    _data: object

    # usage.scipy: 16
    _mask: Union[numpy.ndarray, numpy.bool_]

    # usage.xarray: 1
    base: object

    # usage.dask: 1
    # usage.matplotlib: 18
    # usage.scipy: 12
    # usage.sklearn: 2
    # usage.xarray: 3
    data: object

    # usage.dask: 17
    # usage.matplotlib: 69
    # usage.pandas: 42
    # usage.scipy: 2
    # usage.sklearn: 2
    # usage.xarray: 8
    dtype: object

    # usage.dask: 13
    # usage.skimage: 2
    fill_value: Union[
        numpy.float64, numpy.bool_, numpy.int64, numpy.complex128, numpy.float32
    ]

    # usage.dask: 4
    # usage.matplotlib: 38
    # usage.scipy: 15
    # usage.skimage: 5
    # usage.sklearn: 2
    # usage.xarray: 6
    mask: numpy.ndarray

    # usage.dask: 44
    # usage.matplotlib: 100
    # usage.pandas: 6
    # usage.scipy: 11
    # usage.skimage: 8
    # usage.xarray: 3
    ndim: object

    # usage.dask: 36
    # usage.matplotlib: 123
    # usage.scipy: 20
    # usage.skimage: 3
    # usage.sklearn: 1
    # usage.xarray: 6
    shape: Tuple[int, int]

    # usage.matplotlib: 50
    # usage.scipy: 14
    size: object

    def __add__(self, _0: object, /):
        """
        usage.dask: 1
        usage.matplotlib: 7
        usage.scipy: 16
        usage.skimage: 1
        """
        ...

    def __and__(self, _0: numpy.ma.core.MaskedArray, /):
        """
        usage.matplotlib: 1
        usage.scipy: 1
        """
        ...

    def __eq__(
        self, _0: Union[numpy.ma.core.MaskedArray, int, float, numpy.float64], /
    ):
        """
        usage.matplotlib: 8
        usage.scipy: 8
        usage.skimage: 1
        """
        ...

    def __ge__(
        self, _0: Union[numpy.float64, numpy.ndarray, int, numpy.ma.core.MaskedArray], /
    ):
        """
        usage.matplotlib: 3
        usage.scipy: 5
        """
        ...

    def __getitem__(self, _0: object, /):
        """
        usage.dask: 25
        usage.matplotlib: 101
        usage.scipy: 66
        usage.skimage: 6
        usage.sklearn: 21
        usage.xarray: 1
        """
        ...

    def __gt__(
        self, _0: Union[float, int, numpy.ma.core.MaskedConstant, numpy.float64], /
    ):
        """
        usage.matplotlib: 1
        usage.scipy: 9
        """
        ...

    def __iadd__(self, _0: Union[numpy.ma.core.MaskedArray, numpy.int32], /):
        """
        usage.matplotlib: 1
        usage.scipy: 1
        """
        ...

    def __imul__(self, _0: Union[numpy.ma.core.MaskedArray, int, numpy.ndarray], /):
        """
        usage.matplotlib: 2
        usage.scipy: 2
        usage.xarray: 1
        """
        ...

    def __invert__(self, /):
        """
        usage.matplotlib: 2
        usage.scipy: 1
        """
        ...

    def __ior__(self, _0: numpy.ma.core.MaskedArray, /):
        """
        usage.scipy: 2
        """
        ...

    def __ipow__(self, _0: int, /):
        """
        usage.scipy: 1
        """
        ...

    def __isub__(self, _0: Union[numpy.float64, numpy.ma.core.MaskedArray], /):
        """
        usage.matplotlib: 1
        usage.scipy: 2
        usage.skimage: 2
        """
        ...

    def __iter__(self, /):
        """
        usage.matplotlib: 17
        usage.scipy: 1
        """
        ...

    def __itruediv__(
        self,
        _0: Union[numpy.ma.core.MaskedArray, float, numpy.float64, numpy.ndarray],
        /,
    ):
        """
        usage.matplotlib: 3
        usage.scipy: 1
        """
        ...

    def __le__(self, _0: object, /):
        """
        usage.dask: 1
        usage.matplotlib: 1
        usage.scipy: 8
        usage.sklearn: 2
        """
        ...

    def __lt__(self, _0: numpy.float64, /):
        """
        usage.matplotlib: 1
        """
        ...

    def __mul__(self, _0: object, /):
        """
        usage.dask: 3
        usage.matplotlib: 16
        usage.scipy: 18
        usage.xarray: 1
        """
        ...

    def __neg__(self, /):
        """
        usage.matplotlib: 3
        usage.scipy: 1
        """
        ...

    def __or__(self, _0: Union[numpy.ma.core.MaskedArray, numpy.ndarray], /):
        """
        usage.matplotlib: 2
        """
        ...

    def __pow__(self, _0: Union[int, float], /):
        """
        usage.dask: 2
        usage.matplotlib: 1
        usage.scipy: 10
        """
        ...

    def __radd__(self, _0: object, /):
        """
        usage.dask: 3
        usage.matplotlib: 7
        usage.scipy: 8
        usage.xarray: 1
        """
        ...

    def __rand__(self, _0: Union[numpy.ndarray, numpy.ma.core.MaskedArray], /):
        """
        usage.matplotlib: 3
        usage.scipy: 2
        """
        ...

    def __rmul__(
        self,
        _0: Union[numpy.ma.core.MaskedArray, numpy.ndarray, float, numpy.float64, int],
        /,
    ):
        """
        usage.dask: 2
        usage.matplotlib: 10
        usage.scipy: 23
        """
        ...

    def __ror__(self, _0: Union[numpy.ma.core.MaskedArray, bool], /):
        """
        usage.matplotlib: 1
        usage.scipy: 3
        """
        ...

    def __rsub__(
        self, _0: Union[numpy.ma.core.MaskedArray, int, numpy.ndarray, numpy.float64], /
    ):
        """
        usage.dask: 4
        usage.matplotlib: 3
        usage.scipy: 13
        usage.skimage: 2
        usage.sklearn: 1
        """
        ...

    def __rtruediv__(self, _0: object, /):
        """
        usage.dask: 1
        usage.matplotlib: 1
        usage.scipy: 33
        usage.skimage: 1
        """
        ...

    def __setitem__(self, _0: object, _1: object, /):
        """
        usage.dask: 1
        usage.matplotlib: 19
        usage.pandas: 18
        usage.scipy: 41
        usage.skimage: 6
        usage.sklearn: 25
        usage.xarray: 5
        """
        ...

    def __sub__(self, _0: object, /):
        """
        usage.dask: 5
        usage.matplotlib: 7
        usage.scipy: 27
        usage.skimage: 4
        usage.sklearn: 1
        """
        ...

    def __truediv__(self, _0: object, /):
        """
        usage.dask: 1
        usage.matplotlib: 8
        usage.scipy: 36
        usage.skimage: 1
        """
        ...

    def all(self, /):
        """
        usage.matplotlib: 5
        """
        ...

    def any(self, /):
        """
        usage.scipy: 1
        """
        ...

    def argsort(self, /):
        """
        usage.scipy: 8
        """
        ...

    def astype(self, _0: Union[Literal["bool", "d"], type, numpy.dtype], /):
        """
        usage.dask: 10
        usage.matplotlib: 7
        usage.pandas: 2
        usage.scipy: 8
        """
        ...

    def byteswap(self, /):
        """
        usage.matplotlib: 3
        """
        ...

    def compressed(self, /):
        """
        usage.matplotlib: 6
        usage.scipy: 32
        """
        ...

    def copy(self, /):
        """
        usage.dask: 1
        """
        ...

    def count(self, /):
        """
        usage.scipy: 55
        """
        ...

    def cumprod(self, /, axis: int):
        """
        usage.dask: 1
        """
        ...

    def cumsum(self, /, axis: int):
        """
        usage.dask: 1
        """
        ...

    def dot(self, /, b: numpy.ndarray):
        """
        usage.matplotlib: 1
        """
        ...

    def fill(self, _0: int, /):
        """
        usage.matplotlib: 2
        """
        ...

    def filled(self, /):
        """
        usage.matplotlib: 17
        usage.scipy: 7
        usage.sklearn: 1
        usage.xarray: 2
        """
        ...

    def harden_mask(self, /):
        """
        usage.pandas: 2
        """
        ...

    def item(self, /):
        """
        usage.matplotlib: 2
        """
        ...

    def max(self, /):
        """
        usage.matplotlib: 32
        """
        ...

    def mean(self, /, axis: Union[None, int] = ..., keepdims: bool = ...):
        """
        usage.scipy: 32
        usage.skimage: 1
        usage.sklearn: 1
        """
        ...

    def min(self, /):
        """
        usage.matplotlib: 35
        usage.scipy: 4
        usage.sklearn: 2
        """
        ...

    def newbyteorder(self, /):
        """
        usage.matplotlib: 3
        """
        ...

    def ravel(self, /):
        """
        usage.matplotlib: 10
        usage.scipy: 14
        """
        ...

    def repeat(self, /, *args: Literal["v", "t"]):
        """
        usage.matplotlib: 3
        """
        ...

    def reshape(self, /, *s: Literal["v", "t"]):
        """
        usage.dask: 9
        usage.matplotlib: 9
        usage.scipy: 16
        usage.skimage: 1
        usage.sklearn: 2
        """
        ...

    def round(self, /, decimals: int):
        """
        usage.scipy: 1
        """
        ...

    def shrink_mask(self, /):
        """
        usage.matplotlib: 11
        """
        ...

    def soften_mask(self, /):
        """
        usage.pandas: 4
        """
        ...

    def std(self, /, axis: int = ..., ddof: int = ..., keepdims: bool = ...):
        """
        usage.scipy: 9
        """
        ...

    def sum(
        self,
        /,
        axis: Union[int, None, Tuple[int, ...]] = ...,
        dtype: Union[Literal["f8"], numpy.dtype] = ...,
        keepdims: bool = ...,
    ):
        """
        usage.dask: 27
        usage.scipy: 13
        usage.sklearn: 1
        """
        ...

    def unshare_mask(self, /):
        """
        usage.scipy: 4
        """
        ...

    def var(self, /, ddof: int):
        """
        usage.scipy: 11
        """
        ...

    def view(self, /):
        """
        usage.pandas: 4
        usage.scipy: 2
        """
        ...


class MaskedConstant:

    # usage.scipy: 1
    mask: object

    # usage.dask: 3
    ndim: object

    # usage.dask: 3
    # usage.scipy: 3
    shape: object

    def __add__(self, _0: Union[numpy.float64, numpy.ma.core.MaskedConstant], /):
        """
        usage.matplotlib: 8
        usage.scipy: 1
        """
        ...

    def __eq__(self, _0: int, /):
        """
        usage.scipy: 1
        """
        ...

    def __ge__(self, _0: numpy.ma.core.MaskedArray, /):
        """
        usage.scipy: 1
        """
        ...

    def __getitem__(self, _0: Tuple[None, ...], /):
        """
        usage.dask: 1
        """
        ...

    def __gt__(self, _0: numpy.int32, /):
        """
        usage.matplotlib: 1
        """
        ...

    def __le__(self, _0: numpy.int32, /):
        """
        usage.matplotlib: 1
        """
        ...

    def __lt__(self, _0: numpy.ma.core.MaskedArray, /):
        """
        usage.scipy: 2
        """
        ...

    def __mul__(self, _0: Union[numpy.float64, numpy.ma.core.MaskedConstant], /):
        """
        usage.matplotlib: 3
        usage.scipy: 4
        """
        ...

    def __neg__(self, /):
        """
        usage.scipy: 1
        """
        ...

    def __pow__(self, _0: float, /):
        """
        usage.scipy: 1
        """
        ...

    def __radd__(
        self,
        _0: Union[
            numpy.ma.core.MaskedConstant, numpy.float64, numpy.ma.core.MaskedArray
        ],
        /,
    ):
        """
        usage.matplotlib: 6
        usage.scipy: 3
        """
        ...

    def __rmul__(
        self, _0: Union[numpy.float64, numpy.ma.core.MaskedConstant, numpy.int64], /
    ):
        """
        usage.scipy: 5
        """
        ...

    def __rsub__(self, _0: numpy.ma.core.MaskedArray, /):
        """
        usage.scipy: 1
        """
        ...

    def __rtruediv__(
        self,
        _0: Union[
            numpy.ma.core.MaskedArray, numpy.ma.core.MaskedConstant, numpy.float64
        ],
        /,
    ):
        """
        usage.scipy: 8
        """
        ...

    def __sub__(self, _0: Union[numpy.float64, float], /):
        """
        usage.matplotlib: 1
        usage.scipy: 1
        """
        ...

    def __truediv__(
        self,
        _0: Union[numpy.ma.core.MaskedArray, numpy.ma.core.MaskedConstant, numpy.int64],
        /,
    ):
        """
        usage.scipy: 6
        """
        ...

    def astype(self, _0: Union[Literal["bool"], numpy.dtype], /):
        """
        usage.dask: 3
        """
        ...


class _MaskedBinaryOperation:
    def reduce(self, /, target: numpy.ma.core.MaskedArray):
        """
        usage.scipy: 1
        """
        ...


class _extrema_operation:
    def reduce(self, /, target: numpy.ma.core.MaskedArray):
        """
        usage.scipy: 8
        """
        ...
