from typing import *


@overload
def pprint_thing(thing: Literal["x"]):
    """
    usage.dask: 2
    """
    ...


@overload
def pprint_thing(thing: Literal["y"]):
    """
    usage.dask: 2
    """
    ...


@overload
def pprint_thing(thing: int):
    """
    usage.dask: 2
    """
    ...


@overload
def pprint_thing(thing: numpy.dtype):
    """
    usage.dask: 2
    """
    ...


@overload
def pprint_thing(thing: Literal["C"]):
    """
    usage.dask: 2
    """
    ...


@overload
def pprint_thing(thing: Tuple[Literal["C"], Literal["count"]]):
    """
    usage.dask: 2
    """
    ...


@overload
def pprint_thing(thing: Tuple[Literal["C"], Literal["sum"]]):
    """
    usage.dask: 2
    """
    ...


@overload
def pprint_thing(thing: Literal["z"]):
    """
    usage.dask: 2
    """
    ...


@overload
def pprint_thing(thing: pandas.core.dtypes.dtypes.CategoricalDtype):
    """
    usage.dask: 1
    """
    ...


def pprint_thing(
    thing: Union[
        numpy.dtype,
        int,
        pandas.core.dtypes.dtypes.CategoricalDtype,
        Literal["z", "C", "y", "x"],
        Tuple[Literal["C"], Literal["count", "sum"]],
    ]
):
    """
    usage.dask: 17
    """
    ...


class PrettyDict:
    def __contains__(self, _0: int, /):
        """
        usage.dask: 1
        """
        ...

    def __iter__(self, /):
        """
        usage.dask: 1
        """
        ...
