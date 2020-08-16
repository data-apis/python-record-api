from typing import *


def date_range(
    start: Union[pandas._libs.tslibs.timestamps.Timestamp, int, str],
    end: Union[pandas._libs.tslibs.timestamps.Timestamp, str] = ...,
    periods: int = ...,
    freq: object = ...,
    tz: object = ...,
    name: Union[None, str] = ...,
    closed: Union[None, Literal["left"]] = ...,
):
    """
    usage.dask: 97
    usage.xarray: 122
    """
    ...


class DatetimeIndex:

    # usage.dask: 1
    __module__: ClassVar[object]

    # usage.dask: 2
    __name__: ClassVar[object]

    # usage.dask: 1
    array: object

    # usage.dask: 1
    day: object

    # usage.xarray: 1
    dayofweek: object

    # usage.xarray: 1
    dayofyear: object

    # usage.dask: 4
    # usage.xarray: 5
    dtype: object

    # usage.dask: 4
    freq: None

    # usage.xarray: 1
    hour: object

    # usage.dask: 1
    is_all_dates: object

    # usage.dask: 2
    # usage.xarray: 2
    is_monotonic: object

    # usage.xarray: 2
    is_unique: object

    # usage.dask: 4
    # usage.xarray: 1
    month: object

    # usage.dask: 17
    # usage.xarray: 5
    name: Union[None, Literal["timestamp", "index"]]

    # usage.dask: 1
    names: object

    # usage.xarray: 1
    ndim: object

    # usage.xarray: 1
    shape: object

    # usage.xarray: 5
    size: object

    # usage.xarray: 1
    time: object

    # usage.dask: 2
    tz: object

    # usage.xarray: 16
    values: object

    def __add__(self, _0: object, /):
        """
        usage.dask: 8
        usage.pandas: 103
        usage.xarray: 2
        """
        ...

    def __contains__(self, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        """
        usage.dask: 2
        """
        ...

    def __eq__(self, _0: Union[numpy.ndarray, numpy.datetime64], /):
        """
        usage.pandas: 32
        """
        ...

    def __ge__(self, _0: Union[numpy.ndarray, numpy.datetime64], /):
        """
        usage.pandas: 3
        """
        ...

    def __getitem__(
        self,
        _0: Union[
            int,
            numpy.ndarray,
            slice[Union[None, int], Union[int, None], Union[None, int]],
        ],
        /,
    ):
        """
        usage.dask: 22
        usage.xarray: 20
        """
        ...

    def __gt__(
        self,
        _0: Union[
            pandas._libs.tslibs.timestamps.Timestamp, numpy.datetime64, numpy.ndarray
        ],
        /,
    ):
        """
        usage.dask: 1
        usage.pandas: 2
        """
        ...

    def __iadd__(self, _0: Union[numpy.ndarray, numpy.timedelta64], /):
        """
        usage.pandas: 4
        """
        ...

    def __isub__(self, _0: Union[numpy.ndarray, numpy.timedelta64], /):
        """
        usage.pandas: 3
        """
        ...

    def __le__(
        self,
        _0: Union[
            pandas._libs.tslibs.timestamps.Timestamp, numpy.datetime64, numpy.ndarray
        ],
        /,
    ):
        """
        usage.dask: 1
        usage.pandas: 5
        """
        ...

    def __lt__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    def __ne__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 2
        """
        ...

    def __radd__(
        self, _0: Union[numpy.datetime64, numpy.timedelta64, numpy.ndarray], /
    ):
        """
        usage.pandas: 59
        """
        ...

    def __rsub__(
        self, _0: Union[numpy.ndarray, numpy.timedelta64, numpy.datetime64], /
    ):
        """
        usage.pandas: 32
        """
        ...

    def __sub__(
        self,
        _0: Union[
            numpy.datetime64,
            numpy.timedelta64,
            numpy.ndarray,
            pandas._libs.tslibs.timestamps.Timestamp,
        ],
        /,
    ):
        """
        usage.pandas: 75
        usage.xarray: 4
        """
        ...

    def _maybe_cast_slice_bound(
        self, /, label: str, side: Literal["right", "left"], kind: Literal["loc"]
    ):
        """
        usage.dask: 23
        """
        ...

    def ceil(self, /, *args: Literal["v", "t"]):
        """
        usage.xarray: 3
        """
        ...

    def copy(self, /, deep: bool):
        """
        usage.xarray: 1
        """
        ...

    def equals(self, /, other: pandas.core.indexes.datetimes.DatetimeIndex):
        """
        usage.xarray: 2
        """
        ...

    def floor(self, /, *args: Literal["v", "t"]):
        """
        usage.xarray: 3
        """
        ...

    def get_indexer(
        self,
        /,
        target: numpy.ndarray,
        method: Union[Literal["nearest", "backfill", "pad"], None],
        tolerance: Union[Literal["6H", "12H"], None],
    ):
        """
        usage.xarray: 7
        """
        ...

    def get_loc(
        self,
        /,
        key: Union[Literal["2000-01-01"], numpy.datetime64],
        method: Union[None, Literal["nearest"]],
    ):
        """
        usage.xarray: 3
        """
        ...

    def max(self, /):
        """
        usage.dask: 1
        """
        ...

    def min(self, /):
        """
        usage.dask: 1
        """
        ...

    def round(self, /, *args: Literal["v", "t"]):
        """
        usage.xarray: 3
        """
        ...

    def shift(
        self,
        /,
        periods: int,
        freq: Union[None, Literal["W", "S"], pandas._libs.tslibs.timedeltas.Timedelta],
    ):
        """
        usage.dask: 11
        """
        ...

    def slice_indexer(
        self,
        /,
        start: Union[Literal["2001", "1999", "2000-01-01"], numpy.datetime64],
        end: Union[Literal["2002", "2005", "2000-01-10"], numpy.datetime64],
        step: None,
    ):
        """
        usage.xarray: 4
        """
        ...

    def to_frame(self, /, name: Union[Literal["foo"], None]):
        """
        usage.dask: 3
        """
        ...

    def to_numpy(self, /, dtype: Literal["datetime64[ns]"]):
        """
        usage.xarray: 1
        """
        ...

    def to_series(self, /):
        """
        usage.dask: 4
        usage.xarray: 7
        """
        ...

    def tz_localize(self, /, *args: Literal["v", "t"]):
        """
        usage.dask: 2
        """
        ...
