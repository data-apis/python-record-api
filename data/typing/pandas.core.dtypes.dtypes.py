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

    @overload
    def __eq__(self, _0: Literal["O"], /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def __eq__(self, _0: Union[numpy.dtype, type], /):
        """
        usage.pandas: 19
        """
        ...

    @overload
    def __eq__(self, _0: Literal["category"], /):
        """
        usage.dask: 10
        """
        ...

    @overload
    def __eq__(self, _0: Type[object], /):
        """
        usage.dask: 3
        """
        ...

    @overload
    def __eq__(self, _0: pandas.core.dtypes.dtypes.CategoricalDtype, /):
        """
        usage.dask: 4
        usage.sklearn: 6
        """
        ...

    def __eq__(
        self,
        _0: Union[
            pandas.core.dtypes.dtypes.CategoricalDtype,
            numpy.dtype,
            Literal["category", "O"],
            type,
            Type[object],
        ],
        /,
    ):
        """
        usage.dask: 17
        usage.pandas: 19
        usage.sklearn: 6
        usage.xarray: 1
        """
        ...

    @overload
    def __ne__(self, _0: numpy.dtype, /):
        """
        usage.pandas: 1
        """
        ...

    @overload
    def __ne__(self, _0: Literal["category"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __ne__(self, _0: pandas.core.dtypes.dtypes.CategoricalDtype, /):
        """
        usage.dask: 4
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

    @overload
    def __eq__(self, _0: Literal["O"], /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def __eq__(self, _0: Union[numpy.dtype, type], /):
        """
        usage.pandas: 24
        """
        ...

    @overload
    def __eq__(self, _0: Type[object], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __eq__(self, _0: pandas.core.dtypes.dtypes.DatetimeTZDtype, /):
        """
        usage.dask: 2
        """
        ...

    def __eq__(
        self,
        _0: Union[
            Type[object],
            type,
            pandas.core.dtypes.dtypes.DatetimeTZDtype,
            numpy.dtype,
            Literal["O"],
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
    @overload
    def __eq__(self, _0: Literal["O"], /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def __eq__(self, _0: Union[numpy.dtype, type], /):
        """
        usage.pandas: 13
        """
        ...

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

    @overload
    def __eq__(self, _0: Literal["O"], /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def __eq__(self, _0: Union[numpy.dtype, type], /):
        """
        usage.pandas: 22
        """
        ...

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
