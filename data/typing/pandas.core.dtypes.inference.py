from typing import *


@overload
def is_dict_like(obj: Literal["float"]):
    """
    usage.koalas: 1
    """
    ...


@overload
def is_dict_like(obj: Literal["int64"]):
    """
    usage.koalas: 1
    """
    ...


@overload
def is_dict_like(obj: Dict[Literal["a"], Type[float]]):
    """
    usage.koalas: 1
    """
    ...


@overload
def is_dict_like(obj: Literal["float64"]):
    """
    usage.koalas: 1
    """
    ...


@overload
def is_dict_like(obj: pandas.core.frame.DataFrame):
    """
    usage.modin: 2
    """
    ...


@overload
def is_dict_like(obj: numpy.ndarray):
    """
    usage.modin: 3
    """
    ...


@overload
def is_dict_like(obj: None):
    """
    usage.modin: 1
    """
    ...


@overload
def is_dict_like(obj: Dict[str, numpy.ndarray]):
    """
    usage.modin: 2
    """
    ...


@overload
def is_dict_like(obj: Dict[str, List[Union[float, numpy.float64]]]):
    """
    usage.modin: 2
    """
    ...


@overload
def is_dict_like(obj: Dict[Literal["col4", "col3", "col2", "col1"], List[int]]):
    """
    usage.modin: 2
    """
    ...


@overload
def is_dict_like(
    obj: Dict[
        Literal["group", "lvalue", "key"], List[Union[Literal["e", "c", "a", "b"], int]]
    ]
):
    """
    usage.modin: 2
    """
    ...


@overload
def is_dict_like(
    obj: Dict[Literal["left_val", "a"], List[Union[int, Literal["c", "b", "a"]]]]
):
    """
    usage.modin: 2
    """
    ...


@overload
def is_dict_like(obj: Dict[Literal["zoo", "baz", "bar", "foo"], List[Union[str, int]]]):
    """
    usage.modin: 2
    """
    ...


@overload
def is_dict_like(obj: Dict[Literal["E", "D", "C", "B", "A"], List[Union[str, int]]]):
    """
    usage.modin: 2
    """
    ...


@overload
def is_dict_like(obj: Dict[Literal["day", "month", "year"], List[int]]):
    """
    usage.modin: 2
    """
    ...


@overload
def is_dict_like(obj: Dict[Literal["c", "b", "a"], numpy.ndarray]):
    """
    usage.modin: 2
    """
    ...


@overload
def is_dict_like(
    obj: Dict[str, List[Union[Literal["bar", "foo", "baz"], None, numpy.datetime64]]]
):
    """
    usage.modin: 2
    """
    ...


@overload
def is_dict_like(obj: Dict[Literal["c", "b", "a"], List[int]]):
    """
    usage.modin: 4
    """
    ...


@overload
def is_dict_like(obj: Dict[Literal["c", "b"], List[int]]):
    """
    usage.modin: 2
    """
    ...


@overload
def is_dict_like(obj: Dict[Literal["col5", "col4", "col3", "col2", "col1"], List[int]]):
    """
    usage.modin: 2
    """
    ...


@overload
def is_dict_like(
    obj: Dict[
        Literal["year2", "year1", "team", "hr2", "hr1"],
        List[Union[Literal["Yankees", "Red Sox"], int]],
    ]
):
    """
    usage.modin: 2
    """
    ...


@overload
def is_dict_like(obj: Dict[Literal["B", "A"], range]):
    """
    usage.modin: 2
    """
    ...


@overload
def is_dict_like(obj: List[List[Union[float, int, Literal["high", "medium"]]]]):
    """
    usage.modin: 1
    """
    ...


@overload
def is_dict_like(obj: Dict[Literal["col2", "col1"], List[Union[float, int]]]):
    """
    usage.modin: 2
    """
    ...


