from typing import *


def assert_(val: Union[bool, numpy.bool_]):
    """
    usage.skimage: 78
    """
    ...


def assert_allclose(
    actual: object,
    desired: object,
    rtol: Union[int, float] = ...,
    atol: Union[int, float] = ...,
    err_msg: Union[str, numpy.ndarray] = ...,
):
    """
    usage.matplotlib: 184
    usage.skimage: 158
    usage.sklearn: 760
    usage.xarray: 38
    """
    ...


def assert_almost_equal(
    actual: object, desired: object, decimal: int = ..., err_msg: str = ...
):
    """
    usage.matplotlib: 50
    usage.skimage: 333
    usage.sklearn: 965
    """
    ...


def assert_approx_equal(actual: numpy.float64, desired: Union[numpy.float64, float]):
    """
    usage.matplotlib: 1
    usage.sklearn: 2
    """
    ...


def assert_array_almost_equal(
    x: object, y: object, decimal: Union[bool, int] = ..., err_msg: str = ...
):
    """
    usage.dask: 1
    usage.matplotlib: 86
    usage.skimage: 69
    usage.sklearn: 1569
    """
    ...


def assert_array_almost_equal_nulp(
    x: Union[numpy.ndarray, numpy.ma.core.MaskedArray],
    y: Union[numpy.ndarray, numpy.ma.core.MaskedArray, numpy.float64],
):
    """
    usage.matplotlib: 1
    usage.skimage: 4
    """
    ...


def assert_array_equal(x: object, y: object):
    """
    usage.dask: 36
    usage.matplotlib: 186
    usage.skimage: 430
    usage.sklearn: 1475
    usage.xarray: 400
    """
    ...


def assert_array_less(
    x: Union[numpy.ndarray, float, int, numpy.float64, numpy.ma.core.MaskedArray],
    y: Union[numpy.float64, float, numpy.ndarray, int],
):
    """
    usage.matplotlib: 3
    usage.skimage: 20
    usage.sklearn: 18
    """
    ...


def assert_equal(actual: object, desired: object):
    """
    usage.dask: 26
    usage.matplotlib: 12
    usage.skimage: 630
    usage.sklearn: 27
    usage.xarray: 40
    """
    ...


def assert_no_warnings(*args: Literal["v", "t"]):
    """
    usage.skimage: 1
    usage.sklearn: 1
    """
    ...


def assert_warns(warning_class: type, *args: Literal["v", "t"]):
    """
    usage.skimage: 5
    usage.sklearn: 1
    """
    ...
