from typing import *


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


def is_dict_like(obj: Union[dask.dataframe.core.Series, pandas.core.series.Series]):
    """
    usage.dask: 3
    """
    ...
