from typing import *


def pprint_thing(
    thing: Union[
        numpy.dtype,
        int,
        pandas.core.dtypes.dtypes.CategoricalDtype,
        Literal["z", "C", "y", "x"],
        Tuple[Literal["C"], Literal["count", "sum"]],
    ]
):
    "\n    usage.dask: 17\n    "
    ...


class PrettyDict:
    def __iter__(self: object, /):
        "\n    usage.dask: 1\n    "
        ...

    def __contains__(self: object, _0: int, /):
        "\n    usage.dask: 1\n    "
        ...
