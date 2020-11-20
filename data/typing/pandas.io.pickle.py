from typing import *


@overload
def read_pickle(filepath_or_buffer: Literal["test.pkl"]):
    """
    usage.modin: 1
    """
    ...


@overload
def read_pickle(filepath_or_buffer: str):
    """
    usage.geopandas: 3
    """
    ...


def read_pickle(filepath_or_buffer: str):
    """
    usage.geopandas: 3
    usage.modin: 1
    """
    ...
