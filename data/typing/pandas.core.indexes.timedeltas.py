from typing import *


def timedelta_range(
    start: Union[Literal["1 day", "1 days"], numpy.timedelta64, int],
    end: Literal["30 days"] = ...,
    periods: int = ...,
    freq: Union[
        pandas.tseries.offsets.Day,
        pandas.tseries.offsets.Minute,
        pandas.tseries.offsets.Hour,
        Literal["H", "D", "T", "6H"],
        None,
    ] = ...,
):
    """
    usage.xarray: 2
    usage.dask: 9
    """
    ...


class TimedeltaIndex:
    def __init__(
        self, /, data: List[numpy.timedelta64], name: Literal["timedelta", "foo"]
    ):
        """
        usage.dask: 2
        """
        ...

    # usage.dask: 1
    __module__: ClassVar[object]

    # usage.dask: 2
    __name__: ClassVar[object]

    # usage.dask: 1
    array: object

    # usage.xarray: 4
    # usage.dask: 3
    dtype: object

    # usage.dask: 3
    freq: object

    # usage.dask: 1
    is_monotonic_increasing: object

    # usage.xarray: 1
    # usage.dask: 9
    name: object

    # usage.dask: 1
    names: object

    # usage.xarray: 4
    values: object

    def __add__(self, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        """
        usage.xarray: 1
        """
        ...

    def __getitem__(self, _0: Union[int, numpy.ndarray, slice[int, int, int]], /):
        """
        usage.xarray: 4
        usage.dask: 5
        """
        ...

    def __truediv__(self, _0: numpy.timedelta64, /):
        """
        usage.xarray: 1
        """
        ...

    def ceil(self, /, *args: Literal["v", "t"]):
        """
        usage.xarray: 1
        """
        ...

    def copy(self, /, deep: bool):
        """
        usage.xarray: 1
        """
        ...

    def floor(self, /, *args: Literal["v", "t"]):
        """
        usage.xarray: 1
        """
        ...

    def get_indexer(self, /, target: numpy.ndarray, method: None, tolerance: None):
        """
        usage.xarray: 1
        """
        ...

    def get_loc(
        self,
        /,
        key: pandas._libs.tslibs.timedeltas.Timedelta,
        method: None,
        tolerance: None,
    ):
        """
        usage.xarray: 1
        """
        ...

    def round(self, /, *args: Literal["v", "t"]):
        """
        usage.xarray: 1
        """
        ...

    def shift(
        self,
        /,
        periods: int,
        freq: Union[None, Literal["S"], pandas._libs.tslibs.timedeltas.Timedelta],
    ):
        """
        usage.dask: 8
        """
        ...
