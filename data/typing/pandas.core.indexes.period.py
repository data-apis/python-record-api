from typing import *


@overload
def period_range(start: Literal["2000-01-01"], periods: int, freq: Literal["B"]):
    """
    usage.dask: 1
    usage.xarray: 1
    """
    ...


@overload
def period_range(start: Literal["2000-01-01"], periods: int):
    """
    usage.xarray: 2
    """
    ...


@overload
def period_range(start: Literal["2000"], periods: int, freq: Literal["B"]):
    """
    usage.xarray: 1
    """
    ...


@overload
def period_range(
    start: Literal["1/1/2001"], end: Literal["12/1/2004"], freq: Literal["A"]
):
    """
    usage.dask: 1
    """
    ...


@overload
def period_range(
    start: Literal["1970-01-01"],
    periods: int,
    freq: pandas._libs.tslibs.offsets.YearEnd,
    name: None,
):
    """
    usage.dask: 1
    """
    ...


@overload
def period_range(
    start: Literal["1970-01-01"],
    periods: int,
    freq: pandas._libs.tslibs.offsets.BusinessDay,
    name: None,
):
    """
    usage.dask: 1
    """
    ...


@overload
def period_range(start: Literal["2000-01-01"], periods: int, freq: Literal["D"]):
    """
    usage.dask: 1
    """
    ...


@overload
def period_range(
    start: Literal["1970-01-01"],
    periods: int,
    freq: pandas._libs.tslibs.offsets.Day,
    name: None,
):
    """
    usage.dask: 1
    """
    ...


@overload
def period_range(start: Literal["2000-01-01"], periods: int, freq: Literal["H"]):
    """
    usage.dask: 1
    """
    ...


@overload
def period_range(
    start: Literal["1970-01-01"],
    periods: int,
    freq: pandas._libs.tslibs.offsets.Hour,
    name: None,
):
    """
    usage.dask: 1
    """
    ...


@overload
def period_range(start: Literal["2011-01-01"], periods: int, freq: Literal["H"]):
    """
    usage.dask: 1
    """
    ...


@overload
def period_range(start: Literal["2011-01-01"], periods: int, freq: Literal["D"]):
    """
    usage.dask: 1
    """
    ...


@overload
def period_range(
    start: Literal["1970-01-01"],
    periods: int,
    freq: pandas._libs.tslibs.offsets.Day,
    name: Literal["foo"],
):
    """
    usage.dask: 1
    """
    ...


def period_range(
    start: Literal["1970-01-01", "2011-01-01", "2000-01-01", "1/1/2001", "2000"],
    periods: int = ...,
    name: Union[Literal["foo"], None] = ...,
):
    """
    usage.dask: 11
    usage.xarray: 4
    """
    ...


class PeriodIndex:

    # usage.dask: 1
    __module__: ClassVar[object]

    # usage.dask: 2
    __name__: ClassVar[object]

    # usage.dask: 1
    array: object

    # usage.dask: 3
    # usage.xarray: 1
    dtype: object

    # usage.dask: 3
    freq: object

    # usage.dask: 8
    # usage.xarray: 1
    name: object

    # usage.dask: 1
    names: object

    def __add__(
        self,
        _0: Union[numpy.timedelta64, numpy.ndarray, numpy.datetime64, numpy.int64],
        /,
    ):
        """
        usage.pandas: 20
        """
        ...

    def __eq__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 8
        """
        ...

    def __ge__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 8
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, int, None], /):
        """
        usage.xarray: 2
        """
        ...

    @overload
    def __getitem__(self, _0: slice[int, None, int], /):
        """
        usage.xarray: 2
        """
        ...

    @overload
    def __getitem__(self, _0: slice[int, int, int], /):
        """
        usage.dask: 1
        usage.xarray: 1
        """
        ...

    @overload
    def __getitem__(self, _0: int, /):
        """
        usage.dask: 4
        usage.xarray: 1
        """
        ...

    def __getitem__(
        self,
        _0: Union[int, slice[Union[int, None], Union[None, int], Union[int, None]]],
        /,
    ):
        """
        usage.dask: 5
        usage.xarray: 6
        """
        ...

    def __gt__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 6
        """
        ...

    def __iadd__(self, _0: Union[numpy.timedelta64, numpy.ndarray], /):
        """
        usage.pandas: 7
        """
        ...

    def __isub__(self, _0: Union[numpy.timedelta64, numpy.ndarray], /):
        """
        usage.pandas: 6
        """
        ...

    def __le__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 8
        """
        ...

    def __lt__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 2
        """
        ...

    def __ne__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 6
        """
        ...

    def __radd__(
        self, _0: Union[numpy.timedelta64, numpy.datetime64, numpy.ndarray], /
    ):
        """
        usage.pandas: 11
        """
        ...

    def __rsub__(
        self, _0: Union[numpy.timedelta64, numpy.datetime64, numpy.ndarray], /
    ):
        """
        usage.pandas: 10
        """
        ...

    def __sub__(self, _0: Union[numpy.timedelta64, numpy.datetime64, numpy.ndarray], /):
        """
        usage.pandas: 18
        """
        ...

    def shift(self, /, periods: int):
        """
        usage.dask: 1
        """
        ...
