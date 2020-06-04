from typing import *


def assert_almost_equal(
    actual,
    desired,
    decimal: int = ...,
    err_msg: Literal[
        (
            "Point is not on expected unit circle",
            "Point is not on expected circle",
            "Unexpected std",
        )
    ] = ...,
):
    "usage.skimage: 340, usage.sklearn: 244"


def assert_equal(actual, desired=...):
    "usage.skimage: 664, usage.xarray: 21"


def assert_array_equal(x, y=...):
    "usage.skimage: 495, usage.xarray: 307, usage.sklearn: 562"


def assert_allclose(
    actual,
    desired,
    rtol: Union[(float, int)] = ...,
    atol: Union[(float, int)] = ...,
    err_msg: Literal[
        (
            "",
            "StackingClassifier",
            "Idempotency check failed for method transform",
            "VotingRegressor",
            "StackingRegressor",
            "For VotingRegressor sample_weight=None is not equi",
            "predict_proba of StackingClassifier is not invaria",
            "For StackingClassifier sample_weight=None is not e",
            "Idempotency check failed for method predict",
            "For VotingClassifier sample_weight=None is not equ",
            "transform of StackingClassifier is not invariant w",
            "predict of VotingClassifier is not invariant when ",
            "predict of StackingClassifier is not invariant whe",
            "predict of StackingRegressor is not invariant when",
            "predict of VotingRegressor is not invariant when a",
            "transform of VotingClassifier is not invariant whe",
            "consecutive fit_transform outcomes not consistent ",
            "transform of VotingRegressor is not invariant when",
            "Idempotency check failed for method predict_proba",
            "transform of StackingRegressor is not invariant wh",
            "Idempotency check failed for method decision_funct",
            "For StackingRegressor sample_weight=None is not eq",
            "fit_transform and transform outcomes not consisten",
            "decision_function of StackingClassifier is not inv",
            "VotingClassifier",
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
            "with solver = lbfgs",
            "rotation on Y failed",
            "inverse_transform failed",
            "x weights are not orthogonal",
            "nipals and svd implementations lead to different y",
            "Parameters: strategy = median, missing_values = na",
            "Parameters: strategy = mean, missing_values = nan,",
            "with solver = newton-cg",
            "Y != UQ'",
            "Clusters are not centered on hypercube vertices",
            "Wrong number of samples per class",
            "with solver = sag",
            "y scores are not orthogonal",
            "y weights are not orthogonal",
            "Clusters should not be centered on hypercube verti",
            "rotation on X failed",
            "with solver = liblinear",
            "X != TP'",
            "with solver = saga",
            "nipals and svd implementations lead to different x",
        )
    ] = ...,
):
    "usage.skimage: 107, usage.sklearn: 641"


def assert_warns(warning_class: type, *args: Literal[("v", "t")]):
    "usage.skimage: 5"


def assert_(val: Union[(bool, numpy.bool_)] = ...):
    "usage.skimage: 91"


def assert_array_less(
    x: Union[(float, numpy.ndarray, int, numpy.float64)],
    y: Union[(float, numpy.ndarray, int, numpy.float64)],
):
    "usage.skimage: 20, usage.sklearn: 9"


def assert_array_almost_equal_nulp(
    x: Union[(numpy.ma.core.MaskedArray, numpy.ndarray)],
    y: Union[(numpy.float64, numpy.ma.core.MaskedArray, numpy.ndarray)],
):
    "usage.skimage: 4"


def assert_no_warnings():
    "usage.skimage: 1"


def assert_approx_equal(actual: numpy.float64, desired: numpy.float64 = ...):
    "usage.sklearn: 2"
