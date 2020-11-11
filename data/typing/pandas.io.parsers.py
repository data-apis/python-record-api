from typing import *


@overload
def _validate_usecols_arg(usecols: None):
    """
    usage.modin: 1
    """
    ...


@overload
def _validate_usecols_arg(usecols: List[Literal["a"]]):
    """
    usage.modin: 1
    """
    ...


@overload
def _validate_usecols_arg(usecols: List[Literal["d", "b", "a"]]):
    """
    usage.modin: 1
    """
    ...


@overload
def _validate_usecols_arg(usecols: List[int]):
    """
    usage.modin: 1
    """
    ...


def _validate_usecols_arg(
    usecols: Union[List[Union[Literal["a", "d", "b"], int]], None]
):
    """
    usage.modin: 4
    """
    ...


@overload
def read_csv(
    filepath_or_buffer: str,
    sep: Literal[","],
    engine: Literal["c"],
    float_precision: Literal["high"],
):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def read_csv(filepath_or_buffer: str, sep: Literal["\\s"], engine: Literal["python"]):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def read_csv(filepath_or_buffer: str, sep: Literal[";"], engine: Literal["python"]):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def read_csv(filepath_or_buffer: _io.StringIO, index_col: int):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def read_csv(filepath_or_buffer: _io.StringIO):
    """
    usage.statsmodels: 3
    """
    ...


@overload
def read_csv(filepath_or_buffer: str):
    """
    usage.modin: 4
    usage.seaborn: 1
    usage.statsmodels: 32
    """
    ...


@overload
def read_csv(filepath_or_buffer: str, index_col: Literal["Row.names"]):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def read_csv(filepath_or_buffer: str, index_col: int):
    """
    usage.statsmodels: 2
    """
    ...


@overload
def read_csv(filepath_or_buffer: _io.StringIO, index_col: None):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def read_csv(filepath_or_buffer: str, delimiter: Literal["\\s+"], header: int):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def read_csv(filepath_or_buffer: Literal["test.csv"], nrows: int):
    """
    usage.modin: 2
    """
    ...


@overload
def read_csv(
    _0: str,
    /,
    *,
    _: None,
    cache_dates: bool,
    chunksize: None,
    comment: None,
    compression: Literal["infer"],
    converters: None,
    date_parser: None,
    dayfirst: bool,
    decimal: Literal["."],
    delim_whitespace: bool,
    delimiter: None,
    dialect: None,
    doublequote: bool,
    dtype: None,
    encoding: None,
    engine: None,
    error_bad_lines: bool,
    escapechar: None,
    false_values: None,
    float_precision: None,
    header: Literal["infer"],
    index_col: None,
    infer_datetime_format: bool,
    iterator: bool,
    keep_date_col: bool,
    keep_default_na: bool,
    kwargs: Dict[str, Union[bool, None, Literal["infer", ",", "test.csv"]]],
    lineterminator: None,
    low_memory: bool,
    mangle_dupe_cols: bool,
    memory_map: bool,
    na_filter: bool,
    na_values: None,
    names: None,
    nrows: int,
    parse_dates: bool,
    prefix: None,
    quotechar: Literal['"'],
    quoting: int,
    sep: Literal[","],
    skip_blank_lines: bool,
    skipfooter: int,
    skipinitialspace: bool,
    skiprows: None,
    squeeze: bool,
    thousands: None,
    true_values: None,
    usecols: None,
    verbose: bool,
    warn_bad_lines: bool,
):
    """
    usage.modin: 1
    """
    ...


@overload
def read_csv(filepath_or_buffer: Literal["test.csv"], nrows: None):
    """
    usage.modin: 2
    """
    ...


@overload
def read_csv(filepath_or_buffer: Literal["test.csv"], sep: None, nrows: int):
    """
    usage.modin: 1
    """
    ...


@overload
def read_csv(
    _0: str,
    /,
    *,
    _: None,
    cache_dates: bool,
    chunksize: None,
    comment: None,
    compression: Literal["infer"],
    converters: None,
    date_parser: None,
    dayfirst: bool,
    decimal: Literal["."],
    delim_whitespace: bool,
    delimiter: None,
    dialect: None,
    doublequote: bool,
    dtype: None,
    encoding: None,
    engine: None,
    error_bad_lines: bool,
    escapechar: None,
    false_values: None,
    float_precision: None,
    header: Literal["infer"],
    index_col: None,
    infer_datetime_format: bool,
    iterator: bool,
    keep_date_col: bool,
    keep_default_na: bool,
    kwargs: Dict[str, Union[bool, None, Literal["infer", "test.csv"]]],
    lineterminator: None,
    low_memory: bool,
    mangle_dupe_cols: bool,
    memory_map: bool,
    na_filter: bool,
    na_values: None,
    names: None,
    nrows: int,
    parse_dates: bool,
    prefix: None,
    quotechar: Literal['"'],
    quoting: int,
    sep: None,
    skip_blank_lines: bool,
    skipfooter: int,
    skipinitialspace: bool,
    skiprows: None,
    squeeze: bool,
    thousands: None,
    true_values: None,
    usecols: None,
    verbose: bool,
    warn_bad_lines: bool,
):
    """
    usage.modin: 1
    """
    ...


@overload
def read_csv(filepath_or_buffer: Literal["test.csv"], sep: None, nrows: None):
    """
    usage.modin: 1
    """
    ...


@overload
def read_csv(filepath_or_buffer: Literal["test.csv"], nrows: int, quoting: int):
    """
    usage.modin: 1
    """
    ...


@overload
def read_csv(filepath_or_buffer: Literal["test.csv"], nrows: None, quoting: int):
    """
    usage.modin: 1
    """
    ...


@overload
def read_csv(
    filepath_or_buffer: str,
    names: List[Literal["two", "one"]],
    dtype: Dict[Literal["two", "one"], Literal["category", "int64"]],
):
    """
    usage.modin: 1
    """
    ...


@overload
def read_csv(
    _0: str,
    /,
    *,
    _: None,
    cache_dates: bool,
    chunksize: None,
    comment: None,
    compression: Literal["infer"],
    converters: None,
    date_parser: None,
    dayfirst: bool,
    decimal: Literal["."],
    delim_whitespace: bool,
    delimiter: None,
    dialect: None,
    doublequote: bool,
    dtype: Dict[Literal["two", "one"], Literal["category", "int64"]],
    encoding: None,
    engine: None,
    error_bad_lines: bool,
    escapechar: None,
    false_values: None,
    float_precision: None,
    header: Literal["infer"],
    index_col: None,
    infer_datetime_format: bool,
    iterator: bool,
    keep_date_col: bool,
    keep_default_na: bool,
    kwargs: Dict[str, Union[bool, None, List[Literal["two", "one"]], str]],
    lineterminator: None,
    low_memory: bool,
    mangle_dupe_cols: bool,
    memory_map: bool,
    na_filter: bool,
    na_values: None,
    names: List[Literal["two", "one"]],
    nrows: int,
    parse_dates: bool,
    prefix: None,
    quotechar: Literal['"'],
    quoting: int,
    sep: Literal[","],
    skip_blank_lines: bool,
    skipfooter: int,
    skipinitialspace: bool,
    skiprows: None,
    squeeze: bool,
    thousands: None,
    true_values: None,
    usecols: None,
    verbose: bool,
    warn_bad_lines: bool,
):
    """
    usage.modin: 1
    """
    ...


@overload
def read_csv(filepath_or_buffer: Literal["test.csv.gz"]):
    """
    usage.modin: 1
    """
    ...


@overload
def read_csv(
    _0: str,
    /,
    *,
    _: None,
    cache_dates: bool,
    chunksize: None,
    comment: None,
    compression: Literal["gzip"],
    converters: None,
    date_parser: None,
    dayfirst: bool,
    decimal: Literal["."],
    delim_whitespace: bool,
    delimiter: None,
    dialect: None,
    doublequote: bool,
    dtype: None,
    encoding: None,
    engine: None,
    error_bad_lines: bool,
    escapechar: None,
    false_values: None,
    float_precision: None,
    header: Literal["infer"],
    index_col: None,
    infer_datetime_format: bool,
    iterator: bool,
    keep_date_col: bool,
    keep_default_na: bool,
    kwargs: Dict[str, Union[bool, None, Literal["infer", ",", "test.csv.gz"]]],
    lineterminator: None,
    low_memory: bool,
    mangle_dupe_cols: bool,
    memory_map: bool,
    na_filter: bool,
    na_values: None,
    names: None,
    nrows: int,
    parse_dates: bool,
    prefix: None,
    quotechar: Literal['"'],
    quoting: int,
    sep: Literal[","],
    skip_blank_lines: bool,
    skipfooter: int,
    skipinitialspace: bool,
    skiprows: None,
    squeeze: bool,
    thousands: None,
    true_values: None,
    usecols: None,
    verbose: bool,
    warn_bad_lines: bool,
):
    """
    usage.modin: 1
    """
    ...


