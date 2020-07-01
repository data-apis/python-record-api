from typing import *


def assert_almost_equal(
    actual: object,
    desired: object,
    decimal: int = ...,
    err_msg: Literal[
        "Point is not on expected circle",
        "Point is not on expected unit circle",
        "Unexpected std",
    ] = ...,
):
    "\n    usage.skimage: 340\n    usage.sklearn: 244\n    "
    ...


def assert_equal(actual: object, desired: object):
    "\n    usage.skimage: 664\n    usage.xarray: 21\n    usage.dask: 26\n    "
    ...


def assert_array_equal(x: object, y: object):
    "\n    usage.skimage: 495\n    usage.xarray: 322\n    usage.sklearn: 562\n    usage.dask: 28\n    "
    ...


def assert_allclose(
    actual: object,
    desired: object,
    rtol: Union[float, int] = ...,
    atol: Union[float, int] = ...,
    err_msg: str = ...,
):
    "\n    usage.skimage: 169\n    usage.xarray: 27\n    usage.sklearn: 307\n    "
    ...


def assert_array_almost_equal(
    x: object, y: object, decimal: int = ..., err_msg: str = ...
):
    "\n    usage.skimage: 107\n    usage.sklearn: 641\n    usage.dask: 1\n    "
    ...


def assert_warns(warning_class: type, *args: Literal["v", "t"]):
    "\n    usage.skimage: 5\n    "
    ...


def assert_(val: Union[bool, numpy.bool_]):
    "\n    usage.skimage: 91\n    "
    ...


def assert_array_less(
    x: Union[int, float, numpy.ndarray, numpy.float64],
    y: Union[numpy.ndarray, int, float, numpy.float64],
):
    "\n    usage.skimage: 20\n    usage.sklearn: 9\n    "
    ...


def assert_array_almost_equal_nulp(
    x: Union[numpy.ma.core.MaskedArray, numpy.ndarray],
    y: Union[numpy.float64, numpy.ndarray, numpy.ma.core.MaskedArray],
):
    "\n    usage.skimage: 4\n    "
    ...


def assert_no_warnings():
    "\n    usage.skimage: 1\n    "
    ...


def assert_approx_equal(actual: numpy.float64, desired: numpy.float64):
    "\n    usage.sklearn: 2\n    "
    ...
