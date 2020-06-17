from typing import *


class RClass:
    def __getitem__(
        self,
        _0: Union[
            (
                List[Union[(List[Union[(float, int)]], int)]],
                tuple,
                numpy.ndarray,
                slice[(None, int, None)],
            )
        ],
        /,
    ):
        ""


class OGridClass:
    def __getitem__(
        self,
        _0: Tuple[(slice[(Union[(None, int)], Union[(int, float)], None)], ...)],
        /,
    ):
        ""


class MGridClass:
    def __getitem__(
        self,
        _0: Union[
            (
                Tuple[
                    (
                        slice[
                            (
                                Union[(None, numpy.float64, int)],
                                Union[(int, numpy.float64)],
                                Union[(None, numpy.float64, float, complex, int)],
                            )
                        ],
                        ...,
                    )
                ],
                List[
                    slice[
                        (
                            Union[(numpy.int64, int, None)],
                            Union[(numpy.int64, float, int)],
                            None,
                        )
                    ]
                ],
            )
        ],
        /,
    ):
        ""


class CClass:
    def __getitem__(self, _0: Union[(numpy.ndarray, Tuple[(numpy.ndarray, ...)])], /):
        ""


class IndexExpression:
    def __getitem__(
        self, _0: Tuple[(slice[(int, int, None)], slice[(int, int, None)])], /
    ):
        ""
