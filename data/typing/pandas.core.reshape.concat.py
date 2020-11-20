from typing import *


@overload
def concat(objs: List[pandas.core.frame.DataFrame]):
    """
    usage.dask: 18
    usage.koalas: 4
    usage.modin: 3
    """
    ...


@overload
def concat(
    objs: List[pandas.core.series.Series],
    axis: int,
    join: Literal["inner"],
    ignore_index: bool,
):
    """
    usage.koalas: 1
    """
    ...


@overload
def concat(
    objs: List[Union[pandas.core.series.Series, pandas.core.frame.DataFrame]],
    axis: int,
    join: Literal["inner"],
    ignore_index: bool,
):
    """
    usage.koalas: 1
    """
    ...


@overload
def concat(
    objs: List[Union[pandas.core.frame.DataFrame, pandas.core.series.Series]],
    axis: int,
    join: Literal["inner"],
    ignore_index: bool,
):
    """
    usage.koalas: 1
    """
    ...


@overload
def concat(
    objs: List[pandas.core.frame.DataFrame],
    axis: int,
    join: Literal["inner"],
    ignore_index: bool,
):
    """
    usage.koalas: 1
    """
    ...


@overload
def concat(
    objs: List[pandas.core.series.Series],
    axis: int,
    join: Literal["outer"],
    ignore_index: bool,
):
    """
    usage.koalas: 1
    """
    ...


@overload
def concat(
    objs: List[Union[pandas.core.series.Series, pandas.core.frame.DataFrame]],
    axis: int,
    join: Literal["outer"],
    ignore_index: bool,
):
    """
    usage.koalas: 1
    """
    ...


@overload
def concat(
    objs: List[Union[pandas.core.frame.DataFrame, pandas.core.series.Series]],
    axis: int,
    join: Literal["outer"],
    ignore_index: bool,
):
    """
    usage.koalas: 1
    """
    ...


@overload
def concat(
    objs: List[pandas.core.frame.DataFrame],
    axis: int,
    join: Literal["outer"],
    ignore_index: bool,
):
    """
    usage.koalas: 1
    """
    ...


@overload
def concat(
    objs: List[pandas.core.frame.DataFrame],
    join: Literal["inner"],
    ignore_index: bool,
    sort: bool,
):
    """
    usage.koalas: 2
    """
    ...


@overload
def concat(
    objs: List[Union[pandas.core.series.Series, pandas.core.frame.DataFrame]],
    join: Literal["inner"],
    ignore_index: bool,
    sort: bool,
):
    """
    usage.koalas: 3
    """
    ...


@overload
def concat(
    objs: List[Union[pandas.core.frame.DataFrame, pandas.core.series.Series]],
    join: Literal["inner"],
    ignore_index: bool,
    sort: bool,
):
    """
    usage.koalas: 1
    """
    ...


@overload
def concat(
    objs: List[pandas.core.frame.DataFrame],
    join: Literal["outer"],
    ignore_index: bool,
    sort: bool,
):
    """
    usage.koalas: 2
    """
    ...


@overload
def concat(
    objs: List[Union[pandas.core.series.Series, pandas.core.frame.DataFrame]],
    join: Literal["outer"],
    ignore_index: bool,
    sort: bool,
):
    """
    usage.koalas: 3
    """
    ...


@overload
def concat(
    objs: List[Union[pandas.core.frame.DataFrame, pandas.core.series.Series]],
    join: Literal["outer"],
    ignore_index: bool,
    sort: bool,
):
    """
    usage.koalas: 1
    """
    ...


@overload
def concat(objs: List[pandas.core.frame.DataFrame], axis: int):
    """
    usage.dask: 6
    usage.modin: 1
    usage.prophet: 11
    usage.sklearn: 1
    usage.statsmodels: 24
    """
    ...


@overload
def concat(objs: List[pandas.core.series.Series], axis: int):
    """
    usage.dask: 7
    usage.modin: 6
    usage.statsmodels: 10
    """
    ...


