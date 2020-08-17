from typing import *


@overload
def assert_(val: numpy.bool_):
    """
    usage.skimage: 58
    """
    ...


@overload
def assert_(val: numpy.bool_, msg: str):
    """
    usage.skimage: 2
    """
    ...


@overload
def assert_(val: bool):
    """
    usage.skimage: 18
    """
    ...


@overload
def assert_(val: object, msg: object = ...):
    """
    usage.scipy: 1706
    """
    ...


def assert_(val: object, msg: object = ...):
    """
    usage.scipy: 1706
    usage.skimage: 78
    """
    ...


@overload
def assert_allclose(actual: numpy.float64, desired: int, atol: float):
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: int, atol: float):
    """
    usage.skimage: 15
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: numpy.ndarray, rtol: float):
    """
    usage.skimage: 11
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: numpy.ndarray):
    """
    usage.skimage: 57
    usage.xarray: 21
    """
    ...


@overload
def assert_allclose(actual: float, desired: float, atol: float):
    """
    usage.skimage: 3
    """
    ...


@overload
def assert_allclose(actual: float, desired: numpy.float64, atol: float):
    """
    usage.skimage: 3
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: List[float]):
    """
    usage.skimage: 6
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, rtol: float, atol: int
):
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: int):
    """
    usage.skimage: 22
    """
    ...


@overload
def assert_allclose(actual: numpy.float64, desired: numpy.float64):
    """
    usage.skimage: 2
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: numpy.ndarray, atol: float):
    """
    usage.skimage: 31
    """
    ...


@overload
def assert_allclose(actual: numpy.int64, desired: int, atol: float):
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.float64, desired: float, rtol: float):
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: Tuple[float, float]):
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.float64, desired: int):
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.float64, desired: int, rtol: float, atol: float):
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: List[numpy.float64], atol: float):
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: numpy.float64):
    """
    usage.xarray: 3
    """
    ...


@overload
def assert_allclose(
    actual: pandas.core.indexes.range.RangeIndex,
    desired: xarray.core.dataarray.DataArray,
):
    """
    usage.xarray: 7
    """
    ...


@overload
def assert_allclose(actual: numpy.float64, desired: float):
    """
    usage.xarray: 3
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: float):
    """
    usage.xarray: 1
    """
    ...


