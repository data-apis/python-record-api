from typing import *


def date_range(
    start: Union[int, pandas._libs.tslibs.timestamps.Timestamp, str],
    end: Union[pandas._libs.tslibs.timestamps.Timestamp, str] = ...,
    periods: int = ...,
    freq: object = ...,
    tz: object = ...,
    name: Union[None, str] = ...,
    closed: Union[Literal["left"], None] = ...,
):
    """
    usage.xarray: 79
    usage.dask: 89
    """
    ...


class DatetimeIndex:

    # usage.dask: 1
    __module__: ClassVar[object]

    # usage.dask: 2
    __name__: ClassVar[object]

    # usage.xarray: 4
    # usage.dask: 15
    name: Union[Literal["index"], None]

    # usage.xarray: 5
    # usage.dask: 4
    dtype: object

    # usage.xarray: 9
    values: object

    # usage.xarray: 1
    # usage.dask: 1
    is_monotonic_increasing: object

    # usage.xarray: 4
    size: object

    # usage.xarray: 1
    # usage.dask: 2
    is_monotonic: object

    # usage.xarray: 1
    is_unique: object

    # usage.xarray: 1
    shape: object

    # usage.xarray: 1
    # usage.dask: 4
    month: object

    # usage.xarray: 1
    time: object

    # usage.xarray: 1
    hour: object

    # usage.xarray: 1
    ndim: object

    # usage.dask: 1
    array: object

    # usage.dask: 4
    freq: None

    # usage.dask: 2
    tz: object

    # usage.dask: 1
    names: object

    # usage.dask: 1
    day: object

    # usage.dask: 1
    is_all_dates: object

    def __getitem__(
        self: object,
        _0: Union[
            int,
            numpy.ndarray,
            slice[Union[None, int], Union[int, None], Union[None, int]],
        ],
        /,
    ):
        """
        usage.xarray: 17
        usage.dask: 22
        """
        ...

    def copy(self: object, /, deep: bool):
        """
        usage.xarray: 1
        """
        ...

    def floor(self: object, /, *args: Literal["v", "t"]):
        """
        usage.xarray: 1
        """
        ...

    def ceil(self: object, /, *args: Literal["v", "t"]):
        """
        usage.xarray: 1
        """
        ...

    def round(self: object, /, *args: Literal["v", "t"]):
        """
        usage.xarray: 1
        """
        ...

    def __sub__(
        self: object,
        _0: Union[numpy.timedelta64, pandas._libs.tslibs.timestamps.Timestamp],
        /,
    ):
        """
        usage.xarray: 3
        """
        ...

    def to_series(self: object, /):
        """
        usage.xarray: 7
        usage.dask: 4
        """
        ...

    def slice_indexer(
        self: object,
        /,
        start: Union[Literal["2001", "1999", "2000-01-01"], numpy.datetime64],
        end: Union[Literal["2002", "2005", "2000-01-10"], numpy.datetime64],
        step: None,
    ):
        """
        usage.xarray: 4
        """
        ...

    def get_indexer(
        self: object,
        /,
        target: numpy.ndarray,
        method: Union[Literal["nearest", "backfill", "pad"], None],
        tolerance: Union[Literal["6H", "12H"], None],
    ):
        """
        usage.xarray: 7
        """
        ...

    def __add__(self: object, _0: object, /):
        """
        usage.xarray: 1
        usage.dask: 7
        """
        ...

    def get_loc(
        self: object,
        /,
        key: Union[Literal["2000-01-01"], numpy.datetime64],
        method: Union[None, Literal["nearest"]],
    ):
        """
        usage.xarray: 3
        """
        ...

    def min(self: object, /):
        """
        usage.dask: 1
        """
        ...

    def max(self: object, /):
        """
        usage.dask: 1
        """
        ...

    def shift(
        self: object,
        /,
        periods: int,
        freq: Union[None, Literal["W", "S"], pandas._libs.tslibs.timedeltas.Timedelta],
    ):
        """
        usage.dask: 11
        """
        ...

    def _maybe_cast_slice_bound(
        self: object,
        /,
        label: str,
        side: Literal["right", "left"],
        kind: Literal["loc"],
    ):
        """
        usage.dask: 23
        """
        ...

    def to_frame(self: object, /, name: Union[Literal["foo"], None]):
        """
        usage.dask: 3
        """
        ...

    def __gt__(self: object, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        """
        usage.dask: 1
        """
        ...

    def __le__(self: object, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        """
        usage.dask: 1
        """
        ...

    def tz_localize(self: object, /, *args: Literal["v", "t"]):
        """
        usage.dask: 2
        """
        ...
