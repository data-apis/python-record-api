from typing import *

# usage.pandas: 2
# usage.sklearn: 2
# usage.xarray: 6
MaskedArray: object

# usage.pandas: 1
# usage.skimage: 5
# usage.sklearn: 4
# usage.xarray: 1
array: object

# usage.sklearn: 4
average: object

# usage.xarray: 1
concatenate: object

# usage.skimage: 4
masked: object

# usage.pandas: 9
masked_all: object

# usage.pandas: 2
# usage.sklearn: 2
masked_array: object

# usage.sklearn: 1
mean: object

# usage.sklearn: 1
median: object


def ones(*args: Literal["v", "t"]):
    """
    usage.xarray: 1
    """
    ...


def zeros(*args: Literal["v", "t"]):
    """
    usage.pandas: 1
    usage.skimage: 5
    """
    ...