@overload
def assert_allclose(actual: object, desired: object):
    """
    usage.xarray: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.int64, desired: numpy.int64):
    """
    usage.xarray: 2
    """
    ...


@overload
def assert_allclose(
    actual: object,
    desired: object,
    rtol: Union[int, float, bool, numpy.float64] = ...,
    atol: Union[float, int, numpy.float128, numpy.float32, numpy.float64] = ...,
    err_msg: Union[
        str, float, Tuple[Union[complex, int, float, numpy.float64], ...]
    ] = ...,
    verbose: bool = ...,
):
    """
    usage.scipy: 4704
    """
    ...


@overload
def assert_allclose(
    actual: Union[
        Tuple[Union[numpy.float64, int, numpy.uint8], ...],
        numpy.ndarray,
        numpy.ma.core.MaskedArray,
        numpy.float64,
        List[Union[int, float, numpy.float64]],
    ],
    desired: object,
    rtol: float = ...,
    atol: float = ...,
    err_msg: numpy.ndarray = ...,
):
    """
    usage.matplotlib: 184
    """
    ...


@overload
def assert_allclose(
    actual: object,
    desired: object,
    rtol: Union[float, int] = ...,
    atol: Union[float, int] = ...,
    err_msg: str = ...,
):
    """
    usage.sklearn: 760
    """
    ...


def assert_allclose(
    actual: object,
    desired: object,
    rtol: Union[int, float, numpy.float64, bool] = ...,
    atol: Union[int, float, numpy.float64, numpy.float32, numpy.float128] = ...,
    err_msg: Union[
        str, Tuple[Union[complex, int, float, numpy.float64], ...], float, numpy.ndarray
    ] = ...,
    verbose: bool = ...,
):
    """
    usage.matplotlib: 184
    usage.scipy: 4704
    usage.skimage: 158
    usage.sklearn: 760
    usage.xarray: 38
    """
    ...


@overload
def assert_almost_equal(actual: numpy.float64, desired: int):
    """
    usage.skimage: 7
    """
    ...


@overload
def assert_almost_equal(actual: numpy.float64, desired: float):
    """
    usage.skimage: 47
    """
    ...


@overload
def assert_almost_equal(actual: numpy.ndarray, desired: numpy.ndarray, decimal: int):
    """
    usage.skimage: 15
    """
    ...


@overload
def assert_almost_equal(actual: numpy.float64, desired: float, decimal: int):
    """
    usage.skimage: 35
    """
    ...


@overload
def assert_almost_equal(actual: numpy.float64, desired: numpy.float64, decimal: int):
    """
    usage.skimage: 6
    """
    ...


@overload
def assert_almost_equal(actual: numpy.float16, desired: float, decimal: int):
    """
    usage.skimage: 2
    """
    ...


@overload
def assert_almost_equal(actual: numpy.ndarray, desired: numpy.ndarray):
    """
    usage.skimage: 116
    """
    ...


@overload
def assert_almost_equal(actual: numpy.ndarray, desired: int, decimal: int):
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_almost_equal(actual: numpy.ndarray, desired: List[int], decimal: int):
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_almost_equal(actual: numpy.ndarray, desired: numpy.float64, decimal: int):
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_almost_equal(actual: numpy.ndarray, desired: Tuple[int, int]):
    """
    usage.skimage: 12
    """
    ...


@overload
def assert_almost_equal(actual: numpy.float64, desired: int, decimal: int):
    """
    usage.skimage: 5
    """
    ...


@overload
def assert_almost_equal(actual: numpy.ndarray, desired: List[float]):
    """
    usage.skimage: 2
    """
    ...


@overload
def assert_almost_equal(actual: numpy.ndarray, desired: List[int]):
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_almost_equal(actual: numpy.float64, desired: numpy.float64):
    """
    usage.skimage: 21
    """
    ...


@overload
def assert_almost_equal(
    actual: Tuple[int, int, int],
    desired: Tuple[numpy.float64, numpy.float64, numpy.float64],
    decimal: int,
):
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_almost_equal(actual: numpy.ndarray, desired: int):
    """
    usage.skimage: 5
    """
    ...


@overload
def assert_almost_equal(actual: numpy.ndarray, desired: numpy.float64):
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_almost_equal(actual: Tuple[int, int], desired: List[float], decimal: int):
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: Tuple[int, int, int],
    desired: Tuple[numpy.float64, numpy.float64, numpy.float64],
):
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_almost_equal(actual: numpy.int64, desired: numpy.int64):
    """
    usage.skimage: 2
    """
    ...


@overload
def assert_almost_equal(
    actual: Tuple[int, int, int, int], desired: Tuple[int, int, int, int]
):
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_almost_equal(actual: int, desired: int):
    """
    usage.skimage: 3
    """
    ...


@overload
def assert_almost_equal(
    actual: Tuple[numpy.float64, numpy.float64],
    desired: Tuple[numpy.float64, numpy.float64],
):
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_almost_equal(actual: float, desired: float):
    """
    usage.skimage: 16
    """
    ...


@overload
def assert_almost_equal(actual: List[numpy.float64], desired: List[numpy.float64]):
    """
    usage.skimage: 2
    """
    ...


@overload
def assert_almost_equal(
    actual: Tuple[slice[int, int, int], slice[int, int, int]],
    desired: Tuple[slice[int, int, int], slice[int, int, int]],
):
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: Tuple[int, int, int, int, int, int],
    desired: Tuple[int, int, int, int, int, int],
):
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: Tuple[numpy.float64, numpy.float64, numpy.float64],
    desired: Tuple[numpy.float64, numpy.float64, numpy.float64],
):
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_almost_equal(actual: numpy.uint8, desired: numpy.uint8):
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: Tuple[slice[int, int, int], slice[int, int, int], slice[int, int, int]],
    desired: Tuple[slice[int, int, int], slice[int, int, int], slice[int, int, int]],
):
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_almost_equal(actual: numpy.int64, desired: int):
    """
    usage.skimage: 2
    """
    ...


@overload
def assert_almost_equal(actual: float, desired: numpy.float64, decimal: int):
    """
    usage.skimage: 3
    """
    ...


@overload
def assert_almost_equal(actual: float, desired: int):
    """
    usage.skimage: 8
    """
    ...


@overload
def assert_almost_equal(actual: Tuple[float, float], desired: Tuple[float, float]):
    """
    usage.skimage: 3
    """
    ...


@overload
def assert_almost_equal(actual: numpy.ndarray, desired: List[Union[int, float]]):
    """
    usage.skimage: 2
    """
    ...


@overload
def assert_almost_equal(actual: numpy.ndarray, desired: List[List[int]]):
    """
    usage.skimage: 4
    """
    ...


@overload
def assert_almost_equal(
    actual: object,
    desired: object,
    decimal: int = ...,
    verbose: bool = ...,
    err_msg: str = ...,
):
    """
    usage.scipy: 1344
    """
    ...


@overload
def assert_almost_equal(
    actual: Union[
        List[Union[numpy.float64, float]],
        Tuple[float, float],
        numpy.ndarray,
        numpy.float64,
        float,
    ],
    desired: Union[
        numpy.ndarray,
        numpy.float64,
        float,
        Tuple[Union[int, float], Union[int, float]],
        List[float],
    ],
    decimal: int = ...,
):
    """
    usage.matplotlib: 50
    """
    ...


@overload
def assert_almost_equal(
    actual: Union[numpy.ndarray, numpy.int64, numpy.float64, int, float],
    desired: object,
    decimal: int = ...,
    err_msg: str = ...,
):
    """
    usage.sklearn: 965
    """
    ...


def assert_almost_equal(
    actual: object,
    desired: object,
    decimal: int = ...,
    verbose: bool = ...,
    err_msg: str = ...,
):
    """
    usage.matplotlib: 50
    usage.scipy: 1344
    usage.skimage: 333
    usage.sklearn: 965
    """
    ...


@overload
def assert_approx_equal(
    actual: Union[numpy.float64, float],
    desired: Union[float, int, numpy.float64],
    significant: int = ...,
    err_msg: str = ...,
):
    """
    usage.scipy: 220
    """
    ...


@overload
def assert_approx_equal(actual: numpy.float64, desired: float):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def assert_approx_equal(
    actual: numpy.float64, desired: numpy.float64, significant: int = ...
):
    """
    usage.sklearn: 2
    """
    ...


def assert_approx_equal(
    actual: Union[numpy.float64, float],
    desired: Union[numpy.float64, int, float],
    significant: int = ...,
    err_msg: str = ...,
):
    """
    usage.matplotlib: 1
    usage.scipy: 220
    usage.sklearn: 2
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ndarray, y: List[List[Tuple[int, int, int]]]):
    """
    usage.skimage: 4
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ndarray, y: numpy.ndarray):
    """
    usage.skimage: 39
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ndarray, y: Tuple[int, int, int]):
    """
    usage.skimage: 2
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ndarray, y: List[int]):
    """
    usage.skimage: 6
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ndarray, y: List[Union[int, float]]):
    """
    usage.skimage: 3
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ndarray, y: List[float]):
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ndarray, y: List[Tuple[int, int]]):
    """
    usage.skimage: 2
    """
    ...


@overload
def assert_array_almost_equal(
    x: Tuple[int, int, int, int], y: Tuple[int, int, int, int]
):
    """
    usage.skimage: 2
    """
    ...


@overload
def assert_array_almost_equal(
    x: Tuple[int, int, int, int, int, int], y: Tuple[int, int, int, int, int, int]
):
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_array_almost_equal(x: int, y: int):
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_array_almost_equal(
    x: Tuple[numpy.float64, numpy.float64], y: Tuple[float, float]
):
    """
    usage.skimage: 2
    """
    ...


@overload
def assert_array_almost_equal(
    x: Tuple[numpy.float64, numpy.float64, numpy.float64], y: Tuple[float, float, float]
):
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ndarray, y: int):
    """
    usage.skimage: 5
    """
    ...


@overload
def assert_array_almost_equal(
    x: object, y: object, decimal: int = ..., err_msg: str = ...
):
    """
    usage.scipy: 3904
    """
    ...


@overload
def assert_array_almost_equal(
    x: Union[
        Tuple[Union[numpy.float32, numpy.float64], ...],
        List[Union[List[float], float, numpy.float64]],
        numpy.ndarray,
        numpy.ma.core.MaskedArray,
        numpy.float64,
    ],
    y: object,
    decimal: int = ...,
):
    """
    usage.matplotlib: 86
    """
    ...


@overload
def assert_array_almost_equal(x: dask.array.core.Array, y: numpy.ndarray):
    """
    usage.dask: 1
    """
    ...


@overload
def assert_array_almost_equal(
    x: object, y: object, decimal: Union[int, bool] = ..., err_msg: str = ...
):
    """
    usage.sklearn: 1569
    """
    ...


def assert_array_almost_equal(
    x: object, y: object, decimal: Union[bool, int] = ..., err_msg: str = ...
):
    """
    usage.dask: 1
    usage.matplotlib: 86
    usage.scipy: 3904
    usage.skimage: 69
    usage.sklearn: 1569
    """
    ...


@overload
def assert_array_almost_equal_nulp(x: numpy.ndarray, y: numpy.ndarray):
    """
    usage.matplotlib: 1
    usage.skimage: 1
    """
    ...


@overload
def assert_array_almost_equal_nulp(
    x: numpy.ma.core.MaskedArray, y: numpy.ma.core.MaskedArray
):
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_array_almost_equal_nulp(x: numpy.ma.core.MaskedArray, y: numpy.float64):
    """
    usage.skimage: 2
    """
    ...


@overload
def assert_array_almost_equal_nulp(
    x: Union[numpy.float64, numpy.matrix, int, float, numpy.ndarray],
    y: Union[float, numpy.ndarray, int, numpy.float64],
    nulp: Union[int, float] = ...,
):
    """
    usage.scipy: 67
    """
    ...


def assert_array_almost_equal_nulp(
    x: object,
    y: Union[numpy.ndarray, numpy.ma.core.MaskedArray, float, int, numpy.float64],
    nulp: Union[int, float] = ...,
):
    """
    usage.matplotlib: 1
    usage.scipy: 67
    usage.skimage: 4
    """
    ...


@overload
def assert_array_equal(x: List[int], y: List[int]):
    """
    usage.skimage: 6
    usage.xarray: 2
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: numpy.ndarray):
    """
    usage.skimage: 321
    usage.xarray: 164
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: int):
    """
    usage.skimage: 13
    """
    ...


@overload
def assert_array_equal(x: Tuple[numpy.uint8, numpy.uint8], y: List[int]):
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_array_equal(x: Tuple[int, int], y: List[int]):
    """
    usage.skimage: 2
    usage.xarray: 5
    """
    ...


@overload
def assert_array_equal(x: Tuple[numpy.float64, numpy.float64], y: List[float]):
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_array_equal(x: Tuple[float, float], y: List[float]):
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_array_equal(x: Tuple[int, int], y: Tuple[int, int]):
    """
    usage.skimage: 3
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: List[int]):
    """
    usage.skimage: 11
    usage.xarray: 7
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: Tuple[bool, bool, bool, bool]):
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: Tuple[float, float]):
    """
    usage.skimage: 3
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: Tuple[int, int]):
    """
    usage.skimage: 1
    usage.xarray: 2
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: List[List[List[Tuple[int, int]]]]):
    """
    usage.skimage: 3
    """
    ...


@overload
def assert_array_equal(x: List[Tuple[int, int]], y: List[Tuple[int, int]]):
    """
    usage.skimage: 8
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: List[List[int]]):
    """
    usage.skimage: 12
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: List[List[float]]):
    """
    usage.skimage: 6
    """
    ...


@overload
def assert_array_equal(x: int, y: int):
    """
    usage.skimage: 7
    usage.xarray: 1
    """
    ...


@overload
def assert_array_equal(x: skimage.util._map_array.ArrayMap, y: numpy.ndarray):
    """
    usage.skimage: 8
    """
    ...


@overload
def assert_array_equal(x: Tuple[int, int, int], y: Tuple[float, float, int]):
    """
    usage.skimage: 3
    """
    ...


@overload
def assert_array_equal(x: Tuple[int, int], y: Tuple[float, float]):
    """
    usage.skimage: 2
    """
    ...


@overload
def assert_array_equal(x: Tuple[int], y: numpy.ndarray):
    """
    usage.skimage: 4
    """
    ...


@overload
def assert_array_equal(x: Tuple[int, int], y: numpy.ndarray):
    """
    usage.skimage: 4
    """
    ...


@overload
def assert_array_equal(x: Tuple[int, int, int], y: numpy.ndarray):
    """
    usage.skimage: 4
    """
    ...


@overload
def assert_array_equal(x: Tuple[int, int, int, int], y: numpy.ndarray):
    """
    usage.skimage: 4
    """
    ...


@overload
def assert_array_equal(x: Tuple[int, int, int], y: Tuple[int, int, int]):
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_array_equal(x: netCDF4._netCDF4.Variable, y: numpy.ndarray):
    """
    usage.xarray: 1
    """
    ...


@overload
def assert_array_equal(x: Tuple[int], y: Tuple[int]):
    """
    usage.xarray: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.ma.core.MaskedArray, y: numpy.ma.core.MaskedArray):
    """
    usage.xarray: 2
    """
    ...


