from typing import *


@overload
def _is_string_like(obj: _io.BytesIO):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def _is_string_like(obj: str):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def _is_string_like(obj: pathlib.PosixPath):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def _is_string_like(obj: Literal["/tmp/tmpqlr25op5"]):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def _is_string_like(obj: Literal["/tmp/tmp6_x3j995"]):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def _is_string_like(obj: Literal["/tmp/tmpj2o81hmg"]):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def _is_string_like(obj: Literal["/tmp/tmpamfmfei4"]):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def _is_string_like(obj: Literal["/tmp/tmp7tx7ize_"]):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def _is_string_like(obj: Literal["/tmp/tmpxji2bobd"]):
    """
    usage.statsmodels: 1
    """
    ...


def _is_string_like(obj: Union[str, pathlib.PosixPath, _io.BytesIO]):
    """
    usage.statsmodels: 9
    """
    ...
