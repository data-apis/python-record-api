from typing import *


def melt(
    frame: pandas.core.frame.DataFrame,
    id_vars: Literal["B", "C"] = ...,
    value_vars: Union[List[Literal["C", "A"]], Literal["C"]] = ...,
    value_name: Literal["myval"] = ...,
    var_name: Literal["myvar"] = ...,
):
    """
    usage.dask: 5
    """
    ...
