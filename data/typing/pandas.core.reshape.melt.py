from typing import *


def melt(
    frame: pandas.core.frame.DataFrame,
    id_vars: Literal["B", "C"] = ...,
    value_vars: Union[List[Literal["C", "A"]], Literal["C"]] = ...,
    var_name: Literal["myvar"] = ...,
    value_name: Literal["myval"] = ...,
):
    """
    usage.dask: 5
    """
    ...
