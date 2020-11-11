from typing import *


@overload
def read_stata(filepath_or_buffer: str):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def read_stata(filepath_or_buffer: Literal["test.dta"]):
    """
    usage.modin: 1
    """
    ...


def read_stata(filepath_or_buffer: str):
    """
    usage.modin: 1
    usage.statsmodels: 1
    """
    ...
