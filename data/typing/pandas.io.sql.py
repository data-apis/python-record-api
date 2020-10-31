from typing import *


@overload
def read_sql(sql: str, con: str):
    """
    usage.modin: 2
    """
    ...


@overload
def read_sql(sql: str, con: str, index_col: None):
    """
    usage.modin: 1
    """
    ...


@overload
def read_sql(sql: str, con: str, chunksize: int):
    """
    usage.modin: 1
    """
    ...


def read_sql(sql: str, con: str, index_col: None = ..., chunksize: int = ...):
    """
    usage.modin: 4
    """
    ...