@overload
def read_csv(filepath_or_buffer: Literal["test.csv.bz2"]):
    """
    usage.modin: 1
    """
    ...


@overload
def read_csv(
    _0: str,
    /,
    *,
    _: None,
    cache_dates: bool,
    chunksize: None,
    comment: None,
    compression: Literal["bz2"],
    converters: None,
    date_parser: None,
    dayfirst: bool,
    decimal: Literal["."],
    delim_whitespace: bool,
    delimiter: None,
    dialect: None,
    doublequote: bool,
    dtype: None,
    encoding: None,
    engine: None,
    error_bad_lines: bool,
    escapechar: None,
    false_values: None,
    float_precision: None,
    header: Literal["infer"],
    index_col: None,
    infer_datetime_format: bool,
    iterator: bool,
    keep_date_col: bool,
    keep_default_na: bool,
    kwargs: Dict[str, Union[bool, None, Literal["infer", ",", "test.csv.bz2"]]],
    lineterminator: None,
    low_memory: bool,
    mangle_dupe_cols: bool,
    memory_map: bool,
    na_filter: bool,
    na_values: None,
    names: None,
    nrows: int,
    parse_dates: bool,
    prefix: None,
    quotechar: Literal['"'],
    quoting: int,
    sep: Literal[","],
    skip_blank_lines: bool,
    skipfooter: int,
    skipinitialspace: bool,
    skiprows: None,
    squeeze: bool,
    thousands: None,
    true_values: None,
    usecols: None,
    verbose: bool,
    warn_bad_lines: bool,
):
    """
    usage.modin: 1
    """
    ...


@overload
def read_csv(filepath_or_buffer: Literal["test.csv.xz"]):
    """
    usage.modin: 1
    """
    ...


@overload
def read_csv(
    _0: str,
    /,
    *,
    _: None,
    cache_dates: bool,
    chunksize: None,
    comment: None,
    compression: Literal["xz"],
    converters: None,
    date_parser: None,
    dayfirst: bool,
    decimal: Literal["."],
    delim_whitespace: bool,
    delimiter: None,
    dialect: None,
    doublequote: bool,
    dtype: None,
    encoding: None,
    engine: None,
    error_bad_lines: bool,
    escapechar: None,
    false_values: None,
    float_precision: None,
    header: Literal["infer"],
    index_col: None,
    infer_datetime_format: bool,
    iterator: bool,
    keep_date_col: bool,
    keep_default_na: bool,
    kwargs: Dict[str, Union[bool, None, Literal["infer", ",", "test.csv.xz"]]],
    lineterminator: None,
    low_memory: bool,
    mangle_dupe_cols: bool,
    memory_map: bool,
    na_filter: bool,
    na_values: None,
    names: None,
    nrows: int,
    parse_dates: bool,
    prefix: None,
    quotechar: Literal['"'],
    quoting: int,
    sep: Literal[","],
    skip_blank_lines: bool,
    skipfooter: int,
    skipinitialspace: bool,
    skiprows: None,
    squeeze: bool,
    thousands: None,
    true_values: None,
    usecols: None,
    verbose: bool,
    warn_bad_lines: bool,
):
    """
    usage.modin: 1
    """
    ...


@overload
def read_csv(filepath_or_buffer: Literal["test.csv.zip"]):
    """
    usage.modin: 1
    """
    ...


@overload
def read_csv(
    _0: str,
    /,
    *,
    _: None,
    cache_dates: bool,
    chunksize: None,
    comment: None,
    compression: Literal["zip"],
    converters: None,
    date_parser: None,
    dayfirst: bool,
    decimal: Literal["."],
    delim_whitespace: bool,
    delimiter: None,
    dialect: None,
    doublequote: bool,
    dtype: None,
    encoding: None,
    engine: None,
    error_bad_lines: bool,
    escapechar: None,
    false_values: None,
    float_precision: None,
    header: Literal["infer"],
    index_col: None,
    infer_datetime_format: bool,
    iterator: bool,
    keep_date_col: bool,
    keep_default_na: bool,
    kwargs: Dict[str, Union[bool, None, Literal["infer", ",", "test.csv.zip"]]],
    lineterminator: None,
    low_memory: bool,
    mangle_dupe_cols: bool,
    memory_map: bool,
    na_filter: bool,
    na_values: None,
    names: None,
    nrows: int,
    parse_dates: bool,
    prefix: None,
    quotechar: Literal['"'],
    quoting: int,
    sep: Literal[","],
    skip_blank_lines: bool,
    skipfooter: int,
    skipinitialspace: bool,
    skiprows: None,
    squeeze: bool,
    thousands: None,
    true_values: None,
    usecols: None,
    verbose: bool,
    warn_bad_lines: bool,
):
    """
    usage.modin: 1
    """
    ...


@overload
def read_csv(
    _0: str,
    /,
    *,
    _: None,
    cache_dates: bool,
    chunksize: None,
    comment: None,
    compression: Literal["infer"],
    converters: None,
    date_parser: None,
    dayfirst: bool,
    decimal: Literal["."],
    delim_whitespace: bool,
    delimiter: None,
    dialect: None,
    doublequote: bool,
    dtype: None,
    encoding: None,
    engine: None,
    error_bad_lines: bool,
    escapechar: None,
    false_values: None,
    float_precision: None,
    header: Literal["infer"],
    index_col: None,
    infer_datetime_format: bool,
    iterator: bool,
    keep_date_col: bool,
    keep_default_na: bool,
    kwargs: Dict[str, Union[bool, None, str]],
    lineterminator: None,
    low_memory: bool,
    mangle_dupe_cols: bool,
    memory_map: bool,
    na_filter: bool,
    na_values: None,
    names: None,
    nrows: int,
    parse_dates: bool,
    prefix: None,
    quotechar: Literal['"'],
    quoting: int,
    sep: Literal[","],
    skip_blank_lines: bool,
    skipfooter: int,
    skipinitialspace: bool,
    skiprows: None,
    squeeze: bool,
    thousands: None,
    true_values: None,
    usecols: None,
    verbose: bool,
    warn_bad_lines: bool,
):
    """
    usage.modin: 1
    """
    ...


@overload
def read_csv(filepath_or_buffer: str, header: None, usecols: List[int]):
    """
    usage.modin: 1
    """
    ...


@overload
def read_csv(
    _0: str,
    /,
    *,
    _: None,
    cache_dates: bool,
    chunksize: None,
    comment: None,
    compression: Literal["infer"],
    converters: None,
    date_parser: None,
    dayfirst: bool,
    decimal: Literal["."],
    delim_whitespace: bool,
    delimiter: None,
    dialect: None,
    doublequote: bool,
    dtype: None,
    encoding: None,
    engine: None,
    error_bad_lines: bool,
    escapechar: None,
    false_values: None,
    float_precision: None,
    header: None,
    index_col: None,
    infer_datetime_format: bool,
    iterator: bool,
    keep_date_col: bool,
    keep_default_na: bool,
    kwargs: Dict[str, Union[bool, None, List[int], str]],
    lineterminator: None,
    low_memory: bool,
    mangle_dupe_cols: bool,
    memory_map: bool,
    na_filter: bool,
    na_values: None,
    names: None,
    nrows: int,
    parse_dates: bool,
    prefix: None,
    quotechar: Literal['"'],
    quoting: int,
    sep: Literal[","],
    skip_blank_lines: bool,
    skipfooter: int,
    skipinitialspace: bool,
    skiprows: None,
    squeeze: bool,
    thousands: None,
    true_values: None,
    usecols: None,
    verbose: bool,
    warn_bad_lines: bool,
):
    """
    usage.modin: 1
    """
    ...


@overload
def read_csv(filepath_or_buffer: str, usecols: List[int]):
    """
    usage.modin: 2
    """
    ...