@overload
def assert_array_equal(
    x: List[Literal["strings", "of", "list"]], y: List[Literal["strings", "of", "list"]]
):
    """
    usage.xarray: 1
    """
    ...


@overload
def assert_array_equal(x: List[Literal["one element"]], y: Literal["one element"]):
    """
    usage.xarray: 1
    """
    ...


@overload
def assert_array_equal(x: Tuple[float, float, float], y: List[float]):
    """
    usage.xarray: 1
    """
    ...


@overload
def assert_array_equal(x: Tuple[float], y: List[float]):
    """
    usage.xarray: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: pandas.core.indexes.numeric.Int64Index):
    """
    usage.xarray: 3
    """
    ...


@overload
def assert_array_equal(
    x: pandas.core.indexes.datetimes.DatetimeIndex,
    y: pandas.core.indexes.datetimes.DatetimeIndex,
):
    """
    usage.xarray: 2
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: xarray.coding.strings.StackedBytesArray):
    """
    usage.xarray: 2
    """
    ...


@overload
def assert_array_equal(x: xarray.coding.strings.StackedBytesArray, y: numpy.ndarray):
    """
    usage.xarray: 2
    """
    ...


@overload
def assert_array_equal(x: int, y: numpy.int64):
    """
    usage.xarray: 2
    """
    ...


