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
    """
    usage.dask: 17
    """
    ...


class PrettyDict:
    def __iter__(self: object, /):
        """
        usage.dask: 1
        """
        ...

    def __contains__(self: object, _0: int, /):
        """
        usage.dask: 1
        """
        ...
