from typing import *


class _LocIndexer:
    def __getitem__(self, _0, /):
        ""


class _iLocIndexer:
    def __getitem__(
        self,
        _0: Union[
            (
                Tuple[
                    (
                        slice[(Union[(None, int)], Union[(None, int)], None)],
                        Union[(int, List[Union[(bool, int)]])],
                    )
                ],
                numpy.ndarray,
                int,
                slice[
                    (
                        Union[(int, numpy.int64, None)],
                        Union[(numpy.int64, int, None)],
                        None,
                    )
                ],
            )
        ],
        /,
    ):
        ""

    def __setitem__(
        self,
        _0: Union[
            (Tuple[(Union[(List[int], slice[(None, int, None)], int)], int)], int)
        ],
        _1: float,
        /,
    ):
        ""


class IndexingError:
    def __init__(_0: Literal[("Too many indexers",)], /):
        "usage.dask: 1"
