from typing import *

# usage.pandas: 1
MaskedRecords: object

# usage.pandas: 1
mrecarray: object


def fromarrays(
    arraylist: Tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray],
    names: Tuple[Literal["float"], Literal["int"], Literal["str"]],
):
    """
    usage.pandas: 1
    """
    ...


class MaskedRecords:

    # usage.pandas: 1
    fill_value: object

    def __getitem__(self, _0: Literal["price", "date"], /):
        """
        usage.pandas: 2
        """
        ...