@overload
def assert_array_equal(x: List[int], y: numpy.ndarray):
    """
    usage.xarray: 4
    """
    ...


@overload
def assert_array_equal(x: List[List[int]], y: numpy.ndarray):
    """
    usage.xarray: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: numpy.int64):
    """
    usage.xarray: 1
    """
    ...


@overload
def assert_array_equal(x: List[float], y: numpy.ndarray):
    """
    usage.xarray: 3
    """
    ...


@overload
def assert_array_equal(x: numpy.int32, y: numpy.int64):
    """
    usage.xarray: 1
    """
    ...


@overload
def assert_array_equal(
    x: numpy.ndarray, y: pandas.core.indexes.datetimes.DatetimeIndex
):
    """
    usage.xarray: 3
    """
    ...


@overload
def assert_array_equal(x: numpy.timedelta64, y: numpy.ndarray):
    """
    usage.xarray: 2
    """
    ...


@overload
def assert_array_equal(
    x: Dict[Literal["attr"], Literal["da"]], y: Dict[Literal["attr"], Literal["da"]]
):
    """
    usage.xarray: 1
    """
    ...


@overload
def assert_array_equal(
    x: Dict[Literal["attr"], Literal["da_coord"]],
    y: Dict[Literal["attr"], Literal["da_coord"]],
):
    """
    usage.xarray: 1
    """
    ...


@overload
def assert_array_equal(
    x: Dict[Literal["attr"], Literal["ds"]], y: Dict[Literal["attr"], Literal["ds"]]
):
    """
    usage.xarray: 1
    """
    ...


@overload
def assert_array_equal(x: xarray.conventions.BoolTypeArray, y: numpy.ndarray):
    """
    usage.xarray: 1
    """
    ...


@overload
def assert_array_equal(x: xarray.conventions.NativeEndiannessArray, y: numpy.ndarray):
    """
    usage.xarray: 1
    """
    ...


@overload
def assert_array_equal(
    x: numpy.ndarray, y: List[Literal["2265-10-28T00:00:00", "2000-01-01T00:00:00"]]
):
    """
    usage.xarray: 1
    """
    ...


@overload
def assert_array_equal(
    x: xarray.core.variable.Variable, y: xarray.core.dataarray.DataArray
):
    """
    usage.xarray: 1
    """
    ...


@overload
def assert_array_equal(x: xarray.core.dataarray.DataArray, y: numpy.ndarray):
    """
    usage.xarray: 6
    """
    ...


@overload
def assert_array_equal(
    x: xarray.core.dataarray.DataArray, y: xarray.core.variable.Variable
):
    """
    usage.xarray: 7
    """
    ...


@overload
def assert_array_equal(
    x: xarray.core.dataarray.DataArray, y: xarray.core.dataarray.DataArray
):
    """
    usage.xarray: 9
    """
    ...


@overload
def assert_array_equal(x: range, y: List[int]):
    """
    usage.xarray: 2
    """
    ...


@overload
def assert_array_equal(
    x: pandas.core.indexes.base.Index, y: pandas.core.indexes.base.Index
):
    """
    usage.xarray: 3
    """
    ...


@overload
def assert_array_equal(x: Literal["x"], y: Literal["x"]):
    """
    usage.xarray: 1
    """
    ...


@overload
def assert_array_equal(
    x: pandas.core.indexes.base.Index, y: List[Literal["c", "b", "a"]]
):
    """
    usage.xarray: 1
    """
    ...


@overload
def assert_array_equal(x: pandas.core.indexes.numeric.Int64Index, y: List[int]):
    """
    usage.xarray: 5
    """
    ...


@overload
def assert_array_equal(x: Literal["foo"], y: Literal["foo"]):
    """
    usage.xarray: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.ma.core.MaskedArray, y: numpy.ndarray):
    """
    usage.xarray: 1
    """
    ...


