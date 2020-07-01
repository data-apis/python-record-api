from typing import *

# usage.skimage: 5
# usage.sklearn: 4
# usage.dask: 2
array: object

# usage.skimage: 4
masked: object

# usage.xarray: 6
MaskedArray: object

# usage.xarray: 1
# usage.dask: 1
concatenate: object

# usage.sklearn: 1
# usage.dask: 21
masked_array: object

# usage.sklearn: 1
mean: object

# usage.sklearn: 4
# usage.dask: 1
average: object

# usage.sklearn: 1
median: object

# usage.dask: 1
masked_where: object

# usage.dask: 1
masked_equal: object

# usage.dask: 1
filled: object

# usage.dask: 1
masked_inside: object

# usage.dask: 1
masked_outside: object

# usage.dask: 1
masked_values: object

# usage.dask: 1
masked_invalid: object

# usage.dask: 2
fix_invalid: object

# usage.dask: 1
getmaskarray: object

# usage.dask: 1
getdata: object

# usage.dask: 1
nomask: object

# usage.dask: 1
MaskError: object

# usage.dask: 1
core: object

# usage.dask: 1
set_fill_value: object


def zeros(*args: Literal["v", "t"]):
    "\n    usage.skimage: 5\n    "
    ...


def ones(*args: Literal["v", "t"]):
    "\n    usage.xarray: 1\n    "
    ...
