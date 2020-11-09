from typing import *


@overload
def isna(obj: Literal["dog"]):
    """
    usage.koalas: 1
    """
    ...


@overload
def isna(obj: float):
    """
    usage.dask: 2
    usage.koalas: 1
    """
    ...


@overload
def isna(obj: numpy.ndarray):
    """
    usage.dask: 8
    usage.koalas: 1
    usage.seaborn: 5
    usage.xarray: 22
    """
    ...


@overload
def isna(obj: None):
    """
    usage.xarray: 1
    """
    ...


@overload
def isna(obj: numpy.float64):
    """
    usage.dask: 3
    usage.xarray: 3
    """
    ...


@overload
def isna(obj: numpy.float32):
    """
    usage.xarray: 1
    """
    ...


@overload
def isna(obj: numpy.bytes_):
    """
    usage.xarray: 2
    """
    ...


@overload
def isna(obj: bytes):
    """
    usage.xarray: 1
    """
    ...


@overload
def isna(obj: numpy.int8):
    """
    usage.xarray: 2
    """
    ...


@overload
def isna(obj: numpy.uint8):
    """
    usage.xarray: 1
    """
    ...


@overload
def isna(obj: numpy.int16):
    """
    usage.xarray: 2
    """
    ...


@overload
def isna(obj: Literal["XXX"]):
    """
    usage.xarray: 1
    """
    ...


@overload
def isna(obj: Literal[""]):
    """
    usage.xarray: 1
    """
    ...


@overload
def isna(obj: numpy.int32):
    """
    usage.xarray: 1
    """
    ...


@overload
def isna(obj: numpy.int64):
    """
    usage.dask: 3
    usage.xarray: 2
    """
    ...


@overload
def isna(obj: numpy.timedelta64):
    """
    usage.xarray: 1
    """
    ...


@overload
def isna(obj: sparse._coo.core.COO):
    """
    usage.xarray: 1
    """
    ...


@overload
def isna(obj: Literal["Z"]):
    """
    usage.dask: 1
    usage.xarray: 1
    """
    ...


@overload
def isna(obj: Literal["A"]):
    """
    usage.dask: 2
    usage.xarray: 1
    """
    ...


@overload
def isna(obj: pandas.core.series.Series):
    """
    usage.dask: 3
    usage.seaborn: 1
    """
    ...


@overload
def isna(obj: pandas.core.frame.DataFrame):
    """
    usage.seaborn: 1
    """
    ...


@overload
def isna(obj: List[Literal["b", "a"]]):
    """
    usage.seaborn: 2
    """
    ...


@overload
def isna(obj: List[Literal["m", "n"]]):
    """
    usage.seaborn: 1
    """
    ...


@overload
def isna(obj: List[Literal["d", "c", "b", "a"]]):
    """
    usage.seaborn: 1
    """
    ...


@overload
def isna(obj: List[Literal["y", "x"]]):
    """
    usage.seaborn: 1
    """
    ...


@overload
def isna(obj: List[pandas._libs.tslibs.timestamps.Timestamp]):
    """
    usage.dask: 6
    usage.seaborn: 2
    """
    ...


@overload
def isna(obj: List[float]):
    """
    usage.dask: 14
    usage.seaborn: 1
    """
    ...


@overload
def isna(obj: List[Literal["3", "2", "1"]]):
    """
    usage.dask: 2
    usage.seaborn: 1
    """
    ...


@overload
def isna(obj: List[Literal["d", "a", "b", "c"]]):
    """
    usage.seaborn: 1
    """
    ...


@overload
def isna(obj: List[int]):
    """
    usage.dask: 9
    usage.seaborn: 1
    """
    ...


@overload
def isna(obj: List[Union[Literal["d", "a", "b", "c"], float]]):
    """
    usage.seaborn: 1
    """
    ...


@overload
def isna(obj: int):
    """
    usage.dask: 2
    """
    ...


@overload
def isna(obj: pandas._libs.tslibs.timestamps.Timestamp):
    """
    usage.dask: 2
    """
    ...


@overload
def isna(obj: List[Literal["c", "b", "a"]]):
    """
    usage.dask: 2
    """
    ...


@overload
def isna(obj: Literal["a"]):
    """
    usage.dask: 2
    """
    ...


@overload
def isna(obj: Literal["b"]):
    """
    usage.dask: 2
    """
    ...


