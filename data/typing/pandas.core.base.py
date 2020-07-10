from typing import *


class IndexOpsMixin:
    def factorize(self, /):
        """
        usage.xarray: 4
        """
        ...

    def max(self, /):
        """
        usage.dask: 14
        """
        ...

    def min(self, /):
        """
        usage.dask: 14
        """
        ...

    def nunique(self, /):
        """
        usage.dask: 4
        """
        ...

    def searchsorted(self, /, value: numpy.ndarray):
        """
        usage.dask: 2
        """
        ...

    def to_numpy(self, /):
        """
        usage.xarray: 2
        """
        ...

    def tolist(self, /):
        """
        usage.dask: 14
        """
        ...
