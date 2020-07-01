from typing import *


class IntervalDtype:
    def __eq__(self: object, _0: Literal["O"], /):
        """
        usage.xarray: 1
        """
        ...


class CategoricalDtype:
    def __init__(categories: List[str]):
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
        self: object,
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
        self: object,
        _0: Union[pandas.core.dtypes.dtypes.CategoricalDtype, Literal["category"]],
        /,
    ):
        """
        usage.dask: 5
        """
        ...


class PeriodDtype:

    # usage.dask: 1
    __module__: ClassVar[object]

    # usage.dask: 1
    name: object

    # usage.dask: 1
    kind: object

    def __eq__(self: object, _0: Literal["O"], /):
        """
        usage.xarray: 1
        """
        ...


class DatetimeTZDtype:

    # usage.dask: 1
    __module__: ClassVar[object]

    # usage.dask: 1
    name: object

    # usage.dask: 1
    tz: object

    # usage.dask: 1
    kind: object

    def __eq__(
        self: object,
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
