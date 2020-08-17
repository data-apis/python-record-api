from typing import *


@overload
def assert_(val: Union[bool, numpy.bool_], msg: str = ...):
    """
    usage.skimage: 78
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
def assert_allclose(
    actual: Union[numpy.ndarray, numpy.int64, float, numpy.float64],
    desired: object,
    rtol: float = ...,
    atol: Union[float, int] = ...,
):
    """
    usage.skimage: 158
    """
    ...


@overload
def assert_allclose(actual: object, desired: object):
    """
    usage.xarray: 38
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
    actual: Union[
        Tuple[Union[numpy.float64, int, numpy.uint8], ...],
        numpy.ndarray,
        numpy.ma.core.MaskedArray,
        numpy.float64,
        List[Union[int, float, numpy.float64]],
    ],
    desired: object,
    rtol: float = ...,
    atol: float = ...,
    err_msg: numpy.ndarray = ...,
):
    """
    usage.matplotlib: 184
    """
    ...


@overload
def assert_allclose(
    actual: object,
    desired: object,
    rtol: Union[float, int] = ...,
    atol: Union[float, int] = ...,
    err_msg: str = ...,
):
    """
    usage.sklearn: 760
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
def assert_almost_equal(actual: object, desired: object, decimal: int = ...):
    """
    usage.skimage: 333
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
def assert_almost_equal(
    actual: Union[
        List[Union[numpy.float64, float]],
        Tuple[float, float],
        numpy.ndarray,
        numpy.float64,
        float,
    ],
    desired: Union[
        numpy.ndarray,
        numpy.float64,
        float,
        Tuple[Union[int, float], Union[int, float]],
        List[float],
    ],
    decimal: int = ...,
):
    """
    usage.matplotlib: 50
    """
    ...


@overload
def assert_almost_equal(
    actual: Union[numpy.ndarray, numpy.int64, numpy.float64, int, float],
    desired: object,
    decimal: int = ...,
    err_msg: str = ...,
):
    """
    usage.sklearn: 965
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
def assert_approx_equal(
    actual: numpy.float64, desired: numpy.float64, significant: int = ...
):
    """
    usage.sklearn: 2
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
def assert_array_almost_equal(
    x: Union[numpy.ndarray, int, Tuple[Union[int, numpy.float64], ...]],
    y: Union[
        int,
        numpy.ndarray,
        List[Union[int, float, List[Tuple[int, int, int]], Tuple[int, int]]],
        Tuple[Union[int, float], ...],
    ],
):
    """
    usage.skimage: 69
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
    x: Union[
        Tuple[Union[numpy.float32, numpy.float64], ...],
        List[Union[List[float], float, numpy.float64]],
        numpy.ndarray,
        numpy.ma.core.MaskedArray,
        numpy.float64,
    ],
    y: object,
    decimal: int = ...,
):
    """
    usage.matplotlib: 86
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
    x: object, y: object, decimal: Union[int, bool] = ..., err_msg: str = ...
):
    """
    usage.sklearn: 1569
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
def assert_array_almost_equal_nulp(
    x: Union[numpy.ma.core.MaskedArray, numpy.ndarray],
    y: Union[numpy.float64, numpy.ndarray, numpy.ma.core.MaskedArray],
):
    """
    usage.skimage: 4
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


@overload
def assert_array_almost_equal_nulp(x: numpy.ndarray, y: numpy.ndarray):
    """
    usage.matplotlib: 1
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
def assert_array_equal(
    x: Union[
        numpy.ndarray,
        int,
        skimage.util._map_array.ArrayMap,
        Tuple[Union[numpy.float64, numpy.uint8, int, float], ...],
        List[Union[int, Tuple[int, int]]],
    ],
    y: Union[
        List[
            Union[
                List[Union[int, float, List[Tuple[int, int]]]],
                float,
                int,
                Tuple[int, int],
            ]
        ],
        Tuple[Union[float, bool, int], ...],
        int,
        numpy.ndarray,
    ],
):
    """
    usage.skimage: 430
    """
    ...


@overload
def assert_array_equal(x: object, y: object):
    """
    usage.xarray: 400
    """
    ...


@overload
def assert_array_equal(x: object, y: object, err_msg: str = ...):
    """
    usage.scipy: 1623
    usage.sklearn: 1475
    """
    ...


@overload
def assert_array_equal(
    x: Union[
        numpy.ndarray,
        int,
        numpy.ma.core.MaskedArray,
        Tuple[numpy.float64, ...],
        List[
            Union[
                List[numpy.ndarray],
                int,
                float,
                numpy.ndarray,
                Literal[
                    "2000-10-31T11:50:23",
                    "2054-06-20T14:31:45",
                    "1983-07-09T17:17:34",
                    "1976-03-05T00:00:01",
                    "2014-01-11T00:00:00",
                ],
            ]
        ],
    ],
    y: object,
):
    """
    usage.matplotlib: 186
    """
    ...


@overload
def assert_array_equal(
    x: Union[numpy.ndarray, dask.array.core.Array, dask.dataframe.core.Index],
    y: Union[numpy.ndarray, List[int]],
):
    """
    usage.dask: 36
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
def assert_array_less(
    x: Union[numpy.float64, numpy.ndarray],
    y: Union[float, numpy.float64, numpy.ndarray],
):
    """
    usage.skimage: 20
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
def assert_array_less(
    x: Union[numpy.float64, int, float, numpy.ndarray],
    y: Union[int, numpy.ndarray, float, numpy.float64],
    err_msg: str = ...,
):
    """
    usage.sklearn: 18
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
def assert_equal(actual: object, desired: object, err_msg: str = ...):
    """
    usage.skimage: 630
    """
    ...


