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
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    check_dtype: bool = ...,
    check_categorical: bool = ...,
    check_less_precise: bool = ...,
):
    """
    usage.dask: 23
    """
    ...


@overload
def assert_index_equal(
    left: pandas.core.indexes.base.Index, right: pandas.core.indexes.base.Index
):
    """
    usage.xarray: 2
    """
    ...


@overload
def assert_index_equal(
    left: pandas.core.indexes.multi.MultiIndex,
    right: pandas.core.indexes.multi.MultiIndex,
):
    """
    usage.xarray: 3
    """
    ...


@overload
def assert_index_equal(left: object, right: object):
    """
    usage.dask: 68
    """
    ...


def assert_index_equal(left: object, right: object):
    """
    usage.dask: 68
    usage.xarray: 5
    """
    ...


def assert_series_equal(
    left: pandas.core.series.Series,
    right: pandas.core.series.Series,
    check_less_precise: bool = ...,
    check_dtype: bool = ...,
    check_names: bool = ...,
):
    """
    usage.dask: 20
    """
    ...
