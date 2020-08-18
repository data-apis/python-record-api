from typing import *


@overload
def union_categoricals(to_union: List[pandas.core.series.Series]):
    """
    usage.dask: 8
    """
    ...


@overload
def union_categoricals(to_union: List[pandas.core.indexes.category.CategoricalIndex]):
    """
    usage.dask: 5
    """
    ...


@overload
def union_categoricals(
    to_union: List[
        Union[pandas.core.series.Series, pandas.core.arrays.categorical.Categorical]
    ]
):
    """
    usage.dask: 1
    """
    ...


@overload
def union_categoricals(
    to_union: List[
        Union[pandas.core.arrays.categorical.Categorical, pandas.core.series.Series]
    ]
):
    """
    usage.dask: 1
    """
    ...


def union_categoricals(
    to_union: List[
        Union[
            pandas.core.indexes.category.CategoricalIndex,
            pandas.core.series.Series,
            pandas.core.arrays.categorical.Categorical,
        ]
    ]
):
    """
    usage.dask: 15
    """
    ...
