from typing import *


def to_datetime(
    arg: Union[
        (
            List[Literal[("2002", "2000", "2001")]],
            List[Literal[("2000-01-03T06", "2000-01-02T18", "2000-01-01T18")]],
            List[Literal[("2000-01-02", "2000-01-01", "NaT")]],
            numpy.ndarray,
        )
    ]
):
    "usage.xarray: 4"
