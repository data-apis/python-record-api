from typing import *


class CategoricalDtype:
    def __init__(self, /, categories: List[str]):
        """
        usage.xarray: 2
        usage.dask: 1
        """
        ...

    # usage.dask: 1
    __module__: ClassVar[object]

    # usage.dask: 7
    categories: object

    # usage.dask: 1
    kind: object

    # usage.dask: 1
    ordered: object

    def __eq__(
        self,
        _0: Union[
            pandas.core.dtypes.dtypes.CategoricalDtype,
            Literal["category", "O"],
            Type[object],
        ],
        /,
    ):
        """
        usage.xarray: 1
        usage.dask: 18
        """
        ...

    def __ne__(
        self,
        _0: Union[pandas.core.dtypes.dtypes.CategoricalDtype, Literal["category"]],
        /,
    ):
        """
        usage.dask: 5
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
            Type[object], pandas.core.dtypes.dtypes.DatetimeTZDtype, Literal["O"]
        ],
        /,
    ):
        """
        usage.xarray: 1
        usage.dask: 3
        """
        ...


class IntervalDtype:
    def __eq__(self, _0: Literal["O"], /):
        """
        usage.xarray: 1
        """
        ...


class PeriodDtype:

    # usage.dask: 1
    __module__: ClassVar[object]

    # usage.dask: 1
    kind: object

    # usage.dask: 1
    name: object

    def __eq__(self, _0: Literal["O"], /):
        """
        usage.xarray: 1
        """
        ...
