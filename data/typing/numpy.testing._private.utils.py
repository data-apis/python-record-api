def assert_almost_equal(actual, desired=...):
    "usage.skimage: 340"


def assert_equal(actual, desired=...):
    "usage.skimage: 664\nusage.xarray: 21"


def assert_array_equal(x, y):
    "usage.skimage: 495\nusage.xarray: 307"


def assert_allclose(
    actual: Union[
        (
            float,
            pandas.core.indexes.range.RangeIndex,
            numpy.ndarray,
            numpy.float64,
            numpy.int64,
        )
    ],
    desired,
    rtol: float = ...,
    atol: Union[(int, float)] = ...,
):
    "usage.skimage: 169\nusage.xarray: 27"


def assert_array_almost_equal(x, y=...):
    "usage.skimage: 107"


def assert_warns(warning_class: list, *args: Literal[("v", "t")]):
    "usage.skimage: 5"


def assert_(val: Union[(numpy.bool_, bool)] = ...):
    "usage.skimage: 91"


def assert_array_less(
    x: Union[(numpy.ndarray, numpy.float64)],
    y: Union[(numpy.ndarray, float, numpy.float64)],
):
    "usage.skimage: 20"


def assert_array_almost_equal_nulp(
    x: Union[(numpy.ma.core.MaskedArray, numpy.ndarray)],
    y: Union[(numpy.ma.core.MaskedArray, numpy.ndarray, numpy.float64)],
):
    "usage.skimage: 4"


def assert_no_warnings():
    "usage.skimage: 1"
