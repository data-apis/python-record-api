from typing import *


@overload
def assert_(val: numpy.bool_):
    """
    usage.skimage: 58
    """
    ...


@overload
def assert_(val: numpy.bool_, msg: str):
    """
    usage.skimage: 2
    """
    ...


@overload
def assert_(val: bool):
    """
    usage.skimage: 18
    """
    ...


@overload
def assert_(val: object, msg: object = ...):
    """
    usage.scipy: 1706
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
    usage.skimage: 1
    usage.sklearn: 2
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: int, atol: float):
    """
    usage.skimage: 15
    usage.sklearn: 2
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: numpy.ndarray, rtol: float):
    """
    usage.matplotlib: 3
    usage.skimage: 11
    usage.sklearn: 70
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: numpy.ndarray):
    """
    usage.matplotlib: 22
    usage.skimage: 57
    usage.sklearn: 264
    usage.xarray: 21
    """
    ...


@overload
def assert_allclose(actual: float, desired: float, atol: float):
    """
    usage.skimage: 3
    """
    ...


@overload
def assert_allclose(actual: float, desired: numpy.float64, atol: float):
    """
    usage.skimage: 3
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: List[float]):
    """
    usage.matplotlib: 3
    usage.skimage: 6
    usage.sklearn: 6
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, rtol: float, atol: int
):
    """
    usage.skimage: 1
    usage.sklearn: 2
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: int):
    """
    usage.matplotlib: 2
    usage.skimage: 22
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.float64, desired: numpy.float64):
    """
    usage.skimage: 2
    usage.sklearn: 21
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: numpy.ndarray, atol: float):
    """
    usage.matplotlib: 100
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
    usage.skimage: 1
    usage.sklearn: 7
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: Tuple[float, float]):
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.float64, desired: int):
    """
    usage.matplotlib: 1
    usage.skimage: 1
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.float64, desired: int, rtol: float, atol: float):
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: List[numpy.float64], atol: float):
    """
    usage.skimage: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: numpy.float64):
    """
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
    usage.sklearn: 5
    usage.xarray: 3
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: float):
    """
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
    actual: object,
    desired: object,
    rtol: Union[int, float, bool, numpy.float64] = ...,
    atol: Union[float, int, numpy.float128, numpy.float32, numpy.float64] = ...,
    err_msg: Union[
        str, float, Tuple[Union[complex, int, float, numpy.float64], ...]
    ] = ...,
    verbose: bool = ...,
):
    """
    usage.scipy: 4704
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
def assert_allclose(actual: List[numpy.float64], desired: List[numpy.float64]):
    """
    usage.matplotlib: 1
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
def assert_allclose(actual: numpy.ndarray, desired: List[float], rtol: float):
    """
    usage.matplotlib: 3
    usage.sklearn: 6
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
def assert_allclose(actual: numpy.float64, desired: float, atol: float):
    """
    usage.matplotlib: 1
    usage.sklearn: 3
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: List[int]):
    """
    usage.matplotlib: 4
    usage.sklearn: 9
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: List[Union[float, int]]):
    """
    usage.matplotlib: 2
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: List[Union[int, float]]):
    """
    usage.matplotlib: 2
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
def assert_allclose(actual: List[Union[int, float]], desired: numpy.ndarray):
    """
    usage.matplotlib: 1
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
def assert_allclose(actual: numpy.ndarray, desired: List[List[Union[int, float]]]):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: List[List[int]]):
    """
    usage.sklearn: 5
    """
    ...


@overload
def assert_allclose(actual: float, desired: float, rtol: float):
    """
    usage.sklearn: 9
    """
    ...


@overload
def assert_allclose(actual: float, desired: numpy.float32, rtol: float):
    """
    usage.sklearn: 7
    """
    ...


@overload
def assert_allclose(actual: float, desired: numpy.float64, rtol: float):
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
def assert_allclose(actual: numpy.float64, desired: numpy.float64, rtol: float):
    """
    usage.sklearn: 10
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, rtol: float, atol: float
):
    """
    usage.sklearn: 15
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: List[numpy.float64], rtol: float):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.float64, desired: int, rtol: float):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: List[numpy.float64]):
    """
    usage.sklearn: 4
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: List[Union[numpy.float64, float]]):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: numpy.ndarray, err_msg: str):
    """
    usage.sklearn: 38
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
    rtol: float,
    atol: float,
    err_msg: str,
):
    """
    usage.sklearn: 5
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, atol: float, err_msg: str
):
    """
    usage.sklearn: 7
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
def assert_allclose(actual: numpy.ndarray, desired: List[int], rtol: float):
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
    actual: numpy.ndarray, desired: List[Union[int, float]], rtol: float
):
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
def assert_allclose(
    actual: numpy.float64, desired: numpy.float64, rtol: float, atol: float
):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: List[Union[float, int]], rtol: int, atol: float
):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_allclose(actual: numpy.float64, desired: float, rtol: int, atol: float):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(actual: float, desired: float):
    """
    usage.sklearn: 3
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
def assert_allclose(actual: float, desired: int):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(actual: int, desired: int):
    """
    usage.sklearn: 1
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
def assert_allclose(actual: float, desired: numpy.float64, err_msg: str):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(actual: float, desired: numpy.float64):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.float64, desired: float, err_msg: str):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: List[List[float]]):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: List[List[numpy.float64]]):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(actual: numpy.float64, desired: numpy.float64, atol: float):
    """
    usage.sklearn: 3
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
    actual: numpy.float64, desired: numpy.float64, rtol: int, atol: float
):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_allclose(actual: numpy.ndarray, desired: List[List[float]], rtol: float):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_allclose(
    actual: numpy.ndarray, desired: numpy.ndarray, rtol: int, atol: float
):
    """
    usage.sklearn: 3
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
    usage.scipy: 4704
    usage.skimage: 158
    usage.sklearn: 760
    usage.xarray: 38
    """
    ...