@overload
def assert_array_equal(x: xarray.core.dataarray.DataArray, y: numpy.float64):
    """
    usage.xarray: 3
    """
    ...


@overload
def assert_array_equal(
    x: xarray.core.dataarray.DataArray, y: pandas.core.series.Series
):
    """
    usage.xarray: 1
    """
    ...


@overload
def assert_array_equal(x: xarray.core.dataarray.DataArray, y: List[Literal["b", "a"]]):
    """
    usage.xarray: 2
    """
    ...


@overload
def assert_array_equal(x: xarray.core.dataarray.DataArray, y: List[str]):
    """
    usage.xarray: 2
    """
    ...


@overload
def assert_array_equal(x: xarray.core.dataarray.DataArray, y: List[Literal["b"]]):
    """
    usage.xarray: 3
    """
    ...


@overload
def assert_array_equal(x: xarray.core.dataarray.DataArray, y: List[int]):
    """
    usage.xarray: 2
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: Literal["DJF"]):
    """
    usage.xarray: 1
    """
    ...


@overload
def assert_array_equal(
    x: List[Literal["SON", "JJA", "MAM", "DJF"]], y: xarray.core.dataarray.DataArray
):
    """
    usage.xarray: 1
    """
    ...


@overload
def assert_array_equal(
    x: xarray.core.dataarray.DataArray, y: xarray.coding.cftimeindex.CFTimeIndex
):
    """
    usage.xarray: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: xarray.core.dataarray.DataArray):
    """
    usage.xarray: 1
    """
    ...


@overload
def assert_array_equal(x: dask.array.core.Array, y: numpy.ndarray):
    """
    usage.xarray: 4
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: numpy.float64):
    """
    usage.xarray: 2
    """
    ...


@overload
def assert_array_equal(x: None, y: None):
    """
    usage.xarray: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: List[bool]):
    """
    usage.xarray: 1
    """
    ...


@overload
def assert_array_equal(
    x: slice[numpy.int64, numpy.int64, numpy.int64], y: slice[int, int, int]
):
    """
    usage.xarray: 1
    """
    ...


@overload
def assert_array_equal(
    x: pandas.core.indexes.multi.MultiIndex, y: pandas.core.indexes.multi.MultiIndex
):
    """
    usage.xarray: 2
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: xarray.core.variable.Variable):
    """
    usage.xarray: 2
    """
    ...


@overload
def assert_array_equal(
    x: xarray.core.variable.Variable, y: xarray.core.variable.Variable
):
    """
    usage.xarray: 9
    """
    ...


@overload
def assert_array_equal(x: xarray.core.indexing.CopyOnWriteArray, y: numpy.ndarray):
    """
    usage.xarray: 3
    """
    ...


@overload
def assert_array_equal(x: xarray.core.indexing.MemoryCachedArray, y: numpy.ndarray):
    """
    usage.xarray: 2
    """
    ...


@overload
def assert_array_equal(x: Tuple[numpy.ndarray], y: List[numpy.ndarray]):
    """
    usage.xarray: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.float64, y: numpy.float64):
    """
    usage.xarray: 2
    """
    ...


@overload
def assert_array_equal(x: bool, y: bool):
    """
    usage.xarray: 2
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: dask.array.core.Array):
    """
    usage.xarray: 2
    """
    ...


@overload
def assert_array_equal(
    x: pandas.core.indexes.datetimes.DatetimeIndex, y: numpy.ndarray
):
    """
    usage.xarray: 1
    """
    ...


@overload
def assert_array_equal(x: int, y: numpy.float64):
    """
    usage.xarray: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.float64, y: float):
    """
    usage.xarray: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.int32, y: int):
    """
    usage.xarray: 1
    """
    ...


@overload
def assert_array_equal(x: xarray.core.variable.Variable, y: numpy.ndarray):
    """
    usage.xarray: 38
    """
    ...


@overload
def assert_array_equal(x: xarray.core.variable.Variable, y: numpy.int64):
    """
    usage.xarray: 9
    """
    ...


@overload
def assert_array_equal(x: object, y: numpy.ndarray):
    """
    usage.xarray: 3
    """
    ...


@overload
def assert_array_equal(x: xarray.core.variable.Variable, y: object):
    """
    usage.xarray: 23
    """
    ...


@overload
def assert_array_equal(
    x: pandas.core.indexes.timedeltas.TimedeltaIndex,
    y: pandas.core.indexes.timedeltas.TimedeltaIndex,
):
    """
    usage.xarray: 1
    """
    ...


@overload
def assert_array_equal(
    x: xarray.coding.cftimeindex.CFTimeIndex, y: xarray.coding.cftimeindex.CFTimeIndex
):
    """
    usage.xarray: 1
    """
    ...


@overload
def assert_array_equal(x: pandas.core.indexes.frozen.FrozenList, y: List[List[int]]):
    """
    usage.xarray: 2
    """
    ...


@overload
def assert_array_equal(x: pandas.core.indexes.base.Index, y: List[Literal["a", "b"]]):
    """
    usage.xarray: 2
    """
    ...


@overload
def assert_array_equal(x: xarray.core.variable.IndexVariable, y: numpy.ndarray):
    """
    usage.xarray: 4
    """
    ...


@overload
def assert_array_equal(
    x: xarray.core.variable.IndexVariable, y: xarray.core.variable.Variable
):
    """
    usage.xarray: 1
    """
    ...


@overload
def assert_array_equal(x: xarray.core.variable.IndexVariable, y: numpy.int64):
    """
    usage.xarray: 2
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: xarray.core.variable.IndexVariable):
    """
    usage.xarray: 1
    """
    ...


