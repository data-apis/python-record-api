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
    err_msg: Literal[
        (
            "",
            "transform of VotingClassifier is not invariant whe",
            "Idempotency check failed for method decision_funct",
            "predict of VotingRegressor is not invariant when a",
            "consecutive fit_transform outcomes not consistent ",
            "predict of StackingRegressor is not invariant when",
            "predict_proba of StackingClassifier is not invaria",
            "VotingRegressor",
            "For StackingRegressor sample_weight=None is not eq",
            "Idempotency check failed for method predict",
            "Idempotency check failed for method predict_proba",
            "decision_function of StackingClassifier is not inv",
            "For VotingClassifier sample_weight=None is not equ",
            "StackingRegressor",
            "predict of StackingClassifier is not invariant whe",
            "fit_transform and transform outcomes not consisten",
            "transform of StackingClassifier is not invariant w",
            "Idempotency check failed for method transform",
            "predict of VotingClassifier is not invariant when ",
            "For VotingRegressor sample_weight=None is not equi",
            "transform of VotingRegressor is not invariant when",
            "For StackingClassifier sample_weight=None is not e",
            "VotingClassifier",
            "transform of StackingRegressor is not invariant wh",
            "StackingClassifier",
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
            "x scores are not orthogonal",
            "nipals and svd implementations lead to different x",
            "Parameters: strategy = mean, missing_values = nan,",
            "y weights are not orthogonal",
            "rotation on Y failed",
            "inverse_transform failed",
            "x weights are not orthogonal",
            "Clusters should not be centered on hypercube verti",
            "rotation on X failed",
            "with solver = newton-cg",
            "Wrong number of samples per class",
            "with solver = lbfgs",
            "with solver = liblinear",
            "X != TP'",
            "with solver = sag",
            "Y != UQ'",
            "nipals and svd implementations lead to different y",
            "y scores are not orthogonal",
            "with solver = saga",
            "Clusters are not centered on hypercube vertices",
            "Parameters: strategy = median, missing_values = na",
        )
    ] = ...,
):
    "usage.skimage: 107, usage.sklearn: 641"


def assert_warns(warning_class: type, *args: Literal[("t", "v")]):
    "usage.skimage: 5"


def assert_(val: Union[(bool, numpy.bool_)] = ...):
    "usage.skimage: 91"


def assert_array_less(
    x: Union[(float, int, numpy.ndarray, numpy.float64)],
    y: Union[(float, int, numpy.ndarray, numpy.float64)],
):
    "usage.skimage: 20, usage.sklearn: 9"


def assert_array_almost_equal_nulp(
    x: Union[(numpy.ndarray, numpy.ma.core.MaskedArray)],
    y: Union[(numpy.ndarray, numpy.ma.core.MaskedArray, numpy.float64)],
):
    "usage.skimage: 4"


def assert_no_warnings():
    "usage.skimage: 1"


def assert_approx_equal(actual: numpy.float64, desired: numpy.float64 = ...):
    "usage.sklearn: 2"