@overload
def read_csv(
    _0: str,
    /,
    *,
    _: None,
    cache_dates: bool,
    chunksize: None,
    comment: None,
    compression: Literal["infer"],
    converters: None,
    date_parser: None,
    dayfirst: bool,
    decimal: Literal["."],
    delim_whitespace: bool,
    delimiter: None,
    dialect: None,
    doublequote: bool,
    dtype: None,
    encoding: None,
    engine: None,
    error_bad_lines: bool,
    escapechar: None,
    false_values: None,
    float_precision: None,
    header: Literal["infer"],
    index_col: None,
    infer_datetime_format: bool,
    iterator: bool,
    keep_date_col: bool,
    keep_default_na: bool,
    kwargs: Dict[str, Union[bool, None, List[int], str]],
    lineterminator: None,
    low_memory: bool,
    mangle_dupe_cols: bool,
    memory_map: bool,
    na_filter: bool,
    na_values: None,
    names: None,
    nrows: int,
    parse_dates: bool,
    prefix: None,
    quotechar: Literal['"'],
    quoting: int,
    sep: Literal[","],
    skip_blank_lines: bool,
    skipfooter: int,
    skipinitialspace: bool,
    skiprows: None,
    squeeze: bool,
    thousands: None,
    true_values: None,
    usecols: None,
    verbose: bool,
    warn_bad_lines: bool,
):
    """
    usage.modin: 2
    """
    ...


@overload
def read_csv(filepath_or_buffer: str, names: List[int], usecols: List[int]):
    """
    usage.modin: 1
    """
    ...


@overload
def read_csv(
    _0: str,
    /,
    *,
    _: None,
    cache_dates: bool,
    chunksize: None,
    comment: None,
    compression: Literal["infer"],
    converters: None,
    date_parser: None,
    dayfirst: bool,
    decimal: Literal["."],
    delim_whitespace: bool,
    delimiter: None,
    dialect: None,
    doublequote: bool,
    dtype: None,
    encoding: None,
    engine: None,
    error_bad_lines: bool,
    escapechar: None,
    false_values: None,
    float_precision: None,
    header: Literal["infer"],
    index_col: None,
    infer_datetime_format: bool,
    iterator: bool,
    keep_date_col: bool,
    keep_default_na: bool,
    kwargs: Dict[str, Union[bool, None, List[int], str]],
    lineterminator: None,
    low_memory: bool,
    mangle_dupe_cols: bool,
    memory_map: bool,
    na_filter: bool,
    na_values: None,
    names: List[int],
    nrows: int,
    parse_dates: bool,
    prefix: None,
    quotechar: Literal['"'],
    quoting: int,
    sep: Literal[","],
    skip_blank_lines: bool,
    skipfooter: int,
    skipinitialspace: bool,
    skiprows: None,
    squeeze: bool,
    thousands: None,
    true_values: None,
    usecols: List[int],
    verbose: bool,
    warn_bad_lines: bool,
):
    """
    usage.modin: 1
    """
    ...


@overload
def read_csv(
    _0: str,
    /,
    *,
    _: None,
    cache_dates: bool,
    chunksize: None,
    comment: None,
    compression: Literal["infer"],
    converters: None,
    date_parser: None,
    dayfirst: bool,
    decimal: Literal["."],
    delim_whitespace: bool,
    delimiter: None,
    dialect: None,
    doublequote: bool,
    dtype: None,
    encoding: None,
    engine: None,
    error_bad_lines: bool,
    escapechar: None,
    false_values: None,
    float_precision: None,
    header: Literal["infer"],
    index_col: None,
    infer_datetime_format: bool,
    iterator: bool,
    keep_date_col: bool,
    keep_default_na: bool,
    kwargs: Dict[str, Union[bool, None, Literal["infer", "\t", "test.csv"]]],
    lineterminator: None,
    low_memory: bool,
    mangle_dupe_cols: bool,
    memory_map: bool,
    na_filter: bool,
    na_values: None,
    names: None,
    nrows: int,
    parse_dates: bool,
    prefix: None,
    quotechar: Literal['"'],
    quoting: int,
    sep: Literal["\t"],
    skip_blank_lines: bool,
    skipfooter: int,
    skipinitialspace: bool,
    skiprows: None,
    squeeze: bool,
    thousands: None,
    true_values: None,
    usecols: None,
    verbose: bool,
    warn_bad_lines: bool,
):
    """
    usage.modin: 1
    """
    ...


@overload
def read_csv(filepath_or_buffer: str, usecols: List[Literal["a"]]):
    """
    usage.modin: 1
    """
    ...


@overload
def read_csv(
    _0: str,
    /,
    *,
    _: None,
    cache_dates: bool,
    chunksize: None,
    comment: None,
    compression: Literal["infer"],
    converters: None,
    date_parser: None,
    dayfirst: bool,
    decimal: Literal["."],
    delim_whitespace: bool,
    delimiter: None,
    dialect: None,
    doublequote: bool,
    dtype: None,
    encoding: None,
    engine: None,
    error_bad_lines: bool,
    escapechar: None,
    false_values: None,
    float_precision: None,
    header: Literal["infer"],
    index_col: None,
    infer_datetime_format: bool,
    iterator: bool,
    keep_date_col: bool,
    keep_default_na: bool,
    kwargs: Dict[str, Union[bool, None, List[Literal["a"]], str]],
    lineterminator: None,
    low_memory: bool,
    mangle_dupe_cols: bool,
    memory_map: bool,
    na_filter: bool,
    na_values: None,
    names: None,
    nrows: int,
    parse_dates: bool,
    prefix: None,
    quotechar: Literal['"'],
    quoting: int,
    sep: Literal[","],
    skip_blank_lines: bool,
    skipfooter: int,
    skipinitialspace: bool,
    skiprows: None,
    squeeze: bool,
    thousands: None,
    true_values: None,
    usecols: None,
    verbose: bool,
    warn_bad_lines: bool,
):
    """
    usage.modin: 1
    """
    ...


@overload
def read_csv(filepath_or_buffer: str, usecols: List[Literal["e", "b", "a"]]):
    """
    usage.modin: 1
    """
    ...


@overload
def read_csv(
    _0: str,
    /,
    *,
    _: None,
    cache_dates: bool,
    chunksize: None,
    comment: None,
    compression: Literal["infer"],
    converters: None,
    date_parser: None,
    dayfirst: bool,
    decimal: Literal["."],
    delim_whitespace: bool,
    delimiter: None,
    dialect: None,
    doublequote: bool,
    dtype: None,
    encoding: None,
    engine: None,
    error_bad_lines: bool,
    escapechar: None,
    false_values: None,
    float_precision: None,
    header: Literal["infer"],
    index_col: None,
    infer_datetime_format: bool,
    iterator: bool,
    keep_date_col: bool,
    keep_default_na: bool,
    kwargs: Dict[str, Union[bool, None, List[Literal["e", "b", "a"]], str]],
    lineterminator: None,
    low_memory: bool,
    mangle_dupe_cols: bool,
    memory_map: bool,
    na_filter: bool,
    na_values: None,
    names: None,
    nrows: int,
    parse_dates: bool,
    prefix: None,
    quotechar: Literal['"'],
    quoting: int,
    sep: Literal[","],
    skip_blank_lines: bool,
    skipfooter: int,
    skipinitialspace: bool,
    skiprows: None,
    squeeze: bool,
    thousands: None,
    true_values: None,
    usecols: None,
    verbose: bool,
    warn_bad_lines: bool,
):
    """
    usage.modin: 1
    """
    ...


@overload
def read_csv(
    _0: str,
    /,
    *,
    _: None,
    cache_dates: bool,
    chunksize: None,
    comment: None,
    compression: Literal["infer"],
    converters: None,
    date_parser: None,
    dayfirst: bool,
    decimal: Literal["."],
    delim_whitespace: bool,
    delimiter: None,
    dialect: None,
    doublequote: bool,
    dtype: None,
    encoding: None,
    engine: None,
    error_bad_lines: bool,
    escapechar: None,
    false_values: None,
    float_precision: None,
    header: Literal["infer"],
    index_col: None,
    infer_datetime_format: bool,
    iterator: bool,
    keep_date_col: bool,
    keep_default_na: bool,
    kwargs: Dict[str, Union[bool, None, str]],
    lineterminator: None,
    low_memory: bool,
    mangle_dupe_cols: bool,
    memory_map: bool,
    na_filter: bool,
    na_values: None,
    names: None,
    nrows: None,
    parse_dates: bool,
    prefix: None,
    quotechar: Literal['"'],
    quoting: int,
    sep: Literal[","],
    skip_blank_lines: bool,
    skipfooter: int,
    skipinitialspace: bool,
    skiprows: None,
    squeeze: bool,
    thousands: None,
    true_values: None,
    usecols: None,
    verbose: bool,
    warn_bad_lines: bool,
):
    """
    usage.modin: 1
    """
    ...