@overload
def assert_array_equal(x: object, y: object, err_msg: str = ...):
    """
    usage.scipy: 1623
    usage.sklearn: 1475
    """
    ...


@overload
def assert_array_equal(
    x: Union[
        numpy.ndarray,
        int,
        numpy.ma.core.MaskedArray,
        Tuple[numpy.float64, ...],
        List[
            Union[
                List[numpy.ndarray],
                int,
                float,
                numpy.ndarray,
                Literal[
                    "2000-10-31T11:50:23",
                    "2054-06-20T14:31:45",
                    "1983-07-09T17:17:34",
                    "1976-03-05T00:00:01",
                    "2014-01-11T00:00:00",
                ],
            ]
        ],
    ],
    y: object,
):
    """
    usage.matplotlib: 186
    """
    ...


@overload
def assert_array_equal(
    x: Union[numpy.ndarray, dask.array.core.Array, dask.dataframe.core.Index],
    y: Union[numpy.ndarray, List[int]],
):
    """
    usage.dask: 36
    """
    ...


def assert_array_equal(x: object, y: object, err_msg: str = ...):
    """
    usage.dask: 36
    usage.matplotlib: 186
    usage.scipy: 1623
    usage.skimage: 430
    usage.sklearn: 1475
    usage.xarray: 400
    """
    ...


@overload
def assert_array_less(x: numpy.float64, y: numpy.float64):
    """
    usage.skimage: 16
    """
    ...


@overload
def assert_array_less(x: numpy.ndarray, y: numpy.ndarray):
    """
    usage.skimage: 2
    """
    ...


@overload
def assert_array_less(x: numpy.float64, y: float):
    """
    usage.skimage: 2
    """
    ...


@overload
def assert_array_less(x: object, y: object, err_msg: str = ...):
    """
    usage.scipy: 92
    """
    ...


@overload
def assert_array_less(x: numpy.ma.core.MaskedArray, y: float):
    """
    usage.matplotlib: 3
    """
    ...


@overload
def assert_array_less(
    x: Union[numpy.float64, int, float, numpy.ndarray],
    y: Union[int, numpy.ndarray, float, numpy.float64],
    err_msg: str = ...,
):
    """
    usage.sklearn: 18
    """
    ...


def assert_array_less(x: object, y: object, err_msg: str = ...):
    """
    usage.matplotlib: 3
    usage.scipy: 92
    usage.skimage: 20
    usage.sklearn: 18
    """
    ...


@overload
def assert_equal(actual: numpy.float64, desired: float):
    """
    usage.skimage: 10
    usage.xarray: 1
    """
    ...


@overload
def assert_equal(actual: int, desired: int):
    """
    usage.skimage: 68
    """
    ...


@overload
def assert_equal(actual: numpy.float64, desired: numpy.float64):
    """
    usage.skimage: 7
    """
    ...


@overload
def assert_equal(actual: numpy.int64, desired: int):
    """
    usage.skimage: 19
    usage.xarray: 1
    """
    ...


@overload
def assert_equal(actual: str, desired: str):
    """
    usage.skimage: 4
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: numpy.ndarray):
    """
    usage.skimage: 241
    usage.xarray: 3
    """
    ...


@overload
def assert_equal(actual: Tuple[int, int, int], desired: Tuple[int, int, int]):
    """
    usage.skimage: 20
    """
    ...


@overload
def assert_equal(actual: numpy.dtype, desired: numpy.dtype):
    """
    usage.skimage: 4
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: List[int]):
    """
    usage.skimage: 21
    """
    ...


@overload
def assert_equal(actual: numpy.float64, desired: int):
    """
    usage.skimage: 27
    """
    ...


