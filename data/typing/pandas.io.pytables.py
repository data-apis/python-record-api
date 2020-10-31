from typing import *


@overload
def read_hdf(path_or_buf: Literal["test.hdf"], key: Literal["df"]):
    """
    usage.modin: 2
    """
    ...


@overload
def read_hdf(
    path_or_buf: Literal["test.hdf"],
    key: Literal["df"],
    mode: Literal["r"],
    errors: Literal["strict"],
    where: None,
    start: None,
    stop: None,
    columns: None,
    iterator: bool,
    chunksize: None,
):
    """
    usage.modin: 1
    """
    ...


def read_hdf(
    path_or_buf: Literal["test.hdf"],
    key: Literal["df"],
    mode: Literal["r"] = ...,
    errors: Literal["strict"] = ...,
    where: None = ...,
    start: None = ...,
    stop: None = ...,
    columns: None = ...,
    iterator: bool = ...,
    chunksize: None = ...,
):
    """
    usage.modin: 3
    """
    ...


class HDFStore:
    pass
