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

    # usage.dask: 42
    A: object

    # usage.dask: 3
    A_a: object

    # usage.dask: 19
    B: object

    # usage.dask: 4
    C: object

    # usage.dask: 2
    Date: pandas.core.series.Series

    # usage.dask: 1
    F: object

    # usage.dask: 1
    Name: object

    # usage.dask: 7
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

    # usage.dask: 116
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

    # usage.dask: 26
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

    # usage.dask: 47
    # usage.sklearn: 14
    # usage.xarray: 2
    iloc: object

    # usage.dask: 197
    # usage.sklearn: 3
    # usage.xarray: 12
    index: object

    # usage.dask: 78
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

    # usage.dask: 81
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
    def __add__(
        self,
        _0: Union[
            pandas.core.frame.DataFrame,
            float,
            dask.dataframe.core.Scalar,
            int,
            numpy.ndarray,
        ],
        /,
    ):
        """
        usage.dask: 24
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
    def __eq__(self, _0: Union[int, pandas.core.frame.DataFrame], /):
        """
        usage.dask: 9
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
        usage.sklearn: 1
        usage.xarray: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["x"], /):
        """
        usage.xarray: 3
        """
        ...

    @overload
    def __getitem__(self, _0: object, /):
        """
        usage.dask: 487
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
    def __getitem__(self, _0: numpy.ndarray, /):
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
    def __getitem__(self, _0: str, /):
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
    def __getitem__(self, _0: Literal["name"], /):
        """
        usage.sklearn: 1
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

    @overload
    def __getitem__(self, _0: Literal["0"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["c"], /):
        """
        usage.sklearn: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["A"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["B"], /):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["C"], /):
        """
        usage.sklearn: 1
        """
        ...

    def __getitem__(self, _0: object, /):
        """
        usage.dask: 487
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

    def __le__(
        self,
        _0: Union[numpy.float64, float, pandas.core.series.Series, int, numpy.int64],
        /,
    ):
        """
        usage.dask: 7
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
    def __radd__(
        self, _0: Union[pandas.core.frame.DataFrame, dask.dataframe.core.Scalar], /
    ):
        """
        usage.dask: 2
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
    def __setitem__(
        self,
        _0: Union[
            str,
            List[Literal["b", "a"]],
            pandas.core.indexes.base.Index,
            pandas.core.frame.DataFrame,
            pandas.core.indexes.numeric.Int64Index,
        ],
        _1: object,
        /,
    ):
        """
        usage.dask: 129
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

    @overload
    def __setitem__(self, _0: Literal["c"], _1: pandas.core.series.Series, /):
        """
        usage.sklearn: 2
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
    def __sub__(
        self, _0: Union[int, pandas.core.series.Series, pandas.core.frame.DataFrame], /
    ):
        """
        usage.dask: 8
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

    def all(self, /, axis: int = ..., skipna: bool = ...):
        """
        usage.dask: 11
        """
        ...

    def any(self, /, axis: int = ..., skipna: bool = ...):
        """
        usage.dask: 9
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
    def apply(
        self,
        /,
        func: Callable,
        axis: Union[int, Literal["columns"]],
        raw: bool = ...,
        result_type: None = ...,
        args: Tuple[None, ...] = ...,
    ):
        """
        usage.dask: 10
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
    def astype(
        self,
        /,
        dtype: Union[
            Dict[
                Union[int, str],
                Union[
                    Literal["category", "f8"],
                    numpy.dtype,
                    pandas.core.dtypes.dtypes.CategoricalDtype,
                    Type[float],
                ],
            ],
            pandas.core.series.Series,
            Literal["float", "float64"],
            type,
        ],
        copy: bool = ...,
    ):
        """
        usage.dask: 32
        """
        ...

    @overload
    def astype(self, /, dtype: None):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def astype(self, /, dtype: Type[numpy.float64]):
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

    def bfill(self, /, axis: int = ...):
        """
        usage.dask: 2
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
    def copy(self, /, deep: bool = ...):
        """
        usage.dask: 16
        """
        ...

    @overload
    def copy(self, /):
        """
        usage.sklearn: 4
        """
        ...

    def copy(self, /, deep: bool = ...):
        """
        usage.dask: 16
        usage.sklearn: 4
        """
        ...

    def corr(self, /, min_periods: int = ...):
        """
        usage.dask: 4
        """
        ...

    def count(self, /, axis: Union[Literal["columns", "index"], int] = ...):
        """
        usage.dask: 17
        """
        ...

    def cov(self, /, min_periods: int = ...):
        """
        usage.dask: 5
        """
        ...

    def cummax(self, /, axis: Union[int, None] = ..., skipna: bool = ...):
        """
        usage.dask: 11
        """
        ...

    def cummin(self, /, axis: Union[int, None] = ..., skipna: bool = ...):
        """
        usage.dask: 11
        """
        ...

    def cumprod(self, /, axis: Union[int, None] = ..., skipna: bool = ...):
        """
        usage.dask: 11
        """
        ...

    def cumsum(self, /, axis: Union[int, None] = ..., skipna: bool = ...):
        """
        usage.dask: 11
        """
        ...

    def describe(
        self,
        /,
        percentiles: Union[None, List[float]] = ...,
        include: Union[
            List[
                Union[
                    Type[numpy.timedelta64],
                    Literal["number", "object", "bool", "datetime"],
                ]
            ],
            None,
            Literal["all"],
        ] = ...,
        exclude: Union[None, List[Literal["object", "number"]]] = ...,
    ):
        """
        usage.dask: 21
        """
        ...

    def diff(self, /, periods: int = ..., axis: int = ...):
        """
        usage.dask: 7
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

    def ffill(self, /, axis: int = ...):
        """
        usage.dask: 2
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

    def first(self, /, offset: str):
        """
        usage.dask: 24
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

    def get(self, /, key: str):
        """
        usage.dask: 10
        """
        ...

    def groupby(
        self,
        _0: Literal["a"] = ...,
        /,
        by: object = ...,
        group_keys: bool = ...,
        level: Union[List[int], int] = ...,
        sort: bool = ...,
        *,
        dropna: bool = ...,
    ):
        """
        usage.dask: 448
        """
        ...

    def head(self, /, n: int = ...):
        """
        usage.dask: 18
        """
        ...

    def idxmax(self, /, skipna: bool = ..., axis: int = ...):
        """
        usage.dask: 8
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

    def itertuples(
        self, /, index: bool = ..., name: Union[None, Literal["Pandas"]] = ...
    ):
        """
        usage.dask: 9
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

    def last(self, /, offset: str):
        """
        usage.dask: 8
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

    def max(
        self, /, skipna: bool = ..., axis: Union[Literal["columns", "index"], int] = ...
    ):
        """
        usage.dask: 15
        """
        ...

    def mean(
        self, /, skipna: bool = ..., axis: Union[Literal["columns", "index"], int] = ...
    ):
        """
        usage.dask: 20
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
    def memory_usage(self, /, index: bool, deep: bool = ...):
        """
        usage.dask: 5
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

    def min(
        self, /, skipna: bool = ..., axis: Union[Literal["columns", "index"], int] = ...
    ):
        """
        usage.dask: 15
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

    def nsmallest(
        self, /, n: int, columns: Union[List[Literal["c", "a"]], Literal["a"]]
    ):
        """
        usage.dask: 4
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

    def prod(
        self,
        /,
        axis: Union[int, Literal["columns", "index"]] = ...,
        min_count: int = ...,
    ):
        """
        usage.dask: 15
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

    def query(self, /, expr: Literal["B != 9", "B != 0"]):
        """
        usage.dask: 4
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
    def reindex(
        self,
        /,
        labels: Union[
            pandas.core.indexes.datetimes.DatetimeIndex,
            pandas.core.indexes.multi.MultiIndex,
            pandas.core.indexes.numeric.Int64Index,
            List[str],
        ] = ...,
        fill_value: Union[int, float] = ...,
    ):
        """
        usage.dask: 14
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
        usage.dask: 14
        usage.xarray: 2
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

    def reset_index(self, /, level: int = ..., drop: bool = ...):
        """
        usage.dask: 29
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
    def rolling(
        self,
        /,
        window: Union[str, int, float, pandas.tseries.offsets.Second],
        min_periods: Union[None, int] = ...,
        center: bool = ...,
        win_type: None = ...,
        axis: Union[int, Literal["rows", "columns", "coulombs"]] = ...,
    ):
        """
        usage.dask: 84
        """
        ...

    def rolling(
        self,
        /,
        window: Union[pandas.tseries.offsets.Second, float, int, str],
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

    def round(self, /, decimals: int = ...):
        """
        usage.dask: 3
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
    def select_dtypes(
        self,
        /,
        include: Union[
            List[
                Union[type, Literal["category", "bool", "number", "object", "datetime"]]
            ],
            None,
        ],
        exclude: Union[None, List[Union[Literal["object", "number"], type]]] = ...,
    ):
        """
        usage.dask: 20
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
    def select_dtypes(self, /, include: List[Type[int]], exclude: None):
        """
        usage.sklearn: 1
        """
        ...

    @overload
    def select_dtypes(self, /, include: None, exclude: List[Type[int]]):
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
            Type[object], List[Union[type, Literal["object", "number"]]], None
        ] = ...,
    ):
        """
        usage.dask: 20
        usage.sklearn: 11
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
        usage.dask: 23
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
    def set_index(self, /, keys: object, drop: bool = ...):
        """
        usage.dask: 119
        """
        ...

    def set_index(self, /, keys: object, drop: bool = ...):
        """
        usage.dask: 119
        usage.xarray: 15
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

    def sort_index(self, /, ascending: bool = ...):
        """
        usage.dask: 8
        """
        ...

    def sort_values(
        self,
        /,
        by: List[Union[Tuple[Literal["a", "A", "B", "b"], str], int, float, str]],
    ):
        """
        usage.dask: 193
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

    def std(
        self,
        /,
        axis: Union[Literal["columns", "index"], int] = ...,
        skipna: bool = ...,
        ddof: int = ...,
    ):
        """
        usage.dask: 23
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

    def sum(
        self,
        /,
        axis: Union[int, Literal["columns", "index"]] = ...,
        min_count: int = ...,
    ):
        """
        usage.dask: 34
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

    def to_csv(
        self,
        /,
        path_or_buf: Union[
            _io.TextIOWrapper,
            Literal[
                "/tmp/tmp3ssgt61n.csv", "/tmp/tmpoxer7jfu.csv", "/tmp/tmpz91y_5zr.csv"
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

    def to_html(self, /, max_rows: int, show_dimensions: bool, notebook: bool = ...):
        """
        usage.dask: 2
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

    def to_timestamp(
        self,
        /,
        freq: Union[Literal["M"], None] = ...,
        how: Literal["s", "start"] = ...,
        axis: int = ...,
    ):
        """
        usage.dask: 4
        """
        ...

    def to_xarray(self, /):
        """
        usage.xarray: 5
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

    def var(
        self,
        /,
        axis: Union[Literal["columns", "index"], int] = ...,
        skipna: Union[bool, None] = ...,
        ddof: int = ...,
    ):
        """
        usage.dask: 31
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
