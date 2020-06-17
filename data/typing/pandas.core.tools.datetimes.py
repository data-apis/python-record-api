from typing import *


def to_datetime(
    arg: Union[
        (
            List[Literal[("NaT", "2000-01-02", "2000-01-01")]],
            List[Literal[("2002", "2001", "2000")]],
            List[Literal[("2000-01-02T18", "2000-01-03T06", "2000-01-01T18")]],
            numpy.ndarray,
        )
    ]
):
    "usage.xarray: 4"
