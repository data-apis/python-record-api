from typing import *


@overload
def _check_fill_value(fill_value: int, ndtype: numpy.dtype):
    """
    usage.dask: 1
    """
    ...


@overload
def _check_fill_value(fill_value: float, ndtype: numpy.dtype):
    """
    usage.dask: 1
    """
    ...


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
def array(data: numpy.ndarray, mask: List[List[int]]):
    """
    usage.skimage: 1
    """
    ...


@overload
def array(data: numpy.ndarray, mask: bool, fill_value: float):
    """
    usage.skimage: 2
    """
    ...


@overload
def array(data: numpy.ndarray, mask: numpy.ndarray, fill_value: float):
    """
    usage.skimage: 2
    """
    ...


@overload
def array(data: numpy.ndarray, mask: numpy.ndarray, fill_value: numpy.float64):
    """
    usage.skimage: 1
    """
    ...


@overload
def array(data: numpy.ndarray, mask: numpy.ndarray):
    """
    usage.dask: 2
    usage.matplotlib: 7
    usage.scipy: 8
    usage.skimage: 1
    usage.sklearn: 4
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
def array(data: numpy.ndarray, copy: bool):
    """
    usage.scipy: 5
    """
    ...


@overload
def array(data: List[int]):
    """
    usage.scipy: 17
    """
    ...


@overload
def array(data: List[int], mask: List[int]):
    """
    usage.matplotlib: 1
    usage.scipy: 7
    """
    ...


@overload
def array(data: List[List[int]], mask: List[List[int]]):
    """
    usage.scipy: 2
    """
    ...


@overload
def array(data: List[numpy.float64]):
    """
    usage.scipy: 1
    """
    ...


@overload
def array(data: List[List[int]]):
    """
    usage.matplotlib: 1
    usage.scipy: 4
    """
    ...


@overload
def array(data: numpy.ma.core.MaskedArray, copy: bool):
    """
    usage.scipy: 5
    """
    ...


@overload
def array(data: numpy.ma.core.MaskedArray, mask: bool):
    """
    usage.scipy: 1
    """
    ...


@overload
def array(data: List[float]):
    """
    usage.scipy: 2
    """
    ...


@overload
def array(data: List[float], mask: List[bool]):
    """
    usage.scipy: 1
    """
    ...


@overload
def array(data: List[int], mask: List[bool]):
    """
    usage.scipy: 2
    """
    ...


@overload
def array(data: numpy.ndarray):
    """
    usage.matplotlib: 3
    usage.scipy: 10
    """
    ...


@overload
def array(data: numpy.ma.core.MaskedArray, copy: bool, mask: numpy.ndarray):
    """
    usage.scipy: 4
    """
    ...


@overload
def array(data: numpy.ma.core.MaskedArray, copy: bool, subok: bool, ndmin: int):
    """
    usage.scipy: 1
    """
    ...


@overload
def array(data: numpy.ma.core.MaskedArray, copy: bool, subok: bool):
    """
    usage.scipy: 1
    """
    ...


@overload
def array(data: numpy.ma.core.MaskedArray, copy: numpy.bool_):
    """
    usage.scipy: 2
    """
    ...


@overload
def array(data: List[Union[int, float]]):
    """
    usage.scipy: 3
    """
    ...


@overload
def array(data: numpy.ndarray, mask: bool):
    """
    usage.scipy: 1
    """
    ...


@overload
def array(data: numpy.ndarray, mask: numpy.bool_):
    """
    usage.matplotlib: 2
    usage.scipy: 1
    """
    ...


@overload
def array(data: numpy.ma.core.MaskedArray):
    """
    usage.matplotlib: 1
    usage.scipy: 2
    """
    ...


@overload
def array(data: numpy.ma.core.MaskedArray, mask: numpy.ndarray):
    """
    usage.matplotlib: 2
    usage.scipy: 2
    """
    ...


@overload
def array(data: numpy.ndarray, copy: bool, subok: bool):
    """
    usage.scipy: 2
    """
    ...


@overload
def array(data: numpy.ma.core.MaskedArray, dtype: Type[numpy.float64], copy: bool):
    """
    usage.scipy: 1
    """
    ...


@overload
def array(data: List[float], dtype: Type[numpy.float64], copy: bool):
    """
    usage.scipy: 2
    """
    ...


@overload
def array(data: numpy.ndarray, dtype: Type[numpy.float64], copy: bool):
    """
    usage.scipy: 1
    """
    ...


@overload
def array(data: List[float], copy: bool):
    """
    usage.scipy: 2
    """
    ...


@overload
def array(data: list):
    """
    usage.scipy: 1
    """
    ...


@overload
def array(data: List[list]):
    """
    usage.scipy: 1
    """
    ...


@overload
def array(data: numpy.ndarray, dtype: numpy.dtype, copy: bool, mask: numpy.bool_):
    """
    usage.matplotlib: 9
    """
    ...


@overload
def array(data: numpy.ndarray, copy: bool, mask: numpy.bool_):
    """
    usage.matplotlib: 4
    """
    ...


@overload
def array(data: numpy.ndarray, dtype: numpy.dtype, copy: bool, mask: numpy.ndarray):
    """
    usage.matplotlib: 2
    """
    ...


@overload
def array(data: numpy.ndarray, copy: bool, mask: numpy.ndarray):
    """
    usage.matplotlib: 5
    """
    ...


@overload
def array(data: List[None], dtype: Type[float], mask: List[bool]):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def array(data: List[Union[int, float]], mask: List[bool]):
    """
    usage.matplotlib: 2
    """
    ...


@overload
def array(data: List[Literal["b", "k"]], mask: List[bool]):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def array(data: List[Union[None, int]], dtype: Type[float], mask: List[bool]):
    """
    usage.matplotlib: 3
    """
    ...


@overload
def array(data: List[Union[int, None]], dtype: Type[float], mask: List[bool]):
    """
    usage.matplotlib: 1
    """
    ...


def array(
    data: Union[numpy.ndarray, numpy.ma.core.MaskedArray, list],
    dtype: Union[numpy.dtype, Type[float], Type[numpy.float64]] = ...,
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


@overload
def asanyarray(a: numpy.ma.core.MaskedArray):
    """
    usage.scipy: 8
    """
    ...


@overload
def asanyarray(a: List[float]):
    """
    usage.scipy: 4
    """
    ...


@overload
def asanyarray(a: List[int]):
    """
    usage.scipy: 13
    """
    ...


@overload
def asanyarray(a: numpy.ndarray):
    """
    usage.scipy: 10
    """
    ...


@overload
def asanyarray(a: numpy.float64):
    """
    usage.scipy: 3
    """
    ...


@overload
def asanyarray(a: list):
    """
    usage.scipy: 3
    """
    ...


@overload
def asanyarray(a: Tuple[float, float]):
    """
    usage.scipy: 1
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
def asarray(a: numpy.ma.core.MaskedArray):
    """
    usage.matplotlib: 15
    usage.scipy: 10
    """
    ...