@overload
def read_csv(
    _0: str,
    /,
    *,
    _: None,
    cache_dates: bool,
    chunksize: int,
    comment: None,
    compression: Literal["infer"],
    converters: None,
    date_parser: None,
    dayfirst: bool,
    decimal: Literal["."],
    delim_whitespace: bool,
    delimiter: None,
    dialect: None,
    doublequote: bool,
    dtype: None,
    encoding: None,
    engine: None,
    error_bad_lines: bool,
    escapechar: None,
    false_values: None,
    float_precision: None,
    header: Literal["infer"],
    index_col: None,
    infer_datetime_format: bool,
    iterator: bool,
    keep_date_col: bool,
    keep_default_na: bool,
    kwargs: Dict[str, Union[bool, None, Literal["infer", ",", "test.csv"]]],
    lineterminator: None,
    low_memory: bool,
    mangle_dupe_cols: bool,
    memory_map: bool,
    na_filter: bool,
    na_values: None,
    names: None,
    nrows: None,
    parse_dates: bool,
    prefix: None,
    quotechar: Literal['"'],
    quoting: int,
    sep: Literal[","],
    skip_blank_lines: bool,
    skipfooter: int,
    skipinitialspace: bool,
    skiprows: None,
    squeeze: bool,
    thousands: None,
    true_values: None,
    usecols: None,
    verbose: bool,
    warn_bad_lines: bool,
):
    """
    usage.modin: 1
    """
    ...


@overload
def read_csv(filepath_or_buffer: Literal["test.csv"], skiprows: int, nrows: int):
    """
    usage.modin: 1
    """
    ...


@overload
def read_csv(
    _0: str,
    /,
    *,
    _: None,
    cache_dates: bool,
    chunksize: None,
    comment: None,
    compression: Literal["infer"],
    converters: None,
    date_parser: None,
    dayfirst: bool,
    decimal: Literal["."],
    delim_whitespace: bool,
    delimiter: None,
    dialect: None,
    doublequote: bool,
    dtype: None,
    encoding: None,
    engine: None,
    error_bad_lines: bool,
    escapechar: None,
    false_values: None,
    float_precision: None,
    header: Literal["infer"],
    index_col: None,
    infer_datetime_format: bool,
    iterator: bool,
    keep_date_col: bool,
    keep_default_na: bool,
    kwargs: Dict[str, Union[bool, None, Literal["infer", ",", "test.csv"]]],
    lineterminator: None,
    low_memory: bool,
    mangle_dupe_cols: bool,
    memory_map: bool,
    na_filter: bool,
    na_values: None,
    names: None,
    nrows: int,
    parse_dates: bool,
    prefix: None,
    quotechar: Literal['"'],
    quoting: int,
    sep: Literal[","],
    skip_blank_lines: bool,
    skipfooter: int,
    skipinitialspace: bool,
    skiprows: int,
    squeeze: bool,
    thousands: None,
    true_values: None,
    usecols: None,
    verbose: bool,
    warn_bad_lines: bool,
):
    """
    usage.modin: 1
    """
    ...


@overload
def read_csv(filepath_or_buffer: Literal["test.csv"], skiprows: int, nrows: None):
    """
    usage.modin: 1
    """
    ...


@overload
def read_csv(filepath_or_buffer: Literal["test.csv"], encoding: Literal["latin8"]):
    """
    usage.modin: 1
    """
    ...


@overload
def read_csv(
    _0: str,
    /,
    *,
    _: None,
    cache_dates: bool,
    chunksize: None,
    comment: None,
    compression: Literal["infer"],
    converters: None,
    date_parser: None,
    dayfirst: bool,
    decimal: Literal["."],
    delim_whitespace: bool,
    delimiter: None,
    dialect: None,
    doublequote: bool,
    dtype: None,
    encoding: Literal["latin8"],
    engine: None,
    error_bad_lines: bool,
    escapechar: None,
    false_values: None,
    float_precision: None,
    header: Literal["infer"],
    index_col: None,
    infer_datetime_format: bool,
    iterator: bool,
    keep_date_col: bool,
    keep_default_na: bool,
    kwargs: Dict[str, Union[bool, None, Literal["infer", ",", "test.csv"]]],
    lineterminator: None,
    low_memory: bool,
    mangle_dupe_cols: bool,
    memory_map: bool,
    na_filter: bool,
    na_values: None,
    names: None,
    nrows: int,
    parse_dates: bool,
    prefix: None,
    quotechar: Literal['"'],
    quoting: int,
    sep: Literal[","],
    skip_blank_lines: bool,
    skipfooter: int,
    skipinitialspace: bool,
    skiprows: None,
    squeeze: bool,
    thousands: None,
    true_values: None,
    usecols: None,
    verbose: bool,
    warn_bad_lines: bool,
):
    """
    usage.modin: 1
    """
    ...


@overload
def read_csv(filepath_or_buffer: Literal["test.csv"], encoding: Literal["ISO-8859-1"]):
    """
    usage.modin: 1
    """
    ...


@overload
def read_csv(
    _0: str,
    /,
    *,
    _: None,
    cache_dates: bool,
    chunksize: None,
    comment: None,
    compression: Literal["infer"],
    converters: None,
    date_parser: None,
    dayfirst: bool,
    decimal: Literal["."],
    delim_whitespace: bool,
    delimiter: None,
    dialect: None,
    doublequote: bool,
    dtype: None,
    encoding: Literal["ISO-8859-1"],
    engine: None,
    error_bad_lines: bool,
    escapechar: None,
    false_values: None,
    float_precision: None,
    header: Literal["infer"],
    index_col: None,
    infer_datetime_format: bool,
    iterator: bool,
    keep_date_col: bool,
    keep_default_na: bool,
    kwargs: Dict[str, Union[bool, None, Literal["infer", ",", "test.csv"]]],
    lineterminator: None,
    low_memory: bool,
    mangle_dupe_cols: bool,
    memory_map: bool,
    na_filter: bool,
    na_values: None,
    names: None,
    nrows: int,
    parse_dates: bool,
    prefix: None,
    quotechar: Literal['"'],
    quoting: int,
    sep: Literal[","],
    skip_blank_lines: bool,
    skipfooter: int,
    skipinitialspace: bool,
    skiprows: None,
    squeeze: bool,
    thousands: None,
    true_values: None,
    usecols: None,
    verbose: bool,
    warn_bad_lines: bool,
):
    """
    usage.modin: 1
    """
    ...


@overload
def read_csv(filepath_or_buffer: Literal["test.csv"], encoding: Literal["latin1"]):
    """
    usage.modin: 1
    """
    ...


@overload
def read_csv(
    _0: str,
    /,
    *,
    _: None,
    cache_dates: bool,
    chunksize: None,
    comment: None,
    compression: Literal["infer"],
    converters: None,
    date_parser: None,
    dayfirst: bool,
    decimal: Literal["."],
    delim_whitespace: bool,
    delimiter: None,
    dialect: None,
    doublequote: bool,
    dtype: None,
    encoding: Literal["latin1"],
    engine: None,
    error_bad_lines: bool,
    escapechar: None,
    false_values: None,
    float_precision: None,
    header: Literal["infer"],
    index_col: None,
    infer_datetime_format: bool,
    iterator: bool,
    keep_date_col: bool,
    keep_default_na: bool,
    kwargs: Dict[str, Union[bool, None, Literal["infer", ",", "test.csv"]]],
    lineterminator: None,
    low_memory: bool,
    mangle_dupe_cols: bool,
    memory_map: bool,
    na_filter: bool,
    na_values: None,
    names: None,
    nrows: int,
    parse_dates: bool,
    prefix: None,
    quotechar: Literal['"'],
    quoting: int,
    sep: Literal[","],
    skip_blank_lines: bool,
    skipfooter: int,
    skipinitialspace: bool,
    skiprows: None,
    squeeze: bool,
    thousands: None,
    true_values: None,
    usecols: None,
    verbose: bool,
    warn_bad_lines: bool,
):
    """
    usage.modin: 1
    """
    ...


@overload
def read_csv(filepath_or_buffer: Literal["test.csv"], encoding: Literal["iso-8859-1"]):
    """
    usage.modin: 1
    """
    ...


