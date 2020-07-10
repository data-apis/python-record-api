from typing import *


class CClass:
    def __getitem__(self, _0: Union[numpy.ndarray, Tuple[numpy.ndarray, ...]], /):
        """
        usage.skimage: 1
        usage.sklearn: 26
        """
        ...


class IndexExpression:
    def __getitem__(self, _0: Tuple[slice[int, int, int], slice[int, int, int]], /):
        """
        usage.skimage: 1
        """
        ...


class MGridClass:
    def __getitem__(
        self,
        _0: Union[
            Tuple[
                slice[
                    Union[None, numpy.float64, int],
                    Union[int, numpy.float64],
                    Union[None, numpy.float64, int],
                ],
                ...,
            ],
            List[
                slice[
                    Union[numpy.int64, int, None],
                    Union[numpy.int64, float, int],
                    Union[numpy.int64, int, None],
                ]
            ],
        ],
        /,
    ):
        """
        usage.skimage: 61
        usage.sklearn: 1
        """
        ...


class OGridClass:
    def __getitem__(
        self,
        _0: Tuple[slice[Union[None, int], Union[int, float], Union[None, int]], ...],
        /,
    ):
        """
        usage.skimage: 9
        usage.dask: 2
        """
        ...


class RClass:
    def __getitem__(
        self,
        _0: Union[
            List[Union[List[Union[float, int]], int]],
            tuple,
            numpy.ndarray,
            slice[None, int, None],
        ],
        /,
    ):
        """
        usage.skimage: 16
        usage.xarray: 3
        usage.sklearn: 24
        """
        ...
