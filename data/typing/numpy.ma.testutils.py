from typing import *


@overload
def assert_almost_equal(actual: numpy.ma.core.MaskedArray, desired: List[List[float]]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(actual: numpy.ndarray, desired: List[Union[int, float]]):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_almost_equal(actual: numpy.ndarray, desired: List[List[Union[int, float]]]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_almost_equal(actual: numpy.ndarray, desired: List[List[int]]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(actual: numpy.float64, desired: float):
    """
    usage.scipy: 17
    """
    ...


@overload
def assert_almost_equal(actual: numpy.float64, desired: numpy.float64):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_almost_equal(actual: numpy.ma.core.MaskedArray, desired: float):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_almost_equal(actual: numpy.ndarray, desired: List[float]):
    """
    usage.scipy: 11
    """
    ...


@overload
def assert_almost_equal(actual: numpy.float64, desired: float, decimal: int):
    """
    usage.scipy: 29
    """
    ...


@overload
def assert_almost_equal(actual: numpy.ma.core.MaskedArray, desired: List[float]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(actual: numpy.float64, desired: int, decimal: int):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.ma.core.MaskedArray, desired: float, decimal: int
):
    """
    usage.scipy: 5
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.ma.core.MaskedConstant, desired: numpy.ma.core.MaskedConstant
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.ma.core.MaskedArray, desired: numpy.ma.core.MaskedArray, decimal: int
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.ma.core.MaskedArray, desired: List[List[float]], decimal: int
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(actual: numpy.ndarray, desired: Tuple[float, float]):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_almost_equal(actual: numpy.float64, desired: int):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(actual: numpy.float64, desired: numpy.float64, decimal: int):
    """
    usage.scipy: 27
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: numpy.ma.core.MaskedArray, decimal: int
):
    """
    usage.scipy: 7
    """
    ...


@overload
def assert_almost_equal(
    actual: float, desired: numpy.ma.core.MaskedArray, decimal: int
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_almost_equal(actual: float, desired: numpy.float64, decimal: int):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_almost_equal(actual: numpy.ndarray, desired: numpy.ndarray, decimal: int):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_almost_equal(actual: float, desired: float, decimal: int):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(actual: numpy.ndarray, desired: numpy.ma.core.MaskedArray):
    """
    usage.scipy: 1
    """
    ...


def assert_almost_equal(
    actual: Union[
        numpy.ndarray,
        numpy.float64,
        numpy.ma.core.MaskedArray,
        numpy.ma.core.MaskedConstant,
        float,
    ],
    desired: object,
    decimal: int = ...,
):
    """
    usage.scipy: 131
    """
    ...


@overload
def assert_array_almost_equal(
    x: numpy.ma.core.MaskedArray, y: numpy.ma.core.MaskedArray
):
    """
    usage.matplotlib: 2
    usage.scipy: 2
    """
    ...


@overload
def assert_array_almost_equal(x: List[float], y: numpy.ndarray, decimal: int):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ndarray, y: numpy.ndarray):
    """
    usage.scipy: 5
    """
    ...


@overload
def assert_array_almost_equal(
    x: scipy.stats.mstats_basic.NormaltestResult, y: scipy.stats.stats.NormaltestResult
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_almost_equal(
    x: scipy.stats.mstats_basic.SkewtestResult, y: scipy.stats.stats.SkewtestResult
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_almost_equal(
    x: scipy.stats.mstats_basic.KurtosistestResult,
    y: scipy.stats.stats.KurtosistestResult,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_almost_equal(
    x: numpy.ma.core.MaskedArray, y: numpy.ndarray, decimal: int
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ma.core.MaskedArray, y: numpy.ndarray):
    """
    usage.matplotlib: 1
    """
    ...


def assert_array_almost_equal(
    x: object,
    y: Union[
        numpy.ndarray,
        numpy.ma.core.MaskedArray,
        scipy.stats.stats.KurtosistestResult,
        scipy.stats.stats.NormaltestResult,
        scipy.stats.stats.SkewtestResult,
    ],
    decimal: int = ...,
):
    """
    usage.matplotlib: 3
    usage.scipy: 13
    """
    ...


@overload
def assert_array_equal(x: numpy.ma.core.MaskedConstant, y: Tuple[float, float]):
    """
    usage.scipy: 5
    """
    ...


@overload
def assert_array_equal(x: numpy.ma.core.MaskedArray, y: Tuple[float, float]):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_array_equal(x: numpy.float64, y: numpy.ndarray):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.ma.core.MaskedArray, y: numpy.ndarray):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_array_equal(x: numpy.float64, y: Tuple[float, float]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(
    x: scipy.stats.mstats_basic.Ttest_indResult, y: Tuple[float, float]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.float64, y: float):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.ma.core.MaskedArray, y: list):
    """
    usage.scipy: 1
    """
    ...


def assert_array_equal(
    x: Union[
        numpy.ma.core.MaskedArray,
        scipy.stats.mstats_basic.Ttest_indResult,
        numpy.ma.core.MaskedConstant,
        numpy.float64,
    ],
    y: Union[list, Tuple[float, float], numpy.ndarray, float],
):
    """
    usage.scipy: 16
    """
    ...


@overload
def assert_equal(actual: numpy.dtype, desired: None):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(actual: numpy.float64, desired: numpy.float64):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_equal(actual: numpy.ma.core.MaskedArray, desired: numpy.ma.core.MaskedArray):
    """
    usage.scipy: 7
    """
    ...


@overload
def assert_equal(actual: numpy.ma.core.MaskedArray, desired: List[int]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(actual: numpy.ma.core.MaskedArray, desired: List[Union[None, int]]):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: List[int]):
    """
    usage.scipy: 7
    """
    ...


@overload
def assert_equal(actual: numpy.int64, desired: int):
    """
    usage.scipy: 5
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: numpy.ndarray):
    """
    usage.scipy: 15
    """
    ...


@overload
def assert_equal(actual: scipy.stats.mstats_basic.ModeResult, desired: Tuple[int, int]):
    """
    usage.scipy: 7
    """
    ...


@overload
def assert_equal(
    actual: scipy.stats.mstats_basic.ModeResult,
    desired: Tuple[List[List[int]], List[List[int]]],
):
    """
    usage.scipy: 6
    """
    ...


@overload
def assert_equal(actual: numpy.ma.core.MaskedArray, desired: float):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_equal(
    actual: Tuple[numpy.float64, numpy.float64], desired: Tuple[float, float]
):
    """
    usage.scipy: 5
    """
    ...


@overload
def assert_equal(
    actual: Tuple[numpy.float64, numpy.float64], desired: Tuple[float, int]
):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_equal(
    actual: Tuple[numpy.ma.core.MaskedArray, numpy.ma.core.MaskedArray],
    desired: Tuple[numpy.ma.core.MaskedArray, numpy.ma.core.MaskedArray],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: numpy.float64, desired: numpy.ma.core.MaskedArray):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(
    actual: scipy.stats.stats.RepeatedResults,
    desired: Tuple[numpy.ndarray, numpy.ndarray],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: scipy.stats.stats.KstestResult, desired: scipy.stats.stats.KstestResult
):
    """
    usage.scipy: 1
    """
    ...


def assert_equal(actual: object, desired: object):
    """
    usage.scipy: 75
    """
    ...
