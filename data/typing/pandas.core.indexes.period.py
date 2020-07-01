from typing import *


def period_range(
    start: Literal[("1970-01-01", "2011-01-01", "2000-01-01", "1/1/2001", "2000")],
    periods: int = ...,
    name: Union[Literal["foo"], None] = ...,
):
    "\n    usage.xarray: 4\n    usage.dask: 11\n    "
    ...


class PeriodIndex:
    def __init__(
        data: List[Literal["1970-01-01"]], freq: Literal["d"], name: Literal["foo"]
    ):
        "\n    usage.dask: 1\n    "
        ...

    # usage.dask: 1
    __module__: ClassVar[object]

    # usage.dask: 2
    __name__: ClassVar[object]

    # usage.xarray: 1
    # usage.dask: 8
    name: object

    # usage.xarray: 1
    # usage.dask: 3
    dtype: object

    # usage.dask: 1
    array: object

    # usage.dask: 1
    is_monotonic_increasing: object

    # usage.dask: 3
    freq: object

    # usage.dask: 1
    names: object

    def __getitem__(
        self: object,
        _0: Union[int, slice[Union[int, None], Union[None, int], Union[int, None]]],
        /,
    ):
        "\n    usage.xarray: 6\n    usage.dask: 5\n    "
        ...

    def astype(self: object, /, dtype: Literal["object"]):
        "\n    usage.xarray: 1\n    "
        ...

    def shift(self: object, /, periods: int):
        "\n    usage.dask: 1\n    "
        ...

    def _maybe_cast_slice_bound(
        self: object,
        /,
        label: Literal[("2015", "2012-05", "2011", "2011-01", "2011-01-02")],
        side: Literal[("right", "left")],
        kind: Literal["loc"],
    ):
        "\n    usage.dask: 10\n    "
        ...
