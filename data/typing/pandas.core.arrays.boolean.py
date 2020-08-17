from typing import *


class BooleanArray:

    # usage.dask: 1
    __module__: ClassVar[object]

    def __and__(self, _0: numpy.bool_, /):
        """
        usage.pandas: 1
        """
        ...

    def __eq__(self, _0: numpy.bool_, /):
        """
        usage.pandas: 1
        """
        ...

    def __ior__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    def __or__(self, _0: numpy.bool_, /):
        """
        usage.pandas: 1
        """
        ...

    def __radd__(self, _0: Union[numpy.bool_, numpy.ndarray], /):
        """
        usage.pandas: 2
        """
        ...

    def __rand__(self, _0: numpy.bool_, /):
        """
        usage.pandas: 1
        """
        ...

    def __rfloordiv__(self, _0: Union[numpy.bool_, numpy.ndarray], /):
        """
        usage.pandas: 2
        """
        ...

    def __rmod__(self, _0: Union[numpy.bool_, numpy.ndarray], /):
        """
        usage.pandas: 2
        """
        ...

    def __rmul__(self, _0: numpy.bool_, /):
        """
        usage.pandas: 2
        """
        ...

    def __ror__(self, _0: numpy.bool_, /):
        """
        usage.pandas: 1
        """
        ...

    def __rpow__(self, _0: Union[numpy.bool_, numpy.ndarray], /):
        """
        usage.pandas: 2
        """
        ...

    def __rsub__(self, _0: Union[numpy.bool_, numpy.ndarray], /):
        """
        usage.pandas: 2
        """
        ...

    def __rtruediv__(self, _0: Union[numpy.bool_, numpy.ndarray], /):
        """
        usage.pandas: 2
        """
        ...

    def __rxor__(self, _0: numpy.bool_, /):
        """
        usage.pandas: 1
        """
        ...

    def __xor__(self, _0: numpy.bool_, /):
        """
        usage.pandas: 1
        """
        ...


class BooleanDtype:

    # usage.dask: 1
    kind: object

    @overload
    def __eq__(self, _0: Union[numpy.dtype, Type[numpy.object_]], /):
        """
        usage.pandas: 7
        """
        ...

    @overload
    def __eq__(self, _0: pandas.core.arrays.boolean.BooleanDtype, /):
        """
        usage.dask: 6
        """
        ...

    def __eq__(
        self,
        _0: Union[
            pandas.core.arrays.boolean.BooleanDtype, numpy.dtype, Type[numpy.object_]
        ],
        /,
    ):
        """
        usage.dask: 6
        usage.pandas: 7
        """
        ...

    def __ne__(self, _0: numpy.dtype, /):
        """
        usage.pandas: 1
        """
        ...
