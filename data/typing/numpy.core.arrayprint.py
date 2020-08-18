from typing import *


@overload
def set_string_function(f: Callable):
    """
    usage.dask: 1
    """
    ...


@overload
def set_string_function(f: None):
    """
    usage.dask: 1
    """
    ...


def set_string_function(f: Union[None, Callable]):
    """
    usage.dask: 2
    """
    ...
