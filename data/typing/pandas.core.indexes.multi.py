from typing import *


class MultiIndex:

    # usage.dask: 1
    __module__: ClassVar[object]

    # usage.dask: 3
    # usage.xarray: 1
    __name__: ClassVar[object]

    @overload
    @classmethod
    def from_arrays(
        cls,
        /,
        arrays: List[List[Union[Literal["b", "a"], int]]],
        sortorder: None,
        names: List[Literal["number", "word"]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_arrays(
        cls,
        /,
        arrays: List[List[str]],
        names: Tuple[Literal["first"], Literal["second"]],
    ):
        """
        usage.koalas: 4
        """
        ...

    @overload
    @classmethod
    def from_arrays(
        cls,
        /,
        arrays: Tuple[List[Literal["c", "b", "a"]], List[Literal["f", "e", "d"]]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_arrays(
        cls,
        /,
        arrays: List[List[Union[int, Literal["blue", "red"]]]],
        names: Tuple[Literal["number"], Literal["color"]],
    ):
        """
        usage.koalas: 4
        """
        ...

    @overload
    @classmethod
    def from_arrays(cls, /, arrays: List[List[Literal["b", "a", "blue", "red"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_arrays(
        cls,
        /,
        arrays: List[List[Literal["b", "a", "blue", "red"]]],
        sortorder: None,
        names: None,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_arrays(cls, /, arrays: List[List[Union[Literal["b", "a"], int]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_arrays(
        cls,
        /,
        arrays: List[List[Union[Literal["b", "a"], int]]],
        names: List[Literal["number", "word"]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_arrays(
        cls,
        /,
        arrays: List[List[Union[Literal["b", "a"], int]]],
        names: List[Union[None, Literal["word"]]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_arrays(
        cls, /, arrays: List[List[int]], names: List[Literal["month", "year"]]
    ):
        """
        usage.alphalens: 1
        """
        ...

    @overload
    @classmethod
    def from_arrays(cls, /, arrays: List[xarray.coding.cftimeindex.CFTimeIndex]):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def from_arrays(
        cls,
        /,
        arrays: List[List[Literal["b", "a", "z", "y"]]],
        names: List[Literal["y2", "y1"]],
    ):
        """
        usage.xarray: 2
        """
        ...

    @overload
    @classmethod
    def from_arrays(
        cls,
        /,
        arrays: List[
            Union[
                pandas.core.indexes.category.CategoricalIndex,
                pandas.core.indexes.numeric.Int64Index,
            ]
        ],
        names: pandas.core.indexes.frozen.FrozenList,
    ):
        """
        usage.dask: 1
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def from_arrays(
        cls,
        /,
        arrays: List[
            Union[pandas.core.indexes.datetimes.DatetimeIndex, List[Literal["b", "a"]]]
        ],
        names: Tuple[Literal["level_str"], Literal["level_date"]],
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def from_arrays(
        cls,
        /,
        arrays: List[List[Union[int, Literal["c", "b", "a"]]]],
        names: List[Literal["y", "x"]],
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def from_arrays(cls, /, arrays: List[List[int]], names: List[Literal["y", "x"]]):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def from_arrays(
        cls,
        /,
        arrays: List[pandas.core.indexes.category.CategoricalIndex],
        names: pandas.core.indexes.frozen.FrozenList,
    ):
        """
        usage.dask: 1
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def from_arrays(cls, /, arrays: List[pandas.core.series.Series]):
        """
        usage.statsmodels: 4
        """
        ...

    @overload
    @classmethod
    def from_arrays(
        cls,
        /,
        arrays: List[
            Union[List[Literal["infl"]], pandas.core.indexes.period.PeriodIndex]
        ],
        names: List[Literal["revised variable", "revision date"]],
    ):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def from_arrays(
        cls,
        /,
        arrays: List[
            Union[List[Literal["infl"]], pandas.core.indexes.period.PeriodIndex]
        ],
        names: List[Literal["updated variable", "update date"]],
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def from_arrays(
        cls,
        /,
        arrays: List[list],
        names: List[Literal["revised variable", "revision date"]],
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def from_arrays(
        cls,
        /,
        arrays: List[list],
        names: List[Literal["updated variable", "update date"]],
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def from_arrays(cls, /, arrays: List[numpy.ndarray]):
        """
        usage.modin: 2
        """
        ...

    @overload
    @classmethod
    def from_arrays(cls, /, arrays: List[pandas.core.indexes.numeric.Float64Index]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    @classmethod
    def from_arrays(cls, /, arrays: List[pandas.core.indexes.numeric.Int64Index]):
        """
        usage.dask: 2
        usage.seaborn: 1
        """
        ...

    @overload
    @classmethod
    def from_arrays(
        cls,
        /,
        arrays: List[
            Union[
                pandas.core.indexes.numeric.Int64Index,
                pandas.core.indexes.category.CategoricalIndex,
            ]
        ],
        names: pandas.core.indexes.frozen.FrozenList,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def from_arrays(cls, /, arrays: List[pandas.core.indexes.base.Index]):
        """
        usage.dask: 2
        """
        ...

    @classmethod
    def from_arrays(
        cls,
        /,
        arrays: Union[
            list, Tuple[List[Literal["c", "b", "a"]], List[Literal["f", "e", "d"]]]
        ],
        sortorder: None = ...,
        names: Union[
            pandas.core.indexes.frozen.FrozenList,
            Tuple[
                Literal["first", "number", "level_str"],
                Literal["second", "color", "level_date"],
            ],
            None,
            List[Union[str, None]],
        ] = ...,
    ):
        """
        usage.alphalens: 1
        usage.dask: 7
        usage.koalas: 15
        usage.modin: 2
        usage.seaborn: 2
        usage.statsmodels: 9
        usage.xarray: 8
        """
        ...

    @overload
    @classmethod
    def from_product(cls, /, iterables: List[List[Literal["two", "one", "b", "a"]]]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls, /, iterables: List[List[Union[int, Literal["purple", "green"]]]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[List[Union[int, Literal["purple", "green"]]]],
        sortorder: None,
        names: None,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[
                pandas.core.indexes.base.Index,
                pandas.core.indexes.datetimes.DatetimeIndex,
            ]
        ],
        names: List[Literal["asset", "date"]],
    ):
        """
        usage.alphalens: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[List[Literal["B", "A"]], pandas.core.indexes.datetimes.DatetimeIndex]
        ],
        names: List[Literal["asset", "date"]],
    ):
        """
        usage.alphalens: 3
        """
        ...

    @overload
    @classmethod
    def from_product(cls, /, iterables: List[List[Union[int, Literal["b", "a"]]]]):
        """
        usage.xarray: 2
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[List[Union[Literal["d", "c", "b", "a"], int]]],
        names: Tuple[Literal["level_1"], Literal["level_2"]],
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[List[Union[Literal["b", "a"], int]]],
        names: Tuple[Literal["one"], Literal["two"], Literal["three"]],
    ):
        """
        usage.xarray: 4
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: pandas.core.indexes.frozen.FrozenList,
        names: pandas.core.indexes.frozen.FrozenList,
    ):
        """
        usage.xarray: 2
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[List[Union[int, Literal["c", "b", "a"]]]],
        names: List[Literal["y", "x"]],
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[
                pandas.core.indexes.base.Index, pandas.core.indexes.numeric.Int64Index
            ]
        ],
        names: List[Literal["y", "x"]],
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[List[Union[Literal["c", "b", "a"], int]]],
        names: List[Literal["x", "y"]],
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[
                pandas.core.indexes.numeric.Int64Index, pandas.core.indexes.base.Index
            ]
        ],
        names: List[Literal["x", "y"]],
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[
                pandas.core.indexes.base.Index, pandas.core.indexes.numeric.Int64Index
            ]
        ],
        names: List[Literal["A", "B"]],
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[pandas.core.indexes.range.RangeIndex],
        names: List[Literal["y", "x"]],
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[List[Union[Literal["b", "a"], int]]],
        names: Tuple[Literal["level_1"], Literal["level_2"]],
    ):
        """
        usage.xarray: 2
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[List[Union[Literal["b", "a"], int]]],
        names: Tuple[str, Literal["level_2"]],
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[List[Union[Literal["c", "b", "a"], int]]],
        names: Tuple[Literal["one"], Literal["two"]],
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[List[Union[int, Literal["b", "a"]]]],
        names: List[Literal["y", "x"]],
    ):
        """
        usage.xarray: 2
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[List[Union[Literal["b", "a"], int]]],
        names: List[Literal["x", "y"]],
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[pandas.core.indexes.base.Index, pandas.core.indexes.range.RangeIndex]
        ],
        names: List[Literal["y", "x"]],
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[pandas.core.indexes.numeric.Int64Index],
        names: List[Literal["y", "x"]],
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[Union[range, List[Literal["a"]]]],
        names: List[Literal["two", "one"]],
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[
                pandas.core.indexes.numeric.Int64Index, pandas.core.indexes.base.Index
            ]
        ],
        names: List[Literal["two", "one"]],
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[
                pandas.core.indexes.range.RangeIndex,
                pandas.core.indexes.numeric.Int64Index,
            ]
        ],
        names: List[Literal["y", "x"]],
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[List[Union[Literal["b", "a"], int]]],
        names: Tuple[Literal["one"], Literal["two"]],
    ):
        """
        usage.xarray: 2
        """
        ...

    @overload
    @classmethod
    def from_product(cls, /, iterables: List[List[int]]):
        """
        usage.xarray: 3
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls, /, iterables: List[numpy.ndarray], names: List[Literal["y", "x"]]
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def from_product(cls, /, iterables: List[List[Union[Literal["a", "b"], int]]]):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def from_product(cls, /, iterables: List[List[Union[Literal["c", "b", "a"], int]]]):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def from_product(cls, /, iterables: List[List[Union[Literal["b", "a"], int]]]):
        """
        usage.dask: 1
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[List[Union[Literal["b", "a"], int]]],
        names: List[Literal["level_2", "level_1"]],
    ):
        """
        usage.xarray: 2
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: Tuple[List[str], List[Literal["const"]]],
        names: Tuple[Literal["y"], None],
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls, /, iterables: Tuple[List[str], List[str]], names: Tuple[Literal["y"], None]
    ):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: Tuple[List[str], List[Literal["x4", "x3", "x2", "x1", "const"]]],
        names: Tuple[Literal["y"], None],
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: Tuple[List[str], List[str]],
        names: Tuple[Literal["PID"], None],
    ):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: Tuple[List[Literal["1"]], List[Literal["const"]]],
        names: Tuple[Literal["y"], None],
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: Tuple[List[Literal["1.1"]], List[Literal["B", "Intercept"]]],
        names: Tuple[Literal["A"], None],
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[List[Literal["state.0"]], pandas.core.indexes.datetimes.DatetimeIndex]
        ],
    ):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[
                List[Literal["state.2", "state.1", "state.0"]],
                pandas.core.indexes.datetimes.DatetimeIndex,
            ]
        ],
    ):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[
                List[Literal["state.1", "state.0"]],
                pandas.core.indexes.datetimes.DatetimeIndex,
            ]
        ],
    ):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[
                List[Literal["state.3", "state.2", "state.1", "state.0"]],
                pandas.core.indexes.datetimes.DatetimeIndex,
            ]
        ],
    ):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: Tuple[
            List[Literal["x2", "x1", "x0", "const"]],
            Tuple[Literal["lower"], Literal["upper"]],
        ],
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: Tuple[
            pandas.core.indexes.datetimes.DatetimeIndex,
            List[Literal["x2", "x1", "x0", "const"]],
        ],
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: Tuple[
            List[Literal["x1", "const"]], Tuple[Literal["lower"], Literal["upper"]]
        ],
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: Tuple[
            List[Literal["x2", "x1", "x0"]], Tuple[Literal["lower"], Literal["upper"]]
        ],
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: Tuple[
            pandas.core.indexes.datetimes.DatetimeIndex, List[Literal["x2", "x1", "x0"]]
        ],
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: Tuple[
            List[Literal["const"]], Tuple[Literal["lower"], Literal["upper"]]
        ],
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: Tuple[
            pandas.core.indexes.datetimes.DatetimeIndex, List[Literal["const"]]
        ],
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[
                List[Literal["state.4", "state.3", "state.2", "state.1", "state.0"]],
                pandas.core.indexes.datetimes.DatetimeIndex,
            ]
        ],
    ):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: Tuple[List[Literal["L1.y2", "L1.y1"]], List[Literal["y2", "y1"]]],
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[List[Literal["f1"]], pandas.core.indexes.datetimes.DatetimeIndex]
        ],
    ):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[
                List[Literal["f1.L1", "f1"]],
                pandas.core.indexes.datetimes.DatetimeIndex,
            ]
        ],
    ):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[
                List[Literal["f2", "f1"]], pandas.core.indexes.datetimes.DatetimeIndex
            ]
        ],
    ):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: Tuple[
            List[Literal["L1.y3", "L1.y2", "L1.y1"]], List[Literal["y3", "y2", "y1"]]
        ],
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[
                List[Literal["e(dln_consump)", "e(dln_inc)", "e(dln_inv)", "f1"]],
                pandas.core.indexes.datetimes.DatetimeIndex,
            ]
        ],
    ):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[Union[List[str], pandas.core.indexes.datetimes.DatetimeIndex]],
    ):
        """
        usage.statsmodels: 9
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[List[Literal["dummy"]], pandas.core.indexes.datetimes.DatetimeIndex]
        ],
    ):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[
                List[Literal["e(dln_inc)", "e(dln_inv)"]],
                pandas.core.indexes.datetimes.DatetimeIndex,
            ]
        ],
    ):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[List[Literal["f1"]], pandas.core.indexes.range.RangeIndex]
        ],
    ):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[
                List[Literal["global.2", "global.1"]],
                pandas.core.indexes.period.PeriodIndex,
            ]
        ],
    ):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[
                List[Literal["block", "global"]], pandas.core.indexes.period.PeriodIndex
            ]
        ],
    ):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[List[Literal["0"]], pandas.core.indexes.period.PeriodIndex]
        ],
    ):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[
                List[Literal["eps_M.1", "eps_M.0", "0"]],
                pandas.core.indexes.period.PeriodIndex,
            ]
        ],
    ):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[Union[List[str], pandas.core.indexes.period.PeriodIndex]],
    ):
        """
        usage.statsmodels: 39
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[Union[numpy.ndarray, pandas.core.indexes.period.PeriodIndex]],
    ):
        """
        usage.statsmodels: 5
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[List[Literal["0"]], pandas.core.indexes.range.RangeIndex]
        ],
    ):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def from_product(cls, /, iterables: List[Union[numpy.ndarray, List[Literal["y"]]]]):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls, /, iterables: List[Union[numpy.ndarray, List[Literal["y2", "y1"]]]]
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[
                List[Literal["eps_M.f1", "0"]], pandas.core.indexes.period.PeriodIndex
            ]
        ],
    ):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[
                List[Literal["eps_M.f2", "eps_M.f1", "0"]],
                pandas.core.indexes.period.PeriodIndex,
            ]
        ],
    ):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def from_product(cls, /, iterables: Tuple[List[str], List[Literal["y2", "y1"]]]):
        """
        usage.statsmodels: 8
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: Tuple[
            List[Literal["L2.y2", "L2.y1", "L1.y2", "L1.y1"]], List[Literal["y2", "y1"]]
        ],
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls, /, iterables: Tuple[List[str], List[Literal["y3", "y2", "y1"]]]
    ):
        """
        usage.statsmodels: 7
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[
                List[Literal["level", "error"]], pandas.core.indexes.period.PeriodIndex
            ]
        ],
    ):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[
                List[Literal["trend", "level", "error"]],
                pandas.core.indexes.period.PeriodIndex,
            ]
        ],
    ):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[List[Literal["state.0"]], pandas.core.indexes.range.RangeIndex]
        ],
    ):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[
                List[Literal["state.1", "state.0"]],
                pandas.core.indexes.range.RangeIndex,
            ]
        ],
    ):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[List[Literal["f1.L1", "f1"]], pandas.core.indexes.range.RangeIndex]
        ],
    ):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[List[Literal["f2", "f1"]], pandas.core.indexes.range.RangeIndex]
        ],
    ):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[
                List[Literal["state.3", "state.2", "state.1", "state.0"]],
                pandas.core.indexes.range.RangeIndex,
            ]
        ],
    ):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[List[Literal["level"]], pandas.core.indexes.range.RangeIndex]
        ],
    ):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[List[Literal["trend", "level"]], pandas.core.indexes.range.RangeIndex]
        ],
    ):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[List[Literal["state.0"]], pandas.core.indexes.period.PeriodIndex]
        ],
    ):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[List[Literal["beta.0"]], pandas.core.indexes.datetimes.DatetimeIndex]
        ],
    ):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[
                List[Literal["state.1", "state.0"]],
                pandas.core.indexes.period.PeriodIndex,
            ]
        ],
    ):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[
                pandas.core.indexes.base.Index, pandas.core.indexes.period.PeriodIndex
            ]
        ],
    ):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[
                pandas.core.indexes.base.Index,
                pandas.core.indexes.datetimes.DatetimeIndex,
            ]
        ],
    ):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[
                List[Literal["state.1", "state.0"]],
                pandas.core.indexes.numeric.Int64Index,
            ]
        ],
    ):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[
                pandas.core.indexes.base.Index, pandas.core.indexes.numeric.Int64Index
            ]
        ],
    ):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[pandas.core.indexes.base.Index, pandas.core.indexes.range.RangeIndex]
        ],
    ):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[List[Literal["infl"]], pandas.core.indexes.period.PeriodIndex]
        ],
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[list],
        names: List[Literal["updated variable", "update date"]],
    ):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[List[Literal["level"]], pandas.core.indexes.period.PeriodIndex]
        ],
    ):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[
                List[Literal["unemp", "realgdp"]],
                pandas.core.indexes.period.PeriodIndex,
            ]
        ],
        names: List[Literal["revised variable", "revision date"]],
    ):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[
                List[Literal["unemp", "realgdp"]],
                pandas.core.indexes.period.PeriodIndex,
            ]
        ],
        names: List[Literal["updated variable", "update date"]],
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[
                List[Literal["unemp", "realgdp"]],
                pandas.core.indexes.period.PeriodIndex,
            ]
        ],
        names: List[Literal["impacted variables", "impact dates"]],
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[
                List[Literal["unemp", "realgdp"]],
                pandas.core.indexes.period.PeriodIndex,
            ]
        ],
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[list],
        names: List[Literal["revised variable", "revision date"]],
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[List[Literal["f1.L1", "f1"]], pandas.core.indexes.period.PeriodIndex]
        ],
    ):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[numpy.ndarray, pandas.core.indexes.datetimes.DatetimeIndex]
        ],
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[Union[numpy.ndarray, pandas.core.indexes.range.RangeIndex]],
    ):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[List[Literal["state.0"]], pandas.core.indexes.numeric.Int64Index]
        ],
    ):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[Union[numpy.ndarray, pandas.core.indexes.numeric.Int64Index]],
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[List[Literal["level"]], pandas.core.indexes.datetimes.DatetimeIndex]
        ],
    ):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def from_product(cls, /, iterables: List[List[Union[Literal["y"], int]]]):
        """
        usage.statsmodels: 4
        """
        ...

    @overload
    @classmethod
    def from_product(cls, /, iterables: List[List[Union[Literal["y2", "y1"], int]]]):
        """
        usage.statsmodels: 4
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[
                List[Literal["trend", "level"]],
                pandas.core.indexes.datetimes.DatetimeIndex,
            ]
        ],
    ):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[
                List[Literal["cycle.auxilliary", "cycle"]],
                pandas.core.indexes.datetimes.DatetimeIndex,
            ]
        ],
    ):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[
                List[Literal["seasonal.L2", "seasonal.L1", "seasonal"]],
                pandas.core.indexes.datetimes.DatetimeIndex,
            ]
        ],
    ):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[
                List[
                    Literal[
                        "freq_seasonal.3",
                        "freq_seasonal.2",
                        "freq_seasonal.1",
                        "freq_seasonal.0",
                    ]
                ],
                pandas.core.indexes.datetimes.DatetimeIndex,
            ]
        ],
    ):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[
                List[Literal["beta.realgdp"]],
                pandas.core.indexes.datetimes.DatetimeIndex,
            ]
        ],
    ):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[List[Literal["beta.x1"]], pandas.core.indexes.datetimes.DatetimeIndex]
        ],
    ):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: List[
            Union[
                List[Literal["ar.L1", "trend", "level"]],
                pandas.core.indexes.datetimes.DatetimeIndex,
            ]
        ],
    ):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: Tuple[
            List[Literal["L1.realinv", "L1.realcons", "L1.realgdp", "const"]],
            List[Literal["realinv", "realcons", "realgdp"]],
        ],
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: Tuple[
            List[Literal["const"]], List[Literal["realinv", "realcons", "realgdp"]]
        ],
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls, /, iterables: Tuple[List[Literal["L1.1", "L1.0", "const"]], List[int]]
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: Tuple[
            List[Literal["L2.y", "L2.x", "L1.y", "L1.x", "const"]],
            List[Literal["y", "x"]],
        ],
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: Tuple[
            Tuple[
                Literal["const"],
                Literal["L1.x"],
                Literal["L1.y"],
                Literal["L2.x"],
                Literal["L2.y"],
            ],
            Tuple[Literal["x"], Literal["y"]],
        ],
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: Tuple[
            List[Literal["exog_3", "exog_2", "exog_1", "exog_0", "const"]],
            List[Literal["endog_1", "endog_0"]],
        ],
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls, /, iterables: Tuple[List[str], List[Literal["endog_1", "endog_0"]]]
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: Tuple[
            List[Literal["L1.y2", "L1.y1", "const"]], List[Literal["y2", "y1"]]
        ],
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def from_product(cls, /, iterables: Tuple[List[str], List[str]]):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: Tuple[
            List[
                Literal["L1.realinv", "L1.realcons", "L1.realgdp", "exovar1", "const"]
            ],
            List[Literal["realinv", "realcons", "realgdp"]],
        ],
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls,
        /,
        iterables: Tuple[
            List[Literal["L1.y3", "L1.y2", "L1.y1", "x1", "const"]],
            List[Literal["y3", "y2", "y1"]],
        ],
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def from_product(cls, /, iterables: List[pandas.core.indexes.base.Index]):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def from_product(
        cls, /, iterables: List[Union[List[Literal["e", "d", "c", "b", "a"]], range]]
    ):
        """
        usage.dask: 1
        """
        ...

    @classmethod
    def from_product(
        cls,
        /,
        iterables: Union[
            list,
            pandas.core.indexes.frozen.FrozenList,
            Tuple[
                Union[
                    pandas.core.indexes.datetimes.DatetimeIndex,
                    List[str],
                    Tuple[
                        Literal["const"],
                        Literal["L1.x"],
                        Literal["L1.y"],
                        Literal["L2.x"],
                        Literal["L2.y"],
                    ],
                ],
                Union[
                    List[Union[str, int]],
                    Tuple[Literal["x", "lower"], Literal["y", "upper"]],
                ],
            ],
        ],
        sortorder: None = ...,
        names: Union[
            Tuple[Union[str, None], ...],
            List[str],
            None,
            pandas.core.indexes.frozen.FrozenList,
        ] = ...,
    ):
        """
        usage.alphalens: 4
        usage.dask: 3
        usage.koalas: 4
        usage.statsmodels: 260
        usage.xarray: 38
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["x", "id-x"], Literal["y", "id-y"]]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["x", "y", "z"], Literal["a", "b", "c", "d", "e"]]],
        sortorder: None,
        names: None,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["z", "y", "x"], Literal["a", "b", "c", "d", "e"]]],
        sortorder: None,
        names: None,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["z", "y", "x"], Literal["e", "d", "c", "b", "a"]]],
        sortorder: None,
        names: None,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["x"], Literal["a", "b", "c"]]],
        sortorder: None,
        names: None,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["A", "B", "C"], Literal["sum", "min"]]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["A", "B"], Literal["sum", "min", "max"]]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["num"], Literal["a", "b"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["num"], Literal["b"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["a", "b"], Literal["x", "y", "z", "w"]]]
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["b"], Literal["z", "w"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[int, int]], names: List[Literal["b", "a"]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["c", "d"], Literal["e", "f"]]],
        names: List[Literal["level_2", "level_1"]],
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["c", "d"], Literal["e", "f"]]]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["a", "b", "c"], Literal["x", "y", "z"]]]
    ):
        """
        usage.koalas: 12
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["__tmp_other_col_A__", "__tmp_other_col_B__"]]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["that", "this"], str]]):
        """
        usage.koalas: 8
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["this", "that"], str]]):
        """
        usage.koalas: 8
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["a", "b"], Literal["foo", "bar", "baz"]]]
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["a", "b"], Literal["foo", "baz"]]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[Literal["level_0", "a", "b"], Literal["", "bar", "foo", "baz"]]
        ],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["D"], Literal["bar", "foo"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["D", "E"], Literal["bar", "foo"]]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["a", "b"], Literal["name", "class", "max_speed"]]],
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["b"], Literal["max_speed"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["X", "Y"], Literal["A", "B", "C", "D"]]]
    ):
        """
        usage.koalas: 4
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["x", "y"], Literal["A", "B", "C", "D"]]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[
                Literal["bird", "mammal"], Literal["falcon", "parrot", "lion", "monkey"]
            ]
        ],
        names: List[Literal["name", "class"]],
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["speed", "species"], Literal["max", "type"]]]
    ):
        """
        usage.koalas: 3
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[Literal["class", "speed", "species"], Literal["", "max", "type"]]
        ],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[Literal["", "speed", "species"], Literal["class", "max", "type"]]
        ],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[Literal["species", "speed"], Literal["class", "max", "type"]]
        ],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[Literal["genus", "speed", "species"], Literal["class", "max", "type"]]
        ],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["weight"], Literal["kg", "pounds"]]]
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["weight", "height"], Literal["kg", "m"]]]
    ):
        """
        usage.koalas: 3
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["X"], Literal["A", "B"]]]):
        """
        usage.koalas: 8
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["X", "Y"], Literal["A", "B", "C"]]]
    ):
        """
        usage.koalas: 8
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["B", "C"], Literal["a", "b", "c"]]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["__tmp_cond_col_A__", "__tmp_cond_col_B__"]]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[
                Literal["that", "this"],
                Literal["__tmp_cond_col_A__", "__tmp_cond_col_B__", "A", "B"],
            ]
        ],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[
                Literal["this", "that"],
                Literal["A", "B", "__tmp_cond_col_A__", "__tmp_cond_col_B__"],
            ]
        ],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["x", "y"], Literal["a", "b"]]]):
        """
        usage.koalas: 8
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["b", "c"], str]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["B"], Literal["min", "max"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["B", "C"], Literal["min", "max"]]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["a", "b", "c"], Literal["x", "y", "z"]]],
        sortorder: None,
        names: None,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["a", "b"], Literal["x", "y"]]],
        sortorder: None,
        names: None,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["a", "b", "c"], Literal["x", "y", "z"], int]],
        sortorder: None,
        names: None,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["a", "b", "k"], Literal["x", "z"], int]],
        sortorder: None,
        names: None,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["c", "b", "a"], Literal["z", "y", "x"]]],
        sortorder: None,
        names: None,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["a", "b"], Literal["x", "y"], int]],
        sortorder: None,
        names: None,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["x", "y"], Literal["a", "b", "c"]]],
        sortorder: None,
        names: None,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["a", "c", "b"], Literal["x", "y", "z"], int]],
        sortorder: None,
        names: None,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["x"], Literal["a", "b", "c", "d"]]],
        sortorder: None,
        names: None,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["x"], Literal["c", "d", "e", "f"]]],
        sortorder: None,
        names: None,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["x", "y"], Literal["a", "b"]]],
        sortorder: None,
        names: None,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[Literal["2019-01-01T00:00:00"], Literal["2019-01-01T00:00:00"]]
        ],
        sortorder: None,
        names: None,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[int, Literal["red", "blue"]]],
        sortorder: None,
        names: Tuple[Literal["number"], Literal["color"]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["a", "b"], Literal["x", "y", "z"]]],
        names: List[Literal["column_labels_b", "column_labels_a"]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["foo", "zoo"], Literal["bar"]]],
        names: List[Literal["row_index_b", "row_index_a"]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["a", "b"], Literal["x", "y", "z"]]]
    ):
        """
        usage.koalas: 7
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["a", "b"], Literal["y", "z"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[
                Literal["this", "that"], Literal["letter", "number", "animal", "name"]
            ]
        ],
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["0"], Literal["min", "max"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["x", "y"], Literal["a", "b", "c"]]],
        names: List[Literal["level_2", "level_1"]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["0"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[
                Literal["that", "this"],
                Literal["__tmp_other_col__", "0", "__tmp_cond_col__"],
            ]
        ],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[
                Literal["this", "that"],
                Literal["0", "__tmp_cond_col__", "__tmp_other_col__"],
            ]
        ],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["x"], Literal["a"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["this"], Literal["a"]]]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[Literal["x", "__dummy__", ""], Literal["a", "", "__dummy__"]]
        ],
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["col_X"], Literal["col_A", "col_B"]]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[Literal["Xfirst_series"], Literal["Afirst_series", "Bfirst_series"]]
        ],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["a", "b", "c"], str]]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["A"], Literal["X", "Y"]]]):
        """
        usage.koalas: 3
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["x", "y"], Literal["a", "b", "c"]]]
    ):
        """
        usage.koalas: 21
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["x", "y"], Literal["a", "b", "w"]]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["x", "y", "a"], Literal["a", "b", "w", "c"]]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[Literal["x", "y", "a", "Z"], Literal["a", "b", "w", "c", ""]]
        ],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["that", "this"], Literal["x", "index", "a", "b"]]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["this", "that"], Literal["index", "a", "b", "x"]]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["A", "B"], Literal["one", "two"]]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[
                Literal["x", "y.z"],
                Literal["a", "b", "c.d"],
                Literal["1", "2", "3", "4"],
            ]
        ],
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["a", "b"], Literal["1", "2", "4"]]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["c.d"], Literal["3"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["x"], Literal["a"], Literal["1"]]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[Literal["X", "Y"], Literal["A", "B", "C", "D"], Literal["Z"]]
        ],
        names: List[Literal["lv_3", "lvl_2", "lvl_1"]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[Literal["X", "Y"], Literal["A", "B", "C", "D"], Literal["Z"]]
        ],
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["A", "B"], Literal["Z"]]]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["X"], Literal["A"], Literal["Z"]]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["x", "y"], Literal["Col1", "Col2", "Col3"]]]
    ):
        """
        usage.koalas: 3
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["b"], Literal["z"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["a"], Literal["y"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: zip):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["x", "y", "z"], Literal["a", "b", "c"]]]
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["x", "y"], Literal["a", "b", "c"]]],
        names: List[Literal["index2", "index1"]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["A", "B"], Literal["Z", "X"]]],
        names: List[Literal["column2", "column1"]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["A", "B"], Literal["Z", "X"]]]):
        """
        usage.koalas: 3
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["y"], Literal["c"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["x", "y", "z"], Literal["ba", "cb", "db"]]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["x", "z"], Literal["ba", "db"]]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["y"], Literal["cb"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["x", "Y"], Literal["key", "A"]]]
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["x", "Y"], Literal["key", "B"]]]
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[Literal["x_left", "Y", "x_right"], Literal["key", "A", "B"]]
        ],
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["Y"], Literal["B"]]]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["x", "Y"], Literal["key", "A", "B"]]]
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["a", "b"], Literal["lkey", "value", "x"]]]
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["a", "c"], Literal["rkey", "value", "y"]]]
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[Literal["a", "b", "c"], Literal["lkey", "value", "x", "rkey", "y"]]
        ],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["a", "b"], Literal["value", "x"]]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["a", "c"], Literal["value", "y"]]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["a", "b", "c"], Literal["value", "x", "y"]]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[Literal["a_x", "b", "a_y", "c"], Literal["value", "x", "y"]]
        ],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[
                Literal["a", "c", "e", "", "i"],
                Literal["", "g"],
                Literal["", "d", "f"],
                Literal["b", "", "h"],
            ]
        ],
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["d"], Literal[""]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["", "g"], Literal["f", ""], Literal[""]]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[
                Literal["a", "e"], Literal["", "g"], Literal["", "f"], Literal["b", ""]
            ]
        ],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[
                Literal["e", "a"], Literal["", "g"], Literal["f", ""], Literal["", "b"]
            ]
        ],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["e"], Literal["g"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["i"], Literal[""]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["X", "Y"], Literal["A", "B"]]],
        names: List[Literal["2", "1"]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["b"], Literal["2", "3", "4", "6", "8"]]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["b", "e"], Literal["2", "3", "4", "6", "8"]]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["b", "d"], Literal["2", "3", "4", "6", "8"]]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[Literal["x", "y", "z", "w"], Literal["a", "b", "e", "c", "d"]]
        ],
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[Literal["x"], Literal["b"], Literal["2", "3", "4", "6", "8"]]
        ],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[
                Literal["x", "y"], Literal["b", "e"], Literal["2", "3", "4", "6", "8"]
            ]
        ],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[
                Literal["w", "x"], Literal["d", "b"], Literal["2", "3", "4", "6", "8"]
            ]
        ],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["A", "B", "C"], Literal["Z", "X", "C"]]]
    ):
        """
        usage.koalas: 4
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["x", "y"], Literal["col1", "col2"]]]
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["X"], Literal["numbers"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["X", "Y"], Literal["numbers", "2", "3"]]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["A", "B"], Literal["0", "1"]]]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["x", "y"], Literal["a", "b", "c", "d"]]]
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["X", "Y"], Literal["a", "b", "c", "d"]]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[
                Literal["class", "name", "speed", "species"], Literal["", "max", "type"]
            ]
        ],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[
                Literal["x", "y", "speed", "species"],
                Literal["class", "name", "max", "type"],
            ]
        ],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["A"], Literal["Z"]]]):
        """
        usage.koalas: 3
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["weight"], Literal["kg", "pounds"]]],
        names: List[Literal["y", "x"]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["B", "C"], Literal["X", "C"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["C", "B"], Literal["C", "X"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["rg1", "rg2"], Literal["x", "y", "z"]]]
    ):
        """
        usage.koalas: 3
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["cg1", "cg2", "cg3"], Literal["a", "b", "c", "d"]]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["A", "B", "C"], Literal["Z", "X"]]]
    ):
        """
        usage.koalas: 3
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["B", "C"], Literal["X", "Z"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["0", "1", "2"], Literal["x", "y", "z"]]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["X", "Y"], Literal["B", "C"]]]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["X"], Literal["B"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["Y"], Literal["B", "C"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["mammal"], Literal["dog"], Literal["walks"]]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["a"], Literal["x", "y"]]]):
        """
        usage.koalas: 6
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["B", "C"], Literal["min", "max", "sum"]]]
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["B", "C"], Literal["sum"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["A", "B", "C"], Literal["sum"]]]
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["A", "B", "C"], Literal["", "min", "max", "sum"]]],
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["A", "B", "C"], Literal["", "sum"]]]
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[Literal["X", "Y"], Literal["B", "C"], Literal["min", "max", "sum"]]
        ],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["height", "weight"], Literal["min", "max"]]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[Literal["X", "Y"], Literal["B", "C"], Literal["min", "max"]]
        ],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["y", "x"], Literal["A", "B", "group"]]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["X", "Y"], Literal["A", "B"]]]):
        """
        usage.koalas: 3
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[Literal["__groupkey_0__", "x", "y"], Literal["", "a", "b", "c"]]
        ],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[
                Literal["__groupkey_0__", "__groupkey_1__", "x", "y"],
                Literal["", "a", "b", "c"],
            ]
        ],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["X", "Y", "Z"], Literal["A", "B", "C", "D"]]]
    ):
        """
        usage.koalas: 6
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["X", "Y", "Z"], Literal["B", "C", "D"]]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["x", "y"], Literal["a", "c"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[Literal["b", "c"], Literal["count", "mean", "std", "min", "max"]]
        ],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["b", "c"], Literal["25%", "50%", "75%"]]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["x", "y"], Literal["b", "c"]]]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["__groupkey_0__", "x", "y"], Literal["", "a", "c"]]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[Literal["__groupkey_0__", "__groupkey_1__", "y"], Literal["", "c"]]
        ],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[int, int]],
        sortorder: None,
        names: List[Literal["level2", "level1"]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["a", "b"], Literal["x", "y"]]]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["a", "d"], Literal["x", "y"]]]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["a", "b", "c"], Literal["x", "y", "z"], int]]
    ):
        """
        usage.koalas: 6
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["a", "b", "c"], Literal["x", "y", "z"], int]],
        names: List[Literal["z", "y", "x"]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["a", "b", "c"], Literal["x", "y", "z"], int]],
        names: List[Literal["r", "q", "p"]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["a"], Literal["a", "b", "c"]]],
        sortorder: None,
        names: None,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["a", "b", "c"], Literal["x", "y", "z"], int]],
        names: List[Literal["world", "koalas", "hello"]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["a", "b", "k"], Literal["x", "z"], int]],
        names: List[Literal["world", "koalas", "hello"]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: set, sortorder: None, names: None):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: Dict[Tuple[Literal["a"], Literal["x"], int], List[int]],
        sortorder: None,
        names: None,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[int, int]]):
        """
        usage.koalas: 4
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[int, int]], names: List[Literal["level2", "level1"]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["w", "x", "y", "z"], Literal["a", "b", "c", "d"]]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["w", "x", "y", "z"], Literal["d", "c", "b", "a"]]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["z", "y", "x", "w"], Literal["a", "b", "c", "d"]]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["z", "y", "x", "w"], Literal["d", "c", "b", "a"]]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["z", "x", "y", "w"], Literal["a", "b", "c", "d"]]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["z", "y", "x", "w"], Literal["a", "c", "b", "d"]]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["a", "b", "c", "d", "e"], int]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["e", "d", "c", "b", "a"], int]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[int, Literal["a", "b", "c", "d", "e"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[int, Literal["e", "d", "c", "b", "a"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[int, Literal["e", "c", "b", "d", "a"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Union[None, int], int]]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[int, Union[None, int]]]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[int, Union[int, None]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Union[None, int], Union[None, int]]]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[int, None]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[None, Literal["e", "c", "b", "d", "a"]]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[None, None]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["x", "y", "z"], Literal["d", "c", "b", "a"]]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["x", "y", "z"], Literal["d", "b", "c", "a"]]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[Literal["x", "y", "z"], Union[Literal["d", "c", "a"], None]]
        ],
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["x", "y", "z"], Union[Literal["d", "a"], None]]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[Union[Literal["x", "y"], None], Literal["d", "c", "b", "a"]]
        ],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[Union[Literal["x", "y"], None], Literal["d", "b", "c", "a"]]
        ],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[
                Literal["x", "y", "z"],
                Literal["d", "c", "a"],
                Literal["o", "p", "q", "r"],
            ]
        ],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[
                Literal["x", "y", "z"],
                Literal["d", "c", "a"],
                Literal["o", "q", "p", "r"],
            ]
        ],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[
                Literal["x", "y", "z"],
                Literal["d", "c", "a"],
                Union[Literal["o", "p", "r"], None],
            ]
        ],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[
                Literal["x", "y", "z"],
                Literal["d", "c", "a"],
                Union[Literal["o", "r"], None],
            ]
        ],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Union[int, None], int]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Union[int, None], Union[int, None]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[
                Literal["x", "y", "z"],
                Literal["d", "c", "a"],
                Union[Literal["o", "q", "r"], None],
            ]
        ],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["a", "b"], Literal["x", "y"], int]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["a", "b", "c"], Literal["x", "y", "z"]]],
        names: List[Literal["level2", "level1"]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["a", "b"], Literal["x", "y"], int]],
        names: List[Literal["level3", "level2", "level1"]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[int, Literal["red", "blue"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[int, Literal["red", "blue"]]],
        sortorder: None,
        names: None,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["a", "b", "c"], Literal["d", "e", "f"]]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["x"], Literal["a", "b", "c"]]],
        names: List[Literal["Koalas", "hello"]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["x"], Literal["a", "b"]]]):
        """
        usage.koalas: 7
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["x"], Literal["a", "b", "c", "d"]]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["x"], Literal["a", "b"]]],
        sortorder: None,
        names: None,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[int, int]], sortorder: None, names: None
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["x"], Literal["b", "a"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[Literal["x", "y"], Literal["max_speed", "shield", "min_speed"]]
        ],
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[
                Literal["x", "y", "z"], Literal["max_speed", "shield", "min_speed", ""]
            ]
        ],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["baz"], Literal["two"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["bar"], Literal["one"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["bar"], Literal["one", "two"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["bar"], Literal["two", "one"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["bar", "baz"], Literal["two", "one"]]]
    ):
        """
        usage.koalas: 5
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["bar", "baz"], Literal["one", "two"]]]
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["bar"], Literal["two"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["x", "y", "z"], Literal["a", "b", "c", "d", "e"]]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["x", "y", "z"], Literal["a", "b", "c", "e"]]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["z", "y", "x"], Literal["e", "d", "c", "b", "a"]]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["x", "y"], Literal["cobra", "viper", "sidewinder"]]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["x"], Literal["b"]]]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["X"], Literal["C", "D"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["this", "that"], Literal["A", "C"]]]
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["this", "that"], Literal["A", "B", "C"]]]
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["this", "that"], Literal["A", "C", "D"]]]
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["this", "that"], Literal["X"], Literal["A", "C"]]],
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["X"], Literal["A", "C"]]]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[Literal["this", "that"], Literal["X"], Literal["A", "B", "C"]]
        ],
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["X"], Literal["A", "B", "C"]]]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[Literal["this", "that"], Literal["X"], Literal["A", "C", "D"]]
        ],
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["X"], Literal["A", "C", "D"]]]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[Literal["this", "that"], Literal["X"], Literal["A", "B", "C", "D"]]
        ],
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["X"], Literal["A", "B", "C", "D"]]]
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["(X, A)"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["(X, B)"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["this", "that"], Literal["C", "A", "B"]]]
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["X", "Y", "index"], Literal["A", "B", "C", ""]]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["X", "Y"], Literal["A", "C"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["this"], Literal["a", "b"]]]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["this"], Literal["x"], Literal["a", "b"]]]
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["this", "that"], Literal["b", "a", "c"]]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["this", "that"], Literal["a", "b", "c"]]]
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[Literal["this", "that"], Literal["x", "y"], Literal["b", "a", "c"]]
        ],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[Literal["this", "that"], Literal["x", "y"], Literal["a", "b", "c"]]
        ],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["a", "b"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["that"], Literal["a", "b"]]]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["that", "this"], Literal["b", "a", "c"]]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["that", "this"], Literal["c", "a", "d", "b"]]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["this", "that"], Literal["a", "b", "c", "d"]]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["a", "b"], Literal[""]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[
                Literal["that", "this"],
                Literal["y", "z", "x"],
                Literal["c", "d", "a", "b"],
            ]
        ],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[
                Literal["this", "that"],
                Literal["x", "y", "z"],
                Literal["a", "b", "c", "d"],
            ]
        ],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["x", "y", "z"], Literal["a", "b", "c", "d"]]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["(x, a)", "(x, b)"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["that", "this"], Literal["c", "d", "a", "b"]]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["b", "c"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["that", "this"], Literal["e", "b", "f", "a"]]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["this", "that"], Literal["a", "b", "e", "f"]]],
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["that", "this"], Literal["b", "a", "c", "e", "f"]]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["this", "that"], Literal["a", "b", "e", "f", "c"]]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["a"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["that", "this"], Literal["a", "b"]]]
    ):
        """
        usage.koalas: 3
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["b"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["that", "this"], Literal["c", "a", "b"]]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["a"], Literal[""]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[Literal["that", "this"], Literal["y", "x"], Literal["c", "a", "b"]]
        ],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["that", "this"], Literal["NEW", "a", "Koalas"]]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["this", "that"], Literal["a", "Koalas", "NEW"]]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["c"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["that", "this"], Literal["d", "a", "b"]]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["this", "that"], Literal["a", "b", "d"]]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["z"], Literal["e", "f"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[
                Literal["this", "that"], Literal["x", "z"], Literal["a", "b", "e", "f"]
            ]
        ],
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["x", "z"], Literal["a", "b", "e", "f"]]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["max_speed"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["A"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["that", "this"], Literal["__temp_col__", "A", "B"]]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["this", "that"], Literal["A", "B", "__temp_col__"]]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["that", "this"], Literal["__temp_col__", "A"]]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["this", "that"], Literal["A", "__temp_col__"]]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[str, Literal[""]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["that", "this"], str, Literal["", "A", "B"]]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["this", "that"], str, Literal["A", "B", ""]]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["this", "that"], Literal["c", "e"]]]
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["that"], Literal["c"]]]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["that", "this"], Literal["x", "c"]]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["this", "that"], Literal["c", "x"]]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["c", "e"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["that", "this"], Literal["x", "c", "y", "e"]]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["this", "that"], Literal["c", "e", "x", "y"]]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["e"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["that", "this"], Literal["e", "c"]]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["that", "this"], Literal["c"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["0"], Literal[""]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[Literal["that", "this"], Literal["c", "a"], Literal["", "x", "y"]]
        ],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[Literal["this", "that"], Literal["a", "c"], Literal["x", "y", ""]]
        ],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["1"], Literal[""]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[
                Literal["that", "this"], Literal["d", "a", "c"], Literal["x", "y", ""]
            ]
        ],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[
                Literal["this", "that"], Literal["a", "c", "d"], Literal["x", "y", ""]
            ]
        ],
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["(1, 2)"], Literal[""]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[
                Literal["that", "this"], Literal["d", "a", "c"], Literal["y", "x", ""]
            ]
        ],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["(1, 2, 3)"], Literal[""]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[
                Literal["that", "this"],
                Literal["e", "a", "c", "d"],
                Literal["", "x", "y"],
            ]
        ],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[
                Literal["this", "that"],
                Literal["a", "c", "d", "e"],
                Literal["x", "y", ""],
            ]
        ],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["1", "2"], Literal[""]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[
                Literal["that", "this"],
                Literal["f", "a", "c", "d", "e"],
                Literal["x", "y", ""],
            ]
        ],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[
                Literal["this", "that"],
                Literal["a", "c", "d", "e", "f"],
                Literal["x", "y", ""],
            ]
        ],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["a", "c", "d", "e", "f"], Literal["x", "y", ""]]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["this"], Literal["id"]]]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["x"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["rep"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["that", "this"], Literal["__temp_repeats__", "a"]]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["this", "that"], Literal["a", "__temp_repeats__"]]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[Literal["this", "that"], Literal["C", "B", "__tmp_groupkey_0__"]]
        ],
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[Literal["this", "that"], Literal["C", "B", "__tmp_groupkey_1__"]]
        ],
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[
                Literal["this", "that"],
                Literal["C", "B", "__tmp_groupkey_0__", "__tmp_groupkey_1__"],
            ]
        ],
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["Y", "X"], Literal["C", "B"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["X"], Literal["A"]]]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[
                Literal["this", "that"],
                Literal["Y", "X", ""],
                Literal["C", "B", "__tmp_groupkey_0__"],
            ]
        ],
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[Literal["this", "that"], Literal["a", "b", "c", "__tmp_groupkey_0__"]]
        ],
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[Literal["this", "that"], Literal["a", "b", "c", "__tmp_groupkey_1__"]]
        ],
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[Literal["this", "that"], Literal["A", "__tmp_groupkey_0__"]]
        ],
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[
                Literal["this", "that"],
                Literal["A", "B", "C", "D", "__tmp_groupkey_0__"],
            ]
        ],
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[Literal["this", "that"], Literal["c", "d", "__tmp_groupkey_0__"]]
        ],
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[
                Literal["this", "that"],
                Literal["y", "z", ""],
                Literal["c", "d", "__tmp_groupkey_0__"],
            ]
        ],
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[Literal["this", "that"], Literal["B", "__tmp_groupkey_0__"]]
        ],
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[Literal["this", "that"], Literal["0", "__tmp_groupkey_0__"]]
        ],
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[Literal["this", "that"], Literal["a", "b", "__tmp_groupkey_0__"]]
        ],
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[Literal["this", "that"], Literal["a", "__tmp_groupkey_0__"]]
        ],
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["A", "B"], Literal["X", "Y"]]]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[Literal["x", "y"], Literal["a", "b", "c"], Literal["q", "w", "e"]]
        ],
        names: List[Literal["level_3", "level_2", "level_1"]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["one", "two", "three"], Literal["x", "y", "z"]]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["a", "b", "c"], Literal["1", "2"]]]
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[Literal["y"], Literal["z"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["a"], Literal["b"], Literal["c"]]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[Literal["one", "two"], Literal["a", "b"], Literal["z", "x", "c", "v"]]
        ],
        names: List[Literal["C", "B", "A"]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["x", "y"], Literal["b", "c", "a"]]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Tuple[Literal["x", "y"], Union[None, Literal["c", "a"]]]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[Union[Tuple[Literal["y", "x"], Literal["c", "a"]], None]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[int, Literal["mean", "std"]]],
        names: List[Union[None, Literal["factor_quantile"]]],
    ):
        """
        usage.alphalens: 4
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls, /, tuples: List[List[int]], names: List[Literal["level1", "level0"]]
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: Tuple[
            Tuple[Literal["b"], int],
            Tuple[Literal["b"], int],
            Tuple[Literal["a"], int],
            Tuple[Literal["a"], int],
        ],
        names: List[Literal["two", "one"]],
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: Tuple[
            Tuple[Literal["a"], int],
            Tuple[Literal["a"], int],
            Tuple[Literal["b"], int],
            Tuple[Literal["b"], int],
        ],
        names: List[Literal["two", "one"]],
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[numpy.str_, numpy.str_]],
        names: List[Literal["exog", "endog"]],
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["General Motors"], float]],
        names: List[Literal["year", "firms"]],
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[float, float, float]],
        names: List[Literal["TVnews", "income", "educ"]],
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(cls, /, tuples: List[Tuple[float, float, float]], names: None):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["a"], numpy.int64]],
        names: List[Literal["name2", "name1"]],
    ):
        """
        usage.modin: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[Literal["a"], Literal["col1", "col2", "col3", "col4", "col5"]]
        ],
        names: List[Literal["name2", "name1"]],
    ):
        """
        usage.modin: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[
            Tuple[Literal["a"], Literal["col1", "col2", "col3", "col6", "col7"]]
        ],
        names: List[Literal["name2", "name1"]],
    ):
        """
        usage.modin: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[int, Literal["c", "a", "b"], Literal["Red", "Green"]]],
        names: List[Literal["Color", "Letter", "Number"]],
    ):
        """
        usage.modin: 4
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["foo1", "foo2"], Literal["bar1", "bar2"]]],
        names: List[Literal["bar", "foo"]],
    ):
        """
        usage.modin: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[Literal["fizz1", "fizz2"], Literal["buzz1", "buzz2"]]],
        names: List[Literal["buzz", "fizz"]],
    ):
        """
        usage.modin: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[int, int]],
        names: List[Union[None, Literal["test_index_name"]]],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: List[Tuple[int, int]],
        names: pandas.core.indexes.frozen.FrozenList,
    ):
        """
        usage.geopandas: 2
        """
        ...

    @classmethod
    def from_tuples(
        cls,
        /,
        tuples: Union[
            List[Union[List[int], None, tuple]],
            set,
            zip,
            Dict[Tuple[Literal["a"], Literal["x"], int], List[int]],
            Tuple[
                Tuple[Literal["a", "b"], int],
                Tuple[Literal["a", "b"], int],
                Tuple[Literal["b", "a"], int],
                Tuple[Literal["b", "a"], int],
            ],
        ],
        sortorder: None = ...,
        names: Union[
            List[Union[str, None]],
            pandas.core.indexes.frozen.FrozenList,
            None,
            Tuple[Literal["number"], Literal["color"]],
        ] = ...,
    ):
        """
        usage.alphalens: 4
        usage.geopandas: 3
        usage.koalas: 568
        usage.modin: 9
        usage.statsmodels: 4
        usage.xarray: 3
        """
        ...

    # usage.dask: 1
    __class__: object

    # usage.koalas: 1
    _values: object

    # usage.dask: 2
    # usage.xarray: 6
    codes: object

    # usage.dask: 2
    # usage.koalas: 2
    # usage.xarray: 3
    dtype: object

    # usage.xarray: 1
    is_lexsorted: object

    # usage.xarray: 2
    is_monotonic: object

    # usage.xarray: 3
    is_unique: object

    # usage.alphalens: 9
    # usage.dask: 9
    # usage.xarray: 18
    levels: object

    # usage.koalas: 1
    # usage.statsmodels: 1
    levshape: object

    # usage.alphalens: 1
    # usage.dask: 4
    # usage.modin: 2
    # usage.xarray: 3
    name: Union[Literal["z", "factor_quantile"], None]

    # usage.dask: 11
    # usage.geopandas: 6
    # usage.koalas: 106
    # usage.statsmodels: 13
    # usage.xarray: 23
    names: Union[
        List[Union[Tuple[str, str], str, None]], pandas.core.indexes.frozen.FrozenList
    ]

    # usage.dask: 3
    # usage.koalas: 1
    # usage.xarray: 4
    nlevels: object

    # usage.koalas: 1
    # usage.xarray: 1
    rename: object

    # usage.xarray: 1
    shape: object

    # usage.xarray: 2
    size: object

    # usage.pyjanitor: 2
    # usage.xarray: 6
    values: object

    @overload
    def __contains__(self, _0: Tuple[Literal["a"], Literal["foo"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __contains__(self, _0: Tuple[Literal["x"], Literal["a"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["divisions"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["columns"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["_meta"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["dtype"], /):
        """
        usage.dask: 1
        """
        ...

    def __contains__(
        self,
        _0: Union[
            Literal["dtype", "_meta", "columns", "divisions"],
            Tuple[Literal["a", "x"], Literal["foo", "a"]],
        ],
        /,
    ):
        """
        usage.dask: 4
        usage.koalas: 2
        """
        ...

    def __eq__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 4
        """
        ...

    @overload
    def __getitem__(self, _0: int, /):
        """
        usage.dask: 2
        usage.koalas: 1
        usage.xarray: 2
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, int, None], /):
        """
        usage.koalas: 2
        usage.xarray: 6
        """
        ...

    @overload
    def __getitem__(self, _0: slice[int, None, int], /):
        """
        usage.xarray: 3
        """
        ...

    @overload
    def __getitem__(self, _0: numpy.ndarray, /):
        """
        usage.xarray: 3
        """
        ...

    @overload
    def __getitem__(self, _0: slice[int, int, int], /):
        """
        usage.dask: 1
        usage.xarray: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, None, None], /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, None, None], /):
        """
        usage.xarray: 1
        """
        ...

    def __getitem__(
        self,
        _0: Union[
            slice[Union[int, None], Union[None, int], Union[int, None]],
            int,
            numpy.ndarray,
        ],
        /,
    ):
        """
        usage.dask: 3
        usage.koalas: 3
        usage.xarray: 17
        """
        ...

    def __iter__(self, /):
        """
        usage.dask: 1
        usage.koalas: 1
        usage.statsmodels: 1
        """
        ...

    def copy(self, /, deep: bool):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def drop(self, /, codes: List[Literal["y", "x"]], level: int):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def drop(self, /, codes: List[Literal["y", "x"]], level: Literal["level2"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def drop(self, /, codes: List[Literal["y", "x"]], level: Literal["lv2"]):
        """
        usage.koalas: 1
        """
        ...

    def drop(
        self,
        /,
        codes: List[Literal["y", "x"]],
        level: Union[Literal["lv2", "level2"], int],
    ):
        """
        usage.koalas: 3
        """
        ...

    def equals(self, /, other: pandas.core.indexes.multi.MultiIndex):
        """
        usage.xarray: 2
        """
        ...

    def get_indexer(self, /, target: numpy.ndarray, method: None, tolerance: None):
        """
        usage.xarray: 2
        """
        ...

    def get_level_values(self, /, level: int):
        """
        usage.dask: 4
        """
        ...

    def get_loc(self, /, key: Literal["2001-01"]):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_loc_level(self, /, key: Tuple[Literal["a"], int], level: List[int]):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_loc_level(self, /, key: Tuple[Literal["a"]], level: List[int]):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_loc_level(self, /, key: Literal["a"], level: int):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_loc_level(
        self,
        /,
        key: Tuple[Literal["a"], int],
        level: Tuple[Literal["one"], Literal["two"]],
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_loc_level(self, /, key: Tuple[Literal["a"]], level: Tuple[Literal["one"]]):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_loc_level(self, /, key: Tuple[int], level: Tuple[Literal["x"]]):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_loc_level(self, /, key: Tuple[Literal["a"]], level: Tuple[Literal["y"]]):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_loc_level(
        self, /, key: Tuple[Literal["a"]], level: Tuple[Literal["variable"]]
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_loc_level(
        self, /, key: Tuple[Literal["b"]], level: Tuple[Literal["variable"]]
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_loc_level(self, /, key: Tuple[int, int], level: int):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_loc_level(self, /, key: int, level: int):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_loc_level(
        self,
        /,
        key: Tuple[Literal["a"], int],
        level: Tuple[Literal["one"], Literal["three"]],
    ):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def get_loc_level(self, /, key: Literal["American Steel"], level: int):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def get_loc_level(self, /, key: Literal["Atlantic Refining"], level: int):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def get_loc_level(self, /, key: Literal["Chrysler"], level: int):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def get_loc_level(self, /, key: Literal["Diamond Match"], level: int):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def get_loc_level(self, /, key: Literal["General Electric"], level: int):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def get_loc_level(self, /, key: Literal["General Motors"], level: int):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def get_loc_level(self, /, key: Literal["Goodyear"], level: int):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def get_loc_level(self, /, key: Literal["IBM"], level: int):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def get_loc_level(self, /, key: Literal["US Steel"], level: int):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def get_loc_level(self, /, key: Literal["Union Oil"], level: int):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def get_loc_level(self, /, key: Literal["Westinghouse"], level: int):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def get_loc_level(self, /, key: numpy.float64, level: int):
        """
        usage.statsmodels: 1
        """
        ...

    def get_loc_level(
        self,
        /,
        key: Union[str, numpy.float64, int, Tuple[Union[Literal["a", "b"], int], ...]],
        level: Union[int, List[int], Tuple[str, ...]],
    ):
        """
        usage.statsmodels: 12
        usage.xarray: 12
        """
        ...

    @overload
    def set_levels(self, /, levels: List[Literal["d", "c"]], level: int, inplace: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def set_levels(self, /, levels: List[Literal["c", "b"]], level: int, inplace: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def set_levels(self, /, levels: List[Literal["b"]], level: int, inplace: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def set_levels(self, /, levels: List[Literal["d"]], level: int, inplace: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def set_levels(self, /, levels: List[Literal["a"]], level: int, inplace: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def set_levels(
        self, /, levels: List[Literal["d", "b", "c"]], level: int, inplace: bool
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def set_levels(
        self, /, levels: List[Literal["d", "a", "b", "c"]], level: int, inplace: bool
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def set_levels(
        self, /, levels: List[Literal["c", "b", "a"]], level: int, inplace: bool
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def set_levels(self, /, levels: List[float], level: int, inplace: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def set_levels(
        self, /, levels: List[Literal["3", "2", "1"]], level: int, inplace: bool
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def set_levels(
        self, /, levels: List[Literal["b", "a", ""]], level: int, inplace: bool
    ):
        """
        usage.dask: 1
        """
        ...

    def set_levels(self, /, levels: List[Union[str, float]], level: int, inplace: bool):
        """
        usage.dask: 11
        """
        ...

    @overload
    def set_names(self, /, names: List[Literal["col", "num"]], inplace: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_names(self, /, names: List[Literal["names", "new", "set"]], inplace: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_names(self, /, names: Literal["first"], level: int):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_names(self, /, names: Literal["second"], level: int):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_names(self, /, names: Literal["third"], level: int):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_names(self, /, names: Literal["first"], level: int, inplace: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_names(self, /, names: Literal["second"], level: int, inplace: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_names(self, /, names: Literal["third"], level: int, inplace: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_names(self, /, names: List[Literal["asset", "date"]], inplace: bool):
        """
        usage.alphalens: 1
        """
        ...

    @overload
    def set_names(self, /, names: List[Literal["level1", "level0"]]):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def set_names(self, /, names: pandas.core.indexes.frozen.FrozenList, inplace: bool):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def set_names(self, /, names: List[Literal["year", "firms"]], inplace: bool):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def set_names(
        self, /, names: List[Literal["group2", "group1", "group0"]], inplace: bool
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def set_names(self, /, names: List[Literal["b", "a"]], inplace: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def set_names(self, /, names: List[Literal["c", "b", "a"]], inplace: bool):
        """
        usage.dask: 1
        """
        ...

    def set_names(
        self,
        /,
        names: Union[
            List[str],
            Literal["third", "second", "first"],
            pandas.core.indexes.frozen.FrozenList,
        ],
        level: int = ...,
        inplace: bool = ...,
    ):
        """
        usage.alphalens: 1
        usage.dask: 2
        usage.koalas: 8
        usage.statsmodels: 3
        usage.xarray: 1
        """
        ...

    @overload
    def slice_locs(self, /, start: Literal["B"], end: None):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def slice_locs(self, /, start: None, end: Literal["A"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def slice_locs(self, /, start: Literal["B"], end: Literal["C"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def slice_locs(self, /, start: Literal["bar"], end: Literal["bar"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def slice_locs(
        self, /, start: Literal["bar"], end: Tuple[Literal["baz"], Literal["one"]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def slice_locs(
        self,
        /,
        start: Tuple[Literal["bar"], Literal["two"]],
        end: Tuple[Literal["baz"], Literal["one"]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def slice_locs(
        self, /, start: Tuple[Literal["bar"], Literal["two"]], end: Literal["bar"]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def slice_locs(self, /, start: Literal["a"], end: Literal["bax"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def slice_locs(
        self,
        /,
        start: Tuple[Literal["bar"], Literal["x"]],
        end: Tuple[Literal["baz"], Literal["a"]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def slice_locs(self, /, start: Literal["bar"], end: Literal["baz"]):
        """
        usage.koalas: 1
        """
        ...

    def slice_locs(
        self,
        /,
        start: Union[
            Literal["bar", "a", "B"], None, Tuple[Literal["bar"], Literal["two", "x"]]
        ],
        end: Union[
            Literal["baz", "bax", "bar", "C", "A"],
            None,
            Tuple[Literal["baz"], Literal["one", "a"]],
        ],
    ):
        """
        usage.koalas: 10
        """
        ...

    def sort_values(self, /, ascending: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def to_frame(self, /, index: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def to_frame(self, /, name: List[Literal["y", "x"]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def to_frame(self, /, index: bool, name: List[Literal["y", "x"]]):
        """
        usage.koalas: 1
        """
        ...

    def to_frame(self, /, index: bool = ..., name: List[Literal["y", "x"]] = ...):
        """
        usage.koalas: 3
        """
        ...

    def to_series(self, /, name: Literal["a"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def union(self, /, other: pandas.core.indexes.multi.MultiIndex, sort: bool):
        """
        usage.koalas: 4
        """
        ...

    @overload
    def union(
        self,
        /,
        other: List[Tuple[Literal["x"], Literal["a", "b", "c", "d"]]],
        sort: bool,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def union(self, /, other: List[Tuple[Literal["x"], Literal["a", "b"]]], sort: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def union(self, /, other: List[Tuple[int, int]], sort: bool):
        """
        usage.koalas: 2
        """
        ...

    def union(
        self,
        /,
        other: Union[
            List[
                Tuple[Union[int, Literal["x"]], Union[int, Literal["a", "b", "c", "d"]]]
            ],
            pandas.core.indexes.multi.MultiIndex,
        ],
        sort: bool,
    ):
        """
        usage.koalas: 8
        """
        ...

    @overload
    def value_counts(self, /, normalize: bool):
        """
        usage.koalas: 3
        """
        ...

    @overload
    def value_counts(self, /, ascending: bool):
        """
        usage.koalas: 3
        """
        ...

    @overload
    def value_counts(self, /, normalize: bool, dropna: bool):
        """
        usage.koalas: 3
        """
        ...

    @overload
    def value_counts(self, /, ascending: bool, dropna: bool):
        """
        usage.koalas: 3
        """
        ...

    def value_counts(
        self, /, ascending: bool = ..., normalize: bool = ..., dropna: bool = ...
    ):
        """
        usage.koalas: 12
        """
        ...
