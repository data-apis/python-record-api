from typing import *


@overload
def read_excel(
    io: _io.BufferedReader,
    sheet_name: int,
    header: int,
    names: None,
    index_col: None,
    usecols: None,
    squeeze: bool,
    dtype: None,
    engine: None,
    converters: None,
    true_values: None,
    false_values: None,
    skiprows: None,
    nrows: None,
    na_values: None,
    keep_default_na: bool,
    verbose: bool,
    parse_dates: bool,
    date_parser: None,
    thousands: None,
    comment: None,
    skipfooter: int,
    convert_float: bool,
    mangle_dupe_cols: bool,
):
    """
    usage.koalas: 1
    """
    ...


@overload
def read_excel(io: _io.BufferedReader):
    """
    usage.koalas: 1
    """
    ...


@overload
def read_excel(
    io: _io.BufferedReader,
    sheet_name: int,
    header: int,
    names: None,
    index_col: int,
    usecols: None,
    squeeze: bool,
    dtype: None,
    engine: None,
    converters: None,
    true_values: None,
    false_values: None,
    skiprows: None,
    nrows: None,
    na_values: None,
    keep_default_na: bool,
    verbose: bool,
    parse_dates: bool,
    date_parser: None,
    thousands: None,
    comment: None,
    skipfooter: int,
    convert_float: bool,
    mangle_dupe_cols: bool,
):
    """
    usage.koalas: 1
    """
    ...


@overload
def read_excel(io: _io.BufferedReader, index_col: int):
    """
    usage.koalas: 1
    """
    ...


@overload
def read_excel(
    io: _io.BytesIO,
    sheet_name: int,
    header: int,
    names: None,
    index_col: None,
    usecols: None,
    squeeze: bool,
    dtype: None,
    engine: None,
    converters: None,
    true_values: None,
    false_values: None,
    skiprows: None,
    nrows: None,
    na_values: None,
    keep_default_na: bool,
    verbose: bool,
    parse_dates: bool,
    date_parser: None,
    thousands: None,
    comment: None,
    skipfooter: int,
    convert_float: bool,
    mangle_dupe_cols: bool,
):
    """
    usage.koalas: 1
    """
    ...


@overload
def read_excel(io: str):
    """
    usage.koalas: 2
    """
    ...


@overload
def read_excel(
    io: _io.BytesIO,
    sheet_name: int,
    header: int,
    names: None,
    index_col: int,
    usecols: None,
    squeeze: bool,
    dtype: None,
    engine: None,
    converters: None,
    true_values: None,
    false_values: None,
    skiprows: None,
    nrows: None,
    na_values: None,
    keep_default_na: bool,
    verbose: bool,
    parse_dates: bool,
    date_parser: None,
    thousands: None,
    comment: None,
    skipfooter: int,
    convert_float: bool,
    mangle_dupe_cols: bool,
):
    """
    usage.koalas: 1
    """
    ...


@overload
def read_excel(io: str, index_col: int):
    """
    usage.koalas: 2
    """
    ...


@overload
def read_excel(io: _io.BufferedReader, sheet_name: None, index_col: int):
    """
    usage.koalas: 1
    """
    ...


@overload
def read_excel(
    io: _io.BufferedReader,
    sheet_name: List[Literal["Sheet_name_2", "Sheet_name_1"]],
    header: int,
    names: None,
    index_col: int,
    usecols: None,
    squeeze: bool,
    dtype: None,
    engine: None,
    converters: None,
    true_values: None,
    false_values: None,
    skiprows: None,
    nrows: None,
    na_values: None,
    keep_default_na: bool,
    verbose: bool,
    parse_dates: bool,
    date_parser: None,
    thousands: None,
    comment: None,
    skipfooter: int,
    convert_float: bool,
    mangle_dupe_cols: bool,
):
    """
    usage.koalas: 1
    """
    ...


@overload
def read_excel(
    io: _io.BufferedReader,
    sheet_name: None,
    header: int,
    names: None,
    index_col: int,
    usecols: None,
    squeeze: bool,
    dtype: None,
    engine: None,
    converters: None,
    true_values: None,
    false_values: None,
    skiprows: None,
    nrows: None,
    na_values: None,
    keep_default_na: bool,
    verbose: bool,
    parse_dates: bool,
    date_parser: None,
    thousands: None,
    comment: None,
    skipfooter: int,
    convert_float: bool,
    mangle_dupe_cols: bool,
):
    """
    usage.koalas: 1
    """
    ...


@overload
def read_excel(
    io: _io.BytesIO,
    sheet_name: Literal["Sheet_name_2"],
    header: int,
    names: None,
    index_col: int,
    usecols: None,
    squeeze: bool,
    dtype: None,
    engine: None,
    converters: None,
    true_values: None,
    false_values: None,
    skiprows: None,
    nrows: None,
    na_values: None,
    keep_default_na: bool,
    verbose: bool,
    parse_dates: bool,
    date_parser: None,
    thousands: None,
    comment: None,
    skipfooter: int,
    convert_float: bool,
    mangle_dupe_cols: bool,
):
    """
    usage.koalas: 1
    """
    ...