@overload
def asarray(a: List[int]):
    """
    usage.matplotlib: 6
    usage.scipy: 3
    """
    ...


@overload
def asarray(a: numpy.ndarray):
    """
    usage.matplotlib: 10
    usage.scipy: 5
    """
    ...


@overload
def asarray(a: list):
    """
    usage.scipy: 2
    """
    ...


@overload
def asarray(a: numpy.ndarray, dtype: Type[numpy.float64]):
    """
    usage.matplotlib: 4
    """
    ...


@overload
def asarray(a: numpy.ma.core.MaskedArray, dtype: Type[float]):
    """
    usage.matplotlib: 2
    """
    ...


@overload
def asarray(a: List[List[int]], dtype: Type[numpy.float64]):
    """
    usage.matplotlib: 2
    """
    ...


@overload
def asarray(a: List[float]):
    """
    usage.matplotlib: 2
    """
    ...


@overload
def asarray(a: numpy.float64):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def asarray(a: int):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def asarray(a: numpy.ma.core.MaskedArray, dtype: Type[numpy.float64]):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def asarray(a: List[List[float]], dtype: Type[numpy.float64]):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def asarray(a: numpy.int64):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def asarray(a: List[Union[float, int]]):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def asarray(a: matplotlib.tests.test_units.Quantity, dtype: Type[float]):
    """
    usage.matplotlib: 1
    """
    ...


def asarray(a: object, dtype: type = ...):
    """
    usage.matplotlib: 48
    usage.scipy: 20
    """
    ...


@overload
def compressed(x: numpy.ma.core.MaskedArray):
    """
    usage.scipy: 4
    """
    ...


@overload
def compressed(x: numpy.ndarray):
    """
    usage.scipy: 3
    """
    ...


@overload
def compressed(x: list):
    """
    usage.scipy: 1
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
def concatenate(arrays: Tuple[numpy.ndarray, numpy.ma.core.MaskedArray], axis: int):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def concatenate(arrays: Tuple[numpy.ma.core.MaskedArray, numpy.ndarray], axis: int):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def concatenate(arrays: List[numpy.ma.core.MaskedArray], axis: int):
    """
    usage.dask: 16
    """
    ...


@overload
def concatenate(
    arrays: List[Union[numpy.ma.core.MaskedArray, numpy.ndarray]], axis: int
):
    """
    usage.dask: 12
    """
    ...


@overload
def concatenate(
    arrays: List[Union[numpy.ndarray, numpy.ma.core.MaskedArray]], axis: int
):
    """
    usage.dask: 9
    """
    ...


def concatenate(
    arrays: Union[
        List[Union[numpy.ndarray, numpy.ma.core.MaskedArray]],
        Tuple[
            Union[numpy.ndarray, numpy.ma.core.MaskedArray],
            Union[numpy.ndarray, numpy.ma.core.MaskedArray],
        ],
    ],
    axis: int,
):
    """
    usage.dask: 37
    usage.matplotlib: 2
    usage.xarray: 3
    """
    ...


@overload
def dot(a: numpy.ma.core.MaskedArray, b: numpy.ma.core.MaskedArray):
    """
    usage.dask: 1
    usage.scipy: 1
    """
    ...


@overload
def dot(a: numpy.ma.core.MaskedArray, b: numpy.ndarray):
    """
    usage.dask: 2
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
def filled(a: numpy.ma.core.MaskedArray, fill_value: int):
    """
    usage.dask: 9
    usage.scipy: 1
    """
    ...


@overload
def filled(a: numpy.ndarray, fill_value: int):
    """
    usage.dask: 5
    usage.scipy: 1
    """
    ...


@overload
def filled(a: numpy.float64, fill_value: int):
    """
    usage.dask: 1
    usage.scipy: 1
    """
    ...


@overload
def filled(a: numpy.ndarray, fill_value: float):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def filled(a: numpy.ma.core.MaskedArray):
    """
    usage.dask: 4
    usage.matplotlib: 18
    """
    ...


@overload
def filled(a: numpy.ma.core.MaskedArray, fill_value: float):
    """
    usage.dask: 1
    usage.matplotlib: 2
    """
    ...


@overload
def filled(a: numpy.ndarray, fill_value: bool):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def filled(a: numpy.ma.core.MaskedArray, fill_value: bool):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def filled(a: numpy.ndarray, fill_value: None):
    """
    usage.dask: 5
    """
    ...


@overload
def filled(a: numpy.ma.core.MaskedArray, fill_value: None):
    """
    usage.dask: 6
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
def fix_invalid(a: List[float]):
    """
    usage.scipy: 6
    """
    ...


@overload
def fix_invalid(a: List[int]):
    """
    usage.scipy: 2
    """
    ...


@overload
def fix_invalid(a: List[List[Union[int, float]]]):
    """
    usage.scipy: 3
    """
    ...


@overload
def fix_invalid(a: List[int], copy: bool):
    """
    usage.scipy: 1
    """
    ...


@overload
def fix_invalid(a: List[float], copy: bool):
    """
    usage.scipy: 1
    """
    ...


@overload
def fix_invalid(a: numpy.ndarray, copy: bool):
    """
    usage.scipy: 2
    """
    ...


@overload
def fix_invalid(a: numpy.ma.core.MaskedArray, copy: bool):
    """
    usage.scipy: 1
    """
    ...


@overload
def fix_invalid(a: numpy.ndarray, fill_value: int):
    """
    usage.dask: 1
    """
    ...


@overload
def fix_invalid(a: numpy.ma.core.MaskedArray, fill_value: int):
    """
    usage.dask: 3
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
def getdata(a: numpy.ndarray):
    """
    usage.dask: 5
    usage.matplotlib: 16
    usage.skimage: 2
    """
    ...


@overload
def getdata(a: numpy.ma.core.MaskedArray):
    """
    usage.dask: 4
    usage.matplotlib: 4
    usage.skimage: 1
    usage.sklearn: 2
    """
    ...


