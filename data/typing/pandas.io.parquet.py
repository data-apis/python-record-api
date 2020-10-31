from typing import *


@overload
def read_parquet(path: Literal["test.parquet"]):
    """
    usage.modin: 3
    """
    ...


@overload
def read_parquet(path: Literal["test.parquet"], columns: List[Literal["col1"]]):
    """
    usage.modin: 3
    """
    ...


@overload
def read_parquet(path: Literal["test.parquet"], engine: Literal["auto"], columns: None):
    """
    usage.modin: 1
    """
    ...


@overload
def read_parquet(
    path: Literal["test.parquet"],
    engine: Literal["auto"],
    columns: List[Literal["col1"]],
):
    """
    usage.modin: 1
    """
    ...


@overload
def read_parquet(
    path: Literal["tmp_folder.parquet"], engine: Literal["auto"], columns: None
):
    """
    usage.modin: 1
    """
    ...


@overload
def read_parquet(path: str):
    """
    usage.modin: 1
    """
    ...


def read_parquet(
    path: str,
    engine: Literal["auto"] = ...,
    columns: Union[None, List[Literal["col1"]]] = ...,
):
    """
    usage.modin: 10
    """
    ...
