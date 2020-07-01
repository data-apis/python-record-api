from typing import *


def assert_frame_equal(
    left: pandas.core.frame.DataFrame, right: pandas.core.frame.DataFrame
):
    "\n    usage.xarray: 9\n    usage.dask: 24\n    "
    ...


def assert_index_equal(left: object, right: object):
    "\n    usage.xarray: 5\n    usage.dask: 68\n    "
    ...


def assert_series_equal(
    left: pandas.core.series.Series,
    right: pandas.core.series.Series,
    check_less_precise: bool = ...,
    check_dtype: bool = ...,
    check_names: bool = ...,
):
    "\n    usage.dask: 20\n    "
    ...


def assert_extension_array_equal(
    left: pandas.core.arrays.categorical.Categorical,
    right: pandas.core.arrays.categorical.Categorical,
):
    "\n    usage.dask: 1\n    "
    ...