@overload
def isna(obj: Literal["c"]):
    """
    usage.dask: 1
    """
    ...


@overload
def isna(obj: List[Literal["CAT0"]]):
    """
    usage.dask: 5
    """
    ...


@overload
def isna(obj: Literal["CAT0"]):
    """
    usage.dask: 2
    """
    ...


@overload
def isna(obj: List[Literal["CAT2", "CAT0"]]):
    """
    usage.dask: 1
    """
    ...


@overload
def isna(obj: Literal["CAT2"]):
    """
    usage.dask: 2
    """
    ...


@overload
def isna(obj: List[Literal["CAT5", "CAT0"]]):
    """
    usage.dask: 1
    """
    ...


@overload
def isna(obj: Literal["CAT5"]):
    """
    usage.dask: 2
    """
    ...


@overload
def isna(obj: List[Literal["CAT2", "CAT1", "CAT0"]]):
    """
    usage.dask: 4
    """
    ...


@overload
def isna(obj: List[Literal["CAT5", "CAT3", "CAT0"]]):
    """
    usage.dask: 2
    """
    ...


@overload
def isna(obj: List[str]):
    """
    usage.dask: 2
    """
    ...


@overload
def isna(obj: dask.dataframe.core.Series):
    """
    usage.dask: 1
    """
    ...


@overload
def isna(obj: List[Literal["Edith", "Dan", "Charlie", "Bob", "Alice"]]):
    """
    usage.dask: 2
    """
    ...


@overload
def isna(obj: Literal["Alice"]):
    """
    usage.dask: 2
    """
    ...


@overload
def isna(obj: Literal["Zelda"]):
    """
    usage.dask: 2
    """
    ...


@overload
def isna(obj: List[Literal["d", "c", "a"]]):
    """
    usage.dask: 1
    """
    ...


@overload
def isna(obj: List[Literal["B", "A"]]):
    """
    usage.dask: 2
    """
    ...


@overload
def isna(obj: Literal["B"]):
    """
    usage.dask: 1
    """
    ...


@overload
def isna(obj: Literal["1"]):
    """
    usage.dask: 2
    """
    ...


@overload
def isna(obj: Literal["3"]):
    """
    usage.dask: 2
    """
    ...


@overload
def isna(obj: pandas._libs.tslibs.nattype.NaTType):
    """
    usage.dask: 2
    """
    ...


@overload
def isna(obj: List[None]):
    """
    usage.dask: 2
    """
    ...


@overload
def isna(obj: List[pandas._libs.tslibs.nattype.NaTType]):
    """
    usage.dask: 2
    """
    ...


@overload
def isna(obj: List[Literal["a", "C", "Z"]]):
    """
    usage.dask: 2
    """
    ...


@overload
def isna(obj: Literal["Y"]):
    """
    usage.dask: 1
    """
    ...


@overload
def isna(obj: Literal["g"]):
    """
    usage.dask: 1
    """
    ...


@overload
def isna(obj: List[Literal["2", "1", "0"]]):
    """
    usage.dask: 2
    """
    ...


@overload
def isna(obj: Literal["0"]):
    """
    usage.dask: 1
    """
    ...


@overload
def isna(obj: Literal["2"]):
    """
    usage.dask: 2
    """
    ...


@overload
def isna(obj: numpy.datetime64):
    """
    usage.dask: 2
    """
    ...


def isna(obj: object):
    """
    usage.dask: 117
    usage.koalas: 3
    usage.seaborn: 19
    usage.xarray: 44
    """
    ...


@overload
def notna(obj: databricks.koalas.indexes.Index):
    """
    usage.koalas: 1
    """
    ...


@overload
def notna(obj: numpy.ndarray):
    """
    usage.seaborn: 5
    usage.xarray: 3
    """
    ...


@overload
def notna(obj: pandas.core.series.Series):
    """
    usage.seaborn: 2
    """
    ...


@overload
def notna(obj: pandas.core.indexes.numeric.Int64Index):
    """
    usage.dask: 2
    """
    ...


def notna(
    obj: Union[
        pandas.core.indexes.numeric.Int64Index,
        databricks.koalas.indexes.Index,
        numpy.ndarray,
        pandas.core.series.Series,
    ]
):
    """
    usage.dask: 2
    usage.koalas: 1
    usage.seaborn: 7
    usage.xarray: 3
    """
    ...
