def assert_almost_equal(
    actual,
    desired,
    decimal: int = ...,
    err_msg: Literal[
        (
            "Point is not on expected circle",
            "Unexpected std",
            "Point is not on expected unit circle",
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
    rtol: Union[(int, float)] = ...,
    atol: Union[(int, float)] = ...,
    err_msg: Literal[
        (
            "",
            "transform of StackingClassifier is not invariant w",
            "predict of VotingRegressor is not invariant when a",
            "StackingClassifier",
            "StackingRegressor",
            "predict_proba of StackingClassifier is not invaria",
            "predict of VotingClassifier is not invariant when ",
            "For VotingClassifier sample_weight=None is not equ",
            "transform of StackingRegressor is not invariant wh",
            "transform of VotingClassifier is not invariant whe",
            "Idempotency check failed for method predict_proba",
            "consecutive fit_transform outcomes not consistent ",
            "Idempotency check failed for method predict",
            "Idempotency check failed for method decision_funct",
            "Idempotency check failed for method transform",
            "For VotingRegressor sample_weight=None is not equi",
            "predict of StackingRegressor is not invariant when",
            "decision_function of StackingClassifier is not inv",
            "transform of VotingRegressor is not invariant when",
            "VotingClassifier",
            "For StackingClassifier sample_weight=None is not e",
            "For StackingRegressor sample_weight=None is not eq",
            "predict of StackingClassifier is not invariant whe",
            "fit_transform and transform outcomes not consisten",
            "VotingRegressor",
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
            "Clusters are not centered on hypercube vertices",
            "Wrong number of samples per class",
            "X != TP'",
            "with solver = saga",
            "with solver = lbfgs",
            "rotation on Y failed",
            "with solver = newton-cg",
            "with solver = liblinear",
            "nipals and svd implementations lead to different x",
            "y weights are not orthogonal",
            "Y != UQ'",
            "x weights are not orthogonal",
            "rotation on X failed",
            "Parameters: strategy = median, missing_values = na",
            "x scores are not orthogonal",
            "Clusters should not be centered on hypercube verti",
            "with solver = sag",
            "nipals and svd implementations lead to different y",
            "inverse_transform failed",
            "Parameters: strategy = mean, missing_values = nan,",
            "y scores are not orthogonal",
        )
    ] = ...,
):
    "usage.skimage: 107, usage.sklearn: 641"


def assert_warns(warning_class: list, *args: Literal[("t", "v")]):
    "usage.skimage: 5"


def assert_(val: Union[(bool, numpy.bool_)] = ...):
    "usage.skimage: 91"


def assert_array_less(
    x: Union[(numpy.ndarray, numpy.float64, int, float)],
    y: Union[(numpy.ndarray, float, int, numpy.float64)],
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
