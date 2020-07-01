from typing import *


def pivot_table(
    data: pandas.core.frame.DataFrame,
    values: Literal["C", "B"],
    index: Literal["A"],
    columns: Literal["B", "C"],
    aggfunc: Literal["count", "sum", "mean"],
):
    """
    usage.dask: 7
    """
    ...
