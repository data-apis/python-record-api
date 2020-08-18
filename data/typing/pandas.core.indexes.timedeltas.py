from typing import *


@overload
def timedelta_range(start: int, periods: int):
    """
    usage.xarray: 1
    """
    ...


@overload
def timedelta_range(start: Literal["1 days"], periods: int, freq: Literal["D"]):
    """
    usage.dask: 1
    """
    ...


@overload
def timedelta_range(start: Literal["1 day"], periods: int, freq: Literal["T"]):
    """
    usage.dask: 1
    """
    ...


@overload
def timedelta_range(
    start: numpy.timedelta64,
    periods: int,
    freq: pandas._libs.tslibs.offsets.Minute,
    name: None,
):
    """
    usage.dask: 1
    """
    ...


@overload
def timedelta_range(start: Literal["1 day"], periods: int, freq: Literal["D"]):
    """
    usage.dask: 1
    """
    ...


@overload
def timedelta_range(
    start: numpy.timedelta64,
    periods: int,
    freq: pandas._libs.tslibs.offsets.Day,
    name: None,
):
    """
    usage.dask: 1
    """
    ...


@overload
def timedelta_range(start: Literal["1 day"], periods: int, freq: Literal["H"]):
    """
    usage.dask: 1
    """
    ...


@overload
def timedelta_range(
    start: numpy.timedelta64,
    periods: int,
    freq: pandas._libs.tslibs.offsets.Hour,
    name: None,
):
    """
    usage.dask: 1
    """
    ...


