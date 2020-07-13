from typing import *


class CClass:
    def __getitem__(self, _0: Union[numpy.ndarray, Tuple[numpy.ndarray, ...]], /):
        """
        usage.pandas: 3
        usage.skimage: 1
        usage.sklearn: 40
        """
        ...


class IndexExpression:
    def __getitem__(
        self,
        _0: Union[
            slice[None, None, None], Tuple[slice[int, int, int], slice[int, int, int]]
        ],
        /,
    ):
        """
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
                    Union[None, numpy.float64, int],
                    Union[int, numpy.float64],
                    Union[None, numpy.float64, int],
                ],
                ...,
            ],
            List[
                slice[
                    Union[numpy.int64, None],
                    Union[numpy.int64, int],
                    Union[numpy.int64, None],
                ]
            ],
        ],
        /,
    ):
        """
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
        usage.skimage: 8
        """
        ...


class RClass:
    def __getitem__(
        self,
        _0: Union[
            tuple,
            slice[Union[int, None], int, Union[int, None]],
            numpy.ndarray,
            List[Union[int, List[Union[int, float]]]],
        ],
        /,
    ):
        """
        usage.pandas: 13
        usage.skimage: 16
        usage.sklearn: 37
        usage.xarray: 3
        """
        ...