@overload
def assert_equal(actual: object, desired: object):
    """
    usage.xarray: 40
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
def assert_equal(
    actual: Union[
        List[Union[numpy.ndarray, numpy.float64, float]], numpy.ndarray, float
    ],
    desired: Union[
        numpy.ndarray, numpy.float64, List[Union[bool, numpy.float64, float]]
    ],
):
    """
    usage.matplotlib: 12
    """
    ...


@overload
def assert_equal(
    actual: Union[
        numpy.ndarray,
        numpy.bool_,
        Dict[
            Tuple[Union[int, Literal["y"]], ...],
            Tuple[
                Callable,
                Tuple[Union[Literal["x"], int, numpy.int64], ...],
                Tuple[Union[slice[None, None, None], numpy.ndarray], ...],
            ],
        ],
        List[
            Tuple[
                Tuple[Union[Literal["y"], int], ...],
                Tuple[
                    Callable,
                    Tuple[Union[Literal["x"], numpy.int64, int], ...],
                    Tuple[Union[numpy.ndarray, slice[None, None, None]], ...],
                ],
            ]
        ],
        Tuple[
            Union[
                Tuple[Union[None, Literal["e", "d", "y"]], ...],
                List[Tuple[Union[None, str], ...]],
                float,
                int,
            ],
            ...,
        ],
    ],
    desired: Union[
        numpy.ndarray,
        numpy.bool_,
        Dict[
            Tuple[Union[int, Literal["y"]], ...],
            Tuple[
                Callable,
                Tuple[Union[Literal["x"], int, numpy.int64], ...],
                Tuple[Union[slice[None, None, None], List[int], numpy.ndarray], ...],
            ],
        ],
        List[
            Union[
                int,
                Tuple[
                    Tuple[Union[Literal["y"], int], ...],
                    Tuple[
                        Callable,
                        Tuple[Union[Literal["x"], int], ...],
                        Tuple[Union[numpy.ndarray, slice[None, None, None]], ...],
                    ],
                ],
            ]
        ],
        Tuple[
            Union[
                Tuple[Union[None, Literal["e", "d", "y"]], ...],
                List[Tuple[Union[None, str], ...]],
                float,
                int,
            ],
            ...,
        ],
    ],
):
    """
    usage.dask: 26
    """
    ...


@overload
def assert_equal(
    actual: Union[
        List[Union[float, Tuple[numpy.ndarray, numpy.ndarray]]],
        numpy.ndarray,
        Dict[
            str,
            Union[
                List[
                    Dict[
                        Literal["kernel", "gamma", "C", "degree"],
                        Union[int, float, numpy.float64, Literal["rbf", "poly"]],
                    ]
                ],
                numpy.ma.core.MaskedArray,
                numpy.ndarray,
            ],
        ],
    ],
    desired: Union[
        List[Union[Tuple[numpy.ndarray, numpy.ndarray], float]],
        Dict[
            str,
            Union[
                List[
                    Dict[
                        Literal["kernel", "gamma", "C", "degree"],
                        Union[int, float, numpy.float64, Literal["rbf", "poly"]],
                    ]
                ],
                numpy.ma.core.MaskedArray,
                numpy.ndarray,
            ],
        ],
        numpy.ndarray,
    ],
):
    """
    usage.sklearn: 27
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
def assert_warns(warning_class: type, *args: Literal["v", "t"]):
    """
    usage.scipy: 39
    usage.skimage: 5
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
