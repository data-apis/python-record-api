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
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    check_index_type: Literal["equiv"],
    check_column_type: Literal["equiv"],
    check_exact: bool,
):
    """
    usage.koalas: 1
    """
    ...


@overload
def assert_frame_equal(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    check_index_type: bool,
    check_column_type: Literal["equiv"],
    check_exact: bool,
):
    """
    usage.koalas: 1
    """
    ...


@overload
def assert_frame_equal(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    check_index_type: bool,
    check_column_type: bool,
    check_exact: bool,
):
    """
    usage.koalas: 1
    """
    ...


@overload
def assert_frame_equal(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    check_index_type: Literal["equiv"],
    check_column_type: bool,
    check_exact: bool,
):
    """
    usage.koalas: 1
    """
    ...


@overload
def assert_frame_equal(
    left: pandas.core.frame.DataFrame, right: pandas.core.frame.DataFrame
):
    """
    usage.alphalens: 17
    usage.dask: 20
    usage.geopandas: 8
    usage.networkx: 2
    usage.seaborn: 5
    usage.statsmodels: 88
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
    usage.statsmodels: 1
    """
    ...


@overload
def assert_frame_equal(
    left: geopandas.geodataframe.GeoDataFrame,
    right: geopandas.geodataframe.GeoDataFrame,
    check_dtype: bool,
    check_index_type: Literal["equiv"],
    check_column_type: Literal["equiv"],
    obj: Literal["GeoDataFrame"],
):
    """
    usage.geopandas: 1
    """
    ...


@overload
def assert_frame_equal(
    left: geopandas.geodataframe.GeoDataFrame,
    right: geopandas.geodataframe.GeoDataFrame,
    check_dtype: bool,
    check_index_type: Literal["equiv"],
    check_column_type: bool,
    obj: Literal["GeoDataFrame"],
):
    """
    usage.geopandas: 1
    """
    ...


@overload
def assert_frame_equal(
    left: geopandas.geodataframe.GeoDataFrame,
    right: geopandas.geodataframe.GeoDataFrame,
    check_column_type: bool,
):
    """
    usage.geopandas: 4
    """
    ...


@overload
def assert_frame_equal(
    left: geopandas.geodataframe.GeoDataFrame,
    right: geopandas.geodataframe.GeoDataFrame,
):
    """
    usage.geopandas: 13
    """
    ...


