from typing import *


def assert_(val: object):
    """
    usage.scipy: 1706
    usage.skimage: 78
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


def assert_array_almost_equal_nulp(
    x: object,
    y: Union[numpy.ndarray, numpy.ma.core.MaskedArray, float, int, numpy.float64],
):
    """
    usage.matplotlib: 1
    usage.scipy: 67
    usage.skimage: 4
    """
    ...


def assert_array_equal(x: object, y: object):
    """
    usage.dask: 36
    usage.matplotlib: 186
    usage.scipy: 1623
    usage.skimage: 430
    usage.sklearn: 1475
    usage.xarray: 400
    """
    ...


def assert_array_less(x: object, y: object):
    """
    usage.matplotlib: 3
    usage.scipy: 92
    usage.skimage: 20
    usage.sklearn: 18
    """
    ...


def assert_equal(actual: object, desired: object):
    """
    usage.dask: 26
    usage.matplotlib: 12
    usage.scipy: 4569
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


def assert_string_equal(actual: str, desired: str):
    """
    usage.scipy: 2
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

    def record(self, /, message: str):
        """
        usage.scipy: 11
        """
        ...