@overload
def concat(
    objs: List[Union[pandas.core.frame.DataFrame, pandas.core.series.Series]], axis: int
):
    """
    usage.dask: 3
    usage.statsmodels: 1
    """
    ...


@overload
def concat(
    objs: List[Union[pandas.core.series.Series, pandas.core.frame.DataFrame]], axis: int
):
    """
    usage.dask: 3
    usage.statsmodels: 1
    """
    ...


@overload
def concat(
    objs: Tuple[pandas.core.series.Series, pandas.core.series.Series], axis: int
):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def concat(
    objs: Tuple[
        pandas.core.frame.DataFrame,
        pandas.core.frame.DataFrame,
        pandas.core.frame.DataFrame,
    ],
    axis: int,
):
    """
    usage.prophet: 1
    """
    ...


@overload
def concat(
    objs: Tuple[pandas.core.frame.DataFrame, None, pandas.core.frame.DataFrame],
    axis: int,
):
    """
    usage.prophet: 1
    """
    ...


@overload
def concat(
    objs: Tuple[pandas.core.frame.DataFrame, pandas.core.frame.DataFrame], sort: bool
):
    """
    usage.prophet: 2
    """
    ...


@overload
def concat(objs: List[geopandas.geodataframe.GeoDataFrame], ignore_index: bool):
    """
    usage.geopandas: 2
    """
    ...


@overload
def concat(objs: List[geopandas.geoseries.GeoSeries]):
    """
    usage.geopandas: 2
    """
    ...


@overload
def concat(objs: List[geopandas.geodataframe.GeoDataFrame]):
    """
    usage.geopandas: 3
    """
    ...


@overload
def concat(objs: List[geopandas.geodataframe.GeoDataFrame], axis: int):
    """
    usage.geopandas: 1
    """
    ...


@overload
def concat(
    objs: List[Union[pandas.core.frame.DataFrame, geopandas.geodataframe.GeoDataFrame]],
    axis: int,
):
    """
    usage.geopandas: 1
    """
    ...


@overload
def concat(objs: List[pandas.core.frame.DataFrame], join: Literal["outer"], sort: bool):
    """
    usage.dask: 12
    """
    ...


@overload
def concat(objs: List[pandas.core.series.Series], join: Literal["outer"]):
    """
    usage.dask: 9
    """
    ...


@overload
def concat(objs: List[pandas.core.frame.DataFrame], join: Literal["outer"]):
    """
    usage.dask: 12
    """
    ...


@overload
def concat(objs: List[pandas.core.series.Series], axis: int, sort: bool):
    """
    usage.dask: 5
    """
    ...


@overload
def concat(objs: List[pandas.core.series.Series]):
    """
    usage.dask: 4
    """
    ...


@overload
def concat(objs: List[pandas.core.series.Series], axis: int, join: Literal["outer"]):
    """
    usage.dask: 2
    """
    ...


@overload
def concat(objs: List[pandas.core.series.Series], join: Literal["outer"], sort: bool):
    """
    usage.dask: 2
    """
    ...


@overload
def concat(objs: List[pandas.core.frame.DataFrame], axis: int, join: Literal["outer"]):
    """
    usage.dask: 2
    """
    ...


@overload
def concat(
    objs: Dict[int, pandas.core.series.Series], names: List[Literal["bar", "foo"]]
):
    """
    usage.dask: 1
    """
    ...


@overload
def concat(
    objs: List[pandas.core.frame.DataFrame],
    axis: int,
    join: Literal["inner"],
    sort: bool,
):
    """
    usage.dask: 1
    """
    ...


@overload
def concat(objs: List[pandas.core.frame.DataFrame], join: Literal["inner"]):
    """
    usage.dask: 7
    """
    ...


@overload
def concat(objs: List[pandas.core.frame.DataFrame], join: Literal["inner"], sort: bool):
    """
    usage.dask: 6
    """
    ...


