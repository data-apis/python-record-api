from typing import *


class Int32Dtype:
    def __init__(self, /):
        """
        usage.dask: 1
        """
        ...


class Int64Dtype:
    @classmethod
    def is_dtype(cls, /, dtype: pandas.core.series.Series):
        """
        usage.dask: 1
        """
        ...

    # usage.dask: 1
    kind: object


class IntegerArray:

    # usage.dask: 1
    __module__: ClassVar[object]
