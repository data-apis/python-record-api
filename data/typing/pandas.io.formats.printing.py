from typing import *


@overload
def pprint_thing(thing: Literal["0"]):
    """
    usage.koalas: 2
    """
    ...


@overload
def pprint_thing(thing: int):
    """
    usage.dask: 2
    usage.koalas: 1
    """
    ...


@overload
def pprint_thing(thing: Literal["a"]):
    """
    usage.koalas: 2
    """
    ...


@overload
def pprint_thing(thing: Literal["float64"]):
    """
    usage.koalas: 1
    """
    ...


@overload
def pprint_thing(thing: Literal["int64"]):
    """
    usage.koalas: 1
    """
    ...


@overload
def pprint_thing(thing: Literal["single"]):
    """
    usage.koalas: 1
    """
    ...


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
        Tuple[Literal["C"], Literal["count", "sum"]],
        str,
        pandas.core.dtypes.dtypes.CategoricalDtype,
        int,
        numpy.dtype,
    ]
):
    """
    usage.dask: 17
    usage.koalas: 8
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
