from typing import *


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


@overload
def array(
    data: numpy.ndarray,
    mask: Union[numpy.ndarray, bool, List[List[int]]],
    fill_value: Union[numpy.float64, float] = ...,
):
    """
    usage.skimage: 7
    """
    ...


@overload
def array(data: List[Union[float, int]], mask: List[bool]):
    """
    usage.xarray: 1
    """
    ...


@overload
def array(data: numpy.ma.core.MaskedArray, mask: List[bool]):
    """
    usage.pandas: 1
    """
    ...


@overload
def array(
    data: Union[
        List[Union[List[int], int, numpy.float64, float]],
        numpy.ndarray,
        numpy.ma.core.MaskedArray,
    ],
    dtype: Type[numpy.float64] = ...,
    copy: Union[bool, numpy.bool_] = ...,
    subok: bool = ...,
    ndmin: int = ...,
    mask: Union[
        List[Union[List[int], bool, int]], numpy.bool_, bool, numpy.ndarray
    ] = ...,
):
    """
    usage.scipy: 92
    """
    ...


@overload
def array(
    data: Union[
        List[Union[Literal["b", "k"], int, float, None, List[int]]],
        numpy.ndarray,
        numpy.ma.core.MaskedArray,
    ],
    dtype: Union[Type[float], numpy.dtype] = ...,
    copy: bool = ...,
    mask: Union[List[Union[bool, int]], numpy.ndarray, numpy.bool_] = ...,
):
    """
    usage.matplotlib: 45
    """
    ...


@overload
def array(data: numpy.ndarray, mask: numpy.ndarray):
    """
    usage.dask: 2
    usage.sklearn: 4
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


@overload
def asarray(a: Union[List[int], numpy.ma.core.MaskedArray, numpy.ndarray]):
    """
    usage.scipy: 20
    """
    ...


@overload
def asarray(a: object, dtype: type = ...):
    """
    usage.matplotlib: 48
    """
    ...


def asarray(a: object, dtype: type = ...):
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


@overload
def concatenate(
    arrays: Tuple[numpy.ma.core.MaskedArray, numpy.ma.core.MaskedArray], axis: int
):
    """
    usage.xarray: 3
    """
    ...


@overload
def concatenate(
    arrays: Tuple[
        Union[numpy.ndarray, numpy.ma.core.MaskedArray],
        Union[numpy.ma.core.MaskedArray, numpy.ndarray],
    ],
    axis: int,
):
    """
    usage.matplotlib: 2
    """
    ...


@overload
def concatenate(
    arrays: List[Union[numpy.ndarray, numpy.ma.core.MaskedArray]], axis: int
):
    """
    usage.dask: 36
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


@overload
def dot(a: numpy.ma.core.MaskedArray, b: numpy.ma.core.MaskedArray):
    """
    usage.scipy: 1
    """
    ...


@overload
def dot(
    a: numpy.ma.core.MaskedArray, b: Union[numpy.ma.core.MaskedArray, numpy.ndarray]
):
    """
    usage.dask: 3
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


@overload
def filled(
    a: Union[numpy.float64, numpy.ma.core.MaskedArray, numpy.ndarray], fill_value: int
):
    """
    usage.scipy: 3
    """
    ...


@overload
def filled(
    a: Union[numpy.ma.core.MaskedArray, numpy.ndarray],
    fill_value: Union[bool, float] = ...,
):
    """
    usage.matplotlib: 23
    """
    ...


@overload
def filled(
    a: Union[numpy.ma.core.MaskedArray, numpy.float64, numpy.ndarray],
    fill_value: Union[float, int, None] = ...,
):
    """
    usage.dask: 31
    """
    ...


def filled(
    a: Union[numpy.ndarray, numpy.float64, numpy.ma.core.MaskedArray],
    fill_value: Union[None, int, float, bool] = ...,
):
    """
    usage.dask: 31
    usage.matplotlib: 23
    usage.scipy: 3
    """
    ...


@overload
def fix_invalid(
    a: Union[
        numpy.ma.core.MaskedArray,
        numpy.ndarray,
        List[Union[int, float, List[Union[float, int]]]],
    ],
    copy: bool = ...,
):
    """
    usage.scipy: 16
    """
    ...


@overload
def fix_invalid(a: Union[numpy.ma.core.MaskedArray, numpy.ndarray], fill_value: int):
    """
    usage.dask: 4
    """
    ...


def fix_invalid(
    a: Union[
        numpy.ndarray,
        numpy.ma.core.MaskedArray,
        List[Union[List[Union[int, float]], float, int]],
    ],
    copy: bool = ...,
    fill_value: int = ...,
):
    """
    usage.dask: 4
    usage.scipy: 16
    """
    ...


@overload
def getdata(a: Union[numpy.ndarray, numpy.ma.core.MaskedArray]):
    """
    usage.matplotlib: 20
    usage.skimage: 3
    """
    ...


@overload
def getdata(a: numpy.ma.mrecords.MaskedRecords):
    """
    usage.pandas: 1
    """
    ...


@overload
def getdata(a: Union[numpy.ma.core.MaskedArray, numpy.ndarray]):
    """
    usage.dask: 9
    """
    ...


@overload
def getdata(a: numpy.ma.core.MaskedArray):
    """
    usage.sklearn: 2
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


