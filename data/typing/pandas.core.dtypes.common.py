from typing import *


def is_bool_dtype(arr_or_dtype: pandas.core.series.Series):
    """
    usage.dask: 1
    """
    ...


@overload
def is_categorical_dtype(arr_or_dtype: numpy.dtype):
    """
    usage.dask: 47
    """
    ...


@overload
def is_categorical_dtype(arr_or_dtype: pandas.core.dtypes.dtypes.CategoricalDtype):
    """
    usage.dask: 17
    """
    ...


@overload
def is_categorical_dtype(arr_or_dtype: pandas.core.arrays.string_.StringDtype):
    """
    usage.dask: 2
    """
    ...


@overload
def is_categorical_dtype(arr_or_dtype: pandas.core.arrays.boolean.BooleanDtype):
    """
    usage.dask: 2
    """
    ...


@overload
def is_categorical_dtype(arr_or_dtype: pandas.core.arrays.integer.Int64Dtype):
    """
    usage.dask: 1
    """
    ...


@overload
def is_categorical_dtype(arr_or_dtype: Literal["f8"]):
    """
    usage.dask: 2
    """
    ...


@overload
def is_categorical_dtype(arr_or_dtype: pandas.core.arrays.integer.Int32Dtype):
    """
    usage.dask: 1
    """
    ...


@overload
def is_categorical_dtype(arr_or_dtype: pandas.core.series.Series):
    """
    usage.dask: 7
    """
    ...


@overload
def is_categorical_dtype(arr_or_dtype: dask.dataframe.core.Series):
    """
    usage.dask: 5
    """
    ...


@overload
def is_categorical_dtype(arr_or_dtype: pandas.core.indexes.category.CategoricalIndex):
    """
    usage.dask: 3
    """
    ...


@overload
def is_categorical_dtype(arr_or_dtype: pandas.core.indexes.base.Index):
    """
    usage.dask: 3
    """
    ...


@overload
def is_categorical_dtype(arr_or_dtype: pandas.core.indexes.numeric.Float64Index):
    """
    usage.dask: 2
    """
    ...


@overload
def is_categorical_dtype(arr_or_dtype: pandas.core.arrays.categorical.Categorical):
    """
    usage.dask: 1
    """
    ...


@overload
def is_categorical_dtype(arr_or_dtype: Literal["category"]):
    """
    usage.dask: 2
    """
    ...


@overload
def is_categorical_dtype(arr_or_dtype: pandas.core.indexes.range.RangeIndex):
    """
    usage.dask: 3
    """
    ...


@overload
def is_categorical_dtype(arr_or_dtype: pandas.core.dtypes.dtypes.DatetimeTZDtype):
    """
    usage.dask: 2
    """
    ...


@overload
def is_categorical_dtype(arr_or_dtype: Literal["i8"]):
    """
    usage.dask: 1
    """
    ...


@overload
def is_categorical_dtype(arr_or_dtype: pandas.core.indexes.numeric.Int64Index):
    """
    usage.dask: 2
    """
    ...


@overload
def is_categorical_dtype(arr_or_dtype: Literal["float32"]):
    """
    usage.dask: 1
    """
    ...


@overload
def is_categorical_dtype(arr_or_dtype: Type[float]):
    """
    usage.dask: 2
    """
    ...


@overload
def is_categorical_dtype(arr_or_dtype: Dict[Literal["x"], Literal["category"]]):
    """
    usage.dask: 1
    """
    ...


@overload
def is_categorical_dtype(
    arr_or_dtype: Dict[
        Literal["other", "z", "y", "x"],
        Union[Literal["f8", "category"], pandas.core.dtypes.dtypes.CategoricalDtype],
    ]
):
    """
    usage.dask: 1
    """
    ...


@overload
def is_categorical_dtype(arr_or_dtype: Type[int]):
    """
    usage.dask: 1
    """
    ...


@overload
def is_categorical_dtype(
    arr_or_dtype: pandas.tests.extension.decimal.array.DecimalDtype,
):
    """
    usage.dask: 2
    """
    ...


@overload
def is_categorical_dtype(arr_or_dtype: numpy.ndarray):
    """
    usage.dask: 1
    """
    ...


@overload
def is_categorical_dtype(arr_or_dtype: Literal["-"]):
    """
    usage.dask: 1
    """
    ...


