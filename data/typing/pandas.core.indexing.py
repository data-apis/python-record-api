from typing import *

# usage.dask: 4
IndexingError: object


class IndexingError:
    def __init__(self, _0: Literal["Too many indexers"], /):
        """
        usage.dask: 1
        """
        ...


class _LocIndexer:
    def __getitem__(self, _0: object, /):
        """
        usage.dask: 263
        usage.sklearn: 30
        usage.xarray: 45
        """
        ...


class _iLocIndexer:
    def __getitem__(
        self,
        _0: Union[
            slice[
                Union[numpy.int64, int, None],
                Union[None, numpy.int64, int],
                Union[numpy.int64, int, None],
            ],
            Tuple[
                Union[
                    slice[Union[None, int], Union[None, int], Union[None, int]],
                    numpy.ndarray,
                    int,
                ],
                Union[
                    List[Union[int, bool]],
                    int,
                    numpy.ndarray,
                    slice[Union[int, None], Union[int, None], Union[int, None]],
                ],
            ],
            List[int],
            numpy.ndarray,
            int,
        ],
        /,
    ):
        """
        usage.dask: 72
        usage.sklearn: 24
        usage.xarray: 5
        """
        ...

    def __setitem__(
        self,
        _0: Union[
            Tuple[
                Union[int, slice[None, Union[None, int], None], List[int]],
                Union[int, numpy.int32],
            ],
            int,
        ],
        _1: Union[numpy.float64, pandas.core.series.Series, float],
        /,
    ):
        """
        usage.dask: 5
        usage.sklearn: 5
        """
        ...
