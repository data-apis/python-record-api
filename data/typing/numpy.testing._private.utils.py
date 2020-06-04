def assert_almost_equal(actual, desired, decimal: int = ...):
    "usage.skimage: 340"


def assert_equal(
    actual,
    desired,
    err_msg: Literal[
        (
            "Different regionprops are equal",
            "remove_small_holes in_place argument failed.",
            "remove_small_objects in_place argument failed.",
            "Same regionprops are not equal",
        )
    ] = ...,
):
    "usage.skimage: 664"


def assert_array_equal(x, y):
    "usage.skimage: 495"


def assert_allclose(
    actual: Union[(numpy.int64, numpy.float64, float, numpy.ndarray)],
    desired,
    rtol: float = ...,
    atol: Union[(int, float)] = ...,
):
    "usage.skimage: 169"


def assert_array_almost_equal(x, y, decimal: int = ...):
    "usage.skimage: 107"


def assert_warns(warning_class: list, *args: Literal[("v", "t")]):
    "usage.skimage: 5"


def assert_(
    val: Union[(numpy.bool_, bool)],
    msg: Literal[
        (
            "Maximum of `scharr` is larger than 1.",
            "Minimum of `roberts` is smaller than 0.",
            "Maximum of `farid` is larger than 1.",
            "Maximum of `sobel` is larger than 1.",
            "Minimum of `prewitt` is smaller than 0.",
            "Maximum of `prewitt` is larger than 1.",
            "Minimum of `farid` is smaller than 0.",
            "Minimum of `sobel` is smaller than 0.",
            "Minimum of `scharr` is smaller than 0.",
            "Maximum of `roberts` is larger than 1.",
        )
    ] = ...,
):
    "usage.skimage: 91"


def assert_array_less(
    x: Union[(numpy.float64, numpy.ndarray)],
    y: Union[(numpy.float64, float, numpy.ndarray)],
):
    "usage.skimage: 20"


def assert_array_almost_equal_nulp(
    x: Union[(numpy.ma.core.MaskedArray, numpy.ndarray)],
    y: Union[(numpy.ma.core.MaskedArray, numpy.float64, numpy.ndarray)],
):
    "usage.skimage: 4"


def assert_no_warnings():
    "usage.skimage: 1"
