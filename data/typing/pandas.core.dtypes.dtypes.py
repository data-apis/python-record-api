from typing import *


class CategoricalDtype:
    def __init__(self, /, categories: List[str]):
        """
        usage.xarray: 2
        """
        ...

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
            Literal["O", "category"],
            type,
            numpy.dtype,
            pandas.core.dtypes.dtypes.CategoricalDtype,
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
            numpy.dtype, pandas.core.dtypes.dtypes.CategoricalDtype, Literal["category"]
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
            Literal["O"], pandas.core.dtypes.dtypes.DatetimeTZDtype, numpy.dtype, type
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
    def __eq__(self, _0: Union[Literal["O"], type, numpy.dtype], /):
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

    def __eq__(self, _0: Union[Literal["O"], type, numpy.dtype], /):
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
