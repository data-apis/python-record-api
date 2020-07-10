from typing import *


class Period:
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
        usage.xarray: 2
        usage.dask: 2
        """
        ...

    def __ge__(self, _0: pandas._libs.tslibs.period.Period, /):
        """
        usage.dask: 3
        """
        ...

    def __le__(self, _0: pandas._libs.tslibs.period.Period, /):
        """
        usage.dask: 3
        """
        ...
