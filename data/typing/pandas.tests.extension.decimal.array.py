from typing import *


class DecimalArray:

    # usage.dask: 1
    __module__: ClassVar[object]

    @overload
    @classmethod
    def _from_sequence(cls, /, scalars: List[decimal.Decimal]):
        """
        usage.dask: 2
        """
        ...

    @overload
    @classmethod
    def _from_sequence(
        cls,
        /,
        scalars: List[decimal.Decimal],
        dtype: pandas.tests.extension.decimal.array.DecimalDtype,
    ):
        """
        usage.dask: 1
        """
        ...

    @classmethod
    def _from_sequence(
        cls,
        /,
        scalars: List[decimal.Decimal],
        dtype: pandas.tests.extension.decimal.array.DecimalDtype = ...,
    ):
        """
        usage.dask: 3
        """
        ...


class DecimalDtype:

    # usage.dask: 1
    kind: object

    @overload
    def __eq__(self, _0: numpy.dtype, /):
        """
        usage.pandas: 2
        """
        ...

    @overload
    def __eq__(self, _0: Type[object], /):
        """
        usage.dask: 1
        """
        ...

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