@overload
def getdata(a: numpy.ma.mrecords.MaskedRecords):
    """
    usage.pandas: 1
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
def getmask(a: numpy.ndarray):
    """
    usage.matplotlib: 5
    usage.scipy: 17
    """
    ...


@overload
def getmask(a: numpy.ma.core.MaskedArray):
    """
    usage.matplotlib: 8
    usage.scipy: 16
    usage.sklearn: 1
    """
    ...


@overload
def getmask(a: List[numpy.int64]):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def getmask(a: List[numpy.bool_]):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def getmask(a: List[numpy.float64]):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def getmask(a: List[float]):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def getmask(a: List[Union[int, float]]):
    """
    usage.matplotlib: 2
    """
    ...


@overload
def getmask(a: List[int]):
    """
    usage.matplotlib: 4
    """
    ...


@overload
def getmask(a: List[numpy.float128]):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def getmask(a: List[Union[float, int]]):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def getmask(a: List[None]):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def getmask(a: object):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def getmask(a: List[numpy.ma.core.MaskedArray]):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def getmask(a: List[numpy.uint16]):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def getmask(a: List[numpy.ma.core.MaskedConstant]):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def getmask(a: List[numpy.float32]):
    """
    usage.matplotlib: 1
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
    usage.dask: 5
    usage.matplotlib: 8
    usage.pandas: 7
    usage.scipy: 4
    usage.skimage: 1
    usage.sklearn: 1
    usage.xarray: 2
    """
    ...


@overload
def getmaskarray(arr: numpy.ndarray):
    """
    usage.dask: 4
    usage.scipy: 1
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
def isMaskedArray(x: numpy.ndarray):
    """
    usage.scipy: 12
    usage.skimage: 7
    """
    ...


@overload
def isMaskedArray(x: numpy.ma.core.MaskedArray):
    """
    usage.scipy: 1
    usage.skimage: 11
    """
    ...


@overload
def isMaskedArray(x: numpy.matrix):
    """
    usage.scipy: 4
    """
    ...


@overload
def isMaskedArray(x: list):
    """
    usage.scipy: 1
    """
    ...


@overload
def isMaskedArray(x: float):
    """
    usage.scipy: 1
    """
    ...


@overload
def isMaskedArray(x: List[float]):
    """
    usage.scipy: 4
    """
    ...


@overload
def isMaskedArray(x: List[Union[int, float]]):
    """
    usage.scipy: 1
    """
    ...


@overload
def isMaskedArray(x: List[List[List[float]]]):
    """
    usage.scipy: 1
    """
    ...


@overload
def isMaskedArray(x: int):
    """
    usage.scipy: 1
    """
    ...


@overload
def isMaskedArray(x: List[int]):
    """
    usage.scipy: 5
    """
    ...


@overload
def isMaskedArray(x: List[numpy.float64]):
    """
    usage.scipy: 1
    """
    ...


@overload
def isMaskedArray(x: List[numpy.ndarray]):
    """
    usage.scipy: 1
    """
    ...


@overload
def isMaskedArray(x: List[List[int]]):
    """
    usage.scipy: 8
    """
    ...


@overload
def isMaskedArray(x: List[List[Union[float, int]]]):
    """
    usage.scipy: 1
    """
    ...


@overload
def isMaskedArray(x: List[List[Union[int, float]]]):
    """
    usage.scipy: 3
    """
    ...


@overload
def isMaskedArray(x: List[Union[complex, int]]):
    """
    usage.scipy: 1
    """
    ...


@overload
def isMaskedArray(x: List[Union[int, complex]]):
    """
    usage.scipy: 1
    """
    ...


@overload
def isMaskedArray(x: List[List[Union[complex, int]]]):
    """
    usage.scipy: 5
    """
    ...


@overload
def isMaskedArray(x: List[list]):
    """
    usage.scipy: 2
    """
    ...


@overload
def isMaskedArray(x: List[List[Union[int, complex]]]):
    """
    usage.scipy: 6
    """
    ...


@overload
def isMaskedArray(x: List[List[float]]):
    """
    usage.scipy: 3
    """
    ...


@overload
def isMaskedArray(x: scipy.linalg._testutils._FakeMatrix):
    """
    usage.scipy: 1
    """
    ...


@overload
def isMaskedArray(x: scipy.linalg._testutils._FakeMatrix2):
    """
    usage.scipy: 1
    """
    ...


