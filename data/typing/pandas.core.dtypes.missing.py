from typing import *


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
def isna(obj: numpy.ndarray):
    """
    usage.dask: 8
    usage.xarray: 22
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
def isna(obj: List[int]):
    """
    usage.dask: 9
    """
    ...


@overload
def isna(obj: float):
    """
    usage.dask: 2
    """
    ...


@overload
def isna(obj: List[pandas._libs.tslibs.timestamps.Timestamp]):
    """
    usage.dask: 6
    """
    ...


@overload
def isna(obj: pandas._libs.tslibs.timestamps.Timestamp):
    """
    usage.dask: 2
    """
    ...


@overload
def isna(obj: List[float]):
    """
    usage.dask: 14
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
def isna(obj: pandas.core.series.Series):
    """
    usage.dask: 3
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
def isna(obj: List[Literal["3", "2", "1"]]):
    """
    usage.dask: 2
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
def isna(obj: List[Literal["a", "E", "Z"]]):
    """
    usage.dask: 2
    """
    ...


@overload
def isna(obj: Literal["W"]):
    """
    usage.dask: 1
    """
    ...


@overload
def isna(obj: Literal["f"]):
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
def isna(obj: int):
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
    usage.xarray: 44
    """
    ...


@overload
def notna(obj: numpy.ndarray):
    """
    usage.xarray: 3
    """
    ...


@overload
def notna(obj: pandas.core.indexes.numeric.Int64Index):
    """
    usage.dask: 2
    """
    ...


def notna(obj: Union[pandas.core.indexes.numeric.Int64Index, numpy.ndarray]):
    """
    usage.dask: 2
    usage.xarray: 3
    """
    ...
