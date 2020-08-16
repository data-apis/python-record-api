from typing import *


class CClass:
    def __getitem__(self, _0: Union[numpy.ndarray, Tuple[numpy.ndarray, ...]], /):
        """
        usage.matplotlib: 1
        usage.pandas: 3
        usage.skimage: 1
        usage.sklearn: 40
        """
        ...


class IndexExpression:
    def __getitem__(
        self,
        _0: Union[
            slice[Union[int, None], Union[int, None], Union[int, None]],
            Tuple[slice[int, int, int], slice[int, int, int]],
        ],
        /,
    ):
        """
        usage.matplotlib: 2
        usage.pandas: 2
        usage.skimage: 1
        usage.sklearn: 2
        """
        ...


class MGridClass:
    def __getitem__(
        self,
        _0: Union[
            Tuple[
                slice[
                    Union[None, numpy.float64, int, float],
                    Union[int, numpy.float64, float],
                    Union[None, numpy.float64, int, float],
                ],
                ...,
            ],
            List[
                slice[
                    Union[None, numpy.int64],
                    Union[int, numpy.int64],
                    Union[None, numpy.int64],
                ]
            ],
        ],
        /,
    ):
        """
        usage.matplotlib: 12
        usage.skimage: 57
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
        usage.dask: 2
        usage.matplotlib: 4
        usage.skimage: 8
        """
        ...


class RClass:
    def __getitem__(
        self,
        _0: Union[
            List[Union[List[Union[float, int]], int]],
            tuple,
            slice[Union[None, int], int, Union[None, int]],
            numpy.ndarray,
        ],
        /,
    ):
        """
        usage.matplotlib: 6
        usage.pandas: 13
        usage.skimage: 16
        usage.sklearn: 37
        usage.xarray: 3
        """
        ...
