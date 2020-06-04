def assert_almost_equal(actual, desired=...):
    "usage.skimage: 340"


def assert_equal(actual, desired=...):
    "usage.skimage: 664, usage.xarray: 21"


def assert_array_equal(x, y):
    "usage.skimage: 495, usage.xarray: 307"


def assert_allclose(
    actual: Union[
        (
            pandas.core.indexes.range.RangeIndex,
            float,
            numpy.float64,
            numpy.ndarray,
            numpy.int64,
        )
    ],
    desired,
    rtol: float = ...,
    atol: Union[(float, int)] = ...,
):
    "usage.skimage: 169, usage.xarray: 27"


def assert_array_almost_equal(x, y=...):
    "usage.skimage: 107"


def assert_warns(warning_class: list, *args: Literal[("v", "t")]):
    "usage.skimage: 5"


def assert_(val: Union[(bool, numpy.bool_)] = ...):
    "usage.skimage: 91"


def assert_array_less(
    x: Union[(numpy.float64, numpy.ndarray)],
    y: Union[(numpy.float64, numpy.ndarray, float)],
):
    "usage.skimage: 20"


def assert_array_almost_equal_nulp(
    x: Union[(numpy.ndarray, numpy.ma.core.MaskedArray)],
    y: Union[(numpy.float64, numpy.ndarray, numpy.ma.core.MaskedArray)],
):
    "usage.skimage: 4"


def assert_no_warnings():
    "usage.skimage: 1"