@overload
def assert_frame_equal(
    left: geopandas.geodataframe.GeoDataFrame, right: pandas.core.frame.DataFrame
):
    """
    usage.geopandas: 4
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
    left: Union[pandas.core.frame.DataFrame, geopandas.geodataframe.GeoDataFrame],
    right: Union[pandas.core.frame.DataFrame, geopandas.geodataframe.GeoDataFrame],
    check_dtype: bool = ...,
    check_index_type: Union[Literal["equiv"], bool] = ...,
    check_column_type: Union[Literal["equiv"], bool] = ...,
    obj: Literal["GeoDataFrame"] = ...,
    check_exact: bool = ...,
):
    """
    usage.alphalens: 17
    usage.dask: 23
    usage.geopandas: 31
    usage.koalas: 4
    usage.networkx: 2
    usage.seaborn: 5
    usage.statsmodels: 89
    """
    ...


@overload
def assert_index_equal(
    left: pandas.core.indexes.numeric.Float64Index,
    right: pandas.core.indexes.numeric.Float64Index,
    check_exact: bool,
):
    """
    usage.koalas: 1
    """
    ...


@overload
def assert_index_equal(
    left: pandas.core.indexes.base.Index,
    right: pandas.core.indexes.base.Index,
    check_exact: bool,
):
    """
    usage.koalas: 1
    """
    ...


@overload
def assert_index_equal(
    left: pandas.core.indexes.multi.MultiIndex,
    right: pandas.core.indexes.multi.MultiIndex,
    check_exact: bool,
):
    """
    usage.koalas: 1
    """
    ...


@overload
def assert_index_equal(
    left: pandas.core.indexes.numeric.Int64Index,
    right: pandas.core.indexes.numeric.Int64Index,
    check_exact: bool,
):
    """
    usage.koalas: 1
    """
    ...


@overload
def assert_index_equal(
    left: pandas.core.indexes.datetimes.DatetimeIndex,
    right: pandas.core.indexes.datetimes.DatetimeIndex,
    check_exact: bool,
):
    """
    usage.koalas: 1
    """
    ...


@overload
def assert_index_equal(
    left: pandas.core.indexes.numeric.Int64Index,
    right: pandas.core.indexes.range.RangeIndex,
    check_exact: bool,
):
    """
    usage.koalas: 1
    """
    ...


@overload
def assert_index_equal(
    left: pandas.core.indexes.base.Index, right: pandas.core.indexes.base.Index
):
    """
    usage.dask: 36
    usage.geopandas: 6
    usage.statsmodels: 12
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
    usage.statsmodels: 4
    usage.xarray: 3
    """
    ...


@overload
def assert_index_equal(
    left: pandas.core.indexes.numeric.Int64Index,
    right: pandas.core.indexes.numeric.Int64Index,
):
    """
    usage.dask: 7
    usage.geopandas: 2
    usage.statsmodels: 4
    """
    ...


@overload
def assert_index_equal(
    left: pandas.core.indexes.range.RangeIndex,
    right: pandas.core.indexes.range.RangeIndex,
):
    """
    usage.dask: 3
    usage.statsmodels: 4
    """
    ...


@overload
def assert_index_equal(
    left: pandas.core.indexes.datetimes.DatetimeIndex,
    right: pandas.core.indexes.datetimes.DatetimeIndex,
):
    """
    usage.dask: 1
    usage.statsmodels: 8
    """
    ...


@overload
def assert_index_equal(
    left: pandas.core.indexes.period.PeriodIndex,
    right: pandas.core.indexes.period.PeriodIndex,
):
    """
    usage.dask: 1
    usage.statsmodels: 7
    """
    ...


@overload
def assert_index_equal(
    left: pandas.core.indexes.base.Index,
    right: pandas.core.indexes.base.Index,
    exact: Literal["equiv"],
    obj: Literal["GeoDataFrame.columns"],
):
    """
    usage.geopandas: 1
    """
    ...


@overload
def assert_index_equal(
    left: pandas.core.indexes.base.Index,
    right: pandas.core.indexes.base.Index,
    exact: bool,
    obj: Literal["GeoDataFrame.columns"],
):
    """
    usage.geopandas: 1
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
    left: pandas.core.indexes.numeric.Float64Index,
    right: pandas.core.indexes.numeric.Float64Index,
):
    """
    usage.dask: 5
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


def assert_index_equal(
    left: object,
    right: object,
    exact: Union[bool, Literal["equiv"]] = ...,
    obj: Literal["GeoDataFrame.columns"] = ...,
):
    """
    usage.dask: 68
    usage.geopandas: 10
    usage.koalas: 6
    usage.statsmodels: 39
    usage.xarray: 5
    """
    ...


@overload
def assert_series_equal(
    left: pandas.core.series.Series,
    right: pandas.core.series.Series,
    check_index_type: Literal["equiv"],
    check_exact: bool,
):
    """
    usage.koalas: 1
    """
    ...


@overload
def assert_series_equal(
    left: pandas.core.series.Series,
    right: pandas.core.series.Series,
    check_index_type: bool,
    check_exact: bool,
):
    """
    usage.koalas: 1
    """
    ...


@overload
def assert_series_equal(
    left: pandas.core.series.Series,
    right: pandas.core.series.Series,
    check_less_precise: bool,
):
    """
    usage.alphalens: 1
    """
    ...


@overload
def assert_series_equal(
    left: pandas.core.series.Series, right: pandas.core.series.Series
):
    """
    usage.alphalens: 4
    usage.dask: 17
    usage.geopandas: 22
    usage.seaborn: 1
    usage.statsmodels: 48
    """
    ...


@overload
def assert_series_equal(
    left: pandas.core.series.Series,
    right: geopandas.geoseries.GeoSeries,
    check_series_type: bool,
    check_names: bool,
):
    """
    usage.geopandas: 1
    """
    ...


@overload
def assert_series_equal(
    left: geopandas.geoseries.GeoSeries, right: geopandas.geoseries.GeoSeries
):
    """
    usage.geopandas: 5
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
    left: Union[pandas.core.series.Series, geopandas.geoseries.GeoSeries],
    right: Union[pandas.core.series.Series, geopandas.geoseries.GeoSeries],
    check_dtype: bool = ...,
    check_series_type: bool = ...,
    check_names: bool = ...,
    check_index_type: Union[bool, Literal["equiv"]] = ...,
    check_exact: bool = ...,
):
    """
    usage.alphalens: 5
    usage.dask: 19
    usage.geopandas: 28
    usage.koalas: 2
    usage.seaborn: 1
    usage.statsmodels: 48
    """
    ...


def getSeriesData():
    """
    usage.modin: 4
    """
    ...


def makeDataFrame():
    """
    usage.statsmodels: 5
    """
    ...


def makeMissingDataframe(density: float, random_state: int):
    """
    usage.koalas: 1
    """
    ...
