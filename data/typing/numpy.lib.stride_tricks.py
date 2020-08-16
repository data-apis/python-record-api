from typing import *


def as_strided(
    x: object,
    shape: Tuple[Union[numpy.int64, int], ...],
    strides: Tuple[Union[numpy.int64, int], ...],
):
    """
    usage.matplotlib: 5
    usage.pandas: 3
    usage.skimage: 11
    usage.sklearn: 6
    usage.xarray: 10
    """
    ...


class DummyArray:

    # usage.matplotlib: 2
    base: object
