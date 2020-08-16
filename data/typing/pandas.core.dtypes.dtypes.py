from typing import *


class CategoricalDtype:

    # usage.dask: 1
    __module__: ClassVar[object]

    # usage.dask: 10
    categories: object

    # usage.dask: 1
    # usage.sklearn: 6
    kind: object

    # usage.sklearn: 1
    name: object

    # usage.dask: 4
    ordered: object

    def __eq__(
        self,
        _0: Union[
            pandas.core.dtypes.dtypes.CategoricalDtype,
            numpy.dtype,
            Literal["category", "O"],
            type,
        ],
        /,
    ):
        """
        usage.dask: 19
        usage.pandas: 19
        usage.sklearn: 6
        usage.xarray: 1
        """
        ...

    def __ne__(
        self,
        _0: Union[
            Literal["category"], pandas.core.dtypes.dtypes.CategoricalDtype, numpy.dtype
        ],
        /,
    ):
        """
        usage.dask: 5
        usage.pandas: 1
        """
        ...


class DatetimeTZDtype:

    # usage.dask: 1
    __module__: ClassVar[object]

    # usage.dask: 1
    kind: object

    # usage.dask: 1
    name: object

    # usage.dask: 1
    tz: object

    def __eq__(
        self,
        _0: Union[
            type, pandas.core.dtypes.dtypes.DatetimeTZDtype, numpy.dtype, Literal["O"]
        ],
        /,
    ):
        """
        usage.dask: 3
        usage.pandas: 24
        usage.xarray: 1
        """
        ...

    def __ne__(self, _0: numpy.dtype, /):
        """
        usage.pandas: 1
        """
        ...


class IntervalDtype:
    def __eq__(self, _0: Union[type, numpy.dtype, Literal["O"]], /):
        """
        usage.pandas: 13
        usage.xarray: 1
        """
        ...

    def __ne__(self, _0: numpy.dtype, /):
        """
        usage.pandas: 1
        """
        ...


class PeriodDtype:

    # usage.dask: 1
    __module__: ClassVar[object]

    # usage.dask: 1
    kind: object

    # usage.dask: 1
    name: object

    def __eq__(self, _0: Union[type, numpy.dtype, Literal["O"]], /):
        """
        usage.pandas: 22
        usage.xarray: 1
        """
        ...

    def __ne__(self, _0: numpy.dtype, /):
        """
        usage.pandas: 1
        """
        ...
