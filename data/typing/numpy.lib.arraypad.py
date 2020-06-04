from typing import *


def _as_pairs(
    x: Union[
        (
            List[Tuple[(numpy.int64, numpy.int64)]],
            int,
            Tuple[(Tuple[(int, int)], ...)],
            List[Tuple[(int, int)]],
            Tuple[(int, int)],
        )
    ],
    ndim: int,
    as_index: bool,
):
    "usage.skimage: 6"
