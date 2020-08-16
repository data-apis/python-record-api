from typing import *


class CClass:
    def __getitem__(
        self,
        _0: Union[numpy.ndarray, Tuple[Union[numpy.ndarray, List[complex]], ...]],
        /,
    ):
        """
        usage.matplotlib: 1
        usage.pandas: 3
        usage.scipy: 23
        usage.skimage: 1
        usage.sklearn: 40
        """
        ...


class IndexExpression:
    def __getitem__(
        self,
        _0: Union[
            slice[Union[None, int], Union[None, int], Union[None, int]],
            Tuple[slice[int, int, int], slice[int, int, int]],
        ],
        /,
    ):
        """
        usage.matplotlib: 2
        usage.pandas: 2
        usage.scipy: 21
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
                    Union[int, numpy.int64, None],
                    Union[int, numpy.int64],
                    Union[int, numpy.int64, None],
                ]
            ],
            slice[int, int, int],
        ],
        /,
    ):
        """
        usage.matplotlib: 12
        usage.scipy: 6
        usage.skimage: 57
        usage.sklearn: 1
        """
        ...


class OGridClass:
    def __getitem__(
        self,
        _0: Union[
            Tuple[slice[Union[None, int], Union[int, float], Union[None, int]], ...],
            List[slice[int, int, int]],
        ],
        /,
    ):
        """
        usage.dask: 2
        usage.matplotlib: 4
        usage.scipy: 4
        usage.skimage: 8
        """
        ...


class RClass:
    def __getitem__(
        self,
        _0: Union[
            List[Union[List[Union[int, float]], numpy.ndarray, int]],
            tuple,
            int,
            numpy.ndarray,
            slice[
                Union[int, numpy.int64, None],
                Union[int, numpy.int64],
                Union[int, numpy.int64, None],
            ],
        ],
        /,
    ):
        """
        usage.matplotlib: 6
        usage.pandas: 13
        usage.scipy: 187
        usage.skimage: 16
        usage.sklearn: 37
        usage.xarray: 3
        """
        ...
