from typing import *


@overload
def get_dummies(data: pandas.core.series.Series, dtype: Type[numpy.int8]):
    """
    usage.koalas: 7
    """
    ...


@overload
def get_dummies(data: pandas.core.frame.DataFrame, dtype: Type[numpy.int8]):
    """
    usage.koalas: 6
    """
    ...


@overload
def get_dummies(data: pandas.core.frame.DataFrame, dtype: Literal["float64"]):
    """
    usage.dask: 1
    usage.koalas: 1
    """
    ...


@overload
def get_dummies(
    data: pandas.core.series.Series,
    prefix: Literal["X"],
    prefix_sep: Literal["-"],
    dtype: Type[numpy.int8],
):
    """
    usage.koalas: 1
    """
    ...


@overload
def get_dummies(
    data: pandas.core.series.Series, drop_first: bool, dtype: Type[numpy.int8]
):
    """
    usage.koalas: 1
    """
    ...


@overload
def get_dummies(
    data: pandas.core.series.Series, dummy_na: bool, dtype: Type[numpy.int8]
):
    """
    usage.koalas: 1
    """
    ...


@overload
def get_dummies(
    data: pandas.core.frame.DataFrame,
    columns: List[Tuple[Literal["y", "x"], Literal["c", "a"], Literal["3", "1"]]],
    dtype: Type[numpy.int8],
):
    """
    usage.koalas: 1
    """
    ...


@overload
def get_dummies(
    data: pandas.core.frame.DataFrame,
    columns: List[Literal["x"]],
    dtype: Type[numpy.int8],
):
    """
    usage.koalas: 2
    """
    ...


@overload
def get_dummies(
    data: pandas.core.frame.DataFrame,
    columns: Tuple[Literal["x"], Literal["a"]],
    dtype: Type[numpy.int8],
):
    """
    usage.koalas: 1
    """
    ...


@overload
def get_dummies(
    data: pandas.core.frame.DataFrame,
    columns: List[Literal["c", "a"]],
    dtype: Type[numpy.int8],
):
    """
    usage.koalas: 1
    """
    ...


@overload
def get_dummies(
    data: pandas.core.frame.DataFrame,
    columns: List[Literal["b"]],
    dtype: Type[numpy.int8],
):
    """
    usage.koalas: 1
    """
    ...


@overload
def get_dummies(
    data: pandas.core.frame.DataFrame,
    prefix: List[Literal["bar", "foo"]],
    dtype: Type[numpy.int8],
):
    """
    usage.koalas: 1
    """
    ...


@overload
def get_dummies(
    data: pandas.core.frame.DataFrame,
    prefix: List[Literal["foo"]],
    columns: List[Literal["B"]],
    dtype: Type[numpy.int8],
):
    """
    usage.koalas: 1
    """
    ...


@overload
def get_dummies(
    data: pandas.core.frame.DataFrame,
    prefix: Dict[Literal["B", "A"], Literal["bar", "foo"]],
    dtype: Type[numpy.int8],
):
    """
    usage.koalas: 1
    """
    ...


@overload
def get_dummies(
    data: pandas.core.frame.DataFrame,
    prefix: Dict[Literal["A", "B"], Literal["bar", "foo"]],
    dtype: Type[numpy.int8],
):
    """
    usage.koalas: 1
    """
    ...


@overload
def get_dummies(
    data: pandas.core.frame.DataFrame,
    prefix: Dict[Literal["B", "A"], Literal["bar", "foo"]],
    columns: List[Literal["B", "A"]],
    dtype: Type[numpy.int8],
):
    """
    usage.koalas: 1
    """
    ...


@overload
def get_dummies(
    data: pandas.core.series.Series, prefix: Literal["foo"], dtype: Type[numpy.int8]
):
    """
    usage.koalas: 1
    """
    ...


@overload
def get_dummies(
    data: pandas.core.series.Series,
    prefix: List[Literal["foo"]],
    columns: List[Literal["B"]],
    dtype: Type[numpy.int8],
):
    """
    usage.koalas: 1
    """
    ...


@overload
def get_dummies(data: pandas.core.frame.DataFrame):
    """
    usage.dask: 1
    usage.statsmodels: 1
    """
    ...


@overload
def get_dummies(data: numpy.ndarray, drop_first: bool):
    """
    usage.statsmodels: 2
    """
    ...


