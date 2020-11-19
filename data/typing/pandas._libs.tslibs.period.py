from typing import *


class Period:

    # usage.statsmodels: 2
    day: object

    # usage.statsmodels: 2
    month: object

    # usage.statsmodels: 2
    year: object

    @overload
    def __add__(self, _0: int, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __add__(self, _0: pandas._libs.tslibs.offsets.MonthEnd, /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __add__(self, _0: numpy.timedelta64, /):
        """
        usage.pandas: 9
        """
        ...

    def __add__(
        self, _0: Union[numpy.timedelta64, int, pandas._libs.tslibs.offsets.MonthEnd], /
    ):
        """
        usage.pandas: 9
        usage.statsmodels: 3
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
        usage.statsmodels: 2
        """
        ...

    def __eq__(
        self,
        _0: Union[
            pandas._libs.tslibs.period.Period,
            numpy.ndarray,
            xarray.core.variable.Variable,
        ],
        /,
    ):
        """
        usage.dask: 2
        usage.statsmodels: 2
        usage.xarray: 2
        """
        ...

    @overload
    def __ge__(self, _0: pandas._libs.tslibs.period.Period, /):
        """
        usage.dask: 3
        usage.statsmodels: 2
        """
        ...

    @overload
    def __ge__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    def __ge__(self, _0: Union[pandas._libs.tslibs.period.Period, numpy.ndarray], /):
        """
        usage.dask: 3
        usage.pandas: 1
        usage.statsmodels: 2
        """
        ...

    @overload
    def __gt__(self, _0: pandas._libs.tslibs.period.Period, /):
        """
        usage.dask: 1
        usage.statsmodels: 2
        """
        ...

    @overload
    def __gt__(self, _0: pandas.core.indexes.period.PeriodIndex, /):
        """
        usage.statsmodels: 1
        """
        ...

    def __gt__(
        self,
        _0: Union[
            pandas._libs.tslibs.period.Period, pandas.core.indexes.period.PeriodIndex
        ],
        /,
    ):
        """
        usage.dask: 1
        usage.statsmodels: 3
        """
        ...

    def __le__(self, _0: pandas._libs.tslibs.period.Period, /):
        """
        usage.dask: 3
        usage.statsmodels: 2
        """
        ...

    @overload
    def __lt__(self, _0: pandas._libs.tslibs.period.Period, /):
        """
        usage.dask: 1
        usage.statsmodels: 2
        """
        ...

    @overload
    def __lt__(self, _0: pandas.core.indexes.period.PeriodIndex, /):
        """
        usage.statsmodels: 1
        """
        ...

    def __lt__(
        self,
        _0: Union[
            pandas._libs.tslibs.period.Period, pandas.core.indexes.period.PeriodIndex
        ],
        /,
    ):
        """
        usage.dask: 1
        usage.statsmodels: 3
        """
        ...

    def __radd__(self, _0: numpy.timedelta64, /):
        """
        usage.pandas: 8
        """
        ...

    def __rmod__(self, _0: Literal["%s"], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __sub__(self, _0: int, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __sub__(self, _0: numpy.timedelta64, /):
        """
        usage.pandas: 9
        """
        ...

    def __sub__(self, _0: Union[numpy.timedelta64, int], /):
        """
        usage.pandas: 9
        usage.statsmodels: 1
        """
        ...

    def strftime(self, _0: Literal["%m-%d-%Y"], /):
        """
        usage.statsmodels: 4
        """
        ...

    def to_timestamp(self, /):
        """
        usage.statsmodels: 1
        """
        ...
