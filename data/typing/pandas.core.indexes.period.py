from typing import *


def period_range(
    start: Literal["1970-01-01", "2011-01-01", "2000-01-01", "1/1/2001", "2000"],
    periods: int = ...,
    name: Union[Literal["foo"], None] = ...,
):
    """
    usage.xarray: 4
    usage.dask: 11
    """
    ...


class PeriodIndex:
    def __init__(
        self,
        /,
        data: List[Literal["1970-01-01"]],
        freq: Literal["d"],
        name: Literal["foo"],
    ):
        """
        usage.dask: 1
        """
        ...

    # usage.dask: 1
    __module__: ClassVar[object]

    # usage.dask: 2
    __name__: ClassVar[object]

    # usage.dask: 1
    array: object

    # usage.xarray: 1
    # usage.dask: 3
    dtype: object

    # usage.dask: 3
    freq: object

    # usage.dask: 1
    is_monotonic_increasing: object

    # usage.xarray: 1
    # usage.dask: 8
    name: object

    # usage.dask: 1
    names: object

    def __getitem__(
        self,
        _0: Union[int, slice[Union[int, None], Union[None, int], Union[int, None]]],
        /,
    ):
        """
        usage.xarray: 6
        usage.dask: 5
        """
        ...

    def _maybe_cast_slice_bound(
        self,
        /,
        label: Literal["2015", "2012-05", "2011", "2011-01", "2011-01-02"],
        side: Literal["right", "left"],
        kind: Literal["loc"],
    ):
        """
        usage.dask: 10
        """
        ...

    def astype(self, /, dtype: Literal["object"]):
        """
        usage.xarray: 1
        """
        ...

    def shift(self, /, periods: int):
        """
        usage.dask: 1
        """
        ...
