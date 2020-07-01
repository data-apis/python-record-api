from typing import *


class IndexOpsMixin:
    def to_numpy(self: object, /):
        """
        usage.xarray: 2
        """
        ...

    def factorize(self: object, /):
        """
        usage.xarray: 4
        """
        ...

    def tolist(self: object, /):
        """
        usage.dask: 14
        """
        ...

    def min(self: object, /):
        """
        usage.dask: 14
        """
        ...

    def max(self: object, /):
        """
        usage.dask: 14
        """
        ...

    def searchsorted(self: object, /, value: numpy.ndarray):
        """
        usage.dask: 2
        """
        ...

    def nunique(self: object, /):
        """
        usage.dask: 4
        """
        ...