@overload
def assert_almost_equal(actual: numpy.float64, desired: int):
    """
    usage.skimage: 7
    usage.sklearn: 141
    """
    ...


@overload
def assert_almost_equal(actual: numpy.float64, desired: float):
    """
    usage.matplotlib: 8
    usage.skimage: 47
    usage.sklearn: 189
    """
    ...


@overload
def assert_almost_equal(actual: numpy.ndarray, desired: numpy.ndarray, decimal: int):
    """
    usage.skimage: 15
    usage.sklearn: 77
    """
    ...


@overload
def assert_almost_equal(actual: numpy.float64, desired: float, decimal: int):
    """
    usage.matplotlib: 3
    usage.skimage: 35
    usage.sklearn: 109
    """
    ...


@overload
def assert_almost_equal(actual: numpy.float64, desired: numpy.float64, decimal: int):
    """
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
    usage.skimage: 1
    """
    ...


@overload
def assert_almost_equal(actual: numpy.ndarray, desired: numpy.float64, decimal: int):
    """
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
    usage.skimage: 5
    usage.sklearn: 10
    """
    ...


@overload
def assert_almost_equal(actual: numpy.ndarray, desired: List[float]):
    """
    usage.skimage: 2
    usage.sklearn: 3
    """
    ...


@overload
def assert_almost_equal(actual: numpy.ndarray, desired: List[int]):
    """
    usage.skimage: 1
    usage.sklearn: 6
    """
    ...


@overload
def assert_almost_equal(actual: numpy.float64, desired: numpy.float64):
    """
    usage.matplotlib: 2
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
    usage.skimage: 5
    usage.sklearn: 2
    """
    ...


@overload
def assert_almost_equal(actual: numpy.ndarray, desired: numpy.float64):
    """
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
    usage.skimage: 3
    usage.sklearn: 4
    """
    ...


