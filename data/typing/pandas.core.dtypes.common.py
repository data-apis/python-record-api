from typing import *


@overload
def infer_dtype_from_object(dtype: Literal["byte"]):
    """
    usage.koalas: 1
    """
    ...


@overload
def infer_dtype_from_object(dtype: Literal["decimal"]):
    """
    usage.koalas: 1
    """
    ...


@overload
def infer_dtype_from_object(dtype: Literal["integer"]):
    """
    usage.koalas: 1
    """
    ...


@overload
def infer_dtype_from_object(dtype: Literal["float"]):
    """
    usage.koalas: 1
    """
    ...


@overload
def infer_dtype_from_object(dtype: Literal["long"]):
    """
    usage.koalas: 1
    """
    ...


@overload
def infer_dtype_from_object(dtype: Literal["double"]):
    """
    usage.koalas: 1
    """
    ...


@overload
def infer_dtype_from_object(dtype: Type[numpy.datetime64]):
    """
    usage.koalas: 1
    """
    ...


@overload
def infer_dtype_from_object(dtype: Literal["int64"]):
    """
    usage.koalas: 2
    """
    ...


@overload
def infer_dtype_from_object(dtype: Literal["float64"]):
    """
    usage.koalas: 3
    """
    ...


@overload
def infer_dtype_from_object(dtype: Literal["bool"]):
    """
    usage.koalas: 3
    """
    ...


@overload
def infer_dtype_from_object(dtype: Literal["object"]):
    """
    usage.koalas: 2
    """
    ...


@overload
def infer_dtype_from_object(dtype: Literal["int"]):
    """
    usage.koalas: 1
    """
    ...


@overload
def infer_dtype_from_object(dtype: Literal["string"]):
    """
    usage.koalas: 1
    """
    ...


def infer_dtype_from_object(dtype: Union[str, Type[numpy.datetime64]]):
    """
    usage.koalas: 19
    """
    ...


@overload
def is_bool_dtype(arr_or_dtype: numpy.dtype):
    """
    usage.koalas: 1
    """
    ...


@overload
def is_bool_dtype(arr_or_dtype: pandas.core.series.Series):
    """
    usage.dask: 1
    """
    ...


def is_bool_dtype(arr_or_dtype: Union[pandas.core.series.Series, numpy.dtype]):
    """
    usage.dask: 1
    usage.koalas: 1
    """
    ...


@overload
def is_categorical_dtype(arr_or_dtype: numpy.dtype):
    """
    usage.dask: 47
    usage.koalas: 1
    """
    ...


@overload
def is_categorical_dtype(arr_or_dtype: pandas.core.series.Series):
    """
    usage.dask: 7
    usage.seaborn: 1
    """
    ...


@overload
def is_categorical_dtype(arr_or_dtype: numpy.ndarray):
    """
    usage.dask: 1
    usage.seaborn: 3
    """
    ...


@overload
def is_categorical_dtype(arr_or_dtype: List[Literal["b", "a"]]):
    """
    usage.seaborn: 2
    """
    ...


@overload
def is_categorical_dtype(arr_or_dtype: List[Literal["m", "n"]]):
    """
    usage.seaborn: 1
    """
    ...


@overload
def is_categorical_dtype(arr_or_dtype: List[Literal["d", "c", "b", "a"]]):
    """
    usage.seaborn: 1
    """
    ...


@overload
def is_categorical_dtype(arr_or_dtype: List[Literal["y", "x"]]):
    """
    usage.seaborn: 1
    """
    ...


@overload
def is_categorical_dtype(arr_or_dtype: List[pandas._libs.tslibs.timestamps.Timestamp]):
    """
    usage.seaborn: 2
    """
    ...


@overload
def is_categorical_dtype(arr_or_dtype: List[float]):
    """
    usage.seaborn: 1
    """
    ...


@overload
def is_categorical_dtype(arr_or_dtype: List[Literal["3", "2", "1"]]):
    """
    usage.seaborn: 1
    """
    ...


@overload
def is_categorical_dtype(arr_or_dtype: List[Literal["d", "a", "b", "c"]]):
    """
    usage.seaborn: 1
    """
    ...


@overload
def is_categorical_dtype(arr_or_dtype: List[int]):
    """
    usage.seaborn: 1
    """
    ...


@overload
def is_categorical_dtype(arr_or_dtype: List[Union[Literal["d", "a", "b", "c"], float]]):
    """
    usage.seaborn: 1
    """
    ...


@overload
def is_categorical_dtype(arr_or_dtype: dask.dataframe.core.Series):
    """
    usage.dask: 5
    """
    ...


@overload
def is_categorical_dtype(arr_or_dtype: pandas.core.indexes.range.RangeIndex):
    """
    usage.dask: 3
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
def is_categorical_dtype(arr_or_dtype: Literal["-"]):
    """
    usage.dask: 1
    """
    ...


def is_categorical_dtype(arr_or_dtype: object):
    """
    usage.dask: 113
    usage.koalas: 1
    usage.seaborn: 16
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
def is_datetime64_dtype(arr_or_dtype: numpy.dtype):
    """
    usage.koalas: 17
    """
    ...


@overload
def is_datetime64_dtype(arr_or_dtype: pandas.core.series.Series):
    """
    usage.seaborn: 1
    """
    ...


