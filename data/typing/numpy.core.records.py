from typing import *

# usage.scipy: 1
recarray: object

# usage.scipy: 1
record: object


@overload
def array(
    obj: List[Tuple[int, float, float]],
    dtype: List[Tuple[Literal["group", "group_10", "group_11"], type]],
):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def array(
    obj: List[Tuple[int, int, float, float]],
    dtype: List[Tuple[Literal["group", "whatever", "group_10", "group_11"], type]],
):
    """
    usage.statsmodels: 1
    """
    ...


def array(
    obj: List[Tuple[Union[float, int], ...]],
    dtype: List[Tuple[Literal["group", "whatever", "group_10", "group_11"], type]],
):
    """
    usage.statsmodels: 2
    """
    ...


def fromarrays(
    arrayList: List[numpy.ndarray],
    dtype: Union[
        Dict[Literal["formats", "names"], List[Union[str, numpy.dtype]]],
        List[Tuple[Literal["EXPIRY"], Literal["<M8[ns]"]]],
    ],
):
    """
    usage.pandas: 9
    """
    ...


@overload
def fromrecords(recList: List[List[int]], names: Literal["group"]):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def fromrecords(recList: List[List[int]], names: List[Literal["whatever", "group"]]):
    """
    usage.statsmodels: 1
    """
    ...


@overload
def fromrecords(recList: List[List[int]], names: List[Literal["c", "b", "a"]]):
    """
    usage.matplotlib: 1
    """
    ...


@overload
def fromrecords(
    recList: List[
        List[
            Literal[
                "2014-01-11T00:00:00",
                "1976-03-05T00:00:01",
                "1983-07-09T17:17:34",
                "2054-06-20T14:31:45",
                "2000-10-31T11:50:23",
            ]
        ]
    ],
    names: List[Literal["a"]],
):
    """
    usage.matplotlib: 1
    """
    ...


def fromrecords(
    recList: List[
        List[
            Union[
                int,
                Literal[
                    "2014-01-11T00:00:00",
                    "1976-03-05T00:00:01",
                    "1983-07-09T17:17:34",
                    "2054-06-20T14:31:45",
                    "2000-10-31T11:50:23",
                ],
            ]
        ]
    ],
    names: Union[List[Literal["whatever", "group", "c", "b", "a"]], Literal["group"]],
):
    """
    usage.matplotlib: 2
    usage.statsmodels: 2
    """
    ...
