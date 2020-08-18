from typing import *


@overload
def concat(objs: List[pandas.core.frame.DataFrame], join: Literal["outer"], sort: bool):
    """
    usage.dask: 12
    """
    ...


@overload
def concat(objs: List[pandas.core.series.Series], axis: int):
    """
    usage.dask: 7
    """
    ...


@overload
def concat(objs: List[pandas.core.frame.DataFrame]):
    """
    usage.dask: 18
    """
    ...


@overload
def concat(objs: List[pandas.core.frame.DataFrame], join: Literal["outer"]):
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
def concat(objs: List[pandas.core.frame.DataFrame], axis: int):
    """
    usage.dask: 6
    usage.sklearn: 1
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
    objs: List[Union[pandas.core.series.Series, pandas.core.frame.DataFrame]], axis: int
):
    """
    usage.dask: 3
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
    objs: List[Union[pandas.core.frame.DataFrame, pandas.core.series.Series]], axis: int
):
    """
    usage.dask: 3
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
        List[Union[pandas.core.series.Series, pandas.core.frame.DataFrame]],
        Dict[int, pandas.core.series.Series],
    ],
    axis: int = ...,
    join: Literal["outer", "inner"] = ...,
    sort: bool = ...,
):
    """
    usage.dask: 148
    usage.sklearn: 3
    """
    ...
