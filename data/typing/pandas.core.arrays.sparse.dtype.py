from typing import *


class SparseDtype:

    # usage.dask: 1
    # usage.sklearn: 1
    kind: object

    # usage.sklearn: 1
    name: object

    def __eq__(
        self,
        _0: Union[Type[numpy.object_], numpy.dtype, Literal["Sparse[uint8, 0]"]],
        /,
    ):
        """
        usage.dask: 2
        usage.pandas: 6
        """
        ...

    def __ne__(self, _0: numpy.dtype, /):
        """
        usage.pandas: 2
        """
        ...
