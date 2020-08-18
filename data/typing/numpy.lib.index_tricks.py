from typing import *


class CClass:
    @overload
    def __getitem__(self, _0: Tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray], /):
        """
        usage.skimage: 1
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.ndarray, numpy.ndarray], /):
        """
        usage.matplotlib: 1
        usage.pandas: 3
        usage.sklearn: 38
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Union[numpy.ndarray, List[complex]], ...], /):
        """
        usage.scipy: 23
        """
        ...

    @overload
    def __getitem__(self, _0: numpy.ndarray, /):
        """
        usage.sklearn: 1
        """
        ...

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
    @overload
    def __getitem__(self, _0: Tuple[slice[int, int, int], slice[int, int, int]], /):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, None, None], /):
        """
        usage.pandas: 2
        """
        ...

    @overload
    def __getitem__(
        self, _0: slice[Union[None, int], Union[int, None], Union[None, int]], /
    ):
        """
        usage.scipy: 21
        """
        ...

    @overload
    def __getitem__(self, _0: slice[int, int, int], /):
        """
        usage.matplotlib: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[int, int, int], /):
        """
        usage.matplotlib: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, None, None], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, None, None], /):
        """
        usage.sklearn: 1
        """
        ...

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
    @overload
    def __getitem__(
        self,
        _0: Tuple[
            slice[numpy.float64, numpy.float64, numpy.float64],
            slice[numpy.float64, numpy.float64, numpy.float64],
            slice[numpy.float64, numpy.float64, numpy.float64],
        ],
        /,
    ):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[int, int, int], slice[int, int, int]], /):
        """
        usage.matplotlib: 1
        usage.skimage: 35
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, int, None], slice[None, int, None]], /):
        """
        usage.skimage: 2
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            slice[numpy.float64, numpy.float64, numpy.float64],
            slice[numpy.float64, numpy.float64, numpy.float64],
        ],
        /,
    ):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, int, None], slice[None, int, None]], /):
        """
        usage.matplotlib: 1
        usage.skimage: 2
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            slice[None, int, None], slice[None, int, None], slice[None, int, None]
        ],
        /,
    ):
        """
        usage.skimage: 2
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            slice[numpy.float64, numpy.float64, numpy.float64],
            slice[numpy.float64, numpy.float64, numpy.float64],
            slice[numpy.float64, numpy.float64, numpy.float64],
        ],
        /,
    ):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[slice[numpy.int64, numpy.int64, numpy.int64]], /):
        """
        usage.skimage: 2
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[slice[int, int, int], slice[int, int, int], slice[int, int, int]],
        /,
    ):
        """
        usage.skimage: 2
        """
        ...

    @overload
    def __getitem__(self, _0: List[slice[None, int, None]], /):
        """
        usage.skimage: 3
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[int, int, int], slice[int, int, int]], /):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[slice[int, int, int], slice[int, int, int], slice[int, int, int]],
        /,
    ):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            slice[int, int, int],
            slice[int, int, int],
            slice[int, int, int],
            slice[int, int, int],
        ],
        /,
    ):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            slice[int, int, int],
            slice[int, int, int],
            slice[int, int, int],
            slice[int, int, int],
            slice[int, int, int],
        ],
        /,
    ):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            slice[int, int, int],
            slice[int, int, int],
            slice[int, int, int],
            slice[int, int, int],
            slice[int, int, int],
            slice[int, int, int],
        ],
        /,
    ):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            slice[int, int, int],
            slice[int, int, int],
            slice[int, int, int],
            slice[int, int, int],
            slice[int, int, int],
            slice[int, int, int],
            slice[int, int, int],
        ],
        /,
    ):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Union[
            Tuple[
                slice[int, Union[float, int], int], slice[int, Union[float, int], int]
            ],
            slice[int, int, int],
            List[slice[int, int, int]],
        ],
        /,
    ):
        """
        usage.scipy: 6
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[int, float, int], slice[int, float, int]], /):
        """
        usage.matplotlib: 3
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[int, int, int], slice[int, int, int]], /):
        """
        usage.matplotlib: 2
        """
        ...

    @overload
    def __getitem__(
        self, _0: Tuple[slice[float, float, float], slice[float, float, float]], /
    ):
        """
        usage.matplotlib: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[int, int, int], slice[None, int, None]], /):
        """
        usage.matplotlib: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[int, float, int], slice[int, float, int]], /):
        """
        usage.matplotlib: 1
        """
        ...

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
    @overload
    def __getitem__(self, _0: Tuple[slice[int, float, int], slice[int, float, int]], /):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[int, int, int], slice[int, int, int]], /):
        """
        usage.skimage: 3
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[slice[int, int, int], slice[int, int, int], slice[int, int, int]],
        /,
    ):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, int, None], slice[None, int, None]], /):
        """
        usage.skimage: 2
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            slice[None, int, None], slice[None, int, None], slice[None, int, None]
        ],
        /,
    ):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Union[
            List[slice[int, int, int]],
            Tuple[
                slice[Union[int, None], int, Union[int, None]],
                slice[Union[int, None], Union[float, int], Union[int, None]],
            ],
        ],
        /,
    ):
        """
        usage.scipy: 4
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[int, int, int], slice[int, int, int]], /):
        """
        usage.matplotlib: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[int, int, int], slice[int, int, int]], /):
        """
        usage.matplotlib: 3
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[slice[None, int, None], ...], /):
        """
        usage.dask: 2
        """
        ...

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
    @overload
    def __getitem__(self, _0: Tuple[float, float], /):
        """
        usage.skimage: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, int, int, int, int], /):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[List[Union[int, float]]], /):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[List[int]], /):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, int, int], /):
        """
        usage.skimage: 3
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[float, float, float], /):
        """
        usage.skimage: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[float, int, int], /):
        """
        usage.skimage: 2
        """
        ...

    @overload
    def __getitem__(self, _0: numpy.ndarray, /):
        """
        usage.skimage: 3
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Tuple[float, float], float], /):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[int, numpy.ndarray], /):
        """
        usage.sklearn: 3
        usage.xarray: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, int, None], /):
        """
        usage.xarray: 2
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Union[
            Tuple[Union[bool, int, numpy.ndarray], Union[bool, numpy.ndarray, int]],
            slice[int, int, int],
        ],
        /,
    ):
        """
        usage.pandas: 13
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Union[
            List[numpy.ndarray],
            tuple,
            slice[
                Union[int, numpy.int64],
                Union[numpy.int64, int],
                Union[int, numpy.int64],
            ],
            numpy.ndarray,
            int,
        ],
        /,
    ):
        """
        usage.scipy: 187
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray], /):
        """
        usage.matplotlib: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.ndarray, numpy.ndarray], /):
        """
        usage.matplotlib: 4
        usage.sklearn: 16
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            List[int], List[int], List[int], List[int], List[int], int, List[int]
        ],
        /,
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            List[int], List[int], List[int], List[int], List[int], int, int, List[int]
        ],
        /,
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[int], List[int], List[int]], /):
        """
        usage.sklearn: 3
        """
        ...

    @overload
    def __getitem__(self, _0: List[int], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: Tuple[
            numpy.ndarray, numpy.ndarray, numpy.ndarray, numpy.ndarray, numpy.ndarray
        ],
        /,
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.ndarray, int], /):
        """
        usage.sklearn: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[bool, numpy.ndarray, bool], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.float64, numpy.ndarray], /):
        """
        usage.sklearn: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[List[int], List[int]], /):
        """
        usage.sklearn: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.ndarray, numpy.float64], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.int64, numpy.ndarray], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.float64, numpy.ndarray, numpy.float64], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.int64, numpy.ndarray, numpy.int64], /):
        """
        usage.sklearn: 1
        """
        ...

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
