from typing import *

# usage.scipy: 1
recarray: object

# usage.scipy: 1
record: object


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
                Literal[
                    "2014-01-11T00:00:00",
                    "1976-03-05T00:00:01",
                    "1983-07-09T17:17:34",
                    "2054-06-20T14:31:45",
                    "2000-10-31T11:50:23",
                ],
                int,
            ]
        ]
    ],
    names: List[Literal["c", "b", "a"]],
):
    """
    usage.matplotlib: 2
    """
    ...
