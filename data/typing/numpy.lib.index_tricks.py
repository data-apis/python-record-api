from typing import *


class RClass:
    def __getitem__(
        self: object,
        _0: Union[
            List[Union[List[Union[float, int]], int]],
            tuple,
            numpy.ndarray,
            slice[None, int, None],
        ],
        /,
    ):
        "\n    usage.skimage: 16\n    usage.xarray: 3\n    usage.sklearn: 24\n    "
        ...


class OGridClass:
    def __getitem__(
        self: object,
        _0: Tuple[slice[Union[None, int], Union[int, float], Union[None, int]], ...],
        /,
    ):
        "\n    usage.skimage: 9\n    usage.dask: 2\n    "
        ...


class MGridClass:
    def __getitem__(
        self: object,
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
        "\n    usage.skimage: 61\n    usage.sklearn: 1\n    "
        ...


class CClass:
    def __getitem__(
        self: object, _0: Union[numpy.ndarray, Tuple[numpy.ndarray, ...]], /
    ):
        "\n    usage.skimage: 1\n    usage.sklearn: 26\n    "
        ...


class IndexExpression:
    def __getitem__(
        self: object, _0: Tuple[slice[int, int, int], slice[int, int, int]], /
    ):
        "\n    usage.skimage: 1\n    "
        ...
