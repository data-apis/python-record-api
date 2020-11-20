from typing import *


@overload
def read_parquet(path: Literal["/tmp/tmpnp5ngcgq"], columns: None):
    """
    usage.koalas: 1
    """
    ...


@overload
def read_parquet(
    path: Literal["/tmp/tmpnp5ngcgq"], columns: List[Literal["i64", "i32"]]
):
    """
    usage.koalas: 1
    """
    ...


@overload
def read_parquet(
    path: Literal["/tmp/tmpnp5ngcgq"], columns: List[Literal["i32", "i64"]]
):
    """
    usage.koalas: 1
    """
    ...


@overload
def read_parquet(path: Literal["/tmp/tmpnp5ngcgq"]):
    """
    usage.koalas: 1
    """
    ...


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
    usage.geopandas: 2
    usage.modin: 1
    """
    ...


def read_parquet(
    path: str,
    engine: Literal["auto"] = ...,
    columns: Union[List[Literal["i64", "i32", "col1"]], None] = ...,
):
    """
    usage.geopandas: 2
    usage.koalas: 4
    usage.modin: 10
    """
    ...
