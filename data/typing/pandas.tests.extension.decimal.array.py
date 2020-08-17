from typing import *


class DecimalArray:

    # usage.dask: 1
    __module__: ClassVar[object]

    @classmethod
    def _from_sequence(cls, /, scalars: List[decimal.Decimal]):
        """
        usage.dask: 3
        """
        ...


class DecimalDtype:

    # usage.dask: 1
    kind: object

    def __eq__(self, _0: Union[Type[object], numpy.dtype], /):
        """
        usage.dask: 1
        usage.pandas: 2
        """
        ...

    def __ne__(self, _0: numpy.dtype, /):
        """
        usage.pandas: 1
        """
        ...