@overload
def concat(
    objs: List[pandas.core.frame.DataFrame],
    axis: int,
    join: Literal["outer"],
    sort: bool,
):
    """
    usage.dask: 1
    """
    ...


@overload
def concat(objs: List[pandas.core.frame.DataFrame], sort: bool):
    """
    usage.dask: 7
    """
    ...


@overload
def concat(objs: List[pandas.core.series.Series], sort: bool):
    """
    usage.dask: 2
    """
    ...


@overload
def concat(objs: List[pandas.core.frame.DataFrame], axis: int, join: Literal["inner"]):
    """
    usage.dask: 5
    """
    ...


@overload
def concat(objs: List[pandas.core.series.Series], join: Literal["inner"]):
    """
    usage.dask: 4
    """
    ...


@overload
def concat(objs: List[pandas.core.series.Series], axis: int, join: Literal["inner"]):
    """
    usage.dask: 3
    """
    ...


@overload
def concat(
    objs: List[Union[pandas.core.series.Series, pandas.core.frame.DataFrame]],
    sort: bool,
):
    """
    usage.dask: 1
    """
    ...


@overload
def concat(
    objs: List[Union[pandas.core.series.Series, pandas.core.frame.DataFrame]],
    join: Literal["inner"],
):
    """
    usage.dask: 3
    """
    ...


@overload
def concat(
    objs: List[Union[pandas.core.series.Series, pandas.core.frame.DataFrame]],
    axis: int,
    join: Literal["outer"],
):
    """
    usage.dask: 2
    """
    ...


@overload
def concat(
    objs: List[Union[pandas.core.series.Series, pandas.core.frame.DataFrame]],
    axis: int,
    join: Literal["inner"],
):
    """
    usage.dask: 5
    """
    ...


@overload
def concat(
    objs: List[Union[pandas.core.frame.DataFrame, pandas.core.series.Series]],
    sort: bool,
):
    """
    usage.dask: 2
    """
    ...


@overload
def concat(
    objs: List[Union[pandas.core.frame.DataFrame, pandas.core.series.Series]],
    join: Literal["inner"],
):
    """
    usage.dask: 3
    """
    ...


@overload
def concat(
    objs: List[Union[pandas.core.frame.DataFrame, pandas.core.series.Series]],
    axis: int,
    join: Literal["outer"],
):
    """
    usage.dask: 2
    """
    ...


@overload
def concat(
    objs: List[Union[pandas.core.frame.DataFrame, pandas.core.series.Series]],
    axis: int,
    join: Literal["inner"],
):
    """
    usage.dask: 5
    """
    ...


@overload
def concat(objs: List[Union[pandas.core.series.Series, pandas.core.frame.DataFrame]]):
    """
    usage.dask: 2
    """
    ...


@overload
def concat(objs: List[Union[pandas.core.frame.DataFrame, pandas.core.series.Series]]):
    """
    usage.dask: 1
    """
    ...


@overload
def concat(objs: List[pandas.core.frame.DataFrame], ignore_index: bool):
    """
    usage.sklearn: 2
    """
    ...


def concat(
    objs: Union[
        List[
            Union[
                pandas.core.series.Series,
                pandas.core.frame.DataFrame,
                geopandas.geodataframe.GeoDataFrame,
                geopandas.geoseries.GeoSeries,
            ]
        ],
        Tuple[Union[pandas.core.series.Series, pandas.core.frame.DataFrame, None], ...],
        Dict[int, pandas.core.series.Series],
    ],
    axis: int = ...,
    join: Literal["outer", "inner"] = ...,
    ignore_index: bool = ...,
    sort: bool = ...,
):
    """
    usage.dask: 148
    usage.geopandas: 9
    usage.koalas: 24
    usage.modin: 10
    usage.prophet: 15
    usage.sklearn: 3
    usage.statsmodels: 37
    """
    ...


class _Concatenator:

    # usage.geopandas: 1
    objs: object
