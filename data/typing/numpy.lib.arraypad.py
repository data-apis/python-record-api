from typing import *


def _as_pairs(
    x: Union[
        (
            int,
            Tuple[(int, int)],
            List[Tuple[(int, int)]],
            Tuple[(Tuple[(int, int)], ...)],
            List[Tuple[(numpy.int64, numpy.int64)]],
        )
    ],
    ndim: int,
    as_index: bool,
):
    "usage.skimage: 6"