@overload
def assert_almost_equal(actual: float, desired: int):
    """
    usage.skimage: 8
    usage.sklearn: 10
    """
    ...


@overload
def assert_almost_equal(actual: Tuple[float, float], desired: Tuple[float, float]):
    """
    usage.matplotlib: 1
    usage.skimage: 3
    """
    ...


@overload
def assert_almost_equal(actual: numpy.ndarray, desired: List[Union[int, float]]):
    """
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
def assert_almost_equal(
    actual: object,
    desired: object,
    decimal: int = ...,
    verbose: bool = ...,
    err_msg: str = ...,
):
    """
    usage.scipy: 1344
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
def assert_almost_equal(actual: numpy.ndarray, desired: float):
    """
    usage.matplotlib: 4
    usage.sklearn: 5
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
def assert_almost_equal(actual: float, desired: numpy.float64):
    """
    usage.sklearn: 9
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
def assert_almost_equal(actual: float, desired: float, decimal: int):
    """
    usage.sklearn: 5
    """
    ...


@overload
def assert_almost_equal(actual: numpy.float64, desired: numpy.ndarray):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_almost_equal(actual: numpy.int64, desired: numpy.ndarray):
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
def assert_almost_equal(actual: int, desired: numpy.float64, decimal: int):
    """
    usage.sklearn: 4
    """
    ...


@overload
def assert_almost_equal(
    actual: numpy.ndarray, desired: numpy.ndarray, decimal: int, err_msg: str
):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_almost_equal(actual: numpy.float64, desired: numpy.float64, err_msg: str):
    """
    usage.sklearn: 3
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
def assert_almost_equal(actual: numpy.int64, desired: float):
    """
    usage.sklearn: 1
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
def assert_approx_equal(
    actual: Union[numpy.float64, float],
    desired: Union[float, int, numpy.float64],
    significant: int = ...,
    err_msg: str = ...,
):
    """
    usage.scipy: 220
    """
    ...


@overload
def assert_approx_equal(actual: numpy.float64, desired: float):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def assert_approx_equal(actual: numpy.float64, desired: numpy.float64):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_approx_equal(
    actual: numpy.float64, desired: numpy.float64, significant: int
):
    """
    usage.sklearn: 1
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
    usage.skimage: 6
    usage.sklearn: 61
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ndarray, y: List[Union[int, float]]):
    """
    usage.matplotlib: 1
    usage.skimage: 3
    usage.sklearn: 4
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ndarray, y: List[float]):
    """
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
    usage.skimage: 5
    usage.sklearn: 14
    """
    ...


@overload
def assert_array_almost_equal(
    x: object, y: object, decimal: int = ..., err_msg: str = ...
):
    """
    usage.scipy: 3904
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
def assert_array_almost_equal(x: numpy.ndarray, y: numpy.ndarray, decimal: int):
    """
    usage.matplotlib: 4
    usage.sklearn: 226
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
def assert_array_almost_equal(x: numpy.float64, y: float):
    """
    usage.matplotlib: 4
    usage.sklearn: 7
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
def assert_array_almost_equal(x: List[float], y: numpy.ndarray):
    """
    usage.matplotlib: 1
    usage.sklearn: 2
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
def assert_array_almost_equal(x: numpy.ndarray, y: numpy.float64):
    """
    usage.matplotlib: 1
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
def assert_array_almost_equal(x: numpy.ndarray, y: List[float], decimal: int):
    """
    usage.matplotlib: 4
    usage.sklearn: 61
    """
    ...


@overload
def assert_array_almost_equal(x: List[float], y: numpy.ndarray, decimal: int):
    """
    usage.matplotlib: 1
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
def assert_array_almost_equal(x: numpy.float64, y: numpy.float64):
    """
    usage.matplotlib: 3
    usage.sklearn: 25
    """
    ...


