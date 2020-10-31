from typing import *


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
    io: Literal["test.xlsx"] = ...,
    sheet_name: Union[None, int] = ...,
    index_col: Union[None, int] = ...,
    *,
    EngineDispatcher: Type[
        modin.data_management.factories.dispatcher.EngineDispatcher
    ] = ...,
    _: None = ...,
    comment: None = ...,
    convert_float: bool = ...,
    converters: None = ...,
    date_parser: None = ...,
    dtype: None = ...,
    false_values: None = ...,
    header: int = ...,
    keep_default_na: bool = ...,
    kwargs: Dict[str, Union[int, bool, Literal["xlrd", "test.xlsx"], None]] = ...,
    mangle_dupe_cols: bool = ...,
    na_filter: bool = ...,
    na_values: None = ...,
    names: None = ...,
    nrows: None = ...,
    parse_dates: bool = ...,
    skipfooter: int = ...,
    squeeze: bool = ...,
    thousands: None = ...,
    true_values: None = ...,
    usecols: None = ...,
    verbose: bool = ...,
):
    """
    usage.modin: 6
    """
    ...


class ExcelFile:
    pass
