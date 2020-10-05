from typing import *


@overload
def assert_(val: numpy.bool_):
    """
    usage.scipy: 503
    usage.skimage: 58
    """
    ...


@overload
def assert_(val: numpy.bool_, msg: str):
    """
    usage.scipy: 40
    usage.skimage: 2
    """
    ...


@overload
def assert_(val: bool):
    """
    usage.scipy: 901
    usage.skimage: 18
    """
    ...


@overload
def assert_(val: bool, msg: Literal["1.5.1"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_(val: bool, msg: Literal[""]):
    """
    usage.scipy: 15
    """
    ...


@overload
def assert_(val: bool, msg: str):
    """
    usage.scipy: 84
    """
    ...


@overload
def assert_(
    val: bool,
    msg: Tuple[scipy.integrate.tests.test_integrate.SimpleOscillator, Literal["adams"]],
):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_(
    val: bool,
    msg: Tuple[scipy.integrate.tests.test_integrate.SimpleOscillator, Literal["bdf"]],
):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_(
    val: bool,
    msg: Tuple[scipy.integrate.tests.test_integrate.CoupledDecay, Literal["bdf"]],
):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_(
    val: bool,
    msg: Tuple[scipy.integrate.tests.test_integrate.ComplexExp, Literal["adams"]],
):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_(
    val: bool,
    msg: Tuple[scipy.integrate.tests.test_integrate.ComplexExp, Literal["bdf"]],
):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_(
    val: bool, msg: Tuple[scipy.integrate.tests.test_integrate.Pi, Literal["adams"]]
):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_(
    val: bool, msg: Tuple[scipy.integrate.tests.test_integrate.Pi, Literal["bdf"]]
):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_(
    val: bool,
    msg: Tuple[scipy.integrate.tests.test_integrate.CoupledDecay, Literal["adams"]],
):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_(val: numpy.bool_, msg: Tuple[int, int, numpy.float64, float]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_(val: numpy.bool_, msg: Tuple[int, int]):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_(val: numpy.bool_, msg: numpy.float64):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_(val: bool, msg: Literal["1877"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_(val: bool, msg: Literal["abs-diff: 0.053538"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_(val: bool, msg: Literal["abs-diff: 0.105586"]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_(val: bool, msg: Literal["abs-diff: 0.105546"]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_(val: bool, msg: Literal["abs-diff: 0.103046"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_(val: bool, msg: Literal["abs-diff: 0.066854"]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_(val: bool, msg: Literal["abs-diff: 0.058661"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_(val: bool, msg: Literal["abs-diff: 0.181948"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_(val: bool, msg: Literal["abs-diff: 0.087866"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_(val: bool, msg: Literal["abs-diff: 0.111942"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_(val: bool, msg: Literal["abs-diff: 0.128603"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_(val: bool, msg: Literal["abs-diff: 0.188998"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_(val: numpy.ndarray):
    """
    usage.scipy: 9
    """
    ...


@overload
def assert_(val: int):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_(val: bool, msg: numpy.dtype):
    """
    usage.scipy: 7
    """
    ...


@overload
def assert_(val: bool, msg: Literal["expected rank 0"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_(val: bool, msg: Literal["Spin 0 failed"]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_(val: bool, msg: Literal["Spin 1 failed"]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_(val: bool, msg: Literal["Spin 2 failed"]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_(val: bool, msg: Literal["Spin 3 failed"]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_(val: bool, msg: Literal["Spin 4 failed"]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_(val: bool, msg: Literal["Spin 5 failed"]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_(val: bool, msg: Literal["Spin 6 failed"]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_(val: bool, msg: Literal["Spin 7 failed"]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_(val: bool, msg: Literal["Spin 8 failed"]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_(val: bool, msg: Literal["Spin 9 failed"]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_(val: bool, msg: Literal["0"]):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_(val: Tuple[bool, Literal["There are NaN roots"]]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_(val: numpy.bool_, msg: scipy.optimize.optimize.OptimizeResult):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_(val: bool, msg: scipy.optimize.optimize.OptimizeResult):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_(val: bool, msg: Tuple[Tuple[float, float, float], Callable]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_(val: bool, msg: Tuple[List[int], Callable]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_(val: bool, msg: Tuple[Tuple[float, float, float, float], Callable]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_(val: bool, msg: Tuple[List[int], Callable]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_(val: bool, msg: int):
    """
    usage.scipy: 27
    """
    ...


@overload
def assert_(val: bool, msg: bytes):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_(val: bool, msg: Literal["Number of Taps"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_(val: numpy.bool_, msg: Literal["Zero at zero and pi"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_(val: numpy.bool_, msg: Tuple[numpy.float64, int, int]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_(val: numpy.bool_, msg: Literal["k=None"]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_(val: numpy.bool_, msg: Literal["k=1"]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_(val: numpy.bool_, msg: Literal["k=2"]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_(val: numpy.bool_, msg: Literal["k=40"]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_(val: numpy.bool_, msg: Literal["k=42"]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_(val: bool, msg: float):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_(val: bool, msg: Literal["[2]"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_(val: bool, msg: Literal["[3]"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_(val: scipy.sparse.csr.csr_matrix):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_(val: scipy.sparse.csc.csc_matrix):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_(val: scipy.sparse.lil.lil_matrix):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_(val: scipy.sparse.coo.coo_matrix):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_(val: scipy.sparse.dia.dia_matrix):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_(val: scipy.sparse.bsr.bsr_matrix):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_(val: numpy.bool_, msg: numpy.int64):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_(val: numpy.bool_, msg: Tuple[float, int]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_(val: numpy.bool_, msg: Tuple[int, float]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_(
    val: numpy.bool_,
    msg: Tuple[numpy.float64, numpy.float64, numpy.float64, numpy.float64],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_(
    val: bool, msg: Tuple[numpy.float64, numpy.float64, numpy.float64, numpy.float64]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_(val: bool, msg: Literal["ftest Entropy is nan"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_(val: bool, msg: Literal["fppf private is nan"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_(val: bool, msg: Literal["ttest Entropy is nan"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_(val: bool, msg: Literal["tppf private is nan"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_(val: bool, msg: Literal["<class 'int'>"]):
    """
    usage.scipy: 1
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
    usage.matplotlib: 4
    usage.scipy: 50
    usage.skimage: 1
    usage.sklearn: 2
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: int, atol: float):
    """
    usage.scipy: 68
    usage.skimage: 15
    usage.sklearn: 2
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: numpy.ndarray, rtol: float):
    """
    usage.matplotlib: 3
    usage.scipy: 298
    usage.skimage: 11
    usage.sklearn: 70
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: numpy.ndarray):
    """
    usage.matplotlib: 22
    usage.scipy: 871
    usage.skimage: 57
    usage.sklearn: 264
    usage.xarray: 21
    """
    ...


@overload
def assert_allclose(actual: float, desired: float, atol: float):
    """
    usage.scipy: 27
    usage.skimage: 3
    """
    ...


@overload
def assert_allclose(actual: float, desired: numpy.float64, atol: float):
    """
    usage.scipy: 1
    usage.skimage: 3
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: List[float]):
    """
    usage.matplotlib: 3
    usage.scipy: 88
    usage.skimage: 6
    usage.sklearn: 6
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, rtol: float, atol: int
):
    """
    usage.scipy: 15
    usage.skimage: 1
    usage.sklearn: 2
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: int):
    """
    usage.matplotlib: 2
    usage.scipy: 16
    usage.skimage: 22
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.float64, desired: numpy.float64):
    """
    usage.scipy: 102
    usage.skimage: 2
    usage.sklearn: 21
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: numpy.ndarray, atol: float):
    """
    usage.matplotlib: 100
    usage.scipy: 238
    usage.skimage: 31
    usage.sklearn: 27
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
    usage.scipy: 128
    usage.skimage: 1
    usage.sklearn: 7
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: Tuple[float, float]):
    """
    usage.scipy: 3
    usage.skimage: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.float64, desired: int):
    """
    usage.matplotlib: 1
    usage.scipy: 20
    usage.skimage: 1
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.float64, desired: int, rtol: float, atol: float):
    """
    usage.scipy: 2
    usage.skimage: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: List[numpy.float64], atol: float):
    """
    usage.scipy: 2
    usage.skimage: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: numpy.float64):
    """
    usage.scipy: 37
    usage.sklearn: 1
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
    usage.scipy: 111
    usage.sklearn: 5
    usage.xarray: 3
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: float):
    """
    usage.scipy: 75
    usage.sklearn: 2
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
    usage.sklearn: 1
    usage.xarray: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, rtol: float, atol: float
):
    """
    usage.scipy: 211
    usage.sklearn: 15
    """
    ...


@overload
def assert_allclose(actual: numpy.float64, desired: float, atol: float):
    """
    usage.matplotlib: 1
    usage.scipy: 67
    usage.sklearn: 3
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: List[float], rtol: float, atol: float
):
    """
    usage.scipy: 16
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, rtol: float, atol: numpy.float128
):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, rtol: float, atol: numpy.float64
):
    """
    usage.scipy: 292
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, rtol: int, atol: float
):
    """
    usage.scipy: 15
    usage.sklearn: 3
    """
    ...


@overload
def assert_allclose(actual: numpy.float64, desired: float, rtol: int, atol: float):
    """
    usage.scipy: 20
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.float64, desired: int, rtol: int, atol: float):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_allclose(
    actual: numpy.float64, desired: numpy.float64, rtol: int, atol: float
):
    """
    usage.scipy: 3
    usage.sklearn: 2
    """
    ...


@overload
def assert_allclose(actual: float, desired: float, rtol: int, atol: float):
    """
    usage.scipy: 19
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: List[int], rtol: float):
    """
    usage.scipy: 24
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, err_msg: Literal["sol1 != sol2"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["sol1 != sol3"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, err_msg: Literal["sol3 != sol4"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    err_msg: Literal["sol1 != sol1ty"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: float, desired: float):
    """
    usage.scipy: 14
    usage.sklearn: 3
    """
    ...


@overload
def assert_allclose(actual: float, desired: numpy.float64, rtol: int, atol: float):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.float64, desired: float, rtol: float, atol: int):
    """
    usage.scipy: 13
    """
    ...


@overload
def assert_allclose(
    actual: numpy.float64, desired: numpy.float64, rtol: float, atol: int
):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    atol: float,
    err_msg: Literal["der = 0  k = 1"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    atol: float,
    err_msg: Literal["der = 1  k = 1"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    atol: float,
    err_msg: Literal["der = 0  k = 2"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    atol: float,
    err_msg: Literal["der = 1  k = 2"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    atol: float,
    err_msg: Literal["der = 2  k = 2"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    atol: float,
    err_msg: Literal["der = 0  k = 3"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    atol: float,
    err_msg: Literal["der = 1  k = 3"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    atol: float,
    err_msg: Literal["der = 2  k = 3"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    atol: float,
    err_msg: Literal["der = 3  k = 3"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    atol: float,
    err_msg: Literal["der = 0  k = 4"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    atol: float,
    err_msg: Literal["der = 1  k = 4"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    atol: float,
    err_msg: Literal["der = 2  k = 4"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    atol: float,
    err_msg: Literal["der = 3  k = 4"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    atol: float,
    err_msg: Literal["der = 4  k = 4"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    atol: float,
    err_msg: Literal["der = 0  k = 5"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    atol: float,
    err_msg: Literal["der = 1  k = 5"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    atol: float,
    err_msg: Literal["der = 2  k = 5"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    atol: float,
    err_msg: Literal["der = 3  k = 5"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    atol: float,
    err_msg: Literal["der = 4  k = 5"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    atol: float,
    err_msg: Literal["der = 5  k = 5"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: List[numpy.ndarray], desired: numpy.ndarray, rtol: float, atol: float
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: List[List[numpy.ndarray]], desired: numpy.ndarray, rtol: float, atol: float
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: List[numpy.ndarray], desired: numpy.ndarray, atol: float):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_allclose(actual: float, desired: numpy.ndarray, atol: float):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: float, atol: float):
    """
    usage.scipy: 30
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: float, rtol: float, atol: float):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_allclose(
    actual: List[numpy.ndarray], desired: List[float], rtol: float, atol: float
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: List[numpy.ndarray], desired: List[Union[int, float]]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(actual: List[numpy.ndarray], desired: List[float]):
    """
    usage.scipy: 5
    """
    ...


@overload
def assert_allclose(actual: List[numpy.ndarray], desired: List[float], atol: float):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: List[numpy.ndarray], desired: List[complex], rtol: float, atol: float
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: int, rtol: float, atol: float):
    """
    usage.scipy: 8
    """
    ...


@overload
def assert_allclose(actual: float, desired: numpy.float64):
    """
    usage.scipy: 3
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(actual: float, desired: int, atol: float):
    """
    usage.scipy: 9
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    atol: float,
    err_msg: Literal["item 0"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    atol: float,
    err_msg: Literal["item 1"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    atol: float,
    err_msg: Literal["item 2"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    atol: float,
    err_msg: Literal["item 3"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    atol: float,
    err_msg: Literal["Function 0"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    atol: float,
    err_msg: str,
):
    """
    usage.scipy: 7
    usage.sklearn: 5
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    atol: float,
    err_msg: Literal["Function 1"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    atol: float,
    err_msg: Literal["Function 2"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    atol: float,
    err_msg: Literal["Function 3"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: int,
    atol: float,
    err_msg: Literal["Function 0"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: int,
    atol: float,
    err_msg: Literal["Function 1"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: int,
    atol: float,
    err_msg: Literal["Function 2"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: int,
    atol: float,
    err_msg: Literal["Function 3"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    atol: float,
    err_msg: Literal["Function 4"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, atol: float, err_msg: str
):
    """
    usage.scipy: 6
    usage.sklearn: 7
    """
    ...


@overload
def assert_allclose(actual: numpy.float64, desired: numpy.float64, rtol: float):
    """
    usage.scipy: 62
    usage.sklearn: 10
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, err_msg: Literal["dx=0"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, err_msg: Literal["dx=1"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, err_msg: Literal["dx=2"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, err_msg: Literal["dx=3"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, err_msg: Literal["dx=4"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, err_msg: Literal["dx=5"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, err_msg: Literal["dx=6"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, err_msg: Literal["dx=7"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, err_msg: Literal["dx=8"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, err_msg: Literal["dx=9"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    err_msg: Literal["dx=1 k=0"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    err_msg: Literal["dx=2 k=0"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    err_msg: Literal["dx=2 k=1"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    err_msg: Literal["dx=3 k=0"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    err_msg: Literal["dx=3 k=1"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    err_msg: Literal["dx=3 k=2"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    err_msg: Literal["dx=4 k=0"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    err_msg: Literal["dx=4 k=1"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    err_msg: Literal["dx=4 k=2"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    err_msg: Literal["dx=4 k=3"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    err_msg: Literal["dx=5 k=0"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    err_msg: Literal["dx=5 k=1"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    err_msg: Literal["dx=5 k=2"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    err_msg: Literal["dx=5 k=3"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    err_msg: Literal["dx=5 k=4"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    err_msg: Literal["dx=6 k=0"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    err_msg: Literal["dx=6 k=1"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    err_msg: Literal["dx=6 k=2"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    err_msg: Literal["dx=6 k=3"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    err_msg: Literal["dx=6 k=4"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    err_msg: Literal["dx=6 k=5"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    err_msg: Literal["dx=7 k=0"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    err_msg: Literal["dx=7 k=1"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    err_msg: Literal["dx=7 k=2"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    err_msg: Literal["dx=7 k=3"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    err_msg: Literal["dx=7 k=4"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    err_msg: Literal["dx=7 k=5"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    err_msg: Literal["dx=7 k=6"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    err_msg: Literal["dx=8 k=0"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    err_msg: Literal["dx=8 k=1"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    err_msg: Literal["dx=8 k=2"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    err_msg: Literal["dx=8 k=3"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    err_msg: Literal["dx=8 k=4"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    err_msg: Literal["dx=8 k=5"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    err_msg: Literal["dx=8 k=6"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    err_msg: Literal["dx=8 k=7"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    err_msg: Literal["dx=9 k=0"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    err_msg: Literal["dx=9 k=1"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    err_msg: Literal["dx=9 k=2"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    err_msg: Literal["dx=9 k=3"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    err_msg: Literal["dx=9 k=4"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    err_msg: Literal["dx=9 k=5"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    err_msg: Literal["dx=9 k=6"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    err_msg: Literal["dx=9 k=7"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    err_msg: Literal["dx=9 k=8"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: int, atol: float, err_msg: str):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: List[int]):
    """
    usage.matplotlib: 4
    usage.scipy: 68
    usage.sklearn: 9
    """
    ...


@overload
def assert_allclose(
    actual: numpy.float64, desired: numpy.ndarray, rtol: float, atol: float
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(actual: List[numpy.ndarray], desired: List[numpy.float64]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: List[numpy.float64]):
    """
    usage.scipy: 4
    usage.sklearn: 4
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, err_msg: Literal["None"]
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, err_msg: Literal["(0, 0)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, err_msg: Literal["(0, 1)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, err_msg: Literal["(1, 0)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, err_msg: Literal["(2, 3)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, err_msg: Literal["(9, 2)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, err_msg: Literal["(0, 0, 0)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, err_msg: Literal["(0, 1, 0)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, err_msg: Literal["(1, 0, 0)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, err_msg: Literal["(2, 3, 0)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, err_msg: Literal["(6, 0, 2)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: float,
    rtol: float,
    atol: float,
    err_msg: Literal["[(0, 1), (0, 1)]"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: float,
    rtol: float,
    atol: float,
    err_msg: Literal["[(0, 0.5), (0, 1)]"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: float,
    rtol: float,
    atol: float,
    err_msg: Literal["[(0, 1), (0, 0.5)]"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: float, rtol: float, atol: float, err_msg: str
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, err_msg: Literal["nearest"]
):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, err_msg: Literal["linear"]
):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, err_msg: Literal["splinef2d"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.matrix, desired: numpy.ndarray):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["('nearest', True)"],
):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["('nearest', False)"],
):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["('linear', True)"],
):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["('linear', False)"],
):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["('cubic', True)"],
):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["('cubic', False)"],
):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["nearest"],
):
    """
    usage.scipy: 10
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["linear"],
):
    """
    usage.scipy: 7
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["cubic"],
):
    """
    usage.scipy: 7
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, err_msg: Literal["cubic"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: List[Union[int, complex]], desired: numpy.ndarray):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(actual: List[Union[complex, int]], desired: numpy.ndarray):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.float64, rtol: float, atol: float
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.float64, desired: numpy.float64, rtol: float, atol: float
):
    """
    usage.scipy: 11
    usage.sklearn: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.complex128, desired: numpy.complex128, rtol: float, atol: float
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: complex, rtol: float, atol: float):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(actual: numpy.float32, desired: float):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: List[Union[float, int]]):
    """
    usage.matplotlib: 2
    usage.scipy: 15
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(actual: complex, desired: numpy.complex128, rtol: float):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: numpy.float64,
    atol: numpy.float64,
    err_msg: Literal["driver: gelsd"],
):
    """
    usage.scipy: 16
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: numpy.float64,
    atol: numpy.float64,
    err_msg: Literal["driver: gelss"],
):
    """
    usage.scipy: 16
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: numpy.float64,
    atol: numpy.float64,
    err_msg: Literal["driver: gelsy"],
):
    """
    usage.scipy: 16
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: numpy.float64,
    atol: numpy.float64,
    err_msg: Literal["driver: None"],
):
    """
    usage.scipy: 16
    """
    ...


@overload
def assert_allclose(
    actual: numpy.float32,
    desired: numpy.float32,
    rtol: numpy.float64,
    atol: numpy.float64,
    err_msg: Literal["driver: gelsd"],
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: Tuple[float, float],
    rtol: numpy.float64,
    atol: numpy.float64,
    err_msg: Literal["driver: gelsd"],
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.float32,
    desired: numpy.float32,
    rtol: numpy.float64,
    atol: numpy.float64,
    err_msg: Literal["driver: gelss"],
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: Tuple[float, float],
    rtol: numpy.float64,
    atol: numpy.float64,
    err_msg: Literal["driver: gelss"],
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.float32,
    desired: numpy.float32,
    rtol: numpy.float64,
    atol: numpy.float64,
    err_msg: Literal["driver: gelsy"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: Tuple[float, float],
    rtol: numpy.float64,
    atol: numpy.float64,
    err_msg: Literal["driver: gelsy"],
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.float32,
    desired: numpy.float32,
    rtol: numpy.float64,
    atol: numpy.float64,
    err_msg: Literal["driver: None"],
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: Tuple[float, float],
    rtol: numpy.float64,
    atol: numpy.float64,
    err_msg: Literal["driver: None"],
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.float64,
    desired: numpy.float64,
    rtol: numpy.float64,
    atol: numpy.float64,
    err_msg: Literal["driver: gelsd"],
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.float64,
    desired: numpy.float64,
    rtol: numpy.float64,
    atol: numpy.float64,
    err_msg: Literal["driver: gelss"],
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.float64,
    desired: numpy.float64,
    rtol: numpy.float64,
    atol: numpy.float64,
    err_msg: Literal["driver: gelsy"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.float64,
    desired: numpy.float64,
    rtol: numpy.float64,
    atol: numpy.float64,
    err_msg: Literal["driver: None"],
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.float128,
    desired: numpy.float64,
    rtol: numpy.float64,
    atol: numpy.float64,
    err_msg: Literal["driver: gelsd"],
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.float128,
    desired: numpy.float64,
    rtol: numpy.float64,
    atol: numpy.float64,
    err_msg: Literal["driver: gelss"],
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.float128,
    desired: numpy.float128,
    rtol: numpy.float64,
    atol: numpy.float64,
    err_msg: Literal["driver: gelsy"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.float128,
    desired: numpy.float64,
    rtol: numpy.float64,
    atol: numpy.float64,
    err_msg: Literal["driver: None"],
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: Tuple[complex, complex],
    rtol: numpy.float64,
    atol: numpy.float64,
    err_msg: Literal["driver: gelsd"],
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: Tuple[complex, complex],
    rtol: numpy.float64,
    atol: numpy.float64,
    err_msg: Literal["driver: gelss"],
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.float32,
    desired: numpy.complex64,
    rtol: numpy.float64,
    atol: numpy.float64,
    err_msg: Literal["driver: gelsy"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: Tuple[complex, complex],
    rtol: numpy.float64,
    atol: numpy.float64,
    err_msg: Literal["driver: gelsy"],
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: Tuple[complex, complex],
    rtol: numpy.float64,
    atol: numpy.float64,
    err_msg: Literal["driver: None"],
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.float64,
    desired: numpy.complex128,
    rtol: numpy.float64,
    atol: numpy.float64,
    err_msg: Literal["driver: gelsy"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.float128,
    desired: numpy.complex256,
    rtol: numpy.float64,
    atol: numpy.float64,
    err_msg: Literal["driver: gelsy"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: Tuple[float, float, float],
    rtol: numpy.float64,
    atol: numpy.float64,
    err_msg: Literal["driver: gelsd"],
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: Tuple[float, float, float],
    rtol: numpy.float64,
    atol: numpy.float64,
    err_msg: Literal["driver: gelss"],
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: Tuple[float, float, float],
    rtol: numpy.float64,
    atol: numpy.float64,
    err_msg: Literal["driver: gelsy"],
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: Tuple[float, float, float],
    rtol: numpy.float64,
    atol: numpy.float64,
    err_msg: Literal["driver: None"],
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(actual: numpy.float16, desired: numpy.float64, rtol: numpy.float64):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(actual: float, desired: numpy.float64, rtol: numpy.float64):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_allclose(actual: numpy.float128, desired: numpy.float64, rtol: float):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: List[List[float]]):
    """
    usage.scipy: 2
    usage.sklearn: 2
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: List[List[List[float]]]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(actual: int, desired: int):
    """
    usage.scipy: 2
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: numpy.ndarray, atol: numpy.float64):
    """
    usage.scipy: 81
    """
    ...


@overload
def assert_allclose(actual: complex, desired: complex, rtol: int):
    """
    usage.scipy: 8
    """
    ...


@overload
def assert_allclose(actual: float, desired: float, rtol: int):
    """
    usage.scipy: 16
    """
    ...


@overload
def assert_allclose(actual: numpy.complex128, desired: int):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: int, rtol: float, atol: float, err_msg: str
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: numpy.ndarray, err_msg: str):
    """
    usage.scipy: 28
    usage.sklearn: 38
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: float, rtol: float, atol: numpy.float64
):
    """
    usage.scipy: 6
    """
    ...


@overload
def assert_allclose(actual: List[Union[int, float]], desired: numpy.ndarray):
    """
    usage.matplotlib: 1
    usage.scipy: 4
    """
    ...


@overload
def assert_allclose(actual: List[Union[float, int]], desired: numpy.ndarray):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: List[complex], desired: numpy.ndarray):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: List[float], desired: numpy.ndarray):
    """
    usage.scipy: 11
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: numpy.float32, atol: numpy.float64):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: numpy.float64, atol: numpy.float64):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.complex64, atol: numpy.float64
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.complex128, atol: numpy.float64
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: int, atol: numpy.float64):
    """
    usage.scipy: 11
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: List[float], atol: float):
    """
    usage.scipy: 18
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: float, rtol: float):
    """
    usage.scipy: 17
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: List[Union[int, float]], atol: float
):
    """
    usage.scipy: 5
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, rtol: int, atol: numpy.float64
):
    """
    usage.scipy: 5
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, rtol: float, err_msg: str
):
    """
    usage.scipy: 12
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: List[List[int]], atol: float):
    """
    usage.scipy: 6
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: List[List[int]], atol: numpy.float64
):
    """
    usage.scipy: 10
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: List[List[Union[int, complex]]], atol: numpy.float64
):
    """
    usage.scipy: 10
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: List[List[Union[complex, int]]], atol: numpy.float64
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: numpy.ndarray, rtol: numpy.float64):
    """
    usage.scipy: 32
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: numpy.float64,
    atol: numpy.float64,
):
    """
    usage.scipy: 12
    """
    ...


@overload
def assert_allclose(actual: complex, desired: float):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: complex, desired: complex):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[numpy.ndarray, numpy.ndarray], desired: List[List[int]], atol: float
):
    """
    usage.scipy: 16
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: List[int], atol: float):
    """
    usage.scipy: 21
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[numpy.ndarray, numpy.ndarray],
    desired: List[List[Union[int, complex]]],
    atol: float,
):
    """
    usage.scipy: 12
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: List[List[Union[int, float]]], atol: float
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: List[List[Union[complex, int]]], atol: float
):
    """
    usage.scipy: 7
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: List[List[Union[complex, float, int]]], atol: float
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.complex128, desired: numpy.complex128):
    """
    usage.scipy: 7
    """
    ...


@overload
def assert_allclose(actual: numpy.complex128, desired: complex):
    """
    usage.scipy: 12
    """
    ...


@overload
def assert_allclose(actual: List[Union[numpy.float64, int]], desired: numpy.ndarray):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: List[Union[numpy.complex128, int]], desired: numpy.ndarray):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, err_msg: Literal["#0 failed"]
):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, err_msg: Literal["#1 failed"]
):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, err_msg: Literal["#2 failed"]
):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, err_msg: Literal["#3 failed"]
):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, err_msg: Literal["#4 failed"]
):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_allclose(actual: numpy.int64, desired: int):
    """
    usage.scipy: 10
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: Tuple[int, int, int, int, int, int, int, int, int, int],
    atol: float,
):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: Tuple[float, float, float, float, float, float, float],
    atol: float,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: Tuple[
        float, float, float, float, float, float, float, float, float, float
    ],
    atol: float,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: Tuple[float, float], atol: float):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: List[Union[float, numpy.float64]], atol: float
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: numpy.float64, rtol: float):
    """
    usage.scipy: 8
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: List[int], rtol: float, atol: float
):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_allclose(actual: numpy.float64, desired: List[float], atol: float):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: List[float], rtol: float):
    """
    usage.matplotlib: 3
    usage.scipy: 49
    usage.sklearn: 6
    """
    ...


@overload
def assert_allclose(
    actual: List[float], desired: List[float], rtol: float, atol: float
):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_allclose(actual: float, desired: float, rtol: float, atol: float):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.float64, desired: float, rtol: float, atol: float, err_msg: str
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: List[int], rtol: float, atol: float, err_msg: str
):
    """
    usage.scipy: 6
    """
    ...


@overload
def assert_allclose(
    actual: numpy.float64, desired: int, rtol: float, atol: float, err_msg: str
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: List[float], rtol: float, atol: float, err_msg: str
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.float64, desired: numpy.int64, rtol: float, atol: float, err_msg: str
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: List[Union[float, int]],
    rtol: float,
    atol: float,
    err_msg: str,
):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: List[Union[int, float]],
    rtol: float,
    atol: float,
    err_msg: str,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.float64,
    desired: numpy.float64,
    rtol: float,
    atol: float,
    err_msg: str,
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(actual: numpy.int64, desired: numpy.int64, rtol: float):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: List[Union[int, float]]):
    """
    usage.matplotlib: 2
    usage.scipy: 10
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: numpy.complex128):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(actual: numpy.float64, desired: numpy.float64, atol: float):
    """
    usage.scipy: 40
    usage.sklearn: 3
    """
    ...


@overload
def assert_allclose(actual: int, desired: int, atol: float):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: List[numpy.ndarray],
    desired: List[List[Union[int, float]]],
    rtol: float,
    atol: float,
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: List[numpy.ndarray], desired: List[List[float]], rtol: float, atol: float
):
    """
    usage.scipy: 7
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: List[float], err_msg: str):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.float64, desired: float, err_msg: str):
    """
    usage.scipy: 2
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: Tuple[int, int], atol: float):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_allclose(actual: float, desired: float, atol: float, err_msg: str):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_allclose(actual: numpy.float64, desired: float, atol: float, err_msg: str):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_allclose(
    actual: numpy.float64, desired: numpy.float64, atol: float, err_msg: str
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: float,
    desired: float,
    rtol: numpy.float64,
    atol: numpy.float64,
    err_msg: str,
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(actual: float, desired: int, err_msg: str):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.float64,
    desired: float,
    rtol: numpy.float64,
    atol: numpy.float64,
    err_msg: str,
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: Tuple[
        float, float, float, float, float, float, float, float, float, float
    ],
):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_allclose(
    actual: float,
    desired: float,
    rtol: numpy.float64,
    atol: numpy.float64,
    err_msg: Literal["method bisect"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: float,
    desired: float,
    rtol: numpy.float64,
    atol: numpy.float64,
    err_msg: Literal["method ridder"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: float, desired: float, rtol: numpy.float64, atol: float):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: complex, desired: int, atol: float):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: float, desired: int):
    """
    usage.scipy: 5
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(actual: float, desired: int, rtol: numpy.float64, atol: float):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: int, rtol: numpy.float64, atol: float
):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: List[Union[float, int]], rtol: float
):
    """
    usage.scipy: 5
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: List[List[Union[int, float]]], rtol: float
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: List[complex]):
    """
    usage.scipy: 7
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: List[Union[int, complex]]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: List[List[Union[int, float]]],
    rtol: float,
    atol: float,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: List[int], desired: numpy.ndarray):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_allclose(actual: Tuple[int], desired: numpy.ndarray):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_allclose(actual: Tuple[int, int, int], desired: numpy.ndarray):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: List[Union[int, float]], rtol: float
):
    """
    usage.scipy: 14
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.float64, desired: int, rtol: float):
    """
    usage.scipy: 12
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(actual: float, desired: float, rtol: float):
    """
    usage.scipy: 19
    usage.sklearn: 9
    """
    ...


@overload
def assert_allclose(actual: List[numpy.complex128], desired: List[numpy.complex128]):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_allclose(actual: int, desired: numpy.ndarray):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: List[Union[int, numpy.float64]], desired: numpy.ndarray):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: list, desired: list, rtol: float):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: List[numpy.int64], desired: List[numpy.complex128], rtol: float
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: List[numpy.complex128], desired: List[numpy.complex128], rtol: float
):
    """
    usage.scipy: 9
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: Tuple[int, float], rtol: float):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: Tuple[int, numpy.float64]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: int, desired: numpy.float64, rtol: float):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: float, desired: numpy.float64, rtol: float):
    """
    usage.scipy: 2
    usage.sklearn: 7
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[numpy.ndarray, numpy.ndarray],
    desired: Tuple[numpy.ndarray, numpy.ndarray],
):
    """
    usage.scipy: 10
    """
    ...


@overload
def assert_allclose(
    actual: List[numpy.complex128], desired: List[complex], rtol: float
):
    """
    usage.scipy: 24
    """
    ...


@overload
def assert_allclose(actual: List[numpy.complex128], desired: List[complex]):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_allclose(
    actual: List[numpy.complex128], desired: List[Union[complex, float]], rtol: float
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: List[numpy.complex128], desired: List[Union[complex, int]], rtol: float
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: List[numpy.ndarray],
    err_msg: Literal["bessel(2,...)"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, err_msg: Literal["bessel(3,...)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, err_msg: Literal["bessel(4,...)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: List[numpy.ndarray],
    err_msg: Literal["butter(2,...)"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, err_msg: Literal["butter(3,...)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, err_msg: Literal["butter(4,...)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: List[numpy.ndarray],
    err_msg: Literal["cheby1(2,...)"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, err_msg: Literal["cheby1(3,...)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, err_msg: Literal["cheby1(4,...)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: List[numpy.ndarray],
    err_msg: Literal["cheby2(2,...)"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, err_msg: Literal["cheby2(3,...)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, err_msg: Literal["cheby2(4,...)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: List[numpy.ndarray],
    err_msg: Literal["ellip(2,...)"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, err_msg: Literal["ellip(3,...)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, err_msg: Literal["ellip(4,...)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: List[List[int]], rtol: float):
    """
    usage.scipy: 39
    """
    ...


@overload
def assert_allclose(actual: numpy.float64, desired: int, err_msg: str):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray, numpy.ndarray],
    desired: List[Tuple[float]],
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(actual: List[numpy.float64], desired: List[numpy.float64]):
    """
    usage.matplotlib: 1
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["order=1"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["order=2"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["order=3"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["order=4"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["order=5"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.float64, rtol: float, atol: int
):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, err_msg: Literal["boxcar, 0"]
):
    """
    usage.scipy: 7
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, err_msg: Literal["boxcar, 9"]
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, err_msg: Literal["bartlett, 26"]
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, err_msg: Literal["hann, 128"]
):
    """
    usage.scipy: 8
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    err_msg: Literal["('tukey', 0.5), 64"],
):
    """
    usage.scipy: 5
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, err_msg: Literal["hann, 255"]
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, err_msg: Literal["boxcar, 3"]
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, err_msg: Literal["bartlett, 37"]
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, err_msg: Literal["hann, 127"]
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    err_msg: Literal["('tukey', 0.5), 14"],
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, err_msg: Literal["hann, 5"]
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    atol: float,
    err_msg: Literal["hann, 128"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, err_msg: Literal["boxcar, 10, 0"]
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, err_msg: Literal["boxcar, 10, 9"]
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, err_msg: Literal["bartlett, 51, 26"]
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, err_msg: Literal["hann, 256, 128"]
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, err_msg: Literal["hann, 256, 255"]
):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, err_msg: Literal["boxcar, 0, even"]
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, err_msg: Literal["boxcar, 0, odd"]
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    err_msg: Literal["boxcar, 0, constant"],
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, err_msg: Literal["boxcar, 0, zeros"]
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, err_msg: Literal["boxcar, 9, even"]
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, err_msg: Literal["boxcar, 9, odd"]
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    err_msg: Literal["boxcar, 9, constant"],
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, err_msg: Literal["boxcar, 9, zeros"]
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    err_msg: Literal["istft transpose plus"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: List[Union[float, int]], atol: float
):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: List[List[float]],
    atol: float,
    err_msg: Tuple[int, float, int],
):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: List[float],
    rtol: float,
    atol: float,
    err_msg: Tuple[int, float, int],
):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: List[List[float]],
    atol: float,
    err_msg: Tuple[int, int, int],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: List[float],
    rtol: float,
    atol: float,
    err_msg: Tuple[int, int, int],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: List[List[Union[float, int]]], atol: float
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: numpy.float64,
    atol: numpy.float64,
    err_msg: str,
):
    """
    usage.scipy: 10
    """
    ...


@overload
def assert_allclose(actual: numpy.float64, desired: int, atol: numpy.float32):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: int, atol: numpy.float32):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.float64, desired: int, atol: numpy.float64):
    """
    usage.scipy: 7
    """
    ...


@overload
def assert_allclose(
    actual: numpy.float64,
    desired: numpy.float64,
    err_msg: Literal["array([1, 1, 1, 1])"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.float64,
    desired: numpy.float64,
    err_msg: Literal["array([1, 1, 1, 0])"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.float64,
    desired: numpy.float64,
    err_msg: Literal["array([1, 1, 0, 0])"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.float64,
    desired: numpy.float64,
    err_msg: Literal["array([1, 0, 0, 0])"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: List[numpy.complex128], desired: Tuple[int, int, int]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: Tuple[int, int, int]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: List[List[Union[int, float]]]):
    """
    usage.scipy: 1
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.int64, desired: numpy.float64):
    """
    usage.scipy: 5
    """
    ...


@overload
def assert_allclose(actual: numpy.matrix, desired: numpy.matrix, atol: numpy.float64):
    """
    usage.scipy: 13
    """
    ...


@overload
def assert_allclose(actual: numpy.matrix, desired: numpy.matrix, atol: numpy.float128):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, rtol: bool, atol: float
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: List[List[Union[float, numpy.float64]]]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: List[List[Union[numpy.float64, int]]]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: List[Union[numpy.float64, float]]):
    """
    usage.scipy: 2
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: List[Union[int, numpy.float64]]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: float, desired: int, rtol: int, atol: float):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: float, rtol: bool, atol: float):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: float, desired: float, rtol: float, err_msg: str):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: List[Tuple[float, float]]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(actual: List[numpy.ndarray], desired: List[numpy.ndarray]):
    """
    usage.scipy: 10
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: int, rtol: float):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: List[List[int]]):
    """
    usage.scipy: 1
    usage.sklearn: 5
    """
    ...


@overload
def assert_allclose(actual: numpy.float64, desired: float, rtol: int, atol: int):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: int, rtol: int, atol: float):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_allclose(actual: List[int], desired: numpy.ndarray, atol: float):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: List[complex], rtol: float):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.float64,
    desired: numpy.complex128,
    rtol: float,
    atol: float,
    err_msg: Tuple[int, int],
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.float64,
    desired: numpy.complex128,
    rtol: float,
    atol: float,
    err_msg: Tuple[int, float],
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.float64,
    desired: numpy.complex128,
    rtol: float,
    atol: float,
    err_msg: Tuple[float, float],
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.float64,
    desired: numpy.complex128,
    rtol: float,
    atol: float,
    err_msg: Tuple[float, int],
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.float64,
    desired: numpy.complex128,
    rtol: float,
    atol: float,
    err_msg: Tuple[numpy.float64, float],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.complex128, desired: float):
    """
    usage.scipy: 12
    """
    ...


@overload
def assert_allclose(
    actual: numpy.float64, desired: numpy.float64, atol: numpy.float64, err_msg: float
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.float64,
    desired: numpy.float64,
    atol: numpy.float64,
    err_msg: Tuple[float, float],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.complex128,
    desired: numpy.complex128,
    atol: numpy.float64,
    err_msg: Tuple[float, complex],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.float64, desired: numpy.float64, rtol: int, atol: numpy.float64
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: float, desired: numpy.float64, err_msg: str):
    """
    usage.scipy: 1
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(
    actual: float, desired: numpy.float64, err_msg: Literal["(-10.0, 1.0) dd None"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: float, desired: numpy.float64, err_msg: Literal["(-1.0, -1.0) dd None"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: float, desired: numpy.float64, err_msg: Literal["(-1.0, 1.0) dd None"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: float, desired: numpy.float64, err_msg: Literal["(-1.0, 10.0) dd None"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: float, desired: numpy.float64, err_msg: Literal["(1.0, -10.0) dd None"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: float, desired: numpy.float64, err_msg: Literal["(1.0, -1.0) dd None"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: float, desired: numpy.float64, err_msg: Literal["(1.0, 1.0) dd None"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: float, desired: numpy.float64, err_msg: Literal["(1.0, 10.0) dd None"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: float, desired: numpy.float64, err_msg: Literal["(10.0, -1.0) dd None"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: float, desired: numpy.float64, err_msg: Literal["(10.0, 1.0) dd None"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: float, desired: numpy.float64, err_msg: Literal["(10.0, 10.0) dd None"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[float, float, float, float],
    desired: Tuple[numpy.float64, numpy.float64, numpy.float64, numpy.float64],
    err_msg: str,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[float, float, float, float],
    desired: Tuple[numpy.float64, numpy.float64, numpy.float64, numpy.float64],
    err_msg: Literal["(-1.0,) d ['double']"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[float, float, float, float],
    desired: Tuple[numpy.float64, numpy.float64, numpy.float64, numpy.float64],
    err_msg: Literal["(1.0,) d ['double']"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[float, float, float, float],
    desired: Tuple[numpy.float64, numpy.float64, numpy.float64, numpy.float64],
    err_msg: Literal["(10.0,) d ['double']"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[complex, complex, complex, complex],
    desired: Tuple[
        numpy.complex128, numpy.complex128, numpy.complex128, numpy.complex128
    ],
    err_msg: str,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: float, desired: numpy.float64, err_msg: Literal["(-10.0,) d None"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: float, desired: numpy.float64, err_msg: Literal["(-1.0,) d None"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: float, desired: numpy.float64, err_msg: Literal["(1.0,) d None"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: float, desired: numpy.float64, err_msg: Literal["(10.0,) d None"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: float, desired: numpy.float64, err_msg: Literal["(-1.0,) d ['double']"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: float, desired: numpy.float64, err_msg: Literal["(1.0,) d ['double']"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: float, desired: numpy.float64, err_msg: Literal["(10.0,) d ['double']"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: complex, desired: numpy.complex128, err_msg: str):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[float, float, float, float],
    desired: Tuple[numpy.float64, numpy.float64, numpy.float64, numpy.float64],
    err_msg: Literal["(-10.0, 1.0) dd None"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[float, float, float, float],
    desired: Tuple[numpy.float64, numpy.float64, numpy.float64, numpy.float64],
    err_msg: Literal["(-1.0, -1.0) dd None"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[float, float, float, float],
    desired: Tuple[numpy.float64, numpy.float64, numpy.float64, numpy.float64],
    err_msg: Literal["(-1.0, 1.0) dd None"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[float, float, float, float],
    desired: Tuple[numpy.float64, numpy.float64, numpy.float64, numpy.float64],
    err_msg: Literal["(-1.0, 10.0) dd None"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[float, float, float, float],
    desired: Tuple[numpy.float64, numpy.float64, numpy.float64, numpy.float64],
    err_msg: Literal["(1.0, -10.0) dd None"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[float, float, float, float],
    desired: Tuple[numpy.float64, numpy.float64, numpy.float64, numpy.float64],
    err_msg: Literal["(1.0, -1.0) dd None"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[float, float, float, float],
    desired: Tuple[numpy.float64, numpy.float64, numpy.float64, numpy.float64],
    err_msg: Literal["(1.0, 1.0) dd None"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[float, float, float, float],
    desired: Tuple[numpy.float64, numpy.float64, numpy.float64, numpy.float64],
    err_msg: Literal["(1.0, 10.0) dd None"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[float, float, float, float],
    desired: Tuple[numpy.float64, numpy.float64, numpy.float64, numpy.float64],
    err_msg: Literal["(10.0, -1.0) dd None"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[float, float, float, float],
    desired: Tuple[numpy.float64, numpy.float64, numpy.float64, numpy.float64],
    err_msg: Literal["(10.0, 1.0) dd None"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[float, float, float, float],
    desired: Tuple[numpy.float64, numpy.float64, numpy.float64, numpy.float64],
    err_msg: Literal["(10.0, 10.0) dd None"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: float, desired: numpy.float64, err_msg: Literal["(-10, -10.0) ld None"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: float, desired: numpy.float64, err_msg: Literal["(-10, -1.0) ld None"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: float, desired: numpy.float64, err_msg: Literal["(-10, 1.0) ld None"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: float, desired: numpy.float64, err_msg: Literal["(-10, 10.0) ld None"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: float, desired: numpy.float64, err_msg: Literal["(-1, -10.0) ld None"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: float, desired: numpy.float64, err_msg: Literal["(-1, -1.0) ld None"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: float, desired: numpy.float64, err_msg: Literal["(-1, 1.0) ld None"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: float, desired: numpy.float64, err_msg: Literal["(-1, 10.0) ld None"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: float, desired: numpy.float64, err_msg: Literal["(1, -10.0) ld None"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: float, desired: numpy.float64, err_msg: Literal["(1, -1.0) ld None"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: float, desired: numpy.float64, err_msg: Literal["(1, 1.0) ld None"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: float, desired: numpy.float64, err_msg: Literal["(1, 10.0) ld None"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: float, desired: numpy.float64, err_msg: Literal["(10, -10.0) ld None"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: float, desired: numpy.float64, err_msg: Literal["(10, -1.0) ld None"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: float, desired: numpy.float64, err_msg: Literal["(10, 1.0) ld None"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: float, desired: numpy.float64, err_msg: Literal["(10, 10.0) ld None"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: float, desired: numpy.float64, err_msg: Literal["(-10.0,) f ['float']"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: float, desired: numpy.float64, err_msg: Literal["(-1.0,) f ['float']"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: float, desired: numpy.float64, err_msg: Literal["(1.0,) f ['float']"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: float, desired: numpy.float64, err_msg: Literal["(10.0,) f ['float']"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: float, desired: numpy.float64, err_msg: Literal["(1, 1.0) ld ['long']"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[float, float],
    desired: Tuple[numpy.float64, numpy.float64],
    err_msg: str,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[float, float],
    desired: Tuple[numpy.float64, numpy.float64],
    err_msg: Literal["(-1.0,) d ['double']"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[float, float],
    desired: Tuple[numpy.float64, numpy.float64],
    err_msg: Literal["(1.0,) d ['double']"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[float, float],
    desired: Tuple[numpy.float64, numpy.float64],
    err_msg: Literal["(10.0,) d ['double']"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[complex, complex],
    desired: Tuple[numpy.complex128, numpy.complex128],
    err_msg: str,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[float, float],
    desired: Tuple[numpy.float64, numpy.float64],
    err_msg: Literal["(-10.0,) d None"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[float, float],
    desired: Tuple[numpy.float64, numpy.float64],
    err_msg: Literal["(-1.0,) d None"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[float, float],
    desired: Tuple[numpy.float64, numpy.float64],
    err_msg: Literal["(1.0,) d None"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[float, float],
    desired: Tuple[numpy.float64, numpy.float64],
    err_msg: Literal["(10.0,) d None"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[float, float, float, float],
    desired: Tuple[numpy.float64, numpy.float64, numpy.float64, numpy.float64],
    err_msg: Literal["(-10.0,) d None"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[float, float, float, float],
    desired: Tuple[numpy.float64, numpy.float64, numpy.float64, numpy.float64],
    err_msg: Literal["(-1.0,) d None"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[float, float, float, float],
    desired: Tuple[numpy.float64, numpy.float64, numpy.float64, numpy.float64],
    err_msg: Literal["(1.0,) d None"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[float, float, float, float],
    desired: Tuple[numpy.float64, numpy.float64, numpy.float64, numpy.float64],
    err_msg: Literal["(10.0,) d None"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[complex, complex, complex, complex],
    desired: Tuple[
        numpy.complex128, numpy.complex128, numpy.complex128, numpy.complex128
    ],
    err_msg: Literal["(-10.0,) d None"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[complex, complex, complex, complex],
    desired: Tuple[
        numpy.complex128, numpy.complex128, numpy.complex128, numpy.complex128
    ],
    err_msg: Literal["(-1.0,) d None"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[complex, complex, complex, complex],
    desired: Tuple[
        numpy.complex128, numpy.complex128, numpy.complex128, numpy.complex128
    ],
    err_msg: Literal["(1.0,) d None"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[complex, complex, complex, complex],
    desired: Tuple[
        numpy.complex128, numpy.complex128, numpy.complex128, numpy.complex128
    ],
    err_msg: Literal["(10.0,) d None"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: complex, desired: numpy.complex128, err_msg: Literal["((-10-10j),) D None"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: complex, desired: numpy.complex128, err_msg: Literal["((-10-1j),) D None"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: complex, desired: numpy.complex128, err_msg: Literal["((-10+1j),) D None"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: complex, desired: numpy.complex128, err_msg: Literal["((-10+10j),) D None"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: complex, desired: numpy.complex128, err_msg: Literal["((-1-10j),) D None"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: complex, desired: numpy.complex128, err_msg: Literal["((-1-1j),) D None"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: complex, desired: numpy.complex128, err_msg: Literal["((-1+1j),) D None"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: complex, desired: numpy.complex128, err_msg: Literal["((-1+10j),) D None"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: complex, desired: numpy.complex128, err_msg: Literal["((1-10j),) D None"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: complex, desired: numpy.complex128, err_msg: Literal["((1-1j),) D None"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: complex, desired: numpy.complex128, err_msg: Literal["((1+1j),) D None"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: complex, desired: numpy.complex128, err_msg: Literal["((1+10j),) D None"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: complex, desired: numpy.complex128, err_msg: Literal["((10-10j),) D None"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: complex, desired: numpy.complex128, err_msg: Literal["((10-1j),) D None"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: complex, desired: numpy.complex128, err_msg: Literal["((10+1j),) D None"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: complex, desired: numpy.complex128, err_msg: Literal["((10+10j),) D None"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[complex, complex],
    desired: Tuple[numpy.complex128, numpy.complex128],
    err_msg: Literal["(-10.0,) d None"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[complex, complex],
    desired: Tuple[numpy.complex128, numpy.complex128],
    err_msg: Literal["(-1.0,) d None"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[complex, complex],
    desired: Tuple[numpy.complex128, numpy.complex128],
    err_msg: Literal["(1.0,) d None"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[complex, complex],
    desired: Tuple[numpy.complex128, numpy.complex128],
    err_msg: Literal["(10.0,) d None"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[float, float],
    desired: Tuple[numpy.float64, numpy.float64],
    err_msg: Literal["(-10.0, 1.0) dd None"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[float, float],
    desired: Tuple[numpy.float64, numpy.float64],
    err_msg: Literal["(-1.0, -1.0) dd None"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[float, float],
    desired: Tuple[numpy.float64, numpy.float64],
    err_msg: Literal["(-1.0, 1.0) dd None"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[float, float],
    desired: Tuple[numpy.float64, numpy.float64],
    err_msg: Literal["(-1.0, 10.0) dd None"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[float, float],
    desired: Tuple[numpy.float64, numpy.float64],
    err_msg: Literal["(1.0, -10.0) dd None"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[float, float],
    desired: Tuple[numpy.float64, numpy.float64],
    err_msg: Literal["(1.0, -1.0) dd None"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[float, float],
    desired: Tuple[numpy.float64, numpy.float64],
    err_msg: Literal["(1.0, 1.0) dd None"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[float, float],
    desired: Tuple[numpy.float64, numpy.float64],
    err_msg: Literal["(1.0, 10.0) dd None"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[float, float],
    desired: Tuple[numpy.float64, numpy.float64],
    err_msg: Literal["(10.0, -1.0) dd None"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[float, float],
    desired: Tuple[numpy.float64, numpy.float64],
    err_msg: Literal["(10.0, 1.0) dd None"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[float, float],
    desired: Tuple[numpy.float64, numpy.float64],
    err_msg: Literal["(10.0, 10.0) dd None"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.float64, desired: numpy.float64, rtol: float, atol: int, err_msg: str
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: List[Union[float, int]], rtol: int, atol: float
):
    """
    usage.scipy: 1
    usage.sklearn: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.complex128, desired: numpy.complex128, rtol: float, atol: int
):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_allclose(actual: numpy.complex128, desired: float, rtol: float, atol: int):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.float32, desired: float, atol: float):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(actual: numpy.float128, desired: float, atol: float):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(actual: numpy.float64, desired: float, rtol: float, atol: float):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[numpy.float64, numpy.float64],
    desired: Tuple[float, float],
    rtol: float,
    atol: int,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.float64,
    rtol: float,
    atol: float,
    err_msg: Literal["Y^0_0 incorrect"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    atol: float,
    err_msg: Literal["Y^-1_1 incorrect"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    atol: float,
    err_msg: Literal["Y^0_1 incorrect"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    atol: float,
    err_msg: Literal["Y^1_1 incorrect"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.float64, desired: float, rtol: numpy.float64, atol: int
):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_allclose(actual: List[numpy.int64], desired: numpy.ndarray):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: List[numpy.float64], rtol: float, atol: float
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.float64,
    desired: float,
    rtol: float,
    atol: float,
    err_msg: Literal["binom"],
    verbose: bool,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.float64,
    desired: numpy.float64,
    rtol: float,
    atol: float,
    err_msg: Literal["binom - kurtosis"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: float, desired: numpy.ndarray, rtol: float, atol: float):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: float, desired: numpy.float64, rtol: float, atol: float):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.float64,
    desired: float,
    rtol: float,
    atol: float,
    err_msg: Literal["boltzmann"],
    verbose: bool,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.float64,
    desired: numpy.float64,
    rtol: float,
    atol: float,
    err_msg: Literal["boltzmann - kurtosis"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.float64,
    desired: float,
    rtol: float,
    atol: float,
    err_msg: Literal["dlaplace"],
    verbose: bool,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.float64,
    desired: numpy.float64,
    rtol: float,
    atol: float,
    err_msg: Literal["dlaplace - kurtosis"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.float64,
    desired: float,
    rtol: float,
    atol: float,
    err_msg: Literal["geom"],
    verbose: bool,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.float64,
    desired: numpy.float64,
    rtol: float,
    atol: float,
    err_msg: Literal["geom - kurtosis"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.float64,
    desired: float,
    rtol: float,
    atol: float,
    err_msg: Literal["nbinom"],
    verbose: bool,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.float64,
    desired: numpy.float64,
    rtol: float,
    atol: float,
    err_msg: Literal["nbinom - kurtosis"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.float64,
    desired: float,
    rtol: float,
    atol: float,
    err_msg: Literal["planck"],
    verbose: bool,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.float64,
    desired: numpy.float64,
    rtol: float,
    atol: float,
    err_msg: Literal["planck - kurtosis"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.float64,
    desired: float,
    rtol: float,
    atol: float,
    err_msg: Literal["poisson"],
    verbose: bool,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.float64,
    desired: numpy.float64,
    rtol: float,
    atol: float,
    err_msg: Literal["poisson - kurtosis"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.float64,
    desired: float,
    rtol: float,
    atol: float,
    err_msg: Literal["randint"],
    verbose: bool,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.float64,
    desired: numpy.float64,
    rtol: float,
    atol: float,
    err_msg: Literal["randint - kurtosis"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.float64,
    desired: float,
    rtol: float,
    atol: float,
    err_msg: Literal["sample distribution"],
    verbose: bool,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: List[numpy.float64], desired: numpy.ndarray, rtol: float, atol: int
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: List[Union[float, int]], rtol: float, atol: int
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: List[numpy.float64], desired: List[float]):
    """
    usage.scipy: 5
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray, numpy.ndarray],
    desired: List[int],
    rtol: float,
    atol: float,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray, numpy.ndarray],
    desired: List[Union[float, numpy.float64]],
    rtol: float,
    atol: float,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray, numpy.ndarray],
    desired: List[Union[float, int]],
    rtol: float,
    atol: float,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.float64, desired: numpy.ndarray, atol: float):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray, numpy.ndarray],
    desired: List[Union[float, numpy.float64]],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray, numpy.ndarray],
    desired: Tuple[
        numpy.ndarray,
        numpy.ndarray,
        List[Union[numpy.float64, int, float]],
        List[Union[float, int]],
    ],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[numpy.ndarray, numpy.ndarray],
    desired: Tuple[numpy.float64, numpy.float64],
    rtol: float,
    atol: float,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[numpy.ndarray, numpy.ndarray], desired: Tuple[float, float]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray, numpy.ndarray],
    desired: List[float],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: List[numpy.ndarray]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: List[List[float]], atol: float):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: List[numpy.float64], desired: List[Union[int, float]], atol: float
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: List[numpy.float64], desired: List[int], atol: float):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: List[float], rtol: float, atol: int
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: List[Union[int, numpy.float64]], atol: float
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[float, numpy.float64, numpy.float64, numpy.float64],
    desired: Tuple[float, numpy.float64, numpy.float64, numpy.float64],
    rtol: float,
    atol: float,
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[numpy.float64, float, numpy.float64, numpy.float64],
    desired: Tuple[numpy.float64, float, numpy.float64, numpy.float64],
    rtol: float,
    atol: float,
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[int, numpy.float64, numpy.float64],
    desired: Tuple[int, numpy.float64, numpy.float64],
    rtol: float,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.int64, desired: float, rtol: float):
    """
    usage.scipy: 16
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[float, float], desired: List[float], atol: float, err_msg: str
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[float, float], desired: List[Union[float, int]], atol: float
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[numpy.float64, numpy.float64],
    desired: Tuple[float, float],
    rtol: float,
):
    """
    usage.scipy: 6
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[numpy.float64, numpy.float64, numpy.float64], desired: List[float]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: scipy.stats.morestats.WilcoxonResult, desired: Tuple[float, float]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: List[numpy.float64], desired: List[float], rtol: float):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[numpy.float64, numpy.float64, numpy.float64],
    desired: List[float],
    rtol: float,
    atol: float,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: List[numpy.float64], desired: numpy.ndarray, rtol: float):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(actual: Tuple[float, float], desired: List[float]):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: List[numpy.float64], rtol: float):
    """
    usage.scipy: 6
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ma.core.MaskedArray, desired: numpy.ndarray, rtol: float
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ma.core.MaskedArray, desired: numpy.ma.core.MaskedArray, rtol: float
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ma.core.MaskedArray, desired: List[float], rtol: float
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: scipy.stats.mstats_basic.NormaltestResult,
    desired: scipy.stats.mstats_basic.NormaltestResult,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: scipy.stats.mstats_basic.SkewtestResult,
    desired: scipy.stats.mstats_basic.SkewtestResult,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: scipy.stats.mstats_basic.KurtosistestResult,
    desired: scipy.stats.mstats_basic.KurtosistestResult,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: scipy.stats.mstats_basic.NormaltestResult,
    desired: scipy.stats.stats.NormaltestResult,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: scipy.stats.mstats_basic.SkewtestResult,
    desired: scipy.stats.stats.SkewtestResult,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: scipy.stats.mstats_basic.KurtosistestResult,
    desired: scipy.stats.stats.KurtosistestResult,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.ma.core.MaskedArray, desired: List[numpy.float64]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: scipy.stats.stats.Ttest_relResult,
    desired: scipy.stats.mstats_basic.Ttest_relResult,
):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_allclose(
    actual: scipy.stats.mstats_basic.Ttest_relResult,
    desired: scipy.stats.mstats_basic.Ttest_relResult,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: scipy.stats.stats.Ttest_indResult,
    desired: scipy.stats.mstats_basic.Ttest_indResult,
):
    """
    usage.scipy: 5
    """
    ...


@overload
def assert_allclose(
    actual: scipy.stats.mstats_basic.Ttest_indResult,
    desired: scipy.stats.mstats_basic.Ttest_indResult,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: scipy.stats.stats.Ttest_1sampResult,
    desired: scipy.stats.mstats_basic.Ttest_1sampResult,
):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_allclose(
    actual: scipy.stats.mstats_basic.Ttest_1sampResult,
    desired: scipy.stats.mstats_basic.Ttest_1sampResult,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ma.core.MaskedArray, rtol: float
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(actual: numpy.ma.core.MaskedArray, desired: float, atol: float):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ma.core.MaskedArray, atol: float
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.ma.core.MaskedArray, desired: int, rtol: float):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(actual: numpy.ma.core.MaskedArray, desired: List[int]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[numpy.float64, numpy.float64], desired: Tuple[int, float]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.float64, desired: numpy.ndarray):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: List[List[Union[float, int]]], rtol: float
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: List[List[List[Union[int, float]]]], rtol: float
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: List[List[List[List[Union[float, int]]]]],
    rtol: float,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: List[List[float]], rtol: float):
    """
    usage.scipy: 2
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: List[List[List[float]]], rtol: float
):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: List[numpy.ndarray], rtol: float):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: List[List[numpy.ndarray]], rtol: float
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: List[numpy.float64],
    desired: List[Union[numpy.int64, numpy.float64]],
    rtol: float,
    atol: float,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.float64, desired: float, atol: numpy.float64):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: List[numpy.float64], desired: List[float], rtol: float, atol: int
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: scipy.stats.stats.SpearmanrResult,
    desired: scipy.stats.stats.SpearmanrResult,
):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_allclose(
    actual: scipy.stats.mstats_basic.SpearmanrResult,
    desired: scipy.stats.mstats_basic.SpearmanrResult,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[numpy.float64, numpy.float64, numpy.float64],
    desired: Tuple[float, float, float],
    rtol: float,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: scipy.stats.mstats_basic.SpearmanrResult, desired: Tuple[float, int]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: scipy.stats.mstats_basic.KendalltauResult,
    desired: Tuple[float, float],
    rtol: float,
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: list):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: scipy.stats.mstats_basic.Ttest_relResult,
    desired: scipy.stats.stats.Ttest_relResult,
    atol: float,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: scipy.stats.mstats_basic.Ttest_relResult,
    desired: Tuple[int, float],
    atol: float,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: scipy.stats.mstats_basic.Ttest_indResult,
    desired: scipy.stats.stats.Ttest_indResult,
    atol: float,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: scipy.stats.mstats_basic.Ttest_indResult,
    desired: Tuple[float, float],
    atol: float,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[numpy.ndarray, numpy.ndarray],
    desired: Tuple[List[float], List[float]],
    rtol: float,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.matrix, desired: numpy.matrix, rtol: float):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_allclose(actual: numpy.float32, desired: numpy.float64, rtol: float):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.ma.core.MaskedArray, desired: numpy.ndarray):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.float64, desired: float, rtol: float, err_msg: str):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: float, rtol: int, atol: float):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: Tuple[
        float, float, float, float, float, float, float, float, float, float
    ],
    rtol: int,
    atol: float,
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[numpy.float64, numpy.float64], desired: Tuple[float, float]
):
    """
    usage.matplotlib: 9
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[numpy.float64, numpy.float64],
    desired: Tuple[numpy.float64, numpy.float64],
):
    """
    usage.matplotlib: 4
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[numpy.float64, numpy.float64, numpy.float64, numpy.float64],
    desired: Tuple[numpy.float64, numpy.float64, numpy.float64, numpy.float64],
    atol: float,
):
    """
    usage.matplotlib: 8
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: range):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def assert_allclose(actual: Tuple[numpy.float64, numpy.float64], desired: List[float]):
    """
    usage.matplotlib: 3
    """
    ...


@overload
def assert_allclose(actual: Tuple[int, int], desired: Tuple[int, int], rtol: float):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ma.core.MaskedArray, desired: numpy.ma.core.MaskedArray
):
    """
    usage.matplotlib: 2
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[numpy.uint8, numpy.uint8, numpy.uint8, numpy.uint8, numpy.uint8],
    desired: List[numpy.uint8],
):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: List[Tuple[int, int]]):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: List[Tuple[Union[int, numpy.float64], Union[int, numpy.float64]]],
    atol: float,
):
    """
    usage.matplotlib: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: List[List[Union[float, int]]],
    err_msg: numpy.ndarray,
):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[numpy.float64, numpy.float64, numpy.float64, numpy.float64],
    desired: List[Union[int, float]],
):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[numpy.float64, numpy.float64, numpy.float64, numpy.float64],
    desired: List[Union[float, int]],
):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def assert_allclose(actual: float, desired: numpy.float32, rtol: float):
    """
    usage.sklearn: 7
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    atol: float,
    err_msg: Literal[""],
):
    """
    usage.sklearn: 7
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: pandas.core.frame.DataFrame):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.float64,
    desired: numpy.float64,
    rtol: float,
    atol: float,
    err_msg: Literal[""],
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["StackingClassifier"],
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["StackingRegressor"],
):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["VotingRegressor"],
):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["VotingClassifier"],
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(actual: List[numpy.int64], desired: List[numpy.int64]):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.float32, desired: numpy.float64, rtol: float, atol: float
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.float64, desired: numpy.float64, err_msg: str):
    """
    usage.sklearn: 24
    """
    ...


@overload
def assert_allclose(actual: numpy.int64, desired: numpy.int64, err_msg: str):
    """
    usage.sklearn: 16
    """
    ...


@overload
def assert_allclose(actual: float, desired: float, err_msg: str):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray],
    desired: Tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray],
    err_msg: str,
):
    """
    usage.sklearn: 5
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray],
    desired: Tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray],
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.int64, desired: numpy.float64, err_msg: str):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: List[List[numpy.float64]]):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["LocalOutlierFactor"],
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["ARDRegression"],
):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["AdaBoostClassifier"],
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["AdaBoostRegressor"],
):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["BaggingClassifier"],
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["BaggingRegressor"],
):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["BayesianRidge"],
):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["BernoulliNB"],
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["CategoricalNB"],
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["ComplementNB"],
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["DummyClassifier"],
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["DummyRegressor"],
):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["ElasticNet"],
):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["ElasticNetCV"],
):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["EllipticEnvelope"],
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["ExtraTreeClassifier"],
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["ExtraTreeRegressor"],
):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["ExtraTreesClassifier"],
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["ExtraTreesRegressor"],
):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.memmap, desired: numpy.memmap, rtol: float, atol: float, err_msg: str
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["GammaRegressor"],
):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["GaussianNB"],
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["HuberRegressor"],
):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["IsolationForest"],
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(
    actual: float, desired: float, rtol: float, atol: float, err_msg: Literal[""]
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["KNeighborsClassifier"],
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["KNeighborsRegressor"],
):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["KernelRidge"],
):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["LabelPropagation"],
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["LabelSpreading"],
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, atol: float, err_msg: Literal["Lars"]
):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["LarsCV"],
):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["Lasso"],
):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["LassoCV"],
):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["LassoLars"],
):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["LassoLarsCV"],
):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["LassoLarsIC"],
):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["LinearRegression"],
):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["LinearSVC"],
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["LinearSVR"],
):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["LogisticRegression"],
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["LogisticRegressionCV"],
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["MLPClassifier"],
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["MLPRegressor"],
):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["MultiOutputRegressor"],
):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["MultiTaskElasticNet"],
):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["MultiTaskLasso"],
):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["MultiTaskLassoCV"],
):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["MultinomialNB"],
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["NearestCentroid"],
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["NuSVC"],
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["NuSVR"],
):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["OneClassSVM"],
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["OneVsOneClassifier"],
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["OneVsRestClassifier"],
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["OutputCodeClassifier"],
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["PLSCanonical"],
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["PLSRegression"],
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["Perceptron"],
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["PoissonRegressor"],
):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["RANSACRegressor"],
):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, atol: float, err_msg: Literal["RFE"]
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["RFECV"],
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["RegressorChain"],
):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["Ridge"],
):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["RidgeCV"],
):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["RidgeClassifier"],
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["RidgeClassifierCV"],
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["SGDClassifier"],
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["SGDRegressor"],
):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, atol: float, err_msg: Literal["SVC"]
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, atol: float, err_msg: Literal["SVR"]
):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["TheilSenRegressor"],
):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["TweedieRegressor"],
):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    err_msg: Literal["solver svd"],
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    err_msg: Literal["solver lsqr"],
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    rtol: float,
    err_msg: Literal["solver eigen"],
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: numpy.ndarray, atol: int):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(
    actual: Tuple[float, float, float, float],
    desired: Tuple[numpy.float64, numpy.float64, numpy.float64, numpy.float64],
    rtol: float,
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    atol: float,
    err_msg: Literal["estimator_name"],
):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: List[numpy.ndarray], atol: float):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(
    actual: List[List[int]],
    desired: List[List[int]],
    rtol: float,
    atol: float,
    err_msg: Literal[""],
):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_allclose(
    actual: pandas.core.frame.DataFrame,
    desired: pandas.core.frame.DataFrame,
    rtol: float,
    atol: float,
    err_msg: Literal[""],
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(
    actual: List[int],
    desired: List[int],
    rtol: float,
    atol: float,
    err_msg: Literal[""],
):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_allclose(
    actual: pandas.core.series.Series,
    desired: pandas.core.series.Series,
    rtol: float,
    atol: float,
    err_msg: Literal[""],
):
    """
    usage.sklearn: 1
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
    usage.scipy: 4705
    usage.skimage: 158
    usage.sklearn: 760
    usage.xarray: 38
    """
    ...


@overload
def assert_almost_equal(actual: numpy.float64, desired: int):
    """
    usage.scipy: 41
    usage.skimage: 7
    usage.sklearn: 141
    """
    ...


@overload
def assert_almost_equal(actual: numpy.float64, desired: float):
    """
    usage.matplotlib: 8
    usage.scipy: 173
    usage.skimage: 47
    usage.sklearn: 189
    """
    ...


@overload
def assert_almost_equal(actual: numpy.ndarray, desired: numpy.ndarray, decimal: int):
    """
    usage.scipy: 43
    usage.skimage: 15
    usage.sklearn: 77
    """
    ...


@overload
def assert_almost_equal(actual: numpy.float64, desired: float, decimal: int):
    """
    usage.matplotlib: 3
    usage.scipy: 164
    usage.skimage: 35
    usage.sklearn: 109
    """
    ...


@overload
def assert_almost_equal(actual: numpy.float64, desired: numpy.float64, decimal: int):
    """
    usage.scipy: 64
    usage.skimage: 6
    usage.sklearn: 47
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
    usage.matplotlib: 23
    usage.scipy: 205
    usage.skimage: 116
    usage.sklearn: 127
    """
    ...


@overload
def assert_almost_equal(actual: numpy.ndarray, desired: int, decimal: int):
    """
    usage.skimage: 1
    usage.sklearn: 3
    """
    ...


@overload
def assert_almost_equal(actual: numpy.ndarray, desired: List[int], decimal: int):
    """
    usage.scipy: 1
    usage.skimage: 1
    """
    ...


@overload
def assert_almost_equal(actual: numpy.ndarray, desired: numpy.float64, decimal: int):
    """
    usage.scipy: 3
    usage.skimage: 1
    usage.sklearn: 8
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
    usage.scipy: 10
    usage.skimage: 5
    usage.sklearn: 10
    """
    ...


@overload
def assert_almost_equal(actual: numpy.ndarray, desired: List[float]):
    """
    usage.scipy: 19
    usage.skimage: 2
    usage.sklearn: 3
    """
    ...


@overload
def assert_almost_equal(actual: numpy.ndarray, desired: List[int]):
    """
    usage.scipy: 46
    usage.skimage: 1
    usage.sklearn: 6
    """
    ...


@overload
def assert_almost_equal(actual: numpy.float64, desired: numpy.float64):
    """
    usage.matplotlib: 2
    usage.scipy: 67
    usage.skimage: 21
    usage.sklearn: 131
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
    usage.scipy: 6
    usage.skimage: 5
    usage.sklearn: 2
    """
    ...


@overload
def assert_almost_equal(actual: numpy.ndarray, desired: numpy.float64):
    """
    usage.scipy: 5
    usage.skimage: 1
    usage.sklearn: 9
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
    usage.sklearn: 2
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
    usage.scipy: 1
    usage.skimage: 3
    usage.sklearn: 2
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
    usage.matplotlib: 1
    usage.scipy: 42
    usage.skimage: 16
    usage.sklearn: 33
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
    usage.scipy: 13
    usage.skimage: 3
    usage.sklearn: 4
    """
    ...


@overload
def assert_almost_equal(actual: float, desired: int):
    """
    usage.scipy: 6
    usage.skimage: 8
    usage.sklearn: 10
    """
    ...


@overload
def assert_almost_equal(actual: Tuple[float, float], desired: Tuple[float, float]):
    """
    usage.matplotlib: 1
    usage.scipy: 1
    usage.skimage: 3
    """
    ...


@overload
def assert_almost_equal(actual: numpy.ndarray, desired: List[Union[int, float]]):
    """
    usage.scipy: 7
    usage.skimage: 2
    usage.sklearn: 1
    """
    ...


@overload
def assert_almost_equal(actual: numpy.ndarray, desired: List[List[int]]):
    """
    usage.skimage: 4
    usage.sklearn: 1
    """
    ...


@overload
def assert_almost_equal(actual: numpy.ndarray, desired: float):
    """
    usage.matplotlib: 4
    usage.scipy: 17
    usage.sklearn: 5
    """
    ...


@overload
def assert_almost_equal(actual: float, desired: numpy.float64):
    """
    usage.scipy: 9
    usage.sklearn: 9
    """
    ...


@overload
def assert_almost_equal(actual: numpy.int64, desired: numpy.ndarray):
    """
    usage.scipy: 4
    usage.sklearn: 1
    """
    ...


@overload
def assert_almost_equal(actual: complex, desired: complex):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_almost_equal(actual: float, desired: numpy.ndarray):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(actual: numpy.float32, desired: numpy.float32):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(actual: numpy.complex64, desired: numpy.complex64):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(actual: numpy.complex128, desired: numpy.complex128):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_almost_equal(actual: numpy.float64, desired: numpy.complex128):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(actual: float, desired: numpy.float32, decimal: int):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(actual: numpy.int64, desired: float):
    """
    usage.scipy: 10
    usage.sklearn: 1
    """
    ...


@overload
def assert_almost_equal(actual: numpy.uint64, desired: float):
    """
    usage.scipy: 9
    """
    ...


@overload
def assert_almost_equal(actual: numpy.float32, desired: float):
    """
    usage.scipy: 9
    """
    ...


@overload
def assert_almost_equal(actual: numpy.int8, desired: float):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_almost_equal(actual: numpy.uint8, desired: float):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_almost_equal(actual: numpy.int16, desired: float):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_almost_equal(actual: numpy.uint16, desired: float):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_almost_equal(actual: numpy.int32, desired: float):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_almost_equal(actual: numpy.uint32, desired: float):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_almost_equal(actual: numpy.bool_, desired: float):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_almost_equal(actual: numpy.ndarray, desired: float, decimal: int):
    """
    usage.scipy: 10
    """
    ...


@overload
def assert_almost_equal(actual: numpy.ndarray, desired: Tuple[float, float]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(actual: numpy.ndarray, desired: List[float], decimal: int):
    """
    usage.scipy: 21
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.ndarray, desired: List[Union[float, int]], decimal: int
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    decimal: int,
    err_msg: Literal["N regression"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(actual: numpy.ndarray, desired: List[complex]):
    """
    usage.scipy: 5
    """
    ...


@overload
def assert_almost_equal(actual: numpy.ndarray, desired: List[Union[complex, int]]):
    """
    usage.scipy: 6
    """
    ...


@overload
def assert_almost_equal(actual: numpy.ndarray, desired: List[Union[int, complex]]):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.ndarray, desired: List[Union[int, complex, float]]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.ndarray, desired: List[Union[complex, float]], decimal: int
):
    """
    usage.scipy: 6
    """
    ...


@overload
def assert_almost_equal(actual: numpy.ndarray, desired: List[complex], decimal: int):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.ndarray, desired: List[numpy.complex128], decimal: int
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(actual: numpy.matrix, desired: numpy.matrix):
    """
    usage.scipy: 7
    """
    ...


@overload
def assert_almost_equal(actual: numpy.matrix, desired: numpy.ndarray):
    """
    usage.scipy: 7
    """
    ...


@overload
def assert_almost_equal(actual: numpy.ndarray, desired: numpy.matrix):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: int, err_msg: Literal["2 ; 3 ; 1"]
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: int, err_msg: Literal["-1 ; 8 ; 1"]
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: int, err_msg: Literal["-1 ; -2 ; 1"]
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: int, err_msg: Literal["array(-1) ; -2 ; 1"]
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: int, err_msg: Literal["-1 ; array(-2) ; 1"]
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_almost_equal(actual: numpy.float64, desired: int, err_msg: str):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_almost_equal(actual: float, desired: float, decimal: int):
    """
    usage.scipy: 31
    usage.sklearn: 5
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.ndarray, desired: numpy.ndarray, decimal: int, err_msg: str
):
    """
    usage.scipy: 7
    usage.sklearn: 2
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.complex128, desired: numpy.complex128, decimal: int
):
    """
    usage.scipy: 14
    """
    ...


@overload
def assert_almost_equal(actual: numpy.complex128, desired: complex):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64,
    desired: numpy.float64,
    decimal: int,
    err_msg: Literal["test #0"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64,
    desired: numpy.float64,
    decimal: int,
    err_msg: Literal["test #1"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64,
    desired: numpy.float64,
    decimal: int,
    err_msg: Literal["test #2"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: float, decimal: int, err_msg: Literal["test #3"]
):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64,
    desired: numpy.float64,
    decimal: int,
    err_msg: Literal["test #4"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64,
    desired: numpy.float64,
    decimal: int,
    err_msg: Literal["test #5"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64,
    desired: numpy.float64,
    decimal: int,
    err_msg: Literal["test #6"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64,
    desired: numpy.float64,
    decimal: int,
    err_msg: Literal["test #7"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64,
    desired: numpy.float64,
    decimal: int,
    err_msg: Literal["test #8"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: float, decimal: int, err_msg: Literal["test #9"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: float, decimal: int, err_msg: Literal["test #10"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: float, decimal: int, err_msg: Literal["test #11"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: float, decimal: int, err_msg: Literal["test #12"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: float, decimal: int, err_msg: Literal["test #13"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: float, decimal: int, err_msg: Literal["test #14"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: float, decimal: int, err_msg: Literal["test #15"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: float, decimal: int, err_msg: Literal["test #0"]
):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: float, decimal: int, err_msg: Literal["test #1"]
):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: float, decimal: int, err_msg: Literal["test #2"]
):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: float, decimal: int, err_msg: Literal["test #4"]
):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: float, decimal: int, err_msg: Literal["test #5"]
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: float, decimal: int, err_msg: Literal["test #6"]
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: float, decimal: int, err_msg: Literal["test #7"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(actual: numpy.ndarray, desired: numpy.float64, err_msg: str):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(actual: numpy.float64, desired: numpy.float64, err_msg: str):
    """
    usage.scipy: 1
    usage.sklearn: 3
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: numpy.float64, err_msg: Literal["orth.laguerre(0)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: numpy.float64, err_msg: Literal["orth.hermite(0)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64,
    desired: numpy.float64,
    err_msg: Literal["orth.hermitenorm(0)"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: numpy.float64, err_msg: Literal["orth.chebyt(0)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.ndarray, desired: numpy.float64, err_msg: Literal["orth.chebyu(0)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: numpy.float64, err_msg: Literal["orth.chebyc(0)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: numpy.float64, err_msg: Literal["orth.chebys(0)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.ndarray, desired: numpy.float64, err_msg: Literal["orth.sh_chebyt(0)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.ndarray, desired: numpy.float64, err_msg: Literal["orth.sh_chebyu(0)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: numpy.float64, err_msg: Literal["orth.legendre(0)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64,
    desired: numpy.float64,
    err_msg: Literal["orth.sh_legendre(0)"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: numpy.float64, err_msg: Literal["orth.laguerre(1)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: numpy.float64, err_msg: Literal["orth.hermite(1)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64,
    desired: numpy.float64,
    err_msg: Literal["orth.hermitenorm(1)"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: numpy.float64, err_msg: Literal["orth.chebyt(1)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: numpy.float64, err_msg: Literal["orth.chebyu(1)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: numpy.float64, err_msg: Literal["orth.chebyc(1)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: numpy.float64, err_msg: Literal["orth.chebys(1)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: numpy.float64, err_msg: Literal["orth.sh_chebyt(1)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: numpy.float64, err_msg: Literal["orth.sh_chebyu(1)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: numpy.float64, err_msg: Literal["orth.legendre(1)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64,
    desired: numpy.float64,
    err_msg: Literal["orth.sh_legendre(1)"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: numpy.float64, err_msg: Literal["orth.laguerre(2)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: numpy.float64, err_msg: Literal["orth.hermite(2)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64,
    desired: numpy.float64,
    err_msg: Literal["orth.hermitenorm(2)"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: numpy.float64, err_msg: Literal["orth.chebyt(2)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: numpy.float64, err_msg: Literal["orth.chebyu(2)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: numpy.float64, err_msg: Literal["orth.chebyc(2)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: numpy.float64, err_msg: Literal["orth.chebys(2)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: numpy.float64, err_msg: Literal["orth.sh_chebyt(2)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: numpy.float64, err_msg: Literal["orth.sh_chebyu(2)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: numpy.float64, err_msg: Literal["orth.legendre(2)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64,
    desired: numpy.float64,
    err_msg: Literal["orth.sh_legendre(2)"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: numpy.float64, err_msg: Literal["orth.laguerre(3)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: numpy.float64, err_msg: Literal["orth.hermite(3)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64,
    desired: numpy.float64,
    err_msg: Literal["orth.hermitenorm(3)"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: numpy.float64, err_msg: Literal["orth.chebyt(3)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: numpy.float64, err_msg: Literal["orth.chebyu(3)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: numpy.float64, err_msg: Literal["orth.chebyc(3)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: numpy.float64, err_msg: Literal["orth.chebys(3)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: numpy.float64, err_msg: Literal["orth.sh_chebyt(3)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: numpy.float64, err_msg: Literal["orth.sh_chebyu(3)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: numpy.float64, err_msg: Literal["orth.legendre(3)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64,
    desired: numpy.float64,
    err_msg: Literal["orth.sh_legendre(3)"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: numpy.float64, err_msg: Literal["orth.laguerre(4)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: numpy.float64, err_msg: Literal["orth.hermite(4)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64,
    desired: numpy.float64,
    err_msg: Literal["orth.hermitenorm(4)"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: numpy.float64, err_msg: Literal["orth.chebyt(4)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: numpy.float64, err_msg: Literal["orth.chebyu(4)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: numpy.float64, err_msg: Literal["orth.chebyc(4)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: numpy.float64, err_msg: Literal["orth.chebys(4)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: numpy.float64, err_msg: Literal["orth.sh_chebyt(4)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: numpy.float64, err_msg: Literal["orth.sh_chebyu(4)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: numpy.float64, err_msg: Literal["orth.legendre(4)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64,
    desired: numpy.float64,
    err_msg: Literal["orth.sh_legendre(4)"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.ndarray, desired: List[float], decimal: int, err_msg: str
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: numpy.float64, decimal: int, err_msg: str
):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.ndarray,
    desired: List[numpy.float64],
    decimal: int,
    err_msg: Literal["alpha - ppf multiple"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: List[numpy.float64], decimal: int, err_msg: str
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.ndarray,
    desired: List[numpy.float64],
    decimal: int,
    err_msg: Literal["argus - ppf multiple"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.ndarray,
    desired: List[numpy.float64],
    decimal: int,
    err_msg: Literal["beta - ppf multiple"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.ndarray, desired: List[numpy.float64], decimal: int, err_msg: str
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.ndarray,
    desired: List[numpy.float64],
    decimal: int,
    err_msg: Literal["burr - ppf multiple"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.ndarray,
    desired: List[numpy.float64],
    decimal: int,
    err_msg: Literal["chi - ppf multiple"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.ndarray,
    desired: List[numpy.float64],
    decimal: int,
    err_msg: Literal["chi2 - ppf multiple"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64,
    desired: List[numpy.float64],
    decimal: int,
    err_msg: Literal["expon - ppf multiple"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.ndarray,
    desired: List[float],
    decimal: int,
    err_msg: Literal["f - sf-isf roundtrip"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.ndarray,
    desired: List[numpy.float64],
    decimal: int,
    err_msg: Literal["f - ppf multiple"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.ndarray,
    desired: List[numpy.float64],
    decimal: int,
    err_msg: Literal["fisk - ppf multiple"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.ndarray,
    desired: List[numpy.float64],
    decimal: int,
    err_msg: Literal["gamma - ppf multiple"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64,
    desired: List[numpy.float64],
    decimal: int,
    err_msg: Literal["levy - ppf multiple"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.ndarray,
    desired: List[numpy.float64],
    decimal: int,
    err_msg: Literal["lomax - ppf multiple"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64,
    desired: List[numpy.float64],
    decimal: int,
    err_msg: Literal["moyal - ppf multiple"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.ndarray,
    desired: List[numpy.float64],
    decimal: int,
    err_msg: Literal["ncf - ppf multiple"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.ndarray,
    desired: List[numpy.float64],
    decimal: int,
    err_msg: Literal["nct - ppf multiple"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.ndarray,
    desired: List[numpy.float64],
    decimal: int,
    err_msg: Literal["ncx2 - ppf multiple"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64,
    desired: List[numpy.float64],
    decimal: int,
    err_msg: Literal["norm - ppf multiple"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.ndarray,
    desired: List[numpy.float64],
    decimal: int,
    err_msg: Literal["rdist - ppf multiple"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.ndarray,
    desired: List[numpy.float64],
    decimal: int,
    err_msg: Literal["rice - ppf multiple"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.ndarray,
    desired: List[float],
    decimal: int,
    err_msg: Literal["t - sf-isf roundtrip"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.ndarray,
    desired: List[numpy.float64],
    decimal: int,
    err_msg: Literal["t - ppf multiple"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.ndarray,
    desired: List[numpy.float64],
    decimal: int,
    err_msg: Literal["trapz - ppf multiple"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64,
    desired: List[numpy.float64],
    decimal: int,
    err_msg: Literal["wald - ppf multiple"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: float,
    desired: numpy.ndarray,
    decimal: int,
    err_msg: Literal["binom - 1st moment"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: float,
    desired: numpy.ndarray,
    decimal: int,
    err_msg: Literal["binom - 2ndt moment"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: numpy.ndarray, decimal: int, err_msg: str
):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64,
    desired: numpy.float64,
    decimal: int,
    err_msg: Literal["binom - skew"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64,
    desired: numpy.float64,
    decimal: int,
    err_msg: Literal["boltzmann - skew"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: float, desired: numpy.ndarray, decimal: int, err_msg: str
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64,
    desired: numpy.float64,
    decimal: int,
    err_msg: Literal["dlaplace - skew"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: float,
    desired: numpy.ndarray,
    decimal: int,
    err_msg: Literal["geom - 1st moment"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: float,
    desired: numpy.ndarray,
    decimal: int,
    err_msg: Literal["geom - 2ndt moment"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64,
    desired: numpy.float64,
    decimal: int,
    err_msg: Literal["geom - skew"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: float,
    desired: numpy.ndarray,
    decimal: int,
    err_msg: Literal["nbinom - 1st moment"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: float,
    desired: numpy.ndarray,
    decimal: int,
    err_msg: Literal["nbinom - 2ndt moment"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64,
    desired: numpy.float64,
    decimal: int,
    err_msg: Literal["nbinom - skew"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64,
    desired: numpy.ndarray,
    decimal: int,
    err_msg: Literal["planck - 1st moment"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64,
    desired: numpy.ndarray,
    decimal: int,
    err_msg: Literal["planck - 2ndt moment"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64,
    desired: numpy.float64,
    decimal: int,
    err_msg: Literal["planck - skew"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: float,
    desired: numpy.ndarray,
    decimal: int,
    err_msg: Literal["poisson - 1st moment"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64,
    desired: numpy.float64,
    decimal: int,
    err_msg: Literal["poisson - skew"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64,
    desired: numpy.ndarray,
    decimal: int,
    err_msg: Literal["randint - 1st moment"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64,
    desired: numpy.float64,
    decimal: int,
    err_msg: Literal["randint - skew"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: Tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray, numpy.ndarray],
    desired: List[float],
):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    decimal: int,
    err_msg: Literal["quadrature"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.ndarray,
    desired: numpy.ndarray,
    decimal: int,
    err_msg: Literal["zolotarev"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: Tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray, numpy.ndarray],
    desired: Tuple[int, float, float, float],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: Tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray, numpy.ndarray],
    desired: Tuple[int, float, int, int],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(actual: float, desired: int, decimal: int):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64,
    desired: float,
    decimal: int,
    err_msg: Literal["test_540_567"],
):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_almost_equal(
    actual: Tuple[numpy.float64, numpy.float64],
    desired: Tuple[float, float],
    decimal: int,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: Tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray, numpy.ndarray],
    desired: List[Union[float, int]],
    decimal: int,
):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_almost_equal(actual: int, desired: numpy.float64, decimal: int):
    """
    usage.scipy: 3
    usage.sklearn: 4
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
def assert_almost_equal(actual: numpy.ma.core.MaskedArray, desired: numpy.ndarray):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(actual: numpy.ma.core.MaskedArray, desired: List[float]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.ma.core.MaskedArray, desired: List[float], decimal: int
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.ma.core.MaskedArray, desired: numpy.ma.core.MaskedArray
):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64, desired: float, decimal: int, verbose: bool
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(actual: float, desired: float, decimal: int, verbose: bool):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: scipy.stats.stats.SpearmanrResult,
    desired: Tuple[numpy.float64, numpy.float64],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: scipy.stats.stats.SpearmanrResult,
    desired: scipy.stats.mstats_basic.SpearmanrResult,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: Tuple[numpy.float64, numpy.float64], desired: Tuple[float, float]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(actual: List[float], desired: List[float], decimal: int):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: List[Union[numpy.float64, float]], desired: List[float], decimal: int
):
    """
    usage.scipy: 8
    """
    ...


@overload
def assert_almost_equal(
    actual: List[numpy.float64], desired: List[float], decimal: int
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(
    actual: List[numpy.float64], desired: numpy.ndarray, decimal: int
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_almost_equal(
    actual: scipy.stats.mstats_basic.KruskalResult, desired: Tuple[float, float]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_almost_equal(actual: List[numpy.float64], desired: numpy.ndarray):
    """
    usage.matplotlib: 3
    """
    ...


@overload
def assert_almost_equal(actual: list, desired: numpy.ndarray):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def assert_almost_equal(actual: Tuple[float, float], desired: Tuple[int, int]):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def assert_almost_equal(actual: List[numpy.float64], desired: List[float]):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def assert_almost_equal(actual: List[float], desired: numpy.ndarray):
    """
    usage.matplotlib: 2
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.float64,
    desired: numpy.float64,
    decimal: int,
    err_msg: Literal["Unexpected std"],
):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_almost_equal(actual: numpy.float64, desired: float, err_msg: str):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_almost_equal(actual: numpy.float64, desired: numpy.ndarray):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_almost_equal(actual: int, desired: numpy.float64):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_almost_equal(actual: numpy.int64, desired: numpy.int64, err_msg: str):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_almost_equal(actual: numpy.ndarray, desired: numpy.ndarray, err_msg: str):
    """
    usage.sklearn: 3
    """
    ...


@overload
def assert_almost_equal(actual: float, desired: float, err_msg: str):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_almost_equal(actual: numpy.ndarray, desired: List[Union[float, int]]):
    """
    usage.sklearn: 4
    """
    ...


@overload
def assert_almost_equal(actual: numpy.ndarray, desired: List[int], err_msg: str):
    """
    usage.sklearn: 3
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
def assert_approx_equal(actual: numpy.float64, desired: float, significant: int):
    """
    usage.scipy: 61
    """
    ...


@overload
def assert_approx_equal(actual: numpy.float64, desired: float):
    """
    usage.matplotlib: 1
    usage.scipy: 87
    """
    ...


@overload
def assert_approx_equal(actual: numpy.float64, desired: numpy.float64):
    """
    usage.scipy: 10
    usage.sklearn: 1
    """
    ...


@overload
def assert_approx_equal(actual: numpy.float64, desired: int):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_approx_equal(
    actual: numpy.float64, desired: numpy.float64, significant: int
):
    """
    usage.scipy: 13
    usage.sklearn: 1
    """
    ...


@overload
def assert_approx_equal(actual: float, desired: float):
    """
    usage.scipy: 25
    """
    ...


@overload
def assert_approx_equal(actual: float, desired: float, significant: int):
    """
    usage.scipy: 6
    """
    ...


@overload
def assert_approx_equal(
    actual: numpy.float64,
    desired: float,
    significant: int,
    err_msg: Literal["fail forp=0.100000"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_approx_equal(
    actual: numpy.float64,
    desired: float,
    significant: int,
    err_msg: Literal["fail forp=0.125000"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_approx_equal(
    actual: numpy.float64,
    desired: float,
    significant: int,
    err_msg: Literal["fail forp=0.150000"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_approx_equal(
    actual: numpy.float64,
    desired: float,
    significant: int,
    err_msg: Literal["fail forp=0.175000"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_approx_equal(
    actual: numpy.float64,
    desired: float,
    significant: int,
    err_msg: Literal["fail forp=0.200000"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_approx_equal(
    actual: numpy.float64,
    desired: float,
    significant: int,
    err_msg: Literal["fail forp=0.450000"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_approx_equal(
    actual: numpy.float64,
    desired: float,
    significant: int,
    err_msg: Literal["fail forp=0.500000"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_approx_equal(
    actual: numpy.float64,
    desired: float,
    significant: int,
    err_msg: Literal["fail forp=0.550000"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_approx_equal(
    actual: numpy.float64,
    desired: float,
    significant: int,
    err_msg: Literal["fail forp=0.600000"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_approx_equal(
    actual: numpy.float64,
    desired: float,
    significant: int,
    err_msg: Literal["fail forp=0.650000"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_approx_equal(
    actual: numpy.float64,
    desired: float,
    significant: int,
    err_msg: Literal["fail forp=0.850000"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_approx_equal(
    actual: numpy.float64,
    desired: float,
    significant: int,
    err_msg: Literal["fail forp=0.875000"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_approx_equal(
    actual: numpy.float64,
    desired: float,
    significant: int,
    err_msg: Literal["fail forp=0.900000"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_approx_equal(
    actual: numpy.float64,
    desired: float,
    significant: int,
    err_msg: Literal["fail forp=0.925000"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_approx_equal(
    actual: numpy.float64,
    desired: float,
    significant: int,
    err_msg: Literal["fail forp=0.950000"],
):
    """
    usage.scipy: 2
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
    usage.matplotlib: 29
    usage.scipy: 1966
    usage.skimage: 39
    usage.sklearn: 886
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
    usage.matplotlib: 2
    usage.scipy: 188
    usage.skimage: 6
    usage.sklearn: 61
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ndarray, y: List[Union[int, float]]):
    """
    usage.matplotlib: 1
    usage.scipy: 3
    usage.skimage: 3
    usage.sklearn: 4
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ndarray, y: List[float]):
    """
    usage.scipy: 105
    usage.skimage: 1
    usage.sklearn: 67
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
    usage.scipy: 2
    usage.skimage: 1
    usage.sklearn: 7
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
    usage.scipy: 50
    usage.skimage: 5
    usage.sklearn: 14
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ndarray, y: numpy.ndarray, decimal: int):
    """
    usage.matplotlib: 4
    usage.scipy: 249
    usage.sklearn: 226
    """
    ...


@overload
def assert_array_almost_equal(
    x: numpy.ndarray, y: numpy.ndarray, decimal: int, err_msg: Literal["size=1"]
):
    """
    usage.scipy: 8
    """
    ...


@overload
def assert_array_almost_equal(
    x: numpy.ndarray, y: numpy.ndarray, decimal: int, err_msg: Literal["size=51"]
):
    """
    usage.scipy: 8
    """
    ...


@overload
def assert_array_almost_equal(
    x: numpy.ndarray, y: numpy.ndarray, decimal: int, err_msg: Literal["size=111"]
):
    """
    usage.scipy: 8
    """
    ...


@overload
def assert_array_almost_equal(
    x: numpy.ndarray, y: numpy.ndarray, decimal: int, err_msg: Literal["size=100"]
):
    """
    usage.scipy: 8
    """
    ...


@overload
def assert_array_almost_equal(
    x: numpy.ndarray, y: numpy.ndarray, decimal: int, err_msg: Literal["size=200"]
):
    """
    usage.scipy: 8
    """
    ...


@overload
def assert_array_almost_equal(
    x: numpy.ndarray, y: numpy.ndarray, decimal: int, err_msg: Literal["size=64"]
):
    """
    usage.scipy: 8
    """
    ...


@overload
def assert_array_almost_equal(
    x: numpy.ndarray, y: numpy.ndarray, decimal: int, err_msg: Literal["size=128"]
):
    """
    usage.scipy: 8
    """
    ...


@overload
def assert_array_almost_equal(
    x: numpy.ndarray, y: numpy.ndarray, decimal: int, err_msg: Literal["size=256"]
):
    """
    usage.scipy: 8
    """
    ...


@overload
def assert_array_almost_equal(
    x: numpy.ndarray, y: numpy.ndarray, decimal: int, err_msg: Literal["size=1024"]
):
    """
    usage.scipy: 8
    """
    ...


@overload
def assert_array_almost_equal(
    x: numpy.ndarray, y: numpy.ndarray, decimal: int, err_msg: Literal["Size 2 failed"]
):
    """
    usage.scipy: 8
    """
    ...


@overload
def assert_array_almost_equal(
    x: numpy.ndarray, y: numpy.ndarray, decimal: int, err_msg: Literal["Size 3 failed"]
):
    """
    usage.scipy: 8
    """
    ...


@overload
def assert_array_almost_equal(
    x: numpy.ndarray, y: numpy.ndarray, decimal: int, err_msg: Literal["Size 4 failed"]
):
    """
    usage.scipy: 8
    """
    ...


@overload
def assert_array_almost_equal(
    x: numpy.ndarray, y: numpy.ndarray, decimal: int, err_msg: Literal["Size 8 failed"]
):
    """
    usage.scipy: 8
    """
    ...


@overload
def assert_array_almost_equal(
    x: numpy.ndarray, y: numpy.ndarray, decimal: int, err_msg: Literal["Size 12 failed"]
):
    """
    usage.scipy: 8
    """
    ...


@overload
def assert_array_almost_equal(
    x: numpy.ndarray, y: numpy.ndarray, decimal: int, err_msg: Literal["Size 15 failed"]
):
    """
    usage.scipy: 8
    """
    ...


@overload
def assert_array_almost_equal(
    x: numpy.ndarray, y: numpy.ndarray, decimal: int, err_msg: Literal["Size 16 failed"]
):
    """
    usage.scipy: 8
    """
    ...


@overload
def assert_array_almost_equal(
    x: numpy.ndarray, y: numpy.ndarray, decimal: int, err_msg: Literal["Size 17 failed"]
):
    """
    usage.scipy: 8
    """
    ...


@overload
def assert_array_almost_equal(
    x: numpy.ndarray, y: numpy.ndarray, decimal: int, err_msg: Literal["Size 32 failed"]
):
    """
    usage.scipy: 8
    """
    ...


@overload
def assert_array_almost_equal(
    x: numpy.ndarray, y: numpy.ndarray, decimal: int, err_msg: Literal["Size 64 failed"]
):
    """
    usage.scipy: 8
    """
    ...


@overload
def assert_array_almost_equal(
    x: numpy.ndarray,
    y: numpy.ndarray,
    decimal: int,
    err_msg: Literal["Size 128 failed"],
):
    """
    usage.scipy: 8
    """
    ...


@overload
def assert_array_almost_equal(
    x: numpy.ndarray,
    y: numpy.ndarray,
    decimal: int,
    err_msg: Literal["Size 256 failed"],
):
    """
    usage.scipy: 8
    """
    ...


@overload
def assert_array_almost_equal(
    x: numpy.ndarray,
    y: numpy.ndarray,
    decimal: int,
    err_msg: Literal["Size 512 failed"],
):
    """
    usage.scipy: 8
    """
    ...


@overload
def assert_array_almost_equal(
    x: numpy.ndarray,
    y: numpy.ndarray,
    decimal: int,
    err_msg: Literal["Size 1024 failed"],
):
    """
    usage.scipy: 8
    """
    ...


@overload
def assert_array_almost_equal(
    x: Tuple[numpy.ndarray, numpy.ndarray], y: Tuple[List[int], List[int]]
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ndarray, y: List[List[int]]):
    """
    usage.scipy: 298
    usage.sklearn: 4
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ndarray, y: List[List[List[int]]]):
    """
    usage.scipy: 20
    """
    ...


@overload
def assert_array_almost_equal(
    x: numpy.ndarray, y: numpy.ndarray, err_msg: Literal["linear"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_almost_equal(
    x: Tuple[int, int, int, int, int, int], y: List[int], err_msg: Literal["linear"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_almost_equal(
    x: numpy.ndarray, y: numpy.ndarray, err_msg: Literal["cubic"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_almost_equal(
    x: Tuple[int, int, int, int, int, int], y: List[int], err_msg: Literal["cubic"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_almost_equal(
    x: numpy.ndarray, y: numpy.ndarray, err_msg: Literal["slinear"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_almost_equal(
    x: Tuple[int, int, int, int, int, int], y: List[int], err_msg: Literal["slinear"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_almost_equal(
    x: numpy.ndarray, y: numpy.ndarray, err_msg: Literal["quadratic"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_almost_equal(
    x: Tuple[int, int, int, int, int, int], y: List[int], err_msg: Literal["quadratic"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_almost_equal(
    x: numpy.ndarray, y: numpy.ndarray, err_msg: Literal["nearest"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_almost_equal(
    x: Tuple[int, int, int, int, int, int], y: List[int], err_msg: Literal["nearest"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_almost_equal(
    x: numpy.ndarray, y: numpy.ndarray, err_msg: Literal["zero"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_almost_equal(
    x: Tuple[int, int, int, int, int, int], y: List[int], err_msg: Literal["zero"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_almost_equal(
    x: numpy.ndarray, y: numpy.ndarray, err_msg: Literal["previous"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_almost_equal(
    x: Tuple[int, int, int, int, int, int], y: List[int], err_msg: Literal["previous"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_almost_equal(
    x: numpy.ndarray, y: numpy.ndarray, err_msg: Literal["next"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_almost_equal(
    x: Tuple[int, int, int, int, int, int], y: List[int], err_msg: Literal["next"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ndarray, y: float):
    """
    usage.scipy: 21
    usage.sklearn: 15
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ndarray, y: List[Union[float, complex]]):
    """
    usage.scipy: 7
    """
    ...


@overload
def assert_array_almost_equal(x: List[numpy.ndarray], y: List[List[Union[float, int]]]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_almost_equal(x: float, y: numpy.float64):
    """
    usage.scipy: 2
    usage.sklearn: 2
    """
    ...


@overload
def assert_array_almost_equal(x: int, y: numpy.float64):
    """
    usage.scipy: 1
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_almost_equal(
    x: numpy.ndarray, y: numpy.ndarray, decimal: int, err_msg: str
):
    """
    usage.scipy: 8
    usage.sklearn: 5
    """
    ...


@overload
def assert_array_almost_equal(
    x: numpy.matrix, y: numpy.matrix, decimal: int, err_msg: str
):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.matrix, y: numpy.matrix, err_msg: str):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_almost_equal(x: List[List[Union[float, int]]], y: numpy.ndarray):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_almost_equal(x: List[List[Union[int, float]]], y: numpy.ndarray):
    """
    usage.scipy: 3
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_almost_equal(x: List[List[Union[int, complex]]], y: numpy.ndarray):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.matrix, y: numpy.matrix):
    """
    usage.scipy: 93
    """
    ...


@overload
def assert_array_almost_equal(x: List[List[Union[float, int]]], y: numpy.matrix):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_almost_equal(
    x: List[List[Union[int, float, complex]]], y: numpy.matrix
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_almost_equal(x: List[List[int]], y: numpy.matrix):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ndarray, y: List[Union[int, complex]]):
    """
    usage.scipy: 6
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ndarray, y: List[List[Union[complex, int]]]):
    """
    usage.scipy: 10
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ndarray, y: List[Union[complex, int]]):
    """
    usage.scipy: 12
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ndarray, y: List[Union[float, int]]):
    """
    usage.scipy: 1
    usage.sklearn: 4
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ndarray, y: List[List[Union[float, int]]]):
    """
    usage.scipy: 1
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_almost_equal(
    x: numpy.ndarray, y: List[List[Union[complex, int, float]]]
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ndarray, y: List[List[Union[int, complex]]]):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ndarray, y: List[complex]):
    """
    usage.scipy: 6
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ndarray, y: List[List[complex]]):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ndarray, y: List[Union[numpy.float64, int]]):
    """
    usage.scipy: 5
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ndarray, y: List[Union[numpy.complex128, int]]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_almost_equal(x: List[List[float]], y: numpy.ndarray, decimal: int):
    """
    usage.scipy: 10
    """
    ...


@overload
def assert_array_almost_equal(
    x: numpy.ndarray, y: List[List[Union[float, int]]], decimal: int
):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.matrix, y: numpy.ndarray):
    """
    usage.scipy: 6
    usage.sklearn: 5
    """
    ...


@overload
def assert_array_almost_equal(
    x: List[Tuple[numpy.int64, numpy.int64]], y: List[Tuple[numpy.int64, numpy.int64]]
):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_array_almost_equal(x: Tuple[numpy.float64, numpy.float64], y: List[float]):
    """
    usage.scipy: 6
    """
    ...


@overload
def assert_array_almost_equal(x: Tuple[numpy.float64, numpy.float64], y: List[int]):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_array_almost_equal(
    x: List[Tuple[numpy.float64, numpy.float64]], y: List[Tuple[float, float]]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_almost_equal(x: List[int], y: numpy.ndarray):
    """
    usage.scipy: 24
    """
    ...


@overload
def assert_array_almost_equal(x: list, y: numpy.ndarray):
    """
    usage.scipy: 7
    """
    ...


@overload
def assert_array_almost_equal(x: List[list], y: numpy.ndarray):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_almost_equal(x: List[List[int]], y: numpy.ndarray):
    """
    usage.scipy: 173
    """
    ...


@overload
def assert_array_almost_equal(x: List[List[List[int]]], y: numpy.ndarray):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ndarray, y: List[float], decimal: int):
    """
    usage.matplotlib: 4
    usage.scipy: 37
    usage.sklearn: 61
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ndarray, y: List[int], decimal: int):
    """
    usage.scipy: 35
    usage.sklearn: 12
    """
    ...


@overload
def assert_array_almost_equal(
    x: numpy.ndarray, y: Tuple[float, int, float], decimal: int
):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ndarray, y: List[List[float]], decimal: int):
    """
    usage.scipy: 5
    usage.sklearn: 4
    """
    ...


@overload
def assert_array_almost_equal(x: float, y: numpy.float64, decimal: int):
    """
    usage.scipy: 1
    usage.sklearn: 2
    """
    ...


@overload
def assert_array_almost_equal(x: float, y: int):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.float64, y: int):
    """
    usage.scipy: 12
    usage.sklearn: 7
    """
    ...


@overload
def assert_array_almost_equal(x: bool, y: bool):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.bool_, y: bool):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_almost_equal(x: List[float], y: numpy.ndarray):
    """
    usage.matplotlib: 1
    usage.scipy: 3
    usage.sklearn: 2
    """
    ...


@overload
def assert_array_almost_equal(x: List[complex], y: numpy.ndarray):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.float64, y: float):
    """
    usage.matplotlib: 4
    usage.scipy: 8
    usage.sklearn: 7
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.complex128, y: float):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_almost_equal(
    x: numpy.ndarray, y: List[List[Union[int, float]]], decimal: int
):
    """
    usage.scipy: 8
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ndarray, y: numpy.ndarray, err_msg: str):
    """
    usage.scipy: 4
    usage.sklearn: 8
    """
    ...


@overload
def assert_array_almost_equal(
    x: numpy.ndarray, y: List[Union[complex, int]], err_msg: str
):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_array_almost_equal(
    x: numpy.ndarray, y: List[Union[complex, numpy.float64, int]], err_msg: str
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_almost_equal(
    x: numpy.ndarray, y: List[Union[numpy.float64, complex, int]], err_msg: str
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_almost_equal(
    x: numpy.ndarray, y: List[Union[float, int]], decimal: int
):
    """
    usage.scipy: 10
    usage.sklearn: 4
    """
    ...


@overload
def assert_array_almost_equal(
    x: List[Union[int, float]], y: numpy.ndarray, decimal: int
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_almost_equal(x: float, y: numpy.ndarray, decimal: int):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_array_almost_equal(x: float, y: numpy.ndarray):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_almost_equal(x: float, y: float):
    """
    usage.scipy: 1
    usage.sklearn: 2
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ndarray, y: List[Union[int, numpy.float64]]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_almost_equal(
    x: numpy.ndarray, y: List[Union[int, float]], decimal: int
):
    """
    usage.scipy: 1
    usage.sklearn: 3
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ndarray, y: List[numpy.float64]):
    """
    usage.scipy: 7
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ndarray, y: int, decimal: int):
    """
    usage.scipy: 4
    usage.sklearn: 17
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.complex64, y: numpy.complex128, decimal: int):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.complex128, y: numpy.complex128, decimal: int):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.complex256, y: numpy.complex256, decimal: int):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ndarray, y: numpy.float64):
    """
    usage.matplotlib: 1
    usage.scipy: 4
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ndarray, y: numpy.matrix):
    """
    usage.scipy: 12
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ndarray, y: List[List[Union[int, float]]]):
    """
    usage.scipy: 6
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.uint64, y: numpy.uint64):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.int64, y: numpy.int64):
    """
    usage.scipy: 5
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.complex128, y: numpy.complex128):
    """
    usage.scipy: 9
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.float64, y: numpy.float64):
    """
    usage.matplotlib: 3
    usage.scipy: 9
    usage.sklearn: 25
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ulonglong, y: numpy.uint64):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.longlong, y: numpy.int64):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.complex64, y: numpy.complex64):
    """
    usage.scipy: 6
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.float32, y: numpy.float32):
    """
    usage.scipy: 6
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.complex256, y: numpy.complex256):
    """
    usage.scipy: 6
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.float128, y: numpy.float128):
    """
    usage.scipy: 6
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.uint8, y: numpy.uint8):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.int8, y: numpy.int8):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.uint32, y: numpy.uint32):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.int32, y: numpy.int32):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ulonglong, y: numpy.ulonglong):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.longlong, y: numpy.longlong):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.uint16, y: numpy.uint16):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.int16, y: numpy.int16):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.bool_, y: numpy.bool_):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.matrix, y: numpy.ndarray, err_msg: str):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.matrix, y: numpy.matrix, decimal: int):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ndarray, y: numpy.matrix, decimal: int):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ndarray, y: List[List[float]]):
    """
    usage.scipy: 2
    usage.sklearn: 16
    """
    ...


@overload
def assert_array_almost_equal(x: Tuple[numpy.float64, numpy.float64], y: numpy.ndarray):
    """
    usage.matplotlib: 1
    usage.scipy: 1
    """
    ...


@overload
def assert_array_almost_equal(
    x: Tuple[numpy.float64, numpy.float64, numpy.float64, numpy.float64],
    y: numpy.ndarray,
    decimal: int,
):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_array_almost_equal(
    x: Tuple[numpy.float64, numpy.float64, numpy.float64, numpy.float64],
    y: List[numpy.float64],
    decimal: int,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_almost_equal(
    x: Tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray, numpy.ndarray],
    y: Tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray, numpy.ndarray],
    decimal: int,
):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.float64, y: numpy.float64, decimal: int):
    """
    usage.scipy: 3
    usage.sklearn: 13
    """
    ...


@overload
def assert_array_almost_equal(
    x: Tuple[numpy.complex128, numpy.complex128, numpy.complex128, numpy.complex128],
    y: Tuple[numpy.complex128, numpy.complex128, numpy.complex128, numpy.complex128],
    decimal: int,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_almost_equal(
    x: Tuple[numpy.float64, numpy.float64, numpy.float64],
    y: Tuple[numpy.float64, numpy.float64, numpy.float64],
    decimal: int,
):
    """
    usage.scipy: 5
    """
    ...


@overload
def assert_array_almost_equal(
    x: Tuple[numpy.float64, numpy.float64, numpy.float64, numpy.float64],
    y: List[Union[float, numpy.float64]],
    decimal: int,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ndarray, y: float, decimal: int):
    """
    usage.scipy: 2
    usage.sklearn: 3
    """
    ...


@overload
def assert_array_almost_equal(
    x: Tuple[numpy.ndarray, numpy.ndarray],
    y: Tuple[numpy.ndarray, numpy.ndarray],
    decimal: int,
):
    """
    usage.scipy: 9
    """
    ...


@overload
def assert_array_almost_equal(
    x: Tuple[numpy.float64, numpy.float64], y: numpy.ndarray, decimal: int
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_almost_equal(
    x: numpy.ndarray, y: Tuple[numpy.ndarray, numpy.ndarray], decimal: int
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.complex128, y: numpy.float64):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ndarray, y: List[numpy.float64], decimal: int):
    """
    usage.scipy: 3
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_almost_equal(
    x: Tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray, numpy.ndarray],
    y: List[numpy.float64],
    decimal: int,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_almost_equal(x: List[numpy.float64], y: List[float]):
    """
    usage.scipy: 3
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_almost_equal(
    x: Tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray, numpy.ndarray],
    y: List[Union[float, numpy.float64]],
    decimal: int,
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_almost_equal(x: List[numpy.float64], y: List[Union[float, int]]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_almost_equal(x: List[numpy.float64], y: List[numpy.float64]):
    """
    usage.scipy: 1
    usage.sklearn: 2
    """
    ...


@overload
def assert_array_almost_equal(
    x: Tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray, numpy.ndarray],
    y: Tuple[float, float, float, float],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_almost_equal(x: List[float], y: numpy.ndarray, decimal: int):
    """
    usage.matplotlib: 1
    usage.scipy: 8
    """
    ...


@overload
def assert_array_almost_equal(
    x: scipy.stats.morestats.FlignerResult, y: Tuple[float, float], decimal: int
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_almost_equal(
    x: Tuple[numpy.float64, numpy.float64], y: Tuple[float, float], decimal: int
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_almost_equal(x: List[numpy.ndarray], y: List[numpy.ndarray]):
    """
    usage.scipy: 1
    usage.sklearn: 4
    """
    ...


@overload
def assert_array_almost_equal(
    x: List[numpy.float64], y: Tuple[numpy.float64, numpy.float64]
):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.float64, y: numpy.ndarray, decimal: int):
    """
    usage.scipy: 2
    usage.sklearn: 2
    """
    ...


@overload
def assert_array_almost_equal(
    x: scipy.stats._stats_mstats_common.LinregressResult,
    y: Tuple[float, float, float, float, float],
    decimal: int,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_almost_equal(
    x: numpy.ndarray, y: List[List[Union[numpy.float64, float]]]
):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_array_almost_equal(
    x: scipy.stats.mstats_basic.Ttest_1sampResult, y: Tuple[float, float]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_almost_equal(
    x: scipy.stats.stats.FriedmanchisquareResult, y: Tuple[float, float]
):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_array_almost_equal(
    x: scipy.stats.mstats_basic.FriedmanchisquareResult, y: Tuple[float, float]
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_almost_equal(
    x: numpy.ndarray, y: scipy.stats.stats.KstestResult, decimal: int
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_almost_equal(x: List[numpy.float64], y: Tuple[float, float]):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_array_almost_equal(
    x: List[numpy.ndarray], y: Tuple[List[float], List[float]]
):
    """
    usage.scipy: 6
    """
    ...


@overload
def assert_array_almost_equal(
    x: scipy.stats.mstats_basic.Ttest_relResult, y: Tuple[float, float]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_almost_equal(
    x: scipy.stats.stats.Ttest_indResult, y: List[numpy.float64]
):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_array_almost_equal(
    x: scipy.stats.stats.Ttest_indResult, y: List[numpy.ndarray]
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_almost_equal(
    x: scipy.stats.mstats_basic.Ttest_indResult, y: Tuple[float, float]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_almost_equal(
    x: scipy.stats.stats.Ttest_indResult, y: Tuple[numpy.float64, numpy.float64]
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_almost_equal(
    x: scipy.stats.stats.Ttest_indResult, y: Tuple[numpy.ndarray, numpy.ndarray]
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_almost_equal(x: float, y: float, decimal: int):
    """
    usage.scipy: 4
    usage.sklearn: 2
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ma.core.MaskedArray, y: float):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.float64, y: float, decimal: int):
    """
    usage.scipy: 1
    usage.sklearn: 25
    """
    ...


@overload
def assert_array_almost_equal(
    x: scipy.stats.stats.NormaltestResult, y: Tuple[float, float]
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_almost_equal(
    x: scipy.stats.stats.SkewtestResult, y: Tuple[float, float]
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_almost_equal(
    x: scipy.stats.stats.KurtosistestResult, y: Tuple[float, float]
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_almost_equal(
    x: scipy.stats.mstats_basic.SkewtestResult, y: Tuple[float, float]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_almost_equal(
    x: scipy.stats.mstats_basic.KurtosistestResult, y: Tuple[float, float]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_almost_equal(
    x: scipy.stats.mstats_basic.NormaltestResult, y: Tuple[float, float]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_almost_equal(
    x: scipy.stats.stats.MannwhitneyuResult, y: Tuple[float, float], decimal: int
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_almost_equal(
    x: Tuple[numpy.float32, numpy.float32, numpy.float32, numpy.float32],
    y: Tuple[float, float, float, float],
    decimal: int,
):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def assert_array_almost_equal(
    x: Tuple[numpy.float64, numpy.float64, numpy.float64, numpy.float64],
    y: Tuple[numpy.float64, numpy.float64, numpy.float64, numpy.float64],
    decimal: int,
):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ndarray, y: list):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def assert_array_almost_equal(
    x: Tuple[numpy.float64, numpy.float64, numpy.float64, numpy.float64],
    y: Tuple[int, int, int, int],
    decimal: int,
):
    """
    usage.matplotlib: 2
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.float64, y: List[int]):
    """
    usage.matplotlib: 1
    usage.sklearn: 2
    """
    ...


@overload
def assert_array_almost_equal(
    x: numpy.ma.core.MaskedArray, y: numpy.ma.core.MaskedArray
):
    """
    usage.matplotlib: 4
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ma.core.MaskedArray, y: List[Union[int, float]]):
    """
    usage.matplotlib: 3
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ndarray, y: numpy.ma.core.MaskedArray):
    """
    usage.matplotlib: 2
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ma.core.MaskedArray, y: List[int]):
    """
    usage.matplotlib: 2
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ma.core.MaskedArray, y: numpy.ndarray):
    """
    usage.matplotlib: 7
    """
    ...


@overload
def assert_array_almost_equal(x: List[numpy.float64], y: numpy.ma.core.MaskedArray):
    """
    usage.matplotlib: 2
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ma.core.MaskedArray, y: List[float]):
    """
    usage.matplotlib: 2
    """
    ...


@overload
def assert_array_almost_equal(
    x: Tuple[numpy.float64, numpy.float64], y: List[float], decimal: int
):
    """
    usage.matplotlib: 2
    """
    ...


@overload
def assert_array_almost_equal(x: List[List[float]], y: numpy.ndarray):
    """
    usage.matplotlib: 5
    usage.sklearn: 6
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
    x: numpy.ndarray, y: numpy.ndarray, err_msg: Literal["X != TP'"]
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_almost_equal(
    x: numpy.ndarray, y: numpy.ndarray, err_msg: Literal["Y != UQ'"]
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_almost_equal(
    x: numpy.ndarray, y: numpy.ndarray, err_msg: Literal["rotation on X failed"]
):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_array_almost_equal(
    x: numpy.ndarray, y: numpy.ndarray, err_msg: Literal["rotation on Y failed"]
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_almost_equal(
    x: Tuple[numpy.ndarray, numpy.ndarray], y: Tuple[numpy.ndarray, numpy.ndarray]
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ndarray, y: List[int], err_msg: str):
    """
    usage.sklearn: 4
    """
    ...


@overload
def assert_array_almost_equal(x: List[Union[float, int]], y: numpy.ndarray):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ndarray, y: numpy.memmap, decimal: int):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_almost_equal(x: List[numpy.int64], y: numpy.ndarray):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_array_almost_equal(
    x: numpy.ndarray, y: List[Union[float, int]], err_msg: str
):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.float32, y: numpy.float64):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.float32, y: numpy.float64, decimal: int):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ndarray, y: List[List[int]], decimal: int):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_almost_equal(x: List[numpy.int64], y: List[numpy.int64]):
    """
    usage.sklearn: 3
    """
    ...


@overload
def assert_array_almost_equal(
    x: numpy.ndarray,
    y: numpy.ndarray,
    decimal: int,
    err_msg: Literal["with solver = sag"],
):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_array_almost_equal(
    x: numpy.ndarray,
    y: numpy.ndarray,
    decimal: int,
    err_msg: Literal["with solver = saga"],
):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_array_almost_equal(
    x: numpy.ndarray,
    y: numpy.ndarray,
    decimal: int,
    err_msg: Literal["with solver = lbfgs"],
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_almost_equal(
    x: List[numpy.float64], y: List[numpy.float64], decimal: int
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ndarray, y: numpy.ndarray, decimal: bool):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ndarray, y: List[numpy.int64]):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_almost_equal(
    x: numpy.ndarray, y: Tuple[numpy.float64, numpy.float64], decimal: int
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_almost_equal(x: int, y: numpy.float64, decimal: int):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_almost_equal(x: int, y: numpy.int64):
    """
    usage.sklearn: 1
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
    usage.scipy: 11
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
def assert_array_almost_equal_nulp(x: numpy.ndarray, y: numpy.ndarray, nulp: int):
    """
    usage.scipy: 44
    """
    ...


@overload
def assert_array_almost_equal_nulp(x: numpy.ndarray, y: numpy.ndarray, nulp: float):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_array_almost_equal_nulp(x: int, y: int, nulp: int):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_almost_equal_nulp(x: float, y: float, nulp: int):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_almost_equal_nulp(x: numpy.float64, y: numpy.float64, nulp: int):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_almost_equal_nulp(x: float, y: numpy.float64, nulp: int):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_almost_equal_nulp(x: numpy.matrix, y: numpy.ndarray):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_almost_equal_nulp(x: numpy.float64, y: numpy.float64):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_almost_equal_nulp(x: numpy.float64, y: float, nulp: int):
    """
    usage.scipy: 1
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
    usage.matplotlib: 5
    usage.scipy: 25
    usage.skimage: 6
    usage.sklearn: 13
    usage.xarray: 2
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: numpy.ndarray):
    """
    usage.dask: 22
    usage.matplotlib: 106
    usage.scipy: 663
    usage.skimage: 321
    usage.sklearn: 919
    usage.xarray: 164
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: int):
    """
    usage.scipy: 7
    usage.skimage: 13
    usage.sklearn: 10
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
    usage.sklearn: 1
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
    usage.scipy: 38
    usage.skimage: 3
    usage.sklearn: 10
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: List[int]):
    """
    usage.matplotlib: 10
    usage.scipy: 108
    usage.skimage: 11
    usage.sklearn: 190
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
    usage.scipy: 3
    usage.skimage: 8
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: List[List[int]]):
    """
    usage.matplotlib: 12
    usage.scipy: 56
    usage.skimage: 12
    usage.sklearn: 33
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: List[List[float]]):
    """
    usage.matplotlib: 1
    usage.scipy: 8
    usage.skimage: 6
    usage.sklearn: 14
    """
    ...


@overload
def assert_array_equal(x: int, y: int):
    """
    usage.matplotlib: 3
    usage.scipy: 8
    usage.skimage: 7
    usage.sklearn: 2
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
    usage.scipy: 29
    usage.skimage: 1
    usage.sklearn: 2
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
    usage.scipy: 33
    usage.sklearn: 3
    usage.xarray: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.ma.core.MaskedArray, y: numpy.ma.core.MaskedArray):
    """
    usage.matplotlib: 3
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
    usage.scipy: 1
    usage.xarray: 2
    """
    ...


@overload
def assert_array_equal(x: List[int], y: numpy.ndarray):
    """
    usage.matplotlib: 1
    usage.scipy: 3
    usage.sklearn: 26
    usage.xarray: 4
    """
    ...


@overload
def assert_array_equal(x: List[List[int]], y: numpy.ndarray):
    """
    usage.sklearn: 22
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
    usage.matplotlib: 1
    usage.scipy: 1
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
    usage.sklearn: 1
    usage.xarray: 2
    """
    ...


@overload
def assert_array_equal(
    x: pandas.core.indexes.base.Index, y: pandas.core.indexes.base.Index
):
    """
    usage.sklearn: 1
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
    usage.matplotlib: 2
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
    usage.dask: 12
    usage.xarray: 4
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: numpy.float64):
    """
    usage.scipy: 1
    usage.sklearn: 5
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
    usage.scipy: 5
    usage.sklearn: 1
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
    usage.scipy: 1
    usage.sklearn: 8
    usage.xarray: 2
    """
    ...


@overload
def assert_array_equal(x: bool, y: bool):
    """
    usage.scipy: 1
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
    usage.scipy: 2
    usage.xarray: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.float64, y: float):
    """
    usage.scipy: 2
    usage.sklearn: 1
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
def assert_array_equal(x: numpy.ndarray, y: List[Union[int, float]]):
    """
    usage.matplotlib: 1
    usage.scipy: 5
    usage.sklearn: 2
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: List[float]):
    """
    usage.matplotlib: 1
    usage.scipy: 44
    usage.sklearn: 11
    """
    ...


@overload
def assert_array_equal(x: Tuple[numpy.ndarray, numpy.ndarray], y: numpy.ndarray):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: List[Union[float, int]]):
    """
    usage.scipy: 4
    usage.sklearn: 2
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: list):
    """
    usage.scipy: 34
    usage.sklearn: 5
    """
    ...


@overload
def assert_array_equal(x: Tuple[None, ...], y: Tuple[None, ...]):
    """
    usage.scipy: 5
    """
    ...


@overload
def assert_array_equal(x: numpy.matrix, y: numpy.ndarray):
    """
    usage.scipy: 20
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: List[List[bool]]):
    """
    usage.matplotlib: 1
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.matrix, y: int):
    """
    usage.scipy: 1
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: List[Literal[" "]]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: numpy.memmap):
    """
    usage.scipy: 7
    usage.sklearn: 2
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: numpy.ndarray, err_msg: str):
    """
    usage.scipy: 14
    usage.sklearn: 35
    """
    ...


@overload
def assert_array_equal(x: List[Union[int, float]], y: numpy.ndarray):
    """
    usage.scipy: 1
    usage.sklearn: 2
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: List[numpy.float64]):
    """
    usage.matplotlib: 6
    usage.scipy: 6
    usage.sklearn: 8
    """
    ...


@overload
def assert_array_equal(
    x: List[Tuple[Union[None, numpy.float64], Union[numpy.float64, None]]],
    y: List[Tuple[Union[None, int], Union[int, None]]],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(
    x: List[Tuple[numpy.int64, Union[None, numpy.float64]]],
    y: List[Tuple[int, Union[None, int]]],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(
    x: List[Tuple[None, Union[None, numpy.float64]]],
    y: List[Tuple[None, Union[None, int]]],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(
    x: List[Tuple[Union[None, numpy.float64], numpy.int64]],
    y: List[Tuple[Union[None, int], int]],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(
    x: List[Tuple[Union[None, numpy.float64], None]],
    y: List[Tuple[Union[None, int], None]],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(
    x: List[Tuple[numpy.int64, numpy.int64]], y: List[Tuple[int, int]]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: List[Tuple[None, None]], y: List[Tuple[None, None]]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: float, y: float):
    """
    usage.scipy: 2
    usage.sklearn: 2
    """
    ...


@overload
def assert_array_equal(
    x: Tuple[numpy.ndarray, numpy.ndarray], y: Tuple[numpy.ndarray, numpy.ndarray]
):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_array_equal(x: numpy.bool_, y: bool):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: List[List[Union[int, float]]]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_equal(x: list, y: list):
    """
    usage.matplotlib: 2
    usage.scipy: 3
    usage.sklearn: 2
    """
    ...


@overload
def assert_array_equal(x: List[numpy.complex128], y: List[numpy.complex128]):
    """
    usage.scipy: 15
    """
    ...


@overload
def assert_array_equal(x: List[numpy.float64], y: List[numpy.float64]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_equal(x: List[List[numpy.ndarray]], y: List[List[numpy.ndarray]]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: List[complex]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: List[List[complex]]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: numpy.complex128):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.matrix, y: numpy.ndarray, err_msg: str):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_array_equal(x: List[numpy.float64], y: int):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.matrix, y: numpy.matrix):
    """
    usage.scipy: 264
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.float64, y: int):
    """
    usage.scipy: 2
    usage.sklearn: 3
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: numpy.matrix):
    """
    usage.scipy: 18
    """
    ...


@overload
def assert_array_equal(x: numpy.matrix, y: List[List[int]]):
    """
    usage.scipy: 28
    """
    ...


@overload
def assert_array_equal(x: numpy.matrix, y: List[List[Union[float, int]]]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.matrix, y: List[List[Union[int, float]]]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(
    x: numpy.matrix, y: numpy.matrix, err_msg: Literal["slice(None, 2, None)"]
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_equal(
    x: numpy.matrix, y: numpy.matrix, err_msg: Literal["slice(1, 2, None)"]
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_equal(
    x: numpy.matrix, y: numpy.matrix, err_msg: Literal["slice(3, None, None)"]
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_equal(
    x: numpy.matrix, y: numpy.matrix, err_msg: Literal["slice(3, None, 2)"]
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_equal(
    x: numpy.matrix, y: numpy.matrix, err_msg: Literal["slice(8, 3, -1)"]
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_equal(
    x: numpy.matrix, y: numpy.matrix, err_msg: Literal["slice(4, None, -2)"]
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_equal(x: numpy.matrix, y: numpy.matrix, err_msg: Literal["0"]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_equal(x: numpy.matrix, y: numpy.matrix, err_msg: Literal["1"]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_equal(x: numpy.matrix, y: numpy.matrix, err_msg: str):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_array_equal(
    x: numpy.matrix, y: numpy.matrix, err_msg: Literal["slice(1, 5, None)"]
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_equal(x: numpy.matrix, y: numpy.matrix, err_msg: Literal["-1"]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_equal(x: numpy.matrix, y: numpy.matrix, err_msg: Literal["-2"]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_equal(x: numpy.matrix, y: numpy.matrix, err_msg: Literal["-5"]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_equal(x: numpy.matrix, y: numpy.matrix, err_msg: Literal["array(-1)"]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_equal(x: numpy.matrix, y: numpy.matrix, err_msg: Literal["-3"]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_equal(
    x: numpy.matrix, y: numpy.matrix, err_msg: Literal["(slice(8, 3, -1), 0)"]
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_equal(
    x: numpy.matrix, y: numpy.matrix, err_msg: Literal["(slice(8, 3, -1), 1)"]
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_equal(
    x: numpy.matrix, y: numpy.matrix, err_msg: Literal["(0, slice(8, 3, -1))"]
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_equal(
    x: numpy.matrix, y: numpy.matrix, err_msg: Literal["(1, slice(8, 3, -1))"]
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_equal(
    x: numpy.matrix, y: numpy.matrix, err_msg: Literal["slice(None, 5, -1)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.matrix, y: numpy.matrix, err_msg: Literal["(0, 0)"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.matrix, y: numpy.matrix, err_msg: Literal["(0, 1)"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.matrix, y: numpy.matrix, err_msg: Literal["(0, -1)"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.matrix, y: numpy.matrix, err_msg: Literal["(0, -2)"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.matrix, y: numpy.matrix, err_msg: Literal["(0, -5)"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(
    x: numpy.matrix, y: numpy.matrix, err_msg: Literal["(0, array(-1))"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.matrix, y: numpy.matrix, err_msg: Literal["(0, -3)"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.matrix, y: numpy.matrix, err_msg: Literal["(1, 0)"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.matrix, y: numpy.matrix, err_msg: Literal["(1, 1)"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.matrix, y: numpy.matrix, err_msg: Literal["(1, -1)"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.matrix, y: numpy.matrix, err_msg: Literal["(1, -2)"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.matrix, y: numpy.matrix, err_msg: Literal["(1, -5)"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(
    x: numpy.matrix, y: numpy.matrix, err_msg: Literal["(1, array(-1))"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.matrix, y: numpy.matrix, err_msg: Literal["(1, -3)"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.matrix, y: numpy.matrix, err_msg: Literal["(-1, 0)"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.matrix, y: numpy.matrix, err_msg: Literal["(-1, 1)"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.matrix, y: numpy.matrix, err_msg: Literal["(-1, -1)"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.matrix, y: numpy.matrix, err_msg: Literal["(-1, -2)"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.matrix, y: numpy.matrix, err_msg: Literal["(-1, -5)"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(
    x: numpy.matrix, y: numpy.matrix, err_msg: Literal["(-1, array(-1))"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.matrix, y: numpy.matrix, err_msg: Literal["(-1, -3)"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.matrix, y: numpy.matrix, err_msg: Literal["(-2, 0)"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.matrix, y: numpy.matrix, err_msg: Literal["(-2, 1)"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.matrix, y: numpy.matrix, err_msg: Literal["(-2, -1)"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.matrix, y: numpy.matrix, err_msg: Literal["(-2, -2)"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.matrix, y: numpy.matrix, err_msg: Literal["(-2, -5)"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(
    x: numpy.matrix, y: numpy.matrix, err_msg: Literal["(-2, array(-1))"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.matrix, y: numpy.matrix, err_msg: Literal["(-2, -3)"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.matrix, y: numpy.matrix, err_msg: Literal["(-5, 0)"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.matrix, y: numpy.matrix, err_msg: Literal["(-5, 1)"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.matrix, y: numpy.matrix, err_msg: Literal["(-5, -1)"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.matrix, y: numpy.matrix, err_msg: Literal["(-5, -2)"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.matrix, y: numpy.matrix, err_msg: Literal["(-5, -5)"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(
    x: numpy.matrix, y: numpy.matrix, err_msg: Literal["(-5, array(-1))"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.matrix, y: numpy.matrix, err_msg: Literal["(-5, -3)"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(
    x: numpy.matrix, y: numpy.matrix, err_msg: Literal["(array(-1), 0)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(
    x: numpy.matrix, y: numpy.matrix, err_msg: Literal["(array(-1), 1)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(
    x: numpy.matrix, y: numpy.matrix, err_msg: Literal["(array(-1), -1)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(
    x: numpy.matrix, y: numpy.matrix, err_msg: Literal["(array(-1), -2)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(
    x: numpy.matrix, y: numpy.matrix, err_msg: Literal["(array(-1), -5)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(
    x: numpy.matrix, y: numpy.matrix, err_msg: Literal["(array(-1), -3)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.matrix, y: numpy.matrix, err_msg: Literal["(-3, 0)"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.matrix, y: numpy.matrix, err_msg: Literal["(-3, 1)"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.matrix, y: numpy.matrix, err_msg: Literal["(-3, -1)"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.matrix, y: numpy.matrix, err_msg: Literal["(-3, -2)"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.matrix, y: numpy.matrix, err_msg: Literal["(-3, -5)"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(
    x: numpy.matrix, y: numpy.matrix, err_msg: Literal["(-3, array(-1))"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.matrix, y: numpy.matrix, err_msg: Literal["(-3, -3)"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.int64, y: numpy.int64):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_equal(x: numpy.int64, y: int):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: numpy.int64, err_msg: str):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_equal(x: Tuple[numpy.float64, numpy.int64], y: Tuple[float, int]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(
    x: Tuple[numpy.ndarray, numpy.ndarray], y: Tuple[List[float], List[int]]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: Tuple[float, int], y: Tuple[float, int]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: bool):
    """
    usage.matplotlib: 1
    usage.scipy: 2
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: range):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: scipy.spatial.ckdtree._memoryviewslice, y: List[int]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: List[list], y: List[list]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.matrix, y: bool):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: List[numpy.int64]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: List[int], y: Tuple[int, int, int, int]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.bool_, y: bool, err_msg: str):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: bool, err_msg: str):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: List[int], y: List[numpy.float64]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: List[float], y: List[numpy.float64]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: List[Union[float, int]], y: List[numpy.float64]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: List[numpy.int64], y: List[numpy.float64]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: scipy.stats.stats.SpearmanrResult, y: Tuple[float, float]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_equal(
    x: scipy.stats.mstats_basic.SpearmanrResult, y: Tuple[float, float]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: scipy.stats.stats.KendalltauResult, y: Tuple[float, float]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(
    x: scipy.stats._stats_mstats_common.LinregressResult,
    y: Tuple[float, float, float, float, float],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: scipy.stats.stats.Ttest_1sampResult, y: Tuple[float, float]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: scipy.stats.stats.Ttest_relResult, y: Tuple[float, float]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: scipy.stats.stats.Ttest_indResult, y: Tuple[float, float]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: scipy.stats.stats.SkewtestResult, y: Tuple[float, float]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: scipy.stats.stats.KurtosistestResult, y: Tuple[float, float]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(x: scipy.stats.stats.NormaltestResult, y: Tuple[float, float]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_equal(
    x: Tuple[numpy.float64, numpy.float64], y: Tuple[numpy.float64, numpy.float64]
):
    """
    usage.matplotlib: 2
    """
    ...


@overload
def assert_array_equal(x: Tuple[numpy.float64, numpy.float64], y: Tuple[float, float]):
    """
    usage.matplotlib: 2
    """
    ...


@overload
def assert_array_equal(x: List[int], y: range):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: float):
    """
    usage.matplotlib: 4
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: Literal["red"]):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def assert_array_equal(
    x: Tuple[numpy.float64, numpy.float64, numpy.float64, numpy.float64],
    y: Tuple[numpy.float64, numpy.float64, numpy.float64, numpy.float64],
):
    """
    usage.matplotlib: 3
    """
    ...


@overload
def assert_array_equal(
    x: Tuple[numpy.float64, numpy.float64, numpy.float64, numpy.float64],
    y: numpy.ndarray,
):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.ma.core.MaskedArray, y: List[int]):
    """
    usage.matplotlib: 3
    """
    ...


@overload
def assert_array_equal(x: numpy.ma.core.MaskedArray, y: int):
    """
    usage.matplotlib: 3
    """
    ...


@overload
def assert_array_equal(x: numpy.ma.core.MaskedArray, y: List[Union[float, int]]):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: List[Tuple[int, int, int, int]]):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def assert_array_equal(
    x: numpy.ndarray, y: List[Tuple[int, Union[float, int], int, int]]
):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def assert_array_equal(
    x: List[
        Literal[
            "2000-10-31T11:50:23",
            "2054-06-20T14:31:45",
            "1983-07-09T17:17:34",
            "1976-03-05T00:00:01",
            "2014-01-11T00:00:00",
        ]
    ],
    y: List[
        Literal[
            "2000-10-31T11:50:23",
            "2054-06-20T14:31:45",
            "1983-07-09T17:17:34",
            "1976-03-05T00:00:01",
            "2014-01-11T00:00:00",
        ]
    ],
):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def assert_array_equal(x: List[numpy.ndarray], y: List[List[List[int]]]):
    """
    usage.matplotlib: 5
    """
    ...


@overload
def assert_array_equal(x: List[List[numpy.ndarray]], y: List[List[List[int]]]):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def assert_array_equal(x: dask.dataframe.core.Index, y: List[int]):
    """
    usage.dask: 2
    """
    ...


@overload
def assert_array_equal(x: list, y: numpy.ndarray):
    """
    usage.sklearn: 4
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: numpy.ndarray, err_msg: Literal[""]):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_array_equal(
    x: List[Literal["col_float", "col_int"]], y: List[Literal["col_float", "col_int"]]
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_equal(x: List[Literal["col_str"]], y: List[Literal["col_str"]]):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_array_equal(x: List[Literal["col_float"]], y: List[Literal["col_float"]]):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_equal(x: List[Literal["col_int"]], y: List[Literal["col_int"]]):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_equal(
    x: List[Literal["col_str", "col_float"]], y: List[Literal["col_str", "col_float"]]
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_equal(
    x: List[Literal["col_str", "col_float", "col_int"]],
    y: List[Literal["col_str", "col_float", "col_int"]],
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: pandas.core.series.Series):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: int, err_msg: str):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_equal(
    x: numpy.ndarray, y: List[List[Literal["blue", "red", "green", "purple", "yellow"]]]
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_equal(x: List[numpy.ndarray], y: List[List[int]]):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: List[str]):
    """
    usage.sklearn: 3
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: List[Literal["1", "-1"]]):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: List[Union[int, Literal["foo"]]]):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_equal(x: List[str], y: List[str]):
    """
    usage.sklearn: 5
    """
    ...


@overload
def assert_array_equal(
    x: List[Literal["e", "d", "c", "b", "a"]], y: List[Literal["e", "d", "c", "b", "a"]]
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_equal(x: List[Literal["I", "G", "E", "C", "A"]], y: numpy.ndarray):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_equal(x: List[bool], y: numpy.ndarray):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_equal(x: List[numpy.int64], y: List[int]):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: List[Union[int, float]], err_msg: str):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_array_equal(x: List[numpy.ndarray], y: numpy.ndarray):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_equal(x: Tuple[int, int, int, int], y: Tuple[int, int, int, int]):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: List[Literal["three", "two", "one"]]):
    """
    usage.sklearn: 3
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: List[List[List[int]]]):
    """
    usage.sklearn: 9
    """
    ...


@overload
def assert_array_equal(
    x: Tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray],
    y: Tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray],
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.float64, y: numpy.float64, err_msg: str):
    """
    usage.sklearn: 7
    """
    ...


@overload
def assert_array_equal(x: numpy.int64, y: numpy.int64, err_msg: str):
    """
    usage.sklearn: 3
    """
    ...


@overload
def assert_array_equal(
    x: Tuple[
        Tuple[numpy.float64, numpy.float64, numpy.float64, numpy.float64],
        Tuple[numpy.float64, numpy.float64, numpy.float64, numpy.float64],
        Tuple[numpy.float64, numpy.float64, numpy.float64, numpy.float64],
        Tuple[numpy.float64, numpy.float64, numpy.float64, numpy.float64],
        Tuple[numpy.float64, numpy.float64, numpy.float64, numpy.float64],
    ],
    y: numpy.ndarray,
):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_array_equal(
    x: List[Literal["recall", "accuracy"]],
    y: Tuple[Literal["accuracy"], Literal["recall"]],
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.ma.core.MaskedArray, y: List[Union[None, int]]):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_equal(
    x: numpy.ma.core.MaskedArray, y: numpy.ma.core.MaskedArray, err_msg: str
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_equal(
    x: List[Dict[Literal["max_depth"], int]],
    y: numpy.ndarray,
    err_msg: Literal["Checking params"],
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_equal(
    x: List[Dict[Literal["max_depth", "min_samples_split"], int]],
    y: numpy.ndarray,
    err_msg: Literal["Checking params"],
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_equal(
    x: Tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray, numpy.ndarray, numpy.ndarray],
    y: List[numpy.ndarray],
):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_array_equal(x: List[numpy.ndarray], y: List[numpy.ndarray]):
    """
    usage.sklearn: 3
    """
    ...


@overload
def assert_array_equal(
    x: List[Literal["א", "☮", "\x01F40D", "1"]],
    y: List[Literal["א", "☮", "\x01F40D", "1"]],
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_equal(x: List[str], y: numpy.ndarray):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_array_equal(x: List[Literal["x0_dat2", "x0_c❤t1"]], y: numpy.ndarray):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_equal(x: List[Literal["n👍me_dat2", "n👍me_c❤t1"]], y: numpy.ndarray):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_equal(x: List[Literal["x2_b", "x0_c"]], y: numpy.ndarray):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_equal(x: List[Literal["x2_b", "x1_2", "x0_c"]], y: numpy.ndarray):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_equal(x: List[Literal["x2_a", "x0_b"]], y: numpy.ndarray):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_equal(
    x: List[Union[int, Literal["def"]]], y: List[Union[int, Literal["def"]]]
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: List[Literal["pos"]]):
    """
    usage.sklearn: 4
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: List[Literal["pos", "neg"]]):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: List[Literal["neg", "pos"]]):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: List[Literal["spam", "ham", "eggs", "0"]]):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: List[Literal["0", "ham", "eggs", "spam"]]):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_equal(x: List[Tuple[numpy.int64]], y: List[List[int]]):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: List[Literal["3", "2", "1"]]):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_array_equal(
    x: List[Tuple[Literal["3", "2", "1"], ...]],
    y: List[Tuple[Literal["3", "2", "1"], ...]],
):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: List[Literal["c", "b", "a"]]):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_array_equal(
    x: List[Tuple[Literal["c", "b", "a"], ...]],
    y: List[Tuple[Literal["c", "b", "a"], ...]],
):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_array_equal(
    x: List[Tuple[Tuple[int], ...]], y: List[Tuple[Tuple[int], ...]]
):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: Tuple[List[int], List[int]]):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: Tuple[float, float, float]):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_equal(
    x: numpy.ndarray, y: numpy.ndarray, err_msg: Literal["solver svd"]
):
    """
    usage.sklearn: 3
    """
    ...


@overload
def assert_array_equal(
    x: numpy.ndarray, y: numpy.ndarray, err_msg: Literal["solver lsqr"]
):
    """
    usage.sklearn: 3
    """
    ...


@overload
def assert_array_equal(
    x: numpy.ndarray, y: numpy.ndarray, err_msg: Literal["solver eigen"]
):
    """
    usage.sklearn: 3
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: List[Literal["paris"]]):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_equal(x: List[Union[float, int]], y: numpy.ndarray):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.str_, y: List[Literal["eggs"]]):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_array_equal(x: List[list], y: numpy.ndarray):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: List[int], err_msg: str):
    """
    usage.sklearn: 5
    """
    ...


@overload
def assert_array_equal(x: numpy.flatiter, y: List[float]):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.flatiter, y: List[Union[float, int]]):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_array_equal(x: int, y: numpy.ndarray):
    """
    usage.sklearn: 4
    """
    ...


@overload
def assert_array_equal(x: numpy.float32, y: numpy.float32):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_array_equal(x: List[slice[int, int, int]], y: List[slice[int, int, int]]):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: List[Literal["a", "b", "c"]]):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_equal(x: sklearn.utils._mocking.MockDataFrame, y: numpy.ndarray):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.memmap, y: numpy.memmap):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_equal(
    x: pandas.core.series.Series,
    y: Tuple[Type[numpy.float16], Type[numpy.float32], Type[numpy.float32]],
):
    """
    usage.sklearn: 1
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
    usage.scipy: 2
    usage.skimage: 16
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_less(x: numpy.ndarray, y: numpy.ndarray):
    """
    usage.scipy: 4
    usage.skimage: 2
    usage.sklearn: 4
    """
    ...


@overload
def assert_array_less(x: numpy.float64, y: float):
    """
    usage.scipy: 3
    usage.skimage: 2
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_less(x: numpy.float128, y: numpy.float128, err_msg: str):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_less(x: numpy.float64, y: numpy.float64, err_msg: str):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_less(x: numpy.float32, y: numpy.float64, err_msg: str):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_less(x: float, y: float):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_less(x: int, y: numpy.float64):
    """
    usage.scipy: 1
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_less(x: float, y: numpy.float64):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_less(x: numpy.ndarray, y: float):
    """
    usage.scipy: 33
    usage.sklearn: 3
    """
    ...


@overload
def assert_array_less(x: numpy.ndarray, y: int):
    """
    usage.scipy: 8
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_less(x: int, y: numpy.ndarray):
    """
    usage.scipy: 4
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_less(x: float, y: numpy.ndarray):
    """
    usage.scipy: 20
    usage.sklearn: 3
    """
    ...


@overload
def assert_array_less(x: numpy.ndarray, y: numpy.ndarray, err_msg: str):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_less(x: numpy.ndarray, y: numpy.float64):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_array_less(x: numpy.float64, y: numpy.ndarray):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_array_less(x: List[float], y: List[numpy.float64]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_less(x: List[int], y: List[int]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_array_less(x: numpy.ma.core.MaskedArray, y: float):
    """
    usage.matplotlib: 3
    """
    ...


@overload
def assert_array_less(x: numpy.float64, y: int, err_msg: str):
    """
    usage.sklearn: 3
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
    usage.scipy: 318
    usage.skimage: 10
    usage.xarray: 1
    """
    ...


@overload
def assert_equal(actual: int, desired: int):
    """
    usage.scipy: 534
    usage.skimage: 68
    """
    ...


@overload
def assert_equal(actual: numpy.float64, desired: numpy.float64):
    """
    usage.scipy: 112
    usage.skimage: 7
    """
    ...


@overload
def assert_equal(actual: numpy.int64, desired: int):
    """
    usage.scipy: 67
    usage.skimage: 19
    usage.xarray: 1
    """
    ...


@overload
def assert_equal(actual: str, desired: str):
    """
    usage.scipy: 27
    usage.skimage: 4
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: numpy.ndarray):
    """
    usage.dask: 7
    usage.matplotlib: 3
    usage.scipy: 538
    usage.skimage: 241
    usage.sklearn: 2
    usage.xarray: 3
    """
    ...


@overload
def assert_equal(actual: Tuple[int, int, int], desired: Tuple[int, int, int]):
    """
    usage.scipy: 40
    usage.skimage: 20
    """
    ...


@overload
def assert_equal(actual: numpy.dtype, desired: numpy.dtype):
    """
    usage.scipy: 336
    usage.skimage: 4
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: List[int]):
    """
    usage.dask: 2
    usage.scipy: 107
    usage.skimage: 21
    """
    ...


@overload
def assert_equal(actual: numpy.float64, desired: int):
    """
    usage.scipy: 136
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
    usage.scipy: 50
    usage.skimage: 3
    usage.xarray: 2
    """
    ...


@overload
def assert_equal(actual: Tuple[int, int, int, int], desired: Tuple[int, int, int, int]):
    """
    usage.scipy: 14
    usage.skimage: 7
    """
    ...


@overload
def assert_equal(
    actual: Tuple[int, int, int, int, int], desired: Tuple[int, int, int, int, int]
):
    """
    usage.scipy: 14
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
    usage.scipy: 61
    usage.skimage: 4
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: List[List[int]]):
    """
    usage.scipy: 41
    usage.skimage: 8
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: Tuple[int, int]):
    """
    usage.scipy: 2
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
    usage.scipy: 17
    usage.skimage: 1
    """
    ...


@overload
def assert_equal(actual: Tuple[int, int], desired: Tuple[int, int]):
    """
    usage.scipy: 179
    usage.skimage: 40
    """
    ...


@overload
def assert_equal(actual: None, desired: None):
    """
    usage.scipy: 3
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
    usage.scipy: 1
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
    usage.scipy: 6
    usage.skimage: 1
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: int):
    """
    usage.scipy: 30
    usage.skimage: 56
    usage.xarray: 2
    """
    ...


@overload
def assert_equal(actual: float, desired: float):
    """
    usage.scipy: 125
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
    usage.scipy: 24
    usage.skimage: 1
    """
    ...


@overload
def assert_equal(actual: List[numpy.float64], desired: List[numpy.float64]):
    """
    usage.matplotlib: 1
    usage.skimage: 1
    """
    ...


@overload
def assert_equal(
    actual: Tuple[numpy.float64, numpy.float64],
    desired: Tuple[numpy.float64, numpy.float64],
):
    """
    usage.scipy: 1
    usage.skimage: 1
    """
    ...


@overload
def assert_equal(actual: bool, desired: bool, err_msg: str):
    """
    usage.scipy: 1
    usage.skimage: 4
    """
    ...


@overload
def assert_equal(actual: numpy.dtype, desired: Type[bool]):
    """
    usage.scipy: 6
    usage.skimage: 4
    """
    ...


@overload
def assert_equal(actual: numpy.dtype, desired: Type[numpy.uint8]):
    """
    usage.scipy: 11
    usage.skimage: 5
    """
    ...


@overload
def assert_equal(actual: numpy.uint8, desired: numpy.uint8):
    """
    usage.scipy: 3
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
    usage.scipy: 3
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
    usage.scipy: 6
    usage.skimage: 2
    """
    ...


@overload
def assert_equal(actual: numpy.float32, desired: float):
    """
    usage.scipy: 5
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
    usage.scipy: 15
    usage.skimage: 2
    """
    ...


@overload
def assert_equal(actual: numpy.int8, desired: int):
    """
    usage.scipy: 5
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
    usage.scipy: 5
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
    usage.scipy: 7
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
    usage.scipy: 5
    usage.xarray: 1
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: numpy.int32):
    """
    usage.scipy: 1
    usage.xarray: 1
    """
    ...


@overload
def assert_equal(actual: numpy.float32, desired: numpy.float32):
    """
    usage.scipy: 5
    usage.xarray: 1
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: numpy.float32):
    """
    usage.scipy: 1
    usage.xarray: 1
    """
    ...


@overload
def assert_equal(actual: object, desired: object):
    """
    usage.scipy: 1
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
def assert_equal(actual: bool, desired: bool):
    """
    usage.scipy: 104
    """
    ...


@overload
def assert_equal(actual: Literal["another name"], desired: Literal["another name"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: Tuple[int], desired: Tuple[int], err_msg: str):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: Tuple[int, int, int, int], desired: Tuple[int, int, int, int], err_msg: str
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: numpy.dtype, desired: Type[numpy.float64]):
    """
    usage.scipy: 35
    """
    ...


@overload
def assert_equal(
    actual: Type[numpy.random.mtrand.RandomState],
    desired: Type[numpy.random.mtrand.RandomState],
):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_equal(
    actual: Type[numpy.random._generator.Generator],
    desired: Type[numpy.random._generator.Generator],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: scipy._lib._util.FullArgSpec, desired: scipy._lib._util.FullArgSpec
):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_equal(actual: List[numpy.float64], desired: numpy.ndarray):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_equal(actual: Literal["bad signature"], desired: Literal["bad signature"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: float, desired: int):
    """
    usage.scipy: 29
    """
    ...


@overload
def assert_equal(actual: List[float], desired: List[float]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: Tuple[numpy.ndarray, numpy.ndarray],
    desired: Tuple[numpy.ndarray, numpy.ndarray],
):
    """
    usage.scipy: 11
    """
    ...


@overload
def assert_equal(actual: List[int], desired: numpy.ndarray):
    """
    usage.scipy: 13
    """
    ...


@overload
def assert_equal(actual: List[int], desired: List[int]):
    """
    usage.scipy: 15
    """
    ...


@overload
def assert_equal(actual: numpy.bool_, desired: bool):
    """
    usage.scipy: 19
    """
    ...


@overload
def assert_equal(
    actual: List[Literal["g", "m", "c"]], desired: List[Literal["g", "m", "c"]]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: List[Literal["weak mixing angle"]],
    desired: List[Literal["weak mixing angle"]],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: list, desired: list):
    """
    usage.matplotlib: 2
    usage.scipy: 6
    """
    ...


@overload
def assert_equal(
    actual: Literal["299792458 m s^-1"], desired: Literal["299792458 m s^-1"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: List[float]):
    """
    usage.matplotlib: 1
    usage.scipy: 19
    usage.sklearn: 1
    """
    ...


@overload
def assert_equal(actual: numpy.dtype, desired: Type[numpy.complex256]):
    """
    usage.scipy: 16
    """
    ...


@overload
def assert_equal(actual: numpy.dtype, desired: Type[numpy.complex128]):
    """
    usage.scipy: 35
    """
    ...


@overload
def assert_equal(actual: numpy.dtype, desired: Type[numpy.complex64]):
    """
    usage.scipy: 47
    """
    ...


@overload
def assert_equal(actual: numpy.dtype, desired: Type[numpy.float32]):
    """
    usage.scipy: 37
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: numpy.ndarray, err_msg: str):
    """
    usage.scipy: 36
    """
    ...


@overload
def assert_equal(
    actual: Tuple[numpy.int32, numpy.int32, numpy.int32], desired: Tuple[int, int, int]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: type, desired: type):
    """
    usage.scipy: 10
    """
    ...


@overload
def assert_equal(actual: Tuple[int, int, int, int], desired: List[int]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: Tuple[int, int, int, int, int, int], desired: List[int]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: List[numpy.ndarray]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: Tuple[None, ...], desired: Tuple[None, ...]):
    """
    usage.scipy: 12
    """
    ...


@overload
def assert_equal(actual: Tuple[float, float], desired: Tuple[float, float]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: numpy.dtype, desired: Type[numpy.float16]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(actual: numpy.dtype, desired: Type[numpy.float128]):
    """
    usage.scipy: 15
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: List[List[Union[int, float]]]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: Tuple[int, int, int],
    desired: Tuple[int, int, int],
    err_msg: Literal["nearest"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: Tuple[int, int, int],
    desired: Tuple[int, int, int],
    err_msg: Literal["linear"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: Tuple[int, int],
    desired: Tuple[int, int],
    err_msg: Literal["('nearest', True)"],
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(
    actual: Tuple[int, int],
    desired: Tuple[int, int],
    err_msg: Literal["('nearest', False)"],
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(
    actual: Tuple[int, int],
    desired: Tuple[int, int],
    err_msg: Literal["('linear', True)"],
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(
    actual: Tuple[int, int],
    desired: Tuple[int, int],
    err_msg: Literal["('linear', False)"],
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(
    actual: Tuple[int, int],
    desired: Tuple[int, int],
    err_msg: Literal["('cubic', True)"],
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(
    actual: Tuple[int, int],
    desired: Tuple[int, int],
    err_msg: Literal["('cubic', False)"],
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(
    actual: Tuple[int, int, int, int, int, int, int],
    desired: Tuple[int, int, int, int, int, int, int],
):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_equal(
    actual: List[Literal["nominal", "numeric"]],
    desired: List[Literal["nominal", "numeric"]],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: Literal["attr_date_number"], desired: Literal["attr_date_number"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: Literal["relational"], desired: Literal["relational"]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(actual: Literal["attr_date"], desired: Literal["attr_date"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: Literal["date"], desired: Literal["date"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: Literal["attr_number"], desired: Literal["attr_number"]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(actual: Literal["numeric"], desired: Literal["numeric"]):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_equal(
    actual: Literal["attr_relational"], desired: Literal["attr_relational"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: Literal["age"], desired: Literal["age"]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(actual: Literal["smoker"], desired: Literal["smoker"]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(actual: Literal["nominal"], desired: Literal["nominal"]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(
    actual: Tuple[Literal["yes"], Literal["no"]], desired: List[Literal["no", "yes"]]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: Tuple[Literal["  yes"], Literal["no  "]],
    desired: List[Literal["no  ", "  yes"]],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: Dict[Literal["min", "repeat", "width"], Union[None, int]],
    desired: Dict[Literal["min", "repeat", "width"], Union[None, int]],
):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_equal(
    actual: Dict[Literal["min", "repeat", "significand", "width"], Union[None, int]],
    desired: Dict[Literal["min", "repeat", "significand", "width"], Union[None, int]],
):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_equal(
    actual: Dict[Literal["min", "repeat", "significand", "width"], Union[int, None]],
    desired: Dict[Literal["min", "repeat", "significand", "width"], Union[int, None]],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: Dict[Literal["min", "repeat", "significand", "width"], int],
    desired: Dict[Literal["min", "repeat", "significand", "width"], int],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: Literal["(I10)"], desired: Literal["(I10)"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: Literal["(I12.10)"], desired: Literal["(I12.10)"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: Literal["(3I12.10)"], desired: Literal["(3I12.10)"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: Literal["(E10.5)"], desired: Literal["(E10.5)"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: Literal["(E12.10)"], desired: Literal["(E12.10)"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: Literal["(E12.10E3)"], desired: Literal["(E12.10E3)"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: Literal["(3E10.5)"], desired: Literal["(3E10.5)"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: Literal["inline"], desired: Literal["inline"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: List[Tuple[Literal["testdouble"], Tuple[int, int], Literal["double"]]],
    desired: List[Tuple[Literal["testdouble"], Tuple[int, int], Literal["double"]]],
    err_msg: str,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: List[Tuple[Literal["teststring"], Tuple[int], Literal["char"]]],
    desired: List[Tuple[Literal["teststring"], Tuple[int], Literal["char"]]],
    err_msg: str,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: List[Tuple[Literal["testcomplex"], Tuple[int, int], Literal["double"]]],
    desired: List[Tuple[Literal["testcomplex"], Tuple[int, int], Literal["double"]]],
    err_msg: str,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: List[Tuple[Literal["testmatrix"], Tuple[int, int], Literal["double"]]],
    desired: List[Tuple[Literal["testmatrix"], Tuple[int, int], Literal["double"]]],
    err_msg: str,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: List[Tuple[Literal["testsparse"], Tuple[int, int], Literal["sparse"]]],
    desired: List[Tuple[Literal["testsparse"], Tuple[int, int], Literal["sparse"]]],
    err_msg: str,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: List[
        Tuple[Literal["testsparsecomplex"], Tuple[int, int], Literal["sparse"]]
    ],
    desired: List[
        Tuple[Literal["testsparsecomplex"], Tuple[int, int], Literal["sparse"]]
    ],
    err_msg: str,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: List[Tuple[Literal["a", "theta"], Tuple[int, int], Literal["double"]]],
    desired: List[Tuple[Literal["a", "theta"], Tuple[int, int], Literal["double"]]],
    err_msg: str,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: List[Tuple[Literal["testminus"], Tuple[int, int], Literal["double"]]],
    desired: List[Tuple[Literal["testminus"], Tuple[int, int], Literal["double"]]],
    err_msg: str,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: List[Tuple[Literal["testonechar"], Tuple[int], Literal["char"]]],
    desired: List[Tuple[Literal["testonechar"], Tuple[int], Literal["char"]]],
    err_msg: str,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: List[Tuple[Literal["testcell"], Tuple[int, int], Literal["cell"]]],
    desired: List[Tuple[Literal["testcell"], Tuple[int, int], Literal["cell"]]],
    err_msg: str,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: List[Tuple[Literal["testscalarcell"], Tuple[int, int], Literal["cell"]]],
    desired: List[Tuple[Literal["testscalarcell"], Tuple[int, int], Literal["cell"]]],
    err_msg: str,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: List[Tuple[Literal["testemptycell"], Tuple[int, int], Literal["cell"]]],
    desired: List[Tuple[Literal["testemptycell"], Tuple[int, int], Literal["cell"]]],
    err_msg: str,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: List[Tuple[Literal["teststringarray"], Tuple[int], Literal["char"]]],
    desired: List[Tuple[Literal["teststringarray"], Tuple[int], Literal["char"]]],
    err_msg: str,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: List[
        Tuple[Literal["test3dmatrix"], Tuple[int, int, int], Literal["double"]]
    ],
    desired: List[
        Tuple[Literal["test3dmatrix"], Tuple[int, int, int], Literal["double"]]
    ],
    err_msg: str,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: List[Tuple[Literal["teststruct"], Tuple[int, int], Literal["struct"]]],
    desired: List[Tuple[Literal["teststruct"], Tuple[int, int], Literal["struct"]]],
    err_msg: str,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: List[Tuple[Literal["testcellnest"], Tuple[int, int], Literal["cell"]]],
    desired: List[Tuple[Literal["testcellnest"], Tuple[int, int], Literal["cell"]]],
    err_msg: str,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: List[Tuple[Literal["teststructnest"], Tuple[int, int], Literal["struct"]]],
    desired: List[Tuple[Literal["teststructnest"], Tuple[int, int], Literal["struct"]]],
    err_msg: str,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: List[Tuple[Literal["teststructarr"], Tuple[int, int], Literal["struct"]]],
    desired: List[Tuple[Literal["teststructarr"], Tuple[int, int], Literal["struct"]]],
    err_msg: str,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: List[Tuple[Literal["testobject"], Tuple[int, int], Literal["object"]]],
    desired: List[Tuple[Literal["testobject"], Tuple[int, int], Literal["object"]]],
    err_msg: str,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: List[Tuple[Literal["testunicode"], Tuple[int], Literal["char"]]],
    desired: List[Tuple[Literal["testunicode"], Tuple[int], Literal["char"]]],
    err_msg: str,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: List[Tuple[Literal["testbools"], Tuple[int, int], Literal["logical"]]],
    desired: List[Tuple[Literal["testbools"], Tuple[int, int], Literal["logical"]]],
    err_msg: str,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: List[Literal["avar"]], desired: List[Literal["avar"]]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: set, desired: set):
    """
    usage.scipy: 15
    """
    ...


@overload
def assert_equal(actual: Type[numpy.float64], desired: Type[numpy.float64]):
    """
    usage.scipy: 12
    """
    ...


@overload
def assert_equal(actual: Type[numpy.str_], desired: Type[numpy.str_]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: Type[numpy.int64], desired: Type[numpy.int64]):
    """
    usage.scipy: 7
    """
    ...


@overload
def assert_equal(actual: Type[numpy.object_], desired: Type[numpy.object_]):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: Literal["python"]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: Literal["not perl"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: Literal["a string"]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(actual: int, desired: bool):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_equal(actual: Type[numpy.uint8], desired: Type[numpy.uint8]):
    """
    usage.scipy: 7
    """
    ...


@overload
def assert_equal(actual: Literal["u"], desired: Literal["u"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: Literal["f"], desired: Literal["f"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: List[Literal["theta"]], desired: List[Literal["theta"]]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: Literal["arr"], desired: Literal["arr"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: Literal["mystr"], desired: Literal["mystr"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: Literal["mynum"], desired: Literal["mynum"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: Literal["SchrÃ¶dinger"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: Type[numpy.bool_], desired: Type[numpy.bool_]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: Literal["� am broken"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: bytes, desired: bytes):
    """
    usage.scipy: 24
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: Literal[" "]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(actual: bytes, desired: bytes, err_msg: str):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: numpy.int16, desired: numpy.int16):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_equal(actual: Type[numpy.int16], desired: Type[numpy.int16]):
    """
    usage.scipy: 7
    """
    ...


@overload
def assert_equal(actual: Type[numpy.int32], desired: Type[numpy.int32]):
    """
    usage.scipy: 7
    """
    ...


@overload
def assert_equal(actual: Type[numpy.float32], desired: Type[numpy.float32]):
    """
    usage.scipy: 15
    """
    ...


@overload
def assert_equal(actual: numpy.complex64, desired: numpy.complex64):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_equal(actual: Type[numpy.complex64], desired: Type[numpy.complex64]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(actual: bytes, desired: numpy.bytes_):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: Type[numpy.bytes_], desired: Type[numpy.bytes_]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: numpy.complex128, desired: numpy.complex128):
    """
    usage.scipy: 7
    """
    ...


@overload
def assert_equal(actual: Type[numpy.complex128], desired: Type[numpy.complex128]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(actual: numpy.uint16, desired: numpy.uint16):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_equal(actual: Type[numpy.uint16], desired: Type[numpy.uint16]):
    """
    usage.scipy: 6
    """
    ...


@overload
def assert_equal(actual: numpy.uint32, desired: numpy.uint32):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_equal(actual: Type[numpy.uint32], desired: Type[numpy.uint32]):
    """
    usage.scipy: 6
    """
    ...


@overload
def assert_equal(actual: Type[numpy.uint64], desired: Type[numpy.uint64]):
    """
    usage.scipy: 6
    """
    ...


@overload
def assert_equal(
    actual: Tuple[int, int, int, int, int, int, int, int],
    desired: Tuple[int, int, int, int, int, int, int, int],
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(
    actual: Tuple[
        int, int, int, Literal["array"], Literal["integer"], Literal["general"]
    ],
    desired: Tuple[
        int, int, int, Literal["array"], Literal["integer"], Literal["general"]
    ],
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(
    actual: Tuple[
        int, int, int, Literal["array"], Literal["unsigned-integer"], Literal["general"]
    ],
    desired: Tuple[
        int, int, int, Literal["array"], Literal["unsigned-integer"], Literal["general"]
    ],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: Tuple[int, int, int, Literal["array"], Literal["real"], Literal["general"]],
    desired: Tuple[
        int, int, int, Literal["array"], Literal["real"], Literal["general"]
    ],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: Tuple[
        int, int, int, Literal["array"], Literal["complex"], Literal["general"]
    ],
    desired: Tuple[
        int, int, int, Literal["array"], Literal["complex"], Literal["general"]
    ],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: Tuple[
        int, int, int, Literal["array"], Literal["integer"], Literal["symmetric"]
    ],
    desired: Tuple[
        int, int, int, Literal["array"], Literal["integer"], Literal["symmetric"]
    ],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: Tuple[
        int,
        int,
        int,
        Literal["array"],
        Literal["unsigned-integer"],
        Literal["symmetric"],
    ],
    desired: Tuple[
        int,
        int,
        int,
        Literal["array"],
        Literal["unsigned-integer"],
        Literal["symmetric"],
    ],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: Tuple[
        int, int, int, Literal["array"], Literal["integer"], Literal["skew-symmetric"]
    ],
    desired: Tuple[
        int, int, int, Literal["array"], Literal["integer"], Literal["skew-symmetric"]
    ],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: List[List[int]], desired: numpy.ndarray):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: Tuple[
        int, int, int, Literal["array"], Literal["real"], Literal["skew-symmetric"]
    ],
    desired: Tuple[
        int, int, int, Literal["array"], Literal["real"], Literal["skew-symmetric"]
    ],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: Tuple[
        int, int, int, Literal["array"], Literal["complex"], Literal["hermitian"]
    ],
    desired: Tuple[
        int, int, int, Literal["array"], Literal["complex"], Literal["hermitian"]
    ],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: Tuple[
        int, int, int, Literal["array"], Literal["real"], Literal["symmetric"]
    ],
    desired: Tuple[
        int, int, int, Literal["array"], Literal["real"], Literal["symmetric"]
    ],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: Tuple[
        int, int, int, Literal["coordinate"], Literal["integer"], Literal["general"]
    ],
    desired: Tuple[
        int, int, int, Literal["coordinate"], Literal["integer"], Literal["general"]
    ],
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(actual: numpy.matrix, desired: numpy.matrix):
    """
    usage.scipy: 154
    """
    ...


@overload
def assert_equal(
    actual: Tuple[
        int,
        int,
        int,
        Literal["coordinate"],
        Literal["unsigned-integer"],
        Literal["general"],
    ],
    desired: Tuple[
        int,
        int,
        int,
        Literal["coordinate"],
        Literal["unsigned-integer"],
        Literal["general"],
    ],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: Tuple[
        int, int, int, Literal["coordinate"], Literal["real"], Literal["general"]
    ],
    desired: Tuple[
        int, int, int, Literal["coordinate"], Literal["real"], Literal["general"]
    ],
):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_equal(
    actual: Tuple[
        int, int, int, Literal["coordinate"], Literal["complex"], Literal["general"]
    ],
    desired: Tuple[
        int, int, int, Literal["coordinate"], Literal["complex"], Literal["general"]
    ],
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(
    actual: Tuple[
        int, int, int, Literal["coordinate"], Literal["integer"], Literal["symmetric"]
    ],
    desired: Tuple[
        int, int, int, Literal["coordinate"], Literal["integer"], Literal["symmetric"]
    ],
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(
    actual: Tuple[
        int,
        int,
        int,
        Literal["coordinate"],
        Literal["unsigned-integer"],
        Literal["symmetric"],
    ],
    desired: Tuple[
        int,
        int,
        int,
        Literal["coordinate"],
        Literal["unsigned-integer"],
        Literal["symmetric"],
    ],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: Tuple[
        int,
        int,
        int,
        Literal["coordinate"],
        Literal["integer"],
        Literal["skew-symmetric"],
    ],
    desired: Tuple[
        int,
        int,
        int,
        Literal["coordinate"],
        Literal["integer"],
        Literal["skew-symmetric"],
    ],
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(
    actual: Tuple[
        int, int, int, Literal["coordinate"], Literal["real"], Literal["skew-symmetric"]
    ],
    desired: Tuple[
        int, int, int, Literal["coordinate"], Literal["real"], Literal["skew-symmetric"]
    ],
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(
    actual: Tuple[
        int, int, int, Literal["coordinate"], Literal["complex"], Literal["hermitian"]
    ],
    desired: Tuple[
        int, int, int, Literal["coordinate"], Literal["complex"], Literal["hermitian"]
    ],
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(
    actual: Tuple[
        int, int, int, Literal["coordinate"], Literal["real"], Literal["symmetric"]
    ],
    desired: Tuple[
        int, int, int, Literal["coordinate"], Literal["real"], Literal["symmetric"]
    ],
):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_equal(
    actual: Tuple[
        int, int, int, Literal["coordinate"], Literal["pattern"], Literal["general"]
    ],
    desired: Tuple[
        int, int, int, Literal["coordinate"], Literal["pattern"], Literal["general"]
    ],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: numpy.matrix):
    """
    usage.scipy: 5
    """
    ...


@overload
def assert_equal(
    actual: Tuple[
        int, int, int, Literal["coordinate"], Literal["pattern"], Literal["symmetric"]
    ],
    desired: Tuple[
        int, int, int, Literal["coordinate"], Literal["pattern"], Literal["symmetric"]
    ],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: Literal["data"], desired: Literal["data"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: List[bool]):
    """
    usage.matplotlib: 2
    usage.scipy: 5
    """
    ...


@overload
def assert_equal(actual: numpy.ma.core.MaskedArray, desired: List[int]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: List[List[bool]]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: scipy.linalg._testutils._FakeMatrix, desired: numpy.ndarray, err_msg: str
):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_equal(
    actual: scipy.linalg._testutils._FakeMatrix2, desired: numpy.ndarray, err_msg: str
):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_equal(actual: Literal["z"], desired: Literal["z"]):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_equal(actual: Literal["d"], desired: Literal["d"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: Literal["c"], desired: Literal["c"]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(actual: bool, desired: bool, err_msg: Literal["[[0, 1], [2, 3]]"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: float, desired: numpy.float32):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: float, desired: numpy.float64):
    """
    usage.matplotlib: 1
    usage.scipy: 4
    """
    ...


@overload
def assert_equal(actual: numpy.int32, desired: numpy.int64):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: int, desired: int, err_msg: str):
    """
    usage.scipy: 7
    """
    ...


@overload
def assert_equal(actual: numpy.float32, desired: int, err_msg: str):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: numpy.float64, desired: int, err_msg: str):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: Type[scipy.sparse.csc.csc_matrix],
    desired: Type[scipy.sparse.csc.csc_matrix],
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(actual: numpy.dtype, desired: Type[float]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(actual: int, desired: int, err_msg: Literal["n = 34"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: int, desired: int, err_msg: Literal["n = 35"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: Literal["Something else."], desired: Literal["Something else."]
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(actual: List[numpy.int32], desired: List[numpy.int32]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: List[numpy.int64], desired: List[numpy.int64]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: Literal["i"], desired: Literal["i"]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(
    actual: List[Tuple[slice[int, int, int]]],
    desired: List[Tuple[slice[int, int, int]]],
):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_equal(
    actual: List[Tuple[slice[int, int, int], slice[int, int, int]]],
    desired: List[Tuple[slice[int, int, int], slice[int, int, int]]],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: List[Union[Tuple[slice[int, int, int], slice[int, int, int]], None]],
    desired: List[Union[Tuple[slice[int, int, int], slice[int, int, int]], None]],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: numpy.int64, desired: float):
    """
    usage.scipy: 7
    """
    ...


@overload
def assert_equal(actual: numpy.uint64, desired: float):
    """
    usage.scipy: 5
    """
    ...


@overload
def assert_equal(
    actual: Tuple[
        numpy.int8,
        numpy.int8,
        Tuple[numpy.int64, numpy.int64],
        Tuple[numpy.int64, numpy.int64],
    ],
    desired: Tuple[
        numpy.int8,
        numpy.int8,
        Tuple[numpy.int64, numpy.int64],
        Tuple[numpy.int64, numpy.int64],
    ],
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(
    actual: Tuple[
        numpy.uint8,
        numpy.uint8,
        Tuple[numpy.int64, numpy.int64],
        Tuple[numpy.int64, numpy.int64],
    ],
    desired: Tuple[
        numpy.uint8,
        numpy.uint8,
        Tuple[numpy.int64, numpy.int64],
        Tuple[numpy.int64, numpy.int64],
    ],
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(
    actual: Tuple[
        numpy.int16,
        numpy.int16,
        Tuple[numpy.int64, numpy.int64],
        Tuple[numpy.int64, numpy.int64],
    ],
    desired: Tuple[
        numpy.int16,
        numpy.int16,
        Tuple[numpy.int64, numpy.int64],
        Tuple[numpy.int64, numpy.int64],
    ],
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(
    actual: Tuple[
        numpy.uint16,
        numpy.uint16,
        Tuple[numpy.int64, numpy.int64],
        Tuple[numpy.int64, numpy.int64],
    ],
    desired: Tuple[
        numpy.uint16,
        numpy.uint16,
        Tuple[numpy.int64, numpy.int64],
        Tuple[numpy.int64, numpy.int64],
    ],
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(
    actual: Tuple[
        numpy.int32,
        numpy.int32,
        Tuple[numpy.int64, numpy.int64],
        Tuple[numpy.int64, numpy.int64],
    ],
    desired: Tuple[
        numpy.int32,
        numpy.int32,
        Tuple[numpy.int64, numpy.int64],
        Tuple[numpy.int64, numpy.int64],
    ],
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(
    actual: Tuple[
        numpy.uint32,
        numpy.uint32,
        Tuple[numpy.int64, numpy.int64],
        Tuple[numpy.int64, numpy.int64],
    ],
    desired: Tuple[
        numpy.uint32,
        numpy.uint32,
        Tuple[numpy.int64, numpy.int64],
        Tuple[numpy.int64, numpy.int64],
    ],
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(
    actual: Tuple[
        numpy.int64,
        numpy.int64,
        Tuple[numpy.int64, numpy.int64],
        Tuple[numpy.int64, numpy.int64],
    ],
    desired: Tuple[
        numpy.int64,
        numpy.int64,
        Tuple[numpy.int64, numpy.int64],
        Tuple[numpy.int64, numpy.int64],
    ],
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(
    actual: Tuple[
        numpy.uint64,
        numpy.uint64,
        Tuple[numpy.int64, numpy.int64],
        Tuple[numpy.int64, numpy.int64],
    ],
    desired: Tuple[
        numpy.uint64,
        numpy.uint64,
        Tuple[numpy.int64, numpy.int64],
        Tuple[numpy.int64, numpy.int64],
    ],
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(
    actual: Tuple[
        numpy.float32,
        numpy.float32,
        Tuple[numpy.int64, numpy.int64],
        Tuple[numpy.int64, numpy.int64],
    ],
    desired: Tuple[
        numpy.float32,
        numpy.float32,
        Tuple[numpy.int64, numpy.int64],
        Tuple[numpy.int64, numpy.int64],
    ],
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(
    actual: Tuple[
        numpy.float64,
        numpy.float64,
        Tuple[numpy.int64, numpy.int64],
        Tuple[numpy.int64, numpy.int64],
    ],
    desired: Tuple[
        numpy.float64,
        numpy.float64,
        Tuple[numpy.int64, numpy.int64],
        Tuple[numpy.int64, numpy.int64],
    ],
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(actual: Type[numpy.int8], desired: Type[numpy.int8]):
    """
    usage.scipy: 5
    """
    ...


@overload
def assert_equal(actual: Literal["best1exp"], desired: Literal["best1exp"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: Literal["_best1"], desired: Literal["_best1"]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(actual: Literal["best1bin"], desired: Literal["best1bin"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: Literal["rand1bin"], desired: Literal["rand1bin"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: Literal["_rand1"], desired: Literal["_rand1"]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(actual: Literal["rand1exp"], desired: Literal["rand1exp"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: Literal["rand2exp"], desired: Literal["rand2exp"]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(actual: Literal["_rand2"], desired: Literal["_rand2"]):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_equal(actual: Literal["best2bin"], desired: Literal["best2bin"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: Literal["_best2"], desired: Literal["_best2"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: Literal["rand2bin"], desired: Literal["rand2bin"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: Literal["randtobest1bin"], desired: Literal["randtobest1bin"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: Literal["_randtobest1"], desired: Literal["_randtobest1"]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(actual: Literal["randtobest1exp"], desired: Literal["randtobest1exp"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: Literal["currenttobest1bin"], desired: Literal["currenttobest1bin"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: Literal["_currenttobest1"], desired: Literal["_currenttobest1"]
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(
    actual: Literal["currenttobest1exp"], desired: Literal["currenttobest1exp"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: List[Union[int, float]], desired: List[Union[int, float]]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(actual: float, desired: numpy.ndarray):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: bool):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: List[Tuple[int, float]]):
    """
    usage.scipy: 7
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: List[Tuple[int, int]]):
    """
    usage.scipy: 6
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: List[Tuple[float, int]]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: List[Tuple[float, float]]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(actual: int, desired: numpy.int64):
    """
    usage.scipy: 6
    """
    ...


@overload
def assert_equal(actual: bool, desired: int):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: numpy.float64):
    """
    usage.scipy: 5
    """
    ...


@overload
def assert_equal(actual: numpy.float64, desired: numpy.ndarray):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: List[Union[float, int]]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(actual: List[Union[list, int]], desired: List[Union[list, int]]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: List[Union[int, list]], desired: List[Union[int, list]]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: Tuple[numpy.ndarray, numpy.ndarray], desired: Tuple[list, list]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: Tuple[numpy.ndarray, numpy.ndarray], desired: Tuple[list, List[int]]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: Tuple[int, float], desired: Tuple[int, float]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: Tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray],
    desired: List[Union[int, float]],
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(
    actual: Tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray, numpy.ndarray],
    desired: List[Union[float, int]],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: Literal["direct"], desired: Literal["direct"]):
    """
    usage.scipy: 6
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: List[decimal.Decimal]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: numpy.dtype, desired: Type[numpy.int8]):
    """
    usage.scipy: 16
    """
    ...


@overload
def assert_equal(actual: numpy.dtype, desired: Type[numpy.uint16]):
    """
    usage.scipy: 10
    """
    ...


@overload
def assert_equal(actual: numpy.dtype, desired: Type[numpy.int16]):
    """
    usage.scipy: 11
    """
    ...


@overload
def assert_equal(actual: numpy.dtype, desired: Type[numpy.uint64]):
    """
    usage.scipy: 10
    """
    ...


@overload
def assert_equal(actual: numpy.dtype, desired: Type[int]):
    """
    usage.scipy: 11
    """
    ...


@overload
def assert_equal(actual: numpy.dtype, desired: Type[numpy.ulonglong]):
    """
    usage.scipy: 10
    """
    ...


@overload
def assert_equal(actual: numpy.dtype, desired: Type[decimal.Decimal]):
    """
    usage.scipy: 8
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: List[complex]):
    """
    usage.scipy: 5
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: numpy.complex128):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: complex):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(actual: Tuple[int, int], desired: List[int]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: numpy.ndarray, err_msg: int):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_equal(actual: bool, desired: numpy.bool_, err_msg: Literal["boxcar, 10, 0"]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(actual: bool, desired: numpy.bool_, err_msg: Literal["boxcar, 10, 9"]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(
    actual: bool, desired: numpy.bool_, err_msg: Literal["bartlett, 51, 26"]
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(
    actual: bool, desired: numpy.bool_, err_msg: Literal["hann, 256, 128"]
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(
    actual: bool, desired: numpy.bool_, err_msg: Literal["hann, 256, 192"]
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(
    actual: bool, desired: numpy.bool_, err_msg: Literal["blackman, 300, 200"]
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(actual: bool, desired: numpy.bool_, err_msg: str):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_equal(
    actual: bool, desired: numpy.bool_, err_msg: Literal["hann, 256, 255"]
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(actual: bool, desired: numpy.bool_, err_msg: Literal["boxcar, 10, 7"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: bool, desired: numpy.bool_, err_msg: Literal["bartlett, 51, 10"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: bool, desired: numpy.bool_, err_msg: Literal["hann, 256, 37"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: bool, desired: numpy.bool_, err_msg: Literal["blackman, 300, 123"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: bool, desired: numpy.bool_, err_msg: Literal["hann, 256, 39"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: bool, desired: numpy.bool_, err_msg: Literal["hann, 64, 0"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: numpy.float64, desired: numpy.float64, err_msg: str):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_equal(actual: numpy.int64, desired: int, err_msg: Literal["[1.]"]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(actual: numpy.int64, desired: int, err_msg: str):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_equal(actual: numpy.matrix, desired: List[List[int]]):
    """
    usage.scipy: 12
    """
    ...


@overload
def assert_equal(actual: Callable, desired: Callable):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: numpy.matrix, desired: numpy.ndarray):
    """
    usage.scipy: 20
    """
    ...


@overload
def assert_equal(actual: Literal["csr"], desired: Literal["csr"]):
    """
    usage.scipy: 14
    """
    ...


@overload
def assert_equal(
    actual: Literal["matrix on the left"], desired: Literal["matrix on the left"]
):
    """
    usage.scipy: 8
    """
    ...


@overload
def assert_equal(
    actual: Literal["matrix on the right"], desired: Literal["matrix on the right"]
):
    """
    usage.scipy: 8
    """
    ...


@overload
def assert_equal(actual: Literal["bsr"], desired: Literal["bsr"]):
    """
    usage.scipy: 12
    """
    ...


@overload
def assert_equal(actual: Literal["coo"], desired: Literal["coo"]):
    """
    usage.scipy: 13
    """
    ...


@overload
def assert_equal(actual: Literal["csc"], desired: Literal["csc"]):
    """
    usage.scipy: 14
    """
    ...


@overload
def assert_equal(actual: Literal["dia"], desired: Literal["dia"]):
    """
    usage.scipy: 14
    """
    ...


@overload
def assert_equal(actual: Literal["dok"], desired: Literal["dok"]):
    """
    usage.scipy: 12
    """
    ...


@overload
def assert_equal(actual: Literal["lil"], desired: Literal["lil"]):
    """
    usage.scipy: 13
    """
    ...


@overload
def assert_equal(actual: numpy.bool_, desired: numpy.bool_):
    """
    usage.dask: 1
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(actual: Type[numpy.bool_], desired: numpy.dtype):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: numpy.int8, desired: numpy.int8):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(actual: Type[numpy.int8], desired: numpy.dtype):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: Type[numpy.uint8], desired: numpy.dtype):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: Type[numpy.int16], desired: numpy.dtype):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: Type[numpy.uint16], desired: numpy.dtype):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: Type[numpy.int32], desired: numpy.dtype):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: Type[numpy.uint32], desired: numpy.dtype):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: Type[numpy.int64], desired: numpy.dtype):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: Type[numpy.uint64], desired: numpy.dtype):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: numpy.int64, desired: numpy.longlong):
    """
    usage.scipy: 5
    """
    ...


@overload
def assert_equal(actual: numpy.uint64, desired: numpy.ulonglong):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(actual: Type[numpy.float32], desired: numpy.dtype):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: Type[numpy.float64], desired: numpy.dtype):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: numpy.float128, desired: numpy.float128):
    """
    usage.scipy: 5
    """
    ...


@overload
def assert_equal(actual: Type[numpy.float128], desired: numpy.dtype):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: Type[numpy.complex64], desired: numpy.dtype):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: Type[numpy.complex128], desired: numpy.dtype):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: numpy.complex256, desired: numpy.complex256):
    """
    usage.scipy: 5
    """
    ...


@overload
def assert_equal(actual: Type[numpy.complex256], desired: numpy.dtype):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: numpy.bool_, desired: int):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: numpy.complex128, desired: int):
    """
    usage.scipy: 7
    """
    ...


@overload
def assert_equal(actual: numpy.dtype, desired: Type[numpy.int32]):
    """
    usage.scipy: 22
    """
    ...


@overload
def assert_equal(actual: numpy.int64, desired: numpy.int64, err_msg: Literal["(0, 0)"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: numpy.int64, desired: numpy.int64, err_msg: Literal["(0, 1)"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: numpy.int64, desired: numpy.int64, err_msg: Literal["(0, -1)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: numpy.int64, desired: numpy.int64, err_msg: Literal["(0, -2)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: numpy.int64, desired: numpy.int64, err_msg: Literal["(0, -5)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: numpy.int64, desired: numpy.int64, err_msg: Literal["(0, array(-1))"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: numpy.int64, desired: numpy.int64, err_msg: Literal["(0, -3)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: numpy.int64, desired: numpy.int64, err_msg: Literal["(1, 0)"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: numpy.int64, desired: numpy.int64, err_msg: Literal["(1, 1)"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: numpy.int64, desired: numpy.int64, err_msg: Literal["(1, -1)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: numpy.int64, desired: numpy.int64, err_msg: Literal["(1, -2)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: numpy.int64, desired: numpy.int64, err_msg: Literal["(1, -5)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: numpy.int64, desired: numpy.int64, err_msg: Literal["(1, array(-1))"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: numpy.int64, desired: numpy.int64, err_msg: Literal["(1, -3)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: numpy.int64, desired: numpy.int64, err_msg: Literal["(-1, 0)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: numpy.int64, desired: numpy.int64, err_msg: Literal["(-1, 1)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: numpy.int64, desired: numpy.int64, err_msg: Literal["(-1, -1)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: numpy.int64, desired: numpy.int64, err_msg: Literal["(-1, -2)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: numpy.int64, desired: numpy.int64, err_msg: Literal["(-1, -5)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: numpy.int64, desired: numpy.int64, err_msg: Literal["(-1, array(-1))"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: numpy.int64, desired: numpy.int64, err_msg: Literal["(-1, -3)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: numpy.int64, desired: numpy.int64, err_msg: Literal["(-2, 0)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: numpy.int64, desired: numpy.int64, err_msg: Literal["(-2, 1)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: numpy.int64, desired: numpy.int64, err_msg: Literal["(-2, -1)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: numpy.int64, desired: numpy.int64, err_msg: Literal["(-2, -2)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: numpy.int64, desired: numpy.int64, err_msg: Literal["(-2, -5)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: numpy.int64, desired: numpy.int64, err_msg: Literal["(-2, array(-1))"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: numpy.int64, desired: numpy.int64, err_msg: Literal["(-2, -3)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: numpy.int64, desired: numpy.int64, err_msg: Literal["(-5, 0)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: numpy.int64, desired: numpy.int64, err_msg: Literal["(-5, 1)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: numpy.int64, desired: numpy.int64, err_msg: Literal["(-5, -1)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: numpy.int64, desired: numpy.int64, err_msg: Literal["(-5, -2)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: numpy.int64, desired: numpy.int64, err_msg: Literal["(-5, -5)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: numpy.int64, desired: numpy.int64, err_msg: Literal["(-5, array(-1))"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: numpy.int64, desired: numpy.int64, err_msg: Literal["(-5, -3)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: numpy.int64, desired: numpy.int64, err_msg: Literal["(array(-1), 0)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: numpy.int64, desired: numpy.int64, err_msg: Literal["(array(-1), 1)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: numpy.int64, desired: numpy.int64, err_msg: Literal["(array(-1), -1)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: numpy.int64, desired: numpy.int64, err_msg: Literal["(array(-1), -2)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: numpy.int64, desired: numpy.int64, err_msg: Literal["(array(-1), -5)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: numpy.int64, desired: numpy.int64, err_msg: str):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: numpy.int64, desired: numpy.int64, err_msg: Literal["(array(-1), -3)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: numpy.int64, desired: numpy.int64, err_msg: Literal["(-3, 0)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: numpy.int64, desired: numpy.int64, err_msg: Literal["(-3, 1)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: numpy.int64, desired: numpy.int64, err_msg: Literal["(-3, -1)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: numpy.int64, desired: numpy.int64, err_msg: Literal["(-3, -2)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: numpy.int64, desired: numpy.int64, err_msg: Literal["(-3, -5)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: numpy.int64, desired: numpy.int64, err_msg: Literal["(-3, array(-1))"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: numpy.int64, desired: numpy.int64, err_msg: Literal["(-3, -3)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: scipy.sparse.csr.csr_matrix, desired: numpy.ndarray):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: numpy.uint64, desired: numpy.int64):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_equal(actual: numpy.uint64, desired: numpy.float64):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_equal(actual: numpy.float32, desired: numpy.float64):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_equal(actual: numpy.complex64, desired: numpy.complex128):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_equal(actual: numpy.dtype, desired: Type[numpy.int64]):
    """
    usage.scipy: 15
    """
    ...


@overload
def assert_equal(actual: scipy.sparse.csc.csc_matrix, desired: numpy.ndarray):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: numpy.longlong, desired: numpy.longlong):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: Type[numpy.longlong], desired: numpy.dtype):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: numpy.ulonglong, desired: numpy.ulonglong):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: Type[numpy.ulonglong], desired: numpy.dtype):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: scipy.sparse.dok.dok_matrix, desired: numpy.ndarray):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: scipy.sparse.lil.lil_matrix, desired: numpy.ndarray):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: numpy.matrix, desired: List[List[int]], err_msg: str):
    """
    usage.scipy: 16
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: float, verbose: bool):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(
    actual: Tuple[Literal["MT19937"], numpy.ndarray, int, int, float],
    desired: Tuple[Literal["MT19937"], numpy.ndarray, int, int, float],
):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_equal(actual: Tuple[float, int], desired: Tuple[numpy.float64, numpy.int64]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: list, desired: list):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: dict, desired: dict):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: List[Tuple[int, int]], desired: List[Tuple[int, int]]):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_equal(
    actual: List[Tuple[Union[None, int], ...]],
    desired: List[Tuple[Union[None, int], ...]],
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(
    actual: numpy.ndarray, desired: int, err_msg: Literal["(0.25, 0.25, 1)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: numpy.ndarray, desired: int, err_msg: Literal["(0.75, 0.75, 0)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: numpy.ndarray, desired: int, err_msg: Literal["(0.3, 0.2, 1)"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: List[set], desired: List[set], err_msg: str):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_equal(
    actual: List[Tuple[int, int, int]], desired: List[Tuple[int, int, int]]
):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_equal(
    actual: List[Tuple[int, int, int, int]], desired: List[Tuple[int, int, int, int]]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: List[Tuple[int, int, int, int, int]],
    desired: List[Tuple[int, int, int, int, int]],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: List[Tuple[int, ...]], desired: List[Tuple[int, ...]]):
    """
    usage.scipy: 12
    """
    ...


@overload
def assert_equal(
    actual: List[Tuple[Tuple[int, int], Tuple[int, int]]],
    desired: List[Tuple[Tuple[int, int], Tuple[int, int]]],
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(actual: List[List[numpy.int64]], desired: List[List[numpy.int64]]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(actual: List[List[int]], desired: List[List[int]]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: numpy.complex128, desired: complex):
    """
    usage.scipy: 26
    """
    ...


@overload
def assert_equal(
    actual: Tuple[numpy.float64, numpy.float64], desired: Tuple[float, float]
):
    """
    usage.scipy: 20
    """
    ...


@overload
def assert_equal(actual: scipy.special.orthogonal.orthopoly1d, desired: numpy.poly1d):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(
    actual: Dict[str, Literal["ignore"]], desired: Dict[str, Literal["ignore"]]
):
    """
    usage.scipy: 5
    """
    ...


@overload
def assert_equal(actual: numpy.complex128, desired: float):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: List[numpy.ndarray], desired: List[numpy.ndarray]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: Tuple[float, float]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: Tuple[numpy.float64, numpy.float64]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: Tuple[int, float]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: Tuple[float, int]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(actual: Tuple[int, int, int], desired: List[int], err_msg: str):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: Tuple[int, int], desired: List[int], err_msg: str):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: Tuple[int, int, int, int], desired: List[int], err_msg: str):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: Tuple[int, int, int, int, int], desired: List[int], err_msg: str
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: Tuple[numpy.int64, numpy.int64]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(actual: Tuple[int], desired: List[int], err_msg: str):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: Tuple[numpy.float64, numpy.float64, numpy.float64, numpy.float64],
    desired: Tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray, numpy.ndarray],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: Tuple[numpy.float64, numpy.float64], desired: Tuple[int, int]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: Tuple[numpy.ndarray, numpy.ndarray], desired: Tuple[int, int]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: Tuple[numpy.ndarray, numpy.ndarray], desired: Tuple[float, float]
):
    """
    usage.scipy: 5
    """
    ...


@overload
def assert_equal(
    actual: Tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray, numpy.ndarray],
    desired: Tuple[float, float, float, float],
):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_equal(actual: List[numpy.ndarray], desired: List[float]):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_equal(
    actual: Tuple[numpy.ndarray, numpy.ndarray], desired: List[Union[float, int]]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: Tuple[float, float], desired: Tuple[numpy.ndarray, numpy.ndarray]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: Literal["a"], desired: Literal["a"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: Literal["a, b"], desired: Literal["a, b"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: Tuple[float, float], desired: scipy.stats.morestats.BartlettResult
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: Tuple[float, float], desired: scipy.stats.morestats.FlignerResult
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: Tuple[Tuple[numpy.ndarray, numpy.ndarray], Tuple[float, float, float]],
    desired: Tuple[Tuple[numpy.ndarray, numpy.ndarray], Tuple[float, float, float]],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: Tuple[
        Tuple[numpy.ndarray, numpy.ndarray], Tuple[numpy.float64, numpy.float64, float]
    ],
    desired: Tuple[Tuple[numpy.ndarray, numpy.ndarray], Tuple[float, float, float]],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: scipy.stats.morestats.WilcoxonResult, desired: Tuple[float, float]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: numpy.float64, desired: numpy.int64):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: scipy.stats.morestats.WilcoxonResult,
    desired: scipy.stats.morestats.WilcoxonResult,
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(
    actual: scipy.stats.morestats.WilcoxonResult,
    desired: Tuple[numpy.float64, numpy.float64],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: Tuple[float, float, float, None], desired: Tuple[float, float, float, None]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: Literal["Dimension mismatch"], desired: Literal["Dimension mismatch"]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: scipy.stats.stats.SpearmanrResult, desired: Tuple[float, float]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: scipy.stats.mstats_basic.SpearmanrResult,
    desired: scipy.stats.stats.SpearmanrResult,
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: scipy.stats.stats.KendalltauResult, desired: Tuple[float, float]
):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: List[List[Union[float, int]]]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: Tuple[int, int], desired: Tuple[numpy.int32, numpy.int32]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: numpy.str_, desired: Literal["showers"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: scipy.stats.stats.ModeResult, desired: Tuple[int, int]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: scipy.stats.mstats_basic.ModeResult, desired: Tuple[int, int]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: List[Union[int, float]]):
    """
    usage.scipy: 5
    """
    ...


@overload
def assert_equal(actual: numpy.ma.core.MaskedArray, desired: float):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: Type[float], desired: Type[float]):
    """
    usage.scipy: 1
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
    actual: scipy.stats.stats.Ttest_relResult, desired: Tuple[float, float]
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(
    actual: scipy.stats.stats.Ttest_relResult,
    desired: Tuple[List[Union[float, int]], List[Union[float, int]]],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: scipy.stats.stats.Ttest_indResult, desired: Tuple[float, float]
):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_equal(
    actual: scipy.stats.stats.Ttest_indResult,
    desired: Tuple[List[Union[float, int]], List[Union[float, int]]],
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(
    actual: scipy.stats.stats.Ttest_1sampResult, desired: Tuple[float, float]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: scipy.stats.stats.Ttest_1sampResult,
    desired: Tuple[List[Union[float, int]], List[Union[float, int]]],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: Tuple[numpy.ndarray, numpy.ndarray],
    desired: Tuple[List[float], List[float]],
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(
    actual: Tuple[numpy.ma.core.MaskedArray, numpy.ma.core.MaskedArray],
    desired: Tuple[float, float],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(
    actual: Tuple[numpy.int64, numpy.int64], desired: Tuple[numpy.int64, numpy.int64]
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_equal(actual: numpy.dtype, desired: None):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(actual: List[float], desired: numpy.ndarray):
    """
    usage.matplotlib: 1
    usage.scipy: 1
    usage.sklearn: 1
    """
    ...


@overload
def assert_equal(
    actual: scipy.stats.stats.F_onewayResult, desired: Tuple[float, float]
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(actual: scipy.stats.stats.KruskalResult, desired: Tuple[float, float]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_equal(actual: List[numpy.ndarray], desired: numpy.ndarray):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def assert_equal(
    actual: Tuple[List[Tuple[Literal["x"]]], Tuple[None, ...]],
    desired: Tuple[List[Tuple[Literal["x"]]], Tuple[None, ...]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def assert_equal(
    actual: Tuple[List[Tuple[Literal["x"], Literal["y"]]], Tuple[None, ...]],
    desired: Tuple[List[Tuple[Literal["x"], Literal["y"]]], Tuple[None, ...]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def assert_equal(
    actual: Tuple[List[Tuple[Literal["x", "y"]]], Tuple[None, ...]],
    desired: Tuple[List[Tuple[Literal["x", "y"]]], Tuple[None, ...]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def assert_equal(
    actual: Tuple[List[Tuple[Literal["x"]]], Tuple[Literal["y"]]],
    desired: Tuple[List[Tuple[Literal["x"]]], Tuple[Literal["y"]]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def assert_equal(
    actual: Tuple[
        List[Tuple[Literal["x"]]], List[Tuple[Union[Literal["y"], None], ...]]
    ],
    desired: Tuple[
        List[Tuple[Literal["x"]]], List[Tuple[Union[Literal["y"], None], ...]]
    ],
):
    """
    usage.dask: 1
    """
    ...


@overload
def assert_equal(
    actual: Tuple[
        List[Tuple[Union[None, Literal["c", "b", "a", "d"]], ...]],
        Tuple[Literal["d"], Literal["e"]],
    ],
    desired: Tuple[
        List[Tuple[Union[None, Literal["c", "b", "a", "d"]], ...]],
        Tuple[Literal["d"], Literal["e"]],
    ],
):
    """
    usage.dask: 1
    """
    ...


@overload
def assert_equal(actual: numpy.bool_, desired: numpy.ndarray):
    """
    usage.dask: 1
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: numpy.bool_):
    """
    usage.dask: 1
    """
    ...


@overload
def assert_equal(
    actual: List[
        Tuple[
            Tuple[Literal["y"], int],
            Tuple[Callable, Tuple[Literal["x"], numpy.int64], Tuple[numpy.ndarray]],
        ]
    ],
    desired: List[
        Tuple[
            Tuple[Literal["y"], int],
            Tuple[Callable, Tuple[Literal["x"], int], Tuple[numpy.ndarray]],
        ]
    ],
):
    """
    usage.dask: 1
    """
    ...


@overload
def assert_equal(
    actual: List[
        Tuple[
            Tuple[Literal["y"], int, int],
            Tuple[
                Callable,
                Tuple[Literal["x"], numpy.int64, int],
                Tuple[numpy.ndarray, slice[None, None, None]],
            ],
        ]
    ],
    desired: List[
        Tuple[
            Tuple[Literal["y"], int, int],
            Tuple[
                Callable,
                Tuple[Literal["x"], int, int],
                Tuple[numpy.ndarray, slice[None, None, None]],
            ],
        ]
    ],
):
    """
    usage.dask: 1
    """
    ...


@overload
def assert_equal(
    actual: Dict[
        Tuple[Literal["y"], int],
        Tuple[Callable, Tuple[Literal["x"], numpy.int64], Tuple[numpy.ndarray]],
    ],
    desired: Dict[
        Tuple[Literal["y"], int],
        Tuple[Callable, Tuple[Literal["x"], int], Tuple[List[int]]],
    ],
):
    """
    usage.dask: 1
    """
    ...


@overload
def assert_equal(
    actual: Dict[
        Tuple[Literal["y"], int, int],
        Tuple[
            Callable,
            Tuple[Literal["x"], int, numpy.int64],
            Tuple[slice[None, None, None], numpy.ndarray],
        ],
    ],
    desired: Dict[
        Tuple[Literal["y"], int, int],
        Tuple[
            Callable,
            Tuple[Literal["x"], int, int],
            Tuple[slice[None, None, None], List[int]],
        ],
    ],
):
    """
    usage.dask: 1
    """
    ...


@overload
def assert_equal(
    actual: Dict[
        Tuple[Literal["y"], int, int],
        Tuple[
            Callable,
            Tuple[Literal["x"], numpy.int64, int],
            Tuple[numpy.ndarray, slice[None, None, None]],
        ],
    ],
    desired: Dict[
        Tuple[Literal["y"], int, int],
        Tuple[
            Callable,
            Tuple[Literal["x"], numpy.int64, int],
            Tuple[numpy.ndarray, slice[None, None, None]],
        ],
    ],
):
    """
    usage.dask: 2
    """
    ...


@overload
def assert_equal(actual: Tuple[int, float, float], desired: Tuple[int, float, float]):
    """
    usage.dask: 1
    """
    ...


@overload
def assert_equal(
    actual: Tuple[int, int, float, float], desired: Tuple[int, int, float, float]
):
    """
    usage.dask: 1
    """
    ...


@overload
def assert_equal(
    actual: Dict[
        str,
        Union[
            numpy.ndarray,
            numpy.ma.core.MaskedArray,
            List[
                Dict[
                    Literal["kernel", "gamma", "C", "degree"],
                    Union[Literal["rbf", "poly"], float, int],
                ]
            ],
        ],
    ],
    desired: Dict[
        str,
        Union[
            numpy.ndarray,
            numpy.ma.core.MaskedArray,
            List[
                Dict[
                    Literal["kernel", "gamma", "C", "degree"],
                    Union[Literal["rbf", "poly"], float, int],
                ]
            ],
        ],
    ],
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_equal(
    actual: Dict[
        str,
        Union[
            numpy.ndarray,
            numpy.ma.core.MaskedArray,
            List[Dict[Literal["C", "gamma"], numpy.float64]],
        ],
    ],
    desired: Dict[
        str,
        Union[
            numpy.ndarray,
            numpy.ma.core.MaskedArray,
            List[Dict[Literal["C", "gamma"], numpy.float64]],
        ],
    ],
):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_equal(
    actual: Dict[
        str,
        Union[
            numpy.ndarray, numpy.ma.core.MaskedArray, List[Dict[Literal["C"], float]]
        ],
    ],
    desired: Dict[
        str,
        Union[
            numpy.ndarray, numpy.ma.core.MaskedArray, List[Dict[Literal["C"], float]]
        ],
    ],
):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_equal(
    actual: List[Tuple[numpy.ndarray, numpy.ndarray]],
    desired: List[Tuple[numpy.ndarray, numpy.ndarray]],
):
    """
    usage.sklearn: 19
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
    usage.scipy: 2
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
def assert_warns(
    warning_class: Type[scipy.cluster.hierarchy.ClusterWarning],
    *args: Literal["v", "t"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_warns(warning_class: Type[numpy.ComplexWarning], *args: Literal["v", "t"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_warns(
    warning_class: Type[scipy.linalg._matfuncs_inv_ssq.LogmExactlySingularWarning],
    *args: Literal["v", "t"],
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_warns(
    warning_class: Type[scipy.linalg._matfuncs_inv_ssq.LogmNearlySingularWarning],
    *args: Literal["v", "t"],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_warns(
    warning_class: Type[scipy.odr.odrpack.OdrWarning], *args: Literal["v", "t"]
):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_warns(
    warning_class: Type[scipy.optimize.optimize.OptimizeWarning],
    *args: Literal["v", "t"],
):
    """
    usage.scipy: 4
    """
    ...


@overload
def assert_warns(
    warning_class: Type[scipy.optimize.linesearch.LineSearchWarning],
    *args: Literal["v", "t"],
):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_warns(warning_class: Type[DeprecationWarning], *args: Literal["v", "t"]):
    """
    usage.scipy: 2
    """
    ...


@overload
def assert_warns(warning_class: Type[scipy.optimize.optimize.OptimizeWarning]):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_warns(warning_class: Type[RuntimeWarning], *args: Literal["v", "t"]):
    """
    usage.scipy: 6
    """
    ...


@overload
def assert_warns(warning_class: Type[numpy.VisibleDeprecationWarning]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_warns(warning_class: Type[scipy.stats.stats.PearsonRConstantInputWarning]):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_warns(
    warning_class: Type[scipy.stats.stats.PearsonRNearConstantInputWarning],
):
    """
    usage.scipy: 1
    """
    ...


@overload
def assert_warns(warning_class: Type[scipy.stats.stats.SpearmanRConstantInputWarning]):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_warns(warning_class: Type[scipy.stats.stats.F_onewayConstantInputWarning]):
    """
    usage.scipy: 3
    """
    ...


@overload
def assert_warns(warning_class: Type[scipy.stats.stats.F_onewayBadInputSizesWarning]):
    """
    usage.scipy: 3
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


def assert_warns(
    warning_class: Union[Type[sklearn.exceptions.ConvergenceWarning], type],
    *args: Literal["v", "t"],
):
    """
    usage.scipy: 39
    usage.skimage: 5
    usage.sklearn: 1
    """
    ...


class suppress_warnings:
    @overload
    def filter(self, /, message: str):
        """
        usage.scipy: 7
        """
        ...

    @overload
    def filter(self, /, category: Type[DeprecationWarning]):
        """
        usage.scipy: 5
        """
        ...

    @overload
    def filter(
        self, /, category: Type[RuntimeWarning], message: Literal["divide by zero"]
    ):
        """
        usage.scipy: 2
        """
        ...

    @overload
    def filter(self, /, category: Type[RuntimeWarning], message: str):
        """
        usage.scipy: 7
        """
        ...

    @overload
    def filter(self, /, message: Literal["Got unexpected kwarg"]):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def filter(
        self, /, category: Type[DeprecationWarning], message: Literal[".*frechet_"]
    ):
        """
        usage.scipy: 5
        """
        ...

    @overload
    def filter(
        self, /, category: Type[UserWarning], message: Literal["p-value floored"]
    ):
        """
        usage.scipy: 2
        """
        ...

    @overload
    def filter(
        self, /, category: Type[UserWarning], message: Literal["p-value capped"]
    ):
        """
        usage.scipy: 2
        """
        ...

    @overload
    def filter(self, /, category: Type[UserWarning], message: str):
        """
        usage.scipy: 6
        """
        ...

    def filter(self, /, category: type = ..., message: str = ...):
        """
        usage.scipy: 37
        """
        ...

    @overload
    def record(self, /, message: str):
        """
        usage.scipy: 1
        """
        ...

    @overload
    def record(self, /, message: Literal["Got unexpected kwarg"]):
        """
        usage.scipy: 1
        """
        ...

    def record(self, /, message: str):
        """
        usage.scipy: 2
        """
        ...