@overload
def assert_array_almost_equal(x: Tuple[numpy.float64, numpy.float64], y: numpy.ndarray):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def assert_array_almost_equal(x: dask.array.core.Array, y: numpy.ndarray):
    """
    usage.dask: 1
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ndarray, y: List[List[Union[float, int]]]):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_almost_equal(x: float, y: numpy.float64):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_array_almost_equal(x: float, y: float, decimal: int):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.float64, y: numpy.float64, decimal: int):
    """
    usage.sklearn: 13
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.float64, y: numpy.ndarray, decimal: int):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_array_almost_equal(
    x: numpy.ndarray, y: numpy.ndarray, decimal: int, err_msg: str
):
    """
    usage.sklearn: 5
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ndarray, y: numpy.ndarray, err_msg: str):
    """
    usage.sklearn: 8
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
def assert_array_almost_equal(x: numpy.ndarray, y: int, decimal: int):
    """
    usage.sklearn: 17
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
def assert_array_almost_equal(x: List[List[Union[int, float]]], y: numpy.ndarray):
    """
    usage.sklearn: 1
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
def assert_array_almost_equal(x: numpy.ndarray, y: List[List[int]]):
    """
    usage.sklearn: 4
    """
    ...


@overload
def assert_array_almost_equal(x: List[numpy.ndarray], y: List[numpy.ndarray]):
    """
    usage.sklearn: 4
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
def assert_array_almost_equal(x: numpy.float64, y: int):
    """
    usage.sklearn: 7
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.float32, y: numpy.float64):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ndarray, y: List[int], decimal: int):
    """
    usage.sklearn: 12
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ndarray, y: float, decimal: int):
    """
    usage.sklearn: 3
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.float32, y: numpy.float32):
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
def assert_array_almost_equal(x: float, y: float):
    """
    usage.sklearn: 2
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
def assert_array_almost_equal(x: numpy.float64, y: float, decimal: int):
    """
    usage.sklearn: 25
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ndarray, y: List[List[float]]):
    """
    usage.sklearn: 16
    """
    ...


@overload
def assert_array_almost_equal(
    x: numpy.ndarray, y: List[Union[float, int]], decimal: int
):
    """
    usage.sklearn: 4
    """
    ...


@overload
def assert_array_almost_equal(
    x: numpy.ndarray, y: List[Union[int, float]], decimal: int
):
    """
    usage.sklearn: 3
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ndarray, y: List[numpy.float64]):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.matrix, y: numpy.ndarray):
    """
    usage.sklearn: 5
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ndarray, y: List[numpy.float64], decimal: int):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ndarray, y: List[Union[float, int]]):
    """
    usage.sklearn: 4
    """
    ...


@overload
def assert_array_almost_equal(x: List[numpy.float64], y: List[numpy.float64]):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ndarray, y: numpy.ndarray, decimal: bool):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ndarray, y: float):
    """
    usage.sklearn: 15
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ndarray, y: List[numpy.int64]):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_almost_equal(x: numpy.ndarray, y: List[List[float]], decimal: int):
    """
    usage.sklearn: 4
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
def assert_array_almost_equal(x: List[numpy.float64], y: List[float]):
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
def assert_array_almost_equal(x: float, y: numpy.float64, decimal: int):
    """
    usage.sklearn: 2
    """
    ...


@overload
def assert_array_almost_equal(x: int, y: numpy.float64):
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
def assert_array_almost_equal_nulp(
    x: Union[numpy.float64, numpy.matrix, int, float, numpy.ndarray],
    y: Union[float, numpy.ndarray, int, numpy.float64],
    nulp: Union[int, float] = ...,
):
    """
    usage.scipy: 67
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
    usage.skimage: 321
    usage.sklearn: 919
    usage.xarray: 164
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: int):
    """
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
    usage.skimage: 3
    usage.sklearn: 10
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: List[int]):
    """
    usage.matplotlib: 10
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
    usage.skimage: 8
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: List[List[int]]):
    """
    usage.matplotlib: 12
    usage.skimage: 12
    usage.sklearn: 33
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: List[List[float]]):
    """
    usage.matplotlib: 1
    usage.skimage: 6
    usage.sklearn: 14
    """
    ...