@overload
def is_dict_like(
    obj: Dict[
        Literal["bool_col", "str_col", "float_col", "int_col"],
        List[Union[int, float, bool, Literal["d", "c", "a"]]],
    ]
):
    """
    usage.modin: 2
    """
    ...


@overload
def is_dict_like(obj: Dict[Literal["B", "A"], List[int]]):
    """
    usage.modin: 6
    """
    ...


@overload
def is_dict_like(obj: Dict[Literal["B", "A"], List[Union[None, int]]]):
    """
    usage.modin: 2
    """
    ...


@overload
def is_dict_like(
    obj: Dict[
        Literal["C", "B", "A"], List[Union[int, Literal["e", "d", "c", "b", "a"]]]
    ]
):
    """
    usage.modin: 2
    """
    ...


@overload
def is_dict_like(
    obj: List[
        Tuple[
            Literal["falcon", "parrot", "lion", "monkey"],
            Literal["bird", "mammal"],
            float,
        ]
    ]
):
    """
    usage.modin: 1
    """
    ...


@overload
def is_dict_like(obj: Dict[Literal["b", "a"], List[Union[int, None]]]):
    """
    usage.modin: 2
    """
    ...


@overload
def is_dict_like(obj: Dict[Literal["b", "a"], List[int]]):
    """
    usage.modin: 2
    """
    ...


@overload
def is_dict_like(obj: List[Tuple[int, int]]):
    """
    usage.modin: 1
    """
    ...


@overload
def is_dict_like(obj: Dict[int, List[Union[Literal["bar", "foo", "bas", "bah"], int]]]):
    """
    usage.modin: 2
    """
    ...


@overload
def is_dict_like(obj: Dict[Literal["num_arms", "num_legs"], List[int]]):
    """
    usage.modin: 2
    """
    ...


@overload
def is_dict_like(
    obj: Dict[str, Union[List[Union[Literal["c", "b", "a"], bool, int]], numpy.ndarray]]
):
    """
    usage.modin: 2
    """
    ...


@overload
def is_dict_like(
    obj: Dict[
        Literal["locomotion", "animal", "class", "num_wings", "num_legs"],
        List[Union[int, str]],
    ]
):
    """
    usage.modin: 2
    """
    ...


@overload
def is_dict_like(obj: Dict[Literal["data"], range]):
    """
    usage.modin: 2
    """
    ...


@overload
def is_dict_like(obj: List[List[int]]):
    """
    usage.modin: 4
    """
    ...


@overload
def is_dict_like(obj: dict):
    """
    usage.modin: 2
    """
    ...


@overload
def is_dict_like(obj: Dict[Literal["health", "max_speed", "id"], list]):
    """
    usage.modin: 2
    """
    ...


@overload
def is_dict_like(obj: List[int]):
    """
    usage.modin: 1
    """
    ...


@overload
def is_dict_like(
    obj: List[
        Union[numpy.ndarray, pandas.core.series.Series, modin.pandas.series.Series]
    ]
):
    """
    usage.modin: 1
    """
    ...


@overload
def is_dict_like(obj: pandas.core.arrays.categorical.Categorical):
    """
    usage.modin: 1
    """
    ...


@overload
def is_dict_like(obj: Dict[Literal["col"], List[int]]):
    """
    usage.modin: 2
    """
    ...


@overload
def is_dict_like(
    obj: Dict[Literal["col2", "col1"], List[Union[Literal["A", "B"], int]]]
):
    """
    usage.modin: 2
    """
    ...


@overload
def is_dict_like(obj: Dict[Literal["col2", "col1"], List[Union[str, int]]]):
    """
    usage.modin: 2
    """
    ...


@overload
def is_dict_like(obj: Dict[str, range]):
    """
    usage.modin: 2
    """
    ...


@overload
def is_dict_like(obj: Dict[str, List[float]]):
    """
    usage.modin: 2
    """
    ...


@overload
def is_dict_like(obj: Dict[str, List[int]]):
    """
    usage.modin: 2
    """
    ...


