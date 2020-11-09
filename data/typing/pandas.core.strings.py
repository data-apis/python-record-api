from typing import *


class StringMethods:
    @overload
    def __getitem__(self, _0: slice[None, int, None], /):
        """
        usage.dask: 2
        usage.seaborn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: int, /):
        """
        usage.dask: 2
        """
        ...

    def __getitem__(self, _0: Union[slice[None, int, None], int], /):
        """
        usage.dask: 4
        usage.seaborn: 1
        """
        ...

    @overload
    def cat(self, /, others: pandas.core.series.Series, sep: Literal[":"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def cat(
        self,
        /,
        others: Tuple[pandas.core.series.Series],
        sep: Literal[":"],
        na_rep: None,
    ):
        """
        usage.dask: 1
        """
        ...

    @overload
    def cat(self, /, others: List[pandas.core.series.Series], sep: Literal[":"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def cat(
        self,
        /,
        others: Tuple[pandas.core.series.Series, pandas.core.series.Series],
        sep: Literal[":"],
        na_rep: None,
    ):
        """
        usage.dask: 1
        """
        ...

    def cat(
        self,
        /,
        others: Union[
            Tuple[pandas.core.series.Series, ...],
            pandas.core.series.Series,
            List[pandas.core.series.Series],
        ],
        sep: Literal[":"],
        na_rep: None = ...,
    ):
        """
        usage.dask: 4
        """
        ...

    @overload
    def contains(self, /, pat: Literal["le"], regex: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def contains(self, /, pat: Literal["White"], case: bool, regex: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def contains(self, /, pat: Literal["apples|carrots"], regex: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def contains(self, /, pat: Literal["BANANAS"], flags: re.RegexFlag, na: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def contains(self, /, pat: Literal["a"]):
        """
        usage.dask: 1
        """
        ...

    @overload
    def contains(self, /, pat: Literal["d"], case: bool):
        """
        usage.dask: 2
        """
        ...

    @overload
    def contains(self, /, pat: Literal["a"], na: bool):
        """
        usage.dask: 2
        """
        ...

    @overload
    def contains(self, /, pat: Literal["a"], regex: bool):
        """
        usage.dask: 2
        """
        ...

    @overload
    def contains(self, /, pat: Literal["at$"], regex: bool):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def contains(self, /, pat: Literal["^col_int"], regex: bool):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def contains(self, /, pat: Literal["float|str"], regex: bool):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def contains(self, /, pat: Literal["^col_s"], regex: bool):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def contains(self, /, pat: Literal["str$"], regex: bool):
        """
        usage.sklearn: 1
        """
        ...

    def contains(self, /, pat: str, flags: re.RegexFlag = ..., na: bool = ...):
        """
        usage.dask: 7
        usage.koalas: 4
        usage.sklearn: 5
        """
        ...

    @overload
    def count(self, /, pat: Literal["WH"], flags: re.RegexFlag):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def count(self, /, pat: Literal["A"]):
        """
        usage.dask: 1
        """
        ...

    def count(self, /, pat: Literal["A", "WH"], flags: re.RegexFlag = ...):
        """
        usage.dask: 1
        usage.koalas: 1
        """
        ...

    def endswith(self, /, pat: Literal["s"], na: bool):
        """
        usage.koalas: 1
        """
        ...

    def extractall(self, /, pat: Literal["(.*)b(.*)"], flags: int):
        """
        usage.dask: 2
        """
        ...

    @overload
    def find(self, /, sub: Literal["a"], start: int):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def find(self, /, sub: Literal["a"], start: int, end: int):
        """
        usage.koalas: 1
        """
        ...

    def find(self, /, sub: Literal["a"], start: int, end: int = ...):
        """
        usage.koalas: 2
        """
        ...

    def findall(self, /, pat: Literal["wh.*"], flags: re.RegexFlag):
        """
        usage.koalas: 1
        """
        ...

    def index(self, /, sub: Literal["ea"], start: int, end: int):
        """
        usage.koalas: 1
        """
        ...

    def isalpha(self, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def match(self, /, pat: Literal["apples|carrots"], na: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def match(self, /, pat: Literal["White"], case: bool):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def match(self, /, pat: Literal["BANANAS"], flags: re.RegexFlag):
        """
        usage.koalas: 1
        """
        ...

    def match(
        self,
        /,
        pat: Literal["BANANAS", "White", "apples|carrots"],
        case: bool = ...,
        na: bool = ...,
        flags: re.RegexFlag = ...,
    ):
        """
        usage.koalas: 3
        """
        ...

    @overload
    def pad(self, /, width: int, side: Literal["both"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def pad(self, /, width: int, side: Literal["right"], fillchar: Literal["-"]):
        """
        usage.koalas: 1
        """
        ...

    def pad(
        self,
        /,
        width: int,
        side: Literal["right", "both"],
        fillchar: Literal["-"] = ...,
    ):
        """
        usage.koalas: 2
        """
        ...

    def repeat(self, /, repeats: int):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def replace(self, /, pat: Literal["a."], repl: Literal["xx"], regex: bool):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def replace(self, /, pat: Literal["ing"], repl: Literal["0"], flags: re.RegexFlag):
        """
        usage.koalas: 1
        """
        ...

    def replace(
        self,
        /,
        pat: Literal["ing", "a."],
        repl: Literal["0", "xx"],
        flags: re.RegexFlag = ...,
        regex: bool = ...,
    ):
        """
        usage.koalas: 3
        """
        ...

    @overload
    def rfind(self, /, sub: Literal["a"], start: int):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def rfind(self, /, sub: Literal["a"], start: int, end: int):
        """
        usage.koalas: 1
        """
        ...

    def rfind(self, /, sub: Literal["a"], start: int, end: int = ...):
        """
        usage.koalas: 2
        """
        ...

    def rindex(self, /, sub: Literal["ea"], start: int, end: int):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def rsplit(self, /, n: int):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def rsplit(self, /, pat: Literal["-"], n: int):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def rsplit(self, /, n: int, expand: bool):
        """
        usage.koalas: 1
        """
        ...

    def rsplit(self, /, n: int, pat: Literal["-"] = ..., expand: bool = ...):
        """
        usage.koalas: 3
        """
        ...

    @overload
    def slice(self, /, start: int):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def slice(self, /, stop: int):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def slice(self, /, step: int):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def slice(self, /, start: int, stop: int, step: int):
        """
        usage.koalas: 1
        """
        ...

    def slice(self, /, start: int = ..., stop: int = ..., step: int = ...):
        """
        usage.koalas: 4
        """
        ...

    @overload
    def slice_replace(self, /, start: int, repl: Literal["X"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def slice_replace(self, /, stop: int, repl: Literal["X"]):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def slice_replace(self, /, start: int, stop: int, repl: Literal["X"]):
        """
        usage.koalas: 1
        """
        ...

    def slice_replace(self, /, repl: Literal["X"], start: int = ..., stop: int = ...):
        """
        usage.koalas: 3
        """
        ...

    @overload
    def split(self, /, n: int):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def split(self, /, pat: Literal["-"], n: int):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def split(self, /, n: int, expand: bool):
        """
        usage.dask: 3
        usage.koalas: 1
        """
        ...

    @overload
    def split(self, /, pat: None, n: int, expand: bool):
        """
        usage.dask: 2
        """
        ...

    @overload
    def split(self, /, pat: Literal[","], n: int, expand: bool):
        """
        usage.dask: 3
        """
        ...

    def split(
        self, /, n: int, pat: Union[None, Literal[",", "-"]] = ..., expand: bool = ...
    ):
        """
        usage.dask: 8
        usage.koalas: 3
        """
        ...

    def startswith(self, /, pat: Literal["car"], na: bool):
        """
        usage.koalas: 1
        """
        ...

    def upper(self, /):
        """
        usage.dask: 1
        """
        ...

    def wrap(self, /, width: int):
        """
        usage.koalas: 5
        """
        ...