@overload
def assert_array_equal(x: int, y: int):
    """
    usage.matplotlib: 3
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
    usage.xarray: 2
    """
    ...


@overload
def assert_array_equal(x: List[int], y: numpy.ndarray):
    """
    usage.matplotlib: 1
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
    usage.sklearn: 8
    usage.xarray: 2
    """
    ...


@overload
def assert_array_equal(x: bool, y: bool):
    """
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
    usage.xarray: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.float64, y: float):
    """
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
def assert_array_equal(x: object, y: object, err_msg: str = ...):
    """
    usage.scipy: 1623
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
def assert_array_equal(x: numpy.ndarray, y: List[numpy.float64]):
    """
    usage.matplotlib: 6
    usage.sklearn: 8
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
def assert_array_equal(x: numpy.ndarray, y: List[Union[int, float]]):
    """
    usage.matplotlib: 1
    usage.sklearn: 2
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
def assert_array_equal(x: list, y: list):
    """
    usage.matplotlib: 2
    usage.sklearn: 2
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
def assert_array_equal(x: numpy.ndarray, y: List[float]):
    """
    usage.matplotlib: 1
    usage.sklearn: 11
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: List[List[bool]]):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: bool):
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
def assert_array_equal(x: numpy.ndarray, y: list):
    """
    usage.sklearn: 5
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: numpy.ndarray, err_msg: str):
    """
    usage.sklearn: 35
    """
    ...


@overload
def assert_array_equal(x: numpy.ndarray, y: List[Union[float, int]]):
    """
    usage.sklearn: 2
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
def assert_array_equal(x: numpy.matrix, y: int):
    """
    usage.sklearn: 1
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
def assert_array_equal(x: float, y: float):
    """
    usage.sklearn: 2
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
def assert_array_equal(x: numpy.float64, y: int):
    """
    usage.sklearn: 3
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
def assert_array_equal(x: List[Union[int, float]], y: numpy.ndarray):
    """
    usage.sklearn: 2
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
def assert_array_equal(x: numpy.matrix, y: numpy.matrix):
    """
    usage.sklearn: 1
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
def assert_array_equal(x: numpy.ndarray, y: numpy.memmap):
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
    usage.skimage: 16
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_less(x: numpy.ndarray, y: numpy.ndarray):
    """
    usage.skimage: 2
    usage.sklearn: 4
    """
    ...


@overload
def assert_array_less(x: numpy.float64, y: float):
    """
    usage.skimage: 2
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_less(x: object, y: object, err_msg: str = ...):
    """
    usage.scipy: 92
    """
    ...


@overload
def assert_array_less(x: numpy.ma.core.MaskedArray, y: float):
    """
    usage.matplotlib: 3
    """
    ...


@overload
def assert_array_less(x: numpy.ndarray, y: int):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_less(x: float, y: numpy.ndarray):
    """
    usage.sklearn: 3
    """
    ...


@overload
def assert_array_less(x: int, y: numpy.ndarray):
    """
    usage.sklearn: 1
    """
    ...


@overload
def assert_array_less(x: numpy.ndarray, y: float):
    """
    usage.sklearn: 3
    """
    ...


@overload
def assert_array_less(x: int, y: numpy.float64):
    """
    usage.sklearn: 1
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
    usage.skimage: 10
    usage.xarray: 1
    """
    ...


@overload
def assert_equal(actual: int, desired: int):
    """
    usage.skimage: 68
    """
    ...


@overload
def assert_equal(actual: numpy.float64, desired: numpy.float64):
    """
    usage.skimage: 7
    """
    ...


@overload
def assert_equal(actual: numpy.int64, desired: int):
    """
    usage.skimage: 19
    usage.xarray: 1
    """
    ...


@overload
def assert_equal(actual: str, desired: str):
    """
    usage.skimage: 4
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: numpy.ndarray):
    """
    usage.dask: 7
    usage.matplotlib: 3
    usage.skimage: 241
    usage.sklearn: 2
    usage.xarray: 3
    """
    ...


