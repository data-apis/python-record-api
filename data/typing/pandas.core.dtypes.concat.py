from typing import *


def union_categoricals(
    to_union: List[
        Union[
            pandas.core.series.Series,
            pandas.core.indexes.category.CategoricalIndex,
            pandas.core.arrays.categorical.Categorical,
        ]
    ]
):
    """
    usage.dask: 14
    """
    ...
