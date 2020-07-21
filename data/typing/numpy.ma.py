from typing import *

# usage.xarray: 6
# usage.pandas: 2
# usage.sklearn: 2
MaskedArray: object

# usage.skimage: 5
# usage.xarray: 1
# usage.pandas: 1
# usage.sklearn: 4
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
    usage.skimage: 5
    usage.pandas: 1
    """
    ...
