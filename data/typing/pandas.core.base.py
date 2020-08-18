from typing import *


class IndexOpsMixin:
    def max(self, /):
        """
        usage.dask: 18
        """
        ...

    def min(self, /):
        """
        usage.dask: 18
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

    def tolist(self, /):
        """
        usage.dask: 14
        """
        ...
