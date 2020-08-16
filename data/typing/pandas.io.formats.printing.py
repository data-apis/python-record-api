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
