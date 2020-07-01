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
    "\n    usage.xarray: 79\n    usage.dask: 89\n    "
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
        "\n    usage.xarray: 17\n    usage.dask: 22\n    "
        ...

    def copy(self: object, /, deep: bool):
        "\n    usage.xarray: 1\n    "
        ...

    def floor(self: object, /, *args: Literal["v", "t"]):
        "\n    usage.xarray: 1\n    "
        ...

    def ceil(self: object, /, *args: Literal["v", "t"]):
        "\n    usage.xarray: 1\n    "
        ...

    def round(self: object, /, *args: Literal["v", "t"]):
        "\n    usage.xarray: 1\n    "
        ...

    def __sub__(
        self: object,
        _0: Union[numpy.timedelta64, pandas._libs.tslibs.timestamps.Timestamp],
        /,
    ):
        "\n    usage.xarray: 3\n    "
        ...

    def to_series(self: object, /):
        "\n    usage.xarray: 7\n    usage.dask: 4\n    "
        ...

    def slice_indexer(
        self: object,
        /,
        start: Union[Literal["2001", "1999", "2000-01-01"], numpy.datetime64],
        end: Union[Literal["2002", "2005", "2000-01-10"], numpy.datetime64],
        step: None,
    ):
        "\n    usage.xarray: 4\n    "
        ...

    def get_indexer(
        self: object,
        /,
        target: numpy.ndarray,
        method: Union[Literal["nearest", "backfill", "pad"], None],
        tolerance: Union[Literal["6H", "12H"], None],
    ):
        "\n    usage.xarray: 7\n    "
        ...

    def __add__(self: object, _0: object, /):
        "\n    usage.xarray: 1\n    usage.dask: 7\n    "
        ...

    def get_loc(
        self: object,
        /,
        key: Union[Literal["2000-01-01"], numpy.datetime64],
        method: Union[None, Literal["nearest"]],
    ):
        "\n    usage.xarray: 3\n    "
        ...

    def min(self: object, /):
        "\n    usage.dask: 1\n    "
        ...

    def max(self: object, /):
        "\n    usage.dask: 1\n    "
        ...

    def shift(
        self: object,
        /,
        periods: int,
        freq: Union[None, Literal["W", "S"], pandas._libs.tslibs.timedeltas.Timedelta],
    ):
        "\n    usage.dask: 11\n    "
        ...

    def _maybe_cast_slice_bound(
        self: object,
        /,
        label: str,
        side: Literal["right", "left"],
        kind: Literal["loc"],
    ):
        "\n    usage.dask: 23\n    "
        ...

    def to_frame(self: object, /, name: Union[Literal["foo"], None]):
        "\n    usage.dask: 3\n    "
        ...

    def __gt__(self: object, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        "\n    usage.dask: 1\n    "
        ...

    def __le__(self: object, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        "\n    usage.dask: 1\n    "
        ...

    def tz_localize(self: object, /, *args: Literal["v", "t"]):
        "\n    usage.dask: 2\n    "
        ...