@overload
def is_datetime64_dtype(arr_or_dtype: numpy.ndarray):
    """
    usage.seaborn: 3
    """
    ...


@overload
def is_datetime64_dtype(arr_or_dtype: List[Literal["b", "a"]]):
    """
    usage.seaborn: 2
    """
    ...


@overload
def is_datetime64_dtype(arr_or_dtype: List[Literal["m", "n"]]):
    """
    usage.seaborn: 1
    """
    ...


@overload
def is_datetime64_dtype(arr_or_dtype: List[Literal["d", "c", "b", "a"]]):
    """
    usage.seaborn: 1
    """
    ...


@overload
def is_datetime64_dtype(arr_or_dtype: List[Literal["y", "x"]]):
    """
    usage.seaborn: 1
    """
    ...


@overload
def is_datetime64_dtype(arr_or_dtype: List[pandas._libs.tslibs.timestamps.Timestamp]):
    """
    usage.seaborn: 2
    """
    ...


@overload
def is_datetime64_dtype(arr_or_dtype: List[float]):
    """
    usage.seaborn: 1
    """
    ...


@overload
def is_datetime64_dtype(arr_or_dtype: List[Literal["3", "2", "1"]]):
    """
    usage.seaborn: 1
    """
    ...


@overload
def is_datetime64_dtype(arr_or_dtype: List[Literal["d", "a", "b", "c"]]):
    """
    usage.seaborn: 1
    """
    ...


@overload
def is_datetime64_dtype(arr_or_dtype: List[int]):
    """
    usage.seaborn: 1
    """
    ...


@overload
def is_datetime64_dtype(arr_or_dtype: List[Union[Literal["d", "a", "b", "c"], float]]):
    """
    usage.seaborn: 1
    """
    ...


def is_datetime64_dtype(
    arr_or_dtype: Union[
        pandas.core.series.Series,
        numpy.ndarray,
        numpy.dtype,
        List[Union[pandas._libs.tslibs.timestamps.Timestamp, float, int, str]],
    ]
):
    """
    usage.koalas: 17
    usage.seaborn: 16
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
    usage.koalas: 15
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
    usage.koalas: 15
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
    usage.koalas: 1
    """
    ...


def is_integer_dtype(arr_or_dtype: numpy.dtype):
    """
    usage.dask: 7
    usage.koalas: 1
    """
    ...


@overload
def is_interval_dtype(arr_or_dtype: numpy.dtype):
    """
    usage.dask: 8
    usage.koalas: 1
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
        numpy.dtype,
        pandas.core.arrays.boolean.BooleanDtype,
        pandas.core.arrays.string_.StringDtype,
        pandas.tests.extension.decimal.array.DecimalDtype,
    ]
):
    """
    usage.dask: 11
    usage.koalas: 1
    """
    ...


@overload
def is_numeric_dtype(arr_or_dtype: numpy.dtype):
    """
    usage.koalas: 1
    """
    ...


@overload
def is_numeric_dtype(arr_or_dtype: pandas.core.series.Series):
    """
    usage.dask: 1
    usage.seaborn: 1
    """
    ...


@overload
def is_numeric_dtype(arr_or_dtype: numpy.ndarray):
    """
    usage.seaborn: 5
    """
    ...


@overload
def is_numeric_dtype(arr_or_dtype: List[Literal["b", "a"]]):
    """
    usage.seaborn: 2
    """
    ...


@overload
def is_numeric_dtype(arr_or_dtype: List[Literal["m", "n"]]):
    """
    usage.seaborn: 1
    """
    ...


@overload
def is_numeric_dtype(arr_or_dtype: List[Literal["d", "c", "b", "a"]]):
    """
    usage.seaborn: 1
    """
    ...


@overload
def is_numeric_dtype(arr_or_dtype: List[Literal["y", "x"]]):
    """
    usage.seaborn: 1
    """
    ...


@overload
def is_numeric_dtype(arr_or_dtype: List[pandas._libs.tslibs.timestamps.Timestamp]):
    """
    usage.seaborn: 2
    """
    ...


@overload
def is_numeric_dtype(arr_or_dtype: List[float]):
    """
    usage.seaborn: 1
    """
    ...


@overload
def is_numeric_dtype(arr_or_dtype: List[Literal["3", "2", "1"]]):
    """
    usage.seaborn: 1
    """
    ...


@overload
def is_numeric_dtype(arr_or_dtype: List[Literal["d", "a", "b", "c"]]):
    """
    usage.seaborn: 1
    """
    ...


@overload
def is_numeric_dtype(arr_or_dtype: List[int]):
    """
    usage.seaborn: 1
    """
    ...


@overload
def is_numeric_dtype(arr_or_dtype: List[Union[Literal["d", "a", "b", "c"], float]]):
    """
    usage.seaborn: 1
    """
    ...


def is_numeric_dtype(
    arr_or_dtype: Union[
        pandas.core.series.Series,
        numpy.dtype,
        numpy.ndarray,
        List[Union[str, int, float, pandas._libs.tslibs.timestamps.Timestamp]],
    ]
):
    """
    usage.dask: 1
    usage.koalas: 1
    usage.seaborn: 18
    """
    ...


def is_object_dtype(arr_or_dtype: numpy.dtype):
    """
    usage.dask: 2
    usage.koalas: 1
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
