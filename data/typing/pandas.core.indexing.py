from typing import *


class _LocIndexer:
    def __getitem__(self: object, _0: object, /):
        """
        usage.xarray: 3
        usage.dask: 257
        """
        ...


class _iLocIndexer:
    def __getitem__(
        self: object,
        _0: Union[
            Tuple[
                slice[Union[None, int], Union[None, int], Union[None, int]],
                Union[int, List[Union[bool, int]]],
            ],
            numpy.ndarray,
            int,
            slice[
                Union[int, numpy.int64, None],
                Union[numpy.int64, int, None],
                Union[int, numpy.int64, None],
            ],
        ],
        /,
    ):
        """
        usage.dask: 68
        """
        ...

    def __setitem__(
        self: object,
        _0: Union[Tuple[Union[List[int], slice[None, int, None], int], int], int],
        _1: float,
        /,
    ):
        """
        usage.dask: 5
        """
        ...


class IndexingError:
    def __init__(_0: Literal["Too many indexers"], /):
        """
        usage.dask: 1
        """
        ...