@overload
def getmask(a: Union[numpy.ma.core.MaskedArray, numpy.ndarray]):
    """
    usage.scipy: 33
    """
    ...


@overload
def getmask(a: object):
    """
    usage.matplotlib: 31
    """
    ...


@overload
def getmask(a: numpy.ma.core.MaskedArray):
    """
    usage.sklearn: 1
    """
    ...


def getmask(a: object):
    """
    usage.matplotlib: 31
    usage.scipy: 33
    usage.sklearn: 1
    """
    ...


@overload
def getmaskarray(arr: numpy.ma.core.MaskedArray):
    """
    usage.matplotlib: 8
    usage.pandas: 7
    usage.skimage: 1
    usage.sklearn: 1
    usage.xarray: 2
    """
    ...


@overload
def getmaskarray(arr: Union[numpy.ma.core.MaskedArray, numpy.ndarray]):
    """
    usage.dask: 9
    usage.scipy: 5
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


@overload
def isMaskedArray(x: Union[numpy.ndarray, numpy.ma.core.MaskedArray]):
    """
    usage.skimage: 18
    """
    ...


@overload
def isMaskedArray(x: object):
    """
    usage.scipy: 69
    """
    ...


def isMaskedArray(x: object):
    """
    usage.scipy: 69
    usage.skimage: 18
    """
    ...


@overload
def is_masked(
    x: Union[
        List[Union[numpy.float64, int, float]], numpy.ma.core.MaskedArray, numpy.ndarray
    ]
):
    """
    usage.scipy: 17
    """
    ...


@overload
def is_masked(x: object):
    """
    usage.matplotlib: 32
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


@overload
def mask_or(
    m1: Union[numpy.ndarray, numpy.bool_],
    m2: Union[numpy.ndarray, numpy.bool_],
    shrink: bool = ...,
):
    """
    usage.scipy: 12
    """
    ...


@overload
def mask_or(
    m1: Union[numpy.bool_, numpy.ndarray],
    m2: Union[numpy.bool_, numpy.ndarray],
    copy: bool,
    shrink: bool,
):
    """
    usage.matplotlib: 2
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


@overload
def masked_equal(x: numpy.ndarray, value: int):
    """
    usage.dask: 5
    usage.scipy: 4
    """
    ...


@overload
def masked_equal(x: List[int], value: int):
    """
    usage.matplotlib: 6
    """
    ...


def masked_equal(x: Union[numpy.ndarray, List[int]], value: int):
    """
    usage.dask: 5
    usage.matplotlib: 6
    usage.scipy: 4
    """
    ...


@overload
def masked_greater(
    x: Union[numpy.ma.core.MaskedArray, numpy.ndarray], value: Union[int, float]
):
    """
    usage.scipy: 6
    """
    ...


@overload
def masked_greater(x: numpy.ndarray, value: Union[int, float]):
    """
    usage.matplotlib: 3
    """
    ...


@overload
def masked_greater(
    x: Union[numpy.ndarray, dask.array.core.Array],
    value: Union[numpy.ndarray, int, dask.array.core.Array, float],
):
    """
    usage.dask: 23
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


@overload
def masked_greater_equal(x: numpy.ma.core.MaskedArray, value: int):
    """
    usage.scipy: 2
    """
    ...