@overload
def read_csv(
    _0: str,
    /,
    *,
    _: None,
    cache_dates: bool,
    chunksize: None,
    comment: None,
    compression: Literal["infer"],
    converters: None,
    date_parser: None,
    dayfirst: bool,
    decimal: Literal["."],
    delim_whitespace: bool,
    delimiter: None,
    dialect: None,
    doublequote: bool,
    dtype: None,
    encoding: Literal["iso-8859-1"],
    engine: None,
    error_bad_lines: bool,
    escapechar: None,
    false_values: None,
    float_precision: None,
    header: Literal["infer"],
    index_col: None,
    infer_datetime_format: bool,
    iterator: bool,
    keep_date_col: bool,
    keep_default_na: bool,
    kwargs: Dict[str, Union[bool, None, Literal["infer", ",", "test.csv"]]],
    lineterminator: None,
    low_memory: bool,
    mangle_dupe_cols: bool,
    memory_map: bool,
    na_filter: bool,
    na_values: None,
    names: None,
    nrows: int,
    parse_dates: bool,
    prefix: None,
    quotechar: Literal['"'],
    quoting: int,
    sep: Literal[","],
    skip_blank_lines: bool,
    skipfooter: int,
    skipinitialspace: bool,
    skiprows: None,
    squeeze: bool,
    thousands: None,
    true_values: None,
    usecols: None,
    verbose: bool,
    warn_bad_lines: bool,
):
    """
    usage.modin: 1
    """
    ...


@overload
def read_csv(filepath_or_buffer: Literal["test.csv"], encoding: Literal["cp1252"]):
    """
    usage.modin: 1
    """
    ...


@overload
def read_csv(
    _0: str,
    /,
    *,
    _: None,
    cache_dates: bool,
    chunksize: None,
    comment: None,
    compression: Literal["infer"],
    converters: None,
    date_parser: None,
    dayfirst: bool,
    decimal: Literal["."],
    delim_whitespace: bool,
    delimiter: None,
    dialect: None,
    doublequote: bool,
    dtype: None,
    encoding: Literal["cp1252"],
    engine: None,
    error_bad_lines: bool,
    escapechar: None,
    false_values: None,
    float_precision: None,
    header: Literal["infer"],
    index_col: None,
    infer_datetime_format: bool,
    iterator: bool,
    keep_date_col: bool,
    keep_default_na: bool,
    kwargs: Dict[str, Union[bool, None, Literal["infer", ",", "test.csv"]]],
    lineterminator: None,
    low_memory: bool,
    mangle_dupe_cols: bool,
    memory_map: bool,
    na_filter: bool,
    na_values: None,
    names: None,
    nrows: int,
    parse_dates: bool,
    prefix: None,
    quotechar: Literal['"'],
    quoting: int,
    sep: Literal[","],
    skip_blank_lines: bool,
    skipfooter: int,
    skipinitialspace: bool,
    skiprows: None,
    squeeze: bool,
    thousands: None,
    true_values: None,
    usecols: None,
    verbose: bool,
    warn_bad_lines: bool,
):
    """
    usage.modin: 1
    """
    ...


@overload
def read_csv(filepath_or_buffer: Literal["test.csv"], encoding: Literal["utf8"]):
    """
    usage.modin: 1
    """
    ...


@overload
def read_csv(
    _0: str,
    /,
    *,
    _: None,
    cache_dates: bool,
    chunksize: None,
    comment: None,
    compression: Literal["infer"],
    converters: None,
    date_parser: None,
    dayfirst: bool,
    decimal: Literal["."],
    delim_whitespace: bool,
    delimiter: None,
    dialect: None,
    doublequote: bool,
    dtype: None,
    encoding: Literal["utf8"],
    engine: None,
    error_bad_lines: bool,
    escapechar: None,
    false_values: None,
    float_precision: None,
    header: Literal["infer"],
    index_col: None,
    infer_datetime_format: bool,
    iterator: bool,
    keep_date_col: bool,
    keep_default_na: bool,
    kwargs: Dict[str, Union[bool, None, Literal["infer", ",", "test.csv"]]],
    lineterminator: None,
    low_memory: bool,
    mangle_dupe_cols: bool,
    memory_map: bool,
    na_filter: bool,
    na_values: None,
    names: None,
    nrows: int,
    parse_dates: bool,
    prefix: None,
    quotechar: Literal['"'],
    quoting: int,
    sep: Literal[","],
    skip_blank_lines: bool,
    skipfooter: int,
    skipinitialspace: bool,
    skiprows: None,
    squeeze: bool,
    thousands: None,
    true_values: None,
    usecols: None,
    verbose: bool,
    warn_bad_lines: bool,
):
    """
    usage.modin: 1
    """
    ...


@overload
def read_csv(
    _0: _io.StringIO,
    /,
    *,
    _: None,
    cache_dates: bool,
    chunksize: None,
    comment: None,
    compression: Literal["infer"],
    converters: None,
    date_parser: None,
    dayfirst: bool,
    decimal: Literal["."],
    delim_whitespace: bool,
    delimiter: None,
    dialect: None,
    doublequote: bool,
    dtype: None,
    encoding: None,
    engine: None,
    error_bad_lines: bool,
    escapechar: None,
    false_values: None,
    float_precision: None,
    header: Literal["infer"],
    index_col: None,
    infer_datetime_format: bool,
    iterator: bool,
    keep_date_col: bool,
    keep_default_na: bool,
    kwargs: Dict[str, Union[bool, _io.StringIO, None, Literal["infer", ","]]],
    lineterminator: None,
    low_memory: bool,
    mangle_dupe_cols: bool,
    memory_map: bool,
    na_filter: bool,
    na_values: None,
    names: None,
    nrows: None,
    parse_dates: bool,
    prefix: None,
    quotechar: Literal['"'],
    quoting: int,
    sep: Literal[","],
    skip_blank_lines: bool,
    skipfooter: int,
    skipinitialspace: bool,
    skiprows: None,
    squeeze: bool,
    thousands: None,
    true_values: None,
    usecols: None,
    verbose: bool,
    warn_bad_lines: bool,
):
    """
    usage.modin: 1
    """
    ...


@overload
def read_csv(
    filepath_or_buffer: Literal["test.csv"], index_col: Literal["col1"], nrows: int
):
    """
    usage.modin: 1
    """
    ...


@overload
def read_csv(
    _0: str,
    /,
    *,
    _: None,
    cache_dates: bool,
    chunksize: None,
    comment: None,
    compression: Literal["infer"],
    converters: None,
    date_parser: None,
    dayfirst: bool,
    decimal: Literal["."],
    delim_whitespace: bool,
    delimiter: None,
    dialect: None,
    doublequote: bool,
    dtype: None,
    encoding: None,
    engine: None,
    error_bad_lines: bool,
    escapechar: None,
    false_values: None,
    float_precision: None,
    header: Literal["infer"],
    index_col: None,
    infer_datetime_format: bool,
    iterator: bool,
    keep_date_col: bool,
    keep_default_na: bool,
    kwargs: Dict[str, Union[bool, None, Literal["col1", "infer", ",", "test.csv"]]],
    lineterminator: None,
    low_memory: bool,
    mangle_dupe_cols: bool,
    memory_map: bool,
    na_filter: bool,
    na_values: None,
    names: None,
    nrows: int,
    parse_dates: bool,
    prefix: None,
    quotechar: Literal['"'],
    quoting: int,
    sep: Literal[","],
    skip_blank_lines: bool,
    skipfooter: int,
    skipinitialspace: bool,
    skiprows: None,
    squeeze: bool,
    thousands: None,
    true_values: None,
    usecols: None,
    verbose: bool,
    warn_bad_lines: bool,
):
    """
    usage.modin: 1
    """
    ...


@overload
def read_csv(
    filepath_or_buffer: Literal["test.csv"], index_col: Literal["col1"], nrows: None
):
    """
    usage.modin: 1
    """
    ...


@overload
def read_csv(filepath_or_buffer: Literal["test.csv"], skipfooter: int):
    """
    usage.modin: 1
    """
    ...


@overload
def read_csv(
    filepath_or_buffer: Literal["test.csv"],
    parse_dates: List[List[Literal["col4", "col2"]]],
):
    """
    usage.modin: 1
    """
    ...