@overload
def assert_equal(actual: numpy.uint8, desired: int):
    """
    usage.skimage: 9
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: float):
    """
    usage.skimage: 3
    usage.xarray: 2
    """
    ...


@overload
def assert_equal(actual: Tuple[int, int, int, int], desired: Tuple[int, int, int, int]):
    """
    usage.skimage: 7
    """
    ...


@overload
def assert_equal(
    actual: Tuple[int, int, int, int, int], desired: Tuple[int, int, int, int, int]
):
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_equal(actual: Tuple[numpy.ndarray, numpy.ndarray], desired: List[List[int]]):
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_equal(
    actual: Tuple[numpy.ndarray, numpy.ndarray], desired: List[List[Union[float, int]]]
):
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_equal(actual: Tuple[int], desired: Tuple[int]):
    """
    usage.skimage: 4
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: List[List[int]]):
    """
    usage.skimage: 8
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: Tuple[int, int]):
    """
    usage.skimage: 2
    """
    ...


@overload
def assert_equal(
    actual: Tuple[numpy.int64, numpy.int64, numpy.int64], desired: Tuple[int, int, int]
):
    """
    usage.skimage: 2
    """
    ...


@overload
def assert_equal(actual: Tuple[numpy.int64, numpy.int64], desired: Tuple[int, int]):
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_equal(actual: Tuple[int, int], desired: Tuple[int, int]):
    """
    usage.skimage: 40
    """
    ...


@overload
def assert_equal(actual: None, desired: None):
    """
    usage.skimage: 6
    """
    ...


@overload
def assert_equal(
    actual: List[Union[Literal["a", "z"], int]],
    desired: List[Union[Literal["a", "z"], int]],
):
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_equal(actual: List[str], desired: List[str]):
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_equal(actual: Type[numpy.ndarray], desired: Type[numpy.ndarray]):
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_equal(actual: Literal["pil"], desired: Literal["pil"]):
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_equal(actual: Literal["matplotlib"], desired: Literal["matplotlib"]):
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_equal(actual: int, desired: numpy.ndarray):
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: int):
    """
    usage.skimage: 56
    usage.xarray: 2
    """
    ...


@overload
def assert_equal(actual: float, desired: float):
    """
    usage.skimage: 2
    """
    ...


@overload
def assert_equal(
    actual: Tuple[slice[int, int, int], slice[int, int, int]],
    desired: Tuple[slice[int, int, int], slice[int, int, int]],
):
    """
    usage.skimage: 2
    """
    ...


@overload
def assert_equal(actual: numpy.int64, desired: numpy.int64):
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_equal(actual: List[numpy.float64], desired: List[numpy.float64]):
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_equal(
    actual: Tuple[numpy.float64, numpy.float64],
    desired: Tuple[numpy.float64, numpy.float64],
):
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_equal(actual: bool, desired: bool, err_msg: str):
    """
    usage.skimage: 4
    """
    ...


@overload
def assert_equal(actual: numpy.dtype, desired: Type[bool]):
    """
    usage.skimage: 4
    """
    ...


@overload
def assert_equal(actual: numpy.dtype, desired: Type[numpy.uint8]):
    """
    usage.skimage: 5
    """
    ...


@overload
def assert_equal(actual: numpy.uint8, desired: numpy.uint8):
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_equal(actual: numpy.int64, desired: numpy.ndarray):
    """
    usage.skimage: 3
    """
    ...


@overload
def assert_equal(actual: numpy.uint64, desired: numpy.uint64):
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_equal(actual: numpy.uint64, desired: numpy.ndarray):
    """
    usage.skimage: 4
    """
    ...


@overload
def assert_equal(actual: numpy.uint8, desired: numpy.ndarray):
    """
    usage.skimage: 2
    """
    ...


@overload
def assert_equal(actual: Tuple[int], desired: numpy.ndarray):
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_equal(actual: Tuple[int, int], desired: numpy.ndarray):
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_equal(actual: Tuple[int, int, int], desired: numpy.ndarray):
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_equal(actual: Tuple[int, int, int, int], desired: numpy.ndarray):
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_equal(actual: Tuple[int, int, int, int, int], desired: numpy.ndarray):
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_equal(actual: numpy.int16, desired: int):
    """
    usage.skimage: 2
    """
    ...


@overload
def assert_equal(actual: numpy.float32, desired: int):
    """
    usage.skimage: 2
    """
    ...


@overload
def assert_equal(actual: numpy.float32, desired: float):
    """
    usage.skimage: 4
    """
    ...


@overload
def assert_equal(actual: numpy.uint16, desired: int):
    """
    usage.skimage: 2
    """
    ...


@overload
def assert_equal(actual: numpy.uint32, desired: int):
    """
    usage.skimage: 2
    """
    ...


@overload
def assert_equal(actual: numpy.int32, desired: int):
    """
    usage.skimage: 2
    """
    ...


@overload
def assert_equal(actual: numpy.int8, desired: int):
    """
    usage.skimage: 2
    """
    ...


@overload
def assert_equal(
    actual: Tuple[slice[None, None, None], slice[None, None, None]],
    desired: List[slice[None, None, None]],
):
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_equal(actual: int, desired: numpy.float64):
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_equal(
    actual: Tuple[
        slice[numpy.int64, None, numpy.int64], slice[numpy.int64, None, numpy.int64]
    ],
    desired: List[slice[float, None, float]],
):
    """
    usage.skimage: 2
    """
    ...


@overload
def assert_equal(
    actual: Tuple[
        slice[numpy.int64, None, numpy.int64],
        slice[numpy.int64, None, numpy.int64],
        slice[numpy.int64, None, numpy.int64],
    ],
    desired: List[slice[float, None, float]],
):
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_equal(
    actual: Tuple[int, int, int, int, int, int],
    desired: Tuple[int, int, int, int, int, int],
):
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: List[List[List[List[int]]]]):
    """
    usage.skimage: 4
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: List[cftime._cftime.DatetimeNoLeap]):
    """
    usage.xarray: 3
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: list):
    """
    usage.xarray: 1
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: List[cftime._cftime.Datetime360Day]):
    """
    usage.xarray: 3
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: List[cftime._cftime.DatetimeJulian]):
    """
    usage.xarray: 3
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: List[cftime._cftime.DatetimeAllLeap]):
    """
    usage.xarray: 3
    """
    ...


@overload
def assert_equal(
    actual: numpy.ndarray, desired: List[cftime._cftime.DatetimeGregorian]
):
    """
    usage.xarray: 3
    """
    ...


@overload
def assert_equal(
    actual: numpy.ndarray, desired: List[cftime._cftime.DatetimeProlepticGregorian]
):
    """
    usage.xarray: 2
    """
    ...


@overload
def assert_equal(actual: xarray.core.dataarray.DataArray, desired: numpy.ndarray):
    """
    usage.xarray: 1
    """
    ...


@overload
def assert_equal(actual: numpy.int32, desired: numpy.int32):
    """
    usage.xarray: 1
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: numpy.int32):
    """
    usage.xarray: 1
    """
    ...


@overload
def assert_equal(actual: numpy.float32, desired: numpy.float32):
    """
    usage.xarray: 1
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: numpy.float32):
    """
    usage.xarray: 1
    """
    ...


