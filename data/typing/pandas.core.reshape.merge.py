from typing import *


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["inner"],
    indicator: bool,
    left_index: bool,
    left_on: None,
    npartitions: None,
    on: Literal["idx"],
    right_index: bool,
    right_on: None,
    shuffle: Literal["tasks"],
    suffixes: Tuple[Literal["_x"], Literal["_y"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["left"],
    indicator: bool,
    left_index: bool,
    left_on: None,
    npartitions: None,
    on: Literal["idx"],
    right_index: bool,
    right_on: None,
    shuffle: Literal["tasks"],
    suffixes: Tuple[Literal["_x"], Literal["_y"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["right"],
    indicator: bool,
    left_index: bool,
    left_on: None,
    npartitions: None,
    on: Literal["idx"],
    right_index: bool,
    right_on: None,
    shuffle: Literal["tasks"],
    suffixes: Tuple[Literal["_x"], Literal["_y"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["outer"],
    indicator: bool,
    left_index: bool,
    left_on: None,
    npartitions: None,
    on: Literal["idx"],
    right_index: bool,
    right_on: None,
    shuffle: Literal["tasks"],
    suffixes: Tuple[Literal["_x"], Literal["_y"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["inner"],
    indicator: bool,
    left_index: bool,
    left_on: None,
    npartitions: None,
    on: List[Literal["idx"]],
    right_index: bool,
    right_on: None,
    shuffle: Literal["tasks"],
    suffixes: Tuple[Literal["_x"], Literal["_y"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["left"],
    indicator: bool,
    left_index: bool,
    left_on: None,
    npartitions: None,
    on: List[Literal["idx"]],
    right_index: bool,
    right_on: None,
    shuffle: Literal["tasks"],
    suffixes: Tuple[Literal["_x"], Literal["_y"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["right"],
    indicator: bool,
    left_index: bool,
    left_on: None,
    npartitions: None,
    on: List[Literal["idx"]],
    right_index: bool,
    right_on: None,
    shuffle: Literal["tasks"],
    suffixes: Tuple[Literal["_x"], Literal["_y"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["outer"],
    indicator: bool,
    left_index: bool,
    left_on: None,
    npartitions: None,
    on: List[Literal["idx"]],
    right_index: bool,
    right_on: None,
    shuffle: Literal["tasks"],
    suffixes: Tuple[Literal["_x"], Literal["_y"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["inner"],
    indicator: bool,
    left_index: bool,
    left_on: None,
    npartitions: None,
    on: List[Literal["k", "idx"]],
    right_index: bool,
    right_on: None,
    shuffle: Literal["tasks"],
    suffixes: Tuple[Literal["_x"], Literal["_y"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["left"],
    indicator: bool,
    left_index: bool,
    left_on: None,
    npartitions: None,
    on: List[Literal["k", "idx"]],
    right_index: bool,
    right_on: None,
    shuffle: Literal["tasks"],
    suffixes: Tuple[Literal["_x"], Literal["_y"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["right"],
    indicator: bool,
    left_index: bool,
    left_on: None,
    npartitions: None,
    on: List[Literal["k", "idx"]],
    right_index: bool,
    right_on: None,
    shuffle: Literal["tasks"],
    suffixes: Tuple[Literal["_x"], Literal["_y"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["outer"],
    indicator: bool,
    left_index: bool,
    left_on: None,
    npartitions: None,
    on: List[Literal["k", "idx"]],
    right_index: bool,
    right_on: None,
    shuffle: Literal["tasks"],
    suffixes: Tuple[Literal["_x"], Literal["_y"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["inner"],
    indicator: bool,
    left_index: bool,
    left_on: None,
    npartitions: None,
    on: List[Literal["idx", "k"]],
    right_index: bool,
    right_on: None,
    shuffle: Literal["tasks"],
    suffixes: Tuple[Literal["_x"], Literal["_y"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["left"],
    indicator: bool,
    left_index: bool,
    left_on: None,
    npartitions: None,
    on: List[Literal["idx", "k"]],
    right_index: bool,
    right_on: None,
    shuffle: Literal["tasks"],
    suffixes: Tuple[Literal["_x"], Literal["_y"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["right"],
    indicator: bool,
    left_index: bool,
    left_on: None,
    npartitions: None,
    on: List[Literal["idx", "k"]],
    right_index: bool,
    right_on: None,
    shuffle: Literal["tasks"],
    suffixes: Tuple[Literal["_x"], Literal["_y"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["outer"],
    indicator: bool,
    left_index: bool,
    left_on: None,
    npartitions: None,
    on: List[Literal["idx", "k"]],
    right_index: bool,
    right_on: None,
    shuffle: Literal["tasks"],
    suffixes: Tuple[Literal["_x"], Literal["_y"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    how: Literal["inner"],
    on: Literal["y"],
):
    """
    usage.dask: 2
    """
    ...


@overload
def merge(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    how: Literal["outer"],
    on: None,
    left_on: Literal["x"],
    right_on: Literal["z"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    how: Literal["left"],
    on: Literal["y"],
):
    """
    usage.dask: 2
    """
    ...


@overload
def merge(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    how: Literal["right"],
    on: Literal["y"],
):
    """
    usage.dask: 2
    """
    ...


@overload
def merge(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    how: Literal["outer"],
    on: Literal["y"],
):
    """
    usage.dask: 2
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["inner"],
    left_index: bool,
    left_on: None,
    npartitions: None,
    right_index: bool,
    shuffle: None,
    suffixes: List[Literal["_r", "_l"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: dask.dataframe.core.DataFrame,
    right: dask.dataframe.core.DataFrame,
    how: Literal["inner"],
    on: None,
    left_index: bool,
    right_index: bool,
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: dask.dataframe.core.DataFrame,
    right: dask.dataframe.core.DataFrame,
    how: Literal["outer"],
    on: None,
    left_index: bool,
    right_index: bool,
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: dask.dataframe.core.DataFrame,
    right: dask.dataframe.core.DataFrame,
    how: Literal["left"],
    on: None,
    left_index: bool,
    right_index: bool,
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: dask.dataframe.core.DataFrame,
    right: dask.dataframe.core.DataFrame,
    how: Literal["right"],
    on: None,
    left_index: bool,
    right_index: bool,
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: dask.dataframe.core.DataFrame,
    right: dask.dataframe.core.DataFrame,
    how: Literal["inner"],
    on: List[Literal["A"]],
    left_index: bool,
    right_index: bool,
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: dask.dataframe.core.DataFrame,
    right: dask.dataframe.core.DataFrame,
    how: Literal["outer"],
    on: List[Literal["A"]],
    left_index: bool,
    right_index: bool,
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: dask.dataframe.core.DataFrame,
    right: dask.dataframe.core.DataFrame,
    how: Literal["left"],
    on: List[Literal["A"]],
    left_index: bool,
    right_index: bool,
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: dask.dataframe.core.DataFrame,
    right: dask.dataframe.core.DataFrame,
    how: Literal["right"],
    on: List[Literal["A"]],
    left_index: bool,
    right_index: bool,
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["inner"],
    left_index: bool,
    right_index: bool,
    shuffle: Literal["disk"],
):
    """
    usage.dask: 4
    """
    ...


@overload
def merge(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    how: Literal["inner"],
    left_index: bool,
    right_index: bool,
):
    """
    usage.dask: 4
    """
    ...


@overload
def merge(
    left: dask.dataframe.core.DataFrame,
    right: dask.dataframe.core.DataFrame,
    how: Literal["inner"],
    on: Literal["y"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["inner"],
    left_on: Literal["x"],
    right_on: Literal["z"],
    shuffle: Literal["disk"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    how: Literal["inner"],
    left_on: Literal["x"],
    right_on: Literal["z"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["inner"],
    left_on: Literal["x"],
    right_on: Literal["z"],
    shuffle: Literal["disk"],
    suffixes: Tuple[Literal["1"], Literal["2"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    how: Literal["inner"],
    left_on: Literal["x"],
    right_on: Literal["z"],
    suffixes: Tuple[Literal["1"], Literal["2"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["inner"],
    shuffle: Literal["disk"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    how: Literal["inner"],
):
    """
    usage.dask: 4
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: pandas.core.frame.DataFrame,
    /,
    *,
    how: Literal["inner"],
    shuffle: Literal["disk"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: pandas.core.frame.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["inner"],
    shuffle: Literal["disk"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: pandas.core.frame.DataFrame,
    _1: pandas.core.frame.DataFrame,
    /,
    *,
    how: Literal["inner"],
    shuffle: Literal["disk"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    how: Literal["inner"],
    on: None,
    left_on: List[Literal["y"]],
    right_on: List[Literal["y"]],
    left_index: bool,
    right_index: bool,
    suffixes: Tuple[Literal["_x"], Literal["_y"]],
    indicator: bool,
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["inner"],
    left_index: bool,
    right_index: bool,
    shuffle: Literal["disk"],
    suffixes: Tuple[Literal["1"], Literal["2"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    how: Literal["inner"],
    left_index: bool,
    right_index: bool,
    suffixes: Tuple[Literal["1"], Literal["2"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["inner"],
    left_on: Literal["x"],
    right_index: bool,
    shuffle: Literal["disk"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    how: Literal["inner"],
    left_on: Literal["x"],
    right_index: bool,
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["inner"],
    left_on: Literal["x"],
    right_index: bool,
    shuffle: Literal["disk"],
    suffixes: Tuple[Literal["1"], Literal["2"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    how: Literal["inner"],
    left_on: Literal["x"],
    right_index: bool,
    suffixes: Tuple[Literal["1"], Literal["2"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["outer"],
    left_index: bool,
    right_index: bool,
    shuffle: Literal["disk"],
):
    """
    usage.dask: 4
    """
    ...


@overload
def merge(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    how: Literal["outer"],
    left_index: bool,
    right_index: bool,
):
    """
    usage.dask: 4
    """
    ...


@overload
def merge(
    left: dask.dataframe.core.DataFrame,
    right: dask.dataframe.core.DataFrame,
    how: Literal["outer"],
    on: Literal["y"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["outer"],
    left_on: Literal["x"],
    right_on: Literal["z"],
    shuffle: Literal["disk"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    how: Literal["outer"],
    left_on: Literal["x"],
    right_on: Literal["z"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["outer"],
    left_on: Literal["x"],
    right_on: Literal["z"],
    shuffle: Literal["disk"],
    suffixes: Tuple[Literal["1"], Literal["2"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    how: Literal["outer"],
    left_on: Literal["x"],
    right_on: Literal["z"],
    suffixes: Tuple[Literal["1"], Literal["2"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["outer"],
    shuffle: Literal["disk"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    how: Literal["outer"],
):
    """
    usage.dask: 4
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: pandas.core.frame.DataFrame,
    /,
    *,
    how: Literal["outer"],
    shuffle: Literal["disk"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: pandas.core.frame.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["outer"],
    shuffle: Literal["disk"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: pandas.core.frame.DataFrame,
    _1: pandas.core.frame.DataFrame,
    /,
    *,
    how: Literal["outer"],
    shuffle: Literal["disk"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    how: Literal["outer"],
    on: None,
    left_on: List[Literal["y"]],
    right_on: List[Literal["y"]],
    left_index: bool,
    right_index: bool,
    suffixes: Tuple[Literal["_x"], Literal["_y"]],
    indicator: bool,
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["outer"],
    left_index: bool,
    right_index: bool,
    shuffle: Literal["disk"],
    suffixes: Tuple[Literal["1"], Literal["2"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    how: Literal["outer"],
    left_index: bool,
    right_index: bool,
    suffixes: Tuple[Literal["1"], Literal["2"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["outer"],
    left_on: Literal["x"],
    right_index: bool,
    shuffle: Literal["disk"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    how: Literal["outer"],
    left_on: Literal["x"],
    right_index: bool,
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["outer"],
    left_on: Literal["x"],
    right_index: bool,
    shuffle: Literal["disk"],
    suffixes: Tuple[Literal["1"], Literal["2"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    how: Literal["outer"],
    left_on: Literal["x"],
    right_index: bool,
    suffixes: Tuple[Literal["1"], Literal["2"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["left"],
    left_index: bool,
    right_index: bool,
    shuffle: Literal["disk"],
):
    """
    usage.dask: 4
    """
    ...


@overload
def merge(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    how: Literal["left"],
    left_index: bool,
    right_index: bool,
):
    """
    usage.dask: 4
    """
    ...


@overload
def merge(
    left: dask.dataframe.core.DataFrame,
    right: dask.dataframe.core.DataFrame,
    how: Literal["left"],
    on: Literal["y"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["left"],
    left_on: Literal["x"],
    right_on: Literal["z"],
    shuffle: Literal["disk"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    how: Literal["left"],
    left_on: Literal["x"],
    right_on: Literal["z"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["left"],
    left_on: Literal["x"],
    right_on: Literal["z"],
    shuffle: Literal["disk"],
    suffixes: Tuple[Literal["1"], Literal["2"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    how: Literal["left"],
    left_on: Literal["x"],
    right_on: Literal["z"],
    suffixes: Tuple[Literal["1"], Literal["2"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["left"],
    shuffle: Literal["disk"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    how: Literal["left"],
):
    """
    usage.dask: 4
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: pandas.core.frame.DataFrame,
    /,
    *,
    how: Literal["left"],
    shuffle: Literal["disk"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: pandas.core.frame.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["left"],
    shuffle: Literal["disk"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: pandas.core.frame.DataFrame,
    _1: pandas.core.frame.DataFrame,
    /,
    *,
    how: Literal["left"],
    shuffle: Literal["disk"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    how: Literal["left"],
    on: None,
    left_on: List[Literal["y"]],
    right_on: List[Literal["y"]],
    left_index: bool,
    right_index: bool,
    suffixes: Tuple[Literal["_x"], Literal["_y"]],
    indicator: bool,
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["left"],
    left_index: bool,
    right_index: bool,
    shuffle: Literal["disk"],
    suffixes: Tuple[Literal["1"], Literal["2"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    how: Literal["left"],
    left_index: bool,
    right_index: bool,
    suffixes: Tuple[Literal["1"], Literal["2"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["left"],
    left_on: Literal["x"],
    right_index: bool,
    shuffle: Literal["disk"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    how: Literal["left"],
    left_on: Literal["x"],
    right_index: bool,
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["left"],
    left_on: Literal["x"],
    right_index: bool,
    shuffle: Literal["disk"],
    suffixes: Tuple[Literal["1"], Literal["2"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    how: Literal["left"],
    left_on: Literal["x"],
    right_index: bool,
    suffixes: Tuple[Literal["1"], Literal["2"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["right"],
    left_index: bool,
    right_index: bool,
    shuffle: Literal["disk"],
):
    """
    usage.dask: 4
    """
    ...


@overload
def merge(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    how: Literal["right"],
    left_index: bool,
    right_index: bool,
):
    """
    usage.dask: 4
    """
    ...


@overload
def merge(
    left: dask.dataframe.core.DataFrame,
    right: dask.dataframe.core.DataFrame,
    how: Literal["right"],
    on: Literal["y"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["right"],
    left_on: Literal["x"],
    right_on: Literal["z"],
    shuffle: Literal["disk"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    how: Literal["right"],
    left_on: Literal["x"],
    right_on: Literal["z"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["right"],
    left_on: Literal["x"],
    right_on: Literal["z"],
    shuffle: Literal["disk"],
    suffixes: Tuple[Literal["1"], Literal["2"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    how: Literal["right"],
    left_on: Literal["x"],
    right_on: Literal["z"],
    suffixes: Tuple[Literal["1"], Literal["2"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["right"],
    shuffle: Literal["disk"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    how: Literal["right"],
):
    """
    usage.dask: 4
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: pandas.core.frame.DataFrame,
    /,
    *,
    how: Literal["right"],
    shuffle: Literal["disk"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: pandas.core.frame.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["right"],
    shuffle: Literal["disk"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: pandas.core.frame.DataFrame,
    _1: pandas.core.frame.DataFrame,
    /,
    *,
    how: Literal["right"],
    shuffle: Literal["disk"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    how: Literal["right"],
    on: None,
    left_on: List[Literal["y"]],
    right_on: List[Literal["y"]],
    left_index: bool,
    right_index: bool,
    suffixes: Tuple[Literal["_x"], Literal["_y"]],
    indicator: bool,
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["right"],
    left_index: bool,
    right_index: bool,
    shuffle: Literal["disk"],
    suffixes: Tuple[Literal["1"], Literal["2"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    how: Literal["right"],
    left_index: bool,
    right_index: bool,
    suffixes: Tuple[Literal["1"], Literal["2"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["right"],
    left_on: Literal["x"],
    right_index: bool,
    shuffle: Literal["disk"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    how: Literal["right"],
    left_on: Literal["x"],
    right_index: bool,
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["right"],
    left_on: Literal["x"],
    right_index: bool,
    shuffle: Literal["disk"],
    suffixes: Tuple[Literal["1"], Literal["2"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    how: Literal["right"],
    left_on: Literal["x"],
    right_index: bool,
    suffixes: Tuple[Literal["1"], Literal["2"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["inner"],
    left_index: bool,
    right_index: bool,
    shuffle: Literal["tasks"],
):
    """
    usage.dask: 4
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["inner"],
    left_on: Literal["x"],
    right_on: Literal["z"],
    shuffle: Literal["tasks"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["inner"],
    left_on: Literal["x"],
    right_on: Literal["z"],
    shuffle: Literal["tasks"],
    suffixes: Tuple[Literal["1"], Literal["2"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["inner"],
    shuffle: Literal["tasks"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: pandas.core.frame.DataFrame,
    /,
    *,
    how: Literal["inner"],
    shuffle: Literal["tasks"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: pandas.core.frame.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["inner"],
    shuffle: Literal["tasks"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: pandas.core.frame.DataFrame,
    _1: pandas.core.frame.DataFrame,
    /,
    *,
    how: Literal["inner"],
    shuffle: Literal["tasks"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["inner"],
    left_index: bool,
    right_index: bool,
    shuffle: Literal["tasks"],
    suffixes: Tuple[Literal["1"], Literal["2"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["inner"],
    left_on: Literal["x"],
    right_index: bool,
    shuffle: Literal["tasks"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["inner"],
    left_on: Literal["x"],
    right_index: bool,
    shuffle: Literal["tasks"],
    suffixes: Tuple[Literal["1"], Literal["2"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["outer"],
    left_index: bool,
    right_index: bool,
    shuffle: Literal["tasks"],
):
    """
    usage.dask: 4
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["outer"],
    left_on: Literal["x"],
    right_on: Literal["z"],
    shuffle: Literal["tasks"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["outer"],
    left_on: Literal["x"],
    right_on: Literal["z"],
    shuffle: Literal["tasks"],
    suffixes: Tuple[Literal["1"], Literal["2"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["outer"],
    shuffle: Literal["tasks"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: pandas.core.frame.DataFrame,
    /,
    *,
    how: Literal["outer"],
    shuffle: Literal["tasks"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: pandas.core.frame.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["outer"],
    shuffle: Literal["tasks"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: pandas.core.frame.DataFrame,
    _1: pandas.core.frame.DataFrame,
    /,
    *,
    how: Literal["outer"],
    shuffle: Literal["tasks"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["outer"],
    left_index: bool,
    right_index: bool,
    shuffle: Literal["tasks"],
    suffixes: Tuple[Literal["1"], Literal["2"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["outer"],
    left_on: Literal["x"],
    right_index: bool,
    shuffle: Literal["tasks"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["outer"],
    left_on: Literal["x"],
    right_index: bool,
    shuffle: Literal["tasks"],
    suffixes: Tuple[Literal["1"], Literal["2"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["left"],
    left_index: bool,
    right_index: bool,
    shuffle: Literal["tasks"],
):
    """
    usage.dask: 4
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["left"],
    left_on: Literal["x"],
    right_on: Literal["z"],
    shuffle: Literal["tasks"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["left"],
    left_on: Literal["x"],
    right_on: Literal["z"],
    shuffle: Literal["tasks"],
    suffixes: Tuple[Literal["1"], Literal["2"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["left"],
    shuffle: Literal["tasks"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: pandas.core.frame.DataFrame,
    /,
    *,
    how: Literal["left"],
    shuffle: Literal["tasks"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: pandas.core.frame.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["left"],
    shuffle: Literal["tasks"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: pandas.core.frame.DataFrame,
    _1: pandas.core.frame.DataFrame,
    /,
    *,
    how: Literal["left"],
    shuffle: Literal["tasks"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["left"],
    left_index: bool,
    right_index: bool,
    shuffle: Literal["tasks"],
    suffixes: Tuple[Literal["1"], Literal["2"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["left"],
    left_on: Literal["x"],
    right_index: bool,
    shuffle: Literal["tasks"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["left"],
    left_on: Literal["x"],
    right_index: bool,
    shuffle: Literal["tasks"],
    suffixes: Tuple[Literal["1"], Literal["2"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["right"],
    left_index: bool,
    right_index: bool,
    shuffle: Literal["tasks"],
):
    """
    usage.dask: 4
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["right"],
    left_on: Literal["x"],
    right_on: Literal["z"],
    shuffle: Literal["tasks"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["right"],
    left_on: Literal["x"],
    right_on: Literal["z"],
    shuffle: Literal["tasks"],
    suffixes: Tuple[Literal["1"], Literal["2"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["right"],
    shuffle: Literal["tasks"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: pandas.core.frame.DataFrame,
    /,
    *,
    how: Literal["right"],
    shuffle: Literal["tasks"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: pandas.core.frame.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["right"],
    shuffle: Literal["tasks"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: pandas.core.frame.DataFrame,
    _1: pandas.core.frame.DataFrame,
    /,
    *,
    how: Literal["right"],
    shuffle: Literal["tasks"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["right"],
    left_index: bool,
    right_index: bool,
    shuffle: Literal["tasks"],
    suffixes: Tuple[Literal["1"], Literal["2"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["right"],
    left_on: Literal["x"],
    right_index: bool,
    shuffle: Literal["tasks"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["right"],
    left_on: Literal["x"],
    right_index: bool,
    shuffle: Literal["tasks"],
    suffixes: Tuple[Literal["1"], Literal["2"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["inner"],
    indicator: bool,
    left_index: bool,
    left_on: Literal["a"],
    npartitions: None,
    on: None,
    right_index: bool,
    right_on: Literal["d"],
    shuffle: Literal["tasks"],
    suffixes: Tuple[Literal["_x"], Literal["_y"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["inner"],
    left_index: bool,
    left_on: None,
    npartitions: None,
    right_index: bool,
    shuffle: Literal["disk"],
    suffixes: List[Literal[""]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["inner"],
    left_index: bool,
    left_on: None,
    npartitions: None,
    right_index: bool,
    shuffle: Literal["disk"],
    suffixes: List[Literal["r", "l"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["outer"],
    left_index: bool,
    left_on: None,
    npartitions: None,
    right_index: bool,
    shuffle: Literal["disk"],
    suffixes: List[Literal[""]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["outer"],
    left_index: bool,
    left_on: None,
    npartitions: None,
    right_index: bool,
    shuffle: Literal["disk"],
    suffixes: List[Literal["r", "l"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["left"],
    left_index: bool,
    left_on: None,
    npartitions: None,
    right_index: bool,
    shuffle: Literal["disk"],
    suffixes: List[Literal[""]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["left"],
    left_index: bool,
    left_on: None,
    npartitions: None,
    right_index: bool,
    shuffle: Literal["disk"],
    suffixes: List[Literal["r", "l"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["right"],
    left_index: bool,
    left_on: None,
    npartitions: None,
    right_index: bool,
    shuffle: Literal["disk"],
    suffixes: List[Literal[""]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["right"],
    left_index: bool,
    left_on: None,
    npartitions: None,
    right_index: bool,
    shuffle: Literal["disk"],
    suffixes: List[Literal["r", "l"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["inner"],
    left_index: bool,
    left_on: None,
    npartitions: None,
    right_index: bool,
    shuffle: Literal["tasks"],
    suffixes: List[Literal[""]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["inner"],
    left_index: bool,
    left_on: None,
    npartitions: None,
    right_index: bool,
    shuffle: Literal["tasks"],
    suffixes: List[Literal["r", "l"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["outer"],
    left_index: bool,
    left_on: None,
    npartitions: None,
    right_index: bool,
    shuffle: Literal["tasks"],
    suffixes: List[Literal[""]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["outer"],
    left_index: bool,
    left_on: None,
    npartitions: None,
    right_index: bool,
    shuffle: Literal["tasks"],
    suffixes: List[Literal["r", "l"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["left"],
    left_index: bool,
    left_on: None,
    npartitions: None,
    right_index: bool,
    shuffle: Literal["tasks"],
    suffixes: List[Literal[""]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["left"],
    left_index: bool,
    left_on: None,
    npartitions: None,
    right_index: bool,
    shuffle: Literal["tasks"],
    suffixes: List[Literal["r", "l"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["right"],
    left_index: bool,
    left_on: None,
    npartitions: None,
    right_index: bool,
    shuffle: Literal["tasks"],
    suffixes: List[Literal[""]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["right"],
    left_index: bool,
    left_on: None,
    npartitions: None,
    right_index: bool,
    shuffle: Literal["tasks"],
    suffixes: List[Literal["r", "l"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["inner"],
    left_on: Literal["a"],
    right_on: Literal["d"],
    shuffle: Literal["disk"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    how: Literal["inner"],
    left_on: Literal["a"],
    right_on: Literal["d"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["inner"],
    left_on: Literal["b"],
    right_on: Literal["e"],
    shuffle: Literal["disk"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    how: Literal["inner"],
    left_on: Literal["b"],
    right_on: Literal["e"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["inner"],
    left_on: Literal["d"],
    right_on: Literal["a"],
    shuffle: Literal["disk"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    how: Literal["inner"],
    left_on: Literal["d"],
    right_on: Literal["a"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["inner"],
    left_on: Literal["e"],
    right_on: Literal["b"],
    shuffle: Literal["disk"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    how: Literal["inner"],
    left_on: Literal["e"],
    right_on: Literal["b"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["inner"],
    left_on: List[Literal["b", "a"]],
    right_on: List[Literal["e", "d"]],
    shuffle: Literal["disk"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    how: Literal["inner"],
    left_on: List[Literal["b", "a"]],
    right_on: List[Literal["e", "d"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["outer"],
    left_on: Literal["a"],
    right_on: Literal["d"],
    shuffle: Literal["disk"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    how: Literal["outer"],
    left_on: Literal["a"],
    right_on: Literal["d"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["outer"],
    left_on: Literal["b"],
    right_on: Literal["e"],
    shuffle: Literal["disk"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    how: Literal["outer"],
    left_on: Literal["b"],
    right_on: Literal["e"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["outer"],
    left_on: Literal["d"],
    right_on: Literal["a"],
    shuffle: Literal["disk"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    how: Literal["outer"],
    left_on: Literal["d"],
    right_on: Literal["a"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["outer"],
    left_on: Literal["e"],
    right_on: Literal["b"],
    shuffle: Literal["disk"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    how: Literal["outer"],
    left_on: Literal["e"],
    right_on: Literal["b"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["outer"],
    left_on: List[Literal["b", "a"]],
    right_on: List[Literal["e", "d"]],
    shuffle: Literal["disk"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    how: Literal["outer"],
    left_on: List[Literal["b", "a"]],
    right_on: List[Literal["e", "d"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["left"],
    left_on: Literal["a"],
    right_on: Literal["d"],
    shuffle: Literal["disk"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    how: Literal["left"],
    left_on: Literal["a"],
    right_on: Literal["d"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["left"],
    left_on: Literal["b"],
    right_on: Literal["e"],
    shuffle: Literal["disk"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    how: Literal["left"],
    left_on: Literal["b"],
    right_on: Literal["e"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["left"],
    left_on: Literal["d"],
    right_on: Literal["a"],
    shuffle: Literal["disk"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    how: Literal["left"],
    left_on: Literal["d"],
    right_on: Literal["a"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["left"],
    left_on: Literal["e"],
    right_on: Literal["b"],
    shuffle: Literal["disk"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    how: Literal["left"],
    left_on: Literal["e"],
    right_on: Literal["b"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["left"],
    left_on: List[Literal["b", "a"]],
    right_on: List[Literal["e", "d"]],
    shuffle: Literal["disk"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    how: Literal["left"],
    left_on: List[Literal["b", "a"]],
    right_on: List[Literal["e", "d"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["right"],
    left_on: Literal["a"],
    right_on: Literal["d"],
    shuffle: Literal["disk"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    how: Literal["right"],
    left_on: Literal["a"],
    right_on: Literal["d"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["right"],
    left_on: Literal["b"],
    right_on: Literal["e"],
    shuffle: Literal["disk"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    how: Literal["right"],
    left_on: Literal["b"],
    right_on: Literal["e"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["right"],
    left_on: Literal["d"],
    right_on: Literal["a"],
    shuffle: Literal["disk"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    how: Literal["right"],
    left_on: Literal["d"],
    right_on: Literal["a"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["right"],
    left_on: Literal["e"],
    right_on: Literal["b"],
    shuffle: Literal["disk"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    how: Literal["right"],
    left_on: Literal["e"],
    right_on: Literal["b"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["right"],
    left_on: List[Literal["b", "a"]],
    right_on: List[Literal["e", "d"]],
    shuffle: Literal["disk"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    how: Literal["right"],
    left_on: List[Literal["b", "a"]],
    right_on: List[Literal["e", "d"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["inner"],
    left_on: Literal["a"],
    right_on: Literal["d"],
    shuffle: Literal["tasks"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["inner"],
    left_on: Literal["b"],
    right_on: Literal["e"],
    shuffle: Literal["tasks"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["inner"],
    left_on: Literal["d"],
    right_on: Literal["a"],
    shuffle: Literal["tasks"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["inner"],
    left_on: Literal["e"],
    right_on: Literal["b"],
    shuffle: Literal["tasks"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["inner"],
    left_on: List[Literal["b", "a"]],
    right_on: List[Literal["e", "d"]],
    shuffle: Literal["tasks"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["outer"],
    left_on: Literal["a"],
    right_on: Literal["d"],
    shuffle: Literal["tasks"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["outer"],
    left_on: Literal["b"],
    right_on: Literal["e"],
    shuffle: Literal["tasks"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["outer"],
    left_on: Literal["d"],
    right_on: Literal["a"],
    shuffle: Literal["tasks"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["outer"],
    left_on: Literal["e"],
    right_on: Literal["b"],
    shuffle: Literal["tasks"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["outer"],
    left_on: List[Literal["b", "a"]],
    right_on: List[Literal["e", "d"]],
    shuffle: Literal["tasks"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["left"],
    left_on: Literal["a"],
    right_on: Literal["d"],
    shuffle: Literal["tasks"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["left"],
    left_on: Literal["b"],
    right_on: Literal["e"],
    shuffle: Literal["tasks"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["left"],
    left_on: Literal["d"],
    right_on: Literal["a"],
    shuffle: Literal["tasks"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["left"],
    left_on: Literal["e"],
    right_on: Literal["b"],
    shuffle: Literal["tasks"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["left"],
    left_on: List[Literal["b", "a"]],
    right_on: List[Literal["e", "d"]],
    shuffle: Literal["tasks"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["right"],
    left_on: Literal["a"],
    right_on: Literal["d"],
    shuffle: Literal["tasks"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["right"],
    left_on: Literal["b"],
    right_on: Literal["e"],
    shuffle: Literal["tasks"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["right"],
    left_on: Literal["d"],
    right_on: Literal["a"],
    shuffle: Literal["tasks"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["right"],
    left_on: Literal["e"],
    right_on: Literal["b"],
    shuffle: Literal["tasks"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["right"],
    left_on: List[Literal["b", "a"]],
    right_on: List[Literal["e", "d"]],
    shuffle: Literal["tasks"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: pandas.core.frame.DataFrame,
    /,
    *,
    how: Literal["inner"],
    indicator: bool,
    left_index: bool,
    left_on: None,
    npartitions: None,
    on: Literal["x"],
    right_index: bool,
    right_on: None,
    shuffle: None,
    suffixes: Tuple[Literal["_x"], Literal["_y"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["inner"],
    indicator: bool,
    left_index: bool,
    left_on: None,
    npartitions: None,
    on: Literal["x"],
    right_index: bool,
    right_on: None,
    shuffle: None,
    suffixes: Tuple[Literal["_x"], Literal["_y"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["left"],
    indicator: bool,
    left_index: bool,
    left_on: None,
    npartitions: None,
    on: None,
    right_index: bool,
    right_on: Literal["x"],
    shuffle: None,
    suffixes: Tuple[Literal["_x"], Literal["_y"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["left"],
    indicator: bool,
    left_index: bool,
    left_on: Literal["x"],
    npartitions: None,
    on: None,
    right_index: bool,
    right_on: None,
    shuffle: None,
    suffixes: Tuple[Literal["_x"], Literal["_y"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["right"],
    indicator: bool,
    left_index: bool,
    left_on: None,
    npartitions: None,
    on: None,
    right_index: bool,
    right_on: Literal["x"],
    shuffle: None,
    suffixes: Tuple[Literal["_x"], Literal["_y"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["right"],
    indicator: bool,
    left_index: bool,
    left_on: Literal["x"],
    npartitions: None,
    on: None,
    right_index: bool,
    right_on: None,
    shuffle: None,
    suffixes: Tuple[Literal["_x"], Literal["_y"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["inner"],
    indicator: bool,
    left_index: bool,
    left_on: None,
    npartitions: None,
    on: None,
    right_index: bool,
    right_on: Literal["x"],
    shuffle: None,
    suffixes: Tuple[Literal["_x"], Literal["_y"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["inner"],
    indicator: bool,
    left_index: bool,
    left_on: Literal["x"],
    npartitions: None,
    on: None,
    right_index: bool,
    right_on: None,
    shuffle: None,
    suffixes: Tuple[Literal["_x"], Literal["_y"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: dask.dataframe.core.DataFrame,
    right: pandas.core.frame.DataFrame,
    on: Literal["B"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    right_on: Literal["y"],
    left_index: bool,
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    left_index: bool,
    right_on: Literal["y"],
    shuffle: Literal["tasks"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: dask.dataframe.core.DataFrame,
    right: dask.dataframe.core.DataFrame,
    left_on: Literal["x"],
    right_on: dask.dataframe.core.Series,
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: dask.dataframe.core.DataFrame,
    right: dask.dataframe.core.DataFrame,
    left_on: dask.dataframe.core.Series,
    right_on: dask.dataframe.core.Series,
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["left"],
    left_index: bool,
    left_on: None,
    npartitions: None,
    right_index: bool,
    shuffle: None,
    suffixes: List[Literal["r", ""]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    _0: dask.dataframe.core.DataFrame,
    _1: dask.dataframe.core.DataFrame,
    /,
    *,
    how: Literal["left"],
    indicator: bool,
    left_index: bool,
    left_on: None,
    npartitions: None,
    on: None,
    right_index: bool,
    right_on: None,
    shuffle: None,
    suffixes: Tuple[Literal["_x"], Literal["_y"]],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge(
    left: dask.dataframe.core.DataFrame,
    right: dask.dataframe.core.DataFrame,
    how: Literal["outer"],
):
    """
    usage.dask: 1
    """
    ...


def merge(
    _0: Union[dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame] = ...,
    _1: Union[dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame] = ...,
    /,
    left: Union[dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame] = ...,
    right: Union[dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame] = ...,
    how: Literal["outer", "left", "inner", "right"] = ...,
    on: Union[
        None, List[Literal["idx", "k", "A"]], Literal["B", "x", "y", "idx"]
    ] = ...,
    left_on: Union[
        None,
        dask.dataframe.core.Series,
        List[Literal["y", "b", "a"]],
        Literal["x", "e", "d", "b", "a"],
    ] = ...,
    right_on: Union[
        None, List[Literal["y", "e", "d"]], str, dask.dataframe.core.Series
    ] = ...,
    left_index: bool = ...,
    right_index: bool = ...,
    suffixes: Union[
        Tuple[Literal["1", "_x"], Literal["2", "_y"]],
        List[Literal["_r", "_l", "", "r", "l"]],
    ] = ...,
    indicator: bool = ...,
    *,
    npartitions: None = ...,
    shuffle: Union[None, Literal["tasks", "disk"]] = ...,
):
    """
    usage.dask: 291
    """
    ...


@overload
def merge_asof(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    left_index: bool,
    right_index: bool,
):
    """
    usage.dask: 2
    """
    ...


@overload
def merge_asof(
    left: dask.dataframe.core.DataFrame,
    right: dask.dataframe.core.DataFrame,
    left_index: bool,
    right_index: bool,
):
    """
    usage.dask: 2
    """
    ...


@overload
def merge_asof(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    left_index: bool,
    right_index: bool,
    left_by: None,
    right_by: None,
    suffixes: Tuple[Literal["_x"], Literal["_y"]],
    tolerance: None,
    allow_exact_matches: bool,
    direction: Literal["backward"],
):
    """
    usage.dask: 2
    """
    ...


@overload
def merge_asof(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    on: Literal["a"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge_asof(
    left: dask.dataframe.core.DataFrame,
    right: dask.dataframe.core.DataFrame,
    on: Literal["a"],
):
    """
    usage.dask: 2
    """
    ...


@overload
def merge_asof(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    on: Literal["a"],
    allow_exact_matches: bool,
    direction: Literal["backward"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge_asof(
    left: dask.dataframe.core.DataFrame,
    right: dask.dataframe.core.DataFrame,
    on: Literal["a"],
    allow_exact_matches: bool,
    direction: Literal["backward"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge_asof(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    on: Literal["a"],
    allow_exact_matches: bool,
    direction: Literal["forward"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge_asof(
    left: dask.dataframe.core.DataFrame,
    right: dask.dataframe.core.DataFrame,
    on: Literal["a"],
    allow_exact_matches: bool,
    direction: Literal["forward"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge_asof(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    left_index: bool,
    right_index: bool,
    left_by: None,
    right_by: None,
    suffixes: Tuple[Literal["_x"], Literal["_y"]],
    tolerance: None,
    allow_exact_matches: bool,
    direction: Literal["forward"],
):
    """
    usage.dask: 2
    """
    ...


@overload
def merge_asof(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    on: Literal["a"],
    allow_exact_matches: bool,
    direction: Literal["nearest"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge_asof(
    left: dask.dataframe.core.DataFrame,
    right: dask.dataframe.core.DataFrame,
    on: Literal["a"],
    allow_exact_matches: bool,
    direction: Literal["nearest"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge_asof(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    left_index: bool,
    right_index: bool,
    left_by: None,
    right_by: None,
    suffixes: Tuple[Literal["_x"], Literal["_y"]],
    tolerance: None,
    allow_exact_matches: bool,
    direction: Literal["nearest"],
):
    """
    usage.dask: 2
    """
    ...


@overload
def merge_asof(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    left_on: Literal["a"],
    right_index: bool,
    allow_exact_matches: bool,
    direction: Literal["backward"],
):
    """
    usage.dask: 2
    """
    ...


@overload
def merge_asof(
    left: dask.dataframe.core.DataFrame,
    right: dask.dataframe.core.DataFrame,
    left_on: Literal["a"],
    right_index: bool,
    allow_exact_matches: bool,
    direction: Literal["backward"],
):
    """
    usage.dask: 2
    """
    ...


@overload
def merge_asof(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    left_on: Literal["a"],
    right_index: bool,
    allow_exact_matches: bool,
    direction: Literal["forward"],
):
    """
    usage.dask: 2
    """
    ...


@overload
def merge_asof(
    left: dask.dataframe.core.DataFrame,
    right: dask.dataframe.core.DataFrame,
    left_on: Literal["a"],
    right_index: bool,
    allow_exact_matches: bool,
    direction: Literal["forward"],
):
    """
    usage.dask: 2
    """
    ...


@overload
def merge_asof(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    left_on: Literal["a"],
    right_index: bool,
    allow_exact_matches: bool,
    direction: Literal["nearest"],
):
    """
    usage.dask: 2
    """
    ...


@overload
def merge_asof(
    left: dask.dataframe.core.DataFrame,
    right: dask.dataframe.core.DataFrame,
    left_on: Literal["a"],
    right_index: bool,
    allow_exact_matches: bool,
    direction: Literal["nearest"],
):
    """
    usage.dask: 2
    """
    ...


@overload
def merge_asof(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    on: Literal["time"],
    by: Literal["ticker"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge_asof(
    left: dask.dataframe.core.DataFrame,
    right: dask.dataframe.core.DataFrame,
    on: Literal["time"],
    by: Literal["ticker"],
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge_asof(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    left_index: bool,
    right_index: bool,
    left_by: Literal["ticker"],
    right_by: Literal["ticker"],
    suffixes: Tuple[Literal["_x"], Literal["_y"]],
    tolerance: None,
    allow_exact_matches: bool,
    direction: Literal["backward"],
):
    """
    usage.dask: 2
    """
    ...


@overload
def merge_asof(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    on: Literal["time"],
    by: Literal["ticker"],
    tolerance: pandas._libs.tslibs.timedeltas.Timedelta,
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge_asof(
    left: dask.dataframe.core.DataFrame,
    right: dask.dataframe.core.DataFrame,
    on: Literal["time"],
    by: Literal["ticker"],
    tolerance: pandas._libs.tslibs.timedeltas.Timedelta,
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge_asof(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    left_index: bool,
    right_index: bool,
    left_by: Literal["ticker"],
    right_by: Literal["ticker"],
    suffixes: Tuple[Literal["_x"], Literal["_y"]],
    tolerance: pandas._libs.tslibs.timedeltas.Timedelta,
    allow_exact_matches: bool,
    direction: Literal["backward"],
):
    """
    usage.dask: 2
    """
    ...


@overload
def merge_asof(
    left: pandas.core.frame.DataFrame,
    right: pandas.core.frame.DataFrame,
    on: Literal["time"],
    by: Literal["ticker"],
    tolerance: pandas._libs.tslibs.timedeltas.Timedelta,
    allow_exact_matches: bool,
):
    """
    usage.dask: 1
    """
    ...


@overload
def merge_asof(
    left: dask.dataframe.core.DataFrame,
    right: dask.dataframe.core.DataFrame,
    on: Literal["time"],
    by: Literal["ticker"],
    tolerance: pandas._libs.tslibs.timedeltas.Timedelta,
    allow_exact_matches: bool,
):
    """
    usage.dask: 1
    """
    ...


def merge_asof(
    left: Union[dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame],
    right: Union[dask.dataframe.core.DataFrame, pandas.core.frame.DataFrame],
    left_on: Literal["a"] = ...,
    on: Literal["time", "a"] = ...,
    by: Literal["ticker"] = ...,
    left_index: bool = ...,
    right_index: bool = ...,
    left_by: Union[Literal["ticker"], None] = ...,
    right_by: Union[Literal["ticker"], None] = ...,
    suffixes: Tuple[Literal["_x"], Literal["_y"]] = ...,
    tolerance: Union[pandas._libs.tslibs.timedeltas.Timedelta, None] = ...,
    allow_exact_matches: bool = ...,
    direction: Literal["backward", "nearest", "forward"] = ...,
):
    """
    usage.dask: 41
    """
    ...
