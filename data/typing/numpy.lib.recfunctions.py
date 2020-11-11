from typing import *


@overload
def append_fields(
    base: numpy.recarray,
    names: List[
        Literal[
            "instrument_5.0",
            "instrument_4.0",
            "instrument_3.0",
            "instrument_2.0",
            "instrument_1.0",
        ]
    ],
    data: numpy.ndarray,
    usemask: bool,
    asrecarray: bool,
):
    """
    usage.statsmodels: 2
    """
    ...


@overload
def append_fields(
    base: numpy.recarray,
    names: List[Literal["var_5.0", "var_4.0", "var_3.0", "var_2.0", "var_1.0"]],
    data: numpy.ndarray,
    usemask: bool,
    asrecarray: bool,
):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def append_fields(
    base: numpy.ndarray,
    names: List[
        Literal[
            "instrument_5.0",
            "instrument_4.0",
            "instrument_3.0",
            "instrument_2.0",
            "instrument_1.0",
        ]
    ],
    data: numpy.ndarray,
    usemask: bool,
    asrecarray: bool,
):
    """
    usage.statsmodels: 2
    """
    ...


@overload
def append_fields(
    base: numpy.ndarray,
    names: List[Literal["var1_5.0", "var1_4.0", "var1_3.0", "var1_2.0", "var1_1.0"]],
    data: numpy.ndarray,
    usemask: bool,
    asrecarray: bool,
):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def append_fields(
    base: numpy.recarray,
    names: List[
        Literal[
            "str_instr_uvwxy",
            "str_instr_pqrst",
            "str_instr_klmno",
            "str_instr_fghij",
            "str_instr_abcde",
        ]
    ],
    data: numpy.ndarray,
    usemask: bool,
    asrecarray: bool,
):
    """
    usage.statsmodels: 2
    """
    ...


@overload
def append_fields(
    base: numpy.recarray,
    names: List[
        Literal["var_uvwxy", "var_pqrst", "var_klmno", "var_fghij", "var_abcde"]
    ],
    data: numpy.ndarray,
    usemask: bool,
    asrecarray: bool,
):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def append_fields(
    base: numpy.ndarray,
    names: List[
        Literal[
            "str_instr_uvwxy",
            "str_instr_pqrst",
            "str_instr_klmno",
            "str_instr_fghij",
            "str_instr_abcde",
        ]
    ],
    data: numpy.ndarray,
    usemask: bool,
    asrecarray: bool,
):
    """
    usage.statsmodels: 2
    """
    ...


@overload
def append_fields(
    base: numpy.ndarray,
    names: List[
        Literal["var1_uvwxy", "var1_pqrst", "var1_klmno", "var1_fghij", "var1_abcde"]
    ],
    data: numpy.ndarray,
    usemask: bool,
    asrecarray: bool,
):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def append_fields(
    base: numpy.recarray,
    names: List[Literal["group_11", "group_10"]],
    data: numpy.ndarray,
    usemask: bool,
    asrecarray: bool,
):
    """
    usage.statsmodels: 2
    """
    ...


@overload
def append_fields(
    base: numpy.ndarray,
    names: List[Literal["variable_L(3)", "variable_L(2)", "variable_L(1)"]],
    data: numpy.ndarray,
    usemask: bool,
):
    """
    usage.statsmodels: 1
    """
    ...


def append_fields(
    base: Union[numpy.ndarray, numpy.recarray],
    names: List[str],
    data: numpy.ndarray,
    usemask: bool,
    asrecarray: bool = ...,
):
    """
    usage.statsmodels: 15
    """
    ...


@overload
def drop_fields(
    base: numpy.recarray,
    drop_names: Literal["instrument"],
    usemask: bool,
    asrecarray: bool,
):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def drop_fields(
    base: numpy.ndarray,
    drop_names: Literal["instrument"],
    usemask: bool,
    asrecarray: bool,
):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def drop_fields(
    base: numpy.recarray,
    drop_names: Literal["str_instr"],
    usemask: bool,
    asrecarray: bool,
):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def drop_fields(
    base: numpy.ndarray,
    drop_names: Literal["str_instr"],
    usemask: bool,
    asrecarray: bool,
):
    """
    usage.statsmodels: 1
    """
    ...


def drop_fields(
    base: Union[numpy.ndarray, numpy.recarray],
    drop_names: Literal["str_instr", "instrument"],
    usemask: bool,
    asrecarray: bool,
):
    """
    usage.statsmodels: 4
    """
    ...
