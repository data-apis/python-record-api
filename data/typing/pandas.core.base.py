from typing import *


class IndexOpsMixin:
    def to_numpy(self: object, /):
        "\n    usage.xarray: 2\n    "
        ...

    def factorize(self: object, /):
        "\n    usage.xarray: 4\n    "
        ...

    def tolist(self: object, /):
        "\n    usage.dask: 14\n    "
        ...

    def min(self: object, /):
        "\n    usage.dask: 14\n    "
        ...

    def max(self: object, /):
        "\n    usage.dask: 14\n    "
        ...

    def searchsorted(self: object, /, value: numpy.ndarray):
        "\n    usage.dask: 2\n    "
        ...

    def nunique(self: object, /):
        "\n    usage.dask: 4\n    "
        ...