@overload
def read_csv(
    _0: str,
    /,
    *,
    _: None,
    cache_dates: bool,
    chunksize: None,
    comment: None,
    compression: Literal["infer"],
    converters: None,
    date_parser: None,
    dayfirst: bool,
    decimal: Literal["."],
    delim_whitespace: bool,
    delimiter: None,
    dialect: None,
    doublequote: bool,
    dtype: None,
    encoding: None,
    engine: None,
    error_bad_lines: bool,
    escapechar: None,
    false_values: None,
    float_precision: None,
    header: Literal["infer"],
    index_col: None,
    infer_datetime_format: bool,
    iterator: bool,
    keep_date_col: bool,
    keep_default_na: bool,
    kwargs: Dict[str, Union[bool, None, Literal["infer", ",", "test.csv"]]],
    lineterminator: None,
    low_memory: bool,
    mangle_dupe_cols: bool,
    memory_map: bool,
    na_filter: bool,
    na_values: None,
    names: None,
    nrows: int,
    parse_dates: List[List[Literal["col4", "col2"]]],
    prefix: None,
    quotechar: Literal['"'],
    quoting: int,
    sep: Literal[","],
    skip_blank_lines: bool,
    skipfooter: int,
    skipinitialspace: bool,
    skiprows: None,
    squeeze: bool,
    thousands: None,
    true_values: None,
    usecols: None,
    verbose: bool,
    warn_bad_lines: bool,
):
    """
    usage.modin: 1
    """
    ...


@overload
def read_csv(*, nrows: int, path: str, skiprows: int):
    """
    usage.modin: 1
    """
    ...


@overload
def read_csv(*, nrows: None, path: str, skiprows: int):
    """
    usage.modin: 1
    """
    ...


@overload
def read_csv(*, nrows: int, path: str, skiprows: None):
    """
    usage.modin: 1
    """
    ...


@overload
def read_csv(*, nrows: None, path: str, skiprows: None):
    """
    usage.modin: 1
    """
    ...


@overload
def read_csv(
    _0: str,
    /,
    *,
    _: None,
    cache_dates: bool,
    chunksize: None,
    comment: None,
    compression: Literal["infer"],
    converters: None,
    date_parser: None,
    dayfirst: bool,
    decimal: Literal["."],
    delim_whitespace: bool,
    delimiter: None,
    dialect: None,
    doublequote: bool,
    dtype: None,
    encoding: None,
    engine: None,
    error_bad_lines: bool,
    escapechar: None,
    false_values: None,
    float_precision: None,
    header: List[int],
    index_col: None,
    infer_datetime_format: bool,
    iterator: bool,
    keep_date_col: bool,
    keep_default_na: bool,
    kwargs: Dict[str, Union[bool, int, None, List[int], str]],
    lineterminator: None,
    low_memory: bool,
    mangle_dupe_cols: bool,
    memory_map: bool,
    na_filter: bool,
    na_values: None,
    names: None,
    nrows: int,
    parse_dates: bool,
    prefix: None,
    quotechar: Literal['"'],
    quoting: int,
    sep: Literal[","],
    skip_blank_lines: bool,
    skipfooter: int,
    skipinitialspace: bool,
    skiprows: None,
    squeeze: bool,
    thousands: None,
    true_values: None,
    usecols: None,
    verbose: bool,
    warn_bad_lines: bool,
):
    """
    usage.modin: 1
    """
    ...


@overload
def read_csv(
    _0: str,
    /,
    *,
    _: None,
    cache_dates: bool,
    chunksize: None,
    comment: None,
    compression: Literal["infer"],
    converters: None,
    date_parser: None,
    dayfirst: bool,
    decimal: Literal["."],
    delim_whitespace: bool,
    delimiter: None,
    dialect: None,
    doublequote: bool,
    dtype: None,
    encoding: None,
    engine: None,
    error_bad_lines: bool,
    escapechar: None,
    false_values: None,
    float_precision: None,
    header: Literal["infer"],
    index_col: None,
    infer_datetime_format: bool,
    iterator: bool,
    keep_date_col: bool,
    keep_default_na: bool,
    kwargs: Dict[str, Union[bool, None, Literal["infer", ",", "200kx99.csv"]]],
    lineterminator: None,
    low_memory: bool,
    mangle_dupe_cols: bool,
    memory_map: bool,
    na_filter: bool,
    na_values: None,
    names: None,
    nrows: int,
    parse_dates: bool,
    prefix: None,
    quotechar: Literal['"'],
    quoting: int,
    sep: Literal[","],
    skip_blank_lines: bool,
    skipfooter: int,
    skipinitialspace: bool,
    skiprows: None,
    squeeze: bool,
    thousands: None,
    true_values: None,
    usecols: None,
    verbose: bool,
    warn_bad_lines: bool,
):
    """
    usage.modin: 1
    """
    ...


@overload
def read_csv(filepath_or_buffer: _io.BytesIO):
    """
    usage.dask: 4
    """
    ...


@overload
def read_csv(filepath_or_buffer: _io.BytesIO, usecols: List[Literal["id", "name"]]):
    """
    usage.dask: 1
    """
    ...


@overload
def read_csv(filepath_or_buffer: _io.BytesIO, skiprows: int):
    """
    usage.dask: 2
    """
    ...


@overload
def read_csv(filepath_or_buffer: Literal["2014-01-01.csv"], skiprows: int):
    """
    usage.dask: 1
    """
    ...


@overload
def read_csv(filepath_or_buffer: Literal["2014-01-02.csv"], skiprows: int):
    """
    usage.dask: 1
    """
    ...


@overload
def read_csv(filepath_or_buffer: Literal["2014-01-03.csv"], skiprows: int):
    """
    usage.dask: 1
    """
    ...


@overload
def read_csv(filepath_or_buffer: _io.BytesIO, skiprows: List[int]):
    """
    usage.dask: 2
    """
    ...


@overload
def read_csv(filepath_or_buffer: Literal["2014-01-01.csv"], skiprows: List[int]):
    """
    usage.dask: 1
    """
    ...


@overload
def read_csv(filepath_or_buffer: Literal["2014-01-02.csv"], skiprows: List[int]):
    """
    usage.dask: 1
    """
    ...


@overload
def read_csv(filepath_or_buffer: Literal["2014-01-03.csv"], skiprows: List[int]):
    """
    usage.dask: 1
    """
    ...


@overload
def read_csv(filepath_or_buffer: _io.BytesIO, header: int):
    """
    usage.dask: 3
    """
    ...


@overload
def read_csv(
    filepath_or_buffer: _io.BytesIO, sep: Literal[","], lineterminator: Literal["\n"]
):
    """
    usage.dask: 2
    """
    ...


@overload
def read_csv(filepath_or_buffer: Literal["/tmp/tmp4vq8g9jj."], sep: Literal[","]):
    """
    usage.dask: 1
    """
    ...


@overload
def read_csv(
    filepath_or_buffer: _io.BytesIO,
    names: List[Literal["amount", "name"]],
    skiprows: int,
):
    """
    usage.dask: 2
    """
    ...


@overload
def read_csv(
    filepath_or_buffer: Literal["/tmp/tmpvx5igyqk."],
    names: List[Literal["amount", "name"]],
    skiprows: int,
):
    """
    usage.dask: 1
    """
    ...


@overload
def read_csv(
    filepath_or_buffer: Literal["/tmp/tmp2i4lyzjn."],
    names: List[Literal["amount", "name"]],
    skiprows: int,
):
    """
    usage.dask: 1
    """
    ...


@overload
def read_csv(
    filepath_or_buffer: _io.BytesIO, converters: Dict[Literal["path"], Callable]
):
    """
    usage.dask: 1
    """
    ...


@overload
def read_csv(
    filepath_or_buffer: _io.BytesIO, converters: Dict[Literal["filename"], Callable]
):
    """
    usage.dask: 1
    """
    ...


@overload
def read_csv(filepath_or_buffer: Literal["/tmp/tmpaeer2a5e."]):
    """
    usage.dask: 1
    """
    ...


@overload
def read_csv(filepath_or_buffer: _io.BytesIO, skiprows: range):
    """
    usage.dask: 2
    """
    ...


@overload
def read_csv(filepath_or_buffer: Literal["/tmp/tmpbjftivtd."], skiprows: range):
    """
    usage.dask: 1
    """
    ...


@overload
def read_csv(filepath_or_buffer: _io.BytesIO, usecols: List[Literal["Low", "High"]]):
    """
    usage.dask: 1
    """
    ...


