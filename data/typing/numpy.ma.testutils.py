from typing import *


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
    x: object,
    y: Union[
        numpy.ndarray,
        scipy.stats.stats.SkewtestResult,
        numpy.ma.core.MaskedArray,
        scipy.stats.stats.NormaltestResult,
        scipy.stats.stats.KurtosistestResult,
    ],
    decimal: int = ...,
):
    """
    usage.scipy: 13
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ma.core.MaskedArray, y: numpy.ndarray):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def assert_array_almost_equal(
    x: numpy.ma.core.MaskedArray, y: numpy.ma.core.MaskedArray
):
    """
    usage.matplotlib: 2
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


def assert_equal(actual: object, desired: object):
    """
    usage.scipy: 75
    """
    ...
