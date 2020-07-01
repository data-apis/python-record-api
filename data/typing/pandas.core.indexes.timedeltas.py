from typing import *


def timedelta_range(
    start: Union[Literal[("1 day", "1 days")], numpy.timedelta64, int],
    periods: int = ...,
    end: Literal["30 days"] = ...,
    freq: Union[
        pandas.tseries.offsets.Day,
        pandas.tseries.offsets.Minute,
        pandas.tseries.offsets.Hour,
        Literal[("H", "D", "T", "6H")],
        None,
    ] = ...,
):
    "\n    usage.xarray: 2\n    usage.dask: 9\n    "
    ...


class TimedeltaIndex:
    def __init__(data: List[numpy.timedelta64], name: Literal[("timedelta", "foo")]):
        "\n    usage.dask: 2\n    "
        ...

    # usage.dask: 1
    __module__: ClassVar[object]

    # usage.dask: 2
    __name__: ClassVar[object]

    # usage.xarray: 4
    # usage.dask: 3
    dtype: object

    # usage.xarray: 1
    # usage.dask: 9
    name: object

    # usage.xarray: 4
    values: object

    # usage.dask: 1
    array: object

    # usage.dask: 1
    is_monotonic_increasing: object

    # usage.dask: 3
    freq: object

    # usage.dask: 1
    names: object

    def copy(self: object, /, deep: bool):
        "\n    usage.xarray: 1\n    "
        ...

    def floor(self: object, /, *args: Literal[("v", "t")]):
        "\n    usage.xarray: 1\n    "
        ...

    def ceil(self: object, /, *args: Literal[("v", "t")]):
        "\n    usage.xarray: 1\n    "
        ...

    def round(self: object, /, *args: Literal[("v", "t")]):
        "\n    usage.xarray: 1\n    "
        ...

    def __truediv__(self: object, _0: numpy.timedelta64, /):
        "\n    usage.xarray: 1\n    "
        ...

    def __add__(self: object, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        "\n    usage.xarray: 1\n    "
        ...

    def __getitem__(
        self: object, _0: Union[int, numpy.ndarray, slice[int, int, int]], /
    ):
        "\n    usage.xarray: 4\n    usage.dask: 5\n    "
        ...

    def get_indexer(
        self: object, /, target: numpy.ndarray, method: None, tolerance: None
    ):
        "\n    usage.xarray: 1\n    "
        ...

    def get_loc(
        self: object,
        /,
        key: pandas._libs.tslibs.timedeltas.Timedelta,
        method: None,
        tolerance: None,
    ):
        "\n    usage.xarray: 1\n    "
        ...

    def shift(
        self: object,
        /,
        periods: int,
        freq: Union[None, Literal["S"], pandas._libs.tslibs.timedeltas.Timedelta],
    ):
        "\n    usage.dask: 8\n    "
        ...
