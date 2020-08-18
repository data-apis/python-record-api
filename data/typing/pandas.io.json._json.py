from typing import *


@overload
def read_json(path_or_buf: str, orient: Literal["split"], lines: bool):
    """
    usage.dask: 1
    """
    ...


@overload
def read_json(path_or_buf: str, orient: Literal["records"], lines: bool):
    """
    usage.dask: 2
    """
    ...


@overload
def read_json(path_or_buf: str, orient: Literal["index"], lines: bool):
    """
    usage.dask: 1
    """
    ...


@overload
def read_json(path_or_buf: str, orient: Literal["columns"], lines: bool):
    """
    usage.dask: 1
    """
    ...


@overload
def read_json(path_or_buf: str, orient: Literal["values"], lines: bool):
    """
    usage.dask: 1
    """
    ...


@overload
def read_json(path_or_buf: _io.TextIOWrapper):
    """
    usage.dask: 1
    """
    ...


@overload
def read_json(path_or_buf: _io.TextIOWrapper, orient: Literal["split"], lines: bool):
    """
    usage.dask: 1
    """
    ...


@overload
def read_json(path_or_buf: _io.TextIOWrapper, orient: Literal["records"], lines: bool):
    """
    usage.dask: 1
    """
    ...


@overload
def read_json(path_or_buf: _io.StringIO, orient: Literal["records"], lines: bool):
    """
    usage.dask: 1
    """
    ...


@overload
def read_json(path_or_buf: _io.TextIOWrapper, orient: Literal["index"], lines: bool):
    """
    usage.dask: 1
    """
    ...


@overload
def read_json(path_or_buf: _io.TextIOWrapper, orient: Literal["columns"], lines: bool):
    """
    usage.dask: 1
    """
    ...


@overload
def read_json(path_or_buf: _io.TextIOWrapper, orient: Literal["values"], lines: bool):
    """
    usage.dask: 1
    """
    ...


def read_json(
    path_or_buf: Union[_io.TextIOWrapper, _io.StringIO, str],
    orient: Literal["values", "columns", "index", "records", "split"] = ...,
    lines: bool = ...,
):
    """
    usage.dask: 13
    """
    ...
