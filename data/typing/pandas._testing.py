from typing import *


def assert_extension_array_equal(
    left: pandas.core.arrays.categorical.Categorical,
    right: pandas.core.arrays.categorical.Categorical,
):
    """
    usage.dask: 1
    """
    ...


@overload
def assert_frame_equal(
    left: pandas.core.frame.DataFrame, right: pandas.core.frame.DataFrame
):
    """
    usage.dask: 20
    """
    ...


@overload
def assert_frame_equal(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    check_dtype: bool,
):
    """
    usage.dask: 1
    """
    ...


@overload
def assert_frame_equal(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    check_categorical: bool,
):
    """
    usage.dask: 1
    """
    ...


@overload
def assert_frame_equal(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    check_less_precise: bool,
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
    usage.dask: 36
    usage.xarray: 2
    """
    ...


@overload
def assert_index_equal(
    left: pandas.core.indexes.multi.MultiIndex,
    right: pandas.core.indexes.multi.MultiIndex,
):
    """
    usage.dask: 3
    usage.xarray: 3
    """
    ...


@overload
def assert_index_equal(
    left: pandas.core.indexes.range.RangeIndex,
    right: pandas.core.indexes.numeric.Int64Index,
):
    """
    usage.dask: 2
    """
    ...


@overload
def assert_index_equal(
    left: pandas.core.indexes.numeric.Int64Index,
    right: pandas.core.indexes.numeric.Int64Index,
):
    """
    usage.dask: 7
    """
    ...


@overload
def assert_index_equal(
    left: pandas.core.indexes.range.RangeIndex,
    right: pandas.core.indexes.range.RangeIndex,
):
    """
    usage.dask: 3
    """
    ...


@overload
def assert_index_equal(
    left: pandas.core.indexes.numeric.Int64Index,
    right: pandas.core.indexes.range.RangeIndex,
):
    """
    usage.dask: 2
    """
    ...


@overload
def assert_index_equal(
    left: pandas.core.indexes.category.CategoricalIndex,
    right: pandas.core.indexes.category.CategoricalIndex,
):
    """
    usage.dask: 7
    """
    ...


@overload
def assert_index_equal(
    left: pandas.core.indexes.datetimes.DatetimeIndex,
    right: pandas.core.indexes.datetimes.DatetimeIndex,
):
    """
    usage.dask: 1
    """
    ...


@overload
def assert_index_equal(
    left: pandas.core.indexes.numeric.Float64Index,
    right: pandas.core.indexes.numeric.Float64Index,
):
    """
    usage.dask: 5
    """
    ...


@overload
def assert_index_equal(
    left: pandas.core.indexes.period.PeriodIndex,
    right: pandas.core.indexes.period.PeriodIndex,
):
    """
    usage.dask: 1
    """
    ...


@overload
def assert_index_equal(
    left: pandas.core.indexes.timedeltas.TimedeltaIndex,
    right: pandas.core.indexes.timedeltas.TimedeltaIndex,
):
    """
    usage.dask: 1
    """
    ...


def assert_index_equal(left: object, right: object):
    """
    usage.dask: 68
    usage.xarray: 5
    """
    ...


@overload
def assert_series_equal(
    left: pandas.core.series.Series, right: pandas.core.series.Series, check_names: bool
):
    """
    usage.dask: 1
    """
    ...


@overload
def assert_series_equal(
    left: pandas.core.series.Series, right: pandas.core.series.Series
):
    """
    usage.dask: 17
    """
    ...


@overload
def assert_series_equal(
    left: pandas.core.series.Series,
    right: pandas.core.series.Series,
    check_dtype: bool,
    check_names: bool,
):
    """
    usage.dask: 1
    """
    ...


def assert_series_equal(
    left: pandas.core.series.Series,
    right: pandas.core.series.Series,
    check_dtype: bool = ...,
    check_names: bool = ...,
):
    """
    usage.dask: 19
    """
    ...
