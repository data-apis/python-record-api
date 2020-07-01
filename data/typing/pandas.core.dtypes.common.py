from typing import *


def is_datetime64tz_dtype(arr_or_dtype: object):
    "\n    usage.dask: 15\n    "
    ...


def is_categorical_dtype(arr_or_dtype: object):
    "\n    usage.dask: 115\n    "
    ...


def is_period_dtype(
    arr_or_dtype: Union[
        pandas.tests.extension.decimal.array.DecimalDtype,
        pandas.core.arrays.string_.StringDtype,
        pandas.core.arrays.boolean.BooleanDtype,
        numpy.dtype,
    ]
):
    "\n    usage.dask: 11\n    "
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
    "\n    usage.dask: 14\n    "
    ...


def is_interval_dtype(
    arr_or_dtype: Union[
        pandas.tests.extension.decimal.array.DecimalDtype,
        pandas.core.arrays.string_.StringDtype,
        pandas.core.arrays.boolean.BooleanDtype,
        numpy.dtype,
    ]
):
    "\n    usage.dask: 11\n    "
    ...


def is_float_dtype(arr_or_dtype: numpy.dtype):
    "\n    usage.dask: 5\n    "
    ...


def is_object_dtype(arr_or_dtype: numpy.dtype):
    "\n    usage.dask: 2\n    "
    ...


def is_datetime64_any_dtype(
    arr_or_dtype: Union[pandas.core.series.Series, numpy.dtype]
):
    "\n    usage.dask: 4\n    "
    ...


def is_integer_dtype(arr_or_dtype: numpy.dtype):
    "\n    usage.dask: 7\n    "
    ...


def is_timedelta64_dtype(arr_or_dtype: pandas.core.series.Series):
    "\n    usage.dask: 2\n    "
    ...


def is_datetime64_ns_dtype(
    arr_or_dtype: Union[numpy.dtype, pandas.core.dtypes.dtypes.CategoricalDtype]
):
    "\n    usage.dask: 2\n    "
    ...


def is_bool_dtype(arr_or_dtype: pandas.core.series.Series):
    "\n    usage.dask: 1\n    "
    ...


def is_numeric_dtype(arr_or_dtype: pandas.core.series.Series):
    "\n    usage.dask: 1\n    "
    ...


def is_dtype_equal(source: numpy.dtype, target: numpy.dtype):
    "\n    usage.dask: 3\n    "
    ...