@overload
def read_excel(
    io: _io.BytesIO,
    sheet_name: List[Literal["Sheet_name_2", "Sheet_name_1"]],
    header: int,
    names: None,
    index_col: int,
    usecols: None,
    squeeze: bool,
    dtype: None,
    engine: None,
    converters: None,
    true_values: None,
    false_values: None,
    skiprows: None,
    nrows: None,
    na_values: None,
    keep_default_na: bool,
    verbose: bool,
    parse_dates: bool,
    date_parser: None,
    thousands: None,
    comment: None,
    skipfooter: int,
    convert_float: bool,
    mangle_dupe_cols: bool,
):
    """
    usage.koalas: 1
    """
    ...


@overload
def read_excel(
    io: _io.BytesIO,
    sheet_name: None,
    header: int,
    names: None,
    index_col: int,
    usecols: None,
    squeeze: bool,
    dtype: None,
    engine: None,
    converters: None,
    true_values: None,
    false_values: None,
    skiprows: None,
    nrows: None,
    na_values: None,
    keep_default_na: bool,
    verbose: bool,
    parse_dates: bool,
    date_parser: None,
    thousands: None,
    comment: None,
    skipfooter: int,
    convert_float: bool,
    mangle_dupe_cols: bool,
):
    """
    usage.koalas: 1
    """
    ...


@overload
def read_excel(io: str, sheet_name: None, index_col: int):
    """
    usage.koalas: 1
    """
    ...


@overload
def read_excel(io: Literal["test.xlsx"]):
    """
    usage.modin: 1
    """
    ...


@overload
def read_excel(io: Literal["test.xlsx"], engine: Literal["xlrd"]):
    """
    usage.modin: 1
    """
    ...


@overload
def read_excel(
    _0: Literal["test.xlsx"],
    /,
    *,
    EngineDispatcher: Type[modin.data_management.factories.dispatcher.EngineDispatcher],
    _: None,
    comment: None,
    convert_float: bool,
    converters: None,
    date_parser: None,
    dtype: None,
    engine: Literal["xlrd"],
    false_values: None,
    header: int,
    index_col: None,
    keep_default_na: bool,
    kwargs: Dict[str, Union[None, Literal["xlrd", "test.xlsx"], bool, int]],
    mangle_dupe_cols: bool,
    na_filter: bool,
    na_values: None,
    names: None,
    nrows: None,
    parse_dates: bool,
    sheet_name: int,
    skipfooter: int,
    squeeze: bool,
    thousands: None,
    true_values: None,
    usecols: None,
    verbose: bool,
):
    """
    usage.modin: 1
    """
    ...


@overload
def read_excel(io: Literal["test.xlsx"], index_col: int):
    """
    usage.modin: 1
    """
    ...


@overload
def read_excel(io: Literal["test.xlsx"], sheet_name: None):
    """
    usage.modin: 1
    """
    ...


@overload
def read_excel(
    _0: Literal["test.xlsx"],
    /,
    *,
    EngineDispatcher: Type[modin.data_management.factories.dispatcher.EngineDispatcher],
    _: None,
    comment: None,
    convert_float: bool,
    converters: None,
    date_parser: None,
    dtype: None,
    engine: None,
    false_values: None,
    header: int,
    index_col: None,
    keep_default_na: bool,
    kwargs: Dict[str, Union[None, bool, int, Literal["test.xlsx"]]],
    mangle_dupe_cols: bool,
    na_filter: bool,
    na_values: None,
    names: None,
    nrows: None,
    parse_dates: bool,
    sheet_name: None,
    skipfooter: int,
    squeeze: bool,
    thousands: None,
    true_values: None,
    usecols: None,
    verbose: bool,
):
    """
    usage.modin: 1
    """
    ...


def read_excel(
    _0: Literal["test.xlsx"] = ...,
    /,
    io: Union[str, _io.BytesIO, _io.BufferedReader] = ...,
    sheet_name: Union[
        int,
        None,
        Literal["Sheet_name_2"],
        List[Literal["Sheet_name_2", "Sheet_name_1"]],
    ] = ...,
    header: int = ...,
    names: None = ...,
    index_col: Union[int, None] = ...,
    usecols: None = ...,
    squeeze: bool = ...,
    dtype: None = ...,
    engine: Union[Literal["xlrd"], None] = ...,
    converters: None = ...,
    true_values: None = ...,
    false_values: None = ...,
    skiprows: None = ...,
    nrows: None = ...,
    na_values: None = ...,
    keep_default_na: bool = ...,
    verbose: bool = ...,
    parse_dates: bool = ...,
    date_parser: None = ...,
    thousands: None = ...,
    comment: None = ...,
    skipfooter: int = ...,
    convert_float: bool = ...,
    mangle_dupe_cols: bool = ...,
    *,
    EngineDispatcher: Type[
        modin.data_management.factories.dispatcher.EngineDispatcher
    ] = ...,
    _: None = ...,
    kwargs: Dict[str, Union[int, bool, Literal["xlrd", "test.xlsx"], None]] = ...,
    na_filter: bool = ...,
):
    """
    usage.koalas: 17
    usage.modin: 6
    """
    ...


class ExcelFile:
    pass


class ExcelWriter:
    pass