@overload
def timedelta_range(
    start: numpy.timedelta64,
    periods: int,
    freq: pandas._libs.tslibs.offsets.Day,
    name: Literal["foo"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def timedelta_range(
    start: numpy.timedelta64, periods: int, freq: None, name: Literal["timedelta"]
):
    """
    usage.dask: 1
    """
    ...


def timedelta_range(
    start: Union[Literal["1 day", "1 days"], numpy.timedelta64, int],
    periods: int,
    freq: Union[
        None,
        Literal["H", "D", "T"],
        pandas._libs.tslibs.offsets.Hour,
        pandas._libs.tslibs.offsets.Minute,
        pandas._libs.tslibs.offsets.Day,
    ] = ...,
    name: Union[Literal["timedelta", "foo"], None] = ...,
):
    """
    usage.dask: 9
    usage.xarray: 1
    """
    ...


class TimedeltaIndex:

    # usage.dask: 1
    __module__: ClassVar[object]

    # usage.dask: 2
    __name__: ClassVar[object]

    # usage.dask: 1
    array: object

    # usage.dask: 3
    # usage.xarray: 6
    dtype: object

    # usage.dask: 3
    freq: object

    # usage.dask: 9
    # usage.xarray: 1
    name: object

    # usage.dask: 1
    names: object

    # usage.xarray: 4
    values: object

    @overload
    def __add__(self, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def __add__(self, _0: xarray.coding.cftimeindex.CFTimeIndex, /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def __add__(self, _0: Union[numpy.ndarray, numpy.timedelta64, numpy.datetime64], /):
        """
        usage.pandas: 22
        """
        ...

    def __add__(
        self,
        _0: Union[
            numpy.datetime64,
            numpy.timedelta64,
            numpy.ndarray,
            pandas._libs.tslibs.timestamps.Timestamp,
            xarray.coding.cftimeindex.CFTimeIndex,
        ],
        /,
    ):
        """
        usage.pandas: 22
        usage.xarray: 2
        """
        ...

    def __eq__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 5
        """
        ...

    def __floordiv__(self, _0: numpy.timedelta64, /):
        """
        usage.pandas: 21
        """
        ...

    def __ge__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    @overload
    def __getitem__(self, _0: int, /):
        """
        usage.dask: 4
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
    def __getitem__(self, _0: numpy.ndarray, /):
        """
        usage.xarray: 1
        """
        ...

    def __getitem__(self, _0: Union[int, numpy.ndarray, slice[int, int, int]], /):
        """
        usage.dask: 5
        usage.xarray: 4
        """
        ...

    def __gt__(self, _0: numpy.timedelta64, /):
        """
        usage.pandas: 4
        """
        ...

    def __iadd__(self, _0: Union[numpy.ndarray, numpy.timedelta64], /):
        """
        usage.pandas: 2
        """
        ...

    def __isub__(self, _0: Union[numpy.ndarray, numpy.timedelta64], /):
        """
        usage.pandas: 2
        """
        ...

    def __le__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 2
        """
        ...

    def __lt__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    def __mod__(self, _0: numpy.timedelta64, /):
        """
        usage.pandas: 6
        """
        ...

    def __mul__(self, _0: Union[numpy.ndarray, numpy.timedelta64, numpy.int64], /):
        """
        usage.pandas: 18
        """
        ...

    def __ne__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    def __pow__(self, _0: numpy.timedelta64, /):
        """
        usage.pandas: 4
        """
        ...

    @overload
    def __radd__(self, _0: xarray.coding.cftimeindex.CFTimeIndex, /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def __radd__(self, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def __radd__(
        self, _0: Union[numpy.ndarray, numpy.datetime64, numpy.timedelta64], /
    ):
        """
        usage.pandas: 18
        """
        ...

    def __radd__(
        self,
        _0: Union[
            numpy.timedelta64,
            numpy.datetime64,
            numpy.ndarray,
            xarray.coding.cftimeindex.CFTimeIndex,
            pandas._libs.tslibs.timestamps.Timestamp,
        ],
        /,
    ):
        """
        usage.pandas: 18
        usage.xarray: 2
        """
        ...

    def __rfloordiv__(self, _0: numpy.timedelta64, /):
        """
        usage.pandas: 7
        """
        ...

    def __rmod__(self, _0: numpy.timedelta64, /):
        """
        usage.pandas: 5
        """
        ...

    def __rmul__(self, _0: Union[numpy.ndarray, numpy.timedelta64, numpy.int64], /):
        """
        usage.pandas: 14
        """
        ...

    def __rpow__(self, _0: numpy.timedelta64, /):
        """
        usage.pandas: 4
        """
        ...

    @overload
    def __rsub__(self, _0: xarray.coding.cftimeindex.CFTimeIndex, /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def __rsub__(
        self, _0: Union[numpy.ndarray, numpy.datetime64, numpy.timedelta64], /
    ):
        """
        usage.pandas: 16
        """
        ...

    def __rsub__(
        self,
        _0: Union[
            numpy.timedelta64,
            numpy.datetime64,
            numpy.ndarray,
            xarray.coding.cftimeindex.CFTimeIndex,
        ],
        /,
    ):
        """
        usage.pandas: 16
        usage.xarray: 1
        """
        ...

    def __rtruediv__(self, _0: Union[numpy.ndarray, numpy.timedelta64], /):
        """
        usage.pandas: 19
        """
        ...

    def __sub__(self, _0: Union[numpy.ndarray, numpy.datetime64, numpy.timedelta64], /):
        """
        usage.pandas: 18
        """
        ...

    @overload
    def __truediv__(self, _0: numpy.timedelta64, /):
        """
        usage.xarray: 2
        """
        ...

    @overload
    def __truediv__(self, _0: Union[numpy.ndarray, numpy.timedelta64], /):
        """
        usage.pandas: 21
        """
        ...

    def __truediv__(self, _0: Union[numpy.timedelta64, numpy.ndarray], /):
        """
        usage.pandas: 21
        usage.xarray: 2
        """
        ...

    def copy(self, /, deep: bool):
        """
        usage.xarray: 1
        """
        ...

    def equals(self, /, other: pandas.core.indexes.timedeltas.TimedeltaIndex):
        """
        usage.xarray: 4
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

    @overload
    def shift(self, /, periods: int, freq: Literal["S"]):
        """
        usage.dask: 3
        """
        ...

    @overload
    def shift(self, /, periods: int, freq: pandas._libs.tslibs.timedeltas.Timedelta):
        """
        usage.dask: 3
        """
        ...

    @overload
    def shift(self, /, periods: int, freq: None):
        """
        usage.dask: 2
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
