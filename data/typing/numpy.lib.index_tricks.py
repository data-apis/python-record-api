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
                    Union[None, float, int, numpy.float64],
                    Union[int, float, numpy.float64],
                    Union[None, float, int, numpy.float64],
                ],
                ...,
            ],
            slice[int, int, int],
            List[
                slice[
                    Union[None, int, numpy.int64],
                    Union[int, numpy.int64],
                    Union[None, int, numpy.int64],
                ]
            ],
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
            Tuple[slice[Union[int, None], Union[float, int], Union[int, None]], ...],
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
            tuple,
            slice[
                Union[numpy.int64, int, None],
                Union[numpy.int64, int],
                Union[numpy.int64, int, None],
            ],
            numpy.ndarray,
            int,
            List[Union[int, numpy.ndarray, List[Union[int, float]]]],
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