@overload
def masked_greater_equal(
    x: Union[numpy.ndarray, dask.array.core.Array], value: Union[int, numpy.ndarray]
):
    """
    usage.dask: 3
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


@overload
def masked_invalid(a: List[float]):
    """
    usage.xarray: 4
    """
    ...


@overload
def masked_invalid(a: Union[numpy.ndarray, numpy.ma.core.MaskedArray]):
    """
    usage.scipy: 25
    """
    ...


@overload
def masked_invalid(a: object, copy: bool = ...):
    """
    usage.matplotlib: 72
    """
    ...


@overload
def masked_invalid(a: numpy.ndarray):
    """
    usage.dask: 3
    usage.sklearn: 4
    """
    ...


def masked_invalid(a: object, copy: bool = ...):
    """
    usage.dask: 3
    usage.matplotlib: 72
    usage.scipy: 25
    usage.sklearn: 4
    usage.xarray: 4
    """
    ...


@overload
def masked_less(x: numpy.ma.core.MaskedArray, value: Union[int, float]):
    """
    usage.scipy: 3
    """
    ...


@overload
def masked_less(
    x: Union[numpy.ndarray, dask.array.core.Array], value: Union[int, numpy.ndarray]
):
    """
    usage.dask: 3
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


@overload
def masked_less_equal(x: numpy.ma.core.MaskedArray, value: int):
    """
    usage.scipy: 2
    """
    ...


@overload
def masked_less_equal(
    x: Union[numpy.ma.core.MaskedArray, numpy.ndarray], value: int, copy: bool
):
    """
    usage.matplotlib: 7
    """
    ...


@overload
def masked_less_equal(
    x: Union[numpy.ndarray, dask.array.core.Array], value: Union[int, numpy.ndarray]
):
    """
    usage.dask: 3
    """
    ...


