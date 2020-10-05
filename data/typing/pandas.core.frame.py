from typing import *


class DataFrame:

    # usage.dask: 4
    __module__: ClassVar[object]

    # usage.dask: 4
    __name__: ClassVar[object]

    # usage.dask: 6
    # usage.sklearn: 39
    shape: ClassVar[object]

    # usage.sklearn: 2
    sparse: ClassVar[object]

    @overload
    @classmethod
    def __ne__(cls, _0: Type[pandas.core.frame.DataFrame], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    @classmethod
    def __ne__(cls, _0: Type[dask.dataframe.core.DataFrame], /):
        """
        usage.dask: 1
        """
        ...

    @classmethod
    def __ne__(cls, _0: type, /):
        """
        usage.dask: 3
        """
        ...

    @classmethod
    def __rmod__(cls, _0: Union[numpy.timedelta64, str], /):
        """
        usage.pandas: 1
        usage.sklearn: 1
        """
        ...

    @classmethod
    def from_dict(
        cls,
        /,
        data: List[Dict[Literal["y", "x"], Union[Literal["a", "b", "c", "d"], int]]],
    ):
        """
        usage.dask: 1
        """
        ...

    # usage.dask: 40
    A: object

    # usage.dask: 3
    A_a: object

    # usage.dask: 15
    B: object

    # usage.dask: 4
    C: object

    # usage.dask: 2
    Date: pandas.core.series.Series

    # usage.dask: 1
    F: object

    # usage.dask: 1
    Name: object

    # usage.dask: 5
    # usage.xarray: 1
    T: object

    # usage.dask: 2
    X: object

    # usage.dask: 7
    __class__: object

    # usage.dask: 2
    _constructor: object

    # usage.dask: 2
    _constructor_sliced: object

    # usage.dask: 1
    _data: object

    # usage.dask: 2
    _partitions: object

    # usage.dask: 114
    a: pandas.core.series.Series

    # usage.dask: 1
    amount: object

    # usage.dask: 63
    b: object

    # usage.dask: 1
    c: object

    # usage.dask: 1
    col1: object

    # usage.dask: 1
    col2: object

    # usage.dask: 142
    # usage.sklearn: 19
    # usage.xarray: 9
    columns: object

    # usage.dask: 4
    d: object

    # usage.dask: 3
    div: object

    # usage.dask: 3
    divide: object

    # usage.dask: 2
    dt_col: object

    # usage.dask: 25
    # usage.sklearn: 24
    dtypes: object

    # usage.dask: 2
    e: object

    # usage.dask: 4
    empty: object

    # usage.dask: 3
    f: object

    # usage.sklearn: 1
    fit: object

    # usage.dask: 2
    fruit: object

    # usage.dask: 2
    i32: object

    # usage.dask: 2
    id: object

    # usage.dask: 46
    # usage.sklearn: 14
    # usage.xarray: 2
    iloc: object

    # usage.dask: 197
    # usage.sklearn: 3
    # usage.xarray: 12
    index: object

    # usage.dask: 71
    # usage.sklearn: 1
    # usage.xarray: 3
    loc: object

    # usage.dask: 3
    # usage.sklearn: 4
    ndim: object

    # usage.dask: 2
    path: object

    # usage.dask: 3
    rdiv: object

    # usage.dask: 2
    # usage.sklearn: 2
    size: object

    # usage.dask: 12
    str_col: object

    # usage.dask: 4
    string_col: object

    # usage.dask: 1
    tz: object

    # usage.dask: 2
    value: object

    # usage.dask: 33
    # usage.sklearn: 1
    # usage.xarray: 7
    values: object

    # usage.dask: 7
    w: pandas.core.series.Series

    # usage.dask: 80
    x: pandas.core.series.Series

    # usage.dask: 37
    y: pandas.core.series.Series

    # usage.dask: 4
    z: object

    @overload
    def __add__(self, _0: Union[numpy.ndarray, numpy.timedelta64, numpy.datetime64], /):
        """
        usage.pandas: 37
        """
        ...

    @overload
    def __add__(self, _0: dask.dataframe.core.Scalar, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __add__(self, _0: int, /):
        """
        usage.dask: 17
        """
        ...

    @overload
    def __add__(self, _0: float, /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __add__(self, _0: numpy.ndarray, /):
        """
        usage.dask: 3
        """
        ...

    @overload
    def __add__(self, _0: pandas.core.frame.DataFrame, /):
        """
        usage.dask: 1
        """
        ...

    def __add__(self, _0: object, /):
        """
        usage.dask: 24
        usage.pandas: 37
        """
        ...

    def __array_wrap__(self, /, result: numpy.ndarray):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __eq__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 6
        """
        ...

    @overload
    def __eq__(self, _0: pandas.core.frame.DataFrame, /):
        """
        usage.dask: 8
        """
        ...

    @overload
    def __eq__(self, _0: int, /):
        """
        usage.dask: 1
        """
        ...

    def __eq__(self, _0: Union[pandas.core.frame.DataFrame, int, numpy.ndarray], /):
        """
        usage.dask: 9
        usage.pandas: 6
        """
        ...

    def __floordiv__(self, _0: numpy.timedelta64, /):
        """
        usage.pandas: 3
        """
        ...

    @overload
    def __ge__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 1
        """
        ...

    @overload
    def __ge__(self, _0: int, /):
        """
        usage.dask: 2
        """
        ...

    def __ge__(self, _0: Union[int, numpy.ndarray], /):
        """
        usage.dask: 2
        usage.pandas: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["foo"], /):
        """
        usage.xarray: 3
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["foo", "C"]], /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def __getitem__(self, _0: int, /):
        """
        usage.dask: 11
        usage.sklearn: 1
        usage.xarray: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["x"], /):
        """
        usage.dask: 13
        usage.xarray: 3
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["a"]], /):
        """
        usage.dask: 4
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["amount"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["id"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["id", "name"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["bb"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["aa"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["path"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["filename"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: pandas.core.indexes.base.Index, /):
        """
        usage.dask: 10
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["name"], /):
        """
        usage.dask: 1
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["fruit"], /):
        """
        usage.dask: 3
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["A"], /):
        """
        usage.dask: 27
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["B"], /):
        """
        usage.dask: 7
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["b"], /):
        """
        usage.dask: 23
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["a"], /):
        """
        usage.dask: 40
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["names"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["numbers"], /):
        """
        usage.dask: 3
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["more_numbers"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["integers"], /):
        """
        usage.dask: 3
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["Date"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["date_time"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["C"], /):
        """
        usage.dask: 2
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["A_B"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["B_"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["date"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["idx"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["dt_col"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["str_col"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["string_col"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["int_col"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["y"], /):
        """
        usage.dask: 13
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["X"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["c"], /):
        """
        usage.dask: 14
        usage.sklearn: 2
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["b", "a"]], /):
        """
        usage.dask: 3
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["y", "x"]], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["bool", "float", "int"]], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["float", "int"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["timedelta"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: list, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["c", "b", "a"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["w"], /):
        """
        usage.dask: 6
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["z", "x"]], /):
        """
        usage.dask: 4
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["cat"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["y_"], /):
        """
        usage.dask: 5
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["v"], /):
        """
        usage.dask: 6
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["_partitions"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["_index"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: pandas.core.series.Series, /):
        """
        usage.dask: 13
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["a", "b"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["tz"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["d", "c"]], /):
        """
        usage.dask: 4
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["d"], /):
        """
        usage.dask: 10
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["f"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["e"], /):
        """
        usage.dask: 8
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["B", "A"]], /):
        """
        usage.dask: 4
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["z"], /):
        """
        usage.dask: 3
        """
        ...

    @overload
    def __getitem__(self, _0: numpy.int64, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["cint"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["cdt", "clfoat", "cstr"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["cstr", "cint"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["cdt"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["bools"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["categorical_nans"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["categorical_binary"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["unique_id"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: str, /):
        """
        usage.dask: 6
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["z", "y"]], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["d", "b", "a"]], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["col2"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["col1"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[Literal["A"], Literal["0"]], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: List[Tuple[Literal["A", "B"], Literal["0", "1"]]], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: object, /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["B", "A", "C"]], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: numpy.ndarray, /):
        """
        usage.dask: 8
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["Name"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["x", "y"]], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["D"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["x"]], /):
        """
        usage.dask: 5
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["b"]], /):
        """
        usage.dask: 3
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["__series__"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["c", "b"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["2"], /):
        """
        usage.dask: 4
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["3"], /):
        """
        usage.dask: 4
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["2-count"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["22"], /):
        """
        usage.dask: 3
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["3-count"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["23"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["33"], /):
        """
        usage.dask: 3
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["a", "c", "b"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["0"], /):
        """
        usage.dask: 4
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["1"], /):
        """
        usage.dask: 4
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["0-count"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["00"], /):
        """
        usage.dask: 3
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["1-count"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["01"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["11"], /):
        """
        usage.dask: 3
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["A"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["AA"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["AB", "AA"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["AA"], /):
        """
        usage.dask: 4
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["AB"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: List[int], /):
        """
        usage.dask: 4
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["B"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["a", "d", "c"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["d", "c", "b"]], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["03"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["13"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["b", "a", "d", "c"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["d", "c", "b", "a"]], /):
        """
        usage.dask: 3
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["02"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["12"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["cc"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g0"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g1"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: pandas.core.indexes.numeric.Int64Index, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["group"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["value"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["first_bit"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["X", "A"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["a"], Literal["e"], Literal["a"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["a"], Literal["b"], Literal["a"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[Literal["f"], None, Literal["f"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[int, int, int], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[int, None, int], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: slice[None, int, None], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["2011-01-02"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: slice[Literal["2011-01-02"], Literal["2011-01-10"], Literal["2011-01-02"]],
        /,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["2011-01"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["2011"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(
        self, _0: slice[Literal["2011-01"], Literal["2012-05"], Literal["2011-01"]], /
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(
        self, _0: slice[Literal["2011"], Literal["2015"], Literal["2011"]], /
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["k"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["y"]], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["z"]], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["d"]], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["e"]], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["e", "d"]], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["c"]], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["E"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["F"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["G"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["H"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["I"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["cluster"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["a_a"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["A_a"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["i32"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["f32", "bool", "cat"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["timestamp"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["notz"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["id"]], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["name"]], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["name", "id"]], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["e", "d", "b", "a"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["Time"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["first"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["second"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["col1"]], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["col_str"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["target"]], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[str], /):
        """
        usage.sklearn: 22
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: List[
            Literal[
                "petal width (cm)",
                "petal length (cm)",
                "sepal width (cm)",
                "sepal length (cm)",
            ]
        ],
        /,
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["Jumps", "Situps", "Chins"]], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["Pulse", "Waist", "Weight"]], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: List[
            Literal["class", "petalwidth", "petallength", "sepalwidth", "sepallength"]
        ],
        /,
    ):
        """
        usage.sklearn: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["sepallength"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["sepalwidth"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["petallength"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["petalwidth"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["class"], /):
        """
        usage.sklearn: 2
        """
        ...

    @overload
    def __getitem__(
        self,
        _0: List[Literal["petalwidth", "petallength", "sepalwidth", "sepallength"]],
        /,
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["class", "sepalwidth", "sepallength"]], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: List[Literal["petallength", "petalwidth"]], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["family"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["product-type"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["steel"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["carbon"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["hardness"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["temper_rolling"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["condition"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["formability"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["strength"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["non-ageing"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["surface-finish"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["surface-quality"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["enamelability"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["bc"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["bf"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["bt"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["bw%2Fme"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["bl"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["m"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["chrom"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["phos"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["cbond"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["marvi"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["exptl"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["ferro"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["corr"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["lustre"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["jurofm"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["s"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["p"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["shape"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["thick"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["width"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["len"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["oil"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["bore"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["packing"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["vendor"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["MYCT"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["MMIN"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["MMAX"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["CACH"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["CHMIN"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["CHMAX"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["age"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["workclass"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["fnlwgt:"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["education:"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["education-num:"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["marital-status:"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["occupation:"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["relationship:"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["race:"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["sex:"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["capital-gain:"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["capital-loss:"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["hours-per-week:"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["native-country:"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["DYRK1A_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["ITSN1_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["BDNF_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["NR1_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["NR2A_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["pAKT_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["pBRAF_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["pCAMKII_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["pCREB_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["pELK_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["pERK_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["pJNK_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["PKCA_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["pMEK_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["pNR1_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["pNR2A_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["pNR2B_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["pPKCAB_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["pRSK_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["AKT_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["BRAF_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["CAMKII_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["CREB_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["ELK_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["ERK_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["GSK3B_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["JNK_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["MEK_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["TRKA_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["RSK_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["APP_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["Bcatenin_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["SOD1_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["MTOR_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["P38_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["pMTOR_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["DSCR1_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["AMPKA_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["NR2B_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["pNUMB_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["RAPTOR_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["TIAM1_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["pP70S6_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["NUMB_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["P70S6_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["pGSK3B_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["pPKCG_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["CDK5_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["S6_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["ADARB1_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["AcetylH3K9_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["RRP1_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["BAX_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["ARC_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["ERBB4_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["nNOS_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["Tau_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["GFAP_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["GluR3_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["GluR4_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["IL1B_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["P3525_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["pCASP9_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["PSD95_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["SNCA_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["Ubiquitin_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["pGSK3B_Tyr216_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["SHH_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["BAD_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["BCL2_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["pS6_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["pCFOS_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["SYP_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["H3AcK18_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["EGR1_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["H3MeK4_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["CaNA_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["BH_LowPeakAmp"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["BH_LowPeakBPM"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["BH_HighPeakAmp"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["BH_HighPeakBPM"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["BH_HighLowRatio"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["BHSUM1"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["BHSUM2"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["BHSUM3"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["amazed.suprised"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["happy.pleased"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["relaxing.calm"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["quiet.still"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["sad.lonely"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["angry.aggresive"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["pclass"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["survived"], /):
        """
        usage.sklearn: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["sex"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["sibsp"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["parch"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["ticket"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["fare"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["cabin"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["embarked"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["boat"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["body"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["home.dest"], /):
        """
        usage.sklearn: 1
        """
        ...

    def __getitem__(self, _0: object, /):
        """
        usage.dask: 471
        usage.sklearn: 213
        usage.xarray: 8
        """
        ...

    @overload
    def __gt__(self, _0: Union[numpy.ndarray, numpy.timedelta64], /):
        """
        usage.pandas: 4
        """
        ...

    @overload
    def __gt__(self, _0: pandas.core.series.Series, /):
        """
        usage.dask: 1
        """
        ...

    def __gt__(
        self, _0: Union[pandas.core.series.Series, numpy.timedelta64, numpy.ndarray], /
    ):
        """
        usage.dask: 1
        usage.pandas: 4
        """
        ...

    def __iadd__(self, _0: Union[numpy.ndarray, numpy.timedelta64], /):
        """
        usage.pandas: 2
        """
        ...

    def __isub__(self, _0: Union[numpy.ndarray, numpy.timedelta64], /):
        """
        usage.pandas: 2
        """
        ...

    def __iter__(self, /):
        """
        usage.dask: 1
        """
        ...

    def __itruediv__(self, _0: pandas.core.frame.DataFrame, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __le__(self, _0: int, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __le__(self, _0: float, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __le__(self, _0: numpy.int64, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __le__(self, _0: numpy.float64, /):
        """
        usage.dask: 1
        """
        ...

    def __le__(self, _0: Union[numpy.float64, float, int, numpy.int64], /):
        """
        usage.dask: 4
        """
        ...

    @overload
    def __lt__(self, _0: pandas.core.series.Series, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __lt__(self, _0: int, /):
        """
        usage.dask: 2
        """
        ...

    def __lt__(self, _0: Union[int, pandas.core.series.Series], /):
        """
        usage.dask: 3
        """
        ...

    def __mod__(self, _0: numpy.timedelta64, /):
        """
        usage.pandas: 1
        """
        ...

    @overload
    def __mul__(self, _0: Union[numpy.ndarray, numpy.timedelta64, numpy.int64], /):
        """
        usage.pandas: 20
        """
        ...

    @overload
    def __mul__(self, _0: float, /):
        """
        usage.sklearn: 2
        """
        ...

    @overload
    def __mul__(self, _0: int, /):
        """
        usage.sklearn: 2
        """
        ...

    def __mul__(
        self, _0: Union[float, int, numpy.int64, numpy.timedelta64, numpy.ndarray], /
    ):
        """
        usage.pandas: 20
        usage.sklearn: 4
        """
        ...

    def __neg__(self, /):
        """
        usage.dask: 4
        """
        ...

    def __or__(self, _0: pandas.core.frame.DataFrame, /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __pow__(self, _0: numpy.timedelta64, /):
        """
        usage.pandas: 1
        """
        ...

    @overload
    def __pow__(self, _0: int, /):
        """
        usage.dask: 2
        """
        ...

    def __pow__(self, _0: Union[int, numpy.timedelta64], /):
        """
        usage.dask: 2
        usage.pandas: 1
        """
        ...

    @overload
    def __radd__(
        self, _0: Union[numpy.ndarray, numpy.timedelta64, numpy.datetime64], /
    ):
        """
        usage.pandas: 30
        """
        ...

    @overload
    def __radd__(self, _0: dask.dataframe.core.Scalar, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __radd__(self, _0: pandas.core.frame.DataFrame, /):
        """
        usage.dask: 1
        """
        ...

    def __radd__(
        self,
        _0: Union[
            dask.dataframe.core.Scalar,
            pandas.core.frame.DataFrame,
            numpy.datetime64,
            numpy.timedelta64,
            numpy.ndarray,
        ],
        /,
    ):
        """
        usage.dask: 2
        usage.pandas: 30
        """
        ...

    def __rfloordiv__(self, _0: numpy.timedelta64, /):
        """
        usage.pandas: 1
        """
        ...

    def __rmul__(self, _0: Union[numpy.ndarray, numpy.timedelta64, numpy.int64], /):
        """
        usage.pandas: 16
        """
        ...

    def __ror__(self, _0: pandas.core.frame.DataFrame, /):
        """
        usage.dask: 2
        """
        ...

    def __rpow__(self, _0: numpy.timedelta64, /):
        """
        usage.pandas: 1
        """
        ...

    @overload
    def __rsub__(
        self, _0: Union[numpy.ndarray, numpy.datetime64, numpy.timedelta64], /
    ):
        """
        usage.pandas: 26
        """
        ...

    @overload
    def __rsub__(self, _0: pandas.core.frame.DataFrame, /):
        """
        usage.dask: 1
        """
        ...

    def __rsub__(
        self,
        _0: Union[
            pandas.core.frame.DataFrame,
            numpy.timedelta64,
            numpy.datetime64,
            numpy.ndarray,
        ],
        /,
    ):
        """
        usage.dask: 1
        usage.pandas: 26
        """
        ...

    @overload
    def __rtruediv__(self, _0: Union[numpy.ndarray, numpy.timedelta64], /):
        """
        usage.pandas: 20
        """
        ...

    @overload
    def __rtruediv__(self, _0: pandas.core.frame.DataFrame, /):
        """
        usage.dask: 1
        """
        ...

    def __rtruediv__(
        self,
        _0: Union[pandas.core.frame.DataFrame, numpy.timedelta64, numpy.ndarray],
        /,
    ):
        """
        usage.dask: 1
        usage.pandas: 20
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["C"], _1: List[int], /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["amount"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["id"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["bb"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["path"], _1: pandas.core.arrays.categorical.Categorical, /
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["_partitions"], _1: numpy.ndarray, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["fruit"], _1: pandas.core.arrays.categorical.Categorical, /
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["A"], _1: pandas.core.arrays.categorical.Categorical, /
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["B"], _1: pandas.core.arrays.categorical.Categorical, /
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["A"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 4
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["numbers"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["more_numbers"], _1: pandas.core.series.Series, /
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["integers"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["a"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["E"], _1: List[Literal["e", "d", "c", "b", "a"]], /
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["w"], _1: pandas.core.arrays.categorical.Categorical, /
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["y"], _1: pandas.core.arrays.categorical.Categorical, /
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["y_"], _1: pandas.core.arrays.categorical.Categorical, /
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["v"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["y_"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["w"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["v"], _1: pandas.core.arrays.categorical.Categorical, /
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["_index"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["_index"], _1: pandas.core.arrays.categorical.Categorical, /
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["y"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 4
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["c"], _1: int, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["d"], _1: Literal["string"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["e"], _1: numpy.int64, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["f"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["g"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["dt"], _1: pandas._libs.tslibs.timestamps.Timestamp, /
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["c"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 2
        usage.sklearn: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["c"], _1: pandas.core.indexes.base.Index, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["B"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["hardbools"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["categorical_nans"], _1: pandas.core.series.Series, /
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["categorical_binary"], _1: pandas.core.series.Series, /
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["unique_id"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["x"], _1: pandas.core.arrays.categorical.Categorical, /
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["z"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 4
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["z"], _1: numpy.ndarray, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: List[Literal["b", "a"]], _1: pandas.core.frame.DataFrame, /
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["b"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 3
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["acs"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["acmin"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["acmax"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["acp"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["bcs"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["bcmin"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["bcmax"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["bcp"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["ccs"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["ccmin"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["ccmax"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["ccp"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["dcs"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["dcmin"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["dcmax"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["dcp"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["ecs"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["ecmin"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["ecmax"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["ecp"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __setitem__(self, _0: pandas.core.indexes.base.Index, _1: int, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["A"], _1: int, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["B"], _1: int, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["_partitions"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["_index"], _1: pandas.core.indexes.numeric.Int64Index, /
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: pandas.core.indexes.base.Index, _1: pandas.core.frame.DataFrame, /
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(self, _0: pandas.core.frame.DataFrame, _1: int, /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __setitem__(self, _0: pandas.core.frame.DataFrame, _1: float, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["22"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["23"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["33"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["00"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["01"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["11"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["03"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["13"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["02"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["12"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["ones"], _1: int, /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["twos"], _1: int, /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["idx"], _1: pandas.core.indexes.numeric.Int64Index, /
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: pandas.core.indexes.numeric.Int64Index,
        _1: pandas.core.frame.DataFrame,
        /,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["key"], _1: List[int], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["e"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["d"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["x"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["Time"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["third"], _1: List[int], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["col_str"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["sepallength"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["sepalwidth"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["petallength"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["petalwidth"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["class"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["family"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["product-type"], _1: pandas.core.series.Series, /
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["steel"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["carbon"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["hardness"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["temper_rolling"], _1: pandas.core.series.Series, /
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["condition"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["formability"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["strength"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["non-ageing"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["surface-finish"], _1: pandas.core.series.Series, /
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["surface-quality"], _1: pandas.core.series.Series, /
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["enamelability"], _1: pandas.core.series.Series, /
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["bc"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["bf"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["bt"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["bw%2Fme"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["bl"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["m"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["chrom"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["phos"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["cbond"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["marvi"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["exptl"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["ferro"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["corr"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: str, _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["lustre"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["jurofm"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["s"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["p"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["shape"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["thick"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["width"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["len"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["oil"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["bore"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["packing"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["vendor"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["MYCT"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["MMIN"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["MMAX"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["CACH"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["CHMIN"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["CHMAX"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["age"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["workclass"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["fnlwgt:"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["education:"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["education-num:"], _1: pandas.core.series.Series, /
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["marital-status:"], _1: pandas.core.series.Series, /
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["occupation:"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["relationship:"], _1: pandas.core.series.Series, /
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["race:"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["sex:"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["capital-gain:"], _1: pandas.core.series.Series, /
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["capital-loss:"], _1: pandas.core.series.Series, /
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["hours-per-week:"], _1: pandas.core.series.Series, /
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["native-country:"], _1: pandas.core.series.Series, /
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["DYRK1A_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["ITSN1_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["BDNF_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["NR1_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["NR2A_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["pAKT_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["pBRAF_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["pCAMKII_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["pCREB_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["pELK_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["pERK_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["pJNK_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["PKCA_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["pMEK_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["pNR1_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["pNR2A_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["pNR2B_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["pPKCAB_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["pRSK_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["AKT_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["BRAF_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["CAMKII_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["CREB_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["ELK_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["ERK_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["GSK3B_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["JNK_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["MEK_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["TRKA_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["RSK_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["APP_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["Bcatenin_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["SOD1_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["MTOR_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["P38_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["pMTOR_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["DSCR1_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["AMPKA_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["NR2B_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["pNUMB_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["RAPTOR_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["TIAM1_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["pP70S6_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["NUMB_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["P70S6_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["pGSK3B_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["pPKCG_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["CDK5_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["S6_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["ADARB1_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["AcetylH3K9_N"], _1: pandas.core.series.Series, /
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["RRP1_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["BAX_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["ARC_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["ERBB4_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["nNOS_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["Tau_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["GFAP_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["GluR3_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["GluR4_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["IL1B_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["P3525_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["pCASP9_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["PSD95_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["SNCA_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["Ubiquitin_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["pGSK3B_Tyr216_N"], _1: pandas.core.series.Series, /
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["SHH_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["BAD_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["BCL2_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["pS6_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["pCFOS_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["SYP_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["H3AcK18_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["EGR1_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["H3MeK4_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["CaNA_N"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["BH_LowPeakAmp"], _1: pandas.core.series.Series, /
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["BH_LowPeakBPM"], _1: pandas.core.series.Series, /
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["BH_HighPeakAmp"], _1: pandas.core.series.Series, /
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["BH_HighPeakBPM"], _1: pandas.core.series.Series, /
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["BH_HighLowRatio"], _1: pandas.core.series.Series, /
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["BHSUM1"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["BHSUM2"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["BHSUM3"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["amazed.suprised"], _1: pandas.core.series.Series, /
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["happy.pleased"], _1: pandas.core.series.Series, /
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["relaxing.calm"], _1: pandas.core.series.Series, /
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["quiet.still"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["sad.lonely"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["angry.aggresive"], _1: pandas.core.series.Series, /
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["pclass"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["survived"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["name"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["sex"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["sibsp"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["parch"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["ticket"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["fare"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["cabin"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["embarked"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["boat"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["body"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["home.dest"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["correlated_feature"], _1: numpy.ndarray, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: int, _1: pandas.core.arrays.categorical.Categorical, /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["1"], _1: pandas.core.arrays.sparse.array.SparseArray, /
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["2"], _1: pandas.core.arrays.sparse.array.SparseArray, /
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["3"], _1: pandas.core.arrays.sparse.array.SparseArray, /
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["0"], _1: pandas.core.arrays.sparse.array.SparseArray, /
    ):
        """
        usage.sklearn: 1
        """
        ...

    def __setitem__(self, _0: object, _1: object, /):
        """
        usage.dask: 129
        usage.sklearn: 178
        usage.xarray: 1
        """
        ...

    @overload
    def __sub__(self, _0: Union[numpy.ndarray, numpy.datetime64, numpy.timedelta64], /):
        """
        usage.pandas: 30
        """
        ...

    @overload
    def __sub__(self, _0: pandas.core.series.Series, /):
        """
        usage.dask: 5
        """
        ...

    @overload
    def __sub__(self, _0: pandas.core.frame.DataFrame, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __sub__(self, _0: int, /):
        """
        usage.dask: 2
        """
        ...

    def __sub__(self, _0: object, /):
        """
        usage.dask: 8
        usage.pandas: 30
        """
        ...

    @overload
    def __truediv__(self, _0: Union[numpy.ndarray, numpy.timedelta64], /):
        """
        usage.pandas: 22
        """
        ...

    @overload
    def __truediv__(self, _0: pandas.core.frame.DataFrame, /):
        """
        usage.dask: 1
        """
        ...

    def __truediv__(
        self,
        _0: Union[pandas.core.frame.DataFrame, numpy.timedelta64, numpy.ndarray],
        /,
    ):
        """
        usage.dask: 1
        usage.pandas: 22
        """
        ...

    def _get_numeric_data(self, /):
        """
        usage.dask: 4
        """
        ...

    def abs(self, /):
        """
        usage.dask: 3
        """
        ...

    @overload
    def add(self, /, other: pandas.core.frame.DataFrame, fill_value: int):
        """
        usage.dask: 2
        """
        ...

    @overload
    def add(self, /, other: int, fill_value: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def add(self, /, other: pandas.core.series.Series, axis: int):
        """
        usage.dask: 2
        """
        ...

    @overload
    def add(self, /, other: pandas.core.frame.DataFrame, axis: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def add(self, /, other: pandas.core.frame.DataFrame, axis: Literal["index"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def add(self, /, other: pandas.core.frame.DataFrame, axis: Literal["columns"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def add(self, /, other: pandas.core.series.Series, axis: Literal["index"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def add(self, /, other: pandas.core.series.Series, axis: Literal["columns"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def add(self, /, other: pandas.core.frame.DataFrame):
        """
        usage.dask: 1
        """
        ...

    def add(
        self,
        /,
        other: Union[pandas.core.frame.DataFrame, int, pandas.core.series.Series],
        axis: Union[Literal["columns", "index"], int] = ...,
        fill_value: int = ...,
    ):
        """
        usage.dask: 11
        """
        ...

    @overload
    def align(
        self,
        /,
        other: pandas.core.frame.DataFrame,
        join: Literal["inner"],
        axis: None,
        fill_value: None,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def align(self, /, other: pandas.core.frame.DataFrame, join: Literal["inner"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def align(
        self,
        /,
        other: pandas.core.frame.DataFrame,
        join: Literal["inner"],
        axis: None,
        fill_value: int,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def align(
        self,
        /,
        other: pandas.core.frame.DataFrame,
        join: Literal["inner"],
        fill_value: int,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def align(
        self,
        /,
        other: pandas.core.frame.DataFrame,
        join: Literal["outer"],
        axis: None,
        fill_value: None,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def align(self, /, other: pandas.core.frame.DataFrame, join: Literal["outer"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def align(
        self,
        /,
        other: pandas.core.frame.DataFrame,
        join: Literal["outer"],
        axis: None,
        fill_value: int,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def align(
        self,
        /,
        other: pandas.core.frame.DataFrame,
        join: Literal["outer"],
        fill_value: int,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def align(
        self,
        /,
        other: pandas.core.frame.DataFrame,
        join: Literal["left"],
        axis: None,
        fill_value: None,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def align(self, /, other: pandas.core.frame.DataFrame, join: Literal["left"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def align(
        self,
        /,
        other: pandas.core.frame.DataFrame,
        join: Literal["left"],
        axis: None,
        fill_value: int,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def align(
        self,
        /,
        other: pandas.core.frame.DataFrame,
        join: Literal["left"],
        fill_value: int,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def align(
        self,
        /,
        other: pandas.core.frame.DataFrame,
        join: Literal["right"],
        axis: None,
        fill_value: None,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def align(self, /, other: pandas.core.frame.DataFrame, join: Literal["right"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def align(
        self,
        /,
        other: pandas.core.frame.DataFrame,
        join: Literal["right"],
        axis: None,
        fill_value: int,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def align(
        self,
        /,
        other: pandas.core.frame.DataFrame,
        join: Literal["right"],
        fill_value: int,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def align(
        self,
        /,
        other: pandas.core.frame.DataFrame,
        join: Literal["inner"],
        axis: int,
        fill_value: None,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def align(
        self, /, other: pandas.core.frame.DataFrame, join: Literal["inner"], axis: int
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def align(
        self,
        /,
        other: pandas.core.frame.DataFrame,
        join: Literal["inner"],
        axis: Literal["index"],
        fill_value: None,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def align(
        self,
        /,
        other: pandas.core.frame.DataFrame,
        join: Literal["inner"],
        axis: Literal["index"],
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def align(
        self,
        /,
        other: pandas.core.frame.DataFrame,
        join: Literal["inner"],
        axis: Literal["columns"],
        fill_value: None,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def align(
        self,
        /,
        other: pandas.core.frame.DataFrame,
        join: Literal["inner"],
        axis: Literal["columns"],
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def align(
        self,
        /,
        other: pandas.core.frame.DataFrame,
        join: Literal["inner"],
        axis: Literal["XXX"],
        fill_value: None,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def align(
        self,
        /,
        other: pandas.core.frame.DataFrame,
        join: Literal["outer"],
        axis: int,
        fill_value: None,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def align(
        self, /, other: pandas.core.frame.DataFrame, join: Literal["outer"], axis: int
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def align(
        self,
        /,
        other: pandas.core.frame.DataFrame,
        join: Literal["outer"],
        axis: Literal["index"],
        fill_value: None,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def align(
        self,
        /,
        other: pandas.core.frame.DataFrame,
        join: Literal["outer"],
        axis: Literal["index"],
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def align(
        self,
        /,
        other: pandas.core.frame.DataFrame,
        join: Literal["outer"],
        axis: Literal["columns"],
        fill_value: None,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def align(
        self,
        /,
        other: pandas.core.frame.DataFrame,
        join: Literal["outer"],
        axis: Literal["columns"],
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def align(
        self,
        /,
        other: pandas.core.frame.DataFrame,
        join: Literal["outer"],
        axis: Literal["XXX"],
        fill_value: None,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def align(
        self,
        /,
        other: pandas.core.frame.DataFrame,
        join: Literal["left"],
        axis: int,
        fill_value: None,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def align(
        self, /, other: pandas.core.frame.DataFrame, join: Literal["left"], axis: int
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def align(
        self,
        /,
        other: pandas.core.frame.DataFrame,
        join: Literal["left"],
        axis: Literal["index"],
        fill_value: None,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def align(
        self,
        /,
        other: pandas.core.frame.DataFrame,
        join: Literal["left"],
        axis: Literal["index"],
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def align(
        self,
        /,
        other: pandas.core.frame.DataFrame,
        join: Literal["left"],
        axis: Literal["columns"],
        fill_value: None,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def align(
        self,
        /,
        other: pandas.core.frame.DataFrame,
        join: Literal["left"],
        axis: Literal["columns"],
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def align(
        self,
        /,
        other: pandas.core.frame.DataFrame,
        join: Literal["left"],
        axis: Literal["XXX"],
        fill_value: None,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def align(
        self,
        /,
        other: pandas.core.frame.DataFrame,
        join: Literal["right"],
        axis: int,
        fill_value: None,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def align(
        self, /, other: pandas.core.frame.DataFrame, join: Literal["right"], axis: int
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def align(
        self,
        /,
        other: pandas.core.frame.DataFrame,
        join: Literal["right"],
        axis: Literal["index"],
        fill_value: None,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def align(
        self,
        /,
        other: pandas.core.frame.DataFrame,
        join: Literal["right"],
        axis: Literal["index"],
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def align(
        self,
        /,
        other: pandas.core.frame.DataFrame,
        join: Literal["right"],
        axis: Literal["columns"],
        fill_value: None,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def align(
        self,
        /,
        other: pandas.core.frame.DataFrame,
        join: Literal["right"],
        axis: Literal["columns"],
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def align(
        self,
        /,
        other: pandas.core.frame.DataFrame,
        join: Literal["right"],
        axis: Literal["XXX"],
        fill_value: None,
    ):
        """
        usage.dask: 1
        """
        ...

    def align(
        self,
        /,
        other: pandas.core.frame.DataFrame,
        join: Literal["right", "left", "outer", "inner"],
        axis: Union[Literal["XXX", "columns", "index"], None, int] = ...,
        fill_value: Union[None, int] = ...,
    ):
        """
        usage.dask: 48
        """
        ...

    @overload
    def all(self, /):
        """
        usage.dask: 5
        """
        ...

    @overload
    def all(self, /, axis: int, skipna: bool):
        """
        usage.dask: 2
        """
        ...

    @overload
    def all(self, /, axis: int):
        """
        usage.dask: 4
        """
        ...

    def all(self, /, axis: int = ..., skipna: bool = ...):
        """
        usage.dask: 11
        """
        ...

    @overload
    def any(self, /):
        """
        usage.dask: 3
        """
        ...

    @overload
    def any(self, /, axis: int, skipna: bool):
        """
        usage.dask: 2
        """
        ...

    @overload
    def any(self, /, axis: int):
        """
        usage.dask: 4
        """
        ...

    def any(self, /, axis: int = ..., skipna: bool = ...):
        """
        usage.dask: 9
        """
        ...

    @overload
    def append(self, /, other: pandas.core.series.Series):
        """
        usage.dask: 1
        """
        ...

    @overload
    def append(self, /, other: pandas.core.frame.DataFrame):
        """
        usage.dask: 3
        """
        ...

    @overload
    def append(self, /, other: pandas.core.frame.DataFrame, sort: bool):
        """
        usage.dask: 8
        """
        ...

    def append(
        self,
        /,
        other: Union[pandas.core.frame.DataFrame, pandas.core.series.Series],
        sort: bool = ...,
    ):
        """
        usage.dask: 12
        """
        ...

    @overload
    def apply(self, /, func: Callable):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def apply(self, /, func: Callable, axis: int):
        """
        usage.dask: 5
        """
        ...

    @overload
    def apply(
        self,
        /,
        func: Callable,
        axis: int,
        raw: bool,
        result_type: None,
        args: Tuple[None, ...],
    ):
        """
        usage.dask: 4
        """
        ...

    @overload
    def apply(self, /, func: Callable, axis: Literal["columns"]):
        """
        usage.dask: 1
        """
        ...

    def apply(
        self,
        /,
        func: Callable,
        raw: bool = ...,
        result_type: None = ...,
        args: Tuple[None, ...] = ...,
    ):
        """
        usage.dask: 10
        usage.xarray: 1
        """
        ...

    def applymap(self, /, func: Callable):
        """
        usage.dask: 3
        """
        ...

    def assign(self, /):
        """
        usage.dask: 16
        """
        ...

    @overload
    def astype(self, /, dtype: Dict[int, numpy.dtype], copy: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def astype(self, /, dtype: Dict[Literal["b", "a"], numpy.dtype], copy: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def astype(self, /, dtype: Dict[Literal["a"], numpy.dtype], copy: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def astype(self, /, dtype: Dict[Literal["integers"], Type[float]]):
        """
        usage.dask: 2
        """
        ...

    @overload
    def astype(self, /, dtype: Dict[Literal["v"], Literal["category"]]):
        """
        usage.dask: 3
        """
        ...

    @overload
    def astype(self, /, dtype: Literal["float64"], copy: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def astype(self, /, dtype: Type[float]):
        """
        usage.dask: 9
        """
        ...

    @overload
    def astype(self, /, dtype: Dict[Literal["y"], Literal["category"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def astype(self, /, dtype: Dict[Literal["x"], Literal["category"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def astype(
        self,
        /,
        dtype: Dict[
            Literal["other", "z", "y", "x"],
            Union[
                Literal["f8", "category"], pandas.core.dtypes.dtypes.CategoricalDtype
            ],
        ],
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def astype(self, /, dtype: Dict[Literal["a"], numpy.dtype]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def astype(self, /, dtype: Dict[Literal["b"], numpy.dtype]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def astype(self, /, dtype: Literal["float"]):
        """
        usage.dask: 2
        """
        ...

    @overload
    def astype(self, /, dtype: pandas.core.series.Series):
        """
        usage.dask: 2
        """
        ...

    @overload
    def astype(self, /, dtype: Type[numpy.float64]):
        """
        usage.dask: 4
        usage.sklearn: 1
        """
        ...

    @overload
    def astype(self, /, dtype: Dict[Literal["d", "a"], Literal["f8", "category"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def astype(self, /, dtype: None):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def astype(self, /, dtype: Type[numpy.float32]):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def astype(self, /, dtype: Type[numpy.int16]):
        """
        usage.sklearn: 1
        """
        ...

    def astype(
        self,
        /,
        dtype: Union[
            None,
            type,
            Literal["float", "float64"],
            pandas.core.series.Series,
            Dict[
                Union[str, int],
                Union[
                    Type[float],
                    pandas.core.dtypes.dtypes.CategoricalDtype,
                    numpy.dtype,
                    Literal["category", "f8"],
                ],
            ],
        ],
        copy: bool = ...,
    ):
        """
        usage.dask: 32
        usage.sklearn: 4
        """
        ...

    @overload
    def bfill(self, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def bfill(self, /, axis: int):
        """
        usage.dask: 1
        """
        ...

    def bfill(self, /, axis: int = ...):
        """
        usage.dask: 2
        """
        ...

    @overload
    def clip(self, /, lower: int, upper: int):
        """
        usage.dask: 2
        """
        ...

    @overload
    def clip(self, /, lower: int, upper: None):
        """
        usage.dask: 1
        """
        ...

    @overload
    def clip(self, /, lower: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def clip(self, /, lower: None, upper: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def clip(self, /, upper: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def clip(self, /, lower: float, upper: float):
        """
        usage.dask: 2
        """
        ...

    @overload
    def clip(self, /, lower: float, upper: None):
        """
        usage.dask: 1
        """
        ...

    @overload
    def clip(self, /, lower: float):
        """
        usage.dask: 1
        """
        ...

    @overload
    def clip(self, /, lower: None, upper: float):
        """
        usage.dask: 1
        """
        ...

    @overload
    def clip(self, /, upper: float):
        """
        usage.dask: 1
        """
        ...

    def clip(
        self,
        /,
        lower: Union[None, int, float] = ...,
        upper: Union[float, int, None] = ...,
    ):
        """
        usage.dask: 12
        """
        ...

    @overload
    def combine(
        self, /, other: pandas.core.frame.DataFrame, func: Callable, fill_value: None
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def combine(
        self,
        /,
        other: pandas.core.frame.DataFrame,
        func: Callable,
        fill_value: None,
        overwrite: bool,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def combine(
        self, /, other: pandas.core.frame.DataFrame, func: Callable, fill_value: int
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def combine(
        self,
        /,
        other: pandas.core.frame.DataFrame,
        func: Callable,
        fill_value: int,
        overwrite: bool,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def combine(
        self, /, other: pandas.core.frame.DataFrame, func: Callable, fill_value: None
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def combine(
        self,
        /,
        other: pandas.core.frame.DataFrame,
        func: Callable,
        fill_value: None,
        overwrite: bool,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def combine(
        self, /, other: pandas.core.frame.DataFrame, func: Callable, overwrite: bool
    ):
        """
        usage.dask: 1
        """
        ...

    def combine(
        self,
        /,
        other: pandas.core.frame.DataFrame,
        func: Callable,
        overwrite: bool = ...,
        fill_value: Union[None, int] = ...,
    ):
        """
        usage.dask: 7
        """
        ...

    def combine_first(self, /, other: pandas.core.frame.DataFrame):
        """
        usage.dask: 3
        """
        ...

    @overload
    def copy(self, /, deep: bool):
        """
        usage.dask: 3
        """
        ...

    @overload
    def copy(self, /):
        """
        usage.dask: 13
        usage.sklearn: 4
        """
        ...

    def copy(self, /, deep: bool = ...):
        """
        usage.dask: 16
        usage.sklearn: 4
        """
        ...

    @overload
    def corr(self, /):
        """
        usage.dask: 3
        """
        ...

    @overload
    def corr(self, /, min_periods: int):
        """
        usage.dask: 1
        """
        ...

    def corr(self, /, min_periods: int = ...):
        """
        usage.dask: 4
        """
        ...

    @overload
    def count(self, /):
        """
        usage.dask: 10
        """
        ...

    @overload
    def count(self, /, axis: int):
        """
        usage.dask: 3
        """
        ...

    @overload
    def count(self, /, axis: Literal["index"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def count(self, /, axis: Literal["columns"]):
        """
        usage.dask: 1
        """
        ...

    def count(self, /, axis: Union[Literal["columns", "index"], int] = ...):
        """
        usage.dask: 15
        """
        ...

    @overload
    def cov(self, /):
        """
        usage.dask: 4
        """
        ...

    @overload
    def cov(self, /, min_periods: int):
        """
        usage.dask: 1
        """
        ...

    def cov(self, /, min_periods: int = ...):
        """
        usage.dask: 5
        """
        ...

    @overload
    def cummax(self, /):
        """
        usage.dask: 4
        """
        ...

    @overload
    def cummax(self, /, axis: None, skipna: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def cummax(self, /, axis: int, skipna: bool):
        """
        usage.dask: 2
        """
        ...

    @overload
    def cummax(self, /, axis: int):
        """
        usage.dask: 3
        """
        ...

    @overload
    def cummax(self, /, skipna: bool):
        """
        usage.dask: 1
        """
        ...

    def cummax(self, /, axis: Union[int, None] = ..., skipna: bool = ...):
        """
        usage.dask: 11
        """
        ...

    @overload
    def cummin(self, /):
        """
        usage.dask: 4
        """
        ...

    @overload
    def cummin(self, /, axis: None, skipna: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def cummin(self, /, axis: int, skipna: bool):
        """
        usage.dask: 2
        """
        ...

    @overload
    def cummin(self, /, axis: int):
        """
        usage.dask: 3
        """
        ...

    @overload
    def cummin(self, /, skipna: bool):
        """
        usage.dask: 1
        """
        ...

    def cummin(self, /, axis: Union[int, None] = ..., skipna: bool = ...):
        """
        usage.dask: 11
        """
        ...

    @overload
    def cumprod(self, /):
        """
        usage.dask: 4
        """
        ...

    @overload
    def cumprod(self, /, axis: None, skipna: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def cumprod(self, /, axis: int, skipna: bool):
        """
        usage.dask: 2
        """
        ...

    @overload
    def cumprod(self, /, axis: int):
        """
        usage.dask: 3
        """
        ...

    @overload
    def cumprod(self, /, skipna: bool):
        """
        usage.dask: 1
        """
        ...

    def cumprod(self, /, axis: Union[int, None] = ..., skipna: bool = ...):
        """
        usage.dask: 11
        """
        ...

    @overload
    def cumsum(self, /):
        """
        usage.dask: 4
        """
        ...

    @overload
    def cumsum(self, /, axis: None, skipna: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def cumsum(self, /, axis: int, skipna: bool):
        """
        usage.dask: 2
        """
        ...

    @overload
    def cumsum(self, /, axis: int):
        """
        usage.dask: 3
        """
        ...

    @overload
    def cumsum(self, /, skipna: bool):
        """
        usage.dask: 1
        """
        ...

    def cumsum(self, /, axis: Union[int, None] = ..., skipna: bool = ...):
        """
        usage.dask: 11
        """
        ...

    @overload
    def describe(self, /):
        """
        usage.dask: 6
        """
        ...

    @overload
    def describe(self, /, percentiles: List[float]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def describe(self, /, percentiles: None, include: None, exclude: None):
        """
        usage.dask: 1
        """
        ...

    @overload
    def describe(self, /, include: None, exclude: None):
        """
        usage.dask: 1
        """
        ...

    @overload
    def describe(self, /, include: List[Literal["number"]], exclude: None):
        """
        usage.dask: 1
        """
        ...

    @overload
    def describe(
        self,
        /,
        percentiles: List[float],
        include: List[Literal["number"]],
        exclude: None,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def describe(self, /, include: List[Type[numpy.timedelta64]], exclude: None):
        """
        usage.dask: 1
        """
        ...

    @overload
    def describe(
        self,
        /,
        percentiles: None,
        include: List[Type[numpy.timedelta64]],
        exclude: None,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def describe(self, /, include: List[Literal["object", "number"]], exclude: None):
        """
        usage.dask: 1
        """
        ...

    @overload
    def describe(
        self,
        /,
        percentiles: List[float],
        include: List[Literal["object", "number"]],
        exclude: None,
    ):
        """
        usage.dask: 1
        """
        ...

    def describe(
        self,
        /,
        percentiles: Union[List[float], None] = ...,
        include: Union[
            List[Union[Type[numpy.timedelta64], Literal["number", "object"]]], None
        ] = ...,
        exclude: None = ...,
    ):
        """
        usage.dask: 15
        """
        ...

    @overload
    def diff(self, /, periods: int):
        """
        usage.dask: 4
        """
        ...

    @overload
    def diff(self, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def diff(self, /, periods: int, axis: int):
        """
        usage.dask: 2
        """
        ...

    def diff(self, /, periods: int = ..., axis: int = ...):
        """
        usage.dask: 7
        """
        ...

    @overload
    def drop(self, /, labels: Literal["_partitions"], axis: int):
        """
        usage.dask: 2
        """
        ...

    @overload
    def drop(self, /, labels: Literal["timedelta"], axis: int, inplace: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def drop(self, /, columns: Literal["dt"]):
        """
        usage.dask: 2
        """
        ...

    @overload
    def drop(
        self, /, columns: List[Literal["dt"]], inplace: bool, errors: Literal["raise"]
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def drop(self, /, labels: Literal["timedelta"], axis: int):
        """
        usage.dask: 2
        """
        ...

    @overload
    def drop(
        self,
        /,
        columns: List[Literal["timedelta"]],
        inplace: bool,
        errors: Literal["raise"],
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def drop(
        self, /, columns: List[Literal["y"]], inplace: bool, errors: Literal["raise"]
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def drop(self, /, labels: Literal["y"], axis: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def drop(
        self,
        /,
        columns: List[Literal["z", "y"]],
        inplace: bool,
        errors: Literal["raise"],
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def drop(self, /, labels: List[Literal["z", "y"]], axis: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def drop(
        self,
        /,
        columns: List[Literal["x", "a"]],
        inplace: bool,
        errors: Literal["raise"],
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def drop(
        self,
        /,
        columns: List[Literal["x", "a"]],
        inplace: bool,
        errors: Literal["ignore"],
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def drop(
        self, /, labels: List[Literal["x", "a"]], axis: int, errors: Literal["ignore"]
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def drop(self, /, columns: List[Literal["z", "y"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def drop(
        self, /, columns: List[Literal["x"]], inplace: bool, errors: Literal["raise"]
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def drop(self, /, labels: int):
        """
        usage.dask: 4
        """
        ...

    @overload
    def drop(self, /, labels: List[int]):
        """
        usage.dask: 2
        """
        ...

    @overload
    def drop(
        self,
        /,
        columns: List[Literal["_partitions"]],
        inplace: bool,
        errors: Literal["raise"],
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def drop(self, /, labels: Literal["_index"], axis: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def drop(
        self,
        /,
        columns: List[Literal["_index"]],
        inplace: bool,
        errors: Literal["raise"],
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def drop(self, /, columns: Literal["category_2"]):
        """
        usage.dask: 2
        """
        ...

    @overload
    def drop(
        self,
        /,
        columns: List[Literal["category_2"]],
        inplace: bool,
        errors: Literal["raise"],
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def drop(self, /, labels: Literal["a"], axis: int):
        """
        usage.dask: 2
        """
        ...

    @overload
    def drop(
        self, /, columns: List[Literal["a"]], inplace: bool, errors: Literal["raise"]
    ):
        """
        usage.dask: 1
        """
        ...

    def drop(
        self,
        /,
        columns: Union[List[str], Literal["category_2", "dt"]] = ...,
        inplace: bool = ...,
        labels: Union[
            Literal["a", "_index", "y", "timedelta", "_partitions"],
            List[Union[int, Literal["z", "y", "x", "a"]]],
            int,
        ] = ...,
        axis: int = ...,
        errors: Literal["raise", "ignore"] = ...,
    ):
        """
        usage.dask: 33
        """
        ...

    @overload
    def drop_duplicates(self, /):
        """
        usage.dask: 5
        """
        ...

    @overload
    def drop_duplicates(self, /, keep: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def drop_duplicates(self, /, subset: List[Literal["x"]], keep: Literal["first"]):
        """
        usage.dask: 4
        """
        ...

    @overload
    def drop_duplicates(self, /, subset: Literal["y"], keep: Literal["first"]):
        """
        usage.dask: 4
        """
        ...

    @overload
    def drop_duplicates(
        self, /, subset: List[Literal["y", "x"]], keep: Literal["first"]
    ):
        """
        usage.dask: 4
        """
        ...

    @overload
    def drop_duplicates(self, /, subset: List[Literal["x"]], keep: Literal["last"]):
        """
        usage.dask: 4
        """
        ...

    @overload
    def drop_duplicates(self, /, subset: Literal["y"], keep: Literal["last"]):
        """
        usage.dask: 4
        """
        ...

    @overload
    def drop_duplicates(
        self, /, subset: List[Literal["y", "x"]], keep: Literal["last"]
    ):
        """
        usage.dask: 4
        """
        ...

    @overload
    def drop_duplicates(self, /, subset: None, keep: Literal["first"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def drop_duplicates(self, /, keep: Literal["first"]):
        """
        usage.dask: 2
        """
        ...

    @overload
    def drop_duplicates(self, /, subset: None, keep: Literal["last"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def drop_duplicates(self, /, keep: Literal["last"]):
        """
        usage.dask: 2
        """
        ...

    @overload
    def drop_duplicates(
        self, /, subset: List[Literal["z", "x"]], keep: Literal["first"]
    ):
        """
        usage.dask: 3
        """
        ...

    @overload
    def drop_duplicates(
        self, /, subset: List[Literal["z", "x"]], keep: Literal["last"]
    ):
        """
        usage.dask: 3
        """
        ...

    @overload
    def drop_duplicates(self, /, subset: Literal["ticker"], keep: Literal["last"]):
        """
        usage.dask: 1
        """
        ...

    def drop_duplicates(
        self,
        /,
        subset: Union[Literal["ticker", "y"], None, List[Literal["x", "y", "z"]]] = ...,
        keep: Union[Literal["last", "first"], bool] = ...,
    ):
        """
        usage.dask: 43
        """
        ...

    @overload
    def dropna(self, /, how: Literal["any"], thresh: None, subset: None):
        """
        usage.dask: 1
        """
        ...

    @overload
    def dropna(self, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def dropna(self, /, how: Literal["all"], thresh: None, subset: None):
        """
        usage.dask: 1
        """
        ...

    @overload
    def dropna(self, /, how: Literal["all"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def dropna(self, /, how: Literal["any"], thresh: None, subset: List[Literal["x"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def dropna(self, /, subset: List[Literal["x"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def dropna(
        self, /, how: Literal["any"], thresh: None, subset: List[Literal["z", "y"]]
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def dropna(self, /, subset: List[Literal["z", "y"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def dropna(
        self, /, how: Literal["all"], thresh: None, subset: List[Literal["z", "y"]]
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def dropna(self, /, how: Literal["all"], subset: List[Literal["z", "y"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def dropna(self, /, thresh: None):
        """
        usage.dask: 2
        """
        ...

    @overload
    def dropna(self, /, thresh: int):
        """
        usage.dask: 8
        """
        ...

    @overload
    def dropna(self, /, how: Literal["any"], thresh: int, subset: None):
        """
        usage.dask: 1
        """
        ...

    @overload
    def dropna(self, /, how: Literal["any"], thresh: None, subset: List[str]):
        """
        usage.dask: 1
        """
        ...

    def dropna(
        self,
        /,
        how: Literal["any", "all"] = ...,
        thresh: Union[None, int] = ...,
        subset: Union[List[str], None] = ...,
    ):
        """
        usage.dask: 22
        """
        ...

    def equals(self, /, other: pandas.core.frame.DataFrame):
        """
        usage.dask: 2
        usage.xarray: 10
        """
        ...

    @overload
    def ewm(self, /, span: int):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def ewm(self, /, alpha: float):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def ewm(self, /, com: float):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def ewm(self, /, halflife: int):
        """
        usage.xarray: 1
        """
        ...

    def ewm(
        self,
        /,
        alpha: float = ...,
        span: int = ...,
        com: float = ...,
        halflife: int = ...,
    ):
        """
        usage.xarray: 4
        """
        ...

    def explode(self, /, column: Literal["A"]):
        """
        usage.dask: 2
        """
        ...

    @overload
    def ffill(self, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def ffill(self, /, axis: int):
        """
        usage.dask: 1
        """
        ...

    def ffill(self, /, axis: int = ...):
        """
        usage.dask: 2
        """
        ...

    @overload
    def fillna(self, /, value: Literal["-"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def fillna(self, /, value: int, method: None, axis: int, limit: None):
        """
        usage.dask: 2
        """
        ...

    @overload
    def fillna(self, /, value: int):
        """
        usage.dask: 2
        """
        ...

    @overload
    def fillna(self, /, value: None, method: Literal["pad"], axis: int, limit: None):
        """
        usage.dask: 2
        """
        ...

    @overload
    def fillna(self, /, method: Literal["pad"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def fillna(self, /, method: Literal["ffill"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def fillna(self, /, method: Literal["ffill"], limit: None):
        """
        usage.dask: 1
        """
        ...

    @overload
    def fillna(self, /, value: None, method: Literal["bfill"], axis: int, limit: None):
        """
        usage.dask: 2
        """
        ...

    @overload
    def fillna(self, /, method: Literal["bfill"]):
        """
        usage.dask: 2
        """
        ...

    @overload
    def fillna(self, /, method: Literal["bfill"], limit: None):
        """
        usage.dask: 1
        """
        ...

    @overload
    def fillna(self, /, value: None, method: Literal["pad"], axis: int, limit: int):
        """
        usage.dask: 2
        """
        ...

    @overload
    def fillna(self, /, method: Literal["pad"], limit: int):
        """
        usage.dask: 2
        """
        ...

    @overload
    def fillna(self, /, method: Literal["ffill"], limit: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def fillna(self, /, value: None, method: Literal["bfill"], axis: int, limit: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def fillna(self, /, method: Literal["bfill"], limit: int):
        """
        usage.dask: 2
        """
        ...

    @overload
    def fillna(self, /, value: int, axis: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def fillna(self, /, method: Literal["pad"], axis: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def fillna(self, /, method: Literal["pad"], axis: int, limit: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def fillna(self, /, value: None, method: Literal["ffill"], axis: int, limit: None):
        """
        usage.dask: 2
        """
        ...

    @overload
    def fillna(
        self, /, value: pandas.core.series.Series, method: None, axis: int, limit: None
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def fillna(self, /, value: pandas.core.series.Series):
        """
        usage.dask: 1
        """
        ...

    def fillna(
        self,
        /,
        value: Union[pandas.core.series.Series, int, None, Literal["-"]] = ...,
        method: Union[None, Literal["ffill", "pad", "bfill"]] = ...,
        axis: int = ...,
        limit: Union[None, int] = ...,
    ):
        """
        usage.dask: 31
        """
        ...

    @overload
    def first(self, /, offset: Literal["0d"]):
        """
        usage.dask: 3
        """
        ...

    @overload
    def first(self, /, offset: Literal["100h"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def first(self, /, offset: Literal["20d"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def first(self, /, offset: Literal["20B"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def first(self, /, offset: Literal["3W"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def first(self, /, offset: Literal["3M"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def first(self, /, offset: Literal["400d"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def first(self, /, offset: Literal["13M"]):
        """
        usage.dask: 1
        """
        ...

    def first(self, /, offset: str):
        """
        usage.dask: 10
        """
        ...

    @overload
    def floordiv(self, /, other: pandas.core.frame.DataFrame, fill_value: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def floordiv(self, /, other: int, fill_value: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def floordiv(self, /, other: pandas.core.series.Series, axis: int):
        """
        usage.dask: 2
        """
        ...

    @overload
    def floordiv(self, /, other: pandas.core.frame.DataFrame, axis: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def floordiv(self, /, other: pandas.core.frame.DataFrame, axis: Literal["index"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def floordiv(self, /, other: pandas.core.frame.DataFrame, axis: Literal["columns"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def floordiv(self, /, other: pandas.core.series.Series, axis: Literal["index"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def floordiv(self, /, other: pandas.core.series.Series, axis: Literal["columns"]):
        """
        usage.dask: 1
        """
        ...

    def floordiv(
        self,
        /,
        other: Union[pandas.core.series.Series, pandas.core.frame.DataFrame, int],
        axis: Union[Literal["columns", "index"], int] = ...,
        fill_value: int = ...,
    ):
        """
        usage.dask: 9
        """
        ...

    @overload
    def get(self, /, key: Literal["path"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def get(self, /, key: Literal["fruit"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def get(self, /, key: Literal["A"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def get(self, /, key: Literal["B"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def get(self, /, key: Literal["w"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def get(self, /, key: Literal["y"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def get(self, /, key: Literal["y_"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def get(self, /, key: Literal["v"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def get(self, /, key: Literal["_index"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def get(self, /, key: Literal["x"]):
        """
        usage.dask: 1
        """
        ...

    def get(self, /, key: str):
        """
        usage.dask: 10
        """
        ...

    @overload
    def groupby(self, /, by: Literal["_partitions"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def groupby(self, /, by: Literal["w"], group_keys: bool):
        """
        usage.dask: 2
        """
        ...

    @overload
    def groupby(self, /, by: pandas.core.series.Series):
        """
        usage.dask: 106
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["w"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def groupby(self, /, level: int, sort: bool):
        """
        usage.dask: 8
        """
        ...

    @overload
    def groupby(self, /, by: Literal["x"], group_keys: bool):
        """
        usage.dask: 3
        """
        ...

    @overload
    def groupby(self, /, level: int):
        """
        usage.dask: 5
        """
        ...

    @overload
    def groupby(self, /, by: Callable):
        """
        usage.dask: 1
        """
        ...

    @overload
    def groupby(self, /, by: Callable, group_keys: bool):
        """
        usage.dask: 2
        """
        ...

    @overload
    def groupby(self, /, by: List[Callable]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["B", "A"]], group_keys: bool):
        """
        usage.dask: 2
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["B", "A"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def groupby(self, /, level: List[int], sort: bool):
        """
        usage.dask: 12
        """
        ...

    @overload
    def groupby(self, /, by: Literal["y"]):
        """
        usage.dask: 4
        """
        ...

    @overload
    def groupby(self, /, by: Literal["y"], group_keys: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def groupby(self, /, by: Literal["A"], group_keys: bool):
        """
        usage.dask: 4
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["A", "x"]], group_keys: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def groupby(self, /, by: Literal["does_not_exist"], group_keys: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def groupby(self, /, by: Literal["a"], group_keys: bool):
        """
        usage.dask: 4
        """
        ...

    @overload
    def groupby(self, /, by: Literal["a"]):
        """
        usage.dask: 41
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["a"]]):
        """
        usage.dask: 9
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["a"]], group_keys: bool):
        """
        usage.dask: 3
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["b", "a"]]):
        """
        usage.dask: 9
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["b", "a"]], group_keys: bool):
        """
        usage.dask: 3
        """
        ...

    @overload
    def groupby(self, /, by: List[pandas.core.series.Series]):
        """
        usage.dask: 15
        """
        ...

    @overload
    def groupby(self, /, by: List[pandas.core.series.Series], group_keys: bool):
        """
        usage.dask: 4
        """
        ...

    @overload
    def groupby(self, /, by: pandas.core.indexes.numeric.Int64Index, group_keys: bool):
        """
        usage.dask: 2
        """
        ...

    @overload
    def groupby(self, /, by: List[pandas.core.indexes.numeric.Int64Index]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def groupby(self, /, by: pandas.core.indexes.numeric.Int64Index):
        """
        usage.dask: 2
        """
        ...

    @overload
    def groupby(self, /, by: pandas.core.series.Series, group_keys: bool):
        """
        usage.dask: 4
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["c", "b", "a"]], group_keys: bool):
        """
        usage.dask: 2
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["c", "b", "a"]]):
        """
        usage.dask: 2
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["1", "0"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def groupby(self, /, level: List[int]):
        """
        usage.dask: 4
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["2"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["1"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["2", "1", "0"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["c", "a"]]):
        """
        usage.dask: 2
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["c", "a"]], group_keys: bool):
        """
        usage.dask: 2
        """
        ...

    @overload
    def groupby(self, /, by: Literal["b"], group_keys: bool):
        """
        usage.dask: 2
        """
        ...

    @overload
    def groupby(self, /, by: Literal["b"]):
        """
        usage.dask: 26
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["b"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def groupby(self, /, by: List[int]):
        """
        usage.dask: 4
        """
        ...

    @overload
    def groupby(self, /, by: Literal["strings"]):
        """
        usage.dask: 2
        """
        ...

    @overload
    def groupby(self, /, by: Literal["strings"], group_keys: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["strings"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def groupby(self, /, by: Literal["x"]):
        """
        usage.dask: 8
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["x", "a"]], group_keys: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def groupby(self, /, by: Literal["A"]):
        """
        usage.dask: 9
        """
        ...

    @overload
    def groupby(self, /, by: Literal["AA"], group_keys: bool):
        """
        usage.dask: 4
        """
        ...

    @overload
    def groupby(self, /, by: Literal["AA"]):
        """
        usage.dask: 3
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["AB", "AA"]], group_keys: bool):
        """
        usage.dask: 4
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["AB", "AA"]]):
        """
        usage.dask: 3
        """
        ...

    @overload
    def groupby(self, /, by: int, group_keys: bool):
        """
        usage.dask: 3
        """
        ...

    @overload
    def groupby(self, /, by: int):
        """
        usage.dask: 2
        """
        ...

    @overload
    def groupby(self, /, by: List[int], group_keys: bool):
        """
        usage.dask: 2
        """
        ...

    @overload
    def groupby(self, /, by: Literal["B"], group_keys: bool):
        """
        usage.dask: 2
        """
        ...

    @overload
    def groupby(self, /, by: Literal["B"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["d", "a"]]):
        """
        usage.dask: 2
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["d", "a"]], group_keys: bool):
        """
        usage.dask: 2
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["3", "2"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["1", "2"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["x"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["y", "x"]], group_keys: bool):
        """
        usage.dask: 2
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["y", "x"]]):
        """
        usage.dask: 2
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["A"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def groupby(self, /, by: List[pandas.core.groupby.grouper.Grouper]):
        """
        usage.dask: 2
        """
        ...

    @overload
    def groupby(self, /, by: Literal["foo"], group_keys: bool):
        """
        usage.dask: 2
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["a", "idx"]]):
        """
        usage.dask: 3
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["a", "idx"]], group_keys: bool):
        """
        usage.dask: 3
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["idx", "a"]]):
        """
        usage.dask: 3
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["idx", "a"]], group_keys: bool):
        """
        usage.dask: 3
        """
        ...

    @overload
    def groupby(self, /, by: Literal["idx"]):
        """
        usage.dask: 2
        """
        ...

    @overload
    def groupby(self, /, by: Literal["idx"], group_keys: bool):
        """
        usage.dask: 3
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["idx"]]):
        """
        usage.dask: 2
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["idx"]], group_keys: bool):
        """
        usage.dask: 3
        """
        ...

    @overload
    def groupby(self, /, by: Literal["g"]):
        """
        usage.dask: 2
        """
        ...

    @overload
    def groupby(self, /, by: Literal["g"], group_keys: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["g"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def groupby(self, /, by: Literal["name"], group_keys: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["name"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def groupby(self, /, by: Literal["group"]):
        """
        usage.dask: 12
        """
        ...

    @overload
    def groupby(self, /, by: Literal["group"], group_keys: bool):
        """
        usage.dask: 3
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["group"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def groupby(self, /, by: Literal["key"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def groupby(self, /, by: Literal["key"], group_keys: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["3"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def groupby(self, /, by: Literal["foo"]):
        """
        usage.dask: 2
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["foo"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def groupby(self, /, by: Literal["category_1"]):
        """
        usage.dask: 2
        """
        ...

    @overload
    def groupby(self, /, by: Literal["category_1"], group_keys: bool):
        """
        usage.dask: 2
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["category_1"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["category_2", "category_1"]]):
        """
        usage.dask: 3
        """
        ...

    @overload
    def groupby(
        self, /, by: List[Literal["category_2", "category_1"]], group_keys: bool
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def groupby(self, /, by: Literal["a"], group_keys: bool, dropna: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def groupby(self, /, by: Literal["a"], dropna: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def groupby(self, /, by: Literal["ids"], group_keys: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["ids"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def groupby(self, /, by: Literal["ids"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["c", "b"]], group_keys: bool):
        """
        usage.dask: 2
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["d", "b"]], group_keys: bool):
        """
        usage.dask: 2
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["e", "b"]], group_keys: bool):
        """
        usage.dask: 2
        """
        ...

    @overload
    def groupby(self, /, by: Literal["a"], sort: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def groupby(self, /, by: Literal["b"], sort: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def groupby(self, /, by: Literal["c"], group_keys: bool):
        """
        usage.dask: 2
        """
        ...

    @overload
    def groupby(self, /, by: Literal["c"], sort: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["c"]]):
        """
        usage.dask: 2
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["b", "a"]], sort: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["c", "a"]], sort: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def groupby(self, /, by: Literal["x"], sort: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def groupby(self, /, by: Literal["j"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["c"]], group_keys: bool):
        """
        usage.dask: 2
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["y"]]):
        """
        usage.dask: 1
        """
        ...

    def groupby(
        self,
        /,
        by: object = ...,
        group_keys: bool = ...,
        dropna: bool = ...,
        level: Union[List[int], int] = ...,
        sort: bool = ...,
    ):
        """
        usage.dask: 449
        """
        ...

    @overload
    def head(self, /):
        """
        usage.dask: 5
        """
        ...

    @overload
    def head(self, /, n: int):
        """
        usage.dask: 13
        """
        ...

    def head(self, /, n: int = ...):
        """
        usage.dask: 18
        """
        ...

    @overload
    def idxmax(self, /, axis: int, skipna: bool):
        """
        usage.dask: 3
        """
        ...

    @overload
    def idxmax(self, /, axis: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def idxmax(self, /, skipna: bool):
        """
        usage.dask: 3
        """
        ...

    @overload
    def idxmax(self, /):
        """
        usage.dask: 1
        """
        ...

    def idxmax(self, /, skipna: bool = ..., axis: int = ...):
        """
        usage.dask: 8
        """
        ...

    @overload
    def idxmin(self, /, axis: int, skipna: bool):
        """
        usage.dask: 2
        """
        ...

    @overload
    def idxmin(self, /, skipna: bool):
        """
        usage.dask: 5
        """
        ...

    @overload
    def idxmin(self, /):
        """
        usage.dask: 1
        """
        ...

    def idxmin(self, /, axis: int = ..., skipna: bool = ...):
        """
        usage.dask: 8
        """
        ...

    def info(self, /, buf: _io.StringIO, memory_usage: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def interpolate(self, /, method: Literal["linear"], axis: int):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def interpolate(self, /, method: Literal["nearest"], axis: int):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def interpolate(self, /, method: Literal["zero"], axis: int):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def interpolate(self, /, method: Literal["slinear"], axis: int):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def interpolate(self, /, method: Literal["quadratic"], axis: int):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def interpolate(self, /, method: Literal["cubic"], axis: int):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def interpolate(self, /, method: Literal["time"], axis: int):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def interpolate(self, /, method: Literal["index"], axis: int):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def interpolate(self, /, method: Literal["values"], axis: int):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def interpolate(self, /, method: Literal["polynomial"], axis: int):
        """
        usage.xarray: 1
        """
        ...

    def interpolate(self, /, method: str, axis: int):
        """
        usage.xarray: 10
        """
        ...

    @overload
    def isin(self, /, values: List[int]):
        """
        usage.dask: 3
        """
        ...

    @overload
    def isin(self, /, values: Dict[Literal["b", "a"], List[int]]):
        """
        usage.dask: 3
        """
        ...

    def isin(self, /, values: Union[Dict[Literal["b", "a"], List[int]], List[int]]):
        """
        usage.dask: 6
        """
        ...

    def isna(self, /):
        """
        usage.dask: 1
        """
        ...

    def isnull(self, /):
        """
        usage.dask: 6
        """
        ...

    def items(self, /):
        """
        usage.xarray: 2
        """
        ...

    def iteritems(self, /):
        """
        usage.dask: 2
        usage.xarray: 1
        """
        ...

    def iterrows(self, /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def itertuples(self, /):
        """
        usage.dask: 3
        """
        ...

    @overload
    def itertuples(self, /, index: bool):
        """
        usage.dask: 3
        """
        ...

    @overload
    def itertuples(self, /, index: bool, name: Literal["Pandas"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def itertuples(self, /, name: None):
        """
        usage.dask: 1
        """
        ...

    @overload
    def itertuples(self, /, index: bool, name: None):
        """
        usage.dask: 1
        """
        ...

    def itertuples(
        self, /, index: bool = ..., name: Union[None, Literal["Pandas"]] = ...
    ):
        """
        usage.dask: 9
        """
        ...

    @overload
    def join(self, /, other: pandas.core.frame.DataFrame):
        """
        usage.dask: 1
        """
        ...

    @overload
    def join(self, /, other: pandas.core.frame.DataFrame, how: Literal["right"]):
        """
        usage.dask: 5
        """
        ...

    @overload
    def join(self, /, other: pandas.core.frame.DataFrame, how: Literal["inner"]):
        """
        usage.dask: 6
        """
        ...

    @overload
    def join(self, /, other: pandas.core.frame.DataFrame, how: Literal["outer"]):
        """
        usage.dask: 5
        """
        ...

    @overload
    def join(
        self,
        /,
        other: pandas.core.frame.DataFrame,
        how: Literal["inner"],
        lsuffix: Literal["_l"],
        rsuffix: Literal["_r"],
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def join(
        self,
        /,
        other: pandas.core.frame.DataFrame,
        how: Literal["inner"],
        lsuffix: Literal["l"],
        rsuffix: Literal["r"],
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def join(
        self,
        /,
        other: pandas.core.frame.DataFrame,
        how: Literal["outer"],
        lsuffix: Literal["l"],
        rsuffix: Literal["r"],
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def join(self, /, other: pandas.core.frame.DataFrame, how: Literal["left"]):
        """
        usage.dask: 4
        """
        ...

    @overload
    def join(
        self,
        /,
        other: pandas.core.frame.DataFrame,
        how: Literal["left"],
        lsuffix: Literal["l"],
        rsuffix: Literal["r"],
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def join(
        self,
        /,
        other: pandas.core.frame.DataFrame,
        how: Literal["right"],
        lsuffix: Literal["l"],
        rsuffix: Literal["r"],
    ):
        """
        usage.dask: 2
        """
        ...

    def join(
        self,
        /,
        other: pandas.core.frame.DataFrame,
        how: Literal["right", "left", "outer", "inner"] = ...,
        lsuffix: Literal["l", "_l"] = ...,
        rsuffix: Literal["r", "_r"] = ...,
    ):
        """
        usage.dask: 31
        """
        ...

    @overload
    def last(self, /, offset: Literal["0d"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def last(self, /, offset: Literal["100h"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def last(self, /, offset: Literal["20d"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def last(self, /, offset: Literal["20B"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def last(self, /, offset: Literal["3W"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def last(self, /, offset: Literal["3M"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def last(self, /, offset: Literal["400d"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def last(self, /, offset: Literal["13M"]):
        """
        usage.dask: 1
        """
        ...

    def last(self, /, offset: str):
        """
        usage.dask: 8
        """
        ...

    @overload
    def mask(self, /, cond: pandas.core.frame.DataFrame, other: float):
        """
        usage.dask: 1
        """
        ...

    @overload
    def mask(self, /, cond: pandas.core.frame.DataFrame):
        """
        usage.dask: 1
        """
        ...

    @overload
    def mask(
        self, /, cond: pandas.core.frame.DataFrame, other: pandas.core.frame.DataFrame
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def mask(
        self, /, cond: pandas.core.series.Series, other: pandas.core.frame.DataFrame
    ):
        """
        usage.dask: 2
        """
        ...

    def mask(
        self,
        /,
        cond: Union[pandas.core.series.Series, pandas.core.frame.DataFrame],
        other: Union[pandas.core.frame.DataFrame, float] = ...,
    ):
        """
        usage.dask: 6
        """
        ...

    @overload
    def max(self, /, axis: int, skipna: bool):
        """
        usage.dask: 3
        """
        ...

    @overload
    def max(self, /):
        """
        usage.dask: 4
        """
        ...

    @overload
    def max(self, /, axis: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def max(self, /, axis: Literal["index"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def max(self, /, axis: Literal["columns"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def max(self, /, skipna: bool):
        """
        usage.dask: 2
        """
        ...

    def max(
        self, /, axis: Union[Literal["columns", "index"], int] = ..., skipna: bool = ...
    ):
        """
        usage.dask: 12
        """
        ...

    @overload
    def mean(self, /, axis: int, skipna: bool):
        """
        usage.dask: 3
        """
        ...

    @overload
    def mean(self, /):
        """
        usage.dask: 7
        """
        ...

    @overload
    def mean(self, /, axis: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def mean(self, /, axis: Literal["index"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def mean(self, /, axis: Literal["columns"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def mean(self, /, skipna: bool):
        """
        usage.dask: 2
        """
        ...

    def mean(
        self, /, axis: Union[Literal["columns", "index"], int] = ..., skipna: bool = ...
    ):
        """
        usage.dask: 15
        """
        ...

    @overload
    def melt(
        self,
        /,
        id_vars: None,
        value_vars: None,
        var_name: None,
        value_name: Literal["value"],
        col_level: None,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def melt(
        self,
        /,
        id_vars: Literal["C"],
        value_vars: None,
        var_name: None,
        value_name: Literal["value"],
        col_level: None,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def melt(
        self,
        /,
        id_vars: None,
        value_vars: Literal["C"],
        var_name: None,
        value_name: Literal["value"],
        col_level: None,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def melt(
        self,
        /,
        id_vars: None,
        value_vars: List[Literal["C", "A"]],
        var_name: Literal["myvar"],
        value_name: Literal["value"],
        col_level: None,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def melt(
        self,
        /,
        id_vars: Literal["B"],
        value_vars: List[Literal["C", "A"]],
        var_name: None,
        value_name: Literal["myval"],
        col_level: None,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def melt(self, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def melt(self, /, id_vars: Literal["C"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def melt(self, /, value_vars: Literal["C"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def melt(self, /, value_vars: List[Literal["C", "A"]], var_name: Literal["myvar"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def melt(
        self,
        /,
        id_vars: Literal["B"],
        value_vars: List[Literal["C", "A"]],
        value_name: Literal["myval"],
    ):
        """
        usage.dask: 1
        """
        ...

    def melt(
        self,
        /,
        id_vars: Union[Literal["B", "C"], None] = ...,
        value_vars: Union[List[Literal["C", "A"]], Literal["C"], None] = ...,
        var_name: Union[Literal["myvar"], None] = ...,
        value_name: Literal["myval", "value"] = ...,
        col_level: None = ...,
    ):
        """
        usage.dask: 10
        """
        ...

    @overload
    def memory_usage(self, /, index: bool, deep: bool):
        """
        usage.dask: 4
        """
        ...

    @overload
    def memory_usage(self, /, index: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def memory_usage(self, /, deep: bool):
        """
        usage.sklearn: 1
        """
        ...

    def memory_usage(self, /, deep: bool = ..., index: bool = ...):
        """
        usage.dask: 5
        usage.sklearn: 1
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["inner"],
        on: Literal["idx"],
    ):
        """
        usage.dask: 6
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["inner"],
        left_on: Literal["idx"],
        right_on: Literal["idx"],
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 4
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["left"],
        on: Literal["idx"],
    ):
        """
        usage.dask: 5
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["left"],
        left_on: Literal["idx"],
        right_on: Literal["idx"],
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 4
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["right"],
        on: Literal["idx"],
    ):
        """
        usage.dask: 5
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["right"],
        left_on: Literal["idx"],
        right_on: Literal["idx"],
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 4
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["outer"],
        on: Literal["idx"],
    ):
        """
        usage.dask: 4
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["outer"],
        left_on: Literal["idx"],
        right_on: Literal["idx"],
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 3
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["inner"],
        on: List[Literal["idx"]],
    ):
        """
        usage.dask: 6
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["inner"],
        left_on: List[Literal["idx"]],
        right_on: List[Literal["idx"]],
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 4
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["left"],
        on: List[Literal["idx"]],
    ):
        """
        usage.dask: 5
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["left"],
        left_on: List[Literal["idx"]],
        right_on: List[Literal["idx"]],
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 4
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["right"],
        on: List[Literal["idx"]],
    ):
        """
        usage.dask: 5
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["right"],
        left_on: List[Literal["idx"]],
        right_on: List[Literal["idx"]],
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 4
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["outer"],
        on: List[Literal["idx"]],
    ):
        """
        usage.dask: 4
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["outer"],
        left_on: List[Literal["idx"]],
        right_on: List[Literal["idx"]],
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 3
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["inner"],
        on: List[Literal["k", "idx"]],
    ):
        """
        usage.dask: 6
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["inner"],
        left_on: List[Literal["k", "idx"]],
        right_on: List[Literal["k", "idx"]],
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 4
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["left"],
        on: List[Literal["k", "idx"]],
    ):
        """
        usage.dask: 5
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["left"],
        left_on: List[Literal["k", "idx"]],
        right_on: List[Literal["k", "idx"]],
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 4
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["right"],
        on: List[Literal["k", "idx"]],
    ):
        """
        usage.dask: 5
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["right"],
        left_on: List[Literal["k", "idx"]],
        right_on: List[Literal["k", "idx"]],
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 4
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["outer"],
        on: List[Literal["k", "idx"]],
    ):
        """
        usage.dask: 4
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["outer"],
        left_on: List[Literal["k", "idx"]],
        right_on: List[Literal["k", "idx"]],
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 3
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["inner"],
        on: List[Literal["idx", "k"]],
    ):
        """
        usage.dask: 6
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["inner"],
        left_on: List[Literal["idx", "k"]],
        right_on: List[Literal["idx", "k"]],
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 4
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["left"],
        on: List[Literal["idx", "k"]],
    ):
        """
        usage.dask: 5
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["left"],
        left_on: List[Literal["idx", "k"]],
        right_on: List[Literal["idx", "k"]],
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 4
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["right"],
        on: List[Literal["idx", "k"]],
    ):
        """
        usage.dask: 5
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["right"],
        left_on: List[Literal["idx", "k"]],
        right_on: List[Literal["idx", "k"]],
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 4
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["outer"],
        on: List[Literal["idx", "k"]],
    ):
        """
        usage.dask: 4
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["outer"],
        left_on: List[Literal["idx", "k"]],
        right_on: List[Literal["idx", "k"]],
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 3
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["left"],
        left_index: bool,
        right_index: bool,
    ):
        """
        usage.dask: 3
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["right"],
        left_index: bool,
        right_index: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["inner"],
        left_index: bool,
        right_index: bool,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["outer"],
        left_index: bool,
        right_index: bool,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["inner"],
        left_on: Literal["y"],
        right_on: Literal["y"],
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["outer"],
        left_on: Literal["x"],
        right_on: Literal["z"],
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["outer"],
        left_on: Literal["y"],
        right_on: Literal["y"],
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["left"],
        left_on: Literal["y"],
        right_on: Literal["y"],
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["right"],
        left_on: Literal["y"],
        right_on: Literal["y"],
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["inner"],
        left_on: None,
        right_on: None,
        left_index: bool,
        right_index: bool,
        suffixes: List[Literal["_r", "_l"]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["inner"],
        left_on: None,
        right_on: None,
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["outer"],
        left_on: None,
        right_on: None,
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 3
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["left"],
        left_on: None,
        right_on: None,
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["right"],
        left_on: None,
        right_on: None,
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["inner"],
        left_on: List[Literal["A"]],
        right_on: List[Literal["A"]],
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["outer"],
        left_on: List[Literal["A"]],
        right_on: List[Literal["A"]],
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["left"],
        left_on: List[Literal["A"]],
        right_on: List[Literal["A"]],
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["right"],
        left_on: List[Literal["A"]],
        right_on: List[Literal["A"]],
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["inner"],
        left_on: Literal["x"],
        right_on: Literal["z"],
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["inner"],
        left_on: Literal["x"],
        right_on: Literal["z"],
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["1"], Literal["2"]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["inner"],
        left_on: List[Literal["y"]],
        right_on: List[Literal["y"]],
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 3
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["inner"],
        left_on: None,
        right_on: None,
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["1"], Literal["2"]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["inner"],
        on: None,
        left_on: Literal["x"],
        right_on: None,
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["inner"],
        on: None,
        left_on: Literal["x"],
        right_on: None,
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["1"], Literal["2"]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["outer"],
        left_on: Literal["x"],
        right_on: Literal["z"],
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["1"], Literal["2"]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["outer"],
        left_on: List[Literal["y"]],
        right_on: List[Literal["y"]],
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["outer"],
        left_on: None,
        right_on: None,
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["1"], Literal["2"]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["outer"],
        on: None,
        left_on: Literal["x"],
        right_on: None,
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["outer"],
        on: None,
        left_on: Literal["x"],
        right_on: None,
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["1"], Literal["2"]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["left"],
        left_on: Literal["x"],
        right_on: Literal["z"],
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["left"],
        left_on: Literal["x"],
        right_on: Literal["z"],
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["1"], Literal["2"]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["left"],
        left_on: List[Literal["y"]],
        right_on: List[Literal["y"]],
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 3
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["left"],
        left_on: None,
        right_on: None,
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["1"], Literal["2"]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["left"],
        on: None,
        left_on: Literal["x"],
        right_on: None,
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["left"],
        on: None,
        left_on: Literal["x"],
        right_on: None,
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["1"], Literal["2"]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["right"],
        left_on: Literal["x"],
        right_on: Literal["z"],
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["right"],
        left_on: Literal["x"],
        right_on: Literal["z"],
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["1"], Literal["2"]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["right"],
        left_on: List[Literal["y"]],
        right_on: List[Literal["y"]],
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 3
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["right"],
        left_on: None,
        right_on: None,
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["1"], Literal["2"]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["right"],
        on: None,
        left_on: Literal["x"],
        right_on: None,
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["right"],
        on: None,
        left_on: Literal["x"],
        right_on: None,
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["1"], Literal["2"]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["leftsemi"],
        on: Literal["emp_id"],
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["leftanti"],
        on: Literal["emp_id"],
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["inner"],
        left_on: Literal["a"],
        right_on: Literal["d"],
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["inner"],
        left_on: None,
        right_on: None,
        left_index: bool,
        right_index: bool,
        suffixes: List[Literal[""]],
        indicator: bool,
    ):
        """
        usage.dask: 3
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["inner"],
        left_on: None,
        right_on: None,
        left_index: bool,
        right_index: bool,
        suffixes: List[Literal["r", "l"]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["outer"],
        left_on: None,
        right_on: None,
        left_index: bool,
        right_index: bool,
        suffixes: List[Literal[""]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["outer"],
        left_on: None,
        right_on: None,
        left_index: bool,
        right_index: bool,
        suffixes: List[Literal["r", "l"]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["left"],
        left_on: None,
        right_on: None,
        left_index: bool,
        right_index: bool,
        suffixes: List[Literal[""]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["left"],
        left_on: None,
        right_on: None,
        left_index: bool,
        right_index: bool,
        suffixes: List[Literal["r", "l"]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["right"],
        left_on: None,
        right_on: None,
        left_index: bool,
        right_index: bool,
        suffixes: List[Literal[""]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["right"],
        left_on: None,
        right_on: None,
        left_index: bool,
        right_index: bool,
        suffixes: List[Literal["r", "l"]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["inner"],
        left_on: Literal["b"],
        right_on: Literal["e"],
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["inner"],
        left_on: Literal["d"],
        right_on: Literal["a"],
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["inner"],
        left_on: Literal["e"],
        right_on: Literal["b"],
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["inner"],
        left_on: List[Literal["b", "a"]],
        right_on: List[Literal["e", "d"]],
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["outer"],
        left_on: Literal["a"],
        right_on: Literal["d"],
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["outer"],
        left_on: Literal["b"],
        right_on: Literal["e"],
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["outer"],
        left_on: Literal["d"],
        right_on: Literal["a"],
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["outer"],
        left_on: Literal["e"],
        right_on: Literal["b"],
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["outer"],
        left_on: List[Literal["b", "a"]],
        right_on: List[Literal["e", "d"]],
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["left"],
        left_on: Literal["a"],
        right_on: Literal["d"],
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["left"],
        left_on: Literal["b"],
        right_on: Literal["e"],
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["left"],
        left_on: Literal["d"],
        right_on: Literal["a"],
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["left"],
        left_on: Literal["e"],
        right_on: Literal["b"],
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["left"],
        left_on: List[Literal["b", "a"]],
        right_on: List[Literal["e", "d"]],
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["right"],
        left_on: Literal["a"],
        right_on: Literal["d"],
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["right"],
        left_on: Literal["b"],
        right_on: Literal["e"],
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["right"],
        left_on: Literal["d"],
        right_on: Literal["a"],
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["right"],
        left_on: Literal["e"],
        right_on: Literal["b"],
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["right"],
        left_on: List[Literal["b", "a"]],
        right_on: List[Literal["e", "d"]],
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["inner"],
        left_on: Literal["x"],
        right_on: Literal["x"],
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["inner"],
        on: Literal["x"],
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["left"],
        left_on: None,
        right_on: Literal["x"],
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["left"],
        right_on: Literal["x"],
        left_index: bool,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["left"],
        left_on: Literal["x"],
        right_on: None,
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["left"],
        left_on: Literal["x"],
        right_index: bool,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["right"],
        left_on: None,
        right_on: Literal["x"],
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["right"],
        right_on: Literal["x"],
        left_index: bool,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["right"],
        left_on: Literal["x"],
        right_on: None,
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["right"],
        left_on: Literal["x"],
        right_index: bool,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["inner"],
        left_on: None,
        right_on: Literal["x"],
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["inner"],
        right_on: Literal["x"],
        left_index: bool,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["inner"],
        left_on: Literal["x"],
        right_on: None,
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["inner"],
        left_on: Literal["x"],
        right_index: bool,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["inner"],
        left_on: Literal["B"],
        right_on: Literal["B"],
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["inner"],
        on: None,
        left_on: None,
        right_on: Literal["y"],
        left_index: bool,
        right_index: bool,
        suffixes: Tuple[Literal["_x"], Literal["_y"]],
        indicator: bool,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["left"],
        left_on: None,
        right_on: None,
        left_index: bool,
        right_index: bool,
        suffixes: List[Literal["r", ""]],
        indicator: bool,
    ):
        """
        usage.dask: 1
        """
        ...

    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: str,
        on: Union[None, List[Literal["idx", "k"]], Literal["x", "emp_id", "idx"]] = ...,
        left_on: Union[None, str, List[str]] = ...,
        right_on: Union[None, List[str], str] = ...,
        left_index: bool = ...,
        right_index: bool = ...,
        suffixes: Union[
            List[Literal["_r", "_l", "", "r", "l"]],
            Tuple[Literal["_x", "1"], Literal["_y", "2"]],
        ] = ...,
        indicator: bool = ...,
    ):
        """
        usage.dask: 306
        """
        ...

    @overload
    def min(self, /, axis: int, skipna: bool):
        """
        usage.dask: 3
        """
        ...

    @overload
    def min(self, /):
        """
        usage.dask: 4
        """
        ...

    @overload
    def min(self, /, axis: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def min(self, /, axis: Literal["index"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def min(self, /, axis: Literal["columns"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def min(self, /, skipna: bool):
        """
        usage.dask: 2
        """
        ...

    def min(
        self, /, axis: Union[Literal["columns", "index"], int] = ..., skipna: bool = ...
    ):
        """
        usage.dask: 12
        """
        ...

    @overload
    def mod(self, /, other: pandas.core.frame.DataFrame, fill_value: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def mod(self, /, other: int, fill_value: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def mod(self, /, other: pandas.core.series.Series, axis: int):
        """
        usage.dask: 2
        """
        ...

    @overload
    def mod(self, /, other: pandas.core.frame.DataFrame, axis: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def mod(self, /, other: pandas.core.frame.DataFrame, axis: Literal["index"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def mod(self, /, other: pandas.core.frame.DataFrame, axis: Literal["columns"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def mod(self, /, other: pandas.core.series.Series, axis: Literal["index"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def mod(self, /, other: pandas.core.series.Series, axis: Literal["columns"]):
        """
        usage.dask: 1
        """
        ...

    def mod(
        self,
        /,
        other: Union[pandas.core.series.Series, pandas.core.frame.DataFrame, int],
        axis: Union[Literal["columns", "index"], int] = ...,
        fill_value: int = ...,
    ):
        """
        usage.dask: 9
        """
        ...

    def mode(self, /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def mul(self, /, other: pandas.core.frame.DataFrame, fill_value: int):
        """
        usage.dask: 2
        """
        ...

    @overload
    def mul(self, /, other: int, fill_value: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def mul(self, /, other: pandas.core.series.Series, axis: int):
        """
        usage.dask: 2
        """
        ...

    @overload
    def mul(self, /, other: pandas.core.frame.DataFrame, axis: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def mul(self, /, other: pandas.core.frame.DataFrame, axis: Literal["index"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def mul(self, /, other: pandas.core.frame.DataFrame, axis: Literal["columns"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def mul(self, /, other: pandas.core.series.Series, axis: Literal["index"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def mul(self, /, other: pandas.core.series.Series, axis: Literal["columns"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def mul(self, /, other: pandas.core.frame.DataFrame):
        """
        usage.dask: 1
        """
        ...

    def mul(
        self,
        /,
        other: Union[pandas.core.frame.DataFrame, int, pandas.core.series.Series],
        axis: Union[Literal["columns", "index"], int] = ...,
        fill_value: int = ...,
    ):
        """
        usage.dask: 11
        """
        ...

    @overload
    def nlargest(self, /, n: int, columns: Literal["a"]):
        """
        usage.dask: 2
        """
        ...

    @overload
    def nlargest(self, /, n: int, columns: List[Literal["c", "a"]]):
        """
        usage.dask: 2
        """
        ...

    def nlargest(
        self, /, n: int, columns: Union[List[Literal["c", "a"]], Literal["a"]]
    ):
        """
        usage.dask: 4
        """
        ...

    def notnull(self, /):
        """
        usage.dask: 2
        """
        ...

    @overload
    def nsmallest(self, /, n: int, columns: Literal["a"]):
        """
        usage.dask: 2
        """
        ...

    @overload
    def nsmallest(self, /, n: int, columns: List[Literal["c", "a"]]):
        """
        usage.dask: 2
        """
        ...

    def nsmallest(
        self, /, n: int, columns: Union[List[Literal["c", "a"]], Literal["a"]]
    ):
        """
        usage.dask: 4
        """
        ...

    @overload
    def pivot_table(
        self,
        /,
        values: Literal["B"],
        index: Literal["A"],
        columns: Literal["C"],
        aggfunc: Literal["mean"],
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def pivot_table(
        self,
        /,
        values: Literal["B"],
        index: Literal["A"],
        columns: Literal["C"],
        aggfunc: Literal["sum"],
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def pivot_table(
        self,
        /,
        values: Literal["B"],
        index: Literal["A"],
        columns: Literal["C"],
        aggfunc: Literal["count"],
    ):
        """
        usage.dask: 1
        """
        ...

    def pivot_table(
        self,
        /,
        values: Literal["B"],
        index: Literal["A"],
        columns: Literal["C"],
        aggfunc: Literal["count", "sum", "mean"],
    ):
        """
        usage.dask: 3
        """
        ...

    @overload
    def pow(self, /, other: pandas.core.frame.DataFrame, fill_value: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def pow(self, /, other: int, fill_value: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def pow(self, /, other: pandas.core.series.Series, axis: int):
        """
        usage.dask: 2
        """
        ...

    @overload
    def pow(self, /, other: pandas.core.frame.DataFrame, axis: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def pow(self, /, other: pandas.core.frame.DataFrame, axis: Literal["index"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def pow(self, /, other: pandas.core.frame.DataFrame, axis: Literal["columns"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def pow(self, /, other: pandas.core.series.Series, axis: Literal["index"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def pow(self, /, other: pandas.core.series.Series, axis: Literal["columns"]):
        """
        usage.dask: 1
        """
        ...

    def pow(
        self,
        /,
        other: Union[pandas.core.series.Series, pandas.core.frame.DataFrame, int],
        axis: Union[Literal["columns", "index"], int] = ...,
        fill_value: int = ...,
    ):
        """
        usage.dask: 9
        """
        ...

    @overload
    def prod(self, /, axis: int, skipna: bool):
        """
        usage.dask: 3
        """
        ...

    @overload
    def prod(self, /):
        """
        usage.dask: 4
        """
        ...

    @overload
    def prod(self, /, axis: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def prod(self, /, axis: Literal["index"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def prod(self, /, axis: Literal["columns"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def prod(self, /, skipna: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def prod(self, /, axis: int, min_count: int):
        """
        usage.dask: 1
        """
        ...

    def prod(
        self,
        /,
        axis: Union[int, Literal["columns", "index"]] = ...,
        min_count: int = ...,
        skipna: bool = ...,
    ):
        """
        usage.dask: 12
        """
        ...

    @overload
    def quantile(self, /, q: List[float], axis: int):
        """
        usage.dask: 2
        """
        ...

    @overload
    def quantile(self, /, q: List[numpy.float64], axis: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def quantile(self, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def quantile(self, /, q: float, axis: int):
        """
        usage.dask: 2
        """
        ...

    @overload
    def quantile(self, /, axis: int):
        """
        usage.dask: 1
        """
        ...

    def quantile(
        self,
        /,
        q: Union[List[Union[float, numpy.float64]], float] = ...,
        axis: int = ...,
    ):
        """
        usage.dask: 7
        """
        ...

    @overload
    def query(self, /, expr: Literal["B != 0"]):
        """
        usage.dask: 2
        """
        ...

    @overload
    def query(self, /, expr: Literal["B != 9"]):
        """
        usage.dask: 2
        """
        ...

    def query(self, /, expr: Literal["B != 9", "B != 0"]):
        """
        usage.dask: 4
        """
        ...

    @overload
    def radd(self, /, other: pandas.core.frame.DataFrame, fill_value: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def radd(self, /, other: int, fill_value: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def radd(self, /, other: pandas.core.series.Series, axis: int):
        """
        usage.dask: 2
        """
        ...

    @overload
    def radd(self, /, other: pandas.core.frame.DataFrame, axis: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def radd(self, /, other: pandas.core.frame.DataFrame, axis: Literal["index"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def radd(self, /, other: pandas.core.frame.DataFrame, axis: Literal["columns"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def radd(self, /, other: pandas.core.series.Series, axis: Literal["index"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def radd(self, /, other: pandas.core.series.Series, axis: Literal["columns"]):
        """
        usage.dask: 1
        """
        ...

    def radd(
        self,
        /,
        other: Union[pandas.core.series.Series, pandas.core.frame.DataFrame, int],
        axis: Union[Literal["columns", "index"], int] = ...,
        fill_value: int = ...,
    ):
        """
        usage.dask: 9
        """
        ...

    @overload
    def reindex(self, /, labels: pandas.core.indexes.multi.MultiIndex):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def reindex(self, /, labels: reversed):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def reindex(self, /, columns: pandas.core.indexes.base.Index):
        """
        usage.dask: 1
        """
        ...

    @overload
    def reindex(self, /, labels: List[str]):
        """
        usage.dask: 3
        """
        ...

    @overload
    def reindex(
        self, /, labels: pandas.core.indexes.numeric.Int64Index, fill_value: int
    ):
        """
        usage.dask: 3
        """
        ...

    @overload
    def reindex(self, /, labels: pandas.core.indexes.multi.MultiIndex, fill_value: int):
        """
        usage.dask: 3
        """
        ...

    @overload
    def reindex(
        self, /, labels: pandas.core.indexes.datetimes.DatetimeIndex, fill_value: float
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def reindex(
        self, /, labels: pandas.core.indexes.datetimes.DatetimeIndex, fill_value: int
    ):
        """
        usage.dask: 1
        """
        ...

    def reindex(
        self,
        /,
        labels: Union[
            List[str],
            pandas.core.indexes.numeric.Int64Index,
            pandas.core.indexes.multi.MultiIndex,
            pandas.core.indexes.datetimes.DatetimeIndex,
            reversed,
        ] = ...,
        fill_value: Union[int, float] = ...,
    ):
        """
        usage.dask: 12
        usage.xarray: 2
        """
        ...

    @overload
    def rename(self, /, columns: Dict[Literal["b", "a"], int]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rename(self, /, columns: Dict[Literal["y"], Literal["y_"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rename(self, /, mapper: None, columns: Dict[Literal["y"], Literal["y_"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rename(
        self, /, mapper: None, columns: Dict[Literal["b", "a"], Literal["B", "A"]]
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rename(self, /, columns: Dict[Literal["b", "a"], Literal["B", "A"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rename(self, /, mapper: None, columns: Callable):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rename(self, /, columns: Callable):
        """
        usage.dask: 6
        """
        ...

    @overload
    def rename(self, /, mapper: None, columns: Dict[Literal["B"], Literal["C"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rename(self, /, columns: Dict[Literal["B"], Literal["C"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rename(self, /, columns: collections.OrderedDict):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rename(
        self,
        /,
        mapper: None,
        columns: Dict[Literal["twos", "ones"], Literal["bar", "foo"]],
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rename(self, /, columns: Dict[Literal["A"], int]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rename(self, /, columns: Dict[Literal["F"], int]):
        """
        usage.dask: 1
        """
        ...

    def rename(
        self,
        /,
        columns: Union[Dict[str, Union[int, str]], collections.OrderedDict, Callable],
        mapper: None = ...,
    ):
        """
        usage.dask: 18
        """
        ...

    @overload
    def rename_axis(self, /, mapper: Literal["newindex"]):
        """
        usage.dask: 2
        """
        ...

    @overload
    def rename_axis(self, /, mapper: List[None], copy: bool):
        """
        usage.dask: 2
        """
        ...

    @overload
    def rename_axis(self, /, mapper: None):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rename_axis(self, /, mapper: Literal["myindex"]):
        """
        usage.dask: 1
        """
        ...

    def rename_axis(
        self,
        /,
        mapper: Union[Literal["myindex", "newindex"], List[None], None],
        copy: bool = ...,
    ):
        """
        usage.dask: 6
        """
        ...

    @overload
    def replace(self, /, to_replace: int, value: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def replace(self, /, to_replace: int, value: int, regex: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def replace(self, /, to_replace: Dict[int, int]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def replace(self, /, to_replace: Dict[int, int], value: None, regex: bool):
        """
        usage.dask: 1
        """
        ...

    def replace(
        self,
        /,
        to_replace: Union[Dict[int, int], int],
        value: Union[None, int] = ...,
        regex: bool = ...,
    ):
        """
        usage.dask: 4
        """
        ...

    @overload
    def resample(
        self,
        /,
        rule: pandas._libs.tslibs.offsets.Minute,
        closed: Literal["right"],
        label: Literal["right"],
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def resample(
        self, /, rule: Literal["30T"], closed: Literal["right"], label: Literal["right"]
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def resample(
        self,
        /,
        rule: pandas._libs.tslibs.offsets.Minute,
        closed: Literal["right"],
        label: Literal["left"],
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def resample(
        self, /, rule: Literal["30T"], closed: Literal["right"], label: Literal["left"]
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def resample(
        self,
        /,
        rule: pandas._libs.tslibs.offsets.Minute,
        closed: Literal["left"],
        label: Literal["right"],
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def resample(
        self, /, rule: Literal["30T"], closed: Literal["left"], label: Literal["right"]
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def resample(
        self,
        /,
        rule: pandas._libs.tslibs.offsets.Minute,
        closed: Literal["left"],
        label: Literal["left"],
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def resample(
        self, /, rule: Literal["30T"], closed: Literal["left"], label: Literal["left"]
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def resample(
        self,
        /,
        rule: pandas._libs.tslibs.offsets.Hour,
        closed: Literal["right"],
        label: Literal["right"],
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def resample(
        self, /, rule: Literal["h"], closed: Literal["right"], label: Literal["right"]
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def resample(
        self,
        /,
        rule: pandas._libs.tslibs.offsets.Hour,
        closed: Literal["right"],
        label: Literal["left"],
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def resample(
        self, /, rule: Literal["h"], closed: Literal["right"], label: Literal["left"]
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def resample(
        self,
        /,
        rule: pandas._libs.tslibs.offsets.Hour,
        closed: Literal["left"],
        label: Literal["right"],
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def resample(
        self, /, rule: Literal["h"], closed: Literal["left"], label: Literal["right"]
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def resample(
        self,
        /,
        rule: pandas._libs.tslibs.offsets.Hour,
        closed: Literal["left"],
        label: Literal["left"],
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def resample(
        self, /, rule: Literal["h"], closed: Literal["left"], label: Literal["left"]
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def resample(
        self,
        /,
        rule: pandas._libs.tslibs.offsets.Day,
        closed: Literal["right"],
        label: Literal["right"],
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def resample(
        self, /, rule: Literal["d"], closed: Literal["right"], label: Literal["right"]
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def resample(
        self,
        /,
        rule: pandas._libs.tslibs.offsets.Day,
        closed: Literal["right"],
        label: Literal["left"],
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def resample(
        self, /, rule: Literal["d"], closed: Literal["right"], label: Literal["left"]
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def resample(
        self,
        /,
        rule: pandas._libs.tslibs.offsets.Day,
        closed: Literal["left"],
        label: Literal["right"],
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def resample(
        self, /, rule: Literal["d"], closed: Literal["left"], label: Literal["right"]
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def resample(
        self,
        /,
        rule: pandas._libs.tslibs.offsets.Day,
        closed: Literal["left"],
        label: Literal["left"],
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def resample(
        self, /, rule: Literal["d"], closed: Literal["left"], label: Literal["left"]
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def resample(
        self,
        /,
        rule: pandas._libs.tslibs.offsets.Week,
        closed: Literal["right"],
        label: Literal["right"],
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def resample(
        self, /, rule: Literal["w"], closed: Literal["right"], label: Literal["right"]
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def resample(
        self,
        /,
        rule: pandas._libs.tslibs.offsets.Week,
        closed: Literal["right"],
        label: Literal["left"],
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def resample(
        self, /, rule: Literal["w"], closed: Literal["right"], label: Literal["left"]
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def resample(
        self,
        /,
        rule: pandas._libs.tslibs.offsets.Week,
        closed: Literal["left"],
        label: Literal["right"],
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def resample(
        self, /, rule: Literal["w"], closed: Literal["left"], label: Literal["right"]
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def resample(
        self,
        /,
        rule: pandas._libs.tslibs.offsets.Week,
        closed: Literal["left"],
        label: Literal["left"],
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def resample(
        self, /, rule: Literal["w"], closed: Literal["left"], label: Literal["left"]
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def resample(
        self,
        /,
        rule: pandas._libs.tslibs.offsets.MonthEnd,
        closed: Literal["right"],
        label: Literal["right"],
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def resample(
        self, /, rule: Literal["M"], closed: Literal["right"], label: Literal["right"]
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def resample(
        self,
        /,
        rule: pandas._libs.tslibs.offsets.MonthEnd,
        closed: Literal["right"],
        label: Literal["left"],
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def resample(
        self, /, rule: Literal["M"], closed: Literal["right"], label: Literal["left"]
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def resample(
        self,
        /,
        rule: pandas._libs.tslibs.offsets.MonthEnd,
        closed: Literal["left"],
        label: Literal["right"],
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def resample(
        self, /, rule: Literal["M"], closed: Literal["left"], label: Literal["right"]
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def resample(
        self,
        /,
        rule: pandas._libs.tslibs.offsets.MonthEnd,
        closed: Literal["left"],
        label: Literal["left"],
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def resample(
        self, /, rule: Literal["M"], closed: Literal["left"], label: Literal["left"]
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def resample(self, /, rule: Literal["1Q"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def resample(
        self, /, rule: pandas._libs.tslibs.offsets.QuarterEnd, closed: None, label: None
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def resample(self, /, rule: Literal["2D"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def resample(
        self, /, rule: pandas._libs.tslibs.offsets.Day, closed: None, label: None
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def resample(self, /, rule: Literal["1D"]):
        """
        usage.dask: 1
        """
        ...

    def resample(
        self,
        /,
        rule: object,
        closed: Union[None, Literal["left", "right"]] = ...,
        label: Union[None, Literal["left", "right"]] = ...,
    ):
        """
        usage.dask: 66
        """
        ...

    @overload
    def reset_index(self, /, drop: bool):
        """
        usage.dask: 24
        """
        ...

    @overload
    def reset_index(self, /):
        """
        usage.dask: 3
        """
        ...

    @overload
    def reset_index(self, /, level: int, drop: bool):
        """
        usage.dask: 2
        """
        ...

    def reset_index(self, /, level: int = ..., drop: bool = ...):
        """
        usage.dask: 29
        """
        ...

    @overload
    def rmod(self, /, other: pandas.core.frame.DataFrame, fill_value: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rmod(self, /, other: int, fill_value: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rmod(self, /, other: pandas.core.series.Series, axis: int):
        """
        usage.dask: 2
        """
        ...

    @overload
    def rmod(self, /, other: pandas.core.frame.DataFrame, axis: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rmod(self, /, other: pandas.core.frame.DataFrame, axis: Literal["index"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rmod(self, /, other: pandas.core.frame.DataFrame, axis: Literal["columns"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rmod(self, /, other: pandas.core.series.Series, axis: Literal["index"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rmod(self, /, other: pandas.core.series.Series, axis: Literal["columns"]):
        """
        usage.dask: 1
        """
        ...

    def rmod(
        self,
        /,
        other: Union[pandas.core.series.Series, pandas.core.frame.DataFrame, int],
        axis: Union[Literal["columns", "index"], int] = ...,
        fill_value: int = ...,
    ):
        """
        usage.dask: 9
        """
        ...

    @overload
    def rmul(self, /, other: pandas.core.frame.DataFrame, fill_value: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rmul(self, /, other: int, fill_value: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rmul(self, /, other: pandas.core.series.Series, axis: int):
        """
        usage.dask: 2
        """
        ...

    @overload
    def rmul(self, /, other: pandas.core.frame.DataFrame, axis: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rmul(self, /, other: pandas.core.frame.DataFrame, axis: Literal["index"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rmul(self, /, other: pandas.core.frame.DataFrame, axis: Literal["columns"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rmul(self, /, other: pandas.core.series.Series, axis: Literal["index"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rmul(self, /, other: pandas.core.series.Series, axis: Literal["columns"]):
        """
        usage.dask: 1
        """
        ...

    def rmul(
        self,
        /,
        other: Union[pandas.core.series.Series, pandas.core.frame.DataFrame, int],
        axis: Union[Literal["columns", "index"], int] = ...,
        fill_value: int = ...,
    ):
        """
        usage.dask: 9
        """
        ...

    @overload
    def rolling(self, /, window: int, min_periods: None, center: bool):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def rolling(self, /, window: int, min_periods: int, center: bool):
        """
        usage.xarray: 2
        """
        ...

    @overload
    def rolling(self, /, window: int):
        """
        usage.dask: 10
        """
        ...

    @overload
    def rolling(self, /, window: int, center: bool):
        """
        usage.dask: 2
        """
        ...

    @overload
    def rolling(
        self, /, window: int, min_periods: None, center: bool, win_type: None, axis: int
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def rolling(
        self,
        /,
        window: float,
        min_periods: None,
        center: bool,
        win_type: None,
        axis: int,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rolling(
        self,
        /,
        window: int,
        min_periods: None,
        center: bool,
        win_type: None,
        axis: Literal["coulombs"],
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rolling(self, /, window: int, axis: int):
        """
        usage.dask: 2
        """
        ...

    @overload
    def rolling(self, /, window: int, min_periods: int, axis: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rolling(
        self, /, window: int, min_periods: int, center: bool, win_type: None, axis: int
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def rolling(self, /, window: int, axis: Literal["columns"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rolling(
        self,
        /,
        window: int,
        min_periods: None,
        center: bool,
        win_type: None,
        axis: Literal["columns"],
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def rolling(self, /, window: int, axis: Literal["rows"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rolling(
        self,
        /,
        window: int,
        min_periods: None,
        center: bool,
        win_type: None,
        axis: Literal["rows"],
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def rolling(
        self,
        /,
        window: Literal["4s"],
        min_periods: None,
        center: bool,
        win_type: None,
        axis: int,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rolling(self, /, window: Literal["1S"]):
        """
        usage.dask: 2
        """
        ...

    @overload
    def rolling(
        self,
        /,
        window: Literal["1S"],
        min_periods: None,
        center: bool,
        win_type: None,
        axis: int,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def rolling(self, /, window: Literal["2S"]):
        """
        usage.dask: 2
        """
        ...

    @overload
    def rolling(
        self,
        /,
        window: Literal["2S"],
        min_periods: None,
        center: bool,
        win_type: None,
        axis: int,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def rolling(self, /, window: Literal["3S"]):
        """
        usage.dask: 2
        """
        ...

    @overload
    def rolling(
        self,
        /,
        window: Literal["3S"],
        min_periods: None,
        center: bool,
        win_type: None,
        axis: int,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def rolling(self, /, window: pandas._libs.tslibs.offsets.Second):
        """
        usage.dask: 2
        """
        ...

    @overload
    def rolling(
        self,
        /,
        window: pandas._libs.tslibs.offsets.Second,
        min_periods: None,
        center: bool,
        win_type: None,
        axis: int,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def rolling(
        self,
        /,
        window: Literal["1s"],
        min_periods: None,
        center: bool,
        win_type: None,
        axis: int,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def rolling(self, /, window: Literal["1s"]):
        """
        usage.dask: 3
        """
        ...

    @overload
    def rolling(
        self,
        /,
        window: Literal["2s"],
        min_periods: None,
        center: bool,
        win_type: None,
        axis: int,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def rolling(self, /, window: Literal["2s"]):
        """
        usage.dask: 8
        """
        ...

    @overload
    def rolling(
        self,
        /,
        window: Literal["10s"],
        min_periods: None,
        center: bool,
        win_type: None,
        axis: int,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def rolling(self, /, window: Literal["10s"]):
        """
        usage.dask: 3
        """
        ...

    @overload
    def rolling(
        self,
        /,
        window: Literal["10h"],
        min_periods: None,
        center: bool,
        win_type: None,
        axis: int,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def rolling(self, /, window: Literal["10h"]):
        """
        usage.dask: 6
        """
        ...

    @overload
    def rolling(
        self,
        /,
        window: Literal["5s"],
        min_periods: None,
        center: bool,
        win_type: None,
        axis: int,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def rolling(self, /, window: Literal["5s"]):
        """
        usage.dask: 3
        """
        ...

    @overload
    def rolling(
        self,
        /,
        window: Literal["20s"],
        min_periods: None,
        center: bool,
        win_type: None,
        axis: int,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def rolling(self, /, window: Literal["20s"]):
        """
        usage.dask: 3
        """
        ...

    @overload
    def rolling(self, /, window: Literal["6s"]):
        """
        usage.dask: 2
        """
        ...

    def rolling(
        self,
        /,
        window: Union[pandas._libs.tslibs.offsets.Second, float, int, str],
        min_periods: Union[int, None] = ...,
        center: bool = ...,
        win_type: None = ...,
        axis: Union[int, Literal["rows", "columns", "coulombs"]] = ...,
    ):
        """
        usage.dask: 84
        usage.xarray: 3
        """
        ...

    @overload
    def round(self, /, decimals: int):
        """
        usage.dask: 2
        """
        ...

    @overload
    def round(self, /):
        """
        usage.dask: 1
        """
        ...

    def round(self, /, decimals: int = ...):
        """
        usage.dask: 3
        """
        ...

    @overload
    def rpow(self, /, other: pandas.core.frame.DataFrame, fill_value: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rpow(self, /, other: int, fill_value: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rpow(self, /, other: pandas.core.series.Series, axis: int):
        """
        usage.dask: 2
        """
        ...

    @overload
    def rpow(self, /, other: pandas.core.frame.DataFrame, axis: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rpow(self, /, other: pandas.core.frame.DataFrame, axis: Literal["index"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rpow(self, /, other: pandas.core.frame.DataFrame, axis: Literal["columns"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rpow(self, /, other: pandas.core.series.Series, axis: Literal["index"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rpow(self, /, other: pandas.core.series.Series, axis: Literal["columns"]):
        """
        usage.dask: 1
        """
        ...

    def rpow(
        self,
        /,
        other: Union[pandas.core.series.Series, pandas.core.frame.DataFrame, int],
        axis: Union[Literal["columns", "index"], int] = ...,
        fill_value: int = ...,
    ):
        """
        usage.dask: 9
        """
        ...

    @overload
    def rsub(self, /, other: pandas.core.frame.DataFrame, fill_value: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rsub(self, /, other: int, fill_value: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rsub(self, /, other: pandas.core.series.Series, axis: int):
        """
        usage.dask: 2
        """
        ...

    @overload
    def rsub(self, /, other: pandas.core.frame.DataFrame, axis: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rsub(self, /, other: pandas.core.frame.DataFrame, axis: Literal["index"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rsub(self, /, other: pandas.core.frame.DataFrame, axis: Literal["columns"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rsub(self, /, other: pandas.core.series.Series, axis: Literal["index"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def rsub(self, /, other: pandas.core.series.Series, axis: Literal["columns"]):
        """
        usage.dask: 1
        """
        ...

    def rsub(
        self,
        /,
        other: Union[pandas.core.series.Series, pandas.core.frame.DataFrame, int],
        axis: Union[Literal["columns", "index"], int] = ...,
        fill_value: int = ...,
    ):
        """
        usage.dask: 9
        """
        ...

    @overload
    def rtruediv(self, /, other: pandas.core.frame.DataFrame, fill_value: int):
        """
        usage.dask: 2
        """
        ...

    @overload
    def rtruediv(self, /, other: int, fill_value: int):
        """
        usage.dask: 2
        """
        ...

    @overload
    def rtruediv(self, /, other: pandas.core.series.Series, axis: int):
        """
        usage.dask: 4
        """
        ...

    @overload
    def rtruediv(self, /, other: pandas.core.frame.DataFrame, axis: int):
        """
        usage.dask: 2
        """
        ...

    @overload
    def rtruediv(self, /, other: pandas.core.frame.DataFrame, axis: Literal["index"]):
        """
        usage.dask: 2
        """
        ...

    @overload
    def rtruediv(self, /, other: pandas.core.frame.DataFrame, axis: Literal["columns"]):
        """
        usage.dask: 2
        """
        ...

    @overload
    def rtruediv(self, /, other: pandas.core.series.Series, axis: Literal["index"]):
        """
        usage.dask: 2
        """
        ...

    @overload
    def rtruediv(self, /, other: pandas.core.series.Series, axis: Literal["columns"]):
        """
        usage.dask: 2
        """
        ...

    def rtruediv(
        self,
        /,
        other: Union[pandas.core.series.Series, pandas.core.frame.DataFrame, int],
        axis: Union[Literal["columns", "index"], int] = ...,
        fill_value: int = ...,
    ):
        """
        usage.dask: 18
        """
        ...

    @overload
    def sample(self, /, frac: float, random_state: numpy.random.mtrand.RandomState):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sample(
        self,
        /,
        frac: float,
        replace: bool,
        random_state: numpy.random.mtrand.RandomState,
    ):
        """
        usage.dask: 1
        """
        ...

    def sample(
        self,
        /,
        frac: float,
        random_state: numpy.random.mtrand.RandomState,
        replace: bool = ...,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def select_dtypes(self, /, include: List[Literal["category"]]):
        """
        usage.dask: 2
        """
        ...

    @overload
    def select_dtypes(self, /, include: List[Type[numpy.timedelta64]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def select_dtypes(
        self,
        /,
        include: List[Literal["bool", "number"]],
        exclude: List[Type[numpy.timedelta64]],
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def select_dtypes(self, /, include: List[Literal["category", "object"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def select_dtypes(self, /, include: List[type]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def select_dtypes(
        self, /, include: List[Union[Literal["bool"], Type[numpy.timedelta64]]]
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def select_dtypes(self, /, include: List[Literal["number"]], exclude: None):
        """
        usage.dask: 1
        """
        ...

    @overload
    def select_dtypes(self, /, include: List[Type[numpy.timedelta64]], exclude: None):
        """
        usage.dask: 1
        """
        ...

    @overload
    def select_dtypes(
        self, /, include: List[Literal["object", "number"]], exclude: None
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def select_dtypes(
        self, /, include: None, exclude: List[Literal["object", "number"]]
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def select_dtypes(
        self, /, include: List[Literal["bool", "datetime", "object"]], exclude: None
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def select_dtypes(self, /, include: List[Type[int]], exclude: None):
        """
        usage.dask: 2
        usage.sklearn: 1
        """
        ...

    @overload
    def select_dtypes(self, /, include: None, exclude: List[Type[int]]):
        """
        usage.dask: 2
        usage.sklearn: 1
        """
        ...

    @overload
    def select_dtypes(self, /, include: List[type], exclude: List[Type[float]]):
        """
        usage.dask: 2
        """
        ...

    @overload
    def select_dtypes(self, /, include: List[Literal["datetime"]], exclude: None):
        """
        usage.dask: 2
        """
        ...

    @overload
    def select_dtypes(self, /, include: Type[numpy.number], exclude: None):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def select_dtypes(self, /, include: None, exclude: Type[object]):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def select_dtypes(self, /, include: List[type], exclude: None):
        """
        usage.sklearn: 2
        """
        ...

    @overload
    def select_dtypes(self, /, include: List[Type[object]], exclude: None):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def select_dtypes(self, /, include: Type[object], exclude: None):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def select_dtypes(self, /, include: Type[float], exclude: None):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def select_dtypes(self, /, include: List[Type[numpy.number]], exclude: None):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def select_dtypes(
        self, /, include: List[Union[Type[object], Literal["category"]]], exclude: None
    ):
        """
        usage.sklearn: 1
        """
        ...

    def select_dtypes(
        self,
        /,
        include: Union[
            type,
            None,
            List[
                Union[Literal["category", "bool", "number", "object", "datetime"], type]
            ],
        ],
        exclude: Union[
            Type[object],
            List[Union[type, Type[int], Literal["object", "number"]]],
            None,
        ] = ...,
    ):
        """
        usage.dask: 20
        usage.sklearn: 11
        """
        ...

    @overload
    def sem(self, /, axis: int, skipna: None, ddof: int):
        """
        usage.dask: 2
        """
        ...

    @overload
    def sem(self, /):
        """
        usage.dask: 4
        """
        ...

    @overload
    def sem(self, /, ddof: int):
        """
        usage.dask: 3
        """
        ...

    @overload
    def sem(self, /, axis: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sem(self, /, axis: int, ddof: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sem(self, /, axis: Literal["index"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sem(self, /, axis: Literal["index"], ddof: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sem(self, /, axis: Literal["columns"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sem(self, /, axis: Literal["columns"], ddof: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sem(self, /, skipna: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sem(self, /, axis: int, skipna: bool, ddof: int):
        """
        usage.dask: 3
        """
        ...

    @overload
    def sem(self, /, skipna: bool, ddof: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sem(self, /, axis: int, skipna: bool):
        """
        usage.dask: 1
        """
        ...

    def sem(
        self,
        /,
        axis: Union[int, Literal["columns", "index"]] = ...,
        skipna: Union[bool, None] = ...,
        ddof: int = ...,
    ):
        """
        usage.dask: 21
        """
        ...

    @overload
    def set_index(self, /, keys: List[Literal["y", "x"]]):
        """
        usage.xarray: 3
        """
        ...

    @overload
    def set_index(self, /, keys: pandas.core.indexes.multi.MultiIndex):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def set_index(self, /, keys: pandas.core.indexes.base.Index):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def set_index(self, /, keys: pandas.core.indexes.range.RangeIndex):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["ind"]):
        """
        usage.xarray: 2
        """
        ...

    @overload
    def set_index(self, /, keys: pandas.core.indexes.category.CategoricalIndex):
        """
        usage.dask: 2
        usage.xarray: 1
        """
        ...

    @overload
    def set_index(self, /, keys: List[Literal["i2", "i1"]]):
        """
        usage.xarray: 2
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["i1"]):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["x"]):
        """
        usage.dask: 11
        usage.xarray: 2
        """
        ...

    @overload
    def set_index(self, /, keys: pandas.core.indexes.numeric.Int64Index):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["amount"], drop: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["amount"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["Date"], drop: bool):
        """
        usage.dask: 3
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["date"], drop: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["idx"], drop: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def set_index(self, /, keys: pandas.core.series.Series):
        """
        usage.dask: 8
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["y"], drop: bool):
        """
        usage.dask: 3
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["_index"], drop: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["id"], drop: bool):
        """
        usage.dask: 2
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["x"], drop: bool):
        """
        usage.dask: 4
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["index"], drop: bool):
        """
        usage.dask: 2
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["idx"]):
        """
        usage.dask: 11
        """
        ...

    @overload
    def set_index(self, /, keys: pandas.core.indexes.datetimes.DatetimeIndex):
        """
        usage.dask: 1
        """
        ...

    @overload
    def set_index(self, /, keys: pandas.core.indexes.period.PeriodIndex):
        """
        usage.dask: 1
        """
        ...

    @overload
    def set_index(self, /, keys: pandas.core.indexes.timedeltas.TimedeltaIndex):
        """
        usage.dask: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["A"]):
        """
        usage.dask: 2
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["A"], drop: bool):
        """
        usage.dask: 4
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["a"], drop: bool):
        """
        usage.dask: 3
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["a"]):
        """
        usage.dask: 5
        """
        ...

    @overload
    def set_index(self, /, keys: List[Literal["a"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def set_index(self, /, keys: List[Literal["b", "a"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def set_index(self, /, keys: List[Literal["a", "idx"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def set_index(self, /, keys: List[Literal["idx", "a"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def set_index(self, /, keys: List[Literal["idx"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["group"]):
        """
        usage.dask: 5
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["index"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["time"], drop: bool):
        """
        usage.dask: 2
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["y"]):
        """
        usage.dask: 2
        """
        ...

    @overload
    def set_index(self, /, keys: pandas.core.series.Series, drop: bool):
        """
        usage.dask: 7
        """
        ...

    @overload
    def set_index(self, /, keys: pandas.core.indexes.numeric.Float64Index):
        """
        usage.dask: 2
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["name"], drop: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["b"], drop: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["b"]):
        """
        usage.dask: 6
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["timestamp"], drop: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def set_index(self, /, keys: List[Literal["b"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["notz"], drop: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["tz"], drop: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["B"], drop: bool):
        """
        usage.dask: 3
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["C"], drop: bool):
        """
        usage.dask: 2
        """
        ...

    @overload
    def set_index(self, /, keys: int, drop: bool):
        """
        usage.dask: 3
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["c"], drop: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["c"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["key"], drop: bool):
        """
        usage.dask: 2
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["Time"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["Time"], drop: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["date"]):
        """
        usage.dask: 1
        """
        ...

    def set_index(self, /, keys: object, drop: bool = ...):
        """
        usage.dask: 119
        usage.xarray: 15
        """
        ...

    @overload
    def shift(self, /, periods: int):
        """
        usage.dask: 6
        """
        ...

    @overload
    def shift(self, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def shift(self, /, periods: int, freq: None, axis: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def shift(self, /, periods: int, axis: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def shift(self, /, periods: int, freq: Literal["S"]):
        """
        usage.dask: 4
        """
        ...

    @overload
    def shift(self, /, periods: int, freq: Literal["W"]):
        """
        usage.dask: 3
        """
        ...

    @overload
    def shift(self, /, periods: int, freq: pandas._libs.tslibs.timedeltas.Timedelta):
        """
        usage.dask: 4
        """
        ...

    @overload
    def shift(self, /, periods: int, freq: Literal["B"]):
        """
        usage.dask: 3
        """
        ...

    @overload
    def shift(self, /, periods: int, freq: Literal["D"]):
        """
        usage.dask: 3
        """
        ...

    @overload
    def shift(self, /, periods: int, freq: Literal["H"]):
        """
        usage.dask: 3
        """
        ...

    def shift(
        self,
        /,
        periods: int = ...,
        freq: Union[
            Literal["H", "D", "B", "W", "S"],
            None,
            pandas._libs.tslibs.timedeltas.Timedelta,
        ] = ...,
        axis: int = ...,
    ):
        """
        usage.dask: 29
        """
        ...

    @overload
    def sort_index(self, /):
        """
        usage.dask: 7
        """
        ...

    @overload
    def sort_index(self, /, ascending: bool):
        """
        usage.dask: 1
        """
        ...

    def sort_index(self, /, ascending: bool = ...):
        """
        usage.dask: 8
        """
        ...

    @overload
    def sort_values(self, /, by: List[int]):
        """
        usage.dask: 6
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["b", "a"]]):
        """
        usage.dask: 3
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["a"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["id", "amount", "name"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["id", "name"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["amount", "name"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["name"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["-500", "Edith"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["B", "A"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(
        self,
        /,
        by: List[Literal["dates", "integers", "more_numbers", "names", "numbers"]],
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(
        self, /, by: List[Literal["integers", "more_numbers", "names", "numbers"]]
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["Close"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["d", "c", "b", "a"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["c-d", "b", "a"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["y", "x"]]):
        """
        usage.dask: 3
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["x"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["Val", "Date"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["a", "b"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["D", "C", "B", "A"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["X", "C", "B", "A"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["X", "D", "C", "B", "A"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[str]):
        """
        usage.dask: 29
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["bool", "float", "int"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["A"]]):
        """
        usage.dask: 2
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["z", "x"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["z", "y_", "x", "w", "v"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["d", "c"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["f", "d", "c"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["f"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["f", "d", "c", "a"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["e", "d", "c", "b", "a"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["c", "b", "a"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["z", "y", "x"]]):
        """
        usage.dask: 3
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["C", "B", "A"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["D", "C", "B"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["C", "B"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["cint"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["cdt", "clfoat", "cstr"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["cstr", "cint"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["cdt"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["count", "sum"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["z", "y"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["foo"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["bar"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["col2", "col1"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["mean", "sum"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["x3", "x2"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["y", "x", "index"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["x", "index"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Union[Literal["y"], int]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["b", "a", "x"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Tuple[Literal["A", "B"], Literal["0", "1"]]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["B", "A", "C"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["y"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["Num", "Name"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["x", "y"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["b", "d", "a"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["b"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["c", "b"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["d"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["d", "c", "b"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["d", "b"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["D", "C", "B", "AA", "AB"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["D", "C", "B", "AB"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["b", "c"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["d", "b", "c"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["d", "a", "b", "c"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["a", "b", "c"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["c"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["max", "min"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Tuple[Literal["a"], Literal["min", "max"]]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Tuple[Literal["a", "b"], Literal["min", "max"]]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Tuple[Literal["b"], Literal["min", "max"]]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Tuple[Literal["b"], Literal["mean", "sum"]]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["mean"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["sum", "mean"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["z"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["y", "x", "id"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["val3", "val2", "val1"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[float]):
        """
        usage.dask: 2
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["3", "2", "1"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["b", "a", ""]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["value"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["y", "z"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["e", "c", "b"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["e"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["e", "c", "a"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["e", "b", "a"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["e", "c"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["e", "b"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["e", "a"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["E", "D", "C", "B", "A"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["B"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: list):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["C", "A"]]):
        """
        usage.dask: 2
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["num"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["A", "B"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["A", "C"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["B", "C"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["v1_y", "k_y", "v1_x", "k_x"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["v1_y", "v1_x", "k"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["z", "y_y", "y_x", "x"]]):
        """
        usage.dask: 3
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["right_val", "left_val"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["right_val", "left_val", "a"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["z", "y2", "y1", "x"]]):
        """
        usage.dask: 2
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["b", "a", "d", "c"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["value", "variable"]]):
        """
        usage.dask: 2
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["value", "variable", "C"]]):
        """
        usage.dask: 2
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["value", "myvar"]]):
        """
        usage.dask: 2
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["myval", "variable", "B"]]):
        """
        usage.dask: 2
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["z_y", "x_y", "z_x", "x_x", "x"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["z_y", "x_y", "z_x", "x_x"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["z", "x_y", "y", "x_x", "x"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["y", "x_y", "z", "x_x", "x"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["E", "D", "C"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["H", "G", "F"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["F"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["F", "A"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["H", "F"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Union[int, Literal["E", "D", "C", "B", "A"]]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["A", "E", "D", "C", "B"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Union[str, int]]):
        """
        usage.dask: 2
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["z", "y", "x", "w"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["z", "w", "y", "x"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["a", "c", "b"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["cluster", "user"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["b_d", "b_c", "b_b", "b_a", "a"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["X-4", "X-3", "X-2", "X-1"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["a_c", "a_b", "a_a"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["A_c", "A_b", "A_a", "B"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["e", "d", "c", "b"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(
        self, /, by: List[Tuple[Literal["A", "B"], Literal["mean", "std"]]]
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(
        self, /, by: List[Tuple[Literal["A", "B"], Literal["sum", "mean"]]]
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Tuple[Literal["A"], Literal["sum", "mean"]]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["c", "a"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["y", "x", "name", "id"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["close", "low", "high", "open"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(
        self, /, by: List[Tuple[Literal["a"], Literal["open", "high", "low", "close"]]]
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["min", "mean"]]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["p"]]):
        """
        usage.dask: 1
        """
        ...

    def sort_values(
        self,
        /,
        by: List[Union[Tuple[Literal["a", "A", "B", "b"], str], str, int, float]],
    ):
        """
        usage.dask: 190
        """
        ...

    def squeeze(self, /):
        """
        usage.dask: 3
        """
        ...

    @overload
    def stack(self, /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def stack(self, /, dropna: bool):
        """
        usage.dask: 1
        """
        ...

    def stack(self, /, dropna: bool = ...):
        """
        usage.dask: 1
        usage.xarray: 1
        """
        ...

    @overload
    def std(self, /, axis: int, skipna: bool):
        """
        usage.dask: 2
        """
        ...

    @overload
    def std(self, /, axis: int, skipna: bool, ddof: int):
        """
        usage.dask: 2
        """
        ...

    @overload
    def std(self, /):
        """
        usage.dask: 5
        """
        ...

    @overload
    def std(self, /, ddof: int):
        """
        usage.dask: 3
        """
        ...

    @overload
    def std(self, /, axis: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def std(self, /, axis: int, ddof: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def std(self, /, axis: Literal["index"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def std(self, /, axis: Literal["index"], ddof: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def std(self, /, axis: Literal["columns"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def std(self, /, axis: Literal["columns"], ddof: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def std(self, /, skipna: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def std(self, /, skipna: bool, ddof: int):
        """
        usage.dask: 1
        """
        ...

    def std(
        self,
        /,
        axis: Union[Literal["columns", "index"], int] = ...,
        skipna: bool = ...,
        ddof: int = ...,
    ):
        """
        usage.dask: 20
        """
        ...

    @overload
    def sub(self, /, other: pandas.core.frame.DataFrame, fill_value: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sub(self, /, other: int, fill_value: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sub(self, /, other: pandas.core.series.Series, axis: int):
        """
        usage.dask: 2
        """
        ...

    @overload
    def sub(self, /, other: pandas.core.frame.DataFrame, axis: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sub(self, /, other: pandas.core.frame.DataFrame, axis: Literal["index"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sub(self, /, other: pandas.core.frame.DataFrame, axis: Literal["columns"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sub(self, /, other: pandas.core.series.Series, axis: Literal["index"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sub(self, /, other: pandas.core.series.Series, axis: Literal["columns"]):
        """
        usage.dask: 1
        """
        ...

    def sub(
        self,
        /,
        other: Union[pandas.core.series.Series, pandas.core.frame.DataFrame, int],
        axis: Union[Literal["columns", "index"], int] = ...,
        fill_value: int = ...,
    ):
        """
        usage.dask: 9
        """
        ...

    @overload
    def sum(self, /, axis: int, skipna: bool):
        """
        usage.dask: 3
        """
        ...

    @overload
    def sum(self, /):
        """
        usage.dask: 19
        """
        ...

    @overload
    def sum(self, /, axis: int):
        """
        usage.dask: 3
        """
        ...

    @overload
    def sum(self, /, axis: Literal["index"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sum(self, /, axis: Literal["columns"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sum(self, /, skipna: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def sum(self, /, axis: int, min_count: int):
        """
        usage.dask: 1
        """
        ...

    def sum(
        self,
        /,
        axis: Union[int, Literal["columns", "index"]] = ...,
        min_count: int = ...,
        skipna: bool = ...,
    ):
        """
        usage.dask: 29
        """
        ...

    def tail(self, /, n: int):
        """
        usage.dask: 5
        """
        ...

    def take(self, /, indices: numpy.ndarray):
        """
        usage.dask: 1
        """
        ...

    @overload
    def to_csv(
        self,
        /,
        path_or_buf: Literal["/tmp/tmp12pxwjdr.csv"],
        index: bool,
        encoding: Literal["utf-16"],
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def to_csv(
        self,
        /,
        path_or_buf: Literal["/tmp/tmpigl0owvd.csv"],
        index: bool,
        encoding: Literal["utf-16-le"],
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def to_csv(
        self,
        /,
        path_or_buf: Literal["/tmp/tmpd3mrm6x7.csv"],
        index: bool,
        encoding: Literal["utf-16-be"],
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def to_csv(self, /, path_or_buf: _io.TextIOWrapper, index: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def to_csv(self, /, path_or_buf: _io.TextIOWrapper, header: bool, index: bool):
        """
        usage.dask: 1
        """
        ...

    def to_csv(
        self,
        /,
        path_or_buf: Union[
            _io.TextIOWrapper,
            Literal[
                "/tmp/tmpd3mrm6x7.csv", "/tmp/tmpigl0owvd.csv", "/tmp/tmp12pxwjdr.csv"
            ],
        ],
        index: bool,
        encoding: Literal["utf-16-be", "utf-16-le", "utf-16"] = ...,
        header: bool = ...,
    ):
        """
        usage.dask: 5
        """
        ...

    @overload
    def to_html(self, /, max_rows: int, show_dimensions: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def to_html(self, /, max_rows: int, show_dimensions: bool, notebook: bool):
        """
        usage.dask: 1
        """
        ...

    def to_html(self, /, max_rows: int, show_dimensions: bool, notebook: bool = ...):
        """
        usage.dask: 2
        """
        ...

    @overload
    def to_json(self, /, path_or_buf: str, orient: Literal["split"], lines: bool):
        """
        usage.dask: 6
        """
        ...

    @overload
    def to_json(self, /, path_or_buf: str, orient: Literal["records"], lines: bool):
        """
        usage.dask: 6
        """
        ...

    @overload
    def to_json(self, /, path_or_buf: str, orient: Literal["index"], lines: bool):
        """
        usage.dask: 4
        """
        ...

    @overload
    def to_json(self, /, path_or_buf: str, orient: Literal["columns"], lines: bool):
        """
        usage.dask: 4
        """
        ...

    @overload
    def to_json(self, /, path_or_buf: str, orient: Literal["values"], lines: bool):
        """
        usage.dask: 4
        """
        ...

    def to_json(
        self,
        /,
        path_or_buf: str,
        orient: Literal["values", "columns", "index", "records", "split"],
        lines: bool,
    ):
        """
        usage.dask: 24
        """
        ...

    @overload
    def to_records(self, /, index: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def to_records(self, /):
        """
        usage.dask: 3
        """
        ...

    def to_records(self, /, index: bool = ...):
        """
        usage.dask: 4
        """
        ...

    def to_string(self, /, max_rows: int, show_dimensions: bool):
        """
        usage.dask: 2
        """
        ...

    @overload
    def to_timestamp(self, /, freq: None, how: Literal["start"], axis: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def to_timestamp(self, /):
        """
        usage.dask: 1
        """
        ...

    def to_timestamp(
        self, /, freq: None = ..., how: Literal["start"] = ..., axis: int = ...
    ):
        """
        usage.dask: 2
        """
        ...

    def to_xarray(self, /):
        """
        usage.xarray: 5
        """
        ...

    @overload
    def truediv(self, /, other: pandas.core.frame.DataFrame, fill_value: int):
        """
        usage.dask: 3
        """
        ...

    @overload
    def truediv(self, /, other: int, fill_value: int):
        """
        usage.dask: 3
        """
        ...

    @overload
    def truediv(self, /, other: pandas.core.series.Series, axis: int):
        """
        usage.dask: 6
        """
        ...

    @overload
    def truediv(self, /, other: pandas.core.frame.DataFrame, axis: int):
        """
        usage.dask: 3
        """
        ...

    @overload
    def truediv(self, /, other: pandas.core.frame.DataFrame, axis: Literal["index"]):
        """
        usage.dask: 3
        """
        ...

    @overload
    def truediv(self, /, other: pandas.core.frame.DataFrame, axis: Literal["columns"]):
        """
        usage.dask: 3
        """
        ...

    @overload
    def truediv(self, /, other: pandas.core.series.Series, axis: Literal["index"]):
        """
        usage.dask: 3
        """
        ...

    @overload
    def truediv(self, /, other: pandas.core.series.Series, axis: Literal["columns"]):
        """
        usage.dask: 3
        """
        ...

    def truediv(
        self,
        /,
        other: Union[pandas.core.series.Series, pandas.core.frame.DataFrame, int],
        axis: Union[Literal["columns", "index"], int] = ...,
        fill_value: int = ...,
    ):
        """
        usage.dask: 27
        """
        ...

    @overload
    def var(self, /, axis: int, skipna: bool):
        """
        usage.dask: 2
        """
        ...

    @overload
    def var(self, /):
        """
        usage.dask: 7
        """
        ...

    @overload
    def var(self, /, axis: int, skipna: bool, ddof: int):
        """
        usage.dask: 2
        """
        ...

    @overload
    def var(self, /, axis: int, skipna: None):
        """
        usage.dask: 1
        """
        ...

    @overload
    def var(self, /, ddof: int):
        """
        usage.dask: 4
        """
        ...

    @overload
    def var(self, /, axis: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def var(self, /, axis: int, ddof: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def var(self, /, axis: Literal["index"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def var(self, /, axis: Literal["index"], ddof: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def var(self, /, axis: Literal["columns"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def var(self, /, axis: Literal["columns"], ddof: int):
        """
        usage.dask: 1
        """
        ...

    @overload
    def var(self, /, skipna: bool):
        """
        usage.dask: 2
        """
        ...

    @overload
    def var(self, /, skipna: bool, ddof: int):
        """
        usage.dask: 2
        """
        ...

    def var(
        self,
        /,
        axis: Union[Literal["columns", "index"], int] = ...,
        skipna: Union[bool, None] = ...,
        ddof: int = ...,
    ):
        """
        usage.dask: 26
        """
        ...

    @overload
    def where(
        self,
        /,
        cond: pandas.core.frame.DataFrame,
        other: pandas.core.series.Series,
        axis: int,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def where(self, /, cond: pandas.core.frame.DataFrame, other: float):
        """
        usage.dask: 1
        """
        ...

    @overload
    def where(self, /, cond: pandas.core.frame.DataFrame):
        """
        usage.dask: 1
        """
        ...

    @overload
    def where(
        self, /, cond: pandas.core.frame.DataFrame, other: pandas.core.frame.DataFrame
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    def where(
        self, /, cond: pandas.core.series.Series, other: pandas.core.frame.DataFrame
    ):
        """
        usage.dask: 2
        """
        ...

    def where(
        self,
        /,
        cond: Union[pandas.core.series.Series, pandas.core.frame.DataFrame],
        axis: int = ...,
        other: Union[
            pandas.core.frame.DataFrame, float, pandas.core.series.Series
        ] = ...,
    ):
        """
        usage.dask: 8
        """
        ...


class Pandas:
    def __eq__(self, _0: pandas.core.frame.Pandas, /):
        """
        usage.dask: 4
        """
        ...

    def __iter__(self, /):
        """
        usage.dask: 2
        """
        ...
