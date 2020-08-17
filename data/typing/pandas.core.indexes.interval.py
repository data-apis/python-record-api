from typing import *


class IntervalIndex:

    # usage.xarray: 2
    dtype: object

    # usage.xarray: 1
    is_unique: object

    # usage.xarray: 1
    name: object

    # usage.xarray: 1
    shape: object

    # usage.xarray: 1
    values: object

    def __eq__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 4
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, None, None], /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, int, None], /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[int, None, int], /):
        """
        usage.xarray: 1
        """
        ...

    def __getitem__(
        self, _0: slice[Union[None, int], Union[int, None], Union[None, int]], /
    ):
        """
        usage.xarray: 3
        """
        ...

    def __gt__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 2
        """
        ...

    def get_indexer(self, /, target: numpy.ndarray, method: None, tolerance: None):
        """
        usage.xarray: 1
        """
        ...
