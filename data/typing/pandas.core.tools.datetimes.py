from typing import *


def to_datetime(
    arg: Union[
        (
            List[Literal[("2000", "2001", "2002")]],
            numpy.ndarray,
            List[Literal[("2000-01-02", "NaT", "2000-01-01")]],
            List[Literal[("2000-01-03T06", "2000-01-02T18", "2000-01-01T18")]],
        )
    ]
):
    "usage.xarray: 4"
