from typing import *


class DataFrame:

    # usage.dask: 4
    # usage.hvplot: 1
    __module__: ClassVar[object]

    # usage.dask: 4
    __name__: ClassVar[object]

    # usage.koalas: 1
    info: ClassVar[object]

    # usage.geopandas: 1
    merge: ClassVar[object]

    # usage.dask: 6
    # usage.koalas: 1
    # usage.networkx: 1
    # usage.prophet: 35
    # usage.pyjanitor: 4
    # usage.seaborn: 9
    # usage.sklearn: 39
    # usage.statsmodels: 135
    shape: ClassVar[object]

    # usage.sklearn: 2
    sparse: ClassVar[object]

    # usage.koalas: 1
    to_dict: ClassVar[object]

    # usage.koalas: 5
    to_excel: ClassVar[object]

    # usage.koalas: 2
    to_html: ClassVar[object]

    # usage.koalas: 1
    to_latex: ClassVar[object]

    # usage.koalas: 1
    to_markdown: ClassVar[object]

    # usage.koalas: 1
    to_records: ClassVar[object]

    # usage.koalas: 2
    to_string: ClassVar[object]

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Type[float], Type[str]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["B", "A"]], /):
        """
        usage.dask: 4
        usage.koalas: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["c1", "c0"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["id", "x"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(id-x, id-y)", "(x, y)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["0"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: None, /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["B"]], /):
        """
        usage.dask: 1
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["B"], /):
        """
        usage.dask: 7
        usage.hvplot: 1
        usage.koalas: 4
        usage.sklearn: 1
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["A"]], /):
        """
        usage.dask: 1
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["A"], /):
        """
        usage.dask: 27
        usage.hvplot: 1
        usage.koalas: 11
        usage.sklearn: 1
        usage.statsmodels: 11
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: list, /):
        """
        usage.dask: 1
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["animal"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["animal"], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["Col1"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["Col1"], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["Col2"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["Col2"], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["x"]], /):
        """
        usage.dask: 5
        usage.koalas: 1
        usage.seaborn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["x"], /):
        """
        usage.dask: 13
        usage.geopandas: 3
        usage.hvplot: 4
        usage.koalas: 9
        usage.prophet: 10
        usage.seaborn: 65
        usage.statsmodels: 2
        usage.xarray: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["koalas"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["koalas"], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["dates"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["dates"], /):
        """
        usage.koalas: 1
        usage.pyjanitor: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["cats", "dogs"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["col2", "col1"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["a"]], /):
        """
        usage.dask: 4
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["age", "kids", "score"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["id"]], /):
        """
        usage.dask: 2
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["id"], /):
        """
        usage.dask: 2
        usage.koalas: 5
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["degrees", "angles"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["col_B", "col_A"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["B_col", "A_col"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["C", "B", "A"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[str], /):
        """
        usage.koalas: 30
        usage.prophet: 1
        usage.pyjanitor: 1
        usage.sklearn: 22
        usage.statsmodels: 13
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls, _0: List[Literal["(B, max)", "(B, min)", "(A, min)", "(A, sum)"]], /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["1", "0"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["0"], /):
        """
        usage.dask: 4
        usage.hvplot: 1
        usage.koalas: 6
        usage.sklearn: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["1"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["1"], /):
        """
        usage.dask: 4
        usage.koalas: 4
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["temp_c"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["temp_f", "temp_c"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls, _0: List[Literal["temp_idx", "temp_k", "temp_f", "temp_c"]], /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["b", "a"]], /):
        """
        usage.dask: 3
        usage.koalas: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["None"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["w", "z", "y", "x"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["Single", "Age", "Person"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["numeric2", "numeric1"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(num, b)", "(num, a)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(num, b)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["num"], Literal["b"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["numeric1"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["numeric1"], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["c", "b", "a"]], /):
        """
        usage.dask: 1
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["w", "z", "y"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["w", "x"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(b, w)", "(b, z)", "(a, y)", "(a, x)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(b, w)", "(b, z)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(d, f)", "(c, e)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["d", "c"]], /):
        """
        usage.dask: 4
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["born", "toy", "name"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["name"]], /):
        """
        usage.dask: 2
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["D", "C", "B", "A"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["three", "one"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["three", "two", "one"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["one"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["one"], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["2", "1", "0"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["count"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["__0_bucket"], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(c, z)", "(b, y)", "(a, x)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["float_col", "text_col", "int_col"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["num_wings", "num_legs"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["population", "species"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["species"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["species"], /):
        """
        usage.koalas: 2
        usage.seaborn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["A", "key"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["B", "key"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["B", "key_right", "A", "key_left"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["shield", "max_speed"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["value", "variable"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["value", "variable", "A"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["value", "variable", "B", "A"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["myValname", "myVarname", "A"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["value", "lkey"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["value", "rkey"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["value_y", "rkey", "value_x", "lkey"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["Y", "X"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["IT", "GR", "FR"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["zoo", "baz", "bar", "foo"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["baz", "bar", "foo"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(b, baz)", "(a, foo)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["two", "one"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["E", "D", "C", "B", "A"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["small", "large"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(D, foo)", "(D, bar)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls, _0: List[Literal["(E, foo)", "(E, bar)", "(D, foo)", "(D, bar)"]], /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["max_speed", "class", "name"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["class"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["class"], /):
        """
        usage.koalas: 1
        usage.seaborn: 5
        usage.sklearn: 2
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["max_speed", "name"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls, _0: List[Literal["(b, max_speed)", "(a, class)", "(a, name)"]], /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["class", "name"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(b, max_speed)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["0.5"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["0.5"], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["C C", "B", "A"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["response_time", "http_status"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["user_agent", "http_status"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["prices"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["c", "a"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(y, D)", "(y, C)", "(x, B)", "(x, A)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["weapon", "name"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["max_speed", "class"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["max_speed", "class", "index"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(species, type)", "(speed, max)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls, _0: List[Literal["(species, type)", "(speed, max)", "(class, )"]], /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls, _0: List[Literal["(species, type)", "(speed, max)", "(, class)"]], /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls, _0: List[Literal["(species, type)", "(speed, max)", "(species, class)"]], /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls, _0: List[Literal["(species, type)", "(speed, max)", "(genus, class)"]], /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["d", "c", "b", "a"]], /):
        """
        usage.dask: 3
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["b"]], /):
        """
        usage.dask: 3
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["c"]], /):
        """
        usage.dask: 2
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["d", "c", "b"]], /):
        """
        usage.dask: 2
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["sale", "year", "month"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["sale", "year"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["sale"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["Col3", "Col2", "Col1"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["col3", "col2", "col1"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["height", "weight"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(weight, pounds)", "(weight, kg)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["weight"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(height, m)", "(weight, kg)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["code", "country", "date"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["col2"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["weapon", "mask", "name"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(X, B)", "(X, A)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["C", "B"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["D", "C"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["z", "y", "x"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["y", "x"]], /):
        """
        usage.dask: 2
        usage.koalas: 1
        usage.seaborn: 6
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["int2", "int1", "str"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["Max Speed", "Animal"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["Max Speed"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["C"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["C"], /):
        """
        usage.dask: 2
        usage.koalas: 8
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["b"], /):
        """
        usage.dask: 23
        usage.koalas: 14
        usage.modin: 2
        usage.networkx: 3
        usage.pyjanitor: 1
        usage.seaborn: 11
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["d", "b"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["shield"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["shield"], /):
        """
        usage.koalas: 4
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["max_speed"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["max_speed"], /):
        """
        usage.koalas: 4
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(y, b)", "(x, a)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls, _0: List[Literal["col4", "col3", "col2", "col1", "category"]], /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["value"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["value"], /):
        """
        usage.dask: 1
        usage.koalas: 3
        usage.statsmodels: 13
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["a"], /):
        """
        usage.dask: 40
        usage.geopandas: 1
        usage.hvplot: 1
        usage.koalas: 28
        usage.modin: 2
        usage.pyjanitor: 19
        usage.seaborn: 33
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["date"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["date"], /):
        """
        usage.dask: 1
        usage.koalas: 1
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["col 2", "col 1"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["col 1"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["col 1"], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["weight", "height", "age"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["rank", "max_speed", "name"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(B, max)", "(B, min)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls, _0: List[Literal["(C, max)", "(C, min)", "(B, max)", "(B, min)"]], /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["b_max"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["b_min", "b_max"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["c_min", "b_max"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["C", "B", "A", "__groupkey_0__"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["__groupkey_0__"], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["B", "__groupkey_0__"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["D", "C", "B"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["c", "b"]], /):
        """
        usage.dask: 1
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["value2", "value1", "id"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["value1"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["value1"], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["C", "B", "__groupkey_0__"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["__index_level_0__"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls, _0: List[Literal["__index_level_1__", "__index_level_0__"]], /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["color", "number"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["E", "D", "C", "B"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(Y, D)", "(Y, C)", "(X, B)", "(X, A)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(b, z)", "(a, y)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["x2", "x1"]], /):
        """
        usage.koalas: 2
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["y"]], /):
        """
        usage.dask: 2
        usage.koalas: 2
        usage.prophet: 1
        usage.seaborn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["prediction", "x2", "x1"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["y", "z", "x2", "x1"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["number", "letter"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["0", "number", "letter"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["animal", "number", "letter"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["number", "letter", "animal"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["name", "animal", "number", "letter"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["toy", "name", "born", "age"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["sales"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["val"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["val"], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["lfence"], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["ufence"], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["mean"], /):
        """
        usage.koalas: 1
        usage.prophet: 1
        usage.statsmodels: 22
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["50%"], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["25%"], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["75%"], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["mass"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["mass"], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["species", "width", "length"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(0, max)", "(0, min)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["c"], /):
        """
        usage.dask: 14
        usage.koalas: 8
        usage.modin: 2
        usage.pyjanitor: 3
        usage.seaborn: 9
        usage.sklearn: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["my_name"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["my_name"], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["dogs"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["dogs"], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["vals"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["exp", "sqrt"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(x, a)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["x"], Literal["a"]], /):
        """
        usage.koalas: 15
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["abc"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["abc'abc", 'abc"abc', "abc"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["cond2", "cond1"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["4", "3", "2", "1", "0"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls, _0: List[Literal["(, __dummy__)", "(__dummy__, )", "(x, a)"]], /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["count", "a"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["amount", "name"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["name"], /):
        """
        usage.dask: 1
        usage.koalas: 3
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["amount"], /):
        """
        usage.dask: 2
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: int, /):
        """
        usage.dask: 11
        usage.koalas: 2
        usage.modin: 2
        usage.networkx: 3
        usage.sklearn: 1
        usage.statsmodels: 11
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["a", "n"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["n"], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["amount"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["bb", "aa"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["aa"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["aa"], /):
        """
        usage.dask: 1
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: pandas.core.series.Series, /):
        """
        usage.dask: 13
        usage.hvplot: 3
        usage.koalas: 9
        usage.prophet: 7
        usage.pyjanitor: 5
        usage.seaborn: 7
        usage.statsmodels: 11
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(col_X, col_B)", "(col_X, col_A)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["Bfirst_series", "Afirst_series"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(A, Y)", "(A, X)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(y, c)", "(x, b)", "(x, a)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["w", "b", "a"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(a, c)", "(y, w)", "(x, b)", "(x, a)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls, _0: List[Literal["(Z, )", "(a, c)", "(y, w)", "(x, b)", "(x, a)"]], /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["x", "b", "a"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["X", "B", "A"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["clip", "X", "B", "A"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls, _0: List[Literal["(B, two)", "(B, one)", "(A, two)", "(A, one)"]], /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["A"], Literal["one"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["A"], Literal["two"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["B"], Literal["one"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["B"], Literal["two"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: pandas.core.indexes.base.Index, /):
        """
        usage.dask: 10
        usage.koalas: 1
        usage.networkx: 1
        usage.prophet: 2
        usage.statsmodels: 18
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls,
        _0: List[Literal["(x, b, 4)", "(y.z, c.d, 3)", "(x, b, 2)", "(x, a, 1)"]],
        /,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(b, 4)", "(b, 2)", "(a, 1)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["y.z"], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(c.d, 3)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["4", "2"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["2"], /):
        """
        usage.dask: 4
        usage.koalas: 5
        usage.pyjanitor: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["2"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["x"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["x"], Literal["a"], Literal["1"]], /):
        """
        usage.koalas: 4
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(x, a, 1)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls, _0: List[Literal["(Y, D, Z)", "(Y, C, Z)", "(X, B, Z)", "(X, A, Z)"]], /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["X"], /):
        """
        usage.dask: 2
        usage.koalas: 6
        usage.seaborn: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(B, Z)", "(A, Z)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["Z"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["X"], Literal["A"]], /):
        """
        usage.koalas: 14
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["X"], Literal["A"], Literal["Z"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(X, A, Z)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(y, Col3)", "(x, Col2)", "(x, Col1)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["a.b"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["a.b"], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["z", "y"]], /):
        """
        usage.dask: 2
        usage.koalas: 1
        usage.seaborn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(b, z)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(a, y)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["f", "e"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls, _0: List[Literal["0.5307682923411018", "0.31992251735325117"]], /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls,
        _0: List[
            Literal[
                "0.9001395954082655",
                "0.5307682923411018",
                "0.2635517951467826",
                "0.31992251735325117",
                "0.9655187292975722",
            ]
        ],
        /,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls,
        _0: List[
            Literal[
                "0.9001395954082655",
                "0.5307682923411018",
                "0.2635517951467826",
                "0.31992251735325117",
            ]
        ],
        /,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls,
        _0: List[
            Literal["0.5307682923411018", "0.31992251735325117", "0.9655187292975722"]
        ],
        /,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls,
        _0: List[
            Literal[
                "0.5307682923411018",
                "0.2635517951467826",
                "0.31992251735325117",
                "0.9655187292975722",
            ]
        ],
        /,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["0.9655187292975722"], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["0.9655187292975722"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(b, z)", "(a, y)", "(a, x)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["t"], /):
        """
        usage.koalas: 2
        usage.prophet: 10
        usage.seaborn: 4
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["t"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(B, X)", "(A, Z)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["A"], Literal["Z"]], /):
        """
        usage.koalas: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["B"], Literal["X"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["Z"], /):
        """
        usage.koalas: 2
        usage.seaborn: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["y"], /):
        """
        usage.dask: 13
        usage.geopandas: 3
        usage.hvplot: 6
        usage.koalas: 1
        usage.prophet: 18
        usage.seaborn: 58
        usage.statsmodels: 12
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["z"]], /):
        """
        usage.dask: 2
        usage.koalas: 1
        usage.seaborn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["z"], /):
        """
        usage.dask: 3
        usage.geopandas: 1
        usage.koalas: 1
        usage.seaborn: 17
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(y, c)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["db", "cb", "ba"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["db", "ba"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["cb"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["db", "cb"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(z, db)", "(y, cb)", "(x, ba)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(z, db)", "(x, ba)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(y, cb)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["population"], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["B", "A", "key"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls, _0: List[Literal["(Y, B)", "(x_right, key)", "(Y, A)", "(x_left, key)"]], /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(Y, B)", "(Y, A)", "(x, key)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["value", "variable_1", "variable_0"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls, _0: List[Literal["value", "variable_1", "variable_0", "(X, A)"]], /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["(X, A)"], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["variable_0"], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["variable_1"], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["myValname", "myV2", "myV1", "(X, A)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["myV1"], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["myV2"], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["myValname"], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["value", "v1", "v0"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["y", "rkey", "x", "value", "lkey"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["y", "x", "value"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["y", "value_y", "rkey", "x", "value_x"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["y", "value_y", "x", "value_x", "lkey"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["y", "value_y", "x", "value_x"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["y", "value", "rkey", "x"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["y", "x", "value", "lkey"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["x", "value", "lkey"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["x_right", "x_left", "value", "lkey"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls,
        _0: List[Literal["(c, y)", "(a, rkey)", "(b, x)", "(a, value)", "(a, lkey)"]],
        /,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(c, y)", "(b, x)", "(a, value)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls, _0: List[Literal["(c, y)", "(a_y, value)", "(b, x)", "(a_x, value)"]], /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(d, )"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["d"], /):
        """
        usage.dask: 10
        usage.koalas: 2
        usage.seaborn: 4
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["d"]], /):
        """
        usage.dask: 2
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["e"], /):
        """
        usage.dask: 8
        usage.koalas: 6
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(g, , )", "(, f, )"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal[""], /):
        """
        usage.koalas: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["f"], /):
        """
        usage.dask: 1
        usage.koalas: 4
        usage.seaborn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["f"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["g"], /):
        """
        usage.dask: 2
        usage.koalas: 2
        usage.seaborn: 2
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["g"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["h"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["h"], /):
        """
        usage.koalas: 2
        usage.prophet: 2
        usage.seaborn: 5
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["i"], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["i"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["e", "a"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls, _0: List[Literal["(e, g, , )", "(e, , f, )", "(a, , , b)"]], /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["a", "e"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls, _0: List[Literal["(a, , , b)", "(e, g, , )", "(e, , f, )"]], /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["a"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["e"], Literal["g"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(e, g)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["i"], Literal[""]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(i, )"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["8", "6", "4", "3", "2"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["3"], /):
        """
        usage.dask: 4
        usage.koalas: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["4"], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["6"], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["8"], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls, _0: List[Literal["(b, 8)", "(b, 6)", "(b, 4)", "(b, 3)", "(b, 2)"]], /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["b"], Literal["2"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["b"], int], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["b"], Literal["3"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["b"], Literal["4"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["b"], Literal["6"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["b"], Literal["8"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["e"], Literal["2"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["e"], int], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["e"], Literal["3"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["e"], Literal["4"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["e"], Literal["6"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["e"], Literal["8"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["d"], Literal["2"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["d"], int], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["d"], Literal["3"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["d"], Literal["4"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["d"], Literal["6"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["d"], Literal["8"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls,
        _0: List[
            Literal["(x, b, 8)", "(x, b, 6)", "(x, b, 4)", "(x, b, 3)", "(x, b, 2)"]
        ],
        /,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["x"], Literal["b"], Literal["2"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["x"], Literal["b"], int], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["x"], Literal["b"], Literal["3"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["x"], Literal["b"], Literal["4"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["x"], Literal["b"], Literal["6"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["x"], Literal["b"], Literal["8"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["y"], Literal["e"], Literal["2"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["y"], Literal["e"], int], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["y"], Literal["e"], Literal["3"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["y"], Literal["e"], Literal["4"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["y"], Literal["e"], Literal["6"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["y"], Literal["e"], Literal["8"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["w"], Literal["d"], Literal["2"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["w"], Literal["d"], int], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["w"], Literal["d"], Literal["3"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["w"], Literal["d"], Literal["4"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["w"], Literal["d"], Literal["6"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["w"], Literal["d"], Literal["8"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(y, col2)", "(x, col1)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["3", "2", "numbers"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["numbers"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(Y, 3)", "(Y, 2)", "(X, numbers)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(B, 1)", "(A, 0)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(y, d)", "(y, c)", "(x, b)", "(x, a)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(Y, d)", "(Y, c)", "(X, b)", "(X, a)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(Y, C)", "(X, B)", "(X, A)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["a", "id"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["b", "a", "index"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls,
        _0: List[Literal["(species, type)", "(speed, max)", "(name, )", "(class, )"]],
        /,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls,
        _0: List[Literal["(species, type)", "(speed, max)", "(y, name)", "(x, class)"]],
        /,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["B", "A", "level_1", "level_0"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(A, Z)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["weight", "height"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["B", "C"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(C, C)", "(B, X)", "(A, Z)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(C, C)", "(B, X)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(B, X)", "(C, C)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["animal_2", "animal_1"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["d", "id"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls, _0: List[Literal["(cg3, d)", "(cg2, c)", "(cg1, b)", "(cg1, a)"]], /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(rg2, z)", "(rg1, y)", "(rg1, x)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(C, Z)", "(B, X)", "(A, Z)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(C, Z)", "(B, X)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["0"], Literal["x"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[int, Literal["x"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["0"], Literal["y"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[int, Literal["y"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["0"], Literal["z"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[int, Literal["z"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["1"], Literal["x"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["1"], Literal["y"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["1"], Literal["z"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["2"], Literal["x"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["2"], Literal["y"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["2"], Literal["z"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(mammal, dog, walks)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls, _0: Tuple[Literal["mammal"], Literal["dog"], Literal["walks"]], /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["bhello", "f", "i64", "i32"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["i64", "i32"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["i32", "i64"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["bhello", "f", "i64", "i32", "index"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls, _0: List[Literal["bhello", "f", "i64", "i32", "Unnamed: 0"]], /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(a, y)", "(a, x)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["visits", "signups", "sales"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["val", "lab"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["__a_bucket"], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(C, sum)", "(B, max)", "(B, min)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(C, sum)", "(B, sum)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(C, sum)", "(B, sum)", "(A, sum)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls, _0: List[Literal["(C, sum)", "(B, max)", "(B, min)", "(A, )"]], /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(C, sum)", "(B, sum)", "(A, )"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(Y, C)", "(X, B)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls, _0: List[Literal["(Y, C, sum)", "(X, B, max)", "(X, B, min)"]], /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls,
        _0: List[
            Literal["(weight, max)", "(weight, min)", "(height, max)", "(height, min)"]
        ],
        /,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls,
        _0: List[Literal["(Y, C, max)", "(Y, C, min)", "(X, B, max)", "(X, B, min)"]],
        /,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["b_max", "a_max"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["a_max"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["a_min", "a_max"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(Y, B)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(Y, B)", "(X, A)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["c", "b", "a", "__groupkey_0__"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["a", "__groupkey_0__"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls, _0: List[Literal["c", "b", "a", "__groupkey_1__", "__groupkey_0__"]], /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["__groupkey_1__"], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["c", "__groupkey_0__"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["0", "__groupkey_0__"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls, _0: List[Literal["(y, c)", "(x, b)", "(x, a)", "(__groupkey_0__, )"]], /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["__groupkey_0__"], Literal[""]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls,
        _0: List[
            Literal[
                "(y, c)", "(x, b)", "(x, a)", "(__groupkey_1__, )", "(__groupkey_0__, )"
            ]
        ],
        /,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["__groupkey_1__"], Literal[""]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["v", "d", "__groupkey_0__"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["v", "d"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["car_id", "timestamp", "__groupkey_0__"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["column"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["timestamp"], /):
        """
        usage.dask: 2
        usage.koalas: 4
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["mean"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["v"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["v"], /):
        """
        usage.dask: 6
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(Z, D)", "(Y, C)", "(X, B)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(y, c)", "(x, a)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["y"], Literal["c"]], /):
        """
        usage.koalas: 4
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(y, c)", "(x, b)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["d", "c", "a"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["a", "b"]], /):
        """
        usage.dask: 1
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["c", "a", "b"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["d", "c", "a", "b"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["c", "a", "__groupkey_0__"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["c", "__groupkey_1__", "__groupkey_0__"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls, _0: List[Literal["(y, c)", "(x, a)", "(__groupkey_0__, )"]], /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls, _0: List[Literal["(y, c)", "(__groupkey_1__, )", "(__groupkey_0__, )"]], /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(a, x)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(d, y)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["__index_level_2__"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["__index_level_1__"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["b", "__index_level_0__"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["b", "0"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["Koalas"], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["sale", "year", "month", "index"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["sale", "month"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["sale"], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["s", "month"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["min_speed", "shield", "max_speed"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["min_speed"], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["x"], Literal["shield"]], /):
        """
        usage.koalas: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls,
        _0: List[
            Literal["(y, shield)", "(y, min_speed)", "(x, shield)", "(x, max_speed)"]
        ],
        /,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["x"], Literal["max_speed"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["y"], Literal["min_speed"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["y"], Literal["shield"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls,
        _0: List[
            Literal[
                "(z, )",
                "(y, shield)",
                "(y, min_speed)",
                "(x, shield)",
                "(x, max_speed)",
            ]
        ],
        /,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["z"], Literal[""]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: slice[Literal["a"], Literal["e"], Literal["a"]], /):
        """
        usage.dask: 1
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: slice[Literal["a"], Literal["b"], Literal["a"]], /):
        """
        usage.dask: 1
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: slice[Literal["f"], None, Literal["f"]], /):
        """
        usage.dask: 1
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["3"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(baz, two)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["baz"], Literal["two"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(bar, one)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["bar"], Literal["one"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["A", "B"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(bar, two)", "(bar, one)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(bar, one)", "(bar, two)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls, _0: List[Literal["(baz, two)", "(baz, one)", "(bar, two)"]], /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: slice[None, int, None], /):
        """
        usage.dask: 1
        usage.koalas: 4
        usage.modin: 2
        usage.statsmodels: 5
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: slice[int, None, int], /):
        """
        usage.dask: 1
        usage.koalas: 4
        usage.statsmodels: 7
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: slice[int, int, int], /):
        """
        usage.dask: 1
        usage.koalas: 6
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: slice[None, Literal["2013-01-04T00:00:00"], None], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls,
        _0: slice[Literal["2013-01-02T00:00:00"], None, Literal["2013-01-02T00:00:00"]],
        /,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls,
        _0: slice[
            Literal["2013-01-02T00:00:00"],
            Literal["2013-01-04T00:00:00"],
            Literal["2013-01-02T00:00:00"],
        ],
        /,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls, _0: List[Literal["(baz, one)", "(bar, two)", "(bar, one)"]], /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(baz, one)", "(bar, two)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(bar, two)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls,
        _0: List[Literal["(baz, two)", "(baz, one)", "(bar, one)", "(bar, two)"]],
        /,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(x, b)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["X"], Literal["C"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["X"], Literal["B"]], /):
        """
        usage.koalas: 4
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["3", "2", "1", "0"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["C", "A"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["D", "C", "A"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(X, C)", "(X, A)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(X, C)", "(X, B)", "(X, A)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(X, D)", "(X, C)", "(X, A)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(X, D)", "(X, C)", "(X, B)", "(X, A)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["ABC", "(X, A)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(X, B)", "ABC"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["B", "A", "C"]], /):
        """
        usage.dask: 2
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["A", "C"]], /):
        """
        usage.koalas: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["index", "C", "B", "A"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["index"], /):
        """
        usage.koalas: 3
        usage.pyjanitor: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["0", "C", "B", "A"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["C", "B", "A", "0"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["C", "B", "A", "index"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Tuple[Literal["Y", "X"], Literal["C", "A"]]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls, _0: List[Literal["(index, )", "(Y, C)", "(X, B)", "(X, A)"]], /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(Y, C)", "(X, A)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["day", "month", "year"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["year"]], /):
        """
        usage.koalas: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["year"], /):
        """
        usage.koalas: 1
        usage.statsmodels: 4
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["x"], Literal["b"]], /):
        """
        usage.koalas: 6
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(x, b)", "(x, a)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(z, d)", "(y, c)", "(x, b)", "(x, a)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["c", "f", "e", "b", "a"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["NEW", "Koalas", "a"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["d", "b", "a"]], /):
        """
        usage.dask: 2
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["f", "e", "b", "a"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(z, f)", "(z, e)", "(x, b)", "(x, a)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["z"], Literal["e"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["z"], Literal["f"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["e", "c"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["x", "c"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["y", "x", "e", "c"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls, _0: List[Literal["c", "b", "__groupkey_1__", "__groupkey_0__"]], /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["4", "3", "2", "1"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["b_d", "b_c", "b_b", "b_a", "a"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["b_a"], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["b_b"], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["b_c"], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["b_d"], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["True", "False"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["False"], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: bool, /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["True"], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["d_2019-01-02", "d_2019-01-01", "dt"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["2019-01-02", "2019-01-01"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["2019-01-01"], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["2019-01-02"], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls, _0: List[Literal["2019-01-01 00:00:01", "2019-01-01 00:00:00"]], /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["2019-01-01 00:00:00"], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["2019-01-01 00:00:01"], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["d_2", "d_1"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["2", "1"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: decimal.Decimal, /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["A_b", "A_a", "B"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["X-4", "X-3", "X-2", "X-1"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["4", "3", "2"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["5.0", "3.0", "2.0", "1.0"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["1.0"], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: float, /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["2.0"], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["3.0"], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["5.0"], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["nan", "5.0", "3.0", "2.0", "1.0"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["nan"], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["(x, a, 1)"], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["('x', 'b', '2')_a"], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["('x', 'b', '2')_b"], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["('x', 'b', '2')_c"], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["('x', 'b', '2')_d"], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["('y', 'c', '3')_a"], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["('y', 'c', '3')_b"], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["('y', 'c', '3')_c"], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["('y', 'c', '3')_d"], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["(x, b, 2)"], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["('x', 'a', '1')_1"], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["('x', 'a', '1')_2"], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["('x', 'a', '1')_3"], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["('x', 'a', '1')_4"], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["(y, c, 3)"], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["y"], Literal["c"], Literal["3"]], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["1_1"], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["1_2"], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["1_3"], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["1_4"], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["foo_c", "foo_b", "foo_a", "D", "A"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["foo_4", "foo_3", "foo_2", "foo_1"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls, _0: List[Literal["['foo']_4", "['foo']_3", "['foo']_2", "['foo']_1"]], /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["left"], /):
        """
        usage.koalas: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["right"], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["left"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["Koalas"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(X, A)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["renamed"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["renamed"], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["foo", "idx"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["values", "idx"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["foo"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["foo"], /):
        """
        usage.koalas: 1
        usage.xarray: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["0", "index"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(y, z)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["y"], Literal["z"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["0", "level_1", "level_0"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["z", "x", "v", "c"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["index"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["start_date"], /):
        """
        usage.koalas: 6
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["start_date"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["end_date"], /):
        """
        usage.koalas: 5
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["end_date"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["sales"], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["single"], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["__single_bucket"], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["col1"], /):
        """
        usage.dask: 1
        usage.koalas: 7
        usage.pyjanitor: 4
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["col2"], /):
        """
        usage.dask: 1
        usage.koalas: 4
        usage.modin: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["col1"]], /):
        """
        usage.koalas: 1
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["(Z, D)", "(Y, C)", "(X, B)", "(X, A)"]], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Type[float], /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls,
        _0: Tuple[
            slice[Literal["a"], Type[float], Literal["a"]],
            slice[Literal["b"], Type[str], Literal["b"]],
        ],
        /,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls,
        _0: Tuple[
            slice[Literal["a"], Type[float], Literal["a"]],
            slice[Literal["b"], Type[int], Literal["b"]],
        ],
        /,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: zip, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls,
        _0: Tuple[
            slice[Literal["a"], Type[float], Literal["a"]],
            slice[Literal["b"], Type[str], Literal["b"]],
        ],
        /,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: type, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["foo", "C"]], /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["realinv"], /):
        """
        usage.statsmodels: 10
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["realgdp"], /):
        """
        usage.statsmodels: 26
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["realint"], /):
        """
        usage.statsmodels: 7
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["weights_missing"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["X", "constant"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["weights"], /):
        """
        usage.seaborn: 4
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["statistic"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["pvalue"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["df_constraint"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["df_denom"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["offset"], /):
        """
        usage.statsmodels: 9
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["oracle"], /):
        """
        usage.statsmodels: 5
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["final"], /):
        """
        usage.statsmodels: 8
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["popul"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["PID"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["cancer"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["AVGEXP"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["co2"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["BILLS104"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["WORLDCONSUMPTION"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["EXECUTIONS"], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["income"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["affairs"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["invest"], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["survival"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["TOTEMP"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["choice"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["volume"], /):
        """
        usage.statsmodels: 5
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["mdvis"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["YES"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["GRADE"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["STACKLOSS"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["NABOVE"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["NBELOW"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["murder"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["duration"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["Title"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["groups"], /):
        """
        usage.statsmodels: 6
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["pyears"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["dy/dx"], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["exposure"], /):
        """
        usage.statsmodels: 7
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["Bar", "constant"]], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["pp"]], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["num"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["exog4", "exog3", "exog2", "exog1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["status"], /):
        """
        usage.statsmodels: 5
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["entry"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls, _0: List[Literal["exog1:exog2", "exog2", "np.log(exog2)", "exog1"]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["log HR"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["Group"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["T"], /):
        """
        usage.statsmodels: 15
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["Status"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["SOUTH"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["INCOME"], /):
        """
        usage.statsmodels: 4
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["x2", "x0"]], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["y_est"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["s(x2)", "s(x0)"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["y_est"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["fit"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["se_fit"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["Post. Mean"], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["Post. SD"], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["SD (LB)"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["SD (UB)"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["Year"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["subject"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["time"], /):
        """
        usage.hvplot: 5
        usage.seaborn: 4
        usage.statsmodels: 7
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["Id"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["TheGroups"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["Time"], /):
        """
        usage.dask: 2
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["X2", "X1"]], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["grps"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["fake", "constant"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["SOUTH", "INCOME"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["x1"], /):
        """
        usage.statsmodels: 8
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["x2"], /):
        """
        usage.statsmodels: 8
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["x3"], /):
        """
        usage.statsmodels: 8
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["x4"], /):
        """
        usage.statsmodels: 8
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["x5"], /):
        """
        usage.statsmodels: 8
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: pandas.core.frame.DataFrame, /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["intcol"], /):
        """
        usage.statsmodels: 4
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["var1"], /):
        """
        usage.statsmodels: 4
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["var2"], /):
        """
        usage.statsmodels: 5
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["var3"], /):
        """
        usage.statsmodels: 4
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["var4"], /):
        """
        usage.statsmodels: 4
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["censored"], /):
        """
        usage.statsmodels: 12
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["conc"], /):
        """
        usage.statsmodels: 14
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["censored", "conc"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["lower_dl"], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["nuncen_above"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["nobs_below"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["qual"], /):
        """
        usage.statsmodels: 9
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["Zprelim"], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["estimated"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["res"], /):
        """
        usage.statsmodels: 12
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["plot_pos"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["cen"], /):
        """
        usage.statsmodels: 15
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["obs"], /):
        """
        usage.statsmodels: 14
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["cen", "obs"]], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls,
        _0: List[
            Literal["prob_exceedance", "ncen_equal", "nobs_below", "nuncen_above"]
        ],
        /,
    ):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["cen", "res"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["cen", "conc"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["qual", "value"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["quarter"], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["datetime_c"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["datetime_big_c"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["weekly_date"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["monthly_date"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["quarterly_date"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["half_yearly_date"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["yearly_date"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["Coef."], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["Std.Err."], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Tuple[Literal["x"], Literal["sum"]]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["f2", "f1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["f2b", "f1b"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["f2o", "f1o"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["f2ob", "f1ob"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["Loc"]], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["Max", "Occ", "Basal"]], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["Drug"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["P>|z|"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["[0.025"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["0.975]"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["batch"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["Pig"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["x1", "g", "y"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["y", "x1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["c2", "c1", "x1", "g", "y"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["y", "x1", "c2", "c1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["z1", "x1", "g", "y"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["z1", "y", "x1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["z1", "y", "x1", "c2", "c1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["IDS"], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["grp"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["std err"], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["m1"], /):
        """
        usage.statsmodels: 11
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["m1", "unemp"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["beta2", "beta1"]], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["rec_resid"], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["rr"], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["cusum"], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["uw", "lw"]], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["cusum2"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["uww", "lww"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["infl"], /):
        """
        usage.statsmodels: 44
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["unemp", "m1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["cpi", "unemp", "m1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["fittedvalues"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["sum_sq"], /):
        """
        usage.statsmodels: 7
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["df"], /):
        """
        usage.statsmodels: 18
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["F"], /):
        """
        usage.dask: 2
        usage.statsmodels: 20
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["PR(>F)"], /):
        """
        usage.statsmodels: 13
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["df_resid"], /):
        """
        usage.statsmodels: 4
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["ssr"], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["ss_diff"], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["df_diff"], /):
        """
        usage.statsmodels: 4
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["Pr(>F)"], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["DV"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["D"], /):
        """
        usage.dask: 2
        usage.networkx: 1
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["Pr > F", "Den DF", "Num DF", "F Value"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["v1"], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["v2"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[int], /):
        """
        usage.dask: 4
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["strat", "v2", "v1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["x1", "c"]], /):
        """
        usage.statsmodels: 4
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["x2", "c"]], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["x2", "x1", "c"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["SUNACTIVITY"], /):
        """
        usage.statsmodels: 9
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["x0"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["__index__"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["x5"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["constrict"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["log_volumne", "log_rate", "const"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls,
        _0: List[Literal["dffits_internal", "hat_diag", "standard_resid", "cooks_d"]],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["cong_mesg"], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["emo"], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["ystatus"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["mtime", "exp"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["mstatus"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["exp"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["hs_grad", "murder"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["capital", "value"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["firm"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["const"], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["GNP"], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["UNEMP"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["string_var"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["apple"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["price"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["cpi", "realinv"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["infl", "tbilrate"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["unemp", "infl"]], /):
        """
        usage.statsmodels: 4
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["filtered_0"], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["smoothed_0"], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["duration1", "duration0"]], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["inv"], /):
        """
        usage.statsmodels: 5
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["inc"], /):
        """
        usage.statsmodels: 5
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["consump"], /):
        """
        usage.statsmodels: 4
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["realint", "infl"]], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["count"], /):
        """
        usage.prophet: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["global.2", "global.1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["block"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["order"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["revision date"], /):
        """
        usage.statsmodels: 5
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["revised variable"], /):
        """
        usage.statsmodels: 5
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["update date"], /):
        """
        usage.statsmodels: 7
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["updated variable"], /):
        """
        usage.statsmodels: 7
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["news"], /):
        """
        usage.statsmodels: 4
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["weight"], /):
        """
        usage.networkx: 1
        usage.statsmodels: 6
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls,
        _0: List[Literal["impact", "weight", "news", "forecast (prev)", "observed"]],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls, _0: List[Literal["impact", "weight", "observed", "forecast (prev)"]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["oil_fpp1_mean"], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["oil_fpp1"], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["lower y"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["oil_fpp1_lower"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["upper y"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["oil_fpp1_upper"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["oil_fpp2_mean"], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["oil_fpp2"], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["oil_fpp2_lower"], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["oil_fpp2_upper"], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["oil_fpp3_mean"], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["oil_fpp3"], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["oil_fpp3_lower"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["oil_fpp3_upper"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["oil_ets_mean"], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["oil_ets"], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["oil_ets_lower"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["oil_ets_upper"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["air_fpp1_mean"], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["air_fpp1"], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["air_fpp2_mean"], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["air_fpp2"], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["air_fpp2_lower"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["air_fpp2_upper"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["air_ets_mean"], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["air_ets"], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["air_ets_lower"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["air_ets_upper"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["aust_fpp1_mean"], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["aust_fpp1"], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["aust_fpp1_lower"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["aust_fpp1_upper"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["aust_ets1_mean"], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["aust_ets1"], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["aust_ets1_lower"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["aust_ets1_upper"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["aust_ets2_mean"], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["aust_ets2"], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["aust_ets2_lower"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["aust_ets2_upper"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["aust_ets3_mean"], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["aust_ets3"], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: str, /):
        """
        usage.dask: 6
        usage.prophet: 5
        usage.sklearn: 1
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["realinv", "realgdp", "cpi"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["realgdp", "cpi"]], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["realinv"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["cpi"]], /):
        """
        usage.statsmodels: 4
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["dln_inv"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["r3", "r2", "r1"]], /):
        """
        usage.statsmodels: 4
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["detN"]], /):
        """
        usage.statsmodels: 4
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["m3", "m2", "m1"]], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["v3", "v2", "v1"]], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["F3", "F2", "F1"]], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["a3", "a2", "a1"]], /):
        """
        usage.statsmodels: 6
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["detP"]], /):
        """
        usage.statsmodels: 6
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["alphahat3", "alphahat2", "alphahat1"]], /):
        """
        usage.statsmodels: 7
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["detV"]], /):
        """
        usage.statsmodels: 7
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["muhat3", "muhat2", "muhat1"]], /):
        """
        usage.statsmodels: 4
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["etahat3", "etahat2", "etahat1"]], /):
        """
        usage.statsmodels: 4
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["detVeta"]], /):
        """
        usage.statsmodels: 4
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["epshat3", "epshat2", "epshat1"]], /):
        """
        usage.statsmodels: 4
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["Veps3", "Veps2", "Veps1"]], /):
        """
        usage.statsmodels: 4
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["forecast (prev)"], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["observed"], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["impact"], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls,
        _0: List[Literal["impact", "weight", "news", "observed", "forecast (prev)"]],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["impact date"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["impacted variable"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["impact of revisions"], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["impact of news"], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls,
        _0: List[
            Literal[
                "estimate (new)",
                "total impact",
                "impact of news",
                "impact of revisions",
                "estimate (prev)",
            ]
        ],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["impact of news", "impact of revisions"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["unemp", "realgdp"]], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["lgdp"], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["V1"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["GDP"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["u1"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["u2"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["u3"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["u4"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["u5"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["u6"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["u7"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["u8"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["u9"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["u10"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["u11"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["u12"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["rstd"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["realcons", "realgdp"]], /):
        """
        usage.statsmodels: 7
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["state3", "state2", "state1"]], /):
        """
        usage.statsmodels: 4
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["eps3", "eps2", "eps1"]], /):
        """
        usage.statsmodels: 4
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["eta3", "eta2", "eta1"]], /):
        """
        usage.statsmodels: 4
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["signal3", "signal2", "signal1"]], /):
        """
        usage.statsmodels: 4
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["realinv", "realcons", "realgdp"]], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["dep1"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["sr1"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["sp3", "sp2", "sp1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["sf3", "sf2", "sf1"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["sm3", "sm2", "sm1"]], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["eps"]], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["epsvar"]], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["eta"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["etavar"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["etahat"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["detVeta"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["F1"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["unemp"], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["inc"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["inv", "inc"]], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["cpi"], /):
        """
        usage.statsmodels: 14
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["realcons"], /):
        """
        usage.statsmodels: 5
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["predict"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["realgdp", "m1", "realdpi"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["logcons", "loggdp"]], /):
        """
        usage.statsmodels: 7
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["loginv"], /):
        """
        usage.statsmodels: 4
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["sin(1,12)"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["cos(1,12)"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["sin(2,12)"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["cos(2,12)"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["sin(3,12)"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["cos(3,12)"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["lncoins"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["invt"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["SUNACTIVITY"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["quarter", "year"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["ds"], /):
        """
        usage.prophet: 43
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["floor"], /):
        """
        usage.prophet: 8
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["holiday"], /):
        """
        usage.prophet: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["cap"], /):
        """
        usage.prophet: 4
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["binary_feature"], /):
        """
        usage.prophet: 11
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["component"], /):
        """
        usage.prophet: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["col"], /):
        """
        usage.prophet: 2
        usage.seaborn: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["additive_terms"], /):
        """
        usage.prophet: 9
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["multiplicative_terms"], /):
        """
        usage.prophet: 9
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["y_scaled"], /):
        """
        usage.prophet: 8
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["ds"]], /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["weekly"], /):
        """
        usage.prophet: 4
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["yhat"], /):
        """
        usage.prophet: 13
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["trend"], /):
        """
        usage.prophet: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["trend", "ds"]], /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls, _0: List[Literal["yhat_upper", "yhat_lower", "yhat", "ds"]], /
    ):
        """
        usage.prophet: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["cutoff"], /):
        """
        usage.prophet: 12
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["y_x"], /):
        """
        usage.prophet: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["y_y"], /):
        """
        usage.prophet: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["extra"], /):
        """
        usage.prophet: 9
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["is_conditional_week"], /):
        """
        usage.prophet: 4
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["is_conditional_week", "extra", "ds"]], /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["conditional_weekly"], /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["monthly"], /):
        """
        usage.prophet: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["cap_scaled"], /):
        """
        usage.prophet: 5
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["floor", "cap", "ds"]], /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["floor", "cap", "trend", "ds"]], /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["yhat", "ds"]], /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["horizon"], /):
        """
        usage.prophet: 21
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["mse"], /):
        """
        usage.prophet: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["rmse"], /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["mae"], /):
        """
        usage.prophet: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["mape"], /):
        """
        usage.prophet: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["mdape"], /):
        """
        usage.prophet: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["yhat_lower"], /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["yhat_upper"], /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["coverage"], /):
        """
        usage.prophet: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["numeric_feature"], /):
        """
        usage.prophet: 13
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["numeric_feature2"], /):
        """
        usage.prophet: 10
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["binary_feature2"], /):
        """
        usage.prophet: 12
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["yearly"], /):
        """
        usage.prophet: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["constant_feature"], /):
        """
        usage.prophet: 5
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["special_day_delim_+0"]], /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["special_day"], /):
        """
        usage.prophet: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["lower_window"], /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["upper_window"], /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["Christmas Day"], /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["Columbus Day"], /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["Independence Day"], /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["Labor Day"], /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["Memorial Day"], /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["New Year's Day"], /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["Thanksgiving"], /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["Veterans Day"], /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["holidays"], /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["seans-bday"], /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls, _0: List[Literal["seans-bday_delim_+1", "seans-bday_delim_+0"]], /
    ):
        """
        usage.prophet: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["xmas_delim_-1", "xmas_delim_+0"]], /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["daily"], /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["col0"], /):
        """
        usage.modin: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["col4"], /):
        """
        usage.modin: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["col6"], /):
        """
        usage.modin: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["col8"], /):
        """
        usage.modin: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["col10"], /):
        """
        usage.modin: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["col12"], /):
        """
        usage.modin: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["col14"], /):
        """
        usage.modin: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["__reduced__"], /):
        """
        usage.modin: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["day"], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["sex"], /):
        """
        usage.seaborn: 2
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["smoker"], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["total_bill"], /):
        """
        usage.seaborn: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["sepal_length"], /):
        """
        usage.hvplot: 1
        usage.seaborn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["sepal_width"], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["petal_length"], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["petal_width"], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls,
        _0: List[Literal["petal_width", "petal_length", "sepal_width", "sepal_length"]],
        /,
    ):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["kind"], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["diet"], /):
        """
        usage.seaborn: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: numpy.ndarray, /):
        """
        usage.dask: 8
        usage.seaborn: 1
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["deck"], /):
        """
        usage.seaborn: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["tip"], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["size"], /):
        """
        usage.seaborn: 10
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["b_bool"], /):
        """
        usage.seaborn: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["hasna"], /):
        """
        usage.seaborn: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["x", "b"]], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["hue"], /):
        """
        usage.seaborn: 13
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["x", "y"]], /):
        """
        usage.dask: 2
        usage.seaborn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["x", "z"]], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["y", "z"]], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["z", "x"]], /):
        """
        usage.dask: 4
        usage.seaborn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["edges"], /):
        """
        usage.seaborn: 4
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["heights"], /):
        """
        usage.seaborn: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["widths"], /):
        """
        usage.seaborn: 5
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["a", "y", "x"]], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["a", "x", "y"]], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["hue", "y", "x"]], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["a", "z", "x"]], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["a", "z", "y"]], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["a", "x", "z"]], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["a", "y", "z"]], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["Y"], /):
        """
        usage.seaborn: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["W"], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["Z", "Y", "X"]], /):
        """
        usage.seaborn: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["X", "Z", "Y"]], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["u"], /):
        """
        usage.seaborn: 4
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["@index"], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["@values"], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["@columns"], /):
        """
        usage.seaborn: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["style", "hue", "y", "x"]], /):
        """
        usage.seaborn: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["style"], /):
        """
        usage.seaborn: 9
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["a_cat"], /):
        """
        usage.seaborn: 4
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["s_cat"], /):
        """
        usage.seaborn: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["s"], /):
        """
        usage.seaborn: 5
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["s", "a"]], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["b", "s", "a"]], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["row"], /):
        """
        usage.seaborn: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["hue", "x"]], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Tuple[Literal["hue"], Literal["c"]]], /):
        """
        usage.seaborn: 4
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Tuple[Literal["hue"], Literal["a"]]], /):
        """
        usage.seaborn: 4
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Tuple[Literal["hue"], Literal["b"]]], /):
        """
        usage.seaborn: 4
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["_"], /):
        """
        usage.seaborn: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls,
        _0: Tuple[
            Tuple[Literal["hue"], Literal["c"]], Tuple[Literal["col"], Literal["_"]]
        ],
        /,
    ):
        """
        usage.seaborn: 4
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls,
        _0: Tuple[
            Tuple[Literal["hue"], Literal["a"]], Tuple[Literal["col"], Literal["_"]]
        ],
        /,
    ):
        """
        usage.seaborn: 4
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls,
        _0: Tuple[
            Tuple[Literal["hue"], Literal["b"]], Tuple[Literal["col"], Literal["_"]]
        ],
        /,
    ):
        """
        usage.seaborn: 4
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls,
        _0: Tuple[
            Tuple[Literal["hue"], Literal["c"]], Tuple[Literal["col"], numpy.int64]
        ],
        /,
    ):
        """
        usage.seaborn: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls,
        _0: Tuple[
            Tuple[Literal["hue"], Literal["b"]], Tuple[Literal["col"], numpy.int64]
        ],
        /,
    ):
        """
        usage.seaborn: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls,
        _0: Tuple[
            Tuple[Literal["hue"], Literal["a"]], Tuple[Literal["col"], numpy.int64]
        ],
        /,
    ):
        """
        usage.seaborn: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["_col_"], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["_row_"], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["low"], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["high"], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["units"], /):
        """
        usage.seaborn: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["style", "y", "x"]], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["size", "y", "x"]], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["size", "style", "hue", "y", "x"]], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["size", "hue", "y", "x"]], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["color"], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["clarity"], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["cut"], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["month"], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["category"], /):
        """
        usage.hvplot: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["upper"], /):
        """
        usage.hvplot: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["lower"], /):
        """
        usage.hvplot: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["_color"], /):
        """
        usage.hvplot: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["number"], /):
        """
        usage.hvplot: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["geometry"], /):
        """
        usage.geopandas: 5
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["geom2"], /):
        """
        usage.geopandas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["geom3"], /):
        """
        usage.geopandas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["lon"], /):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["lat"], /):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["geom_list"], /):
        """
        usage.geopandas: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["sequence_accession"], /):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["cities"], /):
        """
        usage.pyjanitor: 4
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls, _0: List[Literal["decorated-elephant", "Bell__Chart", "a"]], /
    ):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["decorated-elephant"], /):
        """
        usage.pyjanitor: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["hire_date"], /):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["bell_chart"], /):
        """
        usage.pyjanitor: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["names"], /):
        """
        usage.dask: 2
        usage.pyjanitor: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["animals@#$%^"], /):
        """
        usage.pyjanitor: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["Bell__Chart"], /):
        """
        usage.pyjanitor: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls, _0: List[Literal["cities", "animals@#$%^", "decorated_elephant", "a"]], /
    ):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["cities", "animals@#$%^"]], /):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["bell_chart", "a"]], /):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls, _0: List[Literal["cities", "animals@#$%^", "decorated_elephant"]], /
    ):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["cities", "Bell__Chart", "a"]], /):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["animals@#$%^", "a", "Bell__Chart"]], /):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["date1"], /):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["another"], /):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["column"], /):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["id", "name"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["bb"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["path"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["filename"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["fruit"], /):
        """
        usage.dask: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["numbers"], /):
        """
        usage.dask: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["more_numbers"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["integers"], /):
        """
        usage.dask: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["Date"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["date_time"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["A_B"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["B_"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["idx"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["dt_col"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["str_col"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["string_col"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["int_col"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["bool", "float", "int"]], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["float", "int"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["timedelta"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["w"], /):
        """
        usage.dask: 6
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["cat"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["y_"], /):
        """
        usage.dask: 5
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["_partitions"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["_index"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["tz"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: numpy.int64, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["cint"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["cdt", "clfoat", "cstr"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["cstr", "cint"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["cdt"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["bools"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["categorical_nans"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["categorical_binary"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["unique_id"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Tuple[Literal["A"], Literal["0"]], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Tuple[Literal["A", "B"], Literal["0", "1"]]], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: object, /):
        """
        usage.dask: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["Name"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["__series__"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["2-count"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["22"], /):
        """
        usage.dask: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["3-count"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["23"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["33"], /):
        """
        usage.dask: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["a", "c", "b"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["0-count"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["00"], /):
        """
        usage.dask: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["1-count"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["01"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["11"], /):
        """
        usage.dask: 3
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["AA"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["AB", "AA"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["AA"], /):
        """
        usage.dask: 4
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["AB"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["a", "d", "c"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["03"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["13"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["b", "a", "d", "c"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["02"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["12"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["cc"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["g0"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["g1"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: pandas.core.indexes.numeric.Int64Index, /):
        """
        usage.dask: 1
        usage.networkx: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["group"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["first_bit"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["X", "A"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["2011-01-02"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls,
        _0: slice[Literal["2011-01-02"], Literal["2011-01-10"], Literal["2011-01-02"]],
        /,
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["2011-01"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["2011"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls, _0: slice[Literal["2011-01"], Literal["2012-05"], Literal["2011-01"]], /
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls, _0: slice[Literal["2011"], Literal["2015"], Literal["2011"]], /
    ):
        """
        usage.dask: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["k"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["e"]], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["e", "d"]], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["E"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["G"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["H"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["I"], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["cluster"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["a_a"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["A_a"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["i32"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["f32", "bool", "cat"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["notz"], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["name", "id"]], /):
        """
        usage.dask: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["e", "d", "b", "a"]], /):
        """
        usage.dask: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["first"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["second"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["col_str"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["target"]], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls,
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
    @classmethod
    def __getitem__(cls, _0: List[Literal["Jumps", "Situps", "Chins"]], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["Pulse", "Waist", "Weight"]], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls,
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
    @classmethod
    def __getitem__(cls, _0: Literal["sepallength"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["sepalwidth"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["petallength"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["petalwidth"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(
        cls,
        _0: List[Literal["petalwidth", "petallength", "sepalwidth", "sepallength"]],
        /,
    ):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["class", "sepalwidth", "sepallength"]], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["petallength", "petalwidth"]], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["family"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["product-type"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["steel"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["carbon"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["hardness"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["temper_rolling"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["condition"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["formability"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["strength"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["non-ageing"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["surface-finish"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["surface-quality"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["enamelability"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["bc"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["bf"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["bt"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["bw%2Fme"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["bl"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["m"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["chrom"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["phos"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["cbond"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["marvi"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["exptl"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["ferro"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["corr"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["lustre"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["jurofm"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["p"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["shape"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["thick"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["width"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["len"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["oil"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["bore"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["packing"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["vendor"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["MYCT"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["MMIN"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["MMAX"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["CACH"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["CHMIN"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["CHMAX"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["age"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["workclass"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["fnlwgt:"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["education:"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["education-num:"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["marital-status:"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["occupation:"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["relationship:"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["race:"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["sex:"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["capital-gain:"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["capital-loss:"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["hours-per-week:"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["native-country:"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["DYRK1A_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["ITSN1_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["BDNF_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["NR1_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["NR2A_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["pAKT_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["pBRAF_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["pCAMKII_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["pCREB_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["pELK_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["pERK_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["pJNK_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["PKCA_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["pMEK_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["pNR1_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["pNR2A_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["pNR2B_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["pPKCAB_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["pRSK_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["AKT_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["BRAF_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["CAMKII_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["CREB_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["ELK_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["ERK_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["GSK3B_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["JNK_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["MEK_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["TRKA_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["RSK_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["APP_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["Bcatenin_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["SOD1_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["MTOR_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["P38_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["pMTOR_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["DSCR1_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["AMPKA_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["NR2B_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["pNUMB_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["RAPTOR_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["TIAM1_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["pP70S6_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["NUMB_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["P70S6_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["pGSK3B_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["pPKCG_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["CDK5_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["S6_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["ADARB1_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["AcetylH3K9_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["RRP1_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["BAX_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["ARC_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["ERBB4_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["nNOS_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["Tau_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["GFAP_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["GluR3_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["GluR4_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["IL1B_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["P3525_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["pCASP9_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["PSD95_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["SNCA_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["Ubiquitin_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["pGSK3B_Tyr216_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["SHH_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["BAD_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["BCL2_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["pS6_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["pCFOS_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["SYP_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["H3AcK18_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["EGR1_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["H3MeK4_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["CaNA_N"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["BH_LowPeakAmp"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["BH_LowPeakBPM"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["BH_HighPeakAmp"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["BH_HighPeakBPM"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["BH_HighLowRatio"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["BHSUM1"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["BHSUM2"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["BHSUM3"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["amazed.suprised"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["happy.pleased"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["relaxing.calm"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["quiet.still"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["sad.lonely"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["angry.aggresive"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["pclass"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["survived"], /):
        """
        usage.sklearn: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["sibsp"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["parch"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["ticket"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["fare"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["cabin"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["embarked"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["boat"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["body"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["home.dest"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: pandas.core.indexes.range.RangeIndex, /):
        """
        usage.networkx: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["source"], /):
        """
        usage.networkx: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["cost"], /):
        """
        usage.networkx: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["St"], /):
        """
        usage.networkx: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["Co"], /):
        """
        usage.networkx: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["Mi"], /):
        """
        usage.networkx: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["O"], /):
        """
        usage.networkx: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["misspell"], /):
        """
        usage.networkx: 1
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: Literal["target"], /):
        """
        usage.networkx: 2
        """
        ...

    @overload
    @classmethod
    def __getitem__(cls, _0: List[Literal["B", "C", "A"]], /):
        """
        usage.networkx: 1
        """
        ...

    @classmethod
    def __getitem__(cls, _0: object, /):
        """
        usage.dask: 471
        usage.geopandas: 21
        usage.hvplot: 32
        usage.koalas: 1033
        usage.modin: 19
        usage.networkx: 22
        usage.prophet: 319
        usage.pyjanitor: 67
        usage.seaborn: 406
        usage.sklearn: 213
        usage.statsmodels: 1071
        usage.xarray: 8
        """
        ...

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

    @overload
    @classmethod
    def __ne__(cls, _0: pandas.core.frame.DataFrame, /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __ne__(cls, _0: int, /):
        """
        usage.prophet: 1
        """
        ...

    @classmethod
    def __ne__(cls, _0: Union[pandas.core.frame.DataFrame, int, type], /):
        """
        usage.dask: 3
        usage.prophet: 1
        usage.statsmodels: 2
        """
        ...

    @overload
    @classmethod
    def __rmod__(cls, _0: Literal["Unsupported type %s"], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def __rmod__(cls, _0: numpy.timedelta64, /):
        """
        usage.pandas: 1
        """
        ...

    @overload
    @classmethod
    def __rmod__(cls, _0: str, /):
        """
        usage.sklearn: 1
        """
        ...

    @classmethod
    def __rmod__(cls, _0: Union[str, numpy.timedelta64], /):
        """
        usage.koalas: 1
        usage.pandas: 1
        usage.sklearn: 1
        """
        ...

    @classmethod
    def _get_axis_number(cls, /, axis: int):
        """
        usage.modin: 1
        """
        ...

    @overload
    @classmethod
    def from_dict(cls, /, data: Dict[str, numpy.ndarray]):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def from_dict(
        cls,
        /,
        data: Dict[Literal["a"], List[str]],
        orient: Literal["columns"],
        dtype: None,
        columns: None,
    ):
        """
        usage.modin: 1
        """
        ...

    @overload
    @classmethod
    def from_dict(cls, /, data: List[Dict[Literal["b", "a"], Union[float, int]]]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
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

    @overload
    @classmethod
    def from_dict(
        cls, /, data: Dict[Literal["Mi", "Co", "St", "D", "O"], List[Union[str, int]]]
    ):
        """
        usage.networkx: 1
        """
        ...

    @classmethod
    def from_dict(
        cls,
        /,
        data: Union[
            Dict[str, Union[List[Union[int, str]], numpy.ndarray]],
            List[
                Dict[
                    Literal["y", "x", "b", "a"],
                    Union[Literal["a", "b", "c", "d"], float, int],
                ]
            ],
        ],
        orient: Literal["columns"] = ...,
        dtype: None = ...,
        columns: None = ...,
    ):
        """
        usage.dask: 1
        usage.geopandas: 1
        usage.modin: 1
        usage.networkx: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    @classmethod
    def from_records(
        cls,
        /,
        data: Dict[Literal["A"], List[int]],
        index: None,
        exclude: None,
        columns: None,
        coerce_float: bool,
        nrows: None,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_records(
        cls,
        /,
        data: List[Tuple[int, int]],
        index: None,
        exclude: None,
        columns: None,
        coerce_float: bool,
        nrows: None,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_records(
        cls,
        /,
        data: numpy.ndarray,
        index: None,
        exclude: None,
        columns: None,
        coerce_float: bool,
        nrows: None,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_records(cls, /, data: Dict[Literal["A"], List[int]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_records(cls, /, data: List[Tuple[int, int]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_records(cls, /, data: numpy.ndarray):
        """
        usage.koalas: 1
        usage.statsmodels: 5
        """
        ...

    @overload
    @classmethod
    def from_records(
        cls,
        /,
        data: List[Tuple[int, int]],
        index: List[int],
        exclude: None,
        columns: None,
        coerce_float: bool,
        nrows: None,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_records(cls, /, data: List[Tuple[int, int]], index: List[int]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_records(
        cls,
        /,
        data: Dict[Literal["B", "A"], List[int]],
        index: None,
        exclude: List[Literal["B"]],
        columns: None,
        coerce_float: bool,
        nrows: None,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_records(
        cls, /, data: Dict[Literal["B", "A"], List[int]], exclude: List[Literal["B"]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_records(
        cls,
        /,
        data: Dict[Literal["B", "A"], List[int]],
        index: None,
        exclude: None,
        columns: List[Literal["A"]],
        coerce_float: bool,
        nrows: None,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_records(
        cls, /, data: Dict[Literal["B", "A"], List[int]], columns: List[Literal["A"]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_records(
        cls,
        /,
        data: List[Tuple[int, int]],
        index: None,
        exclude: None,
        columns: None,
        coerce_float: bool,
        nrows: int,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_records(cls, /, data: List[Tuple[int, int]], nrows: int):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def from_records(cls, /, data: numpy.recarray):
        """
        usage.statsmodels: 4
        """
        ...

    @classmethod
    def from_records(
        cls,
        /,
        data: Union[
            numpy.ndarray,
            numpy.recarray,
            Dict[Literal["A", "B"], List[int]],
            List[Tuple[int, int]],
        ],
        index: Union[None, List[int]] = ...,
        exclude: Union[None, List[Literal["B"]]] = ...,
        columns: Union[None, List[Literal["A"]]] = ...,
        coerce_float: bool = ...,
        nrows: Union[int, None] = ...,
    ):
        """
        usage.koalas: 14
        usage.statsmodels: 9
        """
        ...

    # usage.dask: 40
    # usage.koalas: 72
    A: object

    # usage.dask: 3
    A_a: object

    # usage.dask: 15
    # usage.koalas: 20
    B: object

    # usage.dask: 4
    # usage.koalas: 11
    C: object

    # usage.dask: 2
    Date: pandas.core.series.Series

    # usage.dask: 1
    F: object

    # usage.statsmodels: 2
    Foo: object

    # usage.statsmodels: 15
    Group: object

    # usage.statsmodels: 1
    Item: object

    # usage.dask: 1
    Name: object

    # usage.statsmodels: 1
    Package: object

    # usage.statsmodels: 1
    SD: object

    # usage.statsmodels: 2
    SUNACTIVITY: object

    # usage.statsmodels: 14
    Status: object

    # usage.dask: 5
    # usage.koalas: 1
    # usage.seaborn: 4
    # usage.statsmodels: 39
    # usage.xarray: 1
    T: object

    # usage.statsmodels: 2
    Variance: object

    # usage.statsmodels: 4
    Village: object

    # usage.dask: 2
    X: object

    # usage.statsmodels: 1
    YEAR: object

    # usage.statsmodels: 1
    Year: object

    # usage.dask: 7
    # usage.statsmodels: 1
    __class__: object

    # usage.pyjanitor: 1
    __dict__: object

    # usage.dask: 2
    _constructor: object

    # usage.dask: 2
    _constructor_sliced: object

    # usage.dask: 1
    _data: object

    # usage.dask: 2
    _partitions: object

    # usage.dask: 114
    # usage.koalas: 132
    # usage.seaborn: 9
    # usage.statsmodels: 3
    a: pandas.core.series.Series

    # usage.koalas: 1
    aa: object

    # usage.pyjanitor: 1
    add_column: object

    # usage.dask: 1
    amount: object

    # usage.koalas: 1
    animal: object

    # usage.koalas: 11
    at: object

    # usage.hvplot: 2
    # usage.koalas: 2
    # usage.modin: 3
    axes: object

    # usage.dask: 63
    # usage.koalas: 99
    # usage.seaborn: 2
    # usage.statsmodels: 1
    b: object

    # usage.seaborn: 1
    b_bool: object

    # usage.dask: 1
    # usage.koalas: 9
    # usage.seaborn: 3
    # usage.statsmodels: 3
    c: object

    # usage.statsmodels: 1
    c1: object

    # usage.statsmodels: 1
    c2: object

    # usage.statsmodels: 3
    coef: object

    # usage.dask: 1
    col1: object

    # usage.dask: 1
    col2: object

    # usage.dask: 142
    # usage.geopandas: 3
    # usage.hvplot: 17
    # usage.koalas: 676
    # usage.modin: 17
    # usage.networkx: 3
    # usage.prophet: 14
    # usage.pyjanitor: 42
    # usage.seaborn: 18
    # usage.sklearn: 19
    # usage.statsmodels: 235
    # usage.xarray: 9
    columns: object

    # usage.dask: 4
    # usage.koalas: 2
    # usage.seaborn: 3
    # usage.statsmodels: 1
    d: object

    # usage.seaborn: 2
    dataset: object

    # usage.seaborn: 1
    deck: object

    # usage.statsmodels: 2
    design_info: object

    # usage.dask: 3
    # usage.seaborn: 1
    div: object

    # usage.dask: 3
    # usage.statsmodels: 1
    divide: object

    # usage.koalas: 1
    dt: object

    # usage.dask: 2
    dt_col: object

    # usage.dask: 25
    # usage.geopandas: 1
    # usage.koalas: 19
    # usage.modin: 1
    # usage.pyjanitor: 1
    # usage.sklearn: 24
    # usage.statsmodels: 4
    dtypes: object

    # usage.dask: 2
    # usage.koalas: 4
    e: object

    # usage.seaborn: 1
    embark_town: object

    # usage.dask: 4
    # usage.modin: 2
    # usage.seaborn: 2
    empty: object

    # usage.statsmodels: 1
    entry: object

    # usage.statsmodels: 1
    exposure: object

    # usage.dask: 3
    f: object

    # usage.statsmodels: 1
    fake: object

    # usage.sklearn: 1
    fit: object

    # usage.koalas: 1
    foo: object

    # usage.dask: 2
    fruit: object

    # usage.seaborn: 17
    g: pandas.core.series.Series

    # usage.geopandas: 1
    geometry: object

    # usage.statsmodels: 1
    grps: object

    # usage.seaborn: 6
    h: pandas.core.series.Series

    # usage.prophet: 2
    holiday: object

    # usage.hvplot: 82
    hvplot: object

    # usage.dask: 2
    i32: object

    # usage.koalas: 3
    iat: object

    # usage.dask: 2
    # usage.koalas: 1
    id: object

    # usage.dask: 46
    # usage.koalas: 23
    # usage.modin: 3
    # usage.prophet: 5
    # usage.pyjanitor: 2
    # usage.seaborn: 9
    # usage.sklearn: 14
    # usage.statsmodels: 366
    # usage.xarray: 2
    iloc: object

    # usage.dask: 197
    # usage.hvplot: 8
    # usage.koalas: 57
    # usage.modin: 8
    # usage.networkx: 2
    # usage.prophet: 4
    # usage.pyjanitor: 4
    # usage.seaborn: 12
    # usage.sklearn: 3
    # usage.statsmodels: 358
    # usage.xarray: 12
    index: object

    # usage.statsmodels: 2
    infl: object

    # usage.statsmodels: 1
    intcol: object

    # usage.koalas: 2
    kurtosis: object

    # usage.dask: 71
    # usage.geopandas: 1
    # usage.koalas: 103
    # usage.prophet: 2
    # usage.pyjanitor: 11
    # usage.seaborn: 16
    # usage.sklearn: 1
    # usage.statsmodels: 291
    # usage.xarray: 3
    loc: object

    # usage.koalas: 11
    max_speed: object

    # usage.statsmodels: 1
    mean_ci_lower: object

    # usage.statsmodels: 1
    mean_ci_upper: object

    # usage.statsmodels: 1
    mean_se: object

    # usage.statsmodels: 4
    multiply: object

    # usage.koalas: 1
    name: object

    # usage.dask: 3
    # usage.sklearn: 4
    # usage.statsmodels: 26
    ndim: object

    # usage.statsmodels: 7
    offset: object

    # usage.dask: 2
    path: object

    # usage.hvplot: 3
    # usage.koalas: 12
    plot: object

    # usage.dask: 3
    rdiv: object

    # usage.koalas: 1
    rep: object

    # usage.statsmodels: 5
    rw: object

    # usage.statsmodels: 1
    s: object

    # usage.koalas: 7
    sale: object

    # usage.statsmodels: 1
    se: object

    # usage.statsmodels: 6
    season: object

    # usage.statsmodels: 1
    seasonal: object

    # usage.statsmodels: 1
    ses: object

    # usage.geopandas: 3
    set_geometry: object

    # usage.koalas: 4
    shield: object

    # usage.dask: 2
    # usage.seaborn: 1
    # usage.sklearn: 2
    # usage.statsmodels: 8
    size: object

    # usage.statsmodels: 2
    status: object

    # usage.dask: 12
    str_col: object

    # usage.statsmodels: 7
    strata: object

    # usage.dask: 4
    string_col: object

    # usage.koalas: 1
    style: object

    # usage.statsmodels: 1
    t: object

    # usage.hvplot: 5
    time: object

    # usage.statsmodels: 7
    trend: object

    # usage.statsmodels: 1
    tvalues: object

    # usage.dask: 1
    tz: object

    # usage.dask: 2
    value: object

    # usage.dask: 33
    # usage.geopandas: 2
    # usage.hvplot: 2
    # usage.koalas: 2
    # usage.modin: 1
    # usage.networkx: 1
    # usage.prophet: 4
    # usage.seaborn: 8
    # usage.sklearn: 1
    # usage.statsmodels: 209
    # usage.xarray: 7
    values: object

    # usage.statsmodels: 1
    violent: object

    # usage.dask: 7
    w: pandas.core.series.Series

    # usage.dask: 82
    # usage.hvplot: 3
    # usage.koalas: 25
    # usage.prophet: 1
    # usage.seaborn: 8
    # usage.statsmodels: 13
    x: pandas.core.series.Series

    # usage.statsmodels: 1
    x1: object

    # usage.statsmodels: 1
    x2: object

    # usage.statsmodels: 2
    x3: object

    # usage.statsmodels: 1
    x4: object

    # usage.statsmodels: 1
    x5: object

    # usage.dask: 39
    # usage.koalas: 11
    # usage.seaborn: 7
    # usage.statsmodels: 16
    y: pandas.core.series.Series

    # usage.statsmodels: 2
    y_est: object

    # usage.statsmodels: 2
    y_est_se: object

    # usage.statsmodels: 2
    y_mgcv_gcv: object

    # usage.statsmodels: 1
    ybin: object

    # usage.statsmodels: 1
    ybin_est: object

    # usage.koalas: 1
    # usage.statsmodels: 2
    year: pandas.core.series.Series

    # usage.statsmodels: 2
    year_cen: object

    # usage.dask: 4
    # usage.koalas: 1
    z: object

    # usage.statsmodels: 1
    z1: object

    @overload
    def __add__(self, _0: int, /):
        """
        usage.dask: 17
        usage.koalas: 22
        """
        ...

    @overload
    def __add__(self, _0: pandas.core.series.Series, /):
        """
        usage.koalas: 48
        usage.statsmodels: 2
        """
        ...

    @overload
    def __add__(self, _0: pandas.core.frame.DataFrame, /):
        """
        usage.dask: 1
        usage.koalas: 8
        usage.statsmodels: 4
        """
        ...

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

    def __add__(self, _0: object, /):
        """
        usage.dask: 24
        usage.koalas: 78
        usage.pandas: 37
        usage.statsmodels: 6
        """
        ...

    def __array_wrap__(self, /, result: numpy.ndarray):
        """
        usage.dask: 2
        """
        ...

    @overload
    def __contains__(self, _0: Literal["__index__"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["unknown"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["abcde"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["fghij"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["klmno"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["pqrst"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["uvwxy"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["string_var"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["apple"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["y"], /):
        """
        usage.prophet: 3
        usage.seaborn: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["ds"], /):
        """
        usage.prophet: 2
        """
        ...

    @overload
    def __contains__(self, _0: Literal["holiday"], /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["lower_window"], /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["upper_window"], /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["floor"], /):
        """
        usage.prophet: 3
        """
        ...

    @overload
    def __contains__(self, _0: Literal["cap"], /):
        """
        usage.prophet: 2
        """
        ...

    @overload
    def __contains__(self, _0: Literal["binary_feature"], /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["additive_terms"], /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["multiplicative_terms"], /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["extra"], /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["is_conditional_week"], /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["yhat_lower"], /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["yhat_upper"], /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["numeric_feature"], /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["numeric_feature2"], /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["binary_feature2"], /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["constant_feature"], /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["t"], /):
        """
        usage.prophet: 1
        usage.seaborn: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["y_scaled"], /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["x"], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["a"], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["c"], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["a_cat"], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["s_cat"], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["s"], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["what"], /):
        """
        usage.seaborn: 2
        """
        ...

    @overload
    def __contains__(self, _0: Literal["b"], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["z"], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["_"], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["f"], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["style"], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["hue"], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["size"], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["u"], /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def __contains__(self, _0: Literal["location"], /):
        """
        usage.geopandas: 1
        """
        ...

    def __contains__(self, _0: str, /):
        """
        usage.geopandas: 1
        usage.prophet: 26
        usage.seaborn: 18
        usage.statsmodels: 9
        """
        ...

    @overload
    def __eq__(self, _0: int, /):
        """
        usage.dask: 1
        usage.statsmodels: 3
        """
        ...

    @overload
    def __eq__(self, _0: pandas.core.frame.DataFrame, /):
        """
        usage.dask: 8
        usage.hvplot: 4
        usage.prophet: 2
        usage.statsmodels: 2
        """
        ...

    @overload
    def __eq__(self, _0: pandas.core.series.Series, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __eq__(self, _0: numpy.float64, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __eq__(self, _0: numpy.ndarray, /):
        """
        usage.pandas: 6
        """
        ...

    def __eq__(
        self,
        _0: Union[
            pandas.core.frame.DataFrame,
            int,
            numpy.float64,
            pandas.core.series.Series,
            numpy.ndarray,
        ],
        /,
    ):
        """
        usage.dask: 9
        usage.hvplot: 4
        usage.pandas: 6
        usage.prophet: 2
        usage.statsmodels: 7
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
    def __gt__(self, _0: int, /):
        """
        usage.koalas: 5
        """
        ...

    @overload
    def __gt__(self, _0: float, /):
        """
        usage.statsmodels: 1
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
        self,
        _0: Union[
            pandas.core.series.Series, float, int, numpy.ndarray, numpy.timedelta64
        ],
        /,
    ):
        """
        usage.dask: 1
        usage.koalas: 5
        usage.pandas: 4
        usage.statsmodels: 1
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
        usage.modin: 1
        usage.pyjanitor: 1
        usage.seaborn: 4
        usage.statsmodels: 11
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
    def __lt__(self, _0: int, /):
        """
        usage.dask: 2
        usage.koalas: 5
        """
        ...

    @overload
    def __lt__(self, _0: float, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __lt__(self, _0: pandas.core.series.Series, /):
        """
        usage.dask: 1
        """
        ...

    def __lt__(self, _0: Union[pandas.core.series.Series, int, float], /):
        """
        usage.dask: 3
        usage.koalas: 5
        usage.statsmodels: 1
        """
        ...

    def __matmul__(self, _0: numpy.ndarray, /):
        """
        usage.statsmodels: 3
        """
        ...

    def __mod__(self, _0: numpy.timedelta64, /):
        """
        usage.pandas: 1
        """
        ...

    @overload
    def __mul__(self, _0: pandas.core.series.Series, /):
        """
        usage.statsmodels: 4
        """
        ...

    @overload
    def __mul__(self, _0: int, /):
        """
        usage.sklearn: 2
        usage.statsmodels: 3
        """
        ...

    @overload
    def __mul__(self, _0: numpy.float64, /):
        """
        usage.statsmodels: 2
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

    def __mul__(self, _0: object, /):
        """
        usage.pandas: 20
        usage.sklearn: 4
        usage.statsmodels: 9
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
        usage.seaborn: 1
        """
        ...

    @overload
    def __pow__(self, _0: int, /):
        """
        usage.dask: 2
        usage.statsmodels: 1
        """
        ...

    @overload
    def __pow__(self, _0: numpy.timedelta64, /):
        """
        usage.pandas: 1
        """
        ...

    def __pow__(self, _0: Union[int, numpy.timedelta64], /):
        """
        usage.dask: 2
        usage.pandas: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    def __radd__(self, _0: pandas.core.frame.DataFrame, /):
        """
        usage.dask: 1
        usage.koalas: 8
        usage.statsmodels: 4
        """
        ...

    @overload
    def __radd__(self, _0: int, /):
        """
        usage.statsmodels: 2
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

    def __radd__(self, _0: object, /):
        """
        usage.dask: 2
        usage.koalas: 8
        usage.pandas: 30
        usage.statsmodels: 6
        """
        ...

    def __repr__(self, /):
        """
        usage.koalas: 1
        """
        ...

    def __rfloordiv__(self, _0: numpy.timedelta64, /):
        """
        usage.pandas: 1
        """
        ...

    @overload
    def __rmul__(self, _0: int, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __rmul__(self, _0: Union[numpy.ndarray, numpy.timedelta64, numpy.int64], /):
        """
        usage.pandas: 16
        """
        ...

    def __rmul__(
        self, _0: Union[numpy.int64, numpy.timedelta64, numpy.ndarray, int], /
    ):
        """
        usage.pandas: 16
        usage.statsmodels: 1
        """
        ...

    def __ror__(self, _0: pandas.core.frame.DataFrame, /):
        """
        usage.dask: 2
        usage.seaborn: 1
        """
        ...

    def __rpow__(self, _0: numpy.timedelta64, /):
        """
        usage.pandas: 1
        """
        ...

    @overload
    def __rsub__(self, _0: pandas.core.frame.DataFrame, /):
        """
        usage.dask: 1
        usage.koalas: 2
        usage.statsmodels: 6
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

    def __rsub__(
        self,
        _0: Union[
            pandas.core.frame.DataFrame,
            numpy.ndarray,
            numpy.datetime64,
            numpy.timedelta64,
        ],
        /,
    ):
        """
        usage.dask: 1
        usage.koalas: 2
        usage.pandas: 26
        usage.statsmodels: 6
        """
        ...

    @overload
    def __rtruediv__(self, _0: pandas.core.frame.DataFrame, /):
        """
        usage.dask: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    def __rtruediv__(self, _0: Union[numpy.ndarray, numpy.timedelta64], /):
        """
        usage.pandas: 20
        """
        ...

    def __rtruediv__(
        self,
        _0: Union[pandas.core.frame.DataFrame, numpy.ndarray, numpy.timedelta64],
        /,
    ):
        """
        usage.dask: 1
        usage.pandas: 20
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["__index_level_0__"], _1: pandas.core.series.Series, /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["A"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 4
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["B"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 2
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["x"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 2
        usage.koalas: 2
        usage.seaborn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["(x, y)"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["0"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["dates"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        usage.pyjanitor: 2
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["__index_level_1__"], _1: pandas.core.series.Series, /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["animal"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["Col1"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["Col2"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["Col3"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["longitude"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["latitude"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["dogs"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["cats"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["col1"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 2
        usage.pyjanitor: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["col2"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["a"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 2
        usage.koalas: 6
        usage.pyjanitor: 7
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["b"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 3
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["c"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 2
        usage.koalas: 4
        usage.pyjanitor: 1
        usage.sklearn: 2
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["d"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 1
        usage.koalas: 2
        usage.pyjanitor: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["e"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 1
        usage.koalas: 3
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["score"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["kids"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["age"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["angles"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["degrees"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["C"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["col3"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["col4"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["col5"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["col6"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["1"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["temp_c"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["y"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 4
        usage.koalas: 1
        usage.prophet: 3
        usage.seaborn: 1
        usage.statsmodels: 4
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["z"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 4
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["w"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 1
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["Person"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["Age"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["Single"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["numeric1"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["numeric2"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["object"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["name"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["toy"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["born"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["id"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 1
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["D"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["one"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["two"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["three"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["2"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        usage.pyjanitor: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["lkey"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["value"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["rkey"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["int_col"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["text_col"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["float_col"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["num_legs"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["num_wings"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["species"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["population"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["int"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["float"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["key"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["max_speed"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["shield"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["X"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["Y"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["FR"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["GR"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["IT"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["foo"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["bar"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["baz"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["zoo"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["E"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["class"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        usage.sklearn: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["0.5"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["C C"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["http_status"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["response_time"], _1: pandas.core.series.Series, /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["prices"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["(X, A)"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["(X, B)"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["(Y, C)"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["(Y, D)"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["weapon"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["(speed, max)"], _1: pandas.core.series.Series, /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["(species, type)"], _1: pandas.core.series.Series, /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["num_specimen_seen"], _1: pandas.core.series.Series, /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["month"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["year"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        usage.statsmodels: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["sale"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["weight"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["height"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["(weight, kg)"], _1: pandas.core.series.Series, /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["(weight, pounds)"], _1: pandas.core.series.Series, /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["(height, m)"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["country"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["code"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["mask"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["locomotion"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["str"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["int1"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["int2"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["Animal"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["Max Speed"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["category"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["col 1"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["col 2"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["animal_1"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["animal_2"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["rank"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["value1"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["value2"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["__index_level_2__"], _1: pandas.core.series.Series, /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["(a, x)"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["(a, y)"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["(b, z)"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["x1"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["x2"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["letter"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["number"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["day"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["sales"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["signups"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["visits"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["lab"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["val"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["mass"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["radius"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["length"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["width"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["s1"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["s2"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["vals"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["(x, a)"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["aa"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["bb"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 1
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["(y, b)"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["(x, b)"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["(y, c)"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["w"], _1: float, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Tuple[Literal["a"], Literal["c"]], _1: Literal["def"], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["x"], _1: Literal["ghi"], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["x"], _1: List[int], /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["a b c"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["5"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["clip"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["(A, one)"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["(A, two)"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["(B, one)"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["(B, two)"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["(x, a, 1)"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["(x, b, 2)"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["(y.z, c.d, 3)"], _1: pandas.core.series.Series, /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["(x, b, 4)"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["(X, A, Z)"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["(X, B, Z)"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["(Y, C, Z)"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["(Y, D, Z)"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["a.b"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["(c, e)"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["(d, f)"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["0.9655187292975722"], _1: pandas.core.series.Series, /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["0.31992251735325117"], _1: pandas.core.series.Series, /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["0.2635517951467826"], _1: pandas.core.series.Series, /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["0.5307682923411018"], _1: pandas.core.series.Series, /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["0.7768594149024922"], _1: pandas.core.series.Series, /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["0.9001395954082655"], _1: pandas.core.series.Series, /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["ba"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["cb"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["db"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["(x, ba)"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["(y, cb)"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["(z, db)"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["(b, y)"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["(c, z)"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["(a, , , b)"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["(c, , d, )"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["(e, , f, )"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["(e, g, , )"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["(, , , h)"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["(i, , , )"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["numbers"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 1
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["(A, 0)"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["(B, 1)"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["(A, Z)"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["(x, c)"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["(y, a)"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["(cg1, a)"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["(cg1, b)"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["(cg2, c)"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["(cg3, d)"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["(rg1, x)"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["(rg1, y)"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["(rg2, z)"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["i32"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["i64"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["f"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 1
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["bhello"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["Unnamed: 0"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["kind"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["group"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["(y, A)"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["(y, B)"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["(x, group)"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["v"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 1
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["timestamp"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["car_id"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["column"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        usage.pyjanitor: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["mean"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["(z, d)"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["(d, y)"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["3"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["4"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["(bar, one)"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["(bar, two)"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["(baz, one)"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["(baz, two)"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: List[Literal["b", "a"]], _1: pandas.core.frame.DataFrame, /
    ):
        """
        usage.dask: 1
        usage.koalas: 2
        """
        ...

    @overload
    def __setitem__(
        self, _0: List[Literal["c", "b"]], _1: pandas.core.frame.DataFrame, /
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def __setitem__(
        self, _0: List[Literal["d", "c"]], _1: pandas.core.frame.DataFrame, /
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: List[Tuple[Literal["y", "z"], Literal["c", "d"]]],
        _1: pandas.core.frame.DataFrame,
        /,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: List[Literal["f", "e"]], _1: pandas.core.frame.DataFrame, /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["y"], Literal["c"]], _1: pandas.core.series.Series, /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["Koalas"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["NEW"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: List[Literal["c"]], _1: pandas.core.frame.DataFrame, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: List[Literal["x"]], _1: pandas.core.frame.DataFrame, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: List[Literal["y", "x"]], _1: pandas.core.frame.DataFrame, /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["d"], Literal["x"]], _1: pandas.core.series.Series, /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["(1, 2)"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Tuple[Literal["d"], Literal["y"]], _1: pandas.core.series.Series, /
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["(1, 2, 3)"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: List[Tuple[Literal["f"], Literal["x", "y"]]],
        _1: pandas.core.frame.DataFrame,
        /,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["rep"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["(y, c, 3)"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["left"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["right"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["outlier"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["categorical"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["single"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["(Z, D)"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["g"], _1: pandas.core.series.Series, /):
        """
        usage.dask: 1
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["h"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["i"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["s"], _1: pandas.core.series.Series, /):
        """
        usage.koalas: 1
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["C"], _1: List[int], /):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["const"], _1: int, /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __setitem__(self, _0: int, _1: numpy.ndarray, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["constant"], _1: int, /):
        """
        usage.statsmodels: 4
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["pvalue-hs"], _1: numpy.ndarray, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["reject-hs"], _1: numpy.ndarray, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["pvalue-hommel"], _1: numpy.ndarray, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["reject-hommel"], _1: numpy.ndarray, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["offset"], _1: numpy.ndarray, /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["oracle"], _1: pandas.core.series.Series, /):
        """
        usage.statsmodels: 5
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["final"], _1: pandas.core.series.Series, /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["logpopul"], _1: pandas.core.series.Series, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["NABOVE"], _1: pandas.core.series.Series, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["NBELOW"], _1: pandas.core.series.Series, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["x3"], _1: numpy.ndarray, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["y = 0"], _1: pandas.core.indexes.base.Index, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["y = 1"], _1: pandas.core.indexes.base.Index, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["y = 2"], _1: pandas.core.indexes.base.Index, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["y = 3"], _1: pandas.core.indexes.base.Index, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["y = 4"], _1: pandas.core.indexes.base.Index, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["y = 5"], _1: pandas.core.indexes.base.Index, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["strata"], _1: numpy.ndarray, /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["Type"], _1: List[Literal["V", "M"]], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["Post. Mean"], _1: numpy.ndarray, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["Post. SD"], _1: numpy.ndarray, /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["SD"], _1: pandas.core.series.Series, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["SD (LB)"], _1: pandas.core.series.Series, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["SD (UB)"], _1: pandas.core.series.Series, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["SD"], _1: List[Literal["0.088", "0.092", "0.719"]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["SD (LB)"], _1: List[Literal["0.030", "0.042"]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["SD (UB)"], _1: List[Literal["0.257", "0.286", "12.265"]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["SD"], _1: List[Literal["0.083", "0.488", "2.124"]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["SD (LB)"], _1: List[Literal["0.030", "0.319", "1.358"]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["SD (UB)"], _1: List[Literal["0.227", "0.749", "3.322"]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["SD"], _1: List[Literal["0.527", "0.468", "2.211"]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["SD (LB)"], _1: List[Literal["0.332", "0.304", "1.406"]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["SD (UB)"], _1: List[Literal["0.834", "0.720", "3.476"]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["SD"], _1: List[Literal["0.624", "0.935", "0.930"]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["SD (LB)"], _1: List[Literal["0.352", "0.761", "0.779"]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["SD (UB)"], _1: List[Literal["1.105", "1.148", "1.111"]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["SD"], _1: List[Literal["0.796", "0.938", "0.932"]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["SD (LB)"], _1: List[Literal["0.521", "0.774", "0.784"]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["SD (UB)"], _1: List[Literal["1.218", "1.137", "1.107"]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["SD"], _1: List[Literal["0.094", "0.085", "0.581"]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["SD (LB)"], _1: List[Literal["0.029", "0.030", "0.387"]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["SD (UB)"], _1: List[Literal["0.300", "0.241", "0.872"]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["SD"], _1: List[Literal["1.211", "0.700", "0.492"]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["SD (LB)"], _1: List[Literal["0.815", "0.453", "0.312"]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["SD (UB)"], _1: List[Literal["1.799", "1.081", "0.777"]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["SD"], _1: List[Literal["1.955", "1.357", "0.766"]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["SD (LB)"], _1: List[Literal["1.352", "0.920", "0.431"]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["SD (UB)"], _1: List[Literal["2.828", "2.002", "1.362"]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["SD"], _1: List[Literal["0.503", "1.110", "0.578"]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["SD (LB)"], _1: List[Literal["0.298", "0.696", "0.476"]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["SD (UB)"], _1: List[Literal["0.847", "1.771", "0.702"]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["SD"], _1: List[Literal["0.591", "1.250", "0.579"]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["SD (LB)"], _1: List[Literal["0.377", "0.843", "0.502"]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["SD (UB)"], _1: List[Literal["0.926", "1.853", "0.668"]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["z1"], _1: numpy.ndarray, /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["z2"], _1: numpy.ndarray, /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["year_cen"], _1: pandas.core.series.Series, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["y"], _1: numpy.ndarray, /):
        """
        usage.statsmodels: 4
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["offset"], _1: int, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["time"], _1: int, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["EXECUTIONS"], _1: numpy.ndarray, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["FMI"], _1: numpy.ndarray, /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["intcol"], _1: numpy.ndarray, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["intcol"], _1: pandas.core.series.Series, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["qual"], _1: bool, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["quarter"], _1: pandas.core.series.Series, /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["datetime_c"], _1: pandas.core.series.Series, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["datetime_big_c"], _1: pandas.core.series.Series, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["date"], _1: pandas.core.series.Series, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["weekly_date"], _1: pandas.core.series.Series, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["monthly_date"], _1: pandas.core.series.Series, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["quarterly_date"], _1: pandas.core.series.Series, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["half_yearly_date"], _1: pandas.core.series.Series, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["yearly_date"], _1: pandas.core.series.Series, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["var2"], _1: pandas.core.series.Series, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["Coef."], _1: pandas.core.series.Series, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["Std.Err."], _1: pandas.core.series.Series, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["high"], _1: numpy.ndarray, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["largest"], _1: numpy.ndarray, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: pandas.core.frame.DataFrame, _1: Literal[""], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["dup"], _1: pandas.core.series.Series, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["Coef."], _1: List[Literal["4.966", "0.592", "1.154"]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["Std.Err."], _1: List[Literal["0.892", "0.177", "0.069"]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["z"], _1: List[Literal["", "16.652"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["P>|z|"], _1: List[Literal["", "0.000"]], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["[0.025"], _1: List[Literal["", "1.018"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["0.975]"], _1: List[Literal["", "1.290"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["groups"], _1: numpy.ndarray, /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["x1"], _1: numpy.ndarray, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["x2"], _1: numpy.ndarray, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["v1"], _1: numpy.ndarray, /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["v2"], _1: numpy.ndarray, /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["Coef."], _1: List[Literal["0.703", "0.009"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["Std.Err."], _1: List[Literal["0.172", "0.055"]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["z"], _1: List[Literal["", "0.166"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["P>|z|"], _1: List[Literal["", "0.868"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["[0.025"], _1: List[Literal["", "-0.099"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["0.975]"], _1: List[Literal["", "0.117"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["re1"], _1: numpy.ndarray, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["re2"], _1: numpy.ndarray, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["vc1"], _1: numpy.ndarray, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["vc2"], _1: numpy.ndarray, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["vc3"], _1: numpy.ndarray, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["vc4"], _1: numpy.ndarray, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["exog0"], _1: numpy.ndarray, /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["exog1"], _1: numpy.ndarray, /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["exog2"], _1: numpy.ndarray, /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["exog3"], _1: numpy.ndarray, /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["exog_re"], _1: numpy.ndarray, /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["Coef."], _1: List[str], /):
        """
        usage.statsmodels: 4
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Literal["Std.Err."],
        _1: List[Literal["0.159", "0.057", "0.058", "0.060", "0.055"]],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["z"], _1: List[str], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Literal["P>|z|"],
        _1: List[Literal["", "0.964", "0.666", "0.000", "0.779"]],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["[0.025"], _1: List[str], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["0.975]"], _1: List[str], /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["Std.Err."], _1: List[str], /):
        """
        usage.statsmodels: 4
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Literal["z"],
        _1: List[Literal["", "-0.207", "-16.463", "-0.091", "15.301"]],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["P>|z|"], _1: List[Literal["", "0.836", "0.000", "0.928"]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Literal["[0.025"],
        _1: List[Literal["", "-0.126", "-1.091", "-0.113", "0.764"]],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Literal["0.975]"],
        _1: List[Literal["", "0.102", "-0.859", "0.103", "0.989"]],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Literal["P>|z|"],
        _1: List[Literal["", "0.936", "0.644", "0.000", "0.759"]],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Literal["Coef."],
        _1: List[Literal["0.892", "0.004", "-0.027", "-0.993", "-0.017"]],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Literal["P>|z|"],
        _1: List[Literal["", "0.937", "0.641", "0.000", "0.753"]],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Literal["Coef."],
        _1: List[Literal["12.550", "-0.222", "0.307", "3.676"]],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Literal["Std.Err."],
        _1: List[Literal["17.608", "0.170", "0.143", "2.708"]],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["z"], _1: List[Literal["", "-1.306", "2.144", "1.358"]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["P>|z|"], _1: List[Literal["", "0.192", "0.032", "0.175"]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Literal["[0.025"],
        _1: List[Literal["", "-0.554", "0.026", "-1.631"]],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["0.975]"], _1: List[Literal["", "0.111", "0.589", "8.983"]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Literal["z"],
        _1: List[Literal["", "14.992", "15.204", "16.166", "15.884"]],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Literal["[0.025"],
        _1: List[Literal["", "0.882", "0.898", "0.883", "0.913"]],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Literal["0.975]"],
        _1: List[Literal["", "1.147", "1.163", "1.127", "1.170"]],
        /,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["g"], _1: numpy.ndarray, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["Coef."], _1: List[Literal["0.000", "0.108"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["Std.Err."], _1: List[Literal["", "0.123", "6221529.393"]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["z"], _1: List[Literal["", "0.876", "0.000"]], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["P>|z|"], _1: List[Literal["", "0.381", "1.000"]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["[0.025"], _1: List[Literal["", "-0.134", "-12193973.540"]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["0.975]"], _1: List[Literal["", "0.350", "12193973.540"]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["z3"], _1: numpy.ndarray, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["z4"], _1: numpy.ndarray, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["z5"], _1: numpy.ndarray, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["Type"], _1: List[Literal["SD", "Smooth", "Scale", "Mean"]], /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["coef"], _1: numpy.ndarray, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["std err"], _1: numpy.ndarray, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["tvalues"], _1: pandas.core.series.Series, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["P>|t|"], _1: numpy.ndarray, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["[0.025"], _1: pandas.core.series.Series, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["0.975]"], _1: pandas.core.series.Series, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["F"], _1: pandas.core.series.Series, /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["PR(>F)"], _1: numpy.ndarray, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["mean_sq"], _1: pandas.core.series.Series, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["ssr"], _1: List[numpy.float64], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["df_resid"], _1: List[numpy.float64], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["ss_diff"], _1: pandas.core.series.Series, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["Pr(>F)"], _1: numpy.ndarray, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["sum_sq"], _1: pandas.core.series.Series, /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["strat"], _1: numpy.ndarray, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["c"], _1: float, /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["__index__"], _1: numpy.ndarray, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["Stat"], _1: numpy.ndarray, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["FDR+"], _1: numpy.ndarray, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["FDR"], _1: numpy.ndarray, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["weights"], _1: numpy.ndarray, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["vec"], _1: numpy.ndarray, /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["UNEMP"], _1: pandas.core.series.Series, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["dln_inv"], _1: pandas.core.series.Series, /):
        """
        usage.statsmodels: 4
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["dln_inc"], _1: pandas.core.series.Series, /):
        """
        usage.statsmodels: 4
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["dln_consump"], _1: pandas.core.series.Series, /):
        """
        usage.statsmodels: 4
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["block"], _1: pandas.core.series.Series, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: List[Literal["order"]], _1: pandas.core.frame.DataFrame, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["var."], _1: numpy.ndarray, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["   error variance"], _1: numpy.ndarray, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: str, _1: numpy.ndarray, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["forecast (prev)"], _1: pandas.core.series.Series, /
    ):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["observed"], _1: pandas.core.series.Series, /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["news"], _1: pandas.core.series.Series, /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["impact"], _1: pandas.core.series.Series, /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["revision date"], _1: List[int], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["revised variable"], _1: List[int], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["update date"], _1: List[int], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["updated variable"], _1: List[int], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["observed (prev)"], _1: List[numpy.float64], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["revised"], _1: List[numpy.float64], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["impact of revisions"], _1: pandas.core.series.Series, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["impact of news"], _1: pandas.core.series.Series, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["total impact"], _1: pandas.core.series.Series, /
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["observed (prev)"], _1: list, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["revised"], _1: list, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["forecast (prev)"], _1: list, /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["observed"], _1: list, /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["news"], _1: list, /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["impact"], _1: list, /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["realgdp"], _1: pandas.core.series.Series, /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["lgdp"], _1: pandas.core.series.Series, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["loginv"], _1: pandas.core.series.Series, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["loggdp"], _1: pandas.core.series.Series, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["logcons"], _1: pandas.core.series.Series, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["cpi"], _1: pandas.core.series.Series, /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["cpi.L.1"], _1: pandas.core.series.Series, /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["cpi.L.2"], _1: pandas.core.series.Series, /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["cpi.L.3"], _1: pandas.core.series.Series, /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["const"], _1: numpy.ndarray, /):
        """
        usage.statsmodels: 6
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["trend"], _1: numpy.ndarray, /):
        """
        usage.statsmodels: 4
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["trend_squared"], _1: numpy.ndarray, /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["exovar1"], _1: numpy.ndarray, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["cap"], _1: float, /):
        """
        usage.prophet: 3
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["binary_feature"], _1: List[int], /):
        """
        usage.prophet: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["ds"], _1: pandas.core.series.Series, /):
        """
        usage.prophet: 3
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["floor"], _1: int, /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["t"], _1: pandas.core.series.Series, /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["y_scaled"], _1: pandas.core.series.Series, /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["cap_scaled"], _1: pandas.core.series.Series, /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["binary_feature"], _1: pandas.core.series.Series, /
    ):
        """
        usage.prophet: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["multiplicative_terms"], _1: int, /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["trend"], _1: pandas.core.series.Series, /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["yhat"], _1: pandas.core.series.Series, /):
        """
        usage.prophet: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["extra"], _1: range, /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["is_conditional_week"], _1: numpy.ndarray, /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["extra"], _1: pandas.core.series.Series, /):
        """
        usage.prophet: 2
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["is_conditional_week"], _1: pandas.core.series.Series, /
    ):
        """
        usage.prophet: 1
        """
        ...

    @overload
    def __setitem__(self, _0: pandas.core.series.Series, _1: int, /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["cap"], _1: int, /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["horizon"], _1: pandas.core.series.Series, /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["mse"], _1: pandas.core.series.Series, /):
        """
        usage.prophet: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["rmse"], _1: pandas.core.series.Series, /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["mae"], _1: pandas.core.series.Series, /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["mape"], _1: pandas.core.series.Series, /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["mdape"], _1: pandas.core.series.Series, /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["coverage"], _1: pandas.core.series.Series, /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["binary_feature"], _1: List[Literal["0"]], /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["numeric_feature"], _1: range, /):
        """
        usage.prophet: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["numeric_feature2"], _1: range, /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["numeric_feature"], _1: pandas.core.series.Series, /
    ):
        """
        usage.prophet: 2
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["numeric_feature2"], _1: pandas.core.series.Series, /
    ):
        """
        usage.prophet: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["binary_feature2"], _1: List[int], /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["binary_feature2"], _1: pandas.core.series.Series, /
    ):
        """
        usage.prophet: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["binary_feature2"], _1: int, /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["constant_feature"], _1: int, /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["constant_feature"], _1: pandas.core.series.Series, /
    ):
        """
        usage.prophet: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["additive_terms"], _1: int, /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["is_conditional_week"], _1: List[int], /):
        """
        usage.prophet: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["y"], _1: int, /):
        """
        usage.prophet: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["cap"], _1: numpy.float64, /):
        """
        usage.prophet: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["floor"], _1: float, /):
        """
        usage.prophet: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["floor"], _1: pandas.core.series.Series, /):
        """
        usage.prophet: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["cap"], _1: pandas.core.series.Series, /):
        """
        usage.prophet: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["col0"], _1: List[str], /):
        """
        usage.modin: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["col2"], _1: List[str], /):
        """
        usage.modin: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["col4"], _1: List[str], /):
        """
        usage.modin: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["col6"], _1: List[str], /):
        """
        usage.modin: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["col8"], _1: List[str], /):
        """
        usage.modin: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["col10"], _1: List[str], /):
        """
        usage.modin: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["col12"], _1: List[str], /):
        """
        usage.modin: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["col14"], _1: List[str], /):
        """
        usage.modin: 2
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["day"], _1: pandas.core.arrays.categorical.Categorical, /
    ):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["sex"], _1: pandas.core.arrays.categorical.Categorical, /
    ):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["time"], _1: pandas.core.arrays.categorical.Categorical, /
    ):
        """
        usage.seaborn: 2
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["smoker"], _1: pandas.core.arrays.categorical.Categorical, /
    ):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["kind"], _1: pandas.core.arrays.categorical.Categorical, /
    ):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["diet"], _1: pandas.core.arrays.categorical.Categorical, /
    ):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["class"], _1: pandas.core.arrays.categorical.Categorical, /
    ):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["deck"], _1: pandas.core.arrays.categorical.Categorical, /
    ):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["b_bool"], _1: pandas.core.series.Series, /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["hasna"], _1: pandas.core.series.Series, /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["date"], _1: pandas.core.indexes.datetimes.DatetimeIndex, /
    ):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["@index"], _1: pandas.core.series.Series, /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["hue"], _1: pandas.core.series.Series, /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["style"], _1: pandas.core.series.Series, /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["@columns"], _1: pandas.core.arrays.categorical.Categorical, /
    ):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["_"], _1: Literal["_"], /):
        """
        usage.seaborn: 4
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["widths"], _1: pandas.core.series.Series, /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["edges"], _1: pandas.core.series.Series, /):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["color"], _1: pandas.core.arrays.categorical.Categorical, /
    ):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["clarity"], _1: pandas.core.arrays.categorical.Categorical, /
    ):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["cut"], _1: pandas.core.arrays.categorical.Categorical, /
    ):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["month"], _1: pandas.core.arrays.categorical.Categorical, /
    ):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["sex"], _1: pandas.core.series.Series, /):
        """
        usage.seaborn: 1
        usage.sklearn: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["geometry"], _1: numpy.ndarray, /):
        """
        usage.geopandas: 3
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["geometry"], _1: geopandas.array.GeometryArray, /
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["geom2"], _1: numpy.ndarray, /):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["geom2"], _1: geopandas.array.GeometryArray, /):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["geom3"], _1: numpy.ndarray, /):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["geom3"], _1: geopandas.array.GeometryArray, /):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["sequence"], _1: List[str], /):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["a_cm"], _1: numpy.ndarray, /):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["a_m"], _1: numpy.ndarray, /):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["a_kg"], _1: numpy.ndarray, /):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["a_m2"], _1: numpy.ndarray, /):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["a_m3"], _1: numpy.ndarray, /):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["a_USD"], _1: pandas.core.series.Series, /):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["a_2018"], _1: pandas.core.series.Series, /):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["a_2015"], _1: pandas.core.series.Series, /):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["fortytwo"], _1: int, /):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["fortythousand"], _1: Literal["test string"], /):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["fortythree"], _1: numpy.ndarray, /):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["fill_in_scalar"], _1: List[int], /):
        """
        usage.pyjanitor: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["city_pop"], _1: int, /):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["city_pop"], _1: List[int], /):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["city_pop"], _1: pandas.core.series.Series, /):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["x"], _1: float, /):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["a_bin"], _1: pandas.core.series.Series, /):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["index"], _1: pandas.core.series.Series, /):
        """
        usage.pyjanitor: 2
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Literal["hire_date"],
        _1: pandas.core.indexes.datetimes.DatetimeIndex,
        /,
    ):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["names"], _1: pandas.core.arrays.categorical.Categorical, /
    ):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        _0: Literal["animals@#$%^"],
        _1: pandas.core.arrays.categorical.Categorical,
        /,
    ):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def __setitem__(
        self, _0: Literal["cities"], _1: pandas.core.arrays.categorical.Categorical, /
    ):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["null_flag"], _1: pandas.core.series.Series, /):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["flag"], _1: pandas.core.series.Series, /):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["a_enc"], _1: numpy.ndarray, /):
        """
        usage.pyjanitor: 2
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["c_enc"], _1: numpy.ndarray, /):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["Bell__Chart"], _1: pandas.core.series.Series, /):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["date1"], _1: pandas.core.series.Series, /):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["a_log10"], _1: pandas.core.series.Series, /):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["another"], _1: int, /):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["column"], _1: int, /):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["another"], _1: pandas.core.series.Series, /):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["another_log"], _1: pandas.core.series.Series, /):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["column_log"], _1: pandas.core.series.Series, /):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["hello"], _1: pandas.core.series.Series, /):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["world"], _1: pandas.core.series.Series, /):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["amount"], _1: pandas.core.series.Series, /):
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
    def __setitem__(self, _0: Literal["y_"], _1: pandas.core.series.Series, /):
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
    def __setitem__(
        self, _0: Literal["dt"], _1: pandas._libs.tslibs.timestamps.Timestamp, /
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __setitem__(self, _0: Literal["c"], _1: pandas.core.indexes.base.Index, /):
        """
        usage.dask: 1
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
    def __setitem__(self, _0: Literal["z"], _1: numpy.ndarray, /):
        """
        usage.dask: 1
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
        usage.geopandas: 8
        usage.koalas: 266
        usage.modin: 16
        usage.prophet: 63
        usage.pyjanitor: 56
        usage.seaborn: 29
        usage.sklearn: 178
        usage.statsmodels: 307
        usage.xarray: 1
        """
        ...

    @overload
    def __sub__(self, _0: pandas.core.frame.DataFrame, /):
        """
        usage.dask: 1
        usage.koalas: 2
        usage.statsmodels: 6
        """
        ...

    @overload
    def __sub__(self, _0: pandas.core.series.Series, /):
        """
        usage.dask: 5
        usage.seaborn: 2
        usage.statsmodels: 8
        """
        ...

    @overload
    def __sub__(self, _0: numpy.ndarray, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __sub__(self, _0: Union[numpy.ndarray, numpy.datetime64, numpy.timedelta64], /):
        """
        usage.pandas: 30
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
        usage.koalas: 2
        usage.pandas: 30
        usage.seaborn: 2
        usage.statsmodels: 15
        """
        ...

    @overload
    def __truediv__(self, _0: pandas.core.series.Series, /):
        """
        usage.seaborn: 2
        usage.statsmodels: 5
        """
        ...

    @overload
    def __truediv__(self, _0: pandas.core.frame.DataFrame, /):
        """
        usage.dask: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    def __truediv__(self, _0: int, /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __truediv__(self, _0: Union[numpy.ndarray, numpy.timedelta64], /):
        """
        usage.pandas: 22
        """
        ...

    def __truediv__(
        self,
        _0: Union[
            pandas.core.frame.DataFrame,
            numpy.timedelta64,
            numpy.ndarray,
            int,
            pandas.core.series.Series,
        ],
        /,
    ):
        """
        usage.dask: 1
        usage.pandas: 22
        usage.seaborn: 2
        usage.statsmodels: 8
        """
        ...

    def _get_numeric_data(self, /):
        """
        usage.dask: 4
        """
        ...

    def _repr_html_(self, /):
        """
        usage.koalas: 4
        """
        ...

    def abs(self, /):
        """
        usage.dask: 3
        usage.koalas: 1
        usage.statsmodels: 2
        """
        ...

    @overload
    def add(self, /, other: pandas.core.series.Series, axis: int, level: int):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def add(self, /, other: pandas.core.series.Series, level: int):
        """
        usage.statsmodels: 1
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
        other: Union[pandas.core.series.Series, int, pandas.core.frame.DataFrame],
        axis: Union[int, Literal["columns", "index"]] = ...,
        level: int = ...,
        fill_value: int = ...,
    ):
        """
        usage.dask: 11
        usage.statsmodels: 2
        """
        ...

    @overload
    def add_prefix(self, /, prefix: Literal["col_"]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def add_prefix(self, /, prefix: Literal["col"]):
        """
        usage.modin: 1
        """
        ...

    def add_prefix(self, /, prefix: Literal["col", "col_"]):
        """
        usage.koalas: 2
        usage.modin: 1
        """
        ...

    def add_suffix(self, /, suffix: Literal["first_series"]):
        """
        usage.koalas: 2
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
        usage.hvplot: 2
        usage.koalas: 3
        usage.seaborn: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    def all(self, /, axis: int):
        """
        usage.dask: 4
        usage.pyjanitor: 2
        usage.statsmodels: 1
        """
        ...

    @overload
    def all(self, /, axis: int, skipna: bool):
        """
        usage.dask: 2
        """
        ...

    def all(self, /, axis: int = ..., skipna: bool = ...):
        """
        usage.dask: 11
        usage.hvplot: 2
        usage.koalas: 3
        usage.pyjanitor: 2
        usage.seaborn: 1
        usage.statsmodels: 2
        """
        ...

    @overload
    def any(self, /):
        """
        usage.dask: 3
        usage.koalas: 3
        usage.seaborn: 1
        """
        ...

    @overload
    def any(self, /, axis: int):
        """
        usage.dask: 4
        usage.prophet: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    def any(self, /, axis: int, skipna: bool):
        """
        usage.dask: 2
        """
        ...

    def any(self, /, axis: int = ..., skipna: bool = ...):
        """
        usage.dask: 9
        usage.koalas: 3
        usage.prophet: 1
        usage.seaborn: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    def append(self, /, other: pandas.core.frame.DataFrame):
        """
        usage.dask: 3
        usage.koalas: 5
        usage.prophet: 2
        usage.statsmodels: 9
        """
        ...

    @overload
    def append(self, /, other: pandas.core.frame.DataFrame, ignore_index: bool):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def append(self, /, other: pandas.core.frame.DataFrame, verify_integrity: bool):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def append(
        self,
        /,
        other: pandas.core.frame.DataFrame,
        ignore_index: bool,
        verify_integrity: bool,
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def append(self, /, other: pandas.core.series.Series):
        """
        usage.dask: 1
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
        other: Union[pandas.core.series.Series, pandas.core.frame.DataFrame],
        ignore_index: bool = ...,
        verify_integrity: bool = ...,
    ):
        """
        usage.dask: 12
        usage.koalas: 11
        usage.prophet: 2
        usage.statsmodels: 9
        """
        ...

    @overload
    def apply(self, /, func: Callable, axis: int, args: Tuple[None, ...]):
        """
        usage.koalas: 3
        """
        ...

    @overload
    def apply(self, /, func: Callable, axis: int, args: Tuple[None, ...]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def apply(self, /, func: Callable):
        """
        usage.koalas: 6
        usage.statsmodels: 1
        """
        ...

    @overload
    def apply(self, /, func: Callable, axis: int, args: Tuple[int]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def apply(self, /, func: Callable, args: Tuple[int]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def apply(self, /, func: Callable, axis: int):
        """
        usage.dask: 5
        usage.koalas: 6
        usage.modin: 1
        usage.pyjanitor: 1
        usage.statsmodels: 5
        """
        ...

    @overload
    def apply(self, /, func: Callable):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def apply(self, /, func: Callable, result_type: Literal["expand"]):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def apply(self, /, func: Callable):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def apply(self, /, func: Callable):
        """
        usage.seaborn: 1
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
        result_type: Union[None, Literal["expand"]] = ...,
        axis: Union[Literal["columns"], int] = ...,
        args: Tuple[Union[None, int], ...] = ...,
    ):
        """
        usage.dask: 10
        usage.koalas: 19
        usage.modin: 1
        usage.pyjanitor: 1
        usage.seaborn: 1
        usage.statsmodels: 8
        usage.xarray: 1
        """
        ...

    @overload
    def applymap(self, /, func: Callable):
        """
        usage.dask: 3
        usage.statsmodels: 5
        """
        ...

    @overload
    def applymap(self, /, func: Type[str]):
        """
        usage.statsmodels: 1
        """
        ...

    def applymap(self, /, func: Union[Callable, Type[str]]):
        """
        usage.dask: 3
        usage.statsmodels: 6
        """
        ...

    def assign(self, /):
        """
        usage.dask: 17
        usage.hvplot: 4
        usage.koalas: 4
        usage.pyjanitor: 1
        """
        ...

    @overload
    def astype(self, /, dtype: Dict[Literal["x", "__index_level_0__"], numpy.dtype]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def astype(self, /, dtype: Dict[Literal["0", "__index_level_0__"], numpy.dtype]):
        """
        usage.koalas: 3
        """
        ...

    @overload
    def astype(self, /, dtype: Dict[Literal["__index_level_0__"], numpy.dtype]):
        """
        usage.koalas: 3
        """
        ...

    @overload
    def astype(self, /, dtype: Dict[str, numpy.dtype]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def astype(
        self, /, dtype: Dict[Literal["z", "y", "x", "__index_level_0__"], numpy.dtype]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def astype(self, /, dtype: Dict[Literal["t", "__index_level_0__"], numpy.dtype]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def astype(
        self, /, dtype: Dict[Literal["b", "a", "__index_level_0__"], numpy.dtype]
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def astype(
        self, /, dtype: Dict[Literal["C", "B", "A", "__index_level_0__"], numpy.dtype]
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def astype(
        self,
        /,
        dtype: Dict[
            Literal["(C, Z)", "(B, X)", "(A, Z)", "__index_level_0__"], numpy.dtype
        ],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def astype(self, /, dtype: Type[float]):
        """
        usage.dask: 9
        usage.koalas: 1
        usage.statsmodels: 20
        """
        ...

    @overload
    def astype(
        self, /, dtype: Dict[Literal["c", "b", "a", "__index_level_0__"], numpy.dtype]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def astype(self, /, dtype: Dict[Literal["b", "__index_level_0__"], numpy.dtype]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def astype(
        self,
        /,
        dtype: Dict[
            Literal["c", "b", "a", "__index_level_1__", "__index_level_0__"],
            numpy.dtype,
        ],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def astype(
        self,
        /,
        dtype: Dict[
            Literal["b", "__index_level_1__", "__index_level_0__"], numpy.dtype
        ],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def astype(
        self,
        /,
        dtype: Dict[
            Literal[
                "(y, c)", "(x, b)", "(x, a)", "__index_level_1__", "__index_level_0__"
            ],
            numpy.dtype,
        ],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def astype(
        self,
        /,
        dtype: Dict[Literal["__index_level_1__", "__index_level_0__"], numpy.dtype],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def astype(self, /, dtype: Dict[Literal["a", "__index_level_0__"], numpy.dtype]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def astype(
        self, /, dtype: Dict[Literal["(bar, one)", "__index_level_0__"], numpy.dtype]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def astype(self, /, dtype: Dict[Literal["A", "__index_level_0__"], numpy.dtype]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def astype(
        self,
        /,
        dtype: Dict[Literal["D", "C", "B", "A", "__index_level_0__"], numpy.dtype],
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def astype(
        self, /, dtype: Dict[Literal["Koalas", "__index_level_0__"], numpy.dtype]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def astype(self, /, dtype: Type[str]):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def astype(self, /, dtype: Type[object]):
        """
        usage.geopandas: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    def astype(self, /, dtype: Type[int]):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def astype(self, /, dtype: Dict[Literal["col1"], Literal["category"]]):
        """
        usage.modin: 1
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
            Dict[
                Union[int, str],
                Union[
                    Type[float],
                    Literal["category", "f8"],
                    pandas.core.dtypes.dtypes.CategoricalDtype,
                    numpy.dtype,
                ],
            ],
            pandas.core.series.Series,
            Literal["float", "float64"],
        ],
        copy: bool = ...,
    ):
        """
        usage.dask: 32
        usage.geopandas: 1
        usage.koalas: 29
        usage.modin: 1
        usage.sklearn: 4
        usage.statsmodels: 24
        """
        ...

    @overload
    def bfill(self, /):
        """
        usage.dask: 1
        usage.koalas: 1
        """
        ...

    @overload
    def bfill(self, /, limit: int):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def bfill(self, /, inplace: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def bfill(self, /, axis: int):
        """
        usage.dask: 1
        """
        ...

    def bfill(self, /, limit: int = ..., inplace: bool = ..., axis: int = ...):
        """
        usage.dask: 2
        usage.koalas: 3
        """
        ...

    def bool(self, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def clip(self, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def clip(self, /, lower: int):
        """
        usage.dask: 1
        usage.koalas: 1
        """
        ...

    @overload
    def clip(self, /, upper: int):
        """
        usage.dask: 1
        usage.koalas: 1
        """
        ...

    @overload
    def clip(self, /, lower: int, upper: int):
        """
        usage.dask: 2
        usage.koalas: 1
        """
        ...

    @overload
    def clip(self, /, lower: int, upper: None):
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
        lower: Union[float, int, None] = ...,
        upper: Union[None, int, float] = ...,
    ):
        """
        usage.dask: 12
        usage.koalas: 4
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
    def copy(self, /):
        """
        usage.dask: 13
        usage.koalas: 21
        usage.modin: 4
        usage.prophet: 31
        usage.pyjanitor: 4
        usage.seaborn: 11
        usage.sklearn: 4
        usage.statsmodels: 88
        """
        ...

    @overload
    def copy(self, /, deep: bool):
        """
        usage.dask: 3
        usage.seaborn: 1
        """
        ...

    def copy(self, /, deep: bool = ...):
        """
        usage.dask: 16
        usage.koalas: 21
        usage.modin: 4
        usage.prophet: 31
        usage.pyjanitor: 4
        usage.seaborn: 12
        usage.sklearn: 4
        usage.statsmodels: 88
        """
        ...

    @overload
    def corr(self, /):
        """
        usage.dask: 3
        usage.koalas: 3
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
        usage.koalas: 3
        """
        ...

    @overload
    def count(self, /, axis: int, numeric_only: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def count(self, /, axis: int):
        """
        usage.dask: 3
        usage.koalas: 1
        """
        ...

    @overload
    def count(self, /):
        """
        usage.dask: 12
        usage.pyjanitor: 2
        usage.statsmodels: 2
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

    def count(
        self,
        /,
        numeric_only: bool = ...,
        axis: Union[int, Literal["columns", "index"]] = ...,
    ):
        """
        usage.dask: 17
        usage.koalas: 2
        usage.pyjanitor: 2
        usage.statsmodels: 2
        """
        ...

    @overload
    def cov(self, /):
        """
        usage.dask: 4
        usage.statsmodels: 1
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
        usage.statsmodels: 1
        """
        ...

    @overload
    def cummax(self, /):
        """
        usage.dask: 4
        usage.koalas: 2
        """
        ...

    @overload
    def cummax(self, /, skipna: bool):
        """
        usage.dask: 1
        usage.koalas: 1
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

    def cummax(self, /, axis: Union[int, None] = ..., skipna: bool = ...):
        """
        usage.dask: 11
        usage.koalas: 3
        """
        ...

    @overload
    def cummin(self, /):
        """
        usage.dask: 4
        usage.koalas: 2
        """
        ...

    @overload
    def cummin(self, /, skipna: bool):
        """
        usage.dask: 1
        usage.koalas: 1
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

    def cummin(self, /, axis: Union[int, None] = ..., skipna: bool = ...):
        """
        usage.dask: 11
        usage.koalas: 3
        """
        ...

    @overload
    def cumprod(self, /):
        """
        usage.dask: 4
        usage.koalas: 2
        usage.statsmodels: 2
        """
        ...

    @overload
    def cumprod(self, /, skipna: bool):
        """
        usage.dask: 1
        usage.koalas: 1
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

    def cumprod(self, /, axis: Union[int, None] = ..., skipna: bool = ...):
        """
        usage.dask: 11
        usage.koalas: 3
        usage.statsmodels: 2
        """
        ...

    @overload
    def cumsum(self, /):
        """
        usage.dask: 4
        usage.koalas: 2
        """
        ...

    @overload
    def cumsum(self, /, skipna: bool):
        """
        usage.dask: 1
        usage.koalas: 1
        """
        ...

    @overload
    def cumsum(self, /, axis: Literal["columns"]):
        """
        usage.seaborn: 1
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

    def cumsum(
        self, /, axis: Union[None, int, Literal["columns"]] = ..., skipna: bool = ...
    ):
        """
        usage.dask: 11
        usage.koalas: 3
        usage.seaborn: 1
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
    def diff(self, /):
        """
        usage.dask: 1
        usage.koalas: 2
        usage.statsmodels: 21
        """
        ...

    @overload
    def diff(self, /, periods: int):
        """
        usage.dask: 5
        usage.statsmodels: 1
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
        usage.dask: 8
        usage.koalas: 2
        usage.statsmodels: 22
        """
        ...

    @overload
    def drop(self, /, labels: List[Literal["__groupkey_0__"]], axis: int):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def drop(self, /, labels: Literal["b"], axis: int):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def drop(self, /, labels: Literal["x"], axis: int):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def drop(self, /, labels: List[Literal["z", "y"]], axis: int):
        """
        usage.dask: 1
        usage.koalas: 1
        """
        ...

    @overload
    def drop(self, /, columns: Literal["x"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def drop(self, /, columns: List[Literal["z", "y"]]):
        """
        usage.dask: 1
        usage.koalas: 1
        """
        ...

    @overload
    def drop(self, /, columns: Literal["a"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def drop(self, /, columns: Tuple[Literal["a"], Literal["x"]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def drop(
        self, /, columns: List[Union[Literal["b"], Tuple[Literal["a"], Literal["x"]]]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def drop(
        self, /, labels: List[Literal["__groupkey_1__", "__groupkey_0__"]], axis: int
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def drop(
        self, /, labels: List[Tuple[Literal["__groupkey_0__"], Literal[""]]], axis: int
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def drop(
        self,
        /,
        labels: List[Tuple[Literal["__groupkey_0__", "__groupkey_1__"], Literal[""]]],
        axis: int,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def drop(self, /, columns: List[Literal["75%", "50%", "25%"]], level: int):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def drop(self, /, labels: List[Literal["cancer"]], axis: int):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def drop(self, /, labels: List[Literal["AVGEXP"]], axis: int):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def drop(self, /, labels: List[Literal["BILLS104"]], axis: int):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def drop(self, /, labels: List[Literal["WORLDCONSUMPTION"]], axis: int):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def drop(self, /, labels: List[Literal["EXECUTIONS"]], axis: int):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def drop(self, /, labels: List[Literal["income"]], axis: int):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def drop(self, /, labels: List[Literal["affairs"]], axis: int):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def drop(self, /, labels: List[Literal["invest"]], axis: int):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def drop(self, /, labels: List[Literal["survival"]], axis: int):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def drop(self, /, labels: List[Literal["TOTEMP"]], axis: int):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def drop(self, /, labels: List[Literal["mdvis"]], axis: int):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def drop(self, /, labels: List[Literal["YES"]], axis: int):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def drop(self, /, labels: List[Literal["GRADE"]], axis: int):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def drop(self, /, labels: List[Literal["STACKLOSS"]], axis: int):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def drop(self, /, labels: List[Literal["NBELOW", "NABOVE"]], axis: int):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def drop(self, /, labels: List[Literal["duration"]], axis: int):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def drop(self, /, labels: Literal["index"], axis: int):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def drop(self, /, labels: List[Literal["largest", "high"]], axis: int):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def drop(self, /, labels: List[int]):
        """
        usage.dask: 2
        usage.statsmodels: 11
        """
        ...

    @overload
    def drop(
        self, /, labels: List[Literal["revised variable", "revision date"]], axis: int
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def drop(
        self, /, labels: List[Literal["updated variable", "update date"]], axis: int
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def drop(self, /, labels: List[str], axis: int):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def drop(self, /, labels: pandas.core.indexes.base.Index, axis: int):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def drop(self, /, labels: List[Literal["cpi"]], axis: int):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def drop(
        self,
        /,
        labels: Literal["zeros"],
        axis: int,
        inplace: bool,
        errors: Literal["ignore"],
    ):
        """
        usage.prophet: 1
        """
        ...

    @overload
    def drop(self, /, labels: pandas.core.indexes.numeric.Int64Index):
        """
        usage.prophet: 1
        usage.pyjanitor: 1
        """
        ...

    @overload
    def drop(self, /, labels: Literal["date"], axis: int):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def drop(
        self, /, labels: List[Literal["y", "x"]], axis: int, errors: Literal["ignore"]
    ):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def drop(self, /, columns: List[Literal["c", "b", "a"]]):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def drop(self, /, columns: Literal["index"]):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def drop(self, /, columns: List[Literal["decorated-elephant", "a"]]):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def drop(self, /, columns: List[Literal["a"]]):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def drop(self, /, columns: List[Literal["Bell__Chart", "a"]]):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def drop(self, /, columns: list):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def drop(
        self,
        /,
        columns: List[
            Literal["cities", "animals@#$%^", "decorated-elephant", "Bell__Chart", "a"]
        ],
    ):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def drop(
        self, /, columns: List[Tuple[Literal["bar", "baz"], Literal["one", "two"]]]
    ):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def drop(self, /, index: pandas.core.indexes.numeric.Int64Index):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def drop(self, /, columns: pandas.core.indexes.base.Index):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def drop(self, /, labels: int):
        """
        usage.dask: 4
        usage.pyjanitor: 1
        """
        ...

    @overload
    def drop(self, /, columns: List[Literal["cities", "Bell__Chart", "a"]]):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def drop(self, /, columns: List[Literal["animals@#$%^", "a", "Bell__Chart"]]):
        """
        usage.pyjanitor: 1
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
    def drop(
        self, /, columns: List[Literal["x"]], inplace: bool, errors: Literal["raise"]
    ):
        """
        usage.dask: 1
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
        columns: Union[
            Literal["category_2", "dt", "index", "a", "x"],
            List[
                Union[
                    Tuple[Literal["bar", "baz", "a"], Literal["one", "two", "x"]], str
                ]
            ],
            Tuple[Literal["a"], Literal["x"]],
            pandas.core.indexes.base.Index,
        ] = ...,
        level: int = ...,
        labels: Union[
            int,
            pandas.core.indexes.base.Index,
            pandas.core.indexes.numeric.Int64Index,
            List[
                Union[
                    str,
                    Tuple[Literal["__groupkey_0__", "__groupkey_1__"], Literal[""]],
                    int,
                ]
            ],
            str,
        ] = ...,
        axis: int = ...,
        inplace: bool = ...,
        errors: Literal["raise", "ignore"] = ...,
    ):
        """
        usage.dask: 33
        usage.koalas: 15
        usage.prophet: 2
        usage.pyjanitor: 14
        usage.seaborn: 2
        usage.statsmodels: 34
        """
        ...

    @overload
    def drop_duplicates(self, /, keep: Literal["first"]):
        """
        usage.dask: 2
        usage.koalas: 3
        """
        ...

    @overload
    def drop_duplicates(self, /, subset: Literal["a"], keep: Literal["first"]):
        """
        usage.koalas: 1
        usage.pyjanitor: 1
        """
        ...

    @overload
    def drop_duplicates(
        self, /, subset: List[Literal["b", "a"]], keep: Literal["first"]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def drop_duplicates(self, /, subset: Literal["b"], keep: Literal["first"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def drop_duplicates(self, /, keep: Literal["last"]):
        """
        usage.dask: 2
        usage.koalas: 3
        """
        ...

    @overload
    def drop_duplicates(self, /, subset: Literal["a"], keep: Literal["last"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def drop_duplicates(
        self, /, subset: List[Literal["b", "a"]], keep: Literal["last"]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def drop_duplicates(self, /, subset: Literal["b"], keep: Literal["last"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def drop_duplicates(self, /, keep: bool):
        """
        usage.dask: 1
        usage.koalas: 3
        """
        ...

    @overload
    def drop_duplicates(self, /, subset: Literal["a"], keep: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def drop_duplicates(self, /, subset: List[Literal["b", "a"]], keep: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def drop_duplicates(self, /, subset: Literal["b"], keep: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def drop_duplicates(
        self, /, subset: Tuple[Literal["x"], Literal["a"]], keep: Literal["first"]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def drop_duplicates(
        self,
        /,
        subset: List[Tuple[Literal["x", "y"], Literal["a", "b"]]],
        keep: Literal["first"],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def drop_duplicates(
        self, /, subset: Tuple[Literal["x"], Literal["a"]], keep: Literal["last"]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def drop_duplicates(
        self,
        /,
        subset: List[Tuple[Literal["x", "y"], Literal["a", "b"]]],
        keep: Literal["last"],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def drop_duplicates(self, /, subset: Tuple[Literal["x"], Literal["a"]], keep: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def drop_duplicates(
        self, /, subset: List[Tuple[Literal["x", "y"], Literal["a", "b"]]], keep: bool
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def drop_duplicates(self, /, subset: None, inplace: bool):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def drop_duplicates(self, /, subset: Literal["a"], inplace: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def drop_duplicates(self, /, subset: List[Literal["b", "a"]], inplace: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def drop_duplicates(
        self, /, subset: Tuple[Literal["x"], Literal["a"]], inplace: bool
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def drop_duplicates(
        self,
        /,
        subset: List[Tuple[Literal["x", "y"], Literal["a", "b"]]],
        inplace: bool,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def drop_duplicates(self, /, subset: List[Literal["B", "id"]]):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def drop_duplicates(self, /, subset: List[Literal["B", "A", "id"]]):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def drop_duplicates(self, /, subset: List[Literal["D", "B", "A", "id"]]):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def drop_duplicates(self, /, subset: List[Literal["E", "A", "id"]]):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def drop_duplicates(self, /):
        """
        usage.dask: 5
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
    def drop_duplicates(self, /, subset: None, keep: Literal["last"]):
        """
        usage.dask: 1
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
        subset: Union[
            List[Union[str, Tuple[Literal["x", "y"], Literal["a", "b"]]]],
            None,
            Literal["ticker", "y", "a", "b"],
            Tuple[Literal["x"], Literal["a"]],
        ] = ...,
        keep: Union[bool, Literal["last", "first"]] = ...,
        inplace: bool = ...,
    ):
        """
        usage.dask: 43
        usage.koalas: 30
        usage.pyjanitor: 1
        usage.statsmodels: 4
        """
        ...

    @overload
    def droplevel(self, /, level: Literal["a"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def droplevel(self, /, level: int):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def droplevel(self, /, level: Literal["level_1"], axis: int):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def droplevel(self, /, level: int, axis: int):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def droplevel(self, /, level: List[Tuple[Literal["a"], Literal["b"]]]):
        """
        usage.koalas: 1
        """
        ...

    def droplevel(
        self,
        /,
        level: Union[
            List[Tuple[Literal["a"], Literal["b"]]], Literal["level_1", "a"], int
        ],
        axis: int = ...,
    ):
        """
        usage.koalas: 6
        """
        ...

    @overload
    def dropna(self, /, axis: int):
        """
        usage.koalas: 3
        """
        ...

    @overload
    def dropna(self, /, axis: int, how: Literal["all"]):
        """
        usage.koalas: 3
        """
        ...

    @overload
    def dropna(self, /, axis: int, subset: List[Literal["x"]]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def dropna(self, /, axis: int, subset: List[Literal["z", "y"]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def dropna(
        self, /, axis: int, how: Literal["all"], subset: List[Literal["z", "y"]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def dropna(self, /, axis: int, thresh: int):
        """
        usage.koalas: 4
        """
        ...

    @overload
    def dropna(self, /, axis: int, thresh: int, subset: List[Literal["z", "y"]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def dropna(self, /, inplace: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def dropna(self, /, axis: int, subset: List[Tuple[Literal["a"], Literal["x"]]]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def dropna(
        self, /, axis: int, subset: List[Tuple[Literal["a", "b"], Literal["y", "z"]]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def dropna(
        self,
        /,
        axis: int,
        how: Literal["all"],
        subset: List[Tuple[Literal["a", "b"], Literal["y", "z"]]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def dropna(
        self,
        /,
        axis: int,
        thresh: int,
        subset: List[Tuple[Literal["a", "b"], Literal["y", "z"]]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def dropna(self, /):
        """
        usage.dask: 1
        usage.koalas: 1
        usage.seaborn: 14
        usage.statsmodels: 13
        """
        ...

    @overload
    def dropna(self, /, how: Literal["all"]):
        """
        usage.dask: 1
        usage.koalas: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    def dropna(self, /, thresh: int):
        """
        usage.dask: 8
        usage.koalas: 2
        """
        ...

    @overload
    def dropna(self, /, how: Literal["any"], thresh: None, subset: None):
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
        axis: int = ...,
        how: Literal["any", "all"] = ...,
        thresh: Union[int, None] = ...,
        subset: Union[
            None, List[Union[str, Tuple[Literal["a", "b"], Literal["y", "z", "x"]]]]
        ] = ...,
    ):
        """
        usage.dask: 22
        usage.koalas: 25
        usage.seaborn: 14
        usage.statsmodels: 14
        """
        ...

    @overload
    def duplicated(self, /):
        """
        usage.koalas: 4
        """
        ...

    @overload
    def duplicated(self, /, keep: Literal["last"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def duplicated(self, /, keep: bool):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def duplicated(self, /, subset: List[Literal["b"]]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def duplicated(self, /, subset: List[Tuple[Literal["x"], Literal["b"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def duplicated(self, /, subset: None, keep: bool):
        """
        usage.pyjanitor: 1
        """
        ...

    def duplicated(
        self,
        /,
        subset: Union[
            None, List[Union[Tuple[Literal["x"], Literal["b"]], Literal["b"]]]
        ] = ...,
        keep: Union[bool, Literal["last"]] = ...,
    ):
        """
        usage.koalas: 10
        usage.pyjanitor: 1
        """
        ...

    def equals(self, /, other: pandas.core.frame.DataFrame):
        """
        usage.dask: 2
        usage.prophet: 1
        usage.statsmodels: 6
        usage.xarray: 10
        """
        ...

    @overload
    def eval(self, /, expr: Literal["A + B"], inplace: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def eval(self, /, expr: Literal["C = A + B"], inplace: bool):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def eval(self, /, expr: Literal["A + B"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def eval(self, /, expr: Literal["A + A"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def eval(self, /, expr: Literal["A + A"], inplace: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def eval(self, /, expr: Literal["C = A + B"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def eval(self, /, expr: Literal["A = A + A"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def eval(self, /, expr: Literal["A = A + A"], inplace: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def eval(self, /, expr: Literal["1 + 1"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def eval(self, /, expr: Literal["1 + 1"], inplace: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def eval(self, /, expr: str):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def eval(self, /, expr: str, inplace: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def eval(self, /, expr: Literal["A = B + C"], inplace: bool):
        """
        usage.koalas: 2
        """
        ...

    def eval(self, /, expr: str, inplace: bool = ...):
        """
        usage.koalas: 15
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

    def expanding(self, /, min_periods: int):
        """
        usage.koalas: 3
        """
        ...

    @overload
    def explode(self, /, column: Literal["A"]):
        """
        usage.dask: 2
        usage.koalas: 2
        """
        ...

    @overload
    def explode(self, /, column: Literal["B"]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def explode(self, /, column: Tuple[Literal["A"], Literal["Z"]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def explode(self, /, column: Tuple[Literal["B"], Literal["X"]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def explode(self, /, column: Literal["Z"]):
        """
        usage.koalas: 1
        """
        ...

    def explode(
        self,
        /,
        column: Union[
            Literal["A", "Z", "B"], Tuple[Literal["A", "B"], Literal["Z", "X"]]
        ],
    ):
        """
        usage.dask: 2
        usage.koalas: 7
        """
        ...

    @overload
    def ffill(self, /):
        """
        usage.dask: 1
        usage.koalas: 1
        """
        ...

    @overload
    def ffill(self, /, limit: int):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def ffill(self, /, inplace: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def ffill(self, /, axis: int):
        """
        usage.dask: 1
        """
        ...

    def ffill(self, /, limit: int = ..., inplace: bool = ..., axis: int = ...):
        """
        usage.dask: 2
        usage.koalas: 3
        """
        ...

    @overload
    def fillna(self, /, value: int):
        """
        usage.dask: 2
        usage.koalas: 6
        usage.seaborn: 1
        usage.statsmodels: 4
        """
        ...

    @overload
    def fillna(self, /, value: Dict[Literal["z", "y", "x"], int]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def fillna(self, /, method: Literal["ffill"]):
        """
        usage.dask: 1
        usage.koalas: 3
        """
        ...

    @overload
    def fillna(self, /, method: Literal["ffill"], limit: int):
        """
        usage.dask: 1
        usage.koalas: 2
        """
        ...

    @overload
    def fillna(self, /, method: Literal["bfill"]):
        """
        usage.dask: 2
        usage.koalas: 3
        """
        ...

    @overload
    def fillna(self, /, method: Literal["bfill"], limit: int):
        """
        usage.dask: 2
        usage.koalas: 2
        """
        ...

    @overload
    def fillna(self, /, value: Dict[Literal["z", "y", "x"], int], inplace: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def fillna(self, /, value: pandas.core.series.Series):
        """
        usage.dask: 1
        usage.koalas: 1
        """
        ...

    @overload
    def fillna(
        self, /, value: Dict[Tuple[Literal["x", "y"], Literal["a", "b", "c"]], int]
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def fillna(self, /, value: Dict[Literal["x"], int]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def fillna(
        self,
        /,
        value: Dict[Union[Tuple[Literal["x"], Literal["b"]], Literal["x"]], int],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def fillna(
        self,
        /,
        value: Dict[Union[Literal["x"], Tuple[Literal["x"], Literal["b"]]], int],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def fillna(self, /, value: Literal[""]):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def fillna(self, /, method: Literal["backfill"]):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    def fillna(self, /, value: float):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def fillna(self, /, value: Dict[int, Literal["foo"]]):
        """
        usage.modin: 1
        """
        ...

    @overload
    def fillna(self, /, value: int, downcast: Literal["infer"]):
        """
        usage.modin: 1
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
    def fillna(self, /, value: None, method: Literal["bfill"], axis: int, limit: int):
        """
        usage.dask: 1
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

    def fillna(
        self,
        /,
        value: object = ...,
        method: Union[Literal["ffill", "pad", "bfill", "backfill"], None] = ...,
        axis: int = ...,
        limit: Union[int, None] = ...,
        inplace: bool = ...,
    ):
        """
        usage.dask: 31
        usage.koalas: 24
        usage.modin: 2
        usage.seaborn: 1
        usage.statsmodels: 10
        """
        ...

    @overload
    def filter(self, /, items: List[Literal["aa", "ab"]], axis: int):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def filter(self, /, items: List[Literal["db", "ba"]], axis: int):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def filter(self, /, like: Literal["b"], axis: Literal["index"]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def filter(self, /, like: Literal["c"], axis: Literal["columns"]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def filter(self, /, regex: Literal["b.*"], axis: Literal["index"]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def filter(self, /, regex: Literal["b.*"], axis: Literal["columns"]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def filter(self, /, items: List[Tuple[Literal["aa", "bd"], int]], axis: int):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def filter(self, /, like: Literal["b"], axis: int):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def filter(self, /, regex: Literal["b.*"], axis: int):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def filter(
        self, /, items: List[Tuple[Literal["x", "z"], Literal["ba", "db"]]], axis: int
    ):
        """
        usage.koalas: 1
        """
        ...

    def filter(
        self,
        /,
        axis: Union[int, Literal["columns", "index"]],
        like: Literal["b", "c"] = ...,
        items: List[
            Union[
                Tuple[Literal["x", "z", "aa", "bd"], Union[Literal["ba", "db"], int]],
                Literal["aa", "ab", "db", "ba"],
            ]
        ] = ...,
        regex: Literal["b.*"] = ...,
    ):
        """
        usage.koalas: 15
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

    def first_valid_index(self, /):
        """
        usage.koalas: 1
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
    def get(self, /, key: Literal["day"], default: Literal["day"]):
        """
        usage.seaborn: 2
        """
        ...

    @overload
    def get(self, /, key: Literal["total_bill"], default: Literal["total_bill"]):
        """
        usage.seaborn: 2
        """
        ...

    @overload
    def get(self, /, key: None, default: None):
        """
        usage.seaborn: 4
        """
        ...

    @overload
    def get(self, /, key: Literal["smoker"], default: Literal["smoker"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get(self, /, key: Literal["time"], default: Literal["time"]):
        """
        usage.seaborn: 2
        """
        ...

    @overload
    def get(self, /, key: Literal["tip"], default: Literal["tip"]):
        """
        usage.seaborn: 2
        """
        ...

    @overload
    def get(self, /, key: Literal["sex"], default: Literal["sex"]):
        """
        usage.seaborn: 2
        """
        ...

    @overload
    def get(self, /, key: Literal["pulse"], default: Literal["pulse"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get(self, /, key: Literal["kind"], default: Literal["kind"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get(self, /, key: Literal["alive"], default: Literal["alive"]):
        """
        usage.seaborn: 2
        """
        ...

    @overload
    def get(self, /, key: Literal["age"], default: Literal["age"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get(self, /, key: Literal["embark_town"], default: Literal["embark_town"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get(self, /, key: Literal["who"], default: Literal["who"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get(self, /, key: Literal["survived"], default: Literal["survived"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get(self, /, key: Literal["x"], default: Literal["x"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get(self, /, key: Literal["y"], default: Literal["y"]):
        """
        usage.seaborn: 2
        """
        ...

    @overload
    def get(self, /, key: Literal["hue"], default: pandas.core.series.Series):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get(self, /, key: Literal["size"], default: pandas.core.series.Series):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get(self, /, key: Literal["style"], default: pandas.core.series.Series):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get(self, /, key: Literal["x"], default: numpy.ndarray):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get(self, /, key: Literal["y"], default: numpy.ndarray):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get(self, /, key: Literal["a"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get(self, /, key: Literal["weights"], default: None):
        """
        usage.seaborn: 5
        """
        ...

    @overload
    def get(self, /, key: Literal["x"], default: None):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get(self, /, key: Literal["y"], default: None):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get(self, /, key: Literal["hue"], default: None):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get(self, /, key: Literal["g"], default: Literal["g"]):
        """
        usage.seaborn: 3
        """
        ...

    @overload
    def get(self, /, key: Literal["h"], default: Literal["h"]):
        """
        usage.seaborn: 2
        """
        ...

    @overload
    def get(self, /, key: numpy.ndarray, default: numpy.ndarray):
        """
        usage.seaborn: 2
        """
        ...

    @overload
    def get(self, /, key: Literal["u"], default: Literal["u"]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get(self, /, key: Literal["bad_input"], default: Literal["bad_input"]):
        """
        usage.seaborn: 4
        """
        ...

    @overload
    def get(self, /, key: Literal["x"], default: pandas.core.series.Series):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get(self, /, key: Literal["y"], default: pandas.core.series.Series):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def get(self, /, key: Literal["units"], default: pandas.core.series.Series):
        """
        usage.seaborn: 1
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

    def get(
        self,
        /,
        key: Union[str, numpy.ndarray, None],
        default: Union[pandas.core.series.Series, numpy.ndarray, None, str] = ...,
    ):
        """
        usage.dask: 10
        usage.seaborn: 55
        """
        ...

    @overload
    def groupby(self, /, by: List[pandas.core.series.Series]):
        """
        usage.dask: 15
        usage.koalas: 3
        usage.modin: 4
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["__groupkey_0__"]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def groupby(self, /, by: pandas.core.series.Series):
        """
        usage.dask: 106
        usage.koalas: 98
        usage.seaborn: 1
        """
        ...

    @overload
    def groupby(self, /, by: Tuple[Literal["a"], Literal["x"]]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def groupby(self, /, by: List[Tuple[Literal["a"], Literal["x", "y"]]]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def groupby(self, /, by: Literal["A"], as_index: bool):
        """
        usage.koalas: 9
        """
        ...

    @overload
    def groupby(self, /, by: pandas.core.series.Series, as_index: bool):
        """
        usage.koalas: 28
        """
        ...

    @overload
    def groupby(self, /, by: Tuple[Literal["X"], Literal["A"]], as_index: bool):
        """
        usage.koalas: 3
        """
        ...

    @overload
    def groupby(self, /, by: Tuple[Literal["X"], Literal["A"]]):
        """
        usage.koalas: 8
        """
        ...

    @overload
    def groupby(self, /, by: Literal["kind"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def groupby(self, /, by: Literal["group"]):
        """
        usage.dask: 12
        usage.koalas: 4
        """
        ...

    @overload
    def groupby(self, /, by: Tuple[Literal["x"], Literal["group"]]):
        """
        usage.koalas: 3
        """
        ...

    @overload
    def groupby(self, /, by: Literal["b"]):
        """
        usage.dask: 26
        usage.koalas: 22
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["b", "a"]]):
        """
        usage.dask: 9
        usage.koalas: 11
        usage.modin: 1
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["b"]]):
        """
        usage.dask: 1
        usage.koalas: 18
        """
        ...

    @overload
    def groupby(self, /, by: Tuple[Literal["x"], Literal["b"]]):
        """
        usage.koalas: 11
        """
        ...

    @overload
    def groupby(self, /, by: List[Tuple[Literal["x"], Literal["a", "b"]]]):
        """
        usage.koalas: 11
        """
        ...

    @overload
    def groupby(self, /, by: Literal["d"]):
        """
        usage.koalas: 4
        """
        ...

    @overload
    def groupby(self, /, by: Literal["car_id"]):
        """
        usage.koalas: 4
        """
        ...

    @overload
    def groupby(self, /, by: Literal["A"]):
        """
        usage.dask: 9
        usage.koalas: 23
        """
        ...

    @overload
    def groupby(self, /, by: Literal["a"]):
        """
        usage.dask: 41
        usage.koalas: 31
        """
        ...

    @overload
    def groupby(self, /, by: Tuple[Literal["x"], Literal["a"]]):
        """
        usage.koalas: 12
        """
        ...

    @overload
    def groupby(self, /, by: Tuple[Literal["x"], Literal["a"]], as_index: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def groupby(self, /, by: Literal["a"], as_index: bool):
        """
        usage.koalas: 7
        """
        ...

    @overload
    def groupby(self, /, by: Literal["a"], axis: int):
        """
        usage.koalas: 4
        """
        ...

    @overload
    def groupby(self, /, by: Literal["a"], axis: Literal["index"]):
        """
        usage.koalas: 4
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["a"]]):
        """
        usage.dask: 9
        usage.koalas: 10
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["B", "A"]]):
        """
        usage.dask: 1
        usage.koalas: 1
        """
        ...

    @overload
    def groupby(self, /, by: List[Tuple[Literal["X", "Y"], Literal["A", "B"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def groupby(self, /, by: Literal["b"], as_index: bool):
        """
        usage.koalas: 4
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["__groupkey_1__", "__groupkey_0__"]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def groupby(self, /, by: List[Tuple[Literal["__groupkey_0__"], Literal[""]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def groupby(
        self,
        /,
        by: List[Tuple[Literal["__groupkey_0__", "__groupkey_1__"], Literal[""]]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def groupby(self, /, by: List[pandas.core.series.Series], as_index: bool):
        """
        usage.koalas: 4
        """
        ...

    @overload
    def groupby(self, /, by: List[Union[pandas.core.series.Series, Literal["a"]]]):
        """
        usage.koalas: 3
        usage.modin: 2
        """
        ...

    @overload
    def groupby(self, /, by: List[Union[Literal["b"], pandas.core.series.Series]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["labels", "groups"]]):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["params", "dl_idx"]]):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["censored", "det_limit_index"]]):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["cen", "det_limit_index"]]):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def groupby(self, /, by: Literal["i"]):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def groupby(self, /, by: pandas.core.indexes.numeric.Float64Index):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def groupby(self, /, by: numpy.ndarray):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["D", "B", "A", "id"]], as_index: bool):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def groupby(self, /, by: int):
        """
        usage.dask: 2
        usage.statsmodels: 1
        """
        ...

    @overload
    def groupby(self, /, by: Literal["strat"]):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def groupby(self, /, by: Literal["vec"]):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def groupby(self, /, level: int):
        """
        usage.dask: 6
        usage.statsmodels: 1
        """
        ...

    @overload
    def groupby(self, /, by: Literal["firm"]):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    def groupby(self, /, by: Literal["year"]):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    def groupby(self, /, by: Literal["h"]):
        """
        usage.prophet: 2
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["c", "b", "a"]]):
        """
        usage.dask: 2
        usage.modin: 1
        """
        ...

    @overload
    def groupby(self, /, by: List[Union[pandas.core.series.Series, Literal["b", "a"]]]):
        """
        usage.modin: 2
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["hue"]], as_index: bool, sort: bool):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["size"]], as_index: bool, sort: bool):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["style"]], as_index: bool, sort: bool):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["style", "hue"]], as_index: bool, sort: bool):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def groupby(
        self, /, by: List[Literal["style", "size", "hue"]], as_index: bool, sort: bool
    ):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["size", "hue"]], as_index: bool, sort: bool):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["col", "hue"]], as_index: bool, sort: bool):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def groupby(self, /, by: Literal["c"]):
        """
        usage.seaborn: 3
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["col"]], as_index: bool, sort: bool):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["row"]], as_index: bool, sort: bool):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def groupby(self, /, by: Literal["x"]):
        """
        usage.dask: 8
        usage.seaborn: 1
        """
        ...

    @overload
    def groupby(self, /, by: Literal["date"]):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["user_id", "date"]]):
        """
        usage.pyjanitor: 1
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
    def groupby(self, /, by: List[Literal["a"]], group_keys: bool):
        """
        usage.dask: 3
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["b", "a"]], group_keys: bool):
        """
        usage.dask: 3
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
    def groupby(self, /, by: List[Literal["x", "a"]], group_keys: bool):
        """
        usage.dask: 1
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
        level: Union[int, List[int]] = ...,
        by: object = ...,
        group_keys: bool = ...,
        dropna: bool = ...,
        as_index: bool = ...,
        sort: bool = ...,
    ):
        """
        usage.dask: 450
        usage.koalas: 352
        usage.modin: 10
        usage.prophet: 2
        usage.pyjanitor: 2
        usage.seaborn: 14
        usage.statsmodels: 21
        """
        ...

    @overload
    def head(self, /, n: int):
        """
        usage.dask: 13
        usage.koalas: 6
        usage.prophet: 20
        """
        ...

    @overload
    def head(self, /):
        """
        usage.dask: 5
        """
        ...

    def head(self, /, n: int = ...):
        """
        usage.dask: 18
        usage.koalas: 6
        usage.prophet: 20
        """
        ...

    @overload
    def idxmax(self, /):
        """
        usage.dask: 1
        usage.koalas: 1
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

    def idxmax(self, /, skipna: bool = ..., axis: int = ...):
        """
        usage.dask: 8
        usage.koalas: 1
        """
        ...

    @overload
    def idxmin(self, /):
        """
        usage.dask: 1
        usage.koalas: 1
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

    def idxmin(self, /, axis: int = ..., skipna: bool = ...):
        """
        usage.dask: 8
        usage.koalas: 1
        """
        ...

    def info(self, /, buf: _io.StringIO, memory_usage: bool):
        """
        usage.dask: 1
        """
        ...

    @overload
    def insert(
        self, /, loc: int, column: Literal["HR"], value: pandas.core.series.Series
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def insert(self, /, loc: int, column: Literal["const"], value: numpy.ndarray):
        """
        usage.statsmodels: 6
        """
        ...

    @overload
    def insert(
        self, /, loc: int, column: Literal["x"], value: pandas.core.series.Series
    ):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def insert(
        self, /, loc: int, column: Literal["y"], value: pandas.core.series.Series
    ):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def insert(self, /, loc: int, column: Literal["y"], value: numpy.ndarray):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def insert(self, /, loc: int, column: Literal["x"], value: numpy.ndarray):
        """
        usage.seaborn: 1
        """
        ...

    def insert(
        self,
        /,
        loc: int,
        column: Literal["x", "y", "const", "HR"],
        value: Union[pandas.core.series.Series, numpy.ndarray],
    ):
        """
        usage.seaborn: 4
        usage.statsmodels: 7
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

    @overload
    def interpolate(self, /):
        """
        usage.statsmodels: 3
        """
        ...

    def interpolate(self, /, method: str = ..., axis: int = ...):
        """
        usage.statsmodels: 3
        usage.xarray: 10
        """
        ...

    @overload
    def isin(self, /, values: List[Union[Literal["six"], int]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def isin(
        self,
        /,
        values: Dict[Literal["c", "a"], List[Union[int, Literal["one", "three"]]]],
    ):
        """
        usage.koalas: 1
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

    def isin(
        self,
        /,
        values: Union[
            List[Union[Literal["six"], int]],
            Dict[Literal["c", "a", "b"], List[Union[int, Literal["one", "three"]]]],
        ],
    ):
        """
        usage.dask: 6
        usage.koalas: 2
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
        usage.koalas: 1
        usage.pyjanitor: 2
        usage.seaborn: 1
        usage.statsmodels: 3
        """
        ...

    def items(self, /):
        """
        usage.seaborn: 1
        usage.xarray: 2
        """
        ...

    def iteritems(self, /):
        """
        usage.dask: 2
        usage.koalas: 3
        usage.seaborn: 2
        usage.statsmodels: 1
        usage.xarray: 1
        """
        ...

    def iterrows(self, /):
        """
        usage.dask: 2
        usage.koalas: 1
        usage.prophet: 1
        usage.statsmodels: 5
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
    def join(
        self,
        /,
        other: pandas.core.frame.DataFrame,
        lsuffix: Literal["_left"],
        rsuffix: Literal["_right"],
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def join(
        self,
        /,
        other: pandas.core.frame.DataFrame,
        on: Literal["key"],
        lsuffix: Literal["_left"],
        rsuffix: Literal["_right"],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def join(
        self,
        /,
        other: pandas.core.frame.DataFrame,
        on: List[Tuple[Literal["x"], Literal["key"]]],
        lsuffix: Literal["_left"],
        rsuffix: Literal["_right"],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def join(self, /, other: pandas.core.series.Series, how: Literal["outer"]):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    def join(self, /, other: pandas.core.series.Series):
        """
        usage.pyjanitor: 1
        usage.statsmodels: 3
        """
        ...

    @overload
    def join(self, /, other: pandas.core.frame.DataFrame):
        """
        usage.dask: 1
        usage.pyjanitor: 1
        usage.statsmodels: 2
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
        other: Union[pandas.core.frame.DataFrame, pandas.core.series.Series],
        how: Literal["right", "left", "outer", "inner"] = ...,
        lsuffix: Literal["l", "_l", "_left"] = ...,
        rsuffix: Literal["r", "_r", "_right"] = ...,
    ):
        """
        usage.dask: 31
        usage.koalas: 4
        usage.pyjanitor: 2
        usage.statsmodels: 8
        """
        ...

    def keys(self, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def kurt(self, /, axis: int, numeric_only: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def kurt(self, /, axis: int):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def kurt(self, /, numeric_only: bool):
        """
        usage.koalas: 1
        """
        ...

    def kurt(self, /, numeric_only: bool = ..., axis: int = ...):
        """
        usage.koalas: 3
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

    def last_valid_index(self, /):
        """
        usage.koalas: 3
        """
        ...

    @overload
    def mad(self, /):
        """
        usage.koalas: 3
        """
        ...

    @overload
    def mad(self, /, axis: int):
        """
        usage.koalas: 3
        """
        ...

    def mad(self, /, axis: int = ...):
        """
        usage.koalas: 6
        """
        ...

    @overload
    def mask(self, /, cond: pandas.core.frame.DataFrame):
        """
        usage.dask: 1
        usage.koalas: 5
        """
        ...

    @overload
    def mask(self, /, cond: pandas.core.frame.DataFrame, other: float):
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
        cond: Union[pandas.core.frame.DataFrame, pandas.core.series.Series],
        other: Union[pandas.core.frame.DataFrame, float] = ...,
    ):
        """
        usage.dask: 6
        usage.koalas: 5
        """
        ...

    @overload
    def max(self, /, axis: int, numeric_only: None):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def max(self, /, axis: int):
        """
        usage.dask: 1
        usage.koalas: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    def max(self, /):
        """
        usage.dask: 4
        usage.koalas: 3
        usage.prophet: 1
        usage.seaborn: 1
        usage.statsmodels: 2
        """
        ...

    @overload
    def max(self, /, axis: int, skipna: bool):
        """
        usage.dask: 3
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
        self, /, axis: Union[int, Literal["columns", "index"]] = ..., skipna: bool = ...
    ):
        """
        usage.dask: 12
        usage.koalas: 5
        usage.prophet: 1
        usage.seaborn: 1
        usage.statsmodels: 3
        """
        ...

    @overload
    def mean(self, /, axis: int):
        """
        usage.dask: 1
        usage.koalas: 5
        usage.statsmodels: 2
        """
        ...

    @overload
    def mean(self, /, axis: int, numeric_only: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def mean(self, /):
        """
        usage.dask: 7
        usage.koalas: 3
        usage.seaborn: 1
        usage.statsmodels: 17
        """
        ...

    @overload
    def mean(self, /, numeric_only: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def mean(self, /, axis: int, skipna: bool):
        """
        usage.dask: 3
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
        self, /, axis: Union[int, Literal["columns", "index"]] = ..., skipna: bool = ...
    ):
        """
        usage.dask: 15
        usage.koalas: 10
        usage.seaborn: 1
        usage.statsmodels: 19
        """
        ...

    @overload
    def median(self, /, axis: int, numeric_only: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def median(self, /):
        """
        usage.statsmodels: 1
        """
        ...

    def median(self, /, axis: int = ..., numeric_only: bool = ...):
        """
        usage.koalas: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    def melt(self, /):
        """
        usage.dask: 1
        usage.koalas: 3
        """
        ...

    @overload
    def melt(self, /, id_vars: Literal["A"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def melt(self, /, id_vars: List[Literal["B", "A"]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def melt(self, /, id_vars: Tuple[Literal["A"], Literal["B"]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def melt(self, /, id_vars: List[Literal["A"]], value_vars: List[Literal["C"]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def melt(
        self,
        /,
        id_vars: List[Literal["A"]],
        value_vars: List[Literal["B"]],
        var_name: Literal["myVarname"],
        value_name: Literal["myValname"],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def melt(self, /, value_vars: Tuple[Literal["A"], Literal["B"]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def melt(self, /, id_vars: List[Tuple[Literal["X"], Literal["A"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def melt(
        self,
        /,
        id_vars: List[Tuple[Literal["X"], Literal["A"]]],
        value_vars: List[Tuple[Literal["Y"], Literal["C"]]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def melt(
        self,
        /,
        id_vars: List[Tuple[Literal["X"], Literal["A"]]],
        value_vars: List[Tuple[Literal["X"], Literal["B"]]],
        var_name: List[Literal["myV2", "myV1"]],
        value_name: Literal["myValname"],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def melt(
        self,
        /,
        id_vars: Literal["@index"],
        var_name: Literal["@columns"],
        value_name: Literal["@values"],
    ):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def melt(self, /, var_name: Literal["@columns"], value_name: Literal["@values"]):
        """
        usage.seaborn: 1
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
        id_vars: Union[
            None,
            Literal["B", "C", "@index", "A"],
            List[Union[Literal["B", "A"], Tuple[Literal["X"], Literal["A"]]]],
            Tuple[Literal["A"], Literal["B"]],
        ] = ...,
        value_vars: Union[
            None,
            Literal["C"],
            List[
                Union[
                    Literal["C", "B", "A"], Tuple[Literal["X", "Y"], Literal["B", "C"]]
                ]
            ],
            Tuple[Literal["A"], Literal["B"]],
        ] = ...,
        var_name: Union[
            None,
            Literal["myvar", "@columns", "myVarname"],
            List[Literal["myV2", "myV1"]],
        ] = ...,
        value_name: Literal["myval", "value", "@values", "myValname"] = ...,
        col_level: None = ...,
    ):
        """
        usage.dask: 10
        usage.koalas: 12
        usage.seaborn: 2
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
        how: Literal["left"],
        on: List[Literal["__0_bucket"]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def merge(self, /, right: pandas.core.frame.DataFrame):
        """
        usage.koalas: 4
        """
        ...

    @overload
    def merge(self, /, right: pandas.core.frame.DataFrame, on: Literal["value"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        left_on: Literal["lkey"],
        right_on: Literal["rkey"],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        right_on: Literal["rkey"],
        left_index: bool,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        left_on: Literal["lkey"],
        right_index: bool,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def merge(
        self, /, right: pandas.core.frame.DataFrame, left_index: bool, right_index: bool
    ):
        """
        usage.koalas: 4
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        left_on: List[Literal["value", "lkey"]],
        right_on: List[Literal["value", "rkey"]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        right_on: List[Literal["value", "rkey"]],
        left_index: bool,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        left_on: List[Literal["value", "lkey"]],
        right_index: bool,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["inner"],
        on: Literal["value"],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["inner"],
        left_on: Literal["lkey"],
        right_on: Literal["rkey"],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["left"],
        on: Literal["value"],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["left"],
        left_on: Literal["lkey"],
        right_on: Literal["rkey"],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["right"],
        on: Literal["value"],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["right"],
        left_on: Literal["lkey"],
        right_on: Literal["rkey"],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["outer"],
        on: Literal["value"],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["outer"],
        left_on: Literal["lkey"],
        right_on: Literal["rkey"],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        left_on: Literal["lkey"],
        right_on: Literal["rkey"],
        suffixes: List[Literal["_right", "_left"]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def merge(self, /, right: pandas.core.series.Series):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.series.Series,
        left_on: Literal["x"],
        right_on: Literal["x"],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.series.Series,
        right_on: Literal["x"],
        left_index: bool,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def merge(self, /, right: pandas.core.series.Series, how: Literal["inner"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.series.Series,
        how: Literal["inner"],
        left_on: Literal["x"],
        right_on: Literal["x"],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def merge(self, /, right: pandas.core.series.Series, how: Literal["left"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.series.Series,
        how: Literal["left"],
        left_on: Literal["x"],
        right_on: Literal["x"],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def merge(self, /, right: pandas.core.series.Series, how: Literal["right"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.series.Series,
        how: Literal["right"],
        left_on: Literal["x"],
        right_on: Literal["x"],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def merge(self, /, right: pandas.core.series.Series, how: Literal["outer"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.series.Series,
        how: Literal["outer"],
        left_on: Literal["x"],
        right_on: Literal["x"],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.series.Series,
        how: Literal["outer"],
        left_index: bool,
        right_index: bool,
        suffixes: List[Literal["_right", "_left"]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        on: List[Tuple[Literal["a"], Literal["value"]]],
    ):
        """
        usage.koalas: 1
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
        usage.koalas: 1
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
        usage.koalas: 1
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
        usage.koalas: 1
        usage.statsmodels: 2
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        left_on: Literal["A"],
        right_index: bool,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        right_on: Literal["B"],
        left_index: bool,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        left_on: Literal["A"],
        right_on: Literal["B"],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["left"],
        on: List[Literal["__a_bucket"]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def merge(
        self,
        /,
        right: pandas.core.frame.DataFrame,
        how: Literal["left"],
        on: List[Literal["__single_bucket"]],
    ):
        """
        usage.koalas: 1
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
        right: Union[pandas.core.frame.DataFrame, pandas.core.series.Series],
        how: str = ...,
        on: Union[
            Literal["x", "emp_id", "idx", "value"],
            List[
                Union[
                    Tuple[Literal["a"], Literal["value"]],
                    Literal["__0_bucket", "__a_bucket", "__single_bucket", "idx", "k"],
                ]
            ],
            None,
        ] = ...,
        left_on: Union[List[str], str, None] = ...,
        right_on: Union[str, List[str], None] = ...,
        left_index: bool = ...,
        right_index: bool = ...,
        suffixes: Union[Tuple[Literal["_x", "1"], Literal["_y", "2"]], List[str]] = ...,
        indicator: bool = ...,
    ):
        """
        usage.dask: 306
        usage.koalas: 46
        usage.statsmodels: 2
        """
        ...

    @overload
    def min(self, /, axis: int, numeric_only: None):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def min(self, /):
        """
        usage.dask: 4
        usage.koalas: 51
        usage.seaborn: 2
        usage.statsmodels: 3
        """
        ...

    @overload
    def min(self, /, axis: int):
        """
        usage.dask: 1
        usage.koalas: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    def min(self, /, axis: int, skipna: bool):
        """
        usage.dask: 3
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
        self,
        /,
        axis: Union[int, Literal["columns", "index"]] = ...,
        skipna: bool = ...,
        numeric_only: None = ...,
    ):
        """
        usage.dask: 12
        usage.koalas: 53
        usage.seaborn: 2
        usage.statsmodels: 4
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
    def mul(self, /, other: pandas.core.series.Series, axis: int, level: int):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    def mul(self, /, other: pandas.core.series.Series, level: int):
        """
        usage.statsmodels: 1
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
        other: Union[pandas.core.series.Series, int, pandas.core.frame.DataFrame],
        axis: Union[int, Literal["columns", "index"]] = ...,
        level: int = ...,
        fill_value: int = ...,
    ):
        """
        usage.dask: 11
        usage.statsmodels: 4
        """
        ...

    @overload
    def nlargest(self, /, n: int, columns: Literal["a"]):
        """
        usage.dask: 2
        usage.koalas: 1
        """
        ...

    @overload
    def nlargest(self, /, n: int, columns: List[Literal["b", "a"]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def nlargest(self, /, n: int, columns: List[Literal["c", "a"]]):
        """
        usage.dask: 2
        """
        ...

    def nlargest(
        self, /, n: int, columns: Union[Literal["a"], List[Literal["b", "a", "c"]]]
    ):
        """
        usage.dask: 4
        usage.koalas: 2
        """
        ...

    def notna(self, /):
        """
        usage.seaborn: 1
        """
        ...

    def notnull(self, /):
        """
        usage.dask: 2
        usage.koalas: 1
        """
        ...

    @overload
    def nsmallest(self, /, n: int, columns: Literal["a"]):
        """
        usage.dask: 2
        usage.koalas: 1
        """
        ...

    @overload
    def nsmallest(self, /, n: int, columns: List[Literal["b", "a"]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def nsmallest(self, /, n: int, columns: List[Literal["c", "a"]]):
        """
        usage.dask: 2
        """
        ...

    def nsmallest(
        self, /, n: int, columns: Union[Literal["a"], List[Literal["b", "a", "c"]]]
    ):
        """
        usage.dask: 4
        usage.koalas: 2
        """
        ...

    @overload
    def nunique(self, /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def nunique(self, /, dropna: bool):
        """
        usage.koalas: 2
        """
        ...

    def nunique(self, /, dropna: bool = ...):
        """
        usage.koalas: 4
        """
        ...

    def pct_change(self, /, periods: int):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def pivot_table(self, /, values: Literal["b"], columns: Literal["a"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def pivot_table(
        self, /, values: Literal["b"], index: List[Literal["c"]], columns: Literal["a"]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def pivot_table(
        self,
        /,
        values: Literal["b"],
        index: List[Literal["c"]],
        columns: Literal["a"],
        aggfunc: Literal["sum"],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def pivot_table(
        self,
        /,
        values: List[Literal["b"]],
        index: List[Literal["c"]],
        columns: Literal["a"],
        aggfunc: Literal["sum"],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def pivot_table(
        self,
        /,
        values: List[Literal["e", "b"]],
        index: List[Literal["c"]],
        columns: Literal["a"],
        aggfunc: Literal["sum"],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def pivot_table(
        self,
        /,
        values: List[Literal["d", "e", "b"]],
        index: List[Literal["c"]],
        columns: Literal["a"],
        aggfunc: Literal["sum"],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def pivot_table(
        self,
        /,
        values: List[Literal["e", "b"]],
        index: List[Literal["c"]],
        columns: Literal["a"],
        aggfunc: Dict[Literal["e", "b"], Literal["sum", "mean"]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def pivot_table(
        self,
        /,
        values: Literal["b"],
        index: List[Literal["c", "e"]],
        columns: Literal["a"],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def pivot_table(
        self,
        /,
        values: Literal["b"],
        index: List[Literal["c", "e"]],
        columns: Literal["a"],
        fill_value: int,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def pivot_table(
        self,
        /,
        values: List[Tuple[Literal["x"], Literal["b"]]],
        columns: List[Tuple[Literal["x"], Literal["a"]]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def pivot_table(
        self,
        /,
        values: List[Tuple[Literal["x"], Literal["b"]]],
        index: List[Tuple[Literal["z"], Literal["c"]]],
        columns: List[Tuple[Literal["x"], Literal["a"]]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def pivot_table(
        self,
        /,
        values: List[Tuple[Literal["x", "y"], Literal["b", "e"]]],
        index: List[Tuple[Literal["z"], Literal["c"]]],
        columns: List[Tuple[Literal["x"], Literal["a"]]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def pivot_table(
        self,
        /,
        values: List[Tuple[Literal["x", "y", "w"], Literal["b", "e", "d"]]],
        index: List[Tuple[Literal["z"], Literal["c"]]],
        columns: List[Tuple[Literal["x"], Literal["a"]]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def pivot_table(
        self,
        /,
        values: List[Tuple[Literal["x", "y"], Literal["b", "e"]]],
        index: List[Tuple[Literal["z"], Literal["c"]]],
        columns: List[Tuple[Literal["x"], Literal["a"]]],
        aggfunc: Dict[
            Tuple[Literal["x", "y"], Literal["b", "e"]], Literal["sum", "mean"]
        ],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def pivot_table(
        self,
        /,
        values: Literal["D"],
        index: List[Literal["B", "A"]],
        columns: Literal["C"],
        aggfunc: Literal["sum"],
        fill_value: int,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def pivot_table(
        self,
        /,
        values: List[Literal["b"]],
        index: List[Literal["c"]],
        columns: Literal["a"],
        aggfunc: Dict[Literal["b"], Literal["mean"]],
    ):
        """
        usage.koalas: 1
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
        values: Union[
            Literal["B", "D", "b"],
            List[
                Union[
                    Tuple[Literal["x", "y", "w"], Literal["b", "e", "d"]],
                    Literal["b", "e", "d"],
                ]
            ],
        ],
        columns: Union[Literal["C", "a"], List[Tuple[Literal["x"], Literal["a"]]]],
        index: Union[
            Literal["A"],
            List[Union[Literal["c", "e", "B", "A"], Tuple[Literal["z"], Literal["c"]]]],
        ] = ...,
        aggfunc: Union[
            Literal["count", "sum", "mean"],
            Dict[
                Union[Tuple[Literal["x", "y"], Literal["b", "e"]], Literal["e", "b"]],
                Literal["sum", "mean"],
            ],
        ] = ...,
        fill_value: int = ...,
    ):
        """
        usage.dask: 3
        usage.koalas: 16
        """
        ...

    @overload
    def pop(self, /, item: Literal["realdpi"]):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def pop(self, /, item: Literal["species"]):
        """
        usage.seaborn: 1
        """
        ...

    def pop(self, /, item: Literal["species", "realdpi"]):
        """
        usage.seaborn: 1
        usage.statsmodels: 1
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
    def quantile(self, /, q: float):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def quantile(self, /, q: numpy.ndarray):
        """
        usage.statsmodels: 1
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
        q: Union[float, numpy.ndarray, List[Union[numpy.float64, float]]] = ...,
        axis: int = ...,
    ):
        """
        usage.dask: 7
        usage.statsmodels: 2
        """
        ...

    @overload
    def query(self, /, expr: Literal["A == 1"]):
        """
        usage.koalas: 3
        """
        ...

    @overload
    def query(self, /, expr: Literal["A > @num"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def query(self, /, expr: Literal["A > B"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def query(self, /, expr: Literal["A < C"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def query(self, /, expr: Literal["C == B"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def query(self, /, expr: Literal["A > B"], inplace: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def query(self, /, expr: Literal["A < C"], inplace: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def query(self, /, expr: Literal["C == B"], inplace: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def query(self, /, expr: Literal["not outlier"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def query(self, /, expr: Literal["outlier"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def query(self, /, expr: Literal["not a == 3"]):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def query(self, /, expr: Literal["a == 3"]):
        """
        usage.pyjanitor: 1
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

    def query(self, /, expr: str, inplace: bool = ...):
        """
        usage.dask: 4
        usage.koalas: 12
        usage.pyjanitor: 2
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
    def rank(self, /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def rank(self, /, ascending: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def rank(self, /, method: Literal["min"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def rank(self, /, method: Literal["max"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def rank(self, /, method: Literal["first"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def rank(self, /, method: Literal["dense"]):
        """
        usage.koalas: 1
        """
        ...

    def rank(
        self,
        /,
        ascending: bool = ...,
        method: Literal["dense", "first", "max", "min"] = ...,
    ):
        """
        usage.koalas: 7
        """
        ...

    @overload
    def reindex(
        self,
        /,
        labels: List[Literal["C", "B", "A"]],
        columns: List[Literal["3", "2", "numbers"]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def reindex(
        self,
        /,
        labels: List[Literal["C", "B", "A"]],
        index: List[Literal["3", "2", "numbers"]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def reindex(self, /, index: List[Literal["B", "A"]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def reindex(self, /, index: List[Literal["3", "2", "B", "A"]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def reindex(self, /, index: List[Literal["3", "2", "E", "A"]], fill_value: int):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def reindex(self, /, columns: List[Literal["numbers"]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def reindex(
        self, /, columns: List[Literal["3", "2", "numbers"]], fill_value: float
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def reindex(
        self, /, columns: List[Tuple[Literal["X", "Y"], Literal["numbers", "2", "3"]]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def reindex(
        self,
        /,
        columns: List[Tuple[Literal["X", "Y"], Literal["numbers", "2", "3"]]],
        fill_value: float,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def reindex(self, /, labels: pandas.core.indexes.multi.MultiIndex):
        """
        usage.statsmodels: 1
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
    def reindex(self, /, labels: pandas.core.indexes.numeric.Int64Index):
        """
        usage.seaborn: 1
        usage.statsmodels: 2
        """
        ...

    @overload
    def reindex(self, /, labels: pandas.core.indexes.base.Index):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def reindex(self, /, labels: pandas.core.indexes.range.RangeIndex):
        """
        usage.modin: 2
        usage.statsmodels: 1
        """
        ...

    @overload
    def reindex(self, /, labels: range):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def reindex(self, /, index: List[int], columns: List[int], fill_value: int):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def reindex(self, /, labels: pandas.core.indexes.period.PeriodIndex):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def reindex(self, /, labels: pandas.core.indexes.datetimes.DatetimeIndex):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def reindex(self, /, labels: pandas.core.indexes.numeric.Float64Index):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def reindex(self, /, labels: pandas.core.indexes.category.CategoricalIndex):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def reindex(
        self,
        /,
        columns: List[
            Literal["cities", "animals@#$%^", "decorated-elephant", "Bell__Chart", "a"]
        ],
        copy: bool,
    ):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def reindex(
        self,
        /,
        columns: List[
            Literal["cities", "decorated-elephant", "a", "Bell__Chart", "animals@#$%^"]
        ],
        copy: bool,
    ):
        """
        usage.pyjanitor: 1
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
        labels: object = ...,
        index: List[Union[str, int]] = ...,
        columns: Union[
            pandas.core.indexes.base.Index,
            List[
                Union[str, Tuple[Literal["X", "Y"], Literal["numbers", "2", "3"]], int]
            ],
        ] = ...,
        copy: bool = ...,
        fill_value: Union[float, int] = ...,
    ):
        """
        usage.dask: 12
        usage.koalas: 9
        usage.modin: 2
        usage.pyjanitor: 2
        usage.seaborn: 3
        usage.statsmodels: 10
        usage.xarray: 2
        """
        ...

    @overload
    def rename(self, /, columns: Dict[Literal["B", "A"], Literal["b", "a"]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def rename(self, /, index: Dict[int, int]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def rename(self, /, index: Dict[int, int], inplace: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def rename(self, /, mapper: Callable, axis: Literal["columns"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def rename(self, /, mapper: Callable, axis: Literal["index"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def rename(self, /, index: Dict[int, int], columns: Callable):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def rename(self, /, columns: Callable):
        """
        usage.dask: 6
        usage.koalas: 2
        usage.pyjanitor: 6
        """
        ...

    @overload
    def rename(self, /, columns: Callable, level: int):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def rename(self, /, index: Callable):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def rename(self, /, index: Callable, level: int):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def rename(self, /, columns: Callable, level: int):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def rename(
        self,
        /,
        columns: Dict[
            Literal["df_constraint", "pvalue", "statistic"],
            Literal["df constraint", "P>chi2", "chi2"],
        ],
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def rename(
        self,
        /,
        columns: Dict[
            Literal["df_denom", "df_constraint", "pvalue", "statistic"],
            Literal["df denom", "df constraint", "P>F", "F"],
        ],
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def rename(
        self,
        /,
        columns: Dict[Literal["Std.Err.", "Coef."], Literal["log HR SE", "log HR"]],
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def rename(self, /, columns: Dict[Literal["cpi"], Literal["CPI_"]], inplace: bool):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def rename(
        self, /, columns: Dict[Literal["D", "C", "B", "A"], Literal["H", "G", "F", "E"]]
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def rename(
        self,
        /,
        mapper: Dict[Literal["mse"], Literal["rmse"]],
        axis: Literal["columns"],
        inplace: bool,
    ):
        """
        usage.prophet: 1
        """
        ...

    @overload
    def rename(self, /, columns: Dict[Literal["hue", "x"], None]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def rename(self, /, columns: Dict[Literal["x"], Literal["x"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def rename(self, /, columns: Dict[Literal["col", "x"], Literal["_", "x"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def rename(self, /, columns: Dict[Literal["x"], Literal["t"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def rename(self, /, columns: Dict[Literal["col", "x"], Literal["_", "t"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def rename(self, /, columns: Dict[Literal["x"], Literal["a"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def rename(self, /, columns: Dict[Literal["col", "x"], Literal["_", "a"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def rename(self, /, columns: Dict[Literal["x"], Literal["z"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def rename(self, /, columns: Dict[Literal["col", "x"], Literal["_", "z"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def rename(self, /, columns: Dict[Literal["weights", "x"], Literal["f", "x"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def rename(
        self, /, columns: Dict[Literal["weights", "col", "x"], Literal["f", "_", "x"]]
    ):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def rename(self, /, columns: Dict[Literal["hue", "x"], Literal["a", "x"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def rename(
        self, /, columns: Dict[Literal["col", "hue", "x"], Literal["_", "a", "x"]]
    ):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def rename(self, /, columns: Dict[Literal["hue", "x"], Literal["a", "y"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def rename(
        self, /, columns: Dict[Literal["col", "hue", "x"], Literal["_", "a", "y"]]
    ):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def rename(self, /, columns: Dict[Literal["y", "x"], Literal["y", "x"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def rename(
        self, /, columns: Dict[Literal["col", "y", "x"], Literal["_", "y", "x"]]
    ):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def rename(self, /, columns: Dict[Literal["y"], Literal["x"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def rename(self, /, columns: Dict[Literal["col", "y"], Literal["_", "x"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def rename(self, /, columns: Dict[Literal["col", "x"], Literal["a", "x"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def rename(self, /, columns: Dict[Literal["row", "x"], Literal["a", "x"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def rename(
        self, /, columns: Dict[Literal["col", "hue", "x"], Literal["c", "a", "x"]]
    ):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def rename(self, /, columns: Dict[Literal["col", "x"], Literal["_col_", "x"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def rename(self, /, columns: Dict[Literal["row", "x"], Literal["_row_", "x"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def rename(self, /, columns: dict):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def rename(self, /, columns: Dict[Literal["col", "row"], None]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def rename(self, /, columns: Dict[int, Literal["0"]]):
        """
        usage.hvplot: 1
        """
        ...

    @overload
    def rename(self, /, columns: Callable):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def rename(self, /, columns: Callable):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def rename(self, /, columns: Callable):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def rename(self, /, columns: Dict[Literal["a"], Literal["snakesOnAPlane"]]):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def rename(
        self, /, columns: Dict[Literal["Bell__Chart"], Literal["SnakesOnAPlane2"]]
    ):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def rename(
        self,
        /,
        columns: Dict[Literal["decorated-elephant"], Literal["snakes_on_a_plane3"]],
    ):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def rename(self, /, columns: Callable):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def rename(self, /, columns: Dict[Literal["a"], Literal["index"]]):
        """
        usage.pyjanitor: 1
        """
        ...

    @overload
    def rename(
        self, /, columns: Dict[Literal["bell_chart", "a"], Literal["chart", "index"]]
    ):
        """
        usage.pyjanitor: 1
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
        mapper: Union[None, Callable, Dict[Literal["mse"], Literal["rmse"]]] = ...,
        axis: Literal["columns", "index"] = ...,
        index: Union[Callable, Dict[int, int]] = ...,
        columns: Union[Callable, collections.OrderedDict, dict, Callable] = ...,
        level: int = ...,
        inplace: bool = ...,
    ):
        """
        usage.dask: 18
        usage.hvplot: 1
        usage.koalas: 15
        usage.prophet: 1
        usage.pyjanitor: 15
        usage.seaborn: 26
        usage.statsmodels: 5
        """
        ...

    @overload
    def rename_axis(self, /, mapper: List[Literal["b", "a"]]):
        """
        usage.koalas: 1
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
        mapper: Union[
            None, List[Union[Literal["b", "a"], None]], Literal["myindex", "newindex"]
        ],
        copy: bool = ...,
    ):
        """
        usage.dask: 6
        usage.koalas: 1
        """
        ...

    def reorder_levels(self, /, order: List[int]):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def replace(self, /, to_replace: Literal["Ironman"], value: Literal["Spiderman"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def replace(
        self,
        /,
        to_replace: List[Literal["Captain America", "Ironman"]],
        value: List[Literal["Hawkeye", "Rescue"]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def replace(
        self,
        /,
        to_replace: Literal["Ironman"],
        value: Literal["Spiderman"],
        inplace: bool,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def replace(self, /, to_replace: List[int], value: int):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def replace(self, /, to_replace: List[int], value: List[int]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def replace(self, /, to_replace: Dict[int, int]):
        """
        usage.dask: 1
        usage.koalas: 2
        """
        ...

    @overload
    def replace(self, /, to_replace: Dict[Literal["B", "A"], int], value: int):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def replace(self, /, to_replace: Dict[Literal["A"], Dict[int, int]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def replace(self, /, to_replace: Dict[Literal["X"], Dict[int, int]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def replace(
        self,
        /,
        to_replace: Dict[Tuple[Literal["X"], Literal["A", "B"]], int],
        value: int,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def replace(
        self, /, to_replace: Dict[Tuple[Literal["X"], Literal["A"]], Dict[int, int]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def replace(
        self, /, to_replace: Dict[Tuple[Literal["X"], Literal["B"]], Dict[int, int]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def replace(self, /, to_replace: Dict[bool, Literal["", "X"]]):
        """
        usage.statsmodels: 1
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
    def replace(self, /, to_replace: Dict[int, int], value: None, regex: bool):
        """
        usage.dask: 1
        """
        ...

    def replace(
        self,
        /,
        to_replace: Union[
            int,
            Dict[
                Union[
                    Literal["B", "A", "X"],
                    bool,
                    int,
                    Tuple[Literal["X"], Literal["B", "A"]],
                ],
                Union[Literal["", "X"], int, Dict[int, int]],
            ],
            Literal["Ironman"],
            List[Union[Literal["Captain America", "Ironman"], int]],
        ],
        value: Union[
            int,
            None,
            Literal["Spiderman"],
            List[Union[int, Literal["Hawkeye", "Rescue"]]],
        ] = ...,
        regex: bool = ...,
    ):
        """
        usage.dask: 4
        usage.koalas: 15
        usage.statsmodels: 1
        """
        ...

    @overload
    def resample(self, /, rule: Literal["M"], convention: Literal["end"]):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def resample(self, /, rule: Literal["Q"], convention: Literal["e"]):
        """
        usage.statsmodels: 2
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
        usage.statsmodels: 3
        """
        ...

    @overload
    def reset_index(self, /):
        """
        usage.dask: 3
        usage.hvplot: 6
        usage.koalas: 17
        usage.prophet: 1
        usage.statsmodels: 15
        """
        ...

    @overload
    def reset_index(self, /, drop: bool):
        """
        usage.dask: 24
        usage.koalas: 31
        usage.prophet: 4
        usage.pyjanitor: 1
        usage.statsmodels: 5
        """
        ...

    @overload
    def reset_index(self, /, drop: bool, inplace: bool):
        """
        usage.koalas: 1
        usage.prophet: 3
        usage.pyjanitor: 1
        """
        ...

    @overload
    def reset_index(self, /, level: Literal["class"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def reset_index(self, /, level: Literal["class"], col_level: int):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def reset_index(
        self, /, level: Literal["class"], col_level: int, col_fill: Literal["species"]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def reset_index(
        self, /, level: Literal["class"], col_level: int, col_fill: Literal["genus"]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def reset_index(self, /, level: int):
        """
        usage.koalas: 3
        """
        ...

    @overload
    def reset_index(self, /, level: List[int]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def reset_index(self, /, level: Literal["month"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def reset_index(self, /, level: Literal["year"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def reset_index(self, /, level: List[Literal["year", "month"]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def reset_index(self, /, level: Literal["month"], drop: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def reset_index(self, /, level: List[Literal["year", "month"]], drop: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def reset_index(self, /, level: Literal["unknown"]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def reset_index(self, /, inplace: bool):
        """
        usage.koalas: 1
        usage.prophet: 2
        usage.pyjanitor: 1
        """
        ...

    @overload
    def reset_index(self, /, level: int, drop: bool):
        """
        usage.dask: 2
        """
        ...

    def reset_index(
        self,
        /,
        level: Union[
            int,
            List[Union[int, Literal["year", "month"]]],
            Literal["unknown", "month", "year", "class"],
        ] = ...,
        drop: bool = ...,
        inplace: bool = ...,
        col_level: int = ...,
        col_fill: Literal["genus", "species"] = ...,
    ):
        """
        usage.dask: 29
        usage.hvplot: 6
        usage.koalas: 66
        usage.prophet: 10
        usage.pyjanitor: 3
        usage.statsmodels: 20
        """
        ...

    def rfloordiv(self, /, other: int):
        """
        usage.koalas: 1
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
    def rolling(self, /, window: int):
        """
        usage.dask: 11
        usage.koalas: 3
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
        usage.dask: 85
        usage.koalas: 3
        usage.xarray: 3
        """
        ...

    @overload
    def round(self, /, decimals: int):
        """
        usage.dask: 2
        usage.koalas: 2
        usage.statsmodels: 1
        """
        ...

    @overload
    def round(self, /, decimals: Dict[Literal["C", "A"], int]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def round(self, /, decimals: Dict[Literal["D", "A"], int]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def round(self, /, decimals: pandas.core.series.Series):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def round(
        self, /, decimals: Dict[Tuple[Literal["X", "Y"], Literal["A", "C"]], int]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def round(
        self,
        /,
        decimals: Dict[Union[Literal["Y"], Tuple[Literal["X"], Literal["A"]]], int],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def round(self, /):
        """
        usage.dask: 1
        """
        ...

    def round(
        self,
        /,
        decimals: Union[
            int,
            pandas.core.series.Series,
            Dict[
                Union[
                    Tuple[Literal["X", "Y"], Literal["A", "C"]],
                    Literal["C", "A", "D", "Y"],
                ],
                int,
            ],
        ] = ...,
    ):
        """
        usage.dask: 3
        usage.koalas: 8
        usage.statsmodels: 1
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
    def sample(self, /, frac: int):
        """
        usage.hvplot: 4
        """
        ...

    @overload
    def sample(self, /, frac: int, random_state: None):
        """
        usage.pyjanitor: 1
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
        frac: Union[float, int],
        random_state: Union[numpy.random.mtrand.RandomState, None] = ...,
        replace: bool = ...,
    ):
        """
        usage.dask: 2
        usage.hvplot: 4
        usage.pyjanitor: 1
        """
        ...

    @overload
    def select_dtypes(self, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def select_dtypes(self, /, include: Literal["a"], exclude: Literal["a"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def select_dtypes(
        self, /, include: List[Union[Literal["category"], Type[numpy.number]]]
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def select_dtypes(self, /, include: Literal["category"]):
        """
        usage.modin: 1
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
            Literal["category", "a"],
        ] = ...,
        exclude: Union[
            Type[object],
            List[Union[Literal["object", "number"], type]],
            None,
            Literal["a"],
        ] = ...,
    ):
        """
        usage.dask: 20
        usage.koalas: 2
        usage.modin: 1
        usage.sklearn: 11
        usage.statsmodels: 1
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
    def set_index(
        self, /, keys: Literal["__index_level_0__"], drop: bool, append: bool
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["summary"], drop: bool, append: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_index(
        self, /, keys: Literal["__index_level_1__"], drop: bool, append: bool
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["key"], drop: bool, append: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["foo"], drop: bool, append: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["index"], drop: bool, append: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["(a, bar)"], drop: bool, append: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["level_0"], drop: bool, append: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["A"], drop: bool, append: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["B"], drop: bool, append: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["C"], drop: bool, append: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["month"], drop: bool, append: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["year"], drop: bool, append: bool):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["col1"], drop: bool, append: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_index(
        self, /, keys: Literal["__index_level_2__"], drop: bool, append: bool
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["class"], drop: bool, append: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["animal"], drop: bool, append: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["locomotion"], drop: bool, append: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["index1"], drop: bool, append: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["index2"], drop: bool, append: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["a"], drop: bool, append: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["__groupkey_0__"], drop: bool, append: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["(a, x)"], drop: bool, append: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["index_1"], drop: bool, append: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["index_2"], drop: bool, append: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["name"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["name"], drop: bool, append: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["a"], append: bool):
        """
        usage.koalas: 5
        """
        ...

    @overload
    def set_index(self, /, keys: List[int]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_index(self, /, keys: List[Literal["y", "x"]]):
        """
        usage.koalas: 1
        usage.xarray: 3
        """
        ...

    @overload
    def set_index(self, /, keys: List[Tuple[Literal["x"], Literal["a", "b"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["aa"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["ba"], append: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Tuple[Literal["x"], Literal["aa"]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["key"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Tuple[Literal["x"], Literal["key"]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["lkey"]):
        """
        usage.koalas: 3
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["rkey"]):
        """
        usage.koalas: 3
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["lkey"], drop: bool, append: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_index(self, /, keys: List[Literal["value", "lkey"]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_index(self, /, keys: List[Literal["value", "rkey"]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["x"]):
        """
        usage.dask: 11
        usage.koalas: 1
        usage.xarray: 2
        """
        ...

    @overload
    def set_index(self, /, keys: Tuple[Literal["a"], Literal["lkey"]]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def set_index(self, /, keys: Tuple[Literal["a"], Literal["rkey"]]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["(a, lkey)"], drop: bool, append: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["c"], drop: bool, append: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["e"], drop: bool, append: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["(z, c)"], drop: bool, append: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_index(self, /, keys: List[Literal["locomotion", "animal", "class"]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["index"], append: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["lab"], drop: bool, append: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["a"]):
        """
        usage.dask: 5
        usage.koalas: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["d"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["d"], drop: bool, append: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Tuple[Literal["a"], Literal["x"]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Tuple[Literal["d"], Literal["y"]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["(d, y)"], drop: bool, append: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_index(self, /, keys: List[Literal["b", "a"]]):
        """
        usage.dask: 1
        usage.koalas: 3
        """
        ...

    @overload
    def set_index(
        self, /, keys: Tuple[Literal["a"], Literal["x"]], append: bool, inplace: bool
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["b"], append: bool):
        """
        usage.koalas: 6
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["b"], drop: bool, append: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["month"]):
        """
        usage.koalas: 3
        """
        ...

    @overload
    def set_index(self, /, keys: List[Literal["month", "year"]]):
        """
        usage.koalas: 3
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["month"], drop: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["month"], append: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_index(self, /, keys: List[Literal["month", "year"]], drop: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_index(self, /, keys: List[Literal["month", "year"]], append: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["year"], append: bool, inplace: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["unknown"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_index(self, /, keys: List[Literal["unknown", "month"]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["a"], append: bool, inplace: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["year"], append: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["Koalas"], drop: bool):
        """
        usage.koalas: 1
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
    def set_index(self, /, keys: pandas.core.indexes.numeric.Int64Index):
        """
        usage.xarray: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["Location"]):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["state"]):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def set_index(self, /, keys: pandas.core.series.Series):
        """
        usage.dask: 8
        usage.statsmodels: 1
        """
        ...

    @overload
    def set_index(self, /, keys: List[Literal["year", "firm"]]):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def set_index(self, /, keys: List[Literal["TVnews", "income", "educ"]]):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["factor"]):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["idx"]):
        """
        usage.dask: 11
        usage.modin: 2
        """
        ...

    @overload
    def set_index(self, /, keys: List[Literal["widths", "edges"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["time"]):
        """
        usage.hvplot: 4
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["value2"]):
        """
        usage.geopandas: 2
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["column_name"]):
        """
        usage.pyjanitor: 1
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
    def set_index(self, /, keys: List[Literal["a"]]):
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

    def set_index(
        self, /, keys: object, drop: bool = ..., append: bool = ..., inplace: bool = ...
    ):
        """
        usage.dask: 119
        usage.geopandas: 2
        usage.hvplot: 4
        usage.koalas: 95
        usage.modin: 2
        usage.pyjanitor: 1
        usage.seaborn: 1
        usage.statsmodels: 6
        usage.xarray: 15
        """
        ...

    @overload
    def shift(self, /, periods: int):
        """
        usage.dask: 6
        usage.koalas: 2
        """
        ...

    @overload
    def shift(self, /, periods: int, axis: int):
        """
        usage.dask: 1
        usage.seaborn: 1
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
        usage.koalas: 2
        usage.seaborn: 1
        """
        ...

    @overload
    def skew(self, /, axis: int, numeric_only: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def skew(self, /, axis: int):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def skew(self, /, numeric_only: bool):
        """
        usage.koalas: 1
        """
        ...

    def skew(self, /, numeric_only: bool = ..., axis: int = ...):
        """
        usage.koalas: 3
        """
        ...

    @overload
    def sort_index(self, /):
        """
        usage.dask: 7
        usage.koalas: 356
        usage.statsmodels: 13
        """
        ...

    @overload
    def sort_index(self, /, ascending: bool):
        """
        usage.dask: 1
        usage.koalas: 1
        """
        ...

    @overload
    def sort_index(self, /, na_position: Literal["first"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def sort_index(self, /, inplace: bool):
        """
        usage.koalas: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    def sort_index(self, /, level: List[int]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def sort_index(self, /, level: Literal["col"]):
        """
        usage.prophet: 1
        """
        ...

    @overload
    def sort_index(self, /, axis: int):
        """
        usage.hvplot: 1
        """
        ...

    def sort_index(
        self,
        /,
        ascending: bool = ...,
        na_position: Literal["first"] = ...,
        inplace: bool = ...,
        level: Union[Literal["col"], List[int]] = ...,
        axis: int = ...,
    ):
        """
        usage.dask: 8
        usage.hvplot: 1
        usage.koalas: 360
        usage.prophet: 1
        usage.statsmodels: 14
        """
        ...

    @overload
    def sort_values(self, /, by: Literal["__0_bucket"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def sort_values(
        self, /, by: List[Literal["B", "key_right", "A", "key_left"]], inplace: bool
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["B", "A", "key"]], inplace: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def sort_values(
        self,
        /,
        by: List[Tuple[Literal["x_left", "Y", "x_right"], Literal["key", "A", "B"]]],
        inplace: bool,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def sort_values(
        self,
        /,
        by: List[Tuple[Literal["x", "Y"], Literal["key", "A", "B"]]],
        inplace: bool,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["value", "variable"]]):
        """
        usage.dask: 2
        usage.koalas: 6
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["myValname", "myVarname"]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["value", "variable_1", "variable_0"]]):
        """
        usage.koalas: 3
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["myValname", "myV2", "myV1"]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["value", "v1", "v0"]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["y", "rkey", "x", "value", "lkey"]]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def sort_values(self, /, by: List[str]):
        """
        usage.dask: 29
        usage.koalas: 4
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["y", "x", "value"]]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["y", "value_y", "rkey", "x", "value_x"]]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["y", "value_y", "x", "value_x", "lkey"]]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["y", "value_y", "x", "value_x"]]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["y", "value", "rkey", "x"]]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["y", "x", "value", "lkey"]]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["x", "value", "lkey"]]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["x_right", "x_left", "value", "lkey"]]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def sort_values(
        self,
        /,
        by: List[
            Tuple[Literal["a", "b", "c"], Literal["lkey", "value", "x", "rkey", "y"]]
        ],
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def sort_values(
        self, /, by: List[Tuple[Literal["a", "b", "c"], Literal["value", "x", "y"]]]
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def sort_values(
        self,
        /,
        by: List[Tuple[Literal["a_x", "b", "a_y", "c"], Literal["value", "x", "y"]]],
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["B", "A"]]):
        """
        usage.dask: 1
        usage.koalas: 7
        """
        ...

    @overload
    def sort_values(self, /, by: Literal["b"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["a", "b"]]):
        """
        usage.dask: 1
        usage.koalas: 2
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["a", "b"]], ascending: List[bool]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def sort_values(
        self, /, by: List[Literal["a", "b"]], na_position: Literal["first"]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def sort_values(self, /, by: Literal["b"], inplace: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Tuple[Literal["X"], Literal["A", "B"]]]):
        """
        usage.koalas: 4
        """
        ...

    @overload
    def sort_values(self, /, by: Literal["__a_bucket"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["C", "B", "A"]]):
        """
        usage.dask: 1
        usage.koalas: 2
        """
        ...

    @overload
    def sort_values(
        self,
        /,
        by: List[Tuple[Literal["A", "B", "C"], Literal["", "min", "max", "sum"]]],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def sort_values(
        self, /, by: List[Tuple[Literal["A", "B", "C"], Literal["", "sum"]]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["C", "B"]]):
        """
        usage.dask: 1
        usage.koalas: 2
        """
        ...

    @overload
    def sort_values(
        self, /, by: List[Tuple[Literal["B", "C"], Literal["min", "max", "sum"]]]
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def sort_values(self, /, by: List[Tuple[Literal["A", "B", "C"], Literal["sum"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Tuple[Literal["X", "Y"], Literal["B", "C"]]]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def sort_values(
        self,
        /,
        by: List[
            Tuple[Literal["X", "Y"], Literal["B", "C"], Literal["min", "max", "sum"]]
        ],
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def sort_values(self, /, by: Literal["A"]):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def sort_values(self, /, by: Tuple[Literal["X"], Literal["A"]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def sort_values(self, /, by: Tuple[Literal["x"], Literal["a"]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def sort_values(self, /, by: Literal["a"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["b", "a"]]):
        """
        usage.dask: 3
        usage.koalas: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["c", "a", "b"]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["a"]]):
        """
        usage.dask: 1
        usage.koalas: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["c", "b", "a"]]):
        """
        usage.dask: 1
        usage.koalas: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["d", "c", "a", "b"]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["d", "c", "b", "a"]]):
        """
        usage.dask: 1
        usage.koalas: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[int]):
        """
        usage.dask: 6
        usage.koalas: 3
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["C", "A"]]):
        """
        usage.dask: 2
        usage.koalas: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["D", "C", "A"]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Tuple[Literal["X"], Literal["A", "C"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Tuple[Literal["X"], Literal["A", "B", "C"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Tuple[Literal["X"], Literal["A", "C", "D"]]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def sort_values(
        self, /, by: List[Tuple[Literal["X"], Literal["A", "B", "C", "D"]]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def sort_values(
        self, /, by: List[Union[Literal["ABC"], Tuple[Literal["X"], Literal["A"]]]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def sort_values(
        self, /, by: List[Union[Tuple[Literal["X"], Literal["B"]], Literal["ABC"]]]
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["B", "A", "C"]]):
        """
        usage.dask: 1
        usage.koalas: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["B", "C"]]):
        """
        usage.dask: 1
        usage.koalas: 2
        """
        ...

    @overload
    def sort_values(self, /, by: Literal["c"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def sort_values(self, /, by: Tuple[Literal["y"], Literal["c"]]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["B"]]):
        """
        usage.dask: 1
        usage.koalas: 1
        """
        ...

    @overload
    def sort_values(self, /, by: Literal["__single_bucket"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def sort_values(self, /, by: Literal["conc"], axis: int):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def sort_values(self, /, by: Literal["obs"], axis: int):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def sort_values(self, /, by: Literal["res"], axis: int):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def sort_values(
        self,
        /,
        by: List[Literal["largest", "high"]],
        ascending: List[bool],
        inplace: bool,
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["unadj_p"]], ascending: bool):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["x0"]]):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["x2", "x0"]]):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def sort_values(
        self, /, by: List[Literal["factor", "count"]], ascending: List[bool]
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def sort_values(
        self, /, by: List[Literal["block", "count"]], ascending: List[bool]
    ):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def sort_values(self, /, by: Literal["ds"]):
        """
        usage.prophet: 1
        """
        ...

    @overload
    def sort_values(self, /, by: Literal["horizon"], inplace: bool):
        """
        usage.prophet: 1
        """
        ...

    @overload
    def sort_values(self, /, by: Literal["h"]):
        """
        usage.prophet: 2
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["y", "x"]]):
        """
        usage.dask: 3
        usage.seaborn: 2
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["y", "x", "units"]]):
        """
        usage.seaborn: 1
        """
        ...

    @overload
    def sort_values(self, /, by: Literal["time"]):
        """
        usage.hvplot: 1
        """
        ...

    @overload
    def sort_values(self, /, by: Literal["b"], ascending: bool):
        """
        usage.pyjanitor: 1
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
    def sort_values(self, /, by: List[Literal["c-d", "b", "a"]]):
        """
        usage.dask: 1
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
    def sort_values(self, /, by: List[Literal["z", "y", "x"]]):
        """
        usage.dask: 3
        """
        ...

    @overload
    def sort_values(self, /, by: List[Literal["D", "C", "B"]]):
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
    def sort_values(self, /, by: list):
        """
        usage.dask: 1
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
        by: Union[
            List[Union[Tuple[str, ...], str, int, float]],
            Tuple[Literal["X", "x", "y"], Literal["A", "a", "c"]],
            str,
        ],
        ascending: Union[bool, List[bool]] = ...,
        inplace: bool = ...,
    ):
        """
        usage.dask: 190
        usage.hvplot: 1
        usage.koalas: 105
        usage.prophet: 4
        usage.pyjanitor: 1
        usage.seaborn: 3
        usage.statsmodels: 12
        """
        ...

    @overload
    def squeeze(self, /, axis: int):
        """
        usage.koalas: 7
        """
        ...

    @overload
    def squeeze(self, /, axis: None):
        """
        usage.koalas: 7
        """
        ...

    @overload
    def squeeze(self, /, axis: Literal["rows"]):
        """
        usage.koalas: 6
        """
        ...

    @overload
    def squeeze(self, /, axis: Literal["index"]):
        """
        usage.koalas: 6
        """
        ...

    @overload
    def squeeze(self, /, axis: Literal["columns"]):
        """
        usage.koalas: 6
        """
        ...

    @overload
    def squeeze(self, /):
        """
        usage.dask: 3
        usage.modin: 2
        usage.statsmodels: 3
        """
        ...

    def squeeze(
        self, /, axis: Union[Literal["columns", "index", "rows"], int, None] = ...
    ):
        """
        usage.dask: 3
        usage.koalas: 32
        usage.modin: 2
        usage.statsmodels: 3
        """
        ...

    @overload
    def stack(self, /):
        """
        usage.koalas: 6
        usage.seaborn: 1
        usage.statsmodels: 6
        usage.xarray: 1
        """
        ...

    @overload
    def stack(self, /, level: List[int]):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def stack(self, /, dropna: bool):
        """
        usage.dask: 1
        """
        ...

    def stack(self, /, level: List[int] = ..., dropna: bool = ...):
        """
        usage.dask: 1
        usage.koalas: 6
        usage.seaborn: 1
        usage.statsmodels: 8
        usage.xarray: 1
        """
        ...

    @overload
    def std(self, /, axis: int, numeric_only: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def std(self, /, axis: int):
        """
        usage.dask: 1
        usage.koalas: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    def std(self, /):
        """
        usage.dask: 5
        usage.koalas: 3
        usage.seaborn: 1
        usage.statsmodels: 5
        """
        ...

    @overload
    def std(self, /, numeric_only: bool):
        """
        usage.koalas: 1
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
    def std(self, /, ddof: int):
        """
        usage.dask: 3
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
        axis: Union[int, Literal["columns", "index"]] = ...,
        skipna: bool = ...,
        ddof: int = ...,
    ):
        """
        usage.dask: 20
        usage.koalas: 6
        usage.seaborn: 1
        usage.statsmodels: 6
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
    def sum(self, /, axis: int, numeric_only: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def sum(self, /):
        """
        usage.dask: 22
        usage.koalas: 15
        """
        ...

    @overload
    def sum(self, /, axis: int):
        """
        usage.dask: 3
        usage.koalas: 1
        usage.prophet: 1
        usage.statsmodels: 13
        """
        ...

    @overload
    def sum(self, /, numeric_only: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def sum(self, /, axis: Literal["columns"]):
        """
        usage.dask: 1
        usage.seaborn: 1
        """
        ...

    @overload
    def sum(self, /, axis: int, skipna: bool):
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
        axis: Union[Literal["columns", "index"], int] = ...,
        min_count: int = ...,
        skipna: bool = ...,
        numeric_only: bool = ...,
    ):
        """
        usage.dask: 32
        usage.koalas: 18
        usage.prophet: 1
        usage.seaborn: 1
        usage.statsmodels: 13
        """
        ...

    @overload
    def tail(self, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def tail(self, /, n: int):
        """
        usage.dask: 5
        usage.koalas: 5
        usage.prophet: 8
        """
        ...

    def tail(self, /, n: int = ...):
        """
        usage.dask: 5
        usage.koalas: 6
        usage.prophet: 8
        """
        ...

    @overload
    def take(self, /, indices: List[int]):
        """
        usage.koalas: 8
        """
        ...

    @overload
    def take(self, /, indices: range):
        """
        usage.koalas: 4
        """
        ...

    @overload
    def take(self, /, indices: List[int], axis: int):
        """
        usage.koalas: 8
        """
        ...

    @overload
    def take(self, /, indices: range, axis: int):
        """
        usage.koalas: 4
        """
        ...

    @overload
    def take(self, /, indices: numpy.ndarray):
        """
        usage.dask: 1
        """
        ...

    def take(self, /, indices: Union[numpy.ndarray, range, List[int]], axis: int = ...):
        """
        usage.dask: 1
        usage.koalas: 24
        """
        ...

    @overload
    def to_csv(
        self,
        /,
        path_or_buf: None,
        sep: Literal[","],
        na_rep: Literal[""],
        columns: None,
        header: bool,
        index: bool,
        quotechar: Literal['"'],
        date_format: None,
        escapechar: None,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def to_csv(self, /, index: bool):
        """
        usage.koalas: 5
        """
        ...

    @overload
    def to_csv(
        self,
        /,
        path_or_buf: None,
        sep: Literal[","],
        na_rep: Literal[""],
        columns: List[Literal["aa"]],
        header: bool,
        index: bool,
        quotechar: Literal['"'],
        date_format: None,
        escapechar: None,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def to_csv(self, /, columns: List[Literal["aa"]], index: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def to_csv(
        self,
        /,
        path_or_buf: None,
        sep: Literal[","],
        na_rep: Literal["null"],
        columns: None,
        header: bool,
        index: bool,
        quotechar: Literal['"'],
        date_format: None,
        escapechar: None,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def to_csv(self, /, na_rep: Literal["null"], index: bool):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def to_csv(self, /, header: bool, index: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def to_csv(
        self,
        /,
        sep: Literal["|"],
        columns: List[Literal["aa"]],
        header: bool,
        index: bool,
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def to_csv(self, /, sep: Literal["|"], columns: List[Literal["a"]], index: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def to_csv(
        self,
        /,
        path_or_buf: Literal["test.csv"],
        sep: Literal[","],
        encoding: None,
        compression: Literal["infer"],
    ):
        """
        usage.modin: 1
        """
        ...

    @overload
    def to_csv(
        self,
        /,
        path_or_buf: Literal["test.csv.gz"],
        sep: Literal[","],
        encoding: None,
        compression: Literal["gzip"],
    ):
        """
        usage.modin: 1
        """
        ...

    @overload
    def to_csv(
        self,
        /,
        path_or_buf: Literal["test.csv.bz2"],
        sep: Literal[","],
        encoding: None,
        compression: Literal["bz2"],
    ):
        """
        usage.modin: 1
        """
        ...

    @overload
    def to_csv(
        self,
        /,
        path_or_buf: Literal["test.csv.xz"],
        sep: Literal[","],
        encoding: None,
        compression: Literal["xz"],
    ):
        """
        usage.modin: 1
        """
        ...

    @overload
    def to_csv(
        self,
        /,
        path_or_buf: Literal["test.csv.zip"],
        sep: Literal[","],
        encoding: None,
        compression: Literal["zip"],
    ):
        """
        usage.modin: 1
        """
        ...

    @overload
    def to_csv(
        self,
        /,
        path_or_buf: Literal["test.csv"],
        sep: Literal["\t"],
        encoding: None,
        compression: Literal["infer"],
    ):
        """
        usage.modin: 1
        """
        ...

    @overload
    def to_csv(
        self,
        /,
        path_or_buf: Literal["test.csv"],
        sep: Literal[","],
        encoding: Literal["latin8"],
        compression: Literal["infer"],
    ):
        """
        usage.modin: 1
        """
        ...

    @overload
    def to_csv(
        self,
        /,
        path_or_buf: Literal["test.csv"],
        sep: Literal[","],
        encoding: Literal["ISO-8859-1"],
        compression: Literal["infer"],
    ):
        """
        usage.modin: 1
        """
        ...

    @overload
    def to_csv(
        self,
        /,
        path_or_buf: Literal["test.csv"],
        sep: Literal[","],
        encoding: Literal["latin1"],
        compression: Literal["infer"],
    ):
        """
        usage.modin: 1
        """
        ...

    @overload
    def to_csv(
        self,
        /,
        path_or_buf: Literal["test.csv"],
        sep: Literal[","],
        encoding: Literal["iso-8859-1"],
        compression: Literal["infer"],
    ):
        """
        usage.modin: 1
        """
        ...

    @overload
    def to_csv(
        self,
        /,
        path_or_buf: Literal["test.csv"],
        sep: Literal[","],
        encoding: Literal["cp1252"],
        compression: Literal["infer"],
    ):
        """
        usage.modin: 1
        """
        ...

    @overload
    def to_csv(
        self,
        /,
        path_or_buf: Literal["test.csv"],
        sep: Literal[","],
        encoding: Literal["utf8"],
        compression: Literal["infer"],
    ):
        """
        usage.modin: 1
        """
        ...

    @overload
    def to_csv(
        self,
        /,
        path_or_buf: Literal["/tmp/tmptwszhbso.csv"],
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
        path_or_buf: Literal["/tmp/tmpsu6hgqwx.csv"],
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
        path_or_buf: Literal["/tmp/tmphbpetj19.csv"],
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
        path_or_buf: Union[str, _io.TextIOWrapper, None] = ...,
        index: bool = ...,
        sep: Literal[",", "\t", "|"] = ...,
        encoding: Union[str, None] = ...,
        compression: Literal["infer", "zip", "xz", "bz2", "gzip"] = ...,
        na_rep: Literal["null", ""] = ...,
        columns: Union[List[Literal["aa", "a"]], None] = ...,
        header: bool = ...,
        quotechar: Literal['"'] = ...,
        date_format: None = ...,
        escapechar: None = ...,
    ):
        """
        usage.dask: 5
        usage.koalas: 14
        usage.modin: 12
        """
        ...

    def to_dict(self, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def to_excel(self, /, excel_writer: str):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def to_excel(
        self,
        /,
        excel_writer: pandas.io.excel._openpyxl._OpenpyxlWriter,
        sheet_name: Literal["Sheet_name_1"],
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def to_excel(
        self,
        /,
        excel_writer: pandas.io.excel._openpyxl._OpenpyxlWriter,
        sheet_name: Literal["Sheet_name_2"],
    ):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def to_excel(self, /, excel_writer: Literal["test.xlsx"]):
        """
        usage.modin: 1
        """
        ...

    def to_excel(
        self,
        /,
        excel_writer: Union[str, pandas.io.excel._openpyxl._OpenpyxlWriter],
        sheet_name: Literal["Sheet_name_2", "Sheet_name_1"] = ...,
    ):
        """
        usage.koalas: 6
        usage.modin: 1
        """
        ...

    def to_feather(self, /, path: Literal["test.feather"]):
        """
        usage.modin: 1
        """
        ...

    def to_hdf(
        self, /, path_or_buf: Literal["test.hdf"], key: Literal["df"], format: None
    ):
        """
        usage.modin: 1
        """
        ...

    @overload
    def to_html(self, /, bold_rows: bool, notebook: bool):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def to_html(self, /, show_dimensions: bool, bold_rows: bool, notebook: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def to_html(self, /, buf: Literal["test.html"]):
        """
        usage.modin: 1
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

    def to_html(
        self,
        /,
        max_rows: int = ...,
        show_dimensions: bool = ...,
        bold_rows: bool = ...,
        notebook: bool = ...,
    ):
        """
        usage.dask: 2
        usage.koalas: 3
        usage.modin: 1
        """
        ...

    @overload
    def to_json(self, /, orient: Literal["records"]):
        """
        usage.koalas: 4
        """
        ...

    @overload
    def to_json(self, /, path_or_buf: Literal["test.json"]):
        """
        usage.modin: 1
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
        path_or_buf: str = ...,
        orient: Literal["values", "columns", "index", "records", "split"] = ...,
        lines: bool = ...,
    ):
        """
        usage.dask: 24
        usage.koalas: 4
        usage.modin: 1
        """
        ...

    def to_latex(self, /):
        """
        usage.statsmodels: 1
        """
        ...

    def to_markdown(self, /):
        """
        usage.koalas: 1
        """
        ...

    def to_numpy(self, /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def to_parquet(self, /, path: str):
        """
        usage.geopandas: 3
        usage.koalas: 3
        """
        ...

    @overload
    def to_parquet(self, /, path: Literal["test.parquet"]):
        """
        usage.modin: 1
        """
        ...

    @overload
    def to_parquet(
        self, /, path: Literal["test.parquet"], partition_cols: List[Literal["col1"]]
    ):
        """
        usage.modin: 1
        """
        ...

    @overload
    def to_parquet(self, /, path: Literal["tmp.parquet"]):
        """
        usage.modin: 1
        """
        ...

    @overload
    def to_parquet(
        self, /, path: Literal["tmp_folder.parquet"], partition_cols: List[Literal["A"]]
    ):
        """
        usage.modin: 1
        """
        ...

    def to_parquet(
        self, /, path: str, partition_cols: List[Literal["col1", "A"]] = ...
    ):
        """
        usage.geopandas: 3
        usage.koalas: 3
        usage.modin: 4
        """
        ...

    @overload
    def to_period(self, /, freq: Literal["M"]):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def to_period(self, /, freq: Literal["Q"]):
        """
        usage.statsmodels: 1
        """
        ...

    def to_period(self, /, freq: Literal["Q", "M"]):
        """
        usage.statsmodels: 2
        """
        ...

    def to_pickle(self, /, path: Literal["test.pkl"]):
        """
        usage.modin: 1
        """
        ...

    @overload
    def to_records(self, /, index: bool):
        """
        usage.dask: 1
        usage.statsmodels: 10
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
        usage.statsmodels: 10
        """
        ...

    def to_sql(self, /, name: Literal["test_from_sql"], con: str):
        """
        usage.modin: 1
        """
        ...

    def to_stata(self, /, path: Literal["test.dta"]):
        """
        usage.modin: 1
        """
        ...

    @overload
    def to_string(self, /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def to_string(self, /, show_dimensions: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def to_string(self, /, max_rows: int, show_dimensions: bool):
        """
        usage.dask: 2
        """
        ...

    def to_string(self, /, max_rows: int = ..., show_dimensions: bool = ...):
        """
        usage.dask: 2
        usage.koalas: 3
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
    def transform(self, /, func: Callable, axis: int):
        """
        usage.koalas: 3
        """
        ...

    @overload
    def transform(self, /, func: Callable):
        """
        usage.koalas: 6
        """
        ...

    def transform(self, /, func: Callable, axis: int = ...):
        """
        usage.koalas: 9
        """
        ...

    def transpose(self, /):
        """
        usage.koalas: 7
        """
        ...

    @overload
    def truediv(self, /, other: pandas.core.series.Series, axis: int, level: int):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def truediv(self, /, other: pandas.core.series.Series, axis: Literal["index"]):
        """
        usage.dask: 3
        usage.seaborn: 1
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
    def truediv(self, /, other: pandas.core.series.Series, axis: Literal["columns"]):
        """
        usage.dask: 3
        """
        ...

    def truediv(
        self,
        /,
        other: Union[int, pandas.core.frame.DataFrame, pandas.core.series.Series],
        level: int = ...,
        axis: Union[int, Literal["columns", "index"]] = ...,
        fill_value: int = ...,
    ):
        """
        usage.dask: 27
        usage.seaborn: 1
        usage.statsmodels: 1
        """
        ...

    @overload
    def truncate(self, /):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def truncate(self, /, before: int):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def truncate(self, /, after: int):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def truncate(self, /, copy: bool):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def truncate(self, /, before: int, after: int, copy: bool):
        """
        usage.koalas: 4
        """
        ...

    @overload
    def truncate(self, /, before: int, after: int):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def truncate(self, /, axis: int):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def truncate(self, /, before: Literal["B"], axis: int):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def truncate(self, /, after: Literal["A"], axis: int):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def truncate(self, /, axis: int, copy: bool):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def truncate(self, /, before: Literal["B"], after: Literal["C"], axis: int):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def truncate(
        self, /, before: Literal["B"], after: Literal["C"], axis: int, copy: bool
    ):
        """
        usage.koalas: 2
        """
        ...

    def truncate(
        self,
        /,
        before: Union[Literal["B"], int] = ...,
        after: Union[Literal["C", "A"], int] = ...,
        axis: int = ...,
        copy: bool = ...,
    ):
        """
        usage.koalas: 26
        """
        ...

    @overload
    def unstack(self, /):
        """
        usage.koalas: 1
        usage.statsmodels: 4
        """
        ...

    @overload
    def unstack(self, /, level: int):
        """
        usage.koalas: 1
        """
        ...

    def unstack(self, /, level: int = ...):
        """
        usage.koalas: 2
        usage.statsmodels: 4
        """
        ...

    @overload
    def update(self, /, other: pandas.core.frame.DataFrame):
        """
        usage.koalas: 3
        """
        ...

    @overload
    def update(self, /, other: pandas.core.frame.DataFrame, overwrite: bool):
        """
        usage.koalas: 2
        """
        ...

    def update(self, /, other: pandas.core.frame.DataFrame, overwrite: bool = ...):
        """
        usage.koalas: 5
        """
        ...

    @overload
    def var(self, /, axis: int, numeric_only: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def var(self, /, axis: int):
        """
        usage.dask: 1
        usage.koalas: 1
        usage.statsmodels: 4
        """
        ...

    @overload
    def var(self, /):
        """
        usage.dask: 7
        usage.koalas: 3
        usage.seaborn: 1
        """
        ...

    @overload
    def var(self, /, numeric_only: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def var(self, /, axis: int, skipna: bool):
        """
        usage.dask: 2
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
        axis: Union[int, Literal["columns", "index"]] = ...,
        skipna: Union[bool, None] = ...,
        ddof: int = ...,
    ):
        """
        usage.dask: 26
        usage.koalas: 6
        usage.seaborn: 1
        usage.statsmodels: 4
        """
        ...

    @overload
    def where(self, /, cond: pandas.core.frame.DataFrame):
        """
        usage.dask: 1
        usage.koalas: 5
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
        cond: Union[pandas.core.frame.DataFrame, pandas.core.series.Series],
        axis: int = ...,
        other: Union[
            pandas.core.frame.DataFrame, float, pandas.core.series.Series
        ] = ...,
    ):
        """
        usage.dask: 8
        usage.koalas: 5
        """
        ...

    def xs(self, /, key: Tuple[Literal["mammal"], Literal["dog"], Literal["walks"]]):
        """
        usage.koalas: 1
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