def masked_less_equal(
    x: Union[dask.array.core.Array, numpy.ndarray, numpy.ma.core.MaskedArray],
    value: Union[numpy.ndarray, int],
    copy: bool = ...,
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


@overload
def masked_values(x: numpy.ndarray, value: int):
    """
    usage.scipy: 1
    """
    ...


@overload
def masked_values(
    x: numpy.ndarray,
    value: int,
    rtol: float = ...,
    atol: float = ...,
    shrink: bool = ...,
):
    """
    usage.dask: 4
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


@overload
def masked_where(condition: numpy.ndarray, a: numpy.ndarray):
    """
    usage.matplotlib: 2
    usage.xarray: 1
    """
    ...


@overload
def masked_where(
    condition: Union[numpy.ma.core.MaskedArray, numpy.ndarray],
    a: Union[numpy.ndarray, List[int]],
    copy: bool = ...,
):
    """
    usage.scipy: 12
    """
    ...


@overload
def masked_where(condition: Union[bool, numpy.ndarray], a: numpy.ndarray):
    """
    usage.dask: 3
    """
    ...


def masked_where(
    condition: Union[numpy.ndarray, bool, numpy.ma.core.MaskedArray],
    a: Union[numpy.ndarray, List[int]],
    copy: bool = ...,
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


@overload
def power(a: Union[numpy.ma.core.MaskedArray, numpy.float64], b: float):
    """
    usage.scipy: 4
    """
    ...


@overload
def power(
    a: Union[numpy.ma.core.MaskedArray, float, numpy.float64],
    b: Union[float, numpy.ndarray, numpy.ma.core.MaskedArray],
):
    """
    usage.matplotlib: 4
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
    pass


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

    @overload
    def __add__(self, _0: numpy.float64, /):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __add__(self, _0: object, /):
        """
        usage.scipy: 16
        """
        ...

    @overload
    def __add__(self, _0: Union[numpy.ma.core.MaskedArray, float, numpy.float64], /):
        """
        usage.matplotlib: 7
        """
        ...

    @overload
    def __add__(self, _0: numpy.ma.core.MaskedArray, /):
        """
        usage.dask: 1
        """
        ...

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

    @overload
    def __eq__(self, _0: int, /):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __eq__(self, _0: Union[float, numpy.float64, int], /):
        """
        usage.scipy: 8
        """
        ...

    @overload
    def __eq__(self, _0: Union[int, numpy.ma.core.MaskedArray], /):
        """
        usage.matplotlib: 8
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

    @overload
    def __ge__(self, _0: Union[numpy.ma.core.MaskedArray, int], /):
        """
        usage.scipy: 5
        """
        ...

    @overload
    def __ge__(self, _0: Union[int, numpy.ndarray, numpy.float64], /):
        """
        usage.matplotlib: 3
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

    @overload
    def __getitem__(self, _0: Tuple[Union[slice[None, None, None], int], ...], /):
        """
        usage.skimage: 6
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, int], /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def __getitem__(self, _0: object, /):
        """
        usage.matplotlib: 101
        usage.scipy: 66
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            Union[
                slice[Union[int, None], Union[int, None], Union[int, None]],
                None,
                ellipsis,
                int,
            ],
            ...,
        ],
        /,
    ):
        """
        usage.dask: 25
        """
        ...

    @overload
    def __getitem__(self, _0: int, /):
        """
        usage.sklearn: 21
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

    @overload
    def __gt__(
        self, _0: Union[float, numpy.float64, numpy.ma.core.MaskedConstant, int], /
    ):
        """
        usage.scipy: 9
        """
        ...

    @overload
    def __gt__(self, _0: float, /):
        """
        usage.matplotlib: 1
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

    @overload
    def __iadd__(self, _0: numpy.int32, /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def __iadd__(self, _0: numpy.ma.core.MaskedArray, /):
        """
        usage.matplotlib: 1
        """
        ...

    def __iadd__(self, _0: Union[numpy.ma.core.MaskedArray, numpy.int32], /):
        """
        usage.matplotlib: 1
        usage.scipy: 1
        """
        ...

    @overload
    def __imul__(self, _0: int, /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def __imul__(self, _0: Union[numpy.ndarray, numpy.ma.core.MaskedArray], /):
        """
        usage.scipy: 2
        """
        ...

    @overload
    def __imul__(self, _0: Union[int, numpy.ma.core.MaskedArray], /):
        """
        usage.matplotlib: 2
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

    @overload
    def __isub__(self, _0: numpy.float64, /):
        """
        usage.matplotlib: 1
        usage.skimage: 2
        """
        ...

    @overload
    def __isub__(self, _0: numpy.ma.core.MaskedArray, /):
        """
        usage.scipy: 2
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

    @overload
    def __itruediv__(self, _0: numpy.ndarray, /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def __itruediv__(
        self, _0: Union[numpy.float64, float, numpy.ma.core.MaskedArray], /
    ):
        """
        usage.matplotlib: 3
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

    @overload
    def __le__(self, _0: object, /):
        """
        usage.scipy: 8
        """
        ...

    @overload
    def __le__(self, _0: float, /):
        """
        usage.matplotlib: 1
        """
        ...

    @overload
    def __le__(self, _0: int, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __le__(self, _0: numpy.ndarray, /):
        """
        usage.sklearn: 2
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

    @overload
    def __mul__(self, _0: numpy.float64, /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def __mul__(
        self,
        _0: Union[
            numpy.float64, numpy.ma.core.MaskedArray, numpy.float32, numpy.ndarray
        ],
        /,
    ):
        """
        usage.scipy: 18
        """
        ...

    @overload
    def __mul__(
        self,
        _0: Union[int, numpy.ma.core.MaskedArray, numpy.float64, float, numpy.ndarray],
        /,
    ):
        """
        usage.matplotlib: 16
        """
        ...

    @overload
    def __mul__(self, _0: Union[numpy.ma.core.MaskedArray, int], /):
        """
        usage.dask: 3
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

    @overload
    def __pow__(self, _0: Union[float, int], /):
        """
        usage.scipy: 10
        """
        ...

    @overload
    def __pow__(self, _0: int, /):
        """
        usage.dask: 2
        usage.matplotlib: 1
        """
        ...

    def __pow__(self, _0: Union[int, float], /):
        """
        usage.dask: 2
        usage.matplotlib: 1
        usage.scipy: 10
        """
        ...

    @overload
    def __radd__(self, _0: numpy.float64, /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def __radd__(self, _0: Union[numpy.ma.core.MaskedArray, int], /):
        """
        usage.scipy: 8
        """
        ...

    @overload
    def __radd__(
        self, _0: Union[float, int, numpy.float64, numpy.ma.core.MaskedArray], /
    ):
        """
        usage.matplotlib: 7
        """
        ...

    @overload
    def __radd__(
        self,
        _0: Union[numpy.ndarray, numpy.ma.core.MaskedArray, dask.array.core.Array],
        /,
    ):
        """
        usage.dask: 3
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

    @overload
    def __rand__(self, _0: Union[numpy.ndarray, numpy.ma.core.MaskedArray], /):
        """
        usage.scipy: 2
        """
        ...

    @overload
    def __rand__(self, _0: Union[numpy.ma.core.MaskedArray, numpy.ndarray], /):
        """
        usage.matplotlib: 3
        """
        ...

    def __rand__(self, _0: Union[numpy.ndarray, numpy.ma.core.MaskedArray], /):
        """
        usage.matplotlib: 3
        usage.scipy: 2
        """
        ...

    @overload
    def __rmul__(self, _0: Union[numpy.ndarray, numpy.ma.core.MaskedArray, float], /):
        """
        usage.scipy: 23
        """
        ...

    @overload
    def __rmul__(
        self,
        _0: Union[numpy.ndarray, numpy.ma.core.MaskedArray, float, numpy.float64, int],
        /,
    ):
        """
        usage.matplotlib: 10
        """
        ...

    @overload
    def __rmul__(self, _0: numpy.ma.core.MaskedArray, /):
        """
        usage.dask: 2
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

    @overload
    def __ror__(self, _0: bool, /):
        """
        usage.scipy: 3
        """
        ...

    @overload
    def __ror__(self, _0: numpy.ma.core.MaskedArray, /):
        """
        usage.matplotlib: 1
        """
        ...

    def __ror__(self, _0: Union[numpy.ma.core.MaskedArray, bool], /):
        """
        usage.matplotlib: 1
        usage.scipy: 3
        """
        ...

    @overload
    def __rsub__(self, _0: numpy.ma.core.MaskedArray, /):
        """
        usage.dask: 4
        usage.skimage: 2
        usage.sklearn: 1
        """
        ...

    @overload
    def __rsub__(
        self, _0: Union[numpy.ma.core.MaskedArray, numpy.ndarray, numpy.float64], /
    ):
        """
        usage.scipy: 13
        """
        ...

    @overload
    def __rsub__(self, _0: Union[numpy.ma.core.MaskedArray, int], /):
        """
        usage.matplotlib: 3
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

    @overload
    def __rtruediv__(self, _0: numpy.ma.core.MaskedArray, /):
        """
        usage.dask: 1
        usage.matplotlib: 1
        usage.skimage: 1
        """
        ...

    @overload
    def __rtruediv__(self, _0: object, /):
        """
        usage.scipy: 33
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

    @overload
    def __setitem__(
        self,
        _0: Union[Tuple[int, ...], slice[None, None, None]],
        _1: Union[int, numpy.ma.core.MaskedConstant],
        /,
    ):
        """
        usage.skimage: 6
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Tuple[Union[numpy.ndarray, numpy.bool_, int], int],
        _1: Union[int, float],
        /,
    ):
        """
        usage.xarray: 5
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Union[int, numpy.ndarray, Tuple[int, int]],
        _1: Union[
            Literal[
                "2001-01-02T00:00:00", "2001-01-03T00:00:00", "2001-01-01T00:00:00"
            ],
            bool,
            int,
            float,
            numpy.datetime64,
        ],
        /,
    ):
        """
        usage.pandas: 18
        """
        ...

    @overload
    def __setitem__(self, _0: object, _1: object, /):
        """
        usage.scipy: 41
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Union[
            int,
            numpy.ma.core.MaskedArray,
            Tuple[Union[int, ellipsis], Union[slice[None, None, None], int]],
        ],
        _1: Union[
            numpy.ma.core.MaskedConstant, numpy.ma.core.MaskedArray, numpy.float64, int
        ],
        /,
    ):
        """
        usage.matplotlib: 19
        """
        ...

    @overload
    def __setitem__(self, _0: numpy.ma.core.MaskedArray, _1: float, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(self, _0: int, _1: object, /):
        """
        usage.sklearn: 25
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

    @overload
    def __sub__(self, _0: Union[numpy.ma.core.MaskedArray, numpy.float64], /):
        """
        usage.skimage: 4
        """
        ...

    @overload
    def __sub__(
        self,
        _0: Union[
            numpy.ma.core.MaskedArray,
            numpy.ndarray,
            numpy.ma.core.MaskedConstant,
            numpy.float64,
            int,
        ],
        /,
    ):
        """
        usage.scipy: 27
        """
        ...

    @overload
    def __sub__(
        self,
        _0: Union[numpy.ma.core.MaskedArray, numpy.ndarray, float, numpy.float64],
        /,
    ):
        """
        usage.matplotlib: 7
        """
        ...

    @overload
    def __sub__(self, _0: Union[int, numpy.ma.core.MaskedArray], /):
        """
        usage.dask: 5
        """
        ...

    @overload
    def __sub__(self, _0: numpy.ma.core.MaskedArray, /):
        """
        usage.sklearn: 1
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

    @overload
    def __truediv__(self, _0: numpy.ma.core.MaskedArray, /):
        """
        usage.dask: 1
        usage.skimage: 1
        """
        ...

    @overload
    def __truediv__(self, _0: object, /):
        """
        usage.scipy: 36
        """
        ...

    @overload
    def __truediv__(
        self, _0: Union[numpy.ma.core.MaskedArray, int, float, numpy.float64], /
    ):
        """
        usage.matplotlib: 8
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

    def argsort(self, /, axis: None = ...):
        """
        usage.scipy: 8
        """
        ...

    @overload
    def astype(self, _0: numpy.dtype, /):
        """
        usage.pandas: 2
        """
        ...

    @overload
    def astype(self, _0: Union[type, Literal["d"]], /):
        """
        usage.scipy: 8
        """
        ...

    @overload
    def astype(self, _0: type, /):
        """
        usage.matplotlib: 7
        """
        ...

    @overload
    def astype(self, _0: Union[numpy.dtype, Type[numpy.int64], Literal["bool"]], /):
        """
        usage.dask: 10
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

    def count(self, /, axis: Union[None, int] = ...):
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

    @overload
    def filled(self, /, fill_value: float):
        """
        usage.xarray: 2
        """
        ...

    @overload
    def filled(self, /, fill_value: Union[float, bool, int]):
        """
        usage.scipy: 7
        """
        ...

    @overload
    def filled(self, /, fill_value: Union[int, float] = ...):
        """
        usage.matplotlib: 17
        """
        ...

    @overload
    def filled(self, /, fill_value: int):
        """
        usage.sklearn: 1
        """
        ...

    def filled(self, /, fill_value: Union[int, bool, float] = ...):
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

    def max(self, /, axis: int = ...):
        """
        usage.matplotlib: 32
        """
        ...

    @overload
    def mean(self, /):
        """
        usage.skimage: 1
        usage.sklearn: 1
        """
        ...

    @overload
    def mean(self, /, axis: Union[None, int] = ..., keepdims: bool = ...):
        """
        usage.scipy: 32
        """
        ...

    def mean(self, /, axis: Union[None, int] = ..., keepdims: bool = ...):
        """
        usage.scipy: 32
        usage.skimage: 1
        usage.sklearn: 1
        """
        ...

    @overload
    def min(self, /):
        """
        usage.scipy: 4
        """
        ...

    @overload
    def min(self, /, axis: int = ...):
        """
        usage.matplotlib: 35
        """
        ...

    @overload
    def min(self, /, axis: int):
        """
        usage.sklearn: 2
        """
        ...

    def min(self, /, axis: int = ...):
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

    @overload
    def sum(self, /, axis: Union[None, int] = ...):
        """
        usage.scipy: 13
        """
        ...

    @overload
    def sum(
        self,
        /,
        axis: Tuple[int, ...] = ...,
        dtype: Union[Literal["f8"], numpy.dtype] = ...,
        keepdims: bool = ...,
    ):
        """
        usage.dask: 27
        """
        ...

    @overload
    def sum(self, /, axis: int):
        """
        usage.sklearn: 1
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

    def var(self, /, ddof: int, axis: int = ...):
        """
        usage.scipy: 11
        """
        ...

    @overload
    def view(self, /, dtype: Type[numpy.ma.mrecords.MaskedRecords] = ...):
        """
        usage.pandas: 4
        """
        ...

    @overload
    def view(self, /, dtype: type):
        """
        usage.scipy: 2
        """
        ...

    def view(self, /, dtype: type = ...):
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

    @overload
    def __add__(self, _0: numpy.float64, /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def __add__(self, _0: Union[numpy.ma.core.MaskedConstant, numpy.float64], /):
        """
        usage.matplotlib: 8
        """
        ...

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

    @overload
    def __mul__(self, _0: Union[numpy.float64, numpy.ma.core.MaskedConstant], /):
        """
        usage.scipy: 4
        """
        ...

    @overload
    def __mul__(self, _0: numpy.float64, /):
        """
        usage.matplotlib: 3
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

    @overload
    def __radd__(self, _0: numpy.ma.core.MaskedArray, /):
        """
        usage.scipy: 3
        """
        ...

    @overload
    def __radd__(self, _0: Union[numpy.float64, numpy.ma.core.MaskedConstant], /):
        """
        usage.matplotlib: 6
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

    @overload
    def __sub__(self, _0: float, /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def __sub__(self, _0: numpy.float64, /):
        """
        usage.matplotlib: 1
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
    def reduce(self, /, target: numpy.ma.core.MaskedArray, axis: int = ...):
        """
        usage.scipy: 8
        """
        ...
