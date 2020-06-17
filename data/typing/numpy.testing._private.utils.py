from typing import *


def assert_almost_equal(
    actual,
    desired,
    decimal: int = ...,
    err_msg: Literal[
        (
            "Point is not on expected circle",
            "Point is not on expected unit circle",
            "Unexpected std",
        )
    ] = ...,
):
    "usage.skimage: 340, usage.sklearn: 244"


def assert_equal(actual, desired=...):
    "usage.skimage: 664, usage.xarray: 21"


def assert_array_equal(x, y=...):
    "usage.skimage: 495, usage.xarray: 322, usage.sklearn: 562"


def assert_allclose(
    actual,
    desired,
    rtol: Union[(float, int)] = ...,
    atol: Union[(float, int)] = ...,
    err_msg: str = ...,
):
    "usage.skimage: 169, usage.xarray: 27, usage.sklearn: 307"


def assert_array_almost_equal(x, y, decimal: int = ..., err_msg: str = ...):
    "usage.skimage: 107, usage.sklearn: 641"


def assert_warns(warning_class: type, *args: Literal[("v", "t")]):
    "usage.skimage: 5"


def assert_(val: Union[(bool, numpy.bool_)] = ...):
    "usage.skimage: 91"


def assert_array_less(
    x: Union[(int, float, numpy.ndarray, numpy.float64)],
    y: Union[(numpy.ndarray, int, float, numpy.float64)],
):
    "usage.skimage: 20, usage.sklearn: 9"


def assert_array_almost_equal_nulp(
    x: Union[(numpy.ma.core.MaskedArray, numpy.ndarray)],
    y: Union[(numpy.float64, numpy.ndarray, numpy.ma.core.MaskedArray)],
):
    "usage.skimage: 4"


def assert_no_warnings():
    "usage.skimage: 1"


def assert_approx_equal(actual: numpy.float64, desired: numpy.float64 = ...):
    "usage.sklearn: 2"
