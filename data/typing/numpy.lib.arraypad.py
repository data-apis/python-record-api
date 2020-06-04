def _as_pairs(
    x: Union[
        (
            list[tuple[(numpy.int64, numpy.int64)]],
            int,
            list[tuple[(int, int)]],
            tuple[(tuple[(int, int)], ...)],
            tuple[(int, int)],
        )
    ],
    ndim: int,
    as_index: bool,
):
    "usage.skimage: 6"