def is_categorical_dtype(arr_or_dtype: object):
    """
    usage.dask: 113
    """
    ...


@overload
def is_datetime64_any_dtype(arr_or_dtype: numpy.dtype):
    """
    usage.dask: 3
    """
    ...


@overload
def is_datetime64_any_dtype(arr_or_dtype: pandas.core.series.Series):
    """
    usage.dask: 1
    """
    ...


def is_datetime64_any_dtype(
    arr_or_dtype: Union[pandas.core.series.Series, numpy.dtype]
):
    """
    usage.dask: 4
    """
    ...


@overload
def is_datetime64_ns_dtype(arr_or_dtype: pandas.core.dtypes.dtypes.CategoricalDtype):
    """
    usage.dask: 1
    """
    ...


@overload
def is_datetime64_ns_dtype(arr_or_dtype: numpy.dtype):
    """
    usage.dask: 1
    """
    ...


def is_datetime64_ns_dtype(
    arr_or_dtype: Union[numpy.dtype, pandas.core.dtypes.dtypes.CategoricalDtype]
):
    """
    usage.dask: 2
    """
    ...


@overload
def is_datetime64tz_dtype(arr_or_dtype: numpy.dtype):
    """
    usage.dask: 9
    """
    ...


@overload
def is_datetime64tz_dtype(arr_or_dtype: pandas.core.arrays.string_.StringDtype):
    """
    usage.dask: 1
    """
    ...


@overload
def is_datetime64tz_dtype(arr_or_dtype: pandas.core.dtypes.dtypes.CategoricalDtype):
    """
    usage.dask: 1
    """
    ...


@overload
def is_datetime64tz_dtype(arr_or_dtype: pandas.core.arrays.integer.Int32Dtype):
    """
    usage.dask: 1
    """
    ...


@overload
def is_datetime64tz_dtype(arr_or_dtype: pandas.core.arrays.boolean.BooleanDtype):
    """
    usage.dask: 1
    """
    ...


@overload
def is_datetime64tz_dtype(
    arr_or_dtype: pandas.tests.extension.decimal.array.DecimalDtype,
):
    """
    usage.dask: 1
    """
    ...


@overload
def is_datetime64tz_dtype(arr_or_dtype: pandas.core.dtypes.dtypes.DatetimeTZDtype):
    """
    usage.dask: 1
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


@overload
def is_interval_dtype(arr_or_dtype: numpy.dtype):
    """
    usage.dask: 8
    """
    ...


@overload
def is_interval_dtype(arr_or_dtype: pandas.core.arrays.string_.StringDtype):
    """
    usage.dask: 1
    """
    ...


@overload
def is_interval_dtype(arr_or_dtype: pandas.core.arrays.boolean.BooleanDtype):
    """
    usage.dask: 1
    """
    ...


@overload
def is_interval_dtype(arr_or_dtype: pandas.tests.extension.decimal.array.DecimalDtype):
    """
    usage.dask: 1
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


@overload
def is_period_dtype(arr_or_dtype: numpy.dtype):
    """
    usage.dask: 8
    """
    ...


@overload
def is_period_dtype(arr_or_dtype: pandas.core.arrays.string_.StringDtype):
    """
    usage.dask: 1
    """
    ...


@overload
def is_period_dtype(arr_or_dtype: pandas.core.arrays.boolean.BooleanDtype):
    """
    usage.dask: 1
    """
    ...


@overload
def is_period_dtype(arr_or_dtype: pandas.tests.extension.decimal.array.DecimalDtype):
    """
    usage.dask: 1
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


@overload
def is_sparse(arr: numpy.dtype):
    """
    usage.dask: 8
    """
    ...


@overload
def is_sparse(arr: pandas.core.arrays.string_.StringDtype):
    """
    usage.dask: 1
    """
    ...


@overload
def is_sparse(arr: pandas.core.arrays.boolean.BooleanDtype):
    """
    usage.dask: 1
    """
    ...


@overload
def is_sparse(arr: pandas.tests.extension.decimal.array.DecimalDtype):
    """
    usage.dask: 1
    """
    ...


@overload
def is_sparse(arr: pandas.core.series.Series):
    """
    usage.dask: 3
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
