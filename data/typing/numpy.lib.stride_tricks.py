from typing import *


def as_strided(
    x: numpy.ndarray,
    shape: Tuple[(Union[(int, numpy.int64)], ...)],
    strides: Tuple[(Union[(int, numpy.int64)], ...)] = ...,
):
    "usage.skimage: 11, usage.xarray: 8, usage.sklearn: 6"