@overload
def assert_equal(actual: Tuple[int, int, int], desired: Tuple[int, int, int]):
    """
    usage.skimage: 20
    """
    ...


@overload
def assert_equal(actual: numpy.dtype, desired: numpy.dtype):
    """
    usage.skimage: 4
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: List[int]):
    """
    usage.dask: 2
    usage.skimage: 21
    """
    ...


@overload
def assert_equal(actual: numpy.float64, desired: int):
    """
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
    usage.skimage: 3
    usage.xarray: 2
    """
    ...


@overload
def assert_equal(actual: Tuple[int, int, int, int], desired: Tuple[int, int, int, int]):
    """
    usage.skimage: 7
    """
    ...


@overload
def assert_equal(
    actual: Tuple[int, int, int, int, int], desired: Tuple[int, int, int, int, int]
):
    """
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
    usage.skimage: 4
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: List[List[int]]):
    """
    usage.skimage: 8
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: Tuple[int, int]):
    """
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
    usage.skimage: 1
    """
    ...


@overload
def assert_equal(actual: Tuple[int, int], desired: Tuple[int, int]):
    """
    usage.skimage: 40
    """
    ...


@overload
def assert_equal(actual: None, desired: None):
    """
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
    usage.skimage: 1
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: int):
    """
    usage.skimage: 56
    usage.xarray: 2
    """
    ...


@overload
def assert_equal(actual: float, desired: float):
    """
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
    usage.skimage: 1
    """
    ...


@overload
def assert_equal(actual: bool, desired: bool, err_msg: str):
    """
    usage.skimage: 4
    """
    ...


@overload
def assert_equal(actual: numpy.dtype, desired: Type[bool]):
    """
    usage.skimage: 4
    """
    ...


@overload
def assert_equal(actual: numpy.dtype, desired: Type[numpy.uint8]):
    """
    usage.skimage: 5
    """
    ...


@overload
def assert_equal(actual: numpy.uint8, desired: numpy.uint8):
    """
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
    usage.skimage: 2
    """
    ...


@overload
def assert_equal(actual: numpy.float32, desired: float):
    """
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
    usage.skimage: 2
    """
    ...


@overload
def assert_equal(actual: numpy.int8, desired: int):
    """
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
    usage.xarray: 1
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: numpy.int32):
    """
    usage.xarray: 1
    """
    ...


@overload
def assert_equal(actual: numpy.float32, desired: numpy.float32):
    """
    usage.xarray: 1
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: numpy.float32):
    """
    usage.xarray: 1
    """
    ...


@overload
def assert_equal(actual: object, desired: object):
    """
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
def assert_equal(
    actual: object, desired: object, err_msg: Union[str, int] = ..., verbose: bool = ...
):
    """
    usage.scipy: 4569
    """
    ...


@overload
def assert_equal(actual: list, desired: list):
    """
    usage.matplotlib: 2
    """
    ...


@overload
def assert_equal(actual: float, desired: numpy.float64):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: List[float]):
    """
    usage.matplotlib: 1
    usage.sklearn: 1
    """
    ...


@overload
def assert_equal(actual: numpy.ndarray, desired: List[bool]):
    """
    usage.matplotlib: 2
    """
    ...


@overload
def assert_equal(actual: List[numpy.ndarray], desired: numpy.ndarray):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def assert_equal(actual: List[float], desired: numpy.ndarray):
    """
    usage.matplotlib: 1
    usage.sklearn: 1
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
def assert_equal(actual: numpy.bool_, desired: numpy.bool_):
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
def assert_warns(warning_class: type, *args: Literal["v", "t"]):
    """
    usage.scipy: 39
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

    def record(self, /, message: str, category: type = ...):
        """
        usage.scipy: 11
        """
        ...
