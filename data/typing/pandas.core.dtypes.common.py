from typing import *


def is_bool_dtype(arr_or_dtype: pandas.core.series.Series):
    """
    usage.dask: 1
    """
    ...


def is_categorical_dtype(arr_or_dtype: object):
    """
    usage.dask: 115
    """
    ...


def is_datetime64_any_dtype(
    arr_or_dtype: Union[pandas.core.series.Series, numpy.dtype]
):
    """
    usage.dask: 4
    """
    ...


def is_datetime64_ns_dtype(
    arr_or_dtype: Union[numpy.dtype, pandas.core.dtypes.dtypes.CategoricalDtype]
):
    """
    usage.dask: 2
    """
    ...


def is_datetime64tz_dtype(arr_or_dtype: object):
    """
    usage.dask: 15
    """
    ...


def is_dtype_equal(source: numpy.dtype, target: numpy.dtype):
    """
    usage.dask: 3
    """
    ...


def is_float_dtype(arr_or_dtype: numpy.dtype):
    """
    usage.dask: 5
    """
    ...


def is_integer_dtype(arr_or_dtype: numpy.dtype):
    """
    usage.dask: 7
    """
    ...


def is_interval_dtype(
    arr_or_dtype: Union[
        pandas.tests.extension.decimal.array.DecimalDtype,
        pandas.core.arrays.string_.StringDtype,
        pandas.core.arrays.boolean.BooleanDtype,
        numpy.dtype,
    ]
):
    """
    usage.dask: 11
    """
    ...


def is_numeric_dtype(arr_or_dtype: pandas.core.series.Series):
    """
    usage.dask: 1
    """
    ...


def is_object_dtype(arr_or_dtype: numpy.dtype):
    """
    usage.dask: 2
    """
    ...


def is_period_dtype(
    arr_or_dtype: Union[
        pandas.tests.extension.decimal.array.DecimalDtype,
        pandas.core.arrays.string_.StringDtype,
        pandas.core.arrays.boolean.BooleanDtype,
        numpy.dtype,
    ]
):
    """
    usage.dask: 11
    """
    ...


def is_sparse(
    arr: Union[
        pandas.core.series.Series,
        numpy.dtype,
        pandas.core.arrays.boolean.BooleanDtype,
        pandas.core.arrays.string_.StringDtype,
        pandas.tests.extension.decimal.array.DecimalDtype,
    ]
):
    """
    usage.dask: 14
    """
    ...


def is_timedelta64_dtype(arr_or_dtype: pandas.core.series.Series):
    """
    usage.dask: 2
    """
    ...
