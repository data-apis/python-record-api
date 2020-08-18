from typing import *


class Period:
    def __add__(self, _0: numpy.timedelta64, /):
        """
        usage.pandas: 9
        """
        ...

    @overload
    def __eq__(self, _0: xarray.core.variable.Variable, /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def __eq__(self, _0: numpy.ndarray, /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def __eq__(self, _0: pandas._libs.tslibs.period.Period, /):
        """
        usage.dask: 2
        """
        ...

    def __eq__(
        self,
        _0: Union[
            pandas._libs.tslibs.period.Period,
            xarray.core.variable.Variable,
            numpy.ndarray,
        ],
        /,
    ):
        """
        usage.dask: 2
        usage.xarray: 2
        """
        ...

    @overload
    def __ge__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    @overload
    def __ge__(self, _0: pandas._libs.tslibs.period.Period, /):
        """
        usage.dask: 3
        """
        ...

    def __ge__(self, _0: Union[pandas._libs.tslibs.period.Period, numpy.ndarray], /):
        """
        usage.dask: 3
        usage.pandas: 1
        """
        ...

    def __gt__(self, _0: pandas._libs.tslibs.period.Period, /):
        """
        usage.dask: 1
        """
        ...

    def __le__(self, _0: pandas._libs.tslibs.period.Period, /):
        """
        usage.dask: 3
        """
        ...

    def __lt__(self, _0: pandas._libs.tslibs.period.Period, /):
        """
        usage.dask: 1
        """
        ...

    def __radd__(self, _0: numpy.timedelta64, /):
        """
        usage.pandas: 8
        """
        ...

    def __sub__(self, _0: numpy.timedelta64, /):
        """
        usage.pandas: 9
        """
        ...