@overload
def assert_equal(actual: object, desired: object):
    """
    usage.xarray: 1
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: object):
    """
    usage.xarray: 1
    """
    ...


@overload
def assert_equal(actual: numpy.str_, desired: Literal["foo"]):
    """
    usage.xarray: 1
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: Literal["foo"]):
    """
    usage.xarray: 1
    """
    ...


@overload
def assert_equal(actual: numpy.datetime64, desired: numpy.datetime64):
    """
    usage.xarray: 2
    """
    ...


@overload
def assert_equal(actual: numpy.timedelta64, desired: numpy.timedelta64):
    """
    usage.xarray: 2
    """
    ...


@overload
def assert_equal(
    actual: object, desired: object, err_msg: Union[str, int] = ..., verbose: bool = ...
):
    """
    usage.scipy: 4569
    """
    ...


@overload
def assert_equal(
    actual: Union[
        List[Union[numpy.ndarray, numpy.float64, float]], numpy.ndarray, float
    ],
    desired: Union[
        numpy.ndarray, numpy.float64, List[Union[bool, numpy.float64, float]]
    ],
):
    """
    usage.matplotlib: 12
    """
    ...


@overload
def assert_equal(
    actual: Union[
        numpy.ndarray,
        numpy.bool_,
        Dict[
            Tuple[Union[int, Literal["y"]], ...],
            Tuple[
                Callable,
                Tuple[Union[Literal["x"], int, numpy.int64], ...],
                Tuple[Union[slice[None, None, None], numpy.ndarray], ...],
            ],
        ],
        List[
            Tuple[
                Tuple[Union[Literal["y"], int], ...],
                Tuple[
                    Callable,
                    Tuple[Union[Literal["x"], numpy.int64, int], ...],
                    Tuple[Union[numpy.ndarray, slice[None, None, None]], ...],
                ],
            ]
        ],
        Tuple[
            Union[
                Tuple[Union[None, Literal["e", "d", "y"]], ...],
                List[Tuple[Union[None, str], ...]],
                float,
                int,
            ],
            ...,
        ],
    ],
    desired: Union[
        numpy.ndarray,
        numpy.bool_,
        Dict[
            Tuple[Union[int, Literal["y"]], ...],
            Tuple[
                Callable,
                Tuple[Union[Literal["x"], int, numpy.int64], ...],
                Tuple[Union[slice[None, None, None], List[int], numpy.ndarray], ...],
            ],
        ],
        List[
            Union[
                int,
                Tuple[
                    Tuple[Union[Literal["y"], int], ...],
                    Tuple[
                        Callable,
                        Tuple[Union[Literal["x"], int], ...],
                        Tuple[Union[numpy.ndarray, slice[None, None, None]], ...],
                    ],
                ],
            ]
        ],
        Tuple[
            Union[
                Tuple[Union[None, Literal["e", "d", "y"]], ...],
                List[Tuple[Union[None, str], ...]],
                float,
                int,
            ],
            ...,
        ],
    ],
):
    """
    usage.dask: 26
    """
    ...


@overload
def assert_equal(
    actual: Union[
        List[Union[float, Tuple[numpy.ndarray, numpy.ndarray]]],
        numpy.ndarray,
        Dict[
            str,
            Union[
                List[
                    Dict[
                        Literal["kernel", "gamma", "C", "degree"],
                        Union[int, float, numpy.float64, Literal["rbf", "poly"]],
                    ]
                ],
                numpy.ma.core.MaskedArray,
                numpy.ndarray,
            ],
        ],
    ],
    desired: Union[
        List[Union[Tuple[numpy.ndarray, numpy.ndarray], float]],
        Dict[
            str,
            Union[
                List[
                    Dict[
                        Literal["kernel", "gamma", "C", "degree"],
                        Union[int, float, numpy.float64, Literal["rbf", "poly"]],
                    ]
                ],
                numpy.ma.core.MaskedArray,
                numpy.ndarray,
            ],
        ],
        numpy.ndarray,
    ],
):
    """
    usage.sklearn: 27
    """
    ...


def assert_equal(
    actual: object, desired: object, err_msg: Union[int, str] = ..., verbose: bool = ...
):
    """
    usage.dask: 26
    usage.matplotlib: 12
    usage.scipy: 4569
    usage.skimage: 630
    usage.sklearn: 27
    usage.xarray: 40
    """
    ...


@overload
def assert_no_warnings():
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_no_warnings(*args: Literal["v", "t"]):
    """
    usage.sklearn: 1
    """
    ...


def assert_no_warnings(*args: Literal["v", "t"]):
    """
    usage.skimage: 1
    usage.sklearn: 1
    """
    ...


def assert_string_equal(actual: str, desired: str):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_warns(warning_class: Type[UserWarning], *args: Literal["v", "t"]):
    """
    usage.skimage: 3
    """
    ...


@overload
def assert_warns(warning_class: Type[FutureWarning], *args: Literal["v", "t"]):
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_warns(warning_class: Type[RuntimeWarning]):
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_warns(warning_class: type, *args: Literal["v", "t"]):
    """
    usage.scipy: 39
    """
    ...


@overload
def assert_warns(
    warning_class: Type[sklearn.exceptions.ConvergenceWarning], *args: Literal["v", "t"]
):
    """
    usage.sklearn: 1
    """
    ...


def assert_warns(warning_class: type, *args: Literal["v", "t"]):
    """
    usage.scipy: 39
    usage.skimage: 5
    usage.sklearn: 1
    """
    ...


class suppress_warnings:
    def filter(self, /, category: type = ..., message: str = ...):
        """
        usage.scipy: 298
        """
        ...

    def record(self, /, message: str, category: type = ...):
        """
        usage.scipy: 11
        """
        ...
