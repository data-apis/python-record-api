from typing import *


def assert_extension_array_equal(
    left: pandas.core.arrays.categorical.Categorical,
    right: pandas.core.arrays.categorical.Categorical,
):
    """
    usage.dask: 1
    """
    ...


def assert_frame_equal(
    left: pandas.core.frame.DataFrame, right: pandas.core.frame.DataFrame
):
    """
    usage.xarray: 9
    usage.dask: 24
    """
    ...


def assert_index_equal(left: object, right: object):
    """
    usage.xarray: 5
    usage.dask: 68
    """
    ...


def assert_series_equal(
    left: pandas.core.series.Series,
    right: pandas.core.series.Series,
    check_dtype: bool = ...,
    check_less_precise: bool = ...,
    check_names: bool = ...,
):
    """
    usage.dask: 20
    """
    ...