@overload
def read_csv(
    filepath_or_buffer: Literal["/tmp/tmpik_2a1p4."],
    usecols: List[Literal["Low", "High"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def read_csv(filepath_or_buffer: _io.BytesIO, skipinitialspace: bool):
    """
    usage.dask: 1
    """
    ...


@overload
def read_csv(
    filepath_or_buffer: _io.BytesIO, dtype: Dict[Literal["fruit"], Literal["category"]]
):
    """
    usage.dask: 1
    """
    ...


@overload
def read_csv(
    filepath_or_buffer: _io.BytesIO, dtype: Dict[Literal["B", "A"], Literal["category"]]
):
    """
    usage.dask: 2
    """
    ...


@overload
def read_csv(
    filepath_or_buffer: _io.BytesIO,
    dtype: Dict[
        Literal["B", "A"],
        Union[Literal["category"], pandas.core.dtypes.dtypes.CategoricalDtype],
    ],
):
    """
    usage.dask: 2
    """
    ...


@overload
def read_csv(
    filepath_or_buffer: _io.BytesIO, dtype: pandas.core.dtypes.dtypes.CategoricalDtype
):
    """
    usage.dask: 1
    """
    ...


@overload
def read_csv(filepath_or_buffer: _io.BytesIO, dtype: Literal["category"]):
    """
    usage.dask: 1
    """
    ...


@overload
def read_csv(filepath_or_buffer: _io.BytesIO, header: None):
    """
    usage.dask: 2
    """
    ...


@overload
def read_csv(filepath_or_buffer: _io.BytesIO, skiprows: int, na_values: List[int]):
    """
    usage.dask: 1
    """
    ...


@overload
def read_csv(filepath_or_buffer: Literal["/tmp/tmptmvmud8v."]):
    """
    usage.dask: 1
    """
    ...


@overload
def read_csv(filepath_or_buffer: _io.BytesIO, parse_dates: List[Literal["dates"]]):
    """
    usage.dask: 2
    """
    ...


@overload
def read_csv(
    filepath_or_buffer: _io.BytesIO, dtype: Dict[Literal["names"], Literal["O"]]
):
    """
    usage.dask: 2
    """
    ...


@overload
def read_csv(
    filepath_or_buffer: _io.BytesIO,
    dtype: Dict[Literal["names"], Literal["O"]],
    parse_dates: List[Literal["dates"]],
):
    """
    usage.dask: 2
    """
    ...


@overload
def read_csv(
    filepath_or_buffer: _io.BytesIO,
    dtype: Dict[Literal["numbers", "names", "more_numbers"], type],
    parse_dates: List[Literal["dates"]],
):
    """
    usage.dask: 2
    """
    ...


@overload
def read_csv(
    filepath_or_buffer: _io.BytesIO,
    dtype: Dict[Literal["numbers", "names", "more_numbers"], type],
):
    """
    usage.dask: 2
    """
    ...


@overload
def read_csv(filepath_or_buffer: Literal["/tmp/tmpl_zgedi3."]):
    """
    usage.dask: 1
    """
    ...


@overload
def read_csv(
    filepath_or_buffer: _io.BytesIO, dtype: Dict[Literal["integers"], Literal["int64"]]
):
    """
    usage.dask: 2
    """
    ...


@overload
def read_csv(filepath_or_buffer: _io.BytesIO, dtype: None):
    """
    usage.dask: 2
    """
    ...


@overload
def read_csv(filepath_or_buffer: Literal["/tmp/tmp83cqpbze."]):
    """
    usage.dask: 1
    """
    ...


@overload
def read_csv(filepath_or_buffer: _io.BytesIO, dtype: Literal["int64"]):
    """
    usage.dask: 1
    """
    ...


@overload
def read_csv(
    filepath_or_buffer: Literal["/tmp/tmp1pr16xcl."],
    header: int,
    index_col: int,
    usecols: List[int],
    parse_dates: List[Literal["Date"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def read_csv(
    filepath_or_buffer: _io.BytesIO,
    header: int,
    usecols: List[int],
    parse_dates: List[Literal["Date"]],
):
    """
    usage.dask: 2
    """
    ...


@overload
def read_csv(
    filepath_or_buffer: Literal["/tmp/tmp3ojwelzj."],
    header: int,
    index_col: int,
    usecols: List[int],
    parse_dates: List[Literal["Date"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def read_csv(
    filepath_or_buffer: Literal["/tmp/tmptwszhbso.csv"], encoding: Literal["utf-16"]
):
    """
    usage.dask: 1
    """
    ...


@overload
def read_csv(filepath_or_buffer: _io.BytesIO, encoding: Literal["utf-16"]):
    """
    usage.dask: 1
    """
    ...


@overload
def read_csv(
    filepath_or_buffer: Literal["/tmp/tmpsu6hgqwx.csv"], encoding: Literal["utf-16-le"]
):
    """
    usage.dask: 1
    """
    ...


@overload
def read_csv(filepath_or_buffer: _io.BytesIO, encoding: Literal["utf-16-le"]):
    """
    usage.dask: 1
    """
    ...


@overload
def read_csv(
    filepath_or_buffer: Literal["/tmp/tmphbpetj19.csv"], encoding: Literal["utf-16-be"]
):
    """
    usage.dask: 1
    """
    ...


@overload
def read_csv(filepath_or_buffer: _io.BytesIO, encoding: Literal["utf-16-be"]):
    """
    usage.dask: 1
    """
    ...


@overload
def read_csv(filepath_or_buffer: _io.BytesIO, sep: Literal["\t"]):
    """
    usage.dask: 2
    """
    ...


@overload
def read_csv(filepath_or_buffer: Literal["/tmp/tmpim2gt4pg."], sep: Literal["\t"]):
    """
    usage.dask: 1
    """
    ...


@overload
def read_csv(filepath_or_buffer: _io.BytesIO, delimiter: Literal["\t"]):
    """
    usage.dask: 2
    """
    ...


@overload
def read_csv(
    filepath_or_buffer: Literal["/tmp/tmpim2gt4pg."], delimiter: Literal["\t"]
):
    """
    usage.dask: 1
    """
    ...


@overload
def read_csv(filepath_or_buffer: _io.BytesIO, usecols: None):
    """
    usage.dask: 2
    """
    ...


@overload
def read_csv(filepath_or_buffer: Literal["/tmp/tmp0zzt5eus."], usecols: None):
    """
    usage.dask: 1
    """
    ...


@overload
def read_csv(
    filepath_or_buffer: _io.BytesIO, parse_dates: List[List[Literal["time", "date"]]]
):
    """
    usage.dask: 1
    """
    ...


@overload
def read_csv(
    filepath_or_buffer: Literal["/tmp/tmp7c7vg6tx."],
    parse_dates: List[List[Literal["time", "date"]]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def read_csv(
    filepath_or_buffer: _io.BytesIO, sep: Literal["###"], engine: Literal["python"]
):
    """
    usage.dask: 1
    """
    ...


@overload
def read_csv(
    filepath_or_buffer: Literal["/tmp/tmpn2eyivvm."],
    sep: Literal["###"],
    engine: Literal["python"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def read_csv(
    filepath_or_buffer: _io.BytesIO,
    sep: Literal[","],
    header: None,
    names: List[Literal["b", "a"]],
    lineterminator: Literal["\n"],
):
    """
    usage.dask: 2
    """
    ...


@overload
def read_csv(filepath_or_buffer: Literal["/tmp/tmprnk3u5_v."], dtype: Type[float]):
    """
    usage.dask: 1
    """
    ...


@overload
def read_csv(filepath_or_buffer: _io.BytesIO, dtype: Type[float]):
    """
    usage.dask: 2
    """
    ...


@overload
def read_csv(filepath_or_buffer: Literal["2014-01-01.csv"]):
    """
    usage.dask: 1
    """
    ...


@overload
def read_csv(filepath_or_buffer: Literal["/tmp/tmpfdqvmpl_."], header: None):
    """
    usage.dask: 1
    """
    ...


@overload
def read_csv(filepath_or_buffer: _io.BytesIO, header: None, skiprows: int):
    """
    usage.dask: 2
    """
    ...


@overload
def read_csv(
    filepath_or_buffer: Literal["/tmp/tmp4podujwu."], header: None, skiprows: int
):
    """
    usage.dask: 1
    """
    ...


@overload
def read_csv(filepath_or_buffer: _io.BytesIO, names: List[Literal["amount", "name"]]):
    """
    usage.dask: 2
    """
    ...


@overload
def read_csv(
    filepath_or_buffer: Literal["/tmp/tmpjct67blz."],
    names: List[Literal["amount", "name"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def read_csv(filepath_or_buffer: str, compression: Literal["gzip"]):
    """
    usage.dask: 1
    """
    ...


@overload
def read_csv(
    filepath_or_buffer: Literal["/tmp/tmpa1kne80b.csv"],
    index_col: int,
    compression: Literal["gzip"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def read_csv(filepath_or_buffer: _io.BytesIO, header: None, names: List[Literal["x"]]):
    """
    usage.dask: 1
    """
    ...


def read_csv(
    _0: Union[str, _io.StringIO] = ...,
    /,
    filepath_or_buffer: Union[str, _io.BytesIO, _io.StringIO] = ...,
    skipfooter: int = ...,
    encoding: Union[str, None] = ...,
    sep: Union[Literal[",", "###", "\t", ";", "\\s"], None] = ...,
    engine: Union[Literal["python", "c"], None] = ...,
    delimiter: Union[Literal["\t", "\\s+"], None] = ...,
    header: Union[int, None, Literal["infer"], List[int]] = ...,
    names: Union[List[Union[str, int]], None] = ...,
    lineterminator: Union[None, Literal["\n"]] = ...,
    skiprows: Union[List[int], range, int, None] = ...,
    na_values: Union[None, List[int]] = ...,
    dtype: Union[
        None,
        pandas.core.dtypes.dtypes.CategoricalDtype,
        Dict[
            str,
            Union[
                Literal["category", "int64", "O"],
                type,
                pandas.core.dtypes.dtypes.CategoricalDtype,
            ],
        ],
        Literal["int64", "category"],
        Type[float],
    ] = ...,
    index_col: Union[int, None, Literal["col1", "Row.names"]] = ...,
    compression: Literal["infer", "zip", "xz", "bz2", "gzip"] = ...,
    usecols: Union[List[Union[int, str]], None] = ...,
    parse_dates: Union[
        List[
            Union[
                List[Literal["time", "date", "col4", "col2"]], Literal["dates", "Date"]
            ]
        ],
        bool,
    ] = ...,
    nrows: Union[int, None] = ...,
    quoting: int = ...,
    *,
    _: None = ...,
    cache_dates: bool = ...,
    chunksize: Union[None, int] = ...,
    comment: None = ...,
    date_parser: None = ...,
    dayfirst: bool = ...,
    decimal: Literal["."] = ...,
    delim_whitespace: bool = ...,
    dialect: None = ...,
    doublequote: bool = ...,
    error_bad_lines: bool = ...,
    escapechar: None = ...,
    false_values: None = ...,
    infer_datetime_format: bool = ...,
    iterator: bool = ...,
    keep_date_col: bool = ...,
    keep_default_na: bool = ...,
    kwargs: Dict[str, object] = ...,
    low_memory: bool = ...,
    mangle_dupe_cols: bool = ...,
    memory_map: bool = ...,
    na_filter: bool = ...,
    prefix: None = ...,
    quotechar: Literal['"'] = ...,
    skip_blank_lines: bool = ...,
    squeeze: bool = ...,
    thousands: None = ...,
    true_values: None = ...,
    verbose: bool = ...,
    warn_bad_lines: bool = ...,
    path: str = ...,
):
    """
    usage.dask: 101
    usage.modin: 68
    usage.seaborn: 1
    usage.statsmodels: 44
    """
    ...


@overload
def read_fwf(
    filepath_or_buffer: str,
    colspecs: List[Tuple[int, int]],
    widths: None,
    infer_nrows: int,
):
    """
    usage.modin: 3
    """
    ...


@overload
def read_fwf(
    filepath_or_buffer: str,
    colspecs: Literal["infer"],
    widths: List[int],
    infer_nrows: int,
):
    """
    usage.modin: 1
    """
    ...


@overload
def read_fwf(filepath_or_buffer: Literal["test_fwf.txt"]):
    """
    usage.modin: 6
    """
    ...


@overload
def read_fwf(
    filepath_or_buffer: str, colspecs: Literal["infer"], widths: None, infer_nrows: int
):
    """
    usage.modin: 3
    """
    ...


@overload
def read_fwf(
    filepath_or_buffer: _io.BufferedReader,
    colspecs: Literal["infer"],
    widths: None,
    infer_nrows: int,
):
    """
    usage.modin: 1
    """
    ...


@overload
def read_fwf(filepath_or_buffer: _io.BytesIO):
    """
    usage.dask: 1
    """
    ...


def read_fwf(
    filepath_or_buffer: Union[_io.BytesIO, _io.BufferedReader, str],
    colspecs: Union[Literal["infer"], List[Tuple[int, int]]] = ...,
    widths: Union[None, List[int]] = ...,
    infer_nrows: int = ...,
):
    """
    usage.dask: 1
    usage.modin: 14
    """
    ...


@overload
def read_table(filepath_or_buffer: Literal["test.csv"]):
    """
    usage.modin: 1
    """
    ...


@overload
def read_table(filepath_or_buffer: _io.BytesIO):
    """
    usage.dask: 4
    """
    ...


@overload
def read_table(filepath_or_buffer: _io.BytesIO, usecols: List[Literal["id", "name"]]):
    """
    usage.dask: 1
    """
    ...


@overload
def read_table(filepath_or_buffer: _io.BytesIO, skiprows: int):
    """
    usage.dask: 2
    """
    ...


@overload
def read_table(filepath_or_buffer: Literal["2014-01-01.csv"], skiprows: int):
    """
    usage.dask: 1
    """
    ...


@overload
def read_table(filepath_or_buffer: Literal["2014-01-02.csv"], skiprows: int):
    """
    usage.dask: 1
    """
    ...


@overload
def read_table(filepath_or_buffer: Literal["2014-01-03.csv"], skiprows: int):
    """
    usage.dask: 1
    """
    ...


@overload
def read_table(filepath_or_buffer: _io.BytesIO, skiprows: List[int]):
    """
    usage.dask: 2
    """
    ...


@overload
def read_table(filepath_or_buffer: Literal["2014-01-01.csv"], skiprows: List[int]):
    """
    usage.dask: 1
    """
    ...


@overload
def read_table(filepath_or_buffer: Literal["2014-01-02.csv"], skiprows: List[int]):
    """
    usage.dask: 1
    """
    ...


@overload
def read_table(filepath_or_buffer: Literal["2014-01-03.csv"], skiprows: List[int]):
    """
    usage.dask: 1
    """
    ...


@overload
def read_table(filepath_or_buffer: _io.BytesIO, header: int):
    """
    usage.dask: 2
    """
    ...


@overload
def read_table(
    filepath_or_buffer: _io.BytesIO, sep: Literal["\t"], lineterminator: Literal["\n"]
):
    """
    usage.dask: 2
    """
    ...


@overload
def read_table(filepath_or_buffer: Literal["/tmp/tmp1_iex77n."], sep: Literal["\t"]):
    """
    usage.dask: 1
    """
    ...


@overload
def read_table(
    filepath_or_buffer: _io.BytesIO, sep: Literal["\\s+"], lineterminator: Literal["\n"]
):
    """
    usage.dask: 2
    """
    ...


@overload
def read_table(filepath_or_buffer: Literal["/tmp/tmpxx48veym."], sep: Literal["\\s+"]):
    """
    usage.dask: 1
    """
    ...


@overload
def read_table(
    filepath_or_buffer: _io.BytesIO,
    names: List[Literal["amount", "name"]],
    skiprows: List[int],
):
    """
    usage.dask: 2
    """
    ...


@overload
def read_table(
    filepath_or_buffer: Literal["/tmp/tmp52s3u4dg."],
    names: List[Literal["amount", "name"]],
    skiprows: List[int],
):
    """
    usage.dask: 1
    """
    ...


@overload
def read_table(
    filepath_or_buffer: Literal["/tmp/tmp7jjvwm9p."],
    names: List[Literal["amount", "name"]],
    skiprows: List[int],
):
    """
    usage.dask: 1
    """
    ...


@overload
def read_table(
    filepath_or_buffer: _io.BytesIO, converters: Dict[Literal["path"], Callable]
):
    """
    usage.dask: 1
    """
    ...


@overload
def read_table(
    filepath_or_buffer: _io.BytesIO, converters: Dict[Literal["filename"], Callable]
):
    """
    usage.dask: 1
    """
    ...


def read_table(
    filepath_or_buffer: Union[str, _io.BytesIO],
    names: List[Literal["amount", "name"]] = ...,
    skiprows: Union[List[int], int] = ...,
    sep: Literal["\\s+", "\t"] = ...,
    lineterminator: Literal["\n"] = ...,
):
    """
    usage.dask: 29
    usage.modin: 1
    """
    ...


class TextFileReader:
    def read(self, /, nrows: int):
        """
        usage.modin: 1
        """
        ...
