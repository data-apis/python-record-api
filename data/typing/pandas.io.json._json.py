from typing import *


@overload
def read_json(path_or_buf: Literal["test.json"]):
    """
    usage.modin: 1
    """
    ...


@overload
def read_json(
    _0: str,
    /,
    *,
    EngineDispatcher: Type[modin.data_management.factories.dispatcher.EngineDispatcher],
    _: None,
    chunksize: None,
    compression: Literal["infer"],
    convert_axes: None,
    convert_dates: bool,
    date_unit: None,
    dtype: None,
    encoding: None,
    keep_default_dates: bool,
    kwargs: Dict[str, Union[None, bool, Literal["frame", "test.json"]]],
    lines: bool,
    nrows: None,
    numpy: bool,
    orient: None,
    precise_float: bool,
    typ: Literal["frame"],
):
    """
    usage.modin: 1
    """
    ...


@overload
def read_json(
    path_or_buf: str, dtype: Dict[Literal["two", "one"], Literal["category", "int64"]]
):
    """
    usage.modin: 1
    """
    ...


@overload
def read_json(
    _0: str,
    /,
    *,
    EngineDispatcher: Type[modin.data_management.factories.dispatcher.EngineDispatcher],
    _: None,
    chunksize: None,
    compression: Literal["infer"],
    convert_axes: None,
    convert_dates: bool,
    date_unit: None,
    dtype: Dict[Literal["two", "one"], Literal["category", "int64"]],
    encoding: None,
    keep_default_dates: bool,
    kwargs: Dict[
        str,
        Union[
            None, bool, Dict[Literal["two", "one"], Literal["category", "int64"]], str
        ],
    ],
    lines: bool,
    nrows: None,
    numpy: bool,
    orient: None,
    precise_float: bool,
    typ: Literal["frame"],
):
    """
    usage.modin: 1
    """
    ...


@overload
def read_json(path_or_buf: Literal["test.json"], lines: bool):
    """
    usage.modin: 1
    """
    ...


@overload
def read_json(path_or_buf: _io.BytesIO, lines: bool):
    """
    usage.modin: 1
    """
    ...


@overload
def read_json(
    _0: str,
    /,
    *,
    EngineDispatcher: Type[modin.data_management.factories.dispatcher.EngineDispatcher],
    _: None,
    chunksize: None,
    compression: Literal["infer"],
    convert_axes: None,
    convert_dates: bool,
    date_unit: None,
    dtype: None,
    encoding: None,
    keep_default_dates: bool,
    kwargs: Dict[str, Union[None, bool, str]],
    lines: bool,
    nrows: None,
    numpy: bool,
    orient: None,
    precise_float: bool,
    typ: Literal["frame"],
):
    """
    usage.modin: 1
    """
    ...


@overload
def read_json(
    _0: _io.BytesIO,
    /,
    *,
    EngineDispatcher: Type[modin.data_management.factories.dispatcher.EngineDispatcher],
    _: None,
    chunksize: None,
    compression: Literal["infer"],
    convert_axes: None,
    convert_dates: bool,
    date_unit: None,
    dtype: None,
    encoding: None,
    keep_default_dates: bool,
    kwargs: Dict[str, Union[None, bool, _io.BytesIO, Literal["frame"]]],
    lines: bool,
    nrows: None,
    numpy: bool,
    orient: None,
    precise_float: bool,
    typ: Literal["frame"],
):
    """
    usage.modin: 1
    """
    ...


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
    _0: Union[_io.BytesIO, str] = ...,
    /,
    orient: Union[
        None, Literal["values", "columns", "index", "records", "split"]
    ] = ...,
    path_or_buf: Union[str, _io.StringIO, _io.TextIOWrapper, _io.BytesIO] = ...,
    lines: bool = ...,
    dtype: Union[None, Dict[Literal["two", "one"], Literal["category", "int64"]]] = ...,
    *,
    EngineDispatcher: Type[
        modin.data_management.factories.dispatcher.EngineDispatcher
    ] = ...,
    _: None = ...,
    chunksize: None = ...,
    compression: Literal["infer"] = ...,
    convert_axes: None = ...,
    convert_dates: bool = ...,
    date_unit: None = ...,
    encoding: None = ...,
    keep_default_dates: bool = ...,
    kwargs: Dict[
        str,
        Union[
            str,
            bool,
            _io.BytesIO,
            None,
            Dict[Literal["two", "one"], Literal["category", "int64"]],
        ],
    ] = ...,
    nrows: None = ...,
    numpy: bool = ...,
    precise_float: bool = ...,
    typ: Literal["frame"] = ...,
):
    """
    usage.dask: 13
    usage.modin: 8
    """
    ...
