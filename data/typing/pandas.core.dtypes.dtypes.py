from typing import *


class IntervalDtype:
    def __eq__(self: object, _0: Literal["O"], /):
        "\n    usage.xarray: 1\n    "
        ...


class CategoricalDtype:
    def __init__(categories: List[str]):
        "\n    usage.xarray: 2\n    usage.dask: 1\n    "
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
        "\n    usage.xarray: 1\n    usage.dask: 18\n    "
        ...

    def __ne__(
        self: object,
        _0: Union[pandas.core.dtypes.dtypes.CategoricalDtype, Literal["category"]],
        /,
    ):
        "\n    usage.dask: 5\n    "
        ...


class PeriodDtype:

    # usage.dask: 1
    __module__: ClassVar[object]

    # usage.dask: 1
    name: object

    # usage.dask: 1
    kind: object

    def __eq__(self: object, _0: Literal["O"], /):
        "\n    usage.xarray: 1\n    "
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
        "\n    usage.xarray: 1\n    usage.dask: 3\n    "
        ...