@overload
def get_dummies(data: pandas.core.series.Series):
    """
    usage.dask: 2
    usage.statsmodels: 2
    """
    ...


@overload
def get_dummies(data: pandas.core.frame.DataFrame, drop_first: bool):
    """
    usage.statsmodels: 2
    """
    ...


@overload
def get_dummies(data: pandas.core.series.Series, drop_first: bool):
    """
    usage.dask: 1
    usage.statsmodels: 4
    """
    ...


@overload
def get_dummies(data: pandas.core.arrays.categorical.Categorical):
    """
    usage.statsmodels: 3
    """
    ...


@overload
def get_dummies(
    data: pandas.core.series.Series,
    prefix: None,
    prefix_sep: Literal["_"],
    dummy_na: bool,
    columns: None,
    sparse: bool,
    drop_first: bool,
    dtype: Type[numpy.uint8],
):
    """
    usage.dask: 2
    """
    ...


@overload
def get_dummies(
    data: pandas.core.frame.DataFrame,
    prefix: None,
    prefix_sep: Literal["_"],
    dummy_na: bool,
    columns: pandas.core.indexes.base.Index,
    sparse: bool,
    drop_first: bool,
    dtype: Type[numpy.uint8],
):
    """
    usage.dask: 2
    """
    ...


@overload
def get_dummies(data: pandas.core.frame.DataFrame, columns: List[Literal["c", "a"]]):
    """
    usage.dask: 1
    """
    ...


@overload
def get_dummies(
    data: pandas.core.frame.DataFrame,
    prefix: None,
    prefix_sep: Literal["_"],
    dummy_na: bool,
    columns: List[Literal["c", "a"]],
    sparse: bool,
    drop_first: bool,
    dtype: Type[numpy.uint8],
):
    """
    usage.dask: 2
    """
    ...


@overload
def get_dummies(
    data: pandas.core.series.Series, prefix: Literal["X"], prefix_sep: Literal["-"]
):
    """
    usage.dask: 1
    """
    ...


@overload
def get_dummies(
    data: pandas.core.series.Series,
    prefix: Literal["X"],
    prefix_sep: Literal["-"],
    dummy_na: bool,
    columns: None,
    sparse: bool,
    drop_first: bool,
    dtype: Type[numpy.uint8],
):
    """
    usage.dask: 2
    """
    ...


@overload
def get_dummies(data: pandas.core.series.Series, dummy_na: bool):
    """
    usage.dask: 1
    """
    ...


@overload
def get_dummies(data: pandas.core.series.Series, sparse: bool):
    """
    usage.dask: 1
    """
    ...


@overload
def get_dummies(data: pandas.core.frame.DataFrame, sparse: bool):
    """
    usage.dask: 2
    """
    ...


@overload
def get_dummies(
    data: pandas.core.frame.DataFrame,
    prefix: None,
    prefix_sep: Literal["_"],
    dummy_na: bool,
    columns: pandas.core.indexes.base.Index,
    sparse: bool,
    drop_first: bool,
    dtype: Literal["float64"],
):
    """
    usage.dask: 2
    """
    ...


@overload
def get_dummies(
    data: pandas.core.frame.DataFrame,
    prefix: None,
    prefix_sep: Literal["_"],
    dummy_na: bool,
    columns: None,
    sparse: bool,
    drop_first: bool,
    dtype: Literal["float64"],
):
    """
    usage.dask: 1
    """
    ...


def get_dummies(
    data: Union[
        pandas.core.series.Series,
        pandas.core.frame.DataFrame,
        pandas.core.arrays.categorical.Categorical,
        numpy.ndarray,
    ],
    prefix: Union[
        Literal["X", "foo"],
        None,
        Dict[Literal["B", "A"], Literal["bar", "foo"]],
        List[Literal["bar", "foo"]],
    ] = ...,
    prefix_sep: Literal["_", "-"] = ...,
    dummy_na: bool = ...,
    columns: Union[
        pandas.core.indexes.base.Index,
        List[
            Union[str, Tuple[Literal["y", "x"], Literal["c", "a"], Literal["3", "1"]]]
        ],
        None,
        Tuple[Literal["x"], Literal["a"]],
    ] = ...,
    sparse: bool = ...,
    drop_first: bool = ...,
    dtype: Union[type, Literal["float64"]] = ...,
):
    """
    usage.dask: 22
    usage.koalas: 30
    usage.statsmodels: 14
    """
    ...
