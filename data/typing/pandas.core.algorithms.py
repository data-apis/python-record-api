from typing import *


@overload
def factorize(values: pandas.core.indexes.numeric.Int64Index, sort: bool):
    """
    usage.xarray: 1
    """
    ...


@overload
def factorize(values: pandas.core.indexes.base.Index, sort: bool):
    """
    usage.xarray: 1
    """
    ...


@overload
def factorize(values: pandas.core.indexes.numeric.Float64Index, sort: bool):
    """
    usage.xarray: 1
    """
    ...


@overload
def factorize(values: pandas.core.indexes.datetimes.DatetimeIndex, sort: bool):
    """
    usage.xarray: 1
    """
    ...


def factorize(
    values: Union[
        pandas.core.indexes.datetimes.DatetimeIndex,
        pandas.core.indexes.base.Index,
        pandas.core.indexes.numeric.Int64Index,
        pandas.core.indexes.numeric.Float64Index,
    ],
    sort: bool,
):
    """
    usage.xarray: 4
    """
    ...


@overload
def unique(values: List[Literal["time"]]):
    """
    usage.xarray: 2
    """
    ...


@overload
def unique(values: List[Literal["time", "lon", "lat"]]):
    """
    usage.xarray: 1
    """
    ...


@overload
def unique(values: List[Literal["x"]]):
    """
    usage.xarray: 5
    """
    ...


@overload
def unique(values: List[Literal["x", "t"]]):
    """
    usage.xarray: 2
    """
    ...


@overload
def unique(values: List[Literal["t"]]):
    """
    usage.xarray: 3
    """
    ...


@overload
def unique(values: List[Literal["y", "x"]]):
    """
    usage.xarray: 4
    """
    ...


@overload
def unique(values: List[Literal["DATE-TIME", "VAR", "TSTEP"]]):
    """
    usage.xarray: 1
    """
    ...


@overload
def unique(values: List[Literal["COL", "ROW", "LAY", "TSTEP"]]):
    """
    usage.xarray: 1
    """
    ...


@overload
def unique(values: List[Literal["dim2", "dim1"]]):
    """
    usage.xarray: 5
    """
    ...


@overload
def unique(values: List[Literal["dim1", "dim3"]]):
    """
    usage.xarray: 4
    """
    ...


@overload
def unique(values: List[Literal["a"]]):
    """
    usage.xarray: 2
    """
    ...


@overload
def unique(values: list):
    """
    usage.xarray: 1
    """
    ...


@overload
def unique(values: List[Literal["z"]]):
    """
    usage.xarray: 2
    """
    ...


@overload
def unique(values: List[Literal["dim2"]]):
    """
    usage.xarray: 4
    """
    ...


@overload
def unique(values: List[Literal["y"]]):
    """
    usage.xarray: 5
    """
    ...


@overload
def unique(values: List[Literal["x", "y"]]):
    """
    usage.xarray: 3
    """
    ...


@overload
def unique(values: List[Literal["sign", "y", "x"]]):
    """
    usage.xarray: 1
    """
    ...


@overload
def unique(values: List[Literal["z", "q"]]):
    """
    usage.xarray: 2
    """
    ...


@overload
def unique(values: List[Literal["dim1", "dim2"]]):
    """
    usage.xarray: 1
    """
    ...


@overload
def unique(values: List[Literal["dim4"]]):
    """
    usage.xarray: 2
    """
    ...


@overload
def unique(values: List[Literal["y", "x", "variable"]]):
    """
    usage.xarray: 1
    """
    ...


@overload
def unique(values: List[Literal["y", "a"]]):
    """
    usage.xarray: 1
    """
    ...


@overload
def unique(values: List[Literal["b"]]):
    """
    usage.xarray: 1
    """
    ...


@overload
def unique(values: List[Literal["x", "b"]]):
    """
    usage.xarray: 1
    """
    ...


@overload
def unique(values: List[Literal["stacked_ny_nx"]]):
    """
    usage.xarray: 1
    """
    ...


@overload
def unique(values: List[Literal["stacked_ny_nx", "time"]]):
    """
    usage.xarray: 1
    """
    ...


@overload
def unique(values: List[Literal["features"]]):
    """
    usage.xarray: 1
    """
    ...


@overload
def unique(values: List[Literal["features", "x"]]):
    """
    usage.xarray: 1
    """
    ...


@overload
def unique(values: List[Literal["dim1"]]):
    """
    usage.xarray: 1
    """
    ...


@overload
def unique(values: List[Literal["dim3", "dim1"]]):
    """
    usage.xarray: 1
    """
    ...


@overload
def unique(values: List[Literal["dim3"]]):
    """
    usage.xarray: 1
    """
    ...


@overload
def unique(values: List[Literal["space"]]):
    """
    usage.xarray: 1
    """
    ...


@overload
def unique(values: List[Literal["quantile"]]):
    """
    usage.xarray: 3
    """
    ...


@overload
def unique(values: List[Literal["stacked_lat_lon", "time"]]):
    """
    usage.xarray: 1
    """
    ...


@overload
def unique(values: List[Literal["stacked_lat_lon"]]):
    """
    usage.xarray: 1
    """
    ...


@overload
def unique(values: List[Literal["time", "id"]]):
    """
    usage.xarray: 1
    """
    ...


@overload
def unique(values: List[Literal["id"]]):
    """
    usage.xarray: 1
    """
    ...


@overload
def unique(values: List[Literal["z", "x"]]):
    """
    usage.xarray: 1
    """
    ...


@overload
def unique(values: List[Literal["z", "y"]]):
    """
    usage.xarray: 1
    """
    ...


@overload
def unique(values: List[Literal["y", "z", "x"]]):
    """
    usage.xarray: 1
    """
    ...


@overload
def unique(values: List[Literal["z", "quantile"]]):
    """
    usage.xarray: 1
    """
    ...


def unique(values: List[str]):
    """
    usage.xarray: 74
    """
    ...
