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
    rtol: Union[(int, float)] = ...,
    atol: Union[(int, float)] = ...,
    err_msg: Literal[
        (
            "",
            "predict of VotingRegressor is not invariant when a",
            "fit_transform and transform outcomes not consisten",
            "VotingRegressor",
            "For StackingClassifier sample_weight=None is not e",
            "Idempotency check failed for method decision_funct",
            "predict of StackingRegressor is not invariant when",
            "StackingRegressor",
            "transform of StackingClassifier is not invariant w",
            "predict of StackingClassifier is not invariant whe",
            "consecutive fit_transform outcomes not consistent ",
            "Idempotency check failed for method predict_proba",
            "transform of VotingRegressor is not invariant when",
            "For VotingRegressor sample_weight=None is not equi",
            "predict_proba of StackingClassifier is not invaria",
            "predict of VotingClassifier is not invariant when ",
            "VotingClassifier",
            "decision_function of StackingClassifier is not inv",
            "Idempotency check failed for method predict",
            "transform of StackingRegressor is not invariant wh",
            "StackingClassifier",
            "For VotingClassifier sample_weight=None is not equ",
            "transform of VotingClassifier is not invariant whe",
            "Idempotency check failed for method transform",
            "For StackingRegressor sample_weight=None is not eq",
        )
    ] = ...,
):
    "usage.skimage: 169, usage.xarray: 27, usage.sklearn: 307"


def assert_array_almost_equal(
    x,
    y,
    decimal: int = ...,
    err_msg: Literal[
        (
            "with solver = saga",
            "X != TP'",
            "with solver = sag",
            "rotation on Y failed",
            "nipals and svd implementations lead to different x",
            "Parameters: strategy = median, missing_values = na",
            "inverse_transform failed",
            "Wrong number of samples per class",
            "x weights are not orthogonal",
            "with solver = lbfgs",
            "y scores are not orthogonal",
            "Clusters should not be centered on hypercube verti",
            "y weights are not orthogonal",
            "with solver = newton-cg",
            "with solver = liblinear",
            "Parameters: strategy = mean, missing_values = nan,",
            "Y != UQ'",
            "x scores are not orthogonal",
            "rotation on X failed",
            "Clusters are not centered on hypercube vertices",
            "nipals and svd implementations lead to different y",
        )
    ] = ...,
):
    "usage.skimage: 107, usage.sklearn: 641"


def assert_warns(warning_class: type, *args: Literal[("v", "t")]):
    "usage.skimage: 5"


def assert_(val: Union[(numpy.bool_, bool)] = ...):
    "usage.skimage: 91"


def assert_array_less(
    x: Union[(int, numpy.float64, numpy.ndarray, float)],
    y: Union[(int, numpy.float64, numpy.ndarray, float)],
):
    "usage.skimage: 20, usage.sklearn: 9"


def assert_array_almost_equal_nulp(
    x: Union[(numpy.ma.core.MaskedArray, numpy.ndarray)],
    y: Union[(numpy.ma.core.MaskedArray, numpy.ndarray, numpy.float64)],
):
    "usage.skimage: 4"


def assert_no_warnings():
    "usage.skimage: 1"


def assert_approx_equal(actual: numpy.float64, desired: numpy.float64 = ...):
    "usage.sklearn: 2"
