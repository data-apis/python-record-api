from typing import *


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
def read_csv(filepath_or_buffer: Literal["/tmp/tmpaaqg3bt5."], sep: Literal[","]):
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
    filepath_or_buffer: Literal["/tmp/tmp0cdg5he1."],
    names: List[Literal["amount", "name"]],
    skiprows: int,
):
    """
    usage.dask: 1
    """
    ...


@overload
def read_csv(
    filepath_or_buffer: Literal["/tmp/tmpa2131h2g."],
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
def read_csv(filepath_or_buffer: Literal["/tmp/tmpmileug70."]):
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
def read_csv(filepath_or_buffer: Literal["/tmp/tmpwjmrqbqz."], skiprows: range):
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
    filepath_or_buffer: Literal["/tmp/tmp8rcggz5q."],
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
def read_csv(filepath_or_buffer: Literal["/tmp/tmpi92gaehf."]):
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
def read_csv(filepath_or_buffer: Literal["/tmp/tmpo0nml9pp."]):
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
def read_csv(filepath_or_buffer: Literal["/tmp/tmpayak2gmh."]):
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
    filepath_or_buffer: Literal["/tmp/tmp0____npy."],
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
    filepath_or_buffer: Literal["/tmp/tmpa8vxszi_."],
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
    filepath_or_buffer: Literal["/tmp/tmp12pxwjdr.csv"], encoding: Literal["utf-16"]
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
    filepath_or_buffer: Literal["/tmp/tmpigl0owvd.csv"], encoding: Literal["utf-16-le"]
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
    filepath_or_buffer: Literal["/tmp/tmpd3mrm6x7.csv"], encoding: Literal["utf-16-be"]
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
def read_csv(filepath_or_buffer: Literal["/tmp/tmpdy3f365u."], sep: Literal["\t"]):
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
    filepath_or_buffer: Literal["/tmp/tmpdy3f365u."], delimiter: Literal["\t"]
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
def read_csv(filepath_or_buffer: Literal["/tmp/tmp_hxghznl."], usecols: None):
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
    filepath_or_buffer: Literal["/tmp/tmp4u6hx8pe."],
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
    filepath_or_buffer: Literal["/tmp/tmpeowek22_."],
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
def read_csv(filepath_or_buffer: Literal["/tmp/tmpmv0cd4d8."], dtype: Type[float]):
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
def read_csv(filepath_or_buffer: Literal["/tmp/tmpcz1m0kuu."], header: None):
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
    filepath_or_buffer: Literal["/tmp/tmpmfmeism0."], header: None, skiprows: int
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
    filepath_or_buffer: Literal["/tmp/tmpejaftmnx."],
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
    filepath_or_buffer: Literal["/tmp/tmpqpa91aoq.csv"],
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
    filepath_or_buffer: Union[_io.BytesIO, str],
    dtype: Union[
        Type[float],
        Literal["int64", "category"],
        Dict[
            str,
            Union[
                pandas.core.dtypes.dtypes.CategoricalDtype,
                Literal["category", "O", "int64"],
                type,
            ],
        ],
        pandas.core.dtypes.dtypes.CategoricalDtype,
        None,
    ] = ...,
    sep: Literal[",", "###", "\t"] = ...,
    header: Union[None, int] = ...,
    names: List[Literal["amount", "name", "b", "a", "x"]] = ...,
    lineterminator: Literal["\n"] = ...,
    skiprows: Union[int, range, List[int]] = ...,
    na_values: List[int] = ...,
    index_col: int = ...,
    compression: Literal["gzip"] = ...,
    usecols: Union[None, List[Union[Literal["id", "name", "Low", "High"], int]]] = ...,
    parse_dates: List[
        Union[List[Literal["time", "date"]], Literal["dates", "Date"]]
    ] = ...,
    engine: Literal["python"] = ...,
):
    """
    usage.dask: 101
    """
    ...


def read_fwf(filepath_or_buffer: _io.BytesIO):
    """
    usage.dask: 1
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
def read_table(filepath_or_buffer: Literal["/tmp/tmp3bzhsdib."], sep: Literal["\t"]):
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
def read_table(filepath_or_buffer: Literal["/tmp/tmprl0wgi_k."], sep: Literal["\\s+"]):
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
    filepath_or_buffer: Literal["/tmp/tmpy5308jfo."],
    names: List[Literal["amount", "name"]],
    skiprows: List[int],
):
    """
    usage.dask: 1
    """
    ...


@overload
def read_table(
    filepath_or_buffer: Literal["/tmp/tmpdxee0ld9."],
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
    filepath_or_buffer: Union[_io.BytesIO, str],
    names: List[Literal["amount", "name"]] = ...,
    skiprows: Union[List[int], int] = ...,
    sep: Literal["\\s+", "\t"] = ...,
    lineterminator: Literal["\n"] = ...,
):
    """
    usage.dask: 29
    """
    ...