@overload
def is_dict_like(
    obj: Dict[
        Literal["col7", "col3", "col1", "name"],
        List[Union[Literal["three", "two", "one"], int]],
    ]
):
    """
    usage.modin: 2
    """
    ...


@overload
def is_dict_like(obj: Dict[str, List[Literal["s4", "s3", "s2", "s1", "s0"]]]):
    """
    usage.modin: 2
    """
    ...


@overload
def is_dict_like(obj: List[List[Union[Literal["3", "7", "0", "9"], float]]]):
    """
    usage.modin: 1
    """
    ...


@overload
def is_dict_like(obj: List[Dict[Literal["time", "value"], int]]):
    """
    usage.modin: 1
    """
    ...


@overload
def is_dict_like(obj: Dict[Literal["B", "A"], List[str]]):
    """
    usage.modin: 2
    """
    ...


@overload
def is_dict_like(
    obj: Dict[
        Literal["col4", "col3", "col2", "col1"],
        List[Union[Literal["c", "b", "a"], int]],
    ]
):
    """
    usage.modin: 2
    """
    ...


@overload
def is_dict_like(obj: Dict[Literal["C", "B", "A"], List[int]]):
    """
    usage.modin: 2
    """
    ...


@overload
def is_dict_like(obj: Dict[Literal["b", "a"], numpy.ndarray]):
    """
    usage.modin: 2
    """
    ...


@overload
def is_dict_like(obj: Dict[Literal["y", "x"], List[Union[int, None]]]):
    """
    usage.modin: 2
    """
    ...


@overload
def is_dict_like(obj: Dict[Literal["col2", "col1"], List[Union[int, float]]]):
    """
    usage.modin: 2
    """
    ...


@overload
def is_dict_like(obj: List[List[Union[float, Literal["a", "b", "c"]]]]):
    """
    usage.modin: 1
    """
    ...


@overload
def is_dict_like(obj: Dict[Literal["a"], List[float]]):
    """
    usage.modin: 2
    """
    ...


@overload
def is_dict_like(obj: Dict[Literal["c", "b", "a"], List[Union[int, float]]]):
    """
    usage.modin: 2
    """
    ...


@overload
def is_dict_like(
    obj: Dict[
        Literal["D", "C", "B", "A"],
        Union[
            List[Union[int, float, Literal["bar", "foo", "bar2", "foo2"], None]],
            pandas.core.indexes.datetimes.DatetimeIndex,
        ],
    ]
):
    """
    usage.modin: 2
    """
    ...


@overload
def is_dict_like(
    obj: Dict[Literal["alpha-2", "GDP", "population"], List[Union[int, str]]]
):
    """
    usage.modin: 2
    """
    ...


@overload
def is_dict_like(obj: pandas.core.series.Series):
    """
    usage.dask: 2
    """
    ...


@overload
def is_dict_like(obj: dask.dataframe.core.Series):
    """
    usage.dask: 1
    """
    ...


def is_dict_like(obj: object):
    """
    usage.dask: 3
    usage.koalas: 4
    usage.modin: 119
    """
    ...


@overload
def is_hashable(obj: None):
    """
    usage.koalas: 1
    """
    ...


@overload
def is_hashable(obj: Literal["a"]):
    """
    usage.koalas: 1
    """
    ...


@overload
def is_hashable(obj: Tuple[Literal["x"], Literal["a"]]):
    """
    usage.koalas: 1
    """
    ...


@overload
def is_hashable(obj: List[Literal["a", "x"]]):
    """
    usage.koalas: 1
    """
    ...


def is_hashable(
    obj: Union[
        List[Literal["a", "x"]], Literal["a"], None, Tuple[Literal["x"], Literal["a"]]
    ]
):
    """
    usage.koalas: 4
    """
    ...


def is_sequence(obj: int):
    """
    usage.koalas: 1
    """
    ...