@overload
def isMaskedArray(x: Literal["Some string for fail"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def isMaskedArray(x: List[List[complex]]):
    """
    usage.scipy: 1
    """
    ...


@overload
def isMaskedArray(x: scipy.optimize.nonlin.LowRankMatrix):
    """
    usage.scipy: 1
    """
    ...


@overload
def isMaskedArray(x: numpy.float64):
    """
    usage.scipy: 1
    """
    ...


def isMaskedArray(x: object):
    """
    usage.scipy: 69
    usage.skimage: 18
    """
    ...


@overload
def is_masked(x: numpy.ndarray):
    """
    usage.matplotlib: 7
    usage.scipy: 5
    """
    ...


@overload
def is_masked(x: numpy.ma.core.MaskedArray):
    """
    usage.matplotlib: 13
    usage.scipy: 3
    """
    ...


@overload
def is_masked(x: List[int]):
    """
    usage.scipy: 4
    """
    ...


@overload
def is_masked(x: List[numpy.float64]):
    """
    usage.scipy: 2
    """
    ...


@overload
def is_masked(x: List[float]):
    """
    usage.scipy: 1
    """
    ...


@overload
def is_masked(x: list):
    """
    usage.scipy: 2
    """
    ...


@overload
def is_masked(x: numpy.float64):
    """
    usage.matplotlib: 6
    """
    ...


@overload
def is_masked(x: numpy.int64):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def is_masked(x: List[Union[int, float]]):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def is_masked(x: List[Union[float, int]]):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def is_masked(x: float):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def is_masked(x: int):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def is_masked(x: numpy.ma.core.MaskedConstant):
    """
    usage.matplotlib: 1
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
def mask_or(m1: numpy.bool_, m2: numpy.bool_):
    """
    usage.scipy: 4
    """
    ...


@overload
def mask_or(m1: numpy.ndarray, m2: numpy.ndarray):
    """
    usage.scipy: 3
    """
    ...


@overload
def mask_or(m1: numpy.ndarray, m2: numpy.bool_):
    """
    usage.scipy: 1
    """
    ...


@overload
def mask_or(m1: numpy.bool_, m2: numpy.ndarray):
    """
    usage.scipy: 2
    """
    ...


@overload
def mask_or(m1: numpy.bool_, m2: numpy.bool_, shrink: bool):
    """
    usage.scipy: 1
    """
    ...


@overload
def mask_or(m1: numpy.ndarray, m2: numpy.ndarray, shrink: bool):
    """
    usage.scipy: 1
    """
    ...


@overload
def mask_or(m1: numpy.ndarray, m2: numpy.ndarray, copy: bool, shrink: bool):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def mask_or(m1: numpy.bool_, m2: numpy.bool_, copy: bool, shrink: bool):
    """
    usage.matplotlib: 1
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
def masked_greater(x: numpy.ndarray, value: int):
    """
    usage.dask: 5
    usage.matplotlib: 1
    usage.scipy: 3
    """
    ...


@overload
def masked_greater(x: numpy.ma.core.MaskedArray, value: float):
    """
    usage.scipy: 1
    """
    ...


@overload
def masked_greater(x: numpy.ma.core.MaskedArray, value: int):
    """
    usage.scipy: 2
    """
    ...


@overload
def masked_greater(x: numpy.ndarray, value: float):
    """
    usage.dask: 3
    usage.matplotlib: 2
    """
    ...


@overload
def masked_greater(x: numpy.ndarray, value: numpy.ndarray):
    """
    usage.dask: 5
    """
    ...


@overload
def masked_greater(x: dask.array.core.Array, value: dask.array.core.Array):
    """
    usage.dask: 1
    """
    ...


@overload
def masked_greater(x: dask.array.core.Array, value: numpy.ndarray):
    """
    usage.dask: 1
    """
    ...


@overload
def masked_greater(x: numpy.ndarray, value: dask.array.core.Array):
    """
    usage.dask: 1
    """
    ...


@overload
def masked_greater(x: dask.array.core.Array, value: int):
    """
    usage.dask: 4
    """
    ...


@overload
def masked_greater(x: dask.array.core.Array, value: float):
    """
    usage.dask: 3
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
def masked_greater_equal(x: dask.array.core.Array, value: int):
    """
    usage.dask: 1
    """
    ...


@overload
def masked_greater_equal(x: numpy.ndarray, value: numpy.ndarray):
    """
    usage.dask: 1
    """
    ...


@overload
def masked_greater_equal(x: numpy.ndarray, value: int):
    """
    usage.dask: 1
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
    usage.matplotlib: 5
    usage.xarray: 4
    """
    ...


@overload
def masked_invalid(a: numpy.ma.core.MaskedArray):
    """
    usage.matplotlib: 3
    usage.scipy: 3
    """
    ...


@overload
def masked_invalid(a: numpy.ndarray):
    """
    usage.dask: 3
    usage.matplotlib: 17
    usage.scipy: 22
    usage.sklearn: 4
    """
    ...


@overload
def masked_invalid(a: numpy.ndarray, copy: bool):
    """
    usage.matplotlib: 23
    """
    ...


@overload
def masked_invalid(a: numpy.ma.core.MaskedArray, copy: bool):
    """
    usage.matplotlib: 9
    """
    ...


@overload
def masked_invalid(a: int):
    """
    usage.matplotlib: 4
    """
    ...


@overload
def masked_invalid(a: float):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def masked_invalid(a: range):
    """
    usage.matplotlib: 4
    """
    ...


@overload
def masked_invalid(a: List[Union[int, float]]):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def masked_invalid(a: object, copy: bool):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def masked_invalid(a: List[Union[float, int]]):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def masked_invalid(a: List[int]):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def masked_invalid(a: int, copy: bool):
    """
    usage.matplotlib: 2
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
def masked_less(x: numpy.ma.core.MaskedArray, value: float):
    """
    usage.scipy: 1
    """
    ...


@overload
def masked_less(x: numpy.ma.core.MaskedArray, value: int):
    """
    usage.scipy: 2
    """
    ...


@overload
def masked_less(x: dask.array.core.Array, value: int):
    """
    usage.dask: 1
    """
    ...


@overload
def masked_less(x: numpy.ndarray, value: numpy.ndarray):
    """
    usage.dask: 1
    """
    ...


@overload
def masked_less(x: numpy.ndarray, value: int):
    """
    usage.dask: 1
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
def masked_less_equal(x: numpy.ndarray, value: int, copy: bool):
    """
    usage.matplotlib: 2
    """
    ...


@overload
def masked_less_equal(x: numpy.ma.core.MaskedArray, value: int, copy: bool):
    """
    usage.matplotlib: 5
    """
    ...


@overload
def masked_less_equal(x: dask.array.core.Array, value: int):
    """
    usage.dask: 1
    """
    ...


@overload
def masked_less_equal(x: numpy.ndarray, value: numpy.ndarray):
    """
    usage.dask: 1
    """
    ...


@overload
def masked_less_equal(x: numpy.ndarray, value: int):
    """
    usage.dask: 1
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


@overload
def masked_not_equal(x: dask.array.core.Array, value: int):
    """
    usage.dask: 1
    """
    ...


@overload
def masked_not_equal(x: numpy.ndarray, value: numpy.ndarray):
    """
    usage.dask: 1
    """
    ...


@overload
def masked_not_equal(x: numpy.ndarray, value: int):
    """
    usage.dask: 1
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
    usage.dask: 1
    usage.scipy: 1
    """
    ...


@overload
def masked_values(x: numpy.ndarray, value: int, rtol: float, atol: float, shrink: bool):
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


@overload
def masked_where(condition: numpy.ndarray, a: numpy.ndarray):
    """
    usage.dask: 2
    usage.matplotlib: 2
    usage.scipy: 7
    usage.xarray: 1
    """
    ...


@overload
def masked_where(condition: numpy.ndarray, a: numpy.ndarray, copy: bool):
    """
    usage.scipy: 3
    """
    ...


@overload
def masked_where(condition: numpy.ma.core.MaskedArray, a: List[int]):
    """
    usage.scipy: 1
    """
    ...


@overload
def masked_where(condition: numpy.ma.core.MaskedArray, a: numpy.ndarray):
    """
    usage.scipy: 1
    """
    ...


@overload
def masked_where(condition: bool, a: numpy.ndarray):
    """
    usage.dask: 1
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
def power(a: numpy.float64, b: float):
    """
    usage.scipy: 2
    """
    ...


@overload
def power(a: numpy.ma.core.MaskedArray, b: float):
    """
    usage.matplotlib: 1
    usage.scipy: 2
    """
    ...


@overload
def power(a: float, b: numpy.ndarray):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def power(a: float, b: numpy.ma.core.MaskedArray):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def power(a: numpy.float64, b: numpy.ma.core.MaskedArray):
    """
    usage.matplotlib: 1
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


@overload
def set_fill_value(a: numpy.ma.core.MaskedArray, fill_value: numpy.ndarray):
    """
    usage.dask: 1
    """
    ...


@overload
def set_fill_value(a: numpy.ma.core.MaskedArray, fill_value: int):
    """
    usage.dask: 1
    """
    ...


@overload
def set_fill_value(a: numpy.ndarray, fill_value: int):
    """
    usage.dask: 1
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


@overload
def sort(a: numpy.ma.core.MaskedArray, axis: None):
    """
    usage.scipy: 1
    """
    ...


@overload
def sort(a: numpy.ndarray, axis: None):
    """
    usage.scipy: 1
    """
    ...


@overload
def sort(a: numpy.ndarray, axis: int):
    """
    usage.scipy: 1
    """
    ...


@overload
def sort(a: List[int], axis: None):
    """
    usage.scipy: 1
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


@overload
def where(condition: numpy.bool_, x: numpy.ndarray, y: float):
    """
    usage.scipy: 1
    """
    ...


@overload
def where(condition: numpy.bool_, x: int, y: numpy.float64):
    """
    usage.scipy: 3
    """
    ...


@overload
def where(condition: numpy.ma.core.MaskedArray, x: int, y: numpy.ma.core.MaskedArray):
    """
    usage.scipy: 3
    """
    ...


@overload
def where(
    condition: numpy.ma.core.MaskedConstant, x: int, y: numpy.ma.core.MaskedConstant
):
    """
    usage.scipy: 1
    """
    ...


@overload
def where(
    condition: numpy.bool_,
    x: numpy.ma.core.MaskedArray,
    y: numpy.ma.core.MaskedConstant,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def where(
    condition: numpy.ma.core.MaskedArray,
    x: numpy.ma.core.MaskedArray,
    y: numpy.ma.core.MaskedArray,
):
    """
    usage.scipy: 1
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
        usage.matplotlib: 1
        usage.scipy: 4
        usage.skimage: 1
        """
        ...

    @overload
    def __add__(self, _0: float, /):
        """
        usage.matplotlib: 2
        usage.scipy: 1
        """
        ...

    @overload
    def __add__(self, _0: int, /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def __add__(self, _0: numpy.ma.core.MaskedArray, /):
        """
        usage.dask: 1
        usage.matplotlib: 4
        usage.scipy: 6
        """
        ...

    @overload
    def __add__(self, _0: numpy.ma.core.MaskedConstant, /):
        """
        usage.scipy: 3
        """
        ...

    @overload
    def __add__(self, _0: numpy.ndarray, /):
        """
        usage.scipy: 1
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
        usage.matplotlib: 6
        usage.scipy: 3
        usage.skimage: 1
        """
        ...

    @overload
    def __eq__(self, _0: numpy.float64, /):
        """
        usage.scipy: 4
        """
        ...

    @overload
    def __eq__(self, _0: float, /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def __eq__(self, _0: numpy.ma.core.MaskedArray, /):
        """
        usage.matplotlib: 2
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
    def __ge__(self, _0: int, /):
        """
        usage.matplotlib: 1
        usage.scipy: 3
        """
        ...

    @overload
    def __ge__(self, _0: numpy.ma.core.MaskedArray, /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def __ge__(self, _0: numpy.ndarray, /):
        """
        usage.matplotlib: 1
        """
        ...

    def __ge__(self, _0: Union[numpy.ndarray, int, numpy.ma.core.MaskedArray], /):
        """
        usage.matplotlib: 2
        usage.scipy: 4
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, int], /):
        """
        usage.matplotlib: 12
        usage.scipy: 4
        usage.skimage: 2
        usage.xarray: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, None, None], int], /):
        """
        usage.matplotlib: 6
        usage.scipy: 9
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, int, int], /):
        """
        usage.skimage: 2
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[slice[None, None, None], slice[None, None, None], int], /
    ):
        """
        usage.matplotlib: 1
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, None, None], /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.ndarray, slice[None, None, None]], /):
        """
        usage.scipy: 2
        """
        ...

    @overload
    def __getitem__(self, _0: numpy.ndarray, /):
        """
        usage.matplotlib: 11
        usage.scipy: 3
        """
        ...

    @overload
    def __getitem__(self, _0: slice[int, None, int], /):
        """
        usage.matplotlib: 1
        usage.scipy: 3
        """
        ...

    @overload
    def __getitem__(self, _0: int, /):
        """
        usage.matplotlib: 24
        usage.scipy: 15
        usage.sklearn: 21
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[int, None, int], int], /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def __getitem__(self, _0: numpy.ma.core.MaskedArray, /):
        """
        usage.matplotlib: 5
        usage.scipy: 2
        """
        ...

    @overload
    def __getitem__(self, _0: numpy.int64, /):
        """
        usage.matplotlib: 1
        usage.scipy: 7
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, slice[None, None, None]], /):
        """
        usage.scipy: 4
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int], /):
        """
        usage.scipy: 4
        """
        ...

    @overload
    def __getitem__(self, _0: slice[int, int, int], /):
        """
        usage.scipy: 4
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, None, None], None], /):
        """
        usage.matplotlib: 5
        usage.scipy: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[None, slice[None, None, None]], /):
        """
        usage.scipy: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[ellipsis, int], /):
        """
        usage.dask: 1
        usage.matplotlib: 2
        usage.scipy: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, None, None], List[int]], /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[int], /):
        """
        usage.matplotlib: 4
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, int, None], slice[None, int, None]], /):
        """
        usage.matplotlib: 6
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[int, None, int], slice[None, int, None]], /):
        """
        usage.matplotlib: 4
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[int, None, int], slice[int, None, int]], /):
        """
        usage.matplotlib: 4
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, int, None], slice[int, None, int]], /):
        """
        usage.matplotlib: 4
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[ellipsis, slice[None, int, None]], /):
        """
        usage.matplotlib: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[ellipsis, int, None], /):
        """
        usage.matplotlib: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[ellipsis, None], /):
        """
        usage.dask: 1
        usage.matplotlib: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.int64, numpy.int64], /):
        """
        usage.matplotlib: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.ndarray, numpy.ndarray], /):
        """
        usage.matplotlib: 4
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, int, None], /):
        """
        usage.matplotlib: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[int, int, int]], /):
        """
        usage.dask: 4
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[slice[int, int, int], slice[int, int, int], slice[int, int, int]],
        /,
    ):
        """
        usage.dask: 3
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[int, int, int], slice[int, int, int]], /):
        """
        usage.dask: 5
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            slice[int, int, int],
            slice[int, int, int],
            slice[int, int, int],
            slice[int, int, int],
        ],
        /,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[slice[None, None, None], slice[None, None, None], None], /
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            slice[None, None, None],
            slice[None, None, None],
            None,
            slice[None, None, None],
        ],
        /,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[None, None, slice[None, None, None]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            slice[None, None, None],
            slice[None, None, None],
            None,
            slice[None, None, None],
            slice[None, None, None],
        ],
        /,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            slice[None, None, None],
            None,
            slice[None, None, None],
            slice[None, None, None],
            slice[None, None, None],
        ],
        /,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[slice[None, None, None], None, None, slice[None, None, None]], /
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[None, ...], /):
        """
        usage.dask: 3
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
    def __gt__(self, _0: int, /):
        """
        usage.scipy: 5
        """
        ...

    @overload
    def __gt__(self, _0: numpy.float64, /):
        """
        usage.matplotlib: 1
        usage.scipy: 2
        """
        ...

    @overload
    def __gt__(self, _0: numpy.ma.core.MaskedConstant, /):
        """
        usage.scipy: 2
        """
        ...

    @overload
    def __gt__(self, _0: float, /):
        """
        usage.matplotlib: 1
        usage.scipy: 1
        """
        ...

    @overload
    def __gt__(self, _0: numpy.ma.core.MaskedArray, /):
        """
        usage.scipy: 1
        """
        ...

    def __gt__(
        self,
        _0: Union[
            float,
            numpy.float64,
            numpy.ma.core.MaskedConstant,
            int,
            numpy.ma.core.MaskedArray,
        ],
        /,
    ):
        """
        usage.matplotlib: 2
        usage.scipy: 11
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
        usage.matplotlib: 1
        usage.xarray: 1
        """
        ...

    @overload
    def __imul__(self, _0: numpy.ma.core.MaskedArray, /):
        """
        usage.matplotlib: 1
        usage.scipy: 1
        """
        ...

    @overload
    def __imul__(self, _0: numpy.ndarray, /):
        """
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
    def __itruediv__(self, _0: float, /):
        """
        usage.matplotlib: 1
        """
        ...

    @overload
    def __itruediv__(self, _0: numpy.ma.core.MaskedArray, /):
        """
        usage.matplotlib: 1
        """
        ...

    @overload
    def __itruediv__(self, _0: numpy.float64, /):
        """
        usage.matplotlib: 1
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
    def __le__(self, _0: int, /):
        """
        usage.matplotlib: 1
        usage.scipy: 1
        """
        ...

    @overload
    def __le__(self, _0: numpy.ma.core.MaskedArray, /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def __le__(self, _0: numpy.ndarray, /):
        """
        usage.matplotlib: 1
        usage.scipy: 1
        usage.sklearn: 2
        """
        ...

    @overload
    def __le__(self, _0: numpy.float64, /):
        """
        usage.matplotlib: 1
        """
        ...

    def __le__(
        self, _0: Union[numpy.ndarray, numpy.ma.core.MaskedArray, numpy.float64, int], /
    ):
        """
        usage.matplotlib: 3
        usage.scipy: 3
        usage.sklearn: 2
        """
        ...

    @overload
    def __lt__(self, _0: int, /):
        """
        usage.dask: 1
        usage.scipy: 3
        """
        ...

    @overload
    def __lt__(self, _0: numpy.float64, /):
        """
        usage.matplotlib: 1
        usage.scipy: 1
        """
        ...

    @overload
    def __lt__(self, _0: numpy.ma.core.MaskedConstant, /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def __lt__(self, _0: float, /):
        """
        usage.matplotlib: 1
        usage.scipy: 1
        """
        ...

    @overload
    def __lt__(self, _0: numpy.ma.core.MaskedArray, /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def __lt__(self, _0: numpy.ndarray, /):
        """
        usage.scipy: 1
        """
        ...

    def __lt__(self, _0: object, /):
        """
        usage.dask: 1
        usage.matplotlib: 2
        usage.scipy: 8
        """
        ...

    @overload
    def __mul__(self, _0: numpy.float64, /):
        """
        usage.matplotlib: 3
        usage.scipy: 2
        usage.xarray: 1
        """
        ...

    @overload
    def __mul__(self, _0: numpy.float32, /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def __mul__(self, _0: numpy.ma.core.MaskedArray, /):
        """
        usage.dask: 2
        usage.matplotlib: 3
        usage.scipy: 13
        """
        ...

    @overload
    def __mul__(self, _0: numpy.ndarray, /):
        """
        usage.matplotlib: 5
        usage.scipy: 2
        """
        ...

    @overload
    def __mul__(self, _0: float, /):
        """
        usage.matplotlib: 3
        """
        ...

    @overload
    def __mul__(self, _0: int, /):
        """
        usage.dask: 1
        usage.matplotlib: 2
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

    @overload
    def __or__(self, _0: numpy.ndarray, /):
        """
        usage.matplotlib: 1
        """
        ...

    @overload
    def __or__(self, _0: numpy.ma.core.MaskedArray, /):
        """
        usage.matplotlib: 1
        """
        ...

    def __or__(self, _0: Union[numpy.ma.core.MaskedArray, numpy.ndarray], /):
        """
        usage.matplotlib: 2
        """
        ...

    @overload
    def __pow__(self, _0: int, /):
        """
        usage.dask: 2
        usage.matplotlib: 1
        usage.scipy: 7
        """
        ...

    @overload
    def __pow__(self, _0: float, /):
        """
        usage.scipy: 3
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
        usage.matplotlib: 1
        usage.xarray: 1
        """
        ...

    @overload
    def __radd__(self, _0: int, /):
        """
        usage.matplotlib: 1
        usage.scipy: 2
        """
        ...

    @overload
    def __radd__(self, _0: numpy.ma.core.MaskedArray, /):
        """
        usage.dask: 1
        usage.matplotlib: 4
        usage.scipy: 6
        """
        ...

    @overload
    def __radd__(self, _0: float, /):
        """
        usage.matplotlib: 1
        """
        ...

    @overload
    def __radd__(self, _0: dask.array.core.Array, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __radd__(self, _0: numpy.ndarray, /):
        """
        usage.dask: 1
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
    def __rand__(self, _0: numpy.ma.core.MaskedArray, /):
        """
        usage.matplotlib: 1
        usage.scipy: 1
        """
        ...

    @overload
    def __rand__(self, _0: numpy.ndarray, /):
        """
        usage.matplotlib: 2
        usage.scipy: 1
        """
        ...

    def __rand__(self, _0: Union[numpy.ndarray, numpy.ma.core.MaskedArray], /):
        """
        usage.matplotlib: 3
        usage.scipy: 2
        """
        ...

    @overload
    def __rmul__(self, _0: numpy.ma.core.MaskedArray, /):
        """
        usage.dask: 2
        usage.matplotlib: 3
        usage.scipy: 13
        """
        ...

    @overload
    def __rmul__(self, _0: numpy.ndarray, /):
        """
        usage.matplotlib: 1
        usage.scipy: 4
        """
        ...

    @overload
    def __rmul__(self, _0: float, /):
        """
        usage.matplotlib: 2
        usage.scipy: 6
        """
        ...

    @overload
    def __rmul__(self, _0: numpy.float64, /):
        """
        usage.matplotlib: 1
        """
        ...

    @overload
    def __rmul__(self, _0: int, /):
        """
        usage.matplotlib: 3
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
        usage.matplotlib: 2
        usage.scipy: 11
        usage.skimage: 2
        usage.sklearn: 1
        """
        ...

    @overload
    def __rsub__(self, _0: numpy.float64, /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def __rsub__(self, _0: numpy.ndarray, /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def __rsub__(self, _0: int, /):
        """
        usage.matplotlib: 1
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
        usage.scipy: 20
        usage.skimage: 1
        """
        ...

    @overload
    def __rtruediv__(self, _0: float, /):
        """
        usage.scipy: 3
        """
        ...

    @overload
    def __rtruediv__(self, _0: numpy.ndarray, /):
        """
        usage.scipy: 5
        """
        ...

    @overload
    def __rtruediv__(self, _0: int, /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def __rtruediv__(self, _0: numpy.float64, /):
        """
        usage.scipy: 2
        """
        ...

    @overload
    def __rtruediv__(self, _0: numpy.ma.core.MaskedConstant, /):
        """
        usage.scipy: 2
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
        self, _0: slice[None, None, None], _1: numpy.ma.core.MaskedConstant, /
    ):
        """
        usage.skimage: 4
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[int, int], _1: int, /):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[int, int, int], _1: int, /):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[int, int], _1: float, /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[numpy.bool_, int], _1: int, /):
        """
        usage.xarray: 3
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[numpy.ndarray, int], _1: int, /):
        """
        usage.xarray: 1
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
    def __setitem__(self, _0: numpy.ndarray, _1: numpy.ma.core.MaskedConstant, /):
        """
        usage.scipy: 8
        """
        ...

    @overload
    def __setitem__(self, _0: List[int], _1: numpy.ma.core.MaskedConstant, /):
        """
        usage.scipy: 2
        """
        ...

    @overload
    def __setitem__(self, _0: int, _1: numpy.int64, /):
        """
        usage.scipy: 8
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[int, int], _1: numpy.float64, /):
        """
        usage.scipy: 3
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[int, int], _1: numpy.int64, /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def __setitem__(self, _0: int, _1: numpy.float64, /):
        """
        usage.matplotlib: 4
        usage.scipy: 1
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: int, _1: numpy.ma.core.MaskedConstant, /):
        """
        usage.matplotlib: 6
        usage.scipy: 3
        """
        ...

    @overload
    def __setitem__(
        self, _0: slice[int, int, int], _1: numpy.ma.core.MaskedConstant, /
    ):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def __setitem__(self, _0: numpy.ndarray, _1: numpy.int64, /):
        """
        usage.scipy: 4
        """
        ...

    @overload
    def __setitem__(self, _0: numpy.ndarray, _1: numpy.float64, /):
        """
        usage.scipy: 3
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[int, slice[None, int, None]], _1: List[int], /):
        """
        usage.scipy: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[int, slice[None, int, None]], _1: List[float], /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[int, slice[None, int, None]], _1: numpy.ma.core.MaskedArray, /
    ):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: numpy.ma.core.MaskedArray, _1: numpy.ma.core.MaskedConstant, /
    ):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[int, slice[None, int, None]], _1: numpy.ndarray, /):
        """
        usage.scipy: 2
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[int, slice[None, None, None]], _1: numpy.ma.core.MaskedArray, /
    ):
        """
        usage.matplotlib: 2
        """
        ...

    @overload
    def __setitem__(
        self, _0: numpy.ma.core.MaskedArray, _1: numpy.ma.core.MaskedArray, /
    ):
        """
        usage.matplotlib: 4
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[ellipsis, int], _1: numpy.ma.core.MaskedArray, /):
        """
        usage.matplotlib: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[ellipsis, int], _1: int, /):
        """
        usage.matplotlib: 1
        """
        ...

    @overload
    def __setitem__(self, _0: numpy.ma.core.MaskedArray, _1: float, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(self, _0: int, _1: int, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: int, _1: float, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: int, _1: Literal["soft"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: int, _1: List[float], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: int, _1: Literal["hard"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: int, _1: Literal["SAMME"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: int, _1: Literal["SAMME.R"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: int, _1: Literal["hinge"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: int, _1: Tuple[int, int], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: int, _1: Literal["squared_hinge"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: int, _1: Literal["l1"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: int, _1: Literal["l2"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: int, _1: Literal["mean"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: int, _1: Literal["median"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: int, _1: Literal["most_frequent"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: int, _1: sklearn.linear_model._base.LinearRegression, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: int, _1: sklearn.linear_model._ridge.Ridge, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: int, _1: Literal["rbf"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: int, _1: Literal["poly"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: int, _1: None, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: int, _1: Literal["log"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: int, _1: bool, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: int, _1: Literal["modified_huber"], /):
        """
        usage.sklearn: 1
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
    def __sub__(self, _0: numpy.float64, /):
        """
        usage.matplotlib: 1
        usage.scipy: 6
        usage.skimage: 2
        """
        ...

    @overload
    def __sub__(self, _0: numpy.ma.core.MaskedArray, /):
        """
        usage.dask: 4
        usage.matplotlib: 2
        usage.scipy: 11
        usage.skimage: 2
        usage.sklearn: 1
        """
        ...

    @overload
    def __sub__(self, _0: int, /):
        """
        usage.dask: 1
        usage.scipy: 4
        """
        ...

    @overload
    def __sub__(self, _0: numpy.ma.core.MaskedConstant, /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def __sub__(self, _0: numpy.ndarray, /):
        """
        usage.matplotlib: 2
        usage.scipy: 5
        """
        ...

    @overload
    def __sub__(self, _0: float, /):
        """
        usage.matplotlib: 2
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
        usage.matplotlib: 1
        usage.scipy: 20
        usage.skimage: 1
        """
        ...

    @overload
    def __truediv__(self, _0: float, /):
        """
        usage.matplotlib: 2
        usage.scipy: 1
        """
        ...

    @overload
    def __truediv__(self, _0: numpy.float64, /):
        """
        usage.matplotlib: 1
        usage.scipy: 7
        """
        ...

    @overload
    def __truediv__(self, _0: numpy.ndarray, /):
        """
        usage.scipy: 4
        """
        ...

    @overload
    def __truediv__(self, _0: numpy.ma.core.MaskedConstant, /):
        """
        usage.scipy: 3
        """
        ...

    @overload
    def __truediv__(self, _0: numpy.int64, /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def __truediv__(self, _0: int, /):
        """
        usage.matplotlib: 4
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
        usage.matplotlib: 3
        """
        ...

    def argsort(self, /, axis: None):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def astype(self, _0: numpy.dtype, /):
        """
        usage.dask: 7
        usage.pandas: 2
        """
        ...

    @overload
    def astype(self, _0: Type[numpy.float64], /):
        """
        usage.matplotlib: 2
        usage.scipy: 3
        """
        ...

    @overload
    def astype(self, _0: Type[bool], /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def astype(self, _0: Type[float], /):
        """
        usage.scipy: 3
        """
        ...

    @overload
    def astype(self, _0: Literal["d"], /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def astype(self, _0: Type[numpy.uint8], /):
        """
        usage.matplotlib: 5
        """
        ...

    @overload
    def astype(self, _0: Type[numpy.int64], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def astype(self, _0: Literal["bool"], /):
        """
        usage.dask: 1
        """
        ...

    def astype(
        self, _0: Union[Literal["bool", "d"], Type[numpy.int64], type, numpy.dtype], /
    ):
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

    def copy(self, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def count(self, /, axis: int):
        """
        usage.scipy: 11
        """
        ...

    @overload
    def count(self, /, axis: None):
        """
        usage.scipy: 1
        """
        ...

    def count(self, /, axis: Union[None, int]):
        """
        usage.scipy: 12
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

    def fill(self, _0: int, /):
        """
        usage.matplotlib: 2
        """
        ...

    def filled(self, /, fill_value: float):
        """
        usage.scipy: 1
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

    def max(self, /, axis: int):
        """
        usage.matplotlib: 1
        """
        ...

    @overload
    def mean(self, /, axis: None):
        """
        usage.scipy: 4
        """
        ...

    @overload
    def mean(self, /, axis: int):
        """
        usage.scipy: 3
        """
        ...

    @overload
    def mean(self, /, axis: int, keepdims: bool):
        """
        usage.scipy: 4
        """
        ...

    @overload
    def mean(self, /, axis: None, keepdims: bool):
        """
        usage.scipy: 1
        """
        ...

    def mean(self, /, axis: Union[None, int], keepdims: bool = ...):
        """
        usage.scipy: 12
        """
        ...

    def min(self, /, axis: int):
        """
        usage.matplotlib: 1
        usage.sklearn: 2
        """
        ...

    def newbyteorder(self, /):
        """
        usage.matplotlib: 3
        """
        ...

    def repeat(self, /, *args: Literal["v", "t"]):
        """
        usage.matplotlib: 3
        """
        ...

    def reshape(self, /, *s: Literal["v", "t"]):
        """
        usage.dask: 1
        """
        ...

    def soften_mask(self, /):
        """
        usage.pandas: 4
        """
        ...

    @overload
    def std(self, /, ddof: int):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def std(self, /, axis: int, ddof: int):
        """
        usage.scipy: 3
        """
        ...

    @overload
    def std(self, /, axis: int, ddof: int, keepdims: bool):
        """
        usage.scipy: 2
        """
        ...

    def std(self, /, ddof: int, axis: int = ..., keepdims: bool = ...):
        """
        usage.scipy: 6
        """
        ...

    @overload
    def sum(self, /, axis: int):
        """
        usage.scipy: 1
        usage.sklearn: 1
        """
        ...

    @overload
    def sum(self, /, axis: None):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def sum(self, /, axis: Tuple[int, int], keepdims: bool):
        """
        usage.dask: 3
        """
        ...

    @overload
    def sum(self, /, axis: Tuple[int, int], dtype: numpy.dtype, keepdims: bool):
        """
        usage.dask: 6
        """
        ...

    @overload
    def sum(self, /, axis: Tuple[int], dtype: numpy.dtype, keepdims: bool):
        """
        usage.dask: 6
        """
        ...

    @overload
    def sum(self, /, axis: Tuple[int], keepdims: bool):
        """
        usage.dask: 3
        """
        ...

    @overload
    def sum(self, /, axis: Tuple[int, int], dtype: Literal["f8"], keepdims: bool):
        """
        usage.dask: 4
        """
        ...

    @overload
    def sum(self, /, axis: Tuple[int], dtype: Literal["f8"], keepdims: bool):
        """
        usage.dask: 4
        """
        ...

    def sum(
        self,
        /,
        axis: Union[int, None, Tuple[int, ...]],
        keepdims: bool = ...,
        dtype: Union[Literal["f8"], numpy.dtype] = ...,
    ):
        """
        usage.dask: 26
        usage.scipy: 2
        usage.sklearn: 1
        """
        ...

    @overload
    def var(self, /, ddof: int):
        """
        usage.scipy: 2
        """
        ...

    @overload
    def var(self, /, axis: int, ddof: int):
        """
        usage.scipy: 9
        """
        ...

    def var(self, /, ddof: int, axis: int = ...):
        """
        usage.scipy: 11
        """
        ...

    def view(self, /, dtype: Type[numpy.ma.mrecords.MaskedRecords] = ...):
        """
        usage.pandas: 4
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
        usage.matplotlib: 5
        usage.scipy: 1
        """
        ...

    @overload
    def __add__(self, _0: numpy.ma.core.MaskedConstant, /):
        """
        usage.matplotlib: 3
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

    def __getitem__(self, _0: Tuple[None, ...], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __gt__(self, _0: numpy.ma.core.MaskedArray, /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def __gt__(self, _0: numpy.int32, /):
        """
        usage.matplotlib: 1
        """
        ...

    def __gt__(self, _0: Union[numpy.int32, numpy.ma.core.MaskedArray], /):
        """
        usage.matplotlib: 1
        usage.scipy: 1
        """
        ...

    @overload
    def __lt__(self, _0: numpy.ma.core.MaskedArray, /):
        """
        usage.scipy: 2
        """
        ...

    @overload
    def __lt__(self, _0: numpy.int32, /):
        """
        usage.matplotlib: 1
        """
        ...

    def __lt__(self, _0: Union[numpy.int32, numpy.ma.core.MaskedArray], /):
        """
        usage.matplotlib: 1
        usage.scipy: 2
        """
        ...

    @overload
    def __mul__(self, _0: numpy.ma.core.MaskedConstant, /):
        """
        usage.scipy: 3
        """
        ...

    @overload
    def __mul__(self, _0: numpy.float64, /):
        """
        usage.matplotlib: 3
        usage.scipy: 1
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
    def __radd__(self, _0: numpy.ma.core.MaskedConstant, /):
        """
        usage.matplotlib: 3
        """
        ...

    @overload
    def __radd__(self, _0: numpy.float64, /):
        """
        usage.matplotlib: 3
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

    @overload
    def __rmul__(self, _0: numpy.ma.core.MaskedConstant, /):
        """
        usage.scipy: 3
        """
        ...

    @overload
    def __rmul__(self, _0: numpy.int64, /):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def __rmul__(self, _0: numpy.float64, /):
        """
        usage.scipy: 1
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

    @overload
    def __rtruediv__(self, _0: numpy.ma.core.MaskedConstant, /):
        """
        usage.scipy: 2
        """
        ...

    @overload
    def __rtruediv__(self, _0: numpy.float64, /):
        """
        usage.scipy: 3
        """
        ...

    @overload
    def __rtruediv__(self, _0: numpy.ma.core.MaskedArray, /):
        """
        usage.scipy: 3
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

    @overload
    def __truediv__(self, _0: numpy.ma.core.MaskedConstant, /):
        """
        usage.scipy: 2
        """
        ...

    @overload
    def __truediv__(self, _0: numpy.int64, /):
        """
        usage.scipy: 2
        """
        ...

    @overload
    def __truediv__(self, _0: numpy.ma.core.MaskedArray, /):
        """
        usage.scipy: 2
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

    @overload
    def astype(self, _0: numpy.dtype, /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def astype(self, _0: Literal["bool"], /):
        """
        usage.dask: 1
        """
        ...

    def astype(self, _0: Union[Literal["bool"], numpy.dtype], /):
        """
        usage.dask: 3
        """
        ...
