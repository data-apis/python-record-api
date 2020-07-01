from typing import *

# usage.sample_usage: 1
# usage.skimage: 248
# usage.xarray: 229
# usage.sklearn: 334
# usage.dask: 422
random: object

# usage.skimage: 7
# usage.sklearn: 7
abs: object

# usage.skimage: 82
# usage.xarray: 71
# usage.sklearn: 18
# usage.dask: 27
testing: object

# usage.skimage: 11
# usage.xarray: 3
# usage.sklearn: 24
r_: object

# usage.skimage: 11
# usage.xarray: 10
# usage.sklearn: 3
# usage.dask: 1
floating: object

# usage.skimage: 55
# usage.xarray: 19
# usage.sklearn: 159
# usage.dask: 9
newaxis: object

# usage.skimage: 88
# usage.xarray: 10
# usage.sklearn: 34
pi: object

# usage.skimage: 57
# usage.xarray: 3
# usage.sklearn: 10
# usage.dask: 1
float: object

# usage.skimage: 82
# usage.xarray: 3
# usage.sklearn: 30
# usage.dask: 1
bool: object

# usage.skimage: 24
# usage.xarray: 3
# usage.sklearn: 51
int: object

# usage.skimage: 9
# usage.dask: 1
ogrid: object

# usage.skimage: 10
# usage.xarray: 14
# usage.sklearn: 1
# usage.dask: 6
integer: object

# usage.skimage: 55
# usage.sklearn: 1
mgrid: object

# usage.skimage: 1
# usage.dask: 1
round: object

# usage.skimage: 6
# usage.xarray: 1
# usage.dask: 4
float_: object

# usage.skimage: 21
# usage.xarray: 269
# usage.sklearn: 86
# usage.dask: 124
nan: object

# usage.skimage: 6
# usage.xarray: 2
# usage.sklearn: 9
# usage.dask: 6
min: object

# usage.skimage: 27
# usage.xarray: 1
# usage.sklearn: 15
# usage.dask: 6
max: object

# usage.skimage: 98
# usage.sklearn: 11
# usage.dask: 1
double: object

# usage.skimage: 37
# usage.xarray: 11
# usage.sklearn: 74
# usage.dask: 4
inf: object

# usage.skimage: 20
# usage.xarray: 2
# usage.sklearn: 29
# usage.dask: 21
intp: object

# usage.skimage: 34
# usage.sklearn: 30
# usage.dask: 29
linalg: object

# usage.skimage: 1
# usage.sklearn: 2
divide: object

# usage.skimage: 2
# usage.sklearn: 2
signedinteger: object

# usage.skimage: 1
# usage.xarray: 1
complex: object

# usage.skimage: 1
unsignedinteger: object

# usage.skimage: 1
# usage.xarray: 1
# usage.sklearn: 1
# usage.dask: 2
__version__: object

# usage.skimage: 3
# usage.xarray: 1
int_: object

# usage.skimage: 2
typecodes: object

# usage.skimage: 1
# usage.xarray: 1
e: object

# usage.skimage: 1
# usage.sklearn: 26
c_: object

# usage.skimage: 1
uint: object

# usage.skimage: 1
# usage.xarray: 6
# usage.sklearn: 7
# usage.dask: 5
NaN: object

# usage.skimage: 27
# usage.xarray: 15
# usage.sklearn: 16
# usage.dask: 77
ma: object

# usage.skimage: 1
NAN: object

# usage.skimage: 1
s_: object

# usage.skimage: 1
# usage.dask: 1
bool8: object

# usage.skimage: 1
ubyte: object

# usage.xarray: 1
inexact: object

# usage.xarray: 1
character: object

# usage.xarray: 3
# usage.sklearn: 2
# usage.dask: 6
number: object

# usage.xarray: 3
string_: object

# usage.xarray: 3
# usage.dask: 1
complexfloating: object

# usage.xarray: 1
# usage.dask: 1
lib: object

# usage.sklearn: 1
flexible: object

# usage.sklearn: 1
infty: object

# usage.sklearn: 10
object: object

# usage.sklearn: 5
intc: object

# usage.sklearn: 2
NINF: object

# usage.sklearn: 3
euler_gamma: object

# usage.sklearn: 3
Inf: object

# usage.dask: 1
ScalarType: object

# usage.dask: 11
fft: object

# usage.dask: 3
core: object

# usage.dask: 2
True_: object

# usage.dask: 2
False_: object

# usage.dask: 1
mod: object


def arange(
    _0: object,
    _1: object = ...,
    _2: object = ...,
    _3: Union[Literal["i8"], numpy.dtype, type] = ...,
    /,
    *,
    dtype: Union[None, numpy.dtype, type, str] = ...,
    stop: int = ...,
):
    """
    usage.sample_usage: 4
    usage.skimage: 223
    usage.xarray: 403
    usage.sklearn: 151
    usage.dask: 341
    """
    ...


def array(
    _0: object,
    /,
    *,
    dtype: Union[
        List[Tuple[str, Union[str, type]]], numpy.dtype, type, str, None
    ] = ...,
    ndmin: int = ...,
    copy: bool = ...,
    order: Union[Literal["F", "C", "K"], None] = ...,
):
    """
    usage.sample_usage: 3
    usage.skimage: 1076
    usage.xarray: 400
    usage.sklearn: 815
    usage.dask: 485
    """
    ...


def zeros(
    _0: Union[
        int,
        numpy.ndarray,
        numpy.int64,
        List[int],
        Tuple[Union[numpy.int64, int, None], ...],
    ] = ...,
    _1: Union[type, numpy.dtype, Literal["bool", "double", "uint8"]] = ...,
    /,
    *,
    dtype: Union[type, str, numpy.dtype] = ...,
    order: Literal["C", "F", "f"] = ...,
    shape: Union[Tuple[int, ...], int] = ...,
):
    """
    usage.sample_usage: 1
    usage.skimage: 787
    usage.xarray: 52
    usage.sklearn: 350
    usage.dask: 50
    """
    ...


def ones(
    shape: Union[
        List[int],
        numpy.ndarray,
        int,
        numpy.int64,
        Tuple[Union[numpy.int64, int, None], ...],
    ],
    dtype: Union[
        str,
        List[
            Tuple[
                Literal["a", "b", "c", "col1", "col2"],
                Union[Literal["f8"], Tuple[Literal["f4"], Union[int, Tuple[int, int]]]],
            ]
        ],
        type,
        numpy.dtype,
        None,
    ] = ...,
    order: Literal["C", "F"] = ...,
):
    """
    usage.sample_usage: 1
    usage.skimage: 269
    usage.xarray: 59
    usage.sklearn: 210
    usage.dask: 183
    """
    ...


def linspace(
    start: Union[float, numpy.float64, int, numpy.int64],
    stop: Union[int, float, numpy.float64, numpy.int64, numpy.float32],
    num: Union[int, numpy.int64] = ...,
    endpoint: bool = ...,
    retstep: bool = ...,
    dtype: Union[type, numpy.dtype] = ...,
):
    """
    usage.sample_usage: 1
    usage.skimage: 70
    usage.xarray: 95
    usage.sklearn: 41
    usage.dask: 22
    """
    ...


def eye(N: int, M: int = ..., k: int = ..., dtype: type = ...):
    """
    usage.sample_usage: 1
    usage.skimage: 39
    usage.sklearn: 27
    usage.dask: 35
    """
    ...


def add(
    _0: object,
    _1: object,
    /,
    *,
    dtype: type = ...,
    out: Union[
        numpy.ndarray,
        dask.array.core.Array,
        dask.dataframe.core.DataFrame,
        xarray.core.dataarray.DataArray,
    ] = ...,
):
    """
    usage.sample_usage: 1
    usage.skimage: 11
    usage.xarray: 13
    usage.sklearn: 1
    usage.dask: 29
    """
    ...


def exp(
    _0: object, /, *, dtype: numpy.dtype = ..., out: dask.dataframe.core.DataFrame = ...
):
    """
    usage.sample_usage: 1
    usage.skimage: 26
    usage.xarray: 3
    usage.sklearn: 62
    usage.dask: 42
    """
    ...


def log(
    _0: object,
    /,
    *,
    out: Union[dask.dataframe.core.DataFrame, dask.array.core.Array] = ...,
):
    """
    usage.sample_usage: 1
    usage.skimage: 19
    usage.xarray: 2
    usage.sklearn: 78
    usage.dask: 47
    """
    ...


def column_stack(tup: Union[List[numpy.ndarray], Tuple[numpy.ndarray, numpy.ndarray]]):
    """
    usage.sample_usage: 1
    usage.skimage: 9
    usage.sklearn: 2
    """
    ...


def concatenate(
    _0: Union[list, Tuple[Union[List[Union[int, numpy.float64]], numpy.ndarray], ...]],
    /,
    *,
    axis: int = ...,
):
    """
    usage.sample_usage: 1
    usage.skimage: 48
    usage.xarray: 46
    usage.sklearn: 50
    usage.dask: 96
    """
    ...


def absolute(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    """
    usage.skimage: 113
    usage.sklearn: 154
    usage.dask: 49
    """
    ...


def asarray(
    a: object,
    dtype: Union[numpy.dtype, numpy.ndarray, type, str, None] = ...,
    order: Union[Literal["C", "F"], None] = ...,
):
    """
    usage.skimage: 247
    usage.xarray: 870
    usage.sklearn: 2199
    usage.dask: 126
    """
    ...


def sum(
    a: object,
    axis: Union[int, Tuple[Union[int, None], ...], None] = ...,
    out: Union[
        dask.dataframe.core.Scalar, dask.array.core.Array, dask.dataframe.core.Series
    ] = ...,
    dtype: Union[Literal["i8", "f8", "i4", "f4", "u4"], numpy.dtype, None, type] = ...,
    keepdims: bool = ...,
):
    """
    usage.skimage: 125
    usage.xarray: 54
    usage.sklearn: 208
    usage.dask: 256
    """
    ...


def vstack(tup: object):
    """
    usage.skimage: 33
    usage.sklearn: 69
    usage.dask: 10
    """
    ...


def all(
    a: object = ...,
    axis: Union[int, Tuple[Union[int, None], ...]] = ...,
    keepdims: bool = ...,
    *,
    computing_meta: bool = ...,
):
    """
    usage.skimage: 113
    usage.xarray: 14
    usage.sklearn: 91
    usage.dask: 134
    """
    ...


def round_(a: object):
    """
    usage.skimage: 30
    usage.sklearn: 3
    usage.dask: 9
    """
    ...


def asanyarray(a: object):
    """
    usage.skimage: 50
    usage.sklearn: 14
    usage.dask: 44
    """
    ...


def obj2sctype(rep: Union[Literal["float64", "float32"], type, numpy.dtype]):
    """
    usage.skimage: 14
    """
    ...


def issubdtype(arg1: Union[numpy.dtype, type], arg2: type):
    """
    usage.skimage: 162
    usage.xarray: 256
    usage.sklearn: 19
    usage.dask: 43
    """
    ...


def multiply(
    _0: Union[numpy.ndarray, numpy.ma.core.MaskedArray, dask.array.core.Array, int],
    _1: Union[int, dask.array.core.Array, numpy.ndarray, float],
    /,
    *,
    out: numpy.ndarray = ...,
    dtype: Union[numpy.dtype, type] = ...,
    casting: Literal["no"] = ...,
):
    """
    usage.skimage: 25
    usage.xarray: 2
    usage.sklearn: 2
    usage.dask: 23
    """
    ...


def reshape(
    a: Union[
        numpy.ndarray,
        List[Union[float, int, numpy.ndarray, numpy.float64, numpy.int64]],
        Tuple[numpy.ndarray, ...],
    ],
    newshape: Union[List[int], Tuple[Union[None, numpy.int64, int], ...]],
):
    """
    usage.skimage: 43
    usage.xarray: 7
    usage.sklearn: 50
    """
    ...


def sqrt(
    _0: object, /, *, out: Union[dask.dataframe.core.DataFrame, numpy.ndarray] = ...
):
    """
    usage.skimage: 112
    usage.xarray: 4
    usage.sklearn: 108
    usage.dask: 63
    """
    ...


def moveaxis(
    a: Union[numpy.ndarray, dask.array.core.Array, int, numpy.float64],
    source: Union[int, numpy.ndarray, range, Tuple[None, ...]],
    destination: Union[int, numpy.ndarray, Tuple[None, ...], List[int]],
):
    """
    usage.skimage: 6
    usage.xarray: 17
    usage.dask: 4
    """
    ...


def rollaxis(a: Union[numpy.ndarray, dask.array.core.Array], axis: int):
    """
    usage.skimage: 14
    usage.sklearn: 5
    usage.dask: 5
    """
    ...


def any(
    a: object = ...,
    axis: Union[int, Tuple[Union[int, None], ...]] = ...,
    keepdims: bool = ...,
    *,
    computing_meta: bool = ...,
):
    """
    usage.skimage: 39
    usage.xarray: 5
    usage.sklearn: 45
    usage.dask: 124
    """
    ...


def empty_like(
    _0: Union[
        numpy.ndarray,
        dask.array.core.Array,
        xarray.core.variable.IndexVariable,
        xarray.core.variable.Variable,
        numpy.ma.core.MaskedArray,
    ],
    /,
    *,
    dtype: Union[numpy.dtype, type] = ...,
    order: Literal["C"] = ...,
    subok: bool = ...,
    shape: Tuple[Union[None, int], ...] = ...,
):
    """
    usage.skimage: 48
    usage.xarray: 2
    usage.sklearn: 22
    usage.dask: 8
    """
    ...


def triu(m: numpy.ndarray):
    """
    usage.skimage: 1
    usage.dask: 8
    """
    ...


def seterr(
    divide: Literal["warn"] = ...,
    over: Literal["warn"] = ...,
    under: Literal["ignore"] = ...,
    invalid: Literal["warn", "ignore"] = ...,
):
    """
    usage.skimage: 2
    usage.sklearn: 4
    usage.dask: 2
    """
    ...


def isnan(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    """
    usage.skimage: 14
    usage.xarray: 14
    usage.sklearn: 30
    usage.dask: 150
    """
    ...


def floor(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    """
    usage.skimage: 13
    usage.xarray: 2
    usage.sklearn: 2
    usage.dask: 41
    """
    ...


def stack(arrays: Union[list, Tuple[Union[numpy.float64, numpy.ndarray], ...]]):
    """
    usage.skimage: 35
    usage.xarray: 26
    usage.dask: 30
    """
    ...


def choose(
    a: numpy.ndarray,
    choices: Union[
        Tuple[Union[int, numpy.ndarray], numpy.ndarray], List[Union[numpy.ndarray, int]]
    ],
):
    """
    usage.skimage: 2
    usage.dask: 4
    """
    ...


def amin(
    a: object = ...,
    axis: Union[int, Tuple[Union[int, None], ...], None] = ...,
    out: Union[dask.dataframe.core.Scalar, dask.dataframe.core.Series] = ...,
    keepdims: bool = ...,
    *,
    computing_meta: bool = ...,
):
    """
    usage.skimage: 60
    usage.xarray: 25
    usage.sklearn: 30
    usage.dask: 159
    """
    ...


def amax(
    a: object = ...,
    axis: Union[int, Tuple[Union[int, None], ...], None] = ...,
    out: Union[dask.dataframe.core.Scalar, dask.dataframe.core.Series] = ...,
    keepdims: bool = ...,
    *,
    computing_meta: bool = ...,
):
    """
    usage.skimage: 105
    usage.xarray: 23
    usage.sklearn: 32
    usage.dask: 158
    """
    ...


def rint(
    _0: object, /, *, out: Union[dask.dataframe.core.DataFrame, numpy.ndarray] = ...
):
    """
    usage.skimage: 2
    usage.xarray: 2
    usage.dask: 40
    """
    ...


def clip(a: object, a_min: object, a_max: object):
    """
    usage.skimage: 61
    usage.sklearn: 24
    usage.dask: 23
    """
    ...


def power(
    _0: Union[numpy.ndarray, dask.array.core.Array, int, numpy.float64, float],
    _1: Union[int, float, dask.array.core.Array, numpy.ndarray],
    /,
):
    """
    usage.skimage: 11
    usage.sklearn: 3
    usage.dask: 21
    """
    ...


def log10(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    """
    usage.skimage: 4
    usage.xarray: 2
    usage.sklearn: 3
    usage.dask: 40
    """
    ...


def load(
    file: Literal[
        "/var/folders/xn/05ktz3056kqd9n8frgd6236h0000gn/T/t",
        "/Users/saul/Downloads/scikit-image-0.17.0/skimage/",
    ]
):
    """
    usage.skimage: 28
    usage.dask: 7
    """
    ...


def meshgrid(*xi: Literal["v", "t"]):
    """
    usage.skimage: 28
    usage.xarray: 6
    usage.sklearn: 2
    usage.dask: 5
    """
    ...


def dstack(tup: object):
    """
    usage.skimage: 12
    usage.sklearn: 4
    usage.dask: 8
    """
    ...


def nonzero(a: numpy.ndarray):
    """
    usage.skimage: 22
    usage.xarray: 4
    usage.sklearn: 7
    usage.dask: 2
    """
    ...


def cbrt(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    """
    usage.skimage: 4
    usage.dask: 37
    """
    ...


def hypot(_0: object, _1: object, /):
    """
    usage.skimage: 13
    usage.xarray: 2
    usage.dask: 112
    """
    ...


def arctan2(_0: object, _1: object, /):
    """
    usage.skimage: 8
    usage.xarray: 2
    usage.dask: 112
    """
    ...


def where(_0: object, _1: object = ..., _2: object = ..., /):
    """
    usage.skimage: 26
    usage.xarray: 23
    usage.sklearn: 44
    usage.dask: 59
    """
    ...


def cos(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    """
    usage.skimage: 48
    usage.xarray: 14
    usage.sklearn: 11
    usage.dask: 42
    """
    ...


def sin(_0: object, /, *, out: object = ...):
    """
    usage.skimage: 47
    usage.xarray: 21
    usage.sklearn: 22
    usage.dask: 52
    """
    ...


def ascontiguousarray(a: Union[numpy.ndarray, List[Union[List[int], float, int]]]):
    """
    usage.skimage: 67
    usage.sklearn: 21
    usage.dask: 4
    """
    ...


def swapaxes(a: numpy.ndarray, axis1: int, axis2: int):
    """
    usage.skimage: 4
    usage.xarray: 8
    usage.sklearn: 2
    usage.dask: 4
    """
    ...


def ravel(a: object):
    """
    usage.skimage: 12
    usage.xarray: 44
    usage.sklearn: 43
    usage.dask: 1
    """
    ...


def squeeze(a: Union[numpy.ndarray, float, numpy.float64, int, List[float]]):
    """
    usage.skimage: 16
    usage.sklearn: 18
    usage.dask: 3
    """
    ...


def ones_like(
    a: Union[
        numpy.ma.core.MaskedArray,
        numpy.ndarray,
        xarray.core.variable.Variable,
        numpy.float64,
    ]
):
    """
    usage.skimage: 26
    usage.xarray: 4
    usage.sklearn: 19
    usage.dask: 5
    """
    ...


def can_cast(
    _0: Union[numpy.ndarray, numpy.dtype, int, float],
    _1: Union[numpy.dtype, Type[bool]],
    /,
    *,
    casting: Literal["unsafe", "safe", "same_kind"] = ...,
):
    """
    usage.skimage: 9
    usage.dask: 19
    """
    ...


def empty(
    _0: Union[
        int,
        numpy.ndarray,
        List[Union[numpy.int64, int]],
        Tuple[Union[numpy.int64, int, None], ...],
    ] = ...,
    _1: Union[int, numpy.dtype, Literal["float32"], type] = ...,
    /,
    *,
    dtype: Union[
        numpy.dtype, type, List[Tuple[str, Union[numpy.dtype, Type[numpy.int64]]]], str
    ] = ...,
    order: Literal["C", "F"] = ...,
    shape: Union[Tuple[int, ...], int] = ...,
):
    """
    usage.skimage: 129
    usage.xarray: 11
    usage.sklearn: 131
    usage.dask: 137
    """
    ...


def min_scalar_type(
    _0: Union[numpy.ndarray, dask.array.core.Array, int, numpy.int64, numpy.float64], /
):
    """
    usage.skimage: 5
    usage.dask: 3
    """
    ...


def unique(
    ar: Union[
        list,
        numpy.ndarray,
        pandas.core.series.Series,
        xarray.core.dataarray.DataArray,
        numpy.memmap,
    ],
    return_index: bool = ...,
    return_inverse: bool = ...,
    return_counts: bool = ...,
):
    """
    usage.skimage: 68
    usage.xarray: 14
    usage.sklearn: 216
    usage.dask: 30
    """
    ...


def zeros_like(
    a: Union[numpy.ndarray, Tuple[int, ...]],
    dtype: Union[numpy.dtype, type] = ...,
    shape: Union[int, Tuple[int, int]] = ...,
    order: Literal["F", "C"] = ...,
):
    """
    usage.skimage: 70
    usage.xarray: 43
    usage.sklearn: 15
    usage.dask: 8
    """
    ...


def full(
    shape: Union[Tuple[Union[int, None], ...], List[int], numpy.ndarray, int],
    fill_value: object,
):
    """
    usage.skimage: 36
    usage.xarray: 10
    usage.sklearn: 41
    usage.dask: 10
    """
    ...


def loadtxt(
    fname: Literal[
        "/usr/local/Caskroom/miniconda/base/envs/python-rec",
        "/Users/saul/Downloads/scikit-image-0.17.0/skimage/",
    ]
):
    """
    usage.skimage: 1
    usage.sklearn: 5
    """
    ...


def logical_and(_0: object, _1: object, /):
    """
    usage.skimage: 13
    usage.xarray: 2
    usage.sklearn: 1
    usage.dask: 112
    """
    ...


def deg2rad(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    """
    usage.skimage: 18
    usage.xarray: 2
    usage.dask: 40
    """
    ...


def rad2deg(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    """
    usage.skimage: 6
    usage.xarray: 2
    usage.dask: 40
    """
    ...


def maximum(
    _0: object,
    _1: object,
    /,
    *,
    out: numpy.ndarray = ...,
    dtype: numpy.dtype = ...,
    casting: Literal["unsafe"] = ...,
):
    """
    usage.skimage: 16
    usage.xarray: 87
    usage.sklearn: 20
    usage.dask: 200
    """
    ...


def percentile(
    a: numpy.ndarray, q: Union[numpy.ndarray, numpy.float64, float, int, List[int]]
):
    """
    usage.skimage: 11
    usage.xarray: 20
    usage.sklearn: 9
    usage.dask: 8
    """
    ...


def logical_not(
    _0: object, /, *, out: Union[dask.dataframe.core.DataFrame, numpy.ndarray] = ...
):
    """
    usage.skimage: 14
    usage.xarray: 10
    usage.sklearn: 8
    usage.dask: 31
    """
    ...


def isscalar(element: object):
    """
    usage.skimage: 67
    usage.xarray: 40
    usage.sklearn: 5
    usage.dask: 537
    """
    ...


def ceil(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    """
    usage.skimage: 31
    usage.xarray: 5
    usage.sklearn: 17
    usage.dask: 45
    """
    ...


def minimum(_0: object, _1: object, /, *, out: numpy.ndarray = ...):
    """
    usage.skimage: 9
    usage.xarray: 4
    usage.sklearn: 11
    usage.dask: 115
    """
    ...


def dot(_0: object, _1: object, /, *, out: numpy.ndarray = ...):
    """
    usage.skimage: 1
    usage.sklearn: 322
    usage.dask: 13
    """
    ...


def diag(v: Union[dask.array.core.Array, numpy.ndarray]):
    """
    usage.skimage: 5
    usage.sklearn: 28
    usage.dask: 8
    """
    ...


def arcsin(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    """
    usage.skimage: 1
    usage.xarray: 2
    usage.dask: 40
    """
    ...


def ellipkinc(_0: numpy.float64, _1: float, /):
    """
    usage.skimage: 1
    """
    ...


def ellipeinc(_0: numpy.float64, _1: float, /):
    """
    usage.skimage: 1
    """
    ...


def transpose(a: object):
    """
    usage.skimage: 21
    usage.xarray: 6
    usage.sklearn: 6
    usage.dask: 25
    """
    ...


def shape(a: Union[dask.array.core.Array, numpy.ma.core.MaskedArray, numpy.ndarray]):
    """
    usage.skimage: 1
    usage.xarray: 11
    usage.sklearn: 15
    usage.dask: 1
    """
    ...


def promote_types(_0: numpy.dtype, _1: Union[Type[float], numpy.dtype], /):
    """
    usage.skimage: 1
    usage.dask: 7
    """
    ...


def bincount(
    _0: Union[List[int], numpy.ndarray, dask.array.core.Array],
    /,
    *,
    minlength: int = ...,
    weights: Union[List[Union[int, float]], numpy.ndarray, None] = ...,
):
    """
    usage.skimage: 12
    usage.sklearn: 36
    usage.dask: 6
    """
    ...


def histogram(
    a: Union[list, dask.array.core.Array, numpy.ndarray],
    bins: Union[
        int,
        numpy.ndarray,
        numpy.int64,
        Tuple[
            numpy.float64, numpy.float64, numpy.float64, numpy.float64, numpy.float64
        ],
        List[Union[int, float]],
    ] = ...,
    density: bool = ...,
    range: Union[Tuple[int, int], None] = ...,
    weights: Union[numpy.ndarray, dask.array.core.Array, None] = ...,
):
    """
    usage.skimage: 7
    usage.dask: 11
    """
    ...


def interp(
    x: Union[numpy.ndarray, numpy.flatiter],
    xp: numpy.ndarray,
    fp: Union[
        numpy.ndarray, List[Union[pandas._libs.tslibs.nattype.NaTType, float, None]]
    ],
):
    """
    usage.skimage: 6
    usage.dask: 8
    """
    ...


def polyfit(x: numpy.ndarray, y: numpy.ndarray, deg: int):
    """
    usage.skimage: 1
    """
    ...


def pad(array: Union[numpy.ndarray, List[Union[List[int], int]]], pad_width: object):
    """
    usage.skimage: 126
    usage.xarray: 44
    usage.dask: 21
    """
    ...


def product(*args: Literal["v", "t"]):
    """
    usage.skimage: 14
    usage.sklearn: 1
    """
    ...


def apply_along_axis(
    func1d: Union[int, sklearn.gaussian_process.kernels.PairwiseKernel, Callable],
    axis: Union[Callable, int],
    arr: Union[int, numpy.ndarray],
    *args: Literal["v", "t"],
):
    """
    usage.skimage: 8
    usage.sklearn: 5
    usage.dask: 4
    """
    ...


def count_nonzero(a: Union[str, List[bool], numpy.ndarray]):
    """
    usage.skimage: 9
    usage.sklearn: 12
    usage.dask: 21
    """
    ...


def cumsum(
    a: object,
    axis: Union[None, int] = ...,
    out: Union[
        dask.array.core.Array, dask.dataframe.core.DataFrame, numpy.ndarray
    ] = ...,
    dtype: Type[numpy.float64] = ...,
):
    """
    usage.skimage: 29
    usage.xarray: 10
    usage.sklearn: 16
    usage.dask: 39
    """
    ...


def take_along_axis(arr: numpy.ndarray, indices: numpy.ndarray, axis: int):
    """
    usage.skimage: 1
    usage.dask: 3
    """
    ...


def square(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    """
    usage.skimage: 7
    usage.xarray: 2
    usage.dask: 42
    """
    ...


def mean(
    a: object,
    axis: Union[int, Tuple[Union[int, None], ...], None] = ...,
    out: Union[dask.dataframe.core.Scalar, dask.dataframe.core.Series] = ...,
    keepdims: bool = ...,
    dtype: Union[Literal["float32", "i8", "f8"], None, type] = ...,
):
    """
    usage.skimage: 61
    usage.xarray: 32
    usage.sklearn: 102
    usage.dask: 116
    """
    ...


def log2(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    """
    usage.skimage: 5
    usage.xarray: 2
    usage.sklearn: 9
    usage.dask: 37
    """
    ...


def allclose(
    a: object,
    b: object,
    rtol: Union[float, int] = ...,
    atol: float = ...,
    equal_nan: bool = ...,
):
    """
    usage.skimage: 33
    usage.xarray: 22
    usage.sklearn: 45
    usage.dask: 83
    """
    ...


def argsort(
    a: Union[
        numpy.ndarray,
        numpy.flatiter,
        numpy.matrix,
        Tuple[
            Union[float, numpy.float64],
            Union[float, numpy.float64],
            Union[float, numpy.float64],
            Union[float, numpy.float64],
            Union[float, numpy.float64],
        ],
    ]
):
    """
    usage.skimage: 28
    usage.sklearn: 34
    usage.dask: 12
    """
    ...


def hstack(tup: object):
    """
    usage.skimage: 27
    usage.xarray: 1
    usage.sklearn: 89
    usage.dask: 7
    """
    ...


def argmax(
    a: Union[
        numpy.ndarray,
        numpy.ma.core.MaskedArray,
        dask.array.core.Array,
        numpy.matrix,
        List[numpy.float64],
    ] = ...,
    axis: Union[None, int] = ...,
    out: dask.array.core.Array = ...,
    *,
    keepdims: bool = ...,
):
    """
    usage.skimage: 18
    usage.xarray: 11
    usage.sklearn: 44
    usage.dask: 36
    """
    ...


def logspace(
    start: Union[numpy.float64, int, float],
    stop: Union[numpy.float64, int, float],
    num: int,
):
    """
    usage.skimage: 2
    usage.sklearn: 11
    """
    ...


def logical_or(_0: object, _1: object, /, *, out: numpy.ndarray = ...):
    """
    usage.skimage: 3
    usage.xarray: 2
    usage.sklearn: 4
    usage.dask: 112
    """
    ...


def isinf(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    """
    usage.skimage: 2
    usage.xarray: 2
    usage.sklearn: 10
    usage.dask: 31
    """
    ...


def delete(arr: numpy.ndarray, obj: Union[numpy.ndarray, Tuple[Union[None, int], ...]]):
    """
    usage.skimage: 3
    usage.sklearn: 2
    """
    ...


def split(ary: numpy.ndarray, indices_or_sections: Union[numpy.ndarray, int]):
    """
    usage.skimage: 1
    usage.sklearn: 4
    """
    ...


def atleast_1d(*arys: Literal["v", "t"]):
    """
    usage.skimage: 11
    usage.xarray: 24
    usage.sklearn: 38
    usage.dask: 4
    """
    ...


def isclose(
    a: Union[numpy.float64, numpy.ndarray, float],
    b: Union[int, numpy.ndarray, float, numpy.float32, numpy.float64],
    rtol: float = ...,
    atol: Union[int, float] = ...,
    equal_nan: bool = ...,
):
    """
    usage.skimage: 3
    usage.xarray: 12
    usage.sklearn: 5
    usage.dask: 3
    """
    ...


def gradient(
    f: Union[float, int, numpy.ndarray, xarray.core.dataarray.DataArray],
    *varargs: Literal["v", "t"],
):
    """
    usage.skimage: 8
    usage.xarray: 5
    usage.dask: 14
    """
    ...


def argmin(
    a: Union[
        List[Union[float, numpy.float64, int]],
        numpy.ma.core.MaskedArray,
        numpy.ndarray,
        Tuple[
            numpy.float64, numpy.float64, numpy.float64, numpy.float64, numpy.float64
        ],
    ] = ...,
    axis: Union[None, int] = ...,
    *,
    keepdims: bool = ...,
):
    """
    usage.skimage: 10
    usage.xarray: 5
    usage.sklearn: 23
    usage.dask: 35
    """
    ...


def arctan(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    """
    usage.skimage: 3
    usage.xarray: 2
    usage.sklearn: 2
    usage.dask: 40
    """
    ...


def sort(
    a: Union[
        dask.array.core.Array, numpy.ndarray, List[Union[int, float, numpy.float64]]
    ]
):
    """
    usage.skimage: 14
    usage.xarray: 2
    usage.sklearn: 31
    usage.dask: 14
    """
    ...


def spacing(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    """
    usage.skimage: 1
    usage.dask: 37
    """
    ...


def isfinite(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    """
    usage.skimage: 7
    usage.xarray: 6
    usage.sklearn: 19
    usage.dask: 31
    """
    ...


def diff(
    a: Union[numpy.ndarray, List[Union[numpy.float64, numpy.int64]]],
    n: int = ...,
    axis: int = ...,
):
    """
    usage.skimage: 15
    usage.xarray: 11
    usage.sklearn: 17
    usage.dask: 11
    """
    ...


def flatnonzero(a: numpy.ndarray):
    """
    usage.skimage: 6
    usage.xarray: 2
    usage.sklearn: 24
    usage.dask: 2
    """
    ...


def copy(a: Union[numpy.ndarray, numpy.float64]):
    """
    usage.skimage: 14
    usage.sklearn: 23
    """
    ...


def atleast_2d(*arys: Literal["v", "t"]):
    """
    usage.skimage: 7
    usage.xarray: 2
    usage.sklearn: 25
    usage.dask: 3
    """
    ...


def rot90(m: numpy.ndarray):
    """
    usage.skimage: 7
    """
    ...


def roll(
    a: Union[numpy.ndarray, List[Union[int, float]]], shift: Union[int, Tuple[int, int]]
):
    """
    usage.skimage: 14
    usage.xarray: 1
    usage.dask: 5
    """
    ...


def indices(dimensions: Union[Tuple[Union[int, numpy.int64, None], ...], generator]):
    """
    usage.skimage: 6
    usage.sklearn: 2
    usage.dask: 8
    """
    ...


def tri(N: int, M: int = ..., k: int = ...):
    """
    usage.skimage: 9
    """
    ...


def less(_0: object, _1: object, /):
    """
    usage.skimage: 3
    usage.xarray: 1
    usage.sklearn: 5
    usage.dask: 109
    """
    ...


def prod(
    a: object,
    axis: Union[int, Tuple[Union[None, int], ...], None] = ...,
    out: Union[dask.dataframe.core.Scalar, dask.dataframe.core.Series] = ...,
    keepdims: bool = ...,
    dtype: Union[Literal["i8", "f8", "i4", "f4"], type] = ...,
):
    """
    usage.skimage: 9
    usage.xarray: 15
    usage.sklearn: 8
    usage.dask: 134
    """
    ...


def true_divide(_0: object, _1: object, /, *, out: numpy.ndarray = ...):
    """
    usage.skimage: 2
    usage.sklearn: 2
    usage.dask: 32
    """
    ...


def unravel_index(
    _0: Union[numpy.int64, numpy.ndarray, int],
    _1: Tuple[Union[int, None], ...] = ...,
    _2: Literal["F", "C"] = ...,
    /,
    *,
    order: Literal["F", "C"] = ...,
    shape: Tuple[int, ...] = ...,
):
    """
    usage.skimage: 18
    usage.sklearn: 1
    usage.dask: 12
    """
    ...


def apply_over_axes(
    func: Callable, a: numpy.ndarray, axes: Union[int, Tuple[Union[int, None], ...]]
):
    """
    usage.skimage: 10
    usage.dask: 5
    """
    ...


def tile(
    A: Union[
        list, numpy.ndarray, int, numpy.float64, Tuple[Union[numpy.ndarray, int], ...]
    ],
    reps: Union[int, Tuple[int, ...], List[int]],
):
    """
    usage.skimage: 15
    usage.xarray: 5
    usage.sklearn: 16
    usage.dask: 18
    """
    ...


def real(val: object):
    """
    usage.skimage: 8
    usage.xarray: 1
    usage.sklearn: 1
    usage.dask: 32
    """
    ...


def imag(val: object):
    """
    usage.skimage: 1
    usage.xarray: 1
    usage.dask: 31
    """
    ...


def sign(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    """
    usage.skimage: 4
    usage.xarray: 3
    usage.sklearn: 24
    usage.dask: 38
    """
    ...


def subtract(
    _0: Union[numpy.ndarray, numpy.float64, dask.array.core.Array, int],
    _1: Union[int, dask.array.core.Array, numpy.ndarray],
    /,
    *,
    dtype: numpy.dtype = ...,
):
    """
    usage.skimage: 11
    usage.xarray: 2
    usage.sklearn: 1
    usage.dask: 21
    """
    ...


def ix_(*args: Literal["v", "t"]):
    """
    usage.skimage: 2
    usage.xarray: 3
    usage.sklearn: 2
    """
    ...


def convolve(a: numpy.ndarray, v: List[float], mode: Literal["valid"]):
    """
    usage.skimage: 1
    """
    ...


def invert(_0: Union[numpy.ndarray, dask.array.core.Array, List[bool]], /):
    """
    usage.skimage: 7
    usage.dask: 8
    """
    ...


def array_equal(
    a1: Union[numpy.ndarray, Tuple[float, float, float], List[Union[float, int]]],
    a2: Union[
        numpy.ndarray,
        Tuple[int, ...],
        List[Union[numpy.float32, float, int, numpy.float64]],
    ],
):
    """
    usage.skimage: 5
    usage.xarray: 3
    usage.sklearn: 12
    usage.dask: 4
    """
    ...


def reciprocal(
    _0: object, /, *, out: Union[dask.dataframe.core.DataFrame, numpy.ndarray] = ...
):
    """
    usage.skimage: 1
    usage.dask: 37
    """
    ...


def insert(
    arr: numpy.ndarray,
    obj: Union[slice[int, int, int], int, List[int]],
    values: Union[numpy.ndarray, int],
):
    """
    usage.skimage: 3
    usage.sklearn: 1
    usage.dask: 11
    """
    ...


def full_like(
    a: object,
    fill_value: object,
    dtype: Union[type, Literal["i8", "f8", "i4", "f4"], numpy.dtype, None] = ...,
    shape: Tuple[int, ...] = ...,
):
    """
    usage.skimage: 1
    usage.xarray: 10
    usage.sklearn: 3
    usage.dask: 50
    """
    ...


def sctype2char(sctype: numpy.dtype):
    """
    usage.skimage: 2
    """
    ...


def floor_divide(
    _0: Union[dask.array.core.Array, int, numpy.ndarray],
    _1: Union[dask.array.core.Array, numpy.ndarray, int],
    /,
    *,
    out: numpy.ndarray = ...,
    dtype: numpy.dtype = ...,
    casting: Literal["unsafe"] = ...,
):
    """
    usage.skimage: 4
    usage.dask: 20
    """
    ...


def fromfile(_0: _io.TextIOWrapper, /, *, sep: Literal[" "]):
    """
    usage.skimage: 1
    """
    ...


def median(
    a: Union[Tuple[Union[numpy.int64, int], ...], numpy.ndarray],
    axis: Union[int, List[int], Tuple[int, ...]] = ...,
    keepdims: bool = ...,
):
    """
    usage.skimage: 5
    usage.xarray: 1
    usage.sklearn: 15
    usage.dask: 17
    """
    ...


def asfortranarray(a: Union[numpy.ndarray, List[List[int]]]):
    """
    usage.skimage: 1
    usage.sklearn: 20
    usage.dask: 2
    """
    ...


def cross(a: numpy.ndarray, b: numpy.ndarray):
    """
    usage.skimage: 5
    """
    ...


def einsum(*operands: Literal["v", "t"]):
    """
    usage.skimage: 1
    usage.xarray: 80
    usage.sklearn: 10
    usage.dask: 136
    """
    ...


def nan_to_num(x: object):
    """
    usage.skimage: 1
    usage.sklearn: 2
    usage.dask: 23
    """
    ...


def frombuffer(
    _0: Union[bytes, array.array, numpy.ndarray],
    /,
    *,
    dtype: Union[type, Literal["int8"]] = ...,
):
    """
    usage.skimage: 1
    usage.sklearn: 8
    usage.dask: 1
    """
    ...


def fliplr(m: numpy.ndarray):
    """
    usage.skimage: 5
    usage.dask: 1
    """
    ...


def tril(m: numpy.ndarray):
    """
    usage.skimage: 1
    usage.sklearn: 1
    usage.dask: 7
    """
    ...


def flip(m: object, axis: int):
    """
    usage.skimage: 3
    usage.dask: 5
    """
    ...


def flipud(m: numpy.ndarray):
    """
    usage.skimage: 2
    usage.xarray: 2
    usage.dask: 1
    """
    ...


def set_printoptions(
    precision: int = ...,
    edgeitems: int = ...,
    linewidth: int = ...,
    suppress: bool = ...,
    nanstr: Literal["nan"] = ...,
    infstr: Literal["inf"] = ...,
    formatter: None = ...,
    sign: Literal["-"] = ...,
    floatmode: Literal["maxprec"] = ...,
):
    """
    usage.skimage: 1
    usage.xarray: 3
    """
    ...


def result_type(
    _0: object,
    _1: object = ...,
    _2: Union[
        numpy.dtype, numpy.ndarray, dask.array.core.Array, type, Literal["f8"]
    ] = ...,
    _3: Union[numpy.dtype, dask.array.core.Array, numpy.ndarray] = ...,
    _4: Union[numpy.dtype, dask.array.core.Array, numpy.ndarray] = ...,
    _5: Union[numpy.dtype, numpy.ndarray, dask.array.core.Array] = ...,
    _6: Union[numpy.dtype, numpy.ndarray, dask.array.core.Array] = ...,
    _7: Union[numpy.dtype, numpy.ndarray, dask.array.core.Array] = ...,
    _8: Union[numpy.dtype, numpy.ndarray, dask.array.core.Array] = ...,
    _9: Union[numpy.dtype, numpy.ndarray, dask.array.core.Array] = ...,
    _10: Union[numpy.dtype, dask.array.core.Array, numpy.ndarray] = ...,
    _11: Union[numpy.dtype, dask.array.core.Array, numpy.ndarray] = ...,
    _12: Union[numpy.dtype, dask.array.core.Array, numpy.ndarray] = ...,
    _13: Union[numpy.dtype, dask.array.core.Array, numpy.ndarray] = ...,
    _14: Union[numpy.dtype, dask.array.core.Array, numpy.ndarray] = ...,
    _15: Union[numpy.dtype, dask.array.core.Array, numpy.ndarray] = ...,
    _16: Union[numpy.dtype, dask.array.core.Array, numpy.ndarray] = ...,
    _17: Union[numpy.dtype, dask.array.core.Array, numpy.ndarray] = ...,
    _18: Union[numpy.dtype, dask.array.core.Array, numpy.ndarray] = ...,
    _19: Union[numpy.dtype, dask.array.core.Array, numpy.ndarray] = ...,
    /,
):
    """
    usage.skimage: 7
    usage.xarray: 94
    usage.sklearn: 10
    usage.dask: 80
    """
    ...


def ptp(a: numpy.ndarray):
    """
    usage.skimage: 10
    usage.sklearn: 2
    usage.dask: 2
    """
    ...


def cumprod(
    a: Union[
        numpy.ndarray,
        numpy.ma.core.MaskedArray,
        dask.array.core.Array,
        dask.dataframe.core.DataFrame,
        Tuple[int, ...],
    ],
    axis: Union[None, int] = ...,
    out: Union[dask.dataframe.core.DataFrame, dask.array.core.Array] = ...,
):
    """
    usage.skimage: 5
    usage.xarray: 4
    usage.dask: 14
    """
    ...


def ravel_multi_index(
    _0: Union[
        Tuple[Union[int, numpy.ndarray, numpy.int64], ...], List[int], numpy.ndarray
    ],
    _1: Tuple[int, ...],
    /,
    *,
    order: Literal["F", "C"] = ...,
):
    """
    usage.skimage: 18
    usage.dask: 3
    """
    ...


def logical_xor(_0: object, _1: object, /, *, out: numpy.ndarray = ...):
    """
    usage.skimage: 1
    usage.xarray: 2
    usage.dask: 112
    """
    ...


def in1d(
    ar1: Union[numpy.ndarray, numpy.flatiter],
    ar2: Union[numpy.ndarray, Tuple[int, int], List[numpy.float64]],
):
    """
    usage.skimage: 2
    usage.sklearn: 13
    usage.dask: 1
    """
    ...


def take(
    a: Union[numpy.ndarray, List[Union[Literal["three", "two", "one"], int]]],
    indices: Union[List[int], int, numpy.ndarray],
):
    """
    usage.skimage: 1
    usage.xarray: 11
    usage.sklearn: 8
    usage.dask: 3
    """
    ...


def lexsort(_0: Tuple[Union[numpy.ndarray, xarray.core.dataarray.DataArray], ...], /):
    """
    usage.skimage: 1
    usage.xarray: 2
    """
    ...


def fmax(_0: object, _1: object, /):
    """
    usage.skimage: 3
    usage.xarray: 2
    usage.dask: 112
    """
    ...


def fix(x: Union[numpy.ndarray, numpy.float64, float, xarray.core.dataarray.DataArray]):
    """
    usage.skimage: 2
    usage.xarray: 1
    usage.dask: 3
    """
    ...


def tensordot(
    a: object,
    b: object,
    axes: Union[
        int,
        Tuple[
            Union[List[int], int, Tuple[Union[None, int], ...]],
            Union[List[int], int, Tuple[Union[None, int], ...]],
        ],
        List[int],
    ],
):
    """
    usage.skimage: 1
    usage.xarray: 5
    usage.dask: 23
    """
    ...


def atleast_3d(*arys: Literal["v", "t"]):
    """
    usage.skimage: 11
    usage.sklearn: 6
    usage.dask: 3
    """
    ...


def iscomplexobj(x: Union[dask.array.core.Array, numpy.ndarray]):
    """
    usage.skimage: 4
    usage.sklearn: 1
    usage.dask: 2
    """
    ...


def conjugate(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    """
    usage.skimage: 2
    usage.xarray: 2
    usage.sklearn: 1
    usage.dask: 45
    """
    ...


def angle(z: object):
    """
    usage.skimage: 3
    usage.xarray: 2
    usage.dask: 25
    """
    ...


def require(a: numpy.ndarray, requirements: Union[Literal["W"], List[Literal["C"]]]):
    """
    usage.skimage: 1
    usage.sklearn: 4
    """
    ...


def tanh(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    """
    usage.skimage: 2
    usage.xarray: 2
    usage.sklearn: 3
    usage.dask: 40
    """
    ...


def ndim(a: Union[numpy.float64, numpy.ndarray]):
    """
    usage.skimage: 4
    usage.sklearn: 4
    """
    ...


def searchsorted(a: Union[List[int], Tuple[int, ...], numpy.ndarray], v: object):
    """
    usage.skimage: 3
    usage.xarray: 1
    usage.sklearn: 38
    usage.dask: 16
    """
    ...


def fill_diagonal(a: numpy.ndarray, val: Union[float, int]):
    """
    usage.skimage: 1
    usage.sklearn: 10
    """
    ...


def array2string(a: numpy.ndarray, separator: Literal[", "]):
    """
    usage.skimage: 1
    """
    ...


def std(
    a: object,
    axis: Union[int, Tuple[Union[int, None], ...], None] = ...,
    out: Union[dask.dataframe.core.Scalar, dask.dataframe.core.Series] = ...,
    ddof: int = ...,
    keepdims: bool = ...,
):
    """
    usage.skimage: 1
    usage.xarray: 3
    usage.sklearn: 6
    usage.dask: 92
    """
    ...


def hamming(M: int):
    """
    usage.skimage: 1
    """
    ...


def hanning(M: int):
    """
    usage.skimage: 1
    """
    ...


def around(a: Union[numpy.ndarray, Tuple[numpy.float64, numpy.float64]]):
    """
    usage.skimage: 1
    usage.xarray: 4
    usage.dask: 1
    """
    ...


def alltrue(*args: Literal["v", "t"]):
    """
    usage.skimage: 2
    usage.dask: 1
    """
    ...


def may_share_memory(
    _0: Union[
        scipy.sparse.csc.csc_matrix,
        scipy.sparse.lil.lil_matrix,
        scipy.sparse.csr.csr_matrix,
        numpy.ndarray,
    ],
    _1: object,
    /,
):
    """
    usage.skimage: 2
    usage.sklearn: 44
    """
    ...


def isnat(_0: Union[numpy.ndarray, dask.array.core.Array], /):
    """
    usage.xarray: 6
    """
    ...


def get_printoptions():
    """
    usage.xarray: 3
    """
    ...


def broadcast_arrays(*args: Literal["v", "t"]):
    """
    usage.xarray: 3
    usage.dask: 10
    """
    ...


def broadcast_to(
    array: Union[numpy.ndarray, int, numpy.float64, float],
    shape: Union[List[int], Tuple[Union[int, numpy.int64, None], ...]],
):
    """
    usage.xarray: 25
    usage.dask: 23
    """
    ...


def nanmean(
    a: numpy.ndarray,
    axis: Union[int, Tuple[Union[int, None], ...], None] = ...,
    keepdims: bool = ...,
    dtype: Union[None, type] = ...,
):
    """
    usage.xarray: 21
    usage.sklearn: 3
    usage.dask: 11
    """
    ...


def nanstd(
    a: numpy.ndarray,
    axis: Union[int, Tuple[Union[int, None], ...], None] = ...,
    keepdims: bool = ...,
    dtype: None = ...,
    ddof: int = ...,
):
    """
    usage.xarray: 3
    usage.sklearn: 1
    usage.dask: 49
    """
    ...


def nanargmax(
    _0: numpy.ndarray = ...,
    _1: Union[None, int] = ...,
    /,
    a: numpy.ndarray = ...,
    axis: Union[None, int] = ...,
    *,
    keepdims: bool = ...,
):
    """
    usage.xarray: 5
    usage.dask: 28
    """
    ...


def nanargmin(
    _0: numpy.ndarray = ...,
    _1: Union[None, int] = ...,
    /,
    a: numpy.ndarray = ...,
    axis: Union[None, int] = ...,
    *,
    keepdims: bool = ...,
):
    """
    usage.xarray: 4
    usage.dask: 28
    """
    ...


def expand_dims(a: numpy.ndarray, axis: int):
    """
    usage.xarray: 5
    usage.sklearn: 2
    usage.dask: 2
    """
    ...


def nanquantile(
    a: numpy.ndarray,
    q: numpy.ndarray,
    axis: numpy.ndarray,
    interpolation: Literal["linear"],
):
    """
    usage.xarray: 2
    """
    ...


def nanpercentile(
    a: numpy.ndarray, q: Union[Tuple[float, float], numpy.float64, numpy.ndarray]
):
    """
    usage.xarray: 20
    usage.sklearn: 1
    """
    ...


def quantile(
    a: numpy.ndarray,
    q: numpy.ndarray,
    axis: numpy.ndarray,
    interpolation: Literal["linear"],
):
    """
    usage.xarray: 1
    """
    ...


def repeat(
    a: Union[numpy.ndarray, numpy.float64, float, int, numpy.int64],
    repeats: Union[int, numpy.ndarray, numpy.int64],
):
    """
    usage.xarray: 4
    usage.sklearn: 33
    usage.dask: 4
    """
    ...


def isin(
    element: Union[numpy.ndarray, dask.array.core.Array],
    test_elements: Union[dask.array.core.Array, numpy.ndarray, List[int]],
):
    """
    usage.xarray: 5
    usage.dask: 4
    """
    ...


def nansum(
    a: Union[numpy.ndarray, numpy.ma.core.MaskedArray],
    axis: Union[int, Tuple[Union[int, None], ...], None] = ...,
    dtype: Union[numpy.dtype, Literal["i8", "f8"]] = ...,
    keepdims: bool = ...,
):
    """
    usage.xarray: 8
    usage.sklearn: 3
    usage.dask: 135
    """
    ...


def nanmax(
    a: numpy.ndarray = ...,
    axis: Union[None, int, Tuple[Union[int, None], ...]] = ...,
    keepdims: bool = ...,
    *,
    computing_meta: bool = ...,
):
    """
    usage.xarray: 17
    usage.sklearn: 1
    usage.dask: 106
    """
    ...


def nanmin(
    a: numpy.ndarray = ...,
    axis: Union[None, int, Tuple[Union[None, int], ...]] = ...,
    keepdims: bool = ...,
    *,
    computing_meta: bool = ...,
):
    """
    usage.xarray: 16
    usage.sklearn: 2
    usage.dask: 106
    """
    ...


def nancumsum(a: numpy.ndarray, axis: Union[int, None] = ..., dtype: None = ...):
    """
    usage.xarray: 1
    usage.dask: 16
    """
    ...


def nancumprod(a: numpy.ndarray, axis: Union[int, None] = ..., dtype: None = ...):
    """
    usage.xarray: 1
    usage.dask: 16
    """
    ...


def var(
    a: object,
    axis: Union[int, Tuple[Union[None, int], ...], None] = ...,
    out: Union[dask.dataframe.core.Scalar, dask.dataframe.core.Series] = ...,
    ddof: int = ...,
    keepdims: bool = ...,
):
    """
    usage.xarray: 22
    usage.sklearn: 22
    usage.dask: 96
    """
    ...


def nanvar(
    a: numpy.ndarray,
    axis: Union[int, Tuple[Union[int, None], ...], None] = ...,
    keepdims: bool = ...,
    dtype: Union[Type[float], None] = ...,
    ddof: int = ...,
):
    """
    usage.xarray: 17
    usage.sklearn: 3
    usage.dask: 49
    """
    ...


def nanmedian(a: numpy.ndarray, axis: Union[int, List[int], None]):
    """
    usage.xarray: 3
    usage.sklearn: 1
    usage.dask: 8
    """
    ...


def datetime_data(_0: numpy.dtype, /):
    """
    usage.xarray: 1
    """
    ...


def trapz(
    y: Union[numpy.ndarray, dask.array.core.Array, xarray.core.dataarray.DataArray],
    x: Union[numpy.ndarray, xarray.core.dataarray.DataArray],
):
    """
    usage.xarray: 4
    usage.sklearn: 1
    """
    ...


def nanprod(
    a: numpy.ndarray,
    axis: Union[int, Tuple[Union[int, None], ...], None] = ...,
    dtype: Union[Literal["i8", "f8"], None] = ...,
    out: None = ...,
    keepdims: bool = ...,
):
    """
    usage.xarray: 9
    usage.dask: 71
    """
    ...


def greater(_0: object, _1: object, /):
    """
    usage.xarray: 1
    usage.dask: 109
    """
    ...


def frexp(_0: object, /):
    """
    usage.xarray: 7
    usage.dask: 9
    """
    ...


def arccos(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    """
    usage.xarray: 2
    usage.dask: 40
    """
    ...


def arccosh(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    """
    usage.xarray: 2
    usage.dask: 38
    """
    ...


def arcsinh(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    """
    usage.xarray: 2
    usage.dask: 38
    """
    ...


def arctanh(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    """
    usage.xarray: 2
    usage.dask: 40
    """
    ...


def copysign(_0: object, _1: object, /):
    """
    usage.xarray: 2
    usage.dask: 112
    """
    ...


def cosh(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    """
    usage.xarray: 2
    usage.dask: 38
    """
    ...


def degrees(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    """
    usage.xarray: 2
    usage.dask: 38
    """
    ...


def expm1(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    """
    usage.xarray: 2
    usage.dask: 41
    """
    ...


def fabs(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    """
    usage.xarray: 2
    usage.sklearn: 1
    usage.dask: 39
    """
    ...


def greater_equal(_0: object, _1: object, /):
    """
    usage.xarray: 1
    usage.dask: 111
    """
    ...


def fmin(_0: object, _1: object, /):
    """
    usage.xarray: 2
    usage.dask: 112
    """
    ...


def fmod(_0: object, _1: object, /):
    """
    usage.xarray: 2
    usage.dask: 112
    """
    ...


def iscomplex(x: object):
    """
    usage.xarray: 1
    usage.dask: 28
    """
    ...


def isreal(x: object):
    """
    usage.xarray: 1
    usage.sklearn: 1
    usage.dask: 28
    """
    ...


def ldexp(_0: object, _1: object, /):
    """
    usage.xarray: 2
    usage.dask: 88
    """
    ...


def log1p(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    """
    usage.xarray: 2
    usage.sklearn: 1
    usage.dask: 40
    """
    ...


def logaddexp(_0: object, _1: object, /):
    """
    usage.xarray: 2
    usage.sklearn: 7
    usage.dask: 112
    """
    ...


def logaddexp2(_0: object, _1: object, /):
    """
    usage.xarray: 2
    usage.dask: 112
    """
    ...


def nextafter(_0: object, _1: object, /):
    """
    usage.xarray: 2
    usage.sklearn: 2
    usage.dask: 112
    """
    ...


def radians(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    """
    usage.xarray: 2
    usage.dask: 40
    """
    ...


def signbit(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    """
    usage.xarray: 2
    usage.dask: 31
    """
    ...


def sinh(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    """
    usage.xarray: 2
    usage.dask: 40
    """
    ...


def tan(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    """
    usage.xarray: 2
    usage.dask: 40
    """
    ...


def trunc(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    """
    usage.xarray: 2
    usage.dask: 40
    """
    ...


def outer(
    a: Union[numpy.ndarray, numpy.float64], b: Union[numpy.ndarray, numpy.float64]
):
    """
    usage.sklearn: 6
    usage.dask: 4
    """
    ...


def compress(condition: Union[numpy.ndarray, List[bool]], a: numpy.ndarray):
    """
    usage.sklearn: 4
    usage.dask: 4
    """
    ...


def size(a: Union[Tuple[Union[int, None], ...], numpy.ndarray]):
    """
    usage.sklearn: 18
    """
    ...


def diag_indices_from(arr: numpy.ndarray):
    """
    usage.sklearn: 3
    """
    ...


def triu_indices(n: int, k: int):
    """
    usage.sklearn: 2
    """
    ...


def append(arr: numpy.ndarray, values: Union[float, numpy.ndarray]):
    """
    usage.sklearn: 15
    usage.dask: 1
    """
    ...


def argpartition(a: numpy.ndarray, kth: Union[int, numpy.int64], axis: int):
    """
    usage.sklearn: 3
    usage.dask: 1
    """
    ...


def array_equiv(a1: numpy.ndarray, a2: numpy.ndarray):
    """
    usage.sklearn: 1
    """
    ...


def array_split(ary: numpy.ndarray, indices_or_sections: int):
    """
    usage.sklearn: 1
    """
    ...


def setdiff1d(ar1: numpy.ndarray, ar2: numpy.ndarray):
    """
    usage.sklearn: 10
    """
    ...


def average(
    a: Union[numpy.ndarray, List[int]],
    axis: int = ...,
    weights: Union[
        numpy.ndarray, None, List[Union[numpy.float64, numpy.int64, float, int]]
    ] = ...,
):
    """
    usage.sklearn: 69
    usage.dask: 2
    """
    ...


def cov(m: object):
    """
    usage.sklearn: 4
    usage.dask: 11
    """
    ...


def trace(a: numpy.ndarray):
    """
    usage.sklearn: 4
    """
    ...


def union1d(
    ar1: Union[dask.array.core.Array, numpy.ndarray],
    ar2: Union[dask.array.core.Array, numpy.ndarray],
):
    """
    usage.sklearn: 5
    usage.dask: 2
    """
    ...


def matmul(_0: object, _1: object, /):
    """
    usage.sklearn: 1
    usage.dask: 12
    """
    ...


def fromiter(
    _0: Union[generator, itertools.chain],
    /,
    *,
    dtype: Union[Type[numpy.float64], Literal["float64"]],
    count: int = ...,
):
    """
    usage.sklearn: 3
    """
    ...


def unpackbits(_0: numpy.ndarray, /):
    """
    usage.sklearn: 1
    """
    ...


def resize(a: numpy.ndarray, new_shape: Union[Tuple[int, int], int]):
    """
    usage.sklearn: 6
    """
    ...


def identity(n: int):
    """
    usage.sklearn: 1
    """
    ...


def find_common_type(array_types: List[numpy.dtype], scalar_types: list):
    """
    usage.sklearn: 2
    """
    ...


def gammaln(_0: Union[float, numpy.ndarray], /):
    """
    usage.sklearn: 5
    """
    ...


def psi(_0: Union[int, numpy.int64, numpy.float64, numpy.ndarray], /):
    """
    usage.sklearn: 9
    """
    ...


def expit(_0: Union[numpy.ndarray, numpy.float64], /, *, out: numpy.ndarray = ...):
    """
    usage.sklearn: 13
    """
    ...


def ediff1d(ary: numpy.ndarray, to_begin: Union[List[int], None, int, float]):
    """
    usage.sklearn: 1
    usage.dask: 4
    """
    ...


def digitize(x: Union[List[int], numpy.ndarray], bins: numpy.ndarray):
    """
    usage.sklearn: 1
    usage.dask: 8
    """
    ...


def fdtrc(_0: int, _1: Union[int, numpy.int64], _2: numpy.ndarray, /):
    """
    usage.sklearn: 1
    usage.dask: 2
    """
    ...


def corrcoef(x: numpy.ndarray):
    """
    usage.sklearn: 3
    usage.dask: 5
    """
    ...


def xlogy(_0: numpy.ndarray, _1: numpy.ndarray, /):
    """
    usage.sklearn: 1
    usage.dask: 2
    """
    ...


def chdtrc(_0: int, _1: numpy.ndarray, /):
    """
    usage.sklearn: 1
    """
    ...


def asmatrix(data: numpy.ndarray):
    """
    usage.sklearn: 2
    usage.dask: 1
    """
    ...


def iterable(y: object):
    """
    usage.sklearn: 9
    usage.dask: 8
    """
    ...


def erf(_0: numpy.ndarray, /):
    """
    usage.sklearn: 1
    """
    ...


def inner(_0: numpy.ndarray, _1: numpy.ndarray, /):
    """
    usage.sklearn: 4
    """
    ...


def gamma(_0: float, /):
    """
    usage.sklearn: 1
    """
    ...


def kv(_0: float, _1: numpy.ndarray, /):
    """
    usage.sklearn: 1
    """
    ...


def equal(_0: object, _1: object, /):
    """
    usage.sklearn: 9
    usage.dask: 113
    """
    ...


def vander(x: numpy.ndarray, N: int):
    """
    usage.sklearn: 1
    """
    ...


def not_equal(_0: object, _1: object, /):
    """
    usage.sklearn: 1
    usage.dask: 109
    """
    ...


def isposinf(x: Union[numpy.ndarray, float, int]):
    """
    usage.sklearn: 2
    usage.dask: 1
    """
    ...


def inv(
    _0: Union[dask.array.core.Array, numpy.ndarray],
    /,
    *,
    output_dtypes: Type[float] = ...,
):
    """
    usage.dask: 3
    """
    ...


def eig(
    _0: Union[dask.array.core.Array, numpy.ndarray],
    /,
    *,
    output_dtypes: Tuple[Type[float], Type[float]] = ...,
):
    """
    usage.dask: 3
    """
    ...


def block(
    arrays: Union[
        List[
            Union[
                List[Union[numpy.ndarray, dask.array.core.Array, List[numpy.ndarray]]],
                numpy.ndarray,
                dask.array.core.Array,
            ]
        ],
        int,
        numpy.ndarray,
    ]
):
    """
    usage.dask: 18
    """
    ...


def modf(_0: Union[dask.array.core.Array, numpy.ndarray], /):
    """
    usage.dask: 9
    """
    ...


def save(
    file: Literal["/var/folders/xn/05ktz3056kqd9n8frgd6236h0000gn/T/t"],
    arr: Union[numpy.ndarray, numpy.memmap],
):
    """
    usage.dask: 6
    """
    ...


def diagonal(
    a: Union[numpy.ndarray, dask.array.core.Array],
    offset: int = ...,
    axis1: int = ...,
    axis2: int = ...,
):
    """
    usage.dask: 23
    """
    ...


def fromfunction(function: Callable, shape: Tuple[int, int]):
    """
    usage.dask: 2
    """
    ...


def g(
    _0: Union[numpy.ndarray, dask.array.core.Array],
    _1: Union[numpy.ndarray, dask.array.core.Array],
    /,
    *,
    axis: int = ...,
):
    """
    usage.dask: 3
    """
    ...


def mysum(
    _0: Union[numpy.ndarray, dask.array.core.Array],
    /,
    *,
    allow_rechunk: bool = ...,
    axis: int = ...,
    keepdims: bool = ...,
):
    """
    usage.dask: 3
    """
    ...


def partition(a: numpy.ndarray, kth: int, axis: int):
    """
    usage.dask: 1
    """
    ...


def vdot(_0: numpy.ndarray, _1: numpy.ndarray, /):
    """
    usage.dask: 2
    """
    ...


def extract(condition: numpy.ndarray, arr: numpy.ndarray):
    """
    usage.dask: 1
    """
    ...


def piecewise(
    x: Union[int, numpy.ndarray],
    condlist: Union[numpy.ndarray, List[numpy.ndarray]],
    funclist: List[Union[Callable, int, numpy.ndarray]],
    *args: Literal["v", "t"],
):
    """
    usage.dask: 6
    """
    ...


def argwhere(a: numpy.ndarray):
    """
    usage.dask: 3
    """
    ...


def einsum_path(*operands: Literal["v", "t"]):
    """
    usage.dask: 2
    """
    ...


def exp2(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    """
    usage.dask: 37
    """
    ...


def negative(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    """
    usage.dask: 40
    """
    ...


def bitwise_and(
    _0: Union[int, dask.array.core.Array, numpy.ndarray],
    _1: Union[numpy.ndarray, dask.array.core.Array, int],
    /,
):
    """
    usage.dask: 18
    """
    ...


def bitwise_or(
    _0: Union[int, dask.array.core.Array, numpy.ndarray],
    _1: Union[numpy.ndarray, dask.array.core.Array, int],
    /,
):
    """
    usage.dask: 18
    """
    ...


def bitwise_xor(
    _0: Union[int, dask.array.core.Array, numpy.ndarray],
    _1: Union[numpy.ndarray, dask.array.core.Array, int],
    /,
):
    """
    usage.dask: 18
    """
    ...


def less_equal(_0: object, _1: object, /):
    """
    usage.dask: 109
    """
    ...


def remainder(
    _0: Union[numpy.ndarray, int, dask.array.core.Array],
    _1: Union[int, numpy.ndarray, dask.array.core.Array],
    /,
    *,
    out: numpy.ndarray = ...,
):
    """
    usage.dask: 23
    """
    ...


def float_power(
    _0: Union[int, dask.array.core.Array, numpy.ndarray],
    _1: Union[numpy.ndarray, dask.array.core.Array, int],
    /,
):
    """
    usage.dask: 18
    """
    ...


def isneginf(x: numpy.ndarray):
    """
    usage.dask: 1
    """
    ...


def i0(
    x: Union[
        dask.dataframe.core.DataFrame,
        dask.dataframe.core.Series,
        numpy.ndarray,
        pandas.core.series.Series,
        pandas.core.frame.DataFrame,
    ]
):
    """
    usage.dask: 17
    """
    ...


def sinc(
    x: Union[
        dask.dataframe.core.DataFrame,
        dask.dataframe.core.Series,
        numpy.ndarray,
        pandas.core.series.Series,
        pandas.core.frame.DataFrame,
    ]
):
    """
    usage.dask: 17
    """
    ...


def frompyfunc(_0: Callable, _1: int, _2: int, /):
    """
    usage.dask: 4
    """
    ...


def divmod(
    _0: Union[numpy.ndarray, dask.array.core.Array],
    _1: Union[numpy.ndarray, float, dask.array.core.Array],
    /,
):
    """
    usage.dask: 4
    """
    ...


class ndarray:

    # usage.sklearn: 1
    # usage.dask: 5
    __name__: ClassVar[object]

    # usage.dask: 8
    __module__: ClassVar[object]

    @classmethod
    def mean(_0: numpy.ndarray, /):
        """
        usage.sample_usage: 1
        usage.skimage: 23
        usage.xarray: 1
        usage.sklearn: 62
        usage.dask: 2
        """
        ...

    @classmethod
    def sum(_0: numpy.ndarray, /):
        """
        usage.sample_usage: 1
        usage.skimage: 86
        usage.xarray: 10
        usage.sklearn: 147
        usage.dask: 34
        """
        ...

    @classmethod
    def sort(_0: numpy.ndarray, /):
        """
        usage.sample_usage: 1
        usage.sklearn: 1
        usage.dask: 3
        """
        ...

    @classmethod
    def reshape(
        _0: Union[numpy.matrix, numpy.ndarray],
        _1: Union[
            Tuple[Union[numpy.int64, int, None], ...], int, numpy.ndarray, List[int]
        ],
        _2: int = ...,
        _3: int = ...,
        _4: int = ...,
        /,
    ):
        """
        usage.sample_usage: 2
        usage.skimage: 168
        usage.xarray: 190
        usage.sklearn: 163
        usage.dask: 177
        """
        ...

    @classmethod
    def astype(
        _0: Union[numpy.ma.core.MaskedArray, numpy.ndarray],
        _1: Union[type, numpy.dtype, str],
        /,
    ):
        """
        usage.sample_usage: 1
        usage.skimage: 555
        usage.xarray: 75
        usage.sklearn: 149
        usage.dask: 160
        """
        ...

    @classmethod
    def copy(_0: Union[numpy.ndarray, numpy.matrix, numpy.memmap], /):
        """
        usage.skimage: 135
        usage.xarray: 14
        usage.sklearn: 129
        usage.dask: 7
        """
        ...

    @classmethod
    def max(_0: numpy.ndarray, /):
        """
        usage.skimage: 108
        usage.xarray: 15
        usage.sklearn: 31
        usage.dask: 7
        """
        ...

    @classmethod
    def ptp(_0: numpy.ndarray, /):
        """
        usage.skimage: 5
        """
        ...

    @classmethod
    def min(_0: numpy.ndarray, /):
        """
        usage.skimage: 80
        usage.xarray: 16
        usage.sklearn: 29
        usage.dask: 5
        """
        ...

    @classmethod
    def any(_0: numpy.ndarray, /):
        """
        usage.skimage: 11
        usage.xarray: 6
        usage.sklearn: 13
        usage.dask: 13
        """
        ...

    @classmethod
    def nonzero(_0: Union[numpy.ndarray, numpy.matrix], /):
        """
        usage.skimage: 4
        usage.xarray: 4
        usage.sklearn: 5
        usage.dask: 1
        """
        ...

    @classmethod
    def fill(_0: numpy.ndarray, _1: Union[int, bool, float, numpy.float64], /):
        """
        usage.skimage: 5
        usage.sklearn: 26
        """
        ...

    @classmethod
    def flatten(_0: numpy.ndarray, /):
        """
        usage.skimage: 16
        usage.xarray: 5
        usage.sklearn: 7
        usage.dask: 6
        """
        ...

    @classmethod
    def ravel(_0: numpy.ndarray, /):
        """
        usage.skimage: 207
        usage.xarray: 40
        usage.sklearn: 142
        usage.dask: 12
        """
        ...

    @classmethod
    def cumsum(_0: numpy.ndarray, /):
        """
        usage.skimage: 1
        usage.sklearn: 3
        usage.dask: 3
        """
        ...

    @classmethod
    def transpose(
        _0: numpy.ndarray,
        _1: Union[List[int], int, range, Tuple[int, ...]] = ...,
        _2: int = ...,
        _3: int = ...,
        /,
    ):
        """
        usage.skimage: 5
        usage.xarray: 13
        usage.sklearn: 8
        usage.dask: 10
        """
        ...

    @classmethod
    def argmin(_0: numpy.ndarray, /):
        """
        usage.skimage: 2
        usage.sklearn: 3
        """
        ...

    @classmethod
    def view(_0: numpy.ndarray, /):
        """
        usage.skimage: 22
        usage.xarray: 11
        usage.sklearn: 4
        usage.dask: 35
        """
        ...

    @classmethod
    def swapaxes(_0: numpy.ndarray, _1: int, _2: int, /):
        """
        usage.skimage: 2
        usage.sklearn: 1
        usage.dask: 5
        """
        ...

    @classmethod
    def argsort(_0: numpy.ndarray, /):
        """
        usage.skimage: 5
        usage.sklearn: 7
        """
        ...

    @classmethod
    def argmax(_0: numpy.ndarray, /):
        """
        usage.skimage: 6
        usage.sklearn: 5
        """
        ...

    @classmethod
    def std(_0: numpy.ndarray, /):
        """
        usage.skimage: 63
        usage.xarray: 2
        usage.sklearn: 8
        usage.dask: 3
        """
        ...

    @classmethod
    def all(_0: numpy.ndarray, /):
        """
        usage.skimage: 1
        usage.xarray: 9
        usage.sklearn: 5
        usage.dask: 4
        """
        ...

    @classmethod
    def tobytes(_0: numpy.ndarray, /):
        """
        usage.skimage: 2
        """
        ...

    @classmethod
    def tolist(_0: Union[numpy.ndarray, numpy.memmap], /):
        """
        usage.skimage: 1
        usage.xarray: 17
        usage.sklearn: 23
        usage.dask: 32
        """
        ...

    @classmethod
    def dot(_0: numpy.ndarray, _1: Union[dask.array.core.Array, numpy.ndarray], /):
        """
        usage.skimage: 1
        usage.sklearn: 50
        usage.dask: 9
        """
        ...

    @classmethod
    def conj(_0: numpy.ndarray, /):
        """
        usage.skimage: 4
        usage.dask: 2
        """
        ...

    @classmethod
    def __ne__(_0: Type[numpy.ndarray], /):
        """
        usage.skimage: 2
        """
        ...

    @classmethod
    def item(_0: numpy.ndarray, /):
        """
        usage.xarray: 18
        usage.dask: 21
        """
        ...

    @classmethod
    def squeeze(_0: numpy.ndarray, /):
        """
        usage.xarray: 3
        usage.sklearn: 14
        """
        ...

    @classmethod
    def clip(
        _0: numpy.ndarray,
        _1: int,
        _2: Union[int, float] = ...,
        _3: numpy.ndarray = ...,
        /,
    ):
        """
        usage.xarray: 1
        usage.sklearn: 2
        usage.dask: 3
        """
        ...

    @classmethod
    def __rmod__(_0: Literal["Expected sequence or array-like, got %s"], /):
        """
        usage.sklearn: 1
        """
        ...

    @classmethod
    def take(_0: numpy.ndarray, _1: numpy.ndarray, /):
        """
        usage.sklearn: 8
        usage.dask: 1
        """
        ...

    @classmethod
    def tostring(_0: numpy.ndarray, /):
        """
        usage.sklearn: 1
        """
        ...

    @classmethod
    def repeat(_0: numpy.ndarray, _1: Union[int, numpy.ndarray], /):
        """
        usage.sklearn: 1
        usage.dask: 1
        """
        ...

    @classmethod
    def var(_0: numpy.ndarray, /):
        """
        usage.sklearn: 1
        """
        ...

    @classmethod
    def searchsorted(_0: numpy.ndarray, _1: numpy.int64, /):
        """
        usage.sklearn: 1
        """
        ...

    @classmethod
    def round(_0: numpy.ndarray, /):
        """
        usage.sklearn: 2
        usage.dask: 2
        """
        ...

    @classmethod
    def __array_wrap__(_0: numpy.ndarray, _1: numpy.ndarray, /):
        """
        usage.dask: 2
        """
        ...

    @classmethod
    def cumprod(_0: numpy.ndarray, /):
        """
        usage.dask: 1
        """
        ...

    @classmethod
    def __array_function__(
        _0: numpy.ndarray,
        _1: Callable,
        _2: Tuple[Union[Type[numpy.ndarray], None], ...],
        _3: Tuple[Union[numpy.ndarray, numpy.int64, list], ...],
        _4: Dict[
            str,
            Union[
                Type[numpy.float64],
                int,
                bool,
                numpy.dtype,
                Tuple[Union[int, Tuple[int]], ...],
            ],
        ],
        /,
    ):
        """
        usage.dask: 30
        """
        ...

    @classmethod
    def prod(_0: numpy.ndarray, /):
        """
        usage.dask: 4
        """
        ...

    @classmethod
    def choose(_0: numpy.ndarray, _1: List[Union[int, numpy.ndarray]], /):
        """
        usage.dask: 2
        """
        ...

    # usage.sample_usage: 2
    # usage.skimage: 1335
    # usage.xarray: 333
    # usage.sklearn: 1717
    # usage.dask: 434
    shape: Union[numpy.ndarray, Tuple[int, ...], List[int]]

    # usage.sample_usage: 1
    # usage.skimage: 513
    # usage.xarray: 263
    # usage.sklearn: 261
    # usage.dask: 356
    ndim: object

    # usage.sample_usage: 1
    # usage.skimage: 636
    # usage.xarray: 726
    # usage.sklearn: 508
    # usage.dask: 444
    dtype: object

    # usage.sample_usage: 1
    # usage.skimage: 106
    # usage.xarray: 48
    # usage.sklearn: 128
    # usage.dask: 12
    size: object

    # usage.sample_usage: 1
    # usage.skimage: 87
    # usage.xarray: 34
    # usage.sklearn: 435
    # usage.dask: 28
    T: object

    # usage.skimage: 15
    # usage.xarray: 9
    # usage.sklearn: 15
    flags: object

    # usage.skimage: 20
    # usage.xarray: 43
    # usage.sklearn: 43
    # usage.dask: 7
    flat: numpy.ndarray

    # usage.skimage: 4
    itemsize: object

    # usage.skimage: 12
    # usage.xarray: 4
    # usage.sklearn: 7
    # usage.dask: 24
    strides: Tuple[int, int, int]

    # usage.xarray: 4
    coords: object

    # usage.xarray: 3
    variables: object

    # usage.xarray: 3
    variable: object

    # usage.xarray: 8
    base: object

    # usage.xarray: 2
    # usage.dask: 1
    real: object

    # usage.xarray: 2
    # usage.dask: 1
    imag: object

    # usage.xarray: 2
    dims: object

    # usage.xarray: 1
    attrs: object

    # usage.sklearn: 1
    columns: object

    # usage.sklearn: 13
    # usage.dask: 29
    __class__: object

    # usage.sklearn: 2
    # usage.dask: 9
    nbytes: object

    # usage.dask: 4
    __array_priority__: object

    # usage.dask: 2
    keys: object

    def __pos__(self: object, /):
        """
        usage.sample_usage: 1
        usage.dask: 1
        """
        ...

    def __neg__(self: object, /):
        """
        usage.sample_usage: 1
        usage.skimage: 42
        usage.xarray: 21
        usage.sklearn: 78
        usage.dask: 7
        """
        ...

    def __invert__(self: object, /):
        """
        usage.sample_usage: 1
        usage.skimage: 26
        usage.xarray: 7
        usage.sklearn: 63
        usage.dask: 9
        """
        ...

    def __bool__(self: object, /):
        """
        usage.sample_usage: 1
        """
        ...

    def __iter__(self: object, /):
        """
        usage.sample_usage: 2
        usage.skimage: 149
        usage.xarray: 83
        usage.sklearn: 104
        usage.dask: 6
        """
        ...

    def __getitem__(self: object, _0: object, /):
        """
        usage.sample_usage: 5
        usage.skimage: 2171
        usage.xarray: 747
        usage.sklearn: 2575
        usage.dask: 1145
        """
        ...

    def __pow__(self: object, _0: Union[numpy.ndarray, int, numpy.float64, float], /):
        """
        usage.sample_usage: 1
        usage.skimage: 173
        usage.xarray: 11
        usage.sklearn: 176
        usage.dask: 12
        """
        ...

    def __rpow__(self: object, _0: Union[int, numpy.ndarray, float], /):
        """
        usage.sample_usage: 2
        usage.skimage: 3
        usage.sklearn: 2
        usage.dask: 3
        """
        ...

    def __mul__(self: object, _0: object, /):
        """
        usage.sample_usage: 1
        usage.skimage: 402
        usage.xarray: 41
        usage.sklearn: 319
        usage.dask: 66
        """
        ...

    def __rmul__(self: object, _0: object, /):
        """
        usage.sample_usage: 2
        usage.skimage: 574
        usage.xarray: 56
        usage.sklearn: 545
        usage.dask: 73
        """
        ...

    def __matmul__(
        self: object,
        _0: Union[
            numpy.ndarray,
            scipy.sparse.csc.csc_matrix,
            scipy.sparse.csr.csr_matrix,
            numpy.matrix,
        ],
        /,
    ):
        """
        usage.sample_usage: 1
        usage.skimage: 50
        usage.sklearn: 11
        """
        ...

    def __rmatmul__(self: object, _0: object, /):
        """
        usage.sample_usage: 1
        usage.skimage: 52
        usage.sklearn: 15
        """
        ...

    def __floordiv__(
        self: object,
        _0: Union[int, numpy.ndarray, float, numpy.float64, List[Union[float, int]]],
        /,
    ):
        """
        usage.sample_usage: 1
        usage.skimage: 14
        usage.xarray: 1
        usage.sklearn: 12
        usage.dask: 6
        """
        ...

    def __rfloordiv__(self: object, _0: Union[numpy.ndarray, int], /):
        """
        usage.sample_usage: 1
        usage.skimage: 2
        usage.sklearn: 1
        usage.dask: 2
        """
        ...

    def __mod__(self: object, _0: Union[numpy.ndarray, int, float], /):
        """
        usage.sample_usage: 1
        usage.skimage: 7
        usage.xarray: 2
        usage.sklearn: 8
        usage.dask: 12
        """
        ...

    def __rmod__(
        self: object,
        _0: Union[
            numpy.ndarray,
            int,
            Literal[
                "Deleting features without observed values: %s",
                "Features %s are constant.",
                "unable to convert object into a variable without a",
            ],
        ],
        /,
    ):
        """
        usage.sample_usage: 1
        usage.skimage: 1
        usage.xarray: 1
        usage.sklearn: 2
        usage.dask: 2
        """
        ...

    def __add__(self: object, _0: object, /):
        """
        usage.sample_usage: 2
        usage.skimage: 316
        usage.xarray: 32
        usage.sklearn: 232
        usage.dask: 188
        """
        ...

    def __radd__(self: object, _0: object, /):
        """
        usage.sample_usage: 2
        usage.skimage: 268
        usage.xarray: 40
        usage.sklearn: 171
        usage.dask: 72
        """
        ...

    def __sub__(self: object, _0: object, /):
        """
        usage.sample_usage: 1
        usage.skimage: 374
        usage.xarray: 25
        usage.sklearn: 358
        usage.dask: 45
        """
        ...

    def __rsub__(self: object, _0: object, /):
        """
        usage.sample_usage: 1
        usage.skimage: 274
        usage.xarray: 14
        usage.sklearn: 314
        usage.dask: 20
        """
        ...

    def __lshift__(self: object, _0: int, /):
        """
        usage.sample_usage: 1
        """
        ...

    def __rlshift__(self: object, _0: int, /):
        """
        usage.sample_usage: 1
        usage.dask: 1
        """
        ...

    def __rshift__(self: object, _0: int, /):
        """
        usage.sample_usage: 1
        usage.dask: 1
        """
        ...

    def __rrshift__(self: object, _0: int, /):
        """
        usage.sample_usage: 1
        """
        ...

    def __and__(
        self: object,
        _0: Union[bool, numpy.ndarray, dask.array.core.Array, numpy.bool_, int],
        /,
    ):
        """
        usage.sample_usage: 1
        usage.skimage: 33
        usage.xarray: 3
        usage.sklearn: 8
        usage.dask: 5
        """
        ...

    def __rand__(
        self: object,
        _0: Union[bool, numpy.ndarray, dask.array.core.Array, numpy.bool_, int],
        /,
    ):
        """
        usage.sample_usage: 1
        usage.skimage: 31
        usage.xarray: 3
        usage.sklearn: 8
        usage.dask: 5
        """
        ...

    def __or__(
        self: object,
        _0: Union[bool, numpy.ndarray, numpy.bool_, dask.array.core.Array, int],
        /,
    ):
        """
        usage.sample_usage: 1
        usage.skimage: 8
        usage.xarray: 4
        usage.sklearn: 6
        usage.dask: 3
        """
        ...

    def __ror__(
        self: object,
        _0: Union[bool, numpy.ndarray, dask.array.core.Array, numpy.bool_, int],
        /,
    ):
        """
        usage.sample_usage: 1
        usage.skimage: 8
        usage.xarray: 6
        usage.sklearn: 6
        usage.dask: 3
        """
        ...

    def __ipow__(self: object, _0: Union[int, float], /):
        """
        usage.sample_usage: 1
        usage.sklearn: 22
        """
        ...

    def __imul__(self: object, _0: object, /):
        """
        usage.sample_usage: 1
        usage.skimage: 42
        usage.xarray: 2
        usage.sklearn: 123
        usage.dask: 1
        """
        ...

    def __ifloordiv__(self: object, _0: int, /):
        """
        usage.sample_usage: 1
        usage.skimage: 5
        """
        ...

    def __imod__(self: object, _0: int, /):
        """
        usage.sample_usage: 1
        usage.dask: 3
        """
        ...

    def __iadd__(self: object, _0: object, /):
        """
        usage.sample_usage: 1
        usage.skimage: 131
        usage.xarray: 4
        usage.sklearn: 164
        usage.dask: 12
        """
        ...

    def __isub__(self: object, _0: object, /):
        """
        usage.sample_usage: 1
        usage.skimage: 45
        usage.xarray: 1
        usage.sklearn: 90
        usage.dask: 2
        """
        ...

    def __ilshift__(self: object, _0: int, /):
        """
        usage.sample_usage: 1
        """
        ...

    def __irshift__(self: object, _0: int, /):
        """
        usage.sample_usage: 1
        """
        ...

    def __iand__(self: object, _0: Union[numpy.ndarray, int], /):
        """
        usage.sample_usage: 1
        usage.skimage: 2
        usage.sklearn: 3
        """
        ...

    def __ior__(self: object, _0: Union[numpy.ndarray, int], /):
        """
        usage.sample_usage: 1
        usage.skimage: 3
        usage.xarray: 1
        """
        ...

    def __setitem__(self: object, _0: object, _1: object, /):
        """
        usage.sample_usage: 1
        usage.skimage: 1514
        usage.xarray: 142
        usage.sklearn: 840
        usage.dask: 527
        """
        ...

    def __eq__(self: object, _0: object, /):
        """
        usage.sample_usage: 2
        usage.skimage: 327
        usage.xarray: 330
        usage.sklearn: 280
        usage.dask: 189
        """
        ...

    def __le__(
        self: object,
        _0: Union[float, numpy.ndarray, int, numpy.float64, numpy.int64],
        /,
    ):
        """
        usage.sample_usage: 1
        usage.skimage: 122
        usage.xarray: 15
        usage.sklearn: 94
        usage.dask: 35
        """
        ...

    def sort(
        self: object,
        /,
        *,
        axis: int = ...,
        order: Literal["accumulator"] = ...,
        kind: Literal["mergesort"] = ...,
    ):
        """
        usage.sample_usage: 1
        usage.skimage: 9
        usage.sklearn: 1
        usage.dask: 1
        """
        ...

    def __gt__(self: object, _0: object, /):
        """
        usage.sample_usage: 1
        usage.skimage: 159
        usage.xarray: 9
        usage.sklearn: 81
        usage.dask: 26
        """
        ...

    def __contains__(self: object, _0: Union[int, numpy.int64, Tuple[int, int]], /):
        """
        usage.sample_usage: 1
        usage.skimage: 13
        usage.xarray: 3
        usage.sklearn: 19
        """
        ...

    def mean(
        self: object,
        /,
        *,
        axis: Union[Tuple[Union[int, None], ...], None, int] = ...,
        keepdims: bool = ...,
    ):
        """
        usage.skimage: 28
        usage.xarray: 5
        usage.sklearn: 48
        usage.dask: 10
        """
        ...

    def __truediv__(self: object, _0: object, /):
        """
        usage.skimage: 249
        usage.xarray: 9
        usage.sklearn: 223
        usage.dask: 23
        """
        ...

    def __rtruediv__(
        self: object,
        _0: Union[int, numpy.ndarray, numpy.float64, numpy.complex128, float],
        /,
    ):
        """
        usage.skimage: 102
        usage.xarray: 1
        usage.sklearn: 153
        usage.dask: 13
        """
        ...

    def __itruediv__(self: object, _0: object, /):
        """
        usage.skimage: 38
        usage.xarray: 2
        usage.sklearn: 80
        usage.dask: 1
        """
        ...

    def __ne__(self: object, _0: object, /):
        """
        usage.skimage: 44
        usage.xarray: 15
        usage.sklearn: 98
        usage.dask: 6
        """
        ...

    def __ge__(self: object, _0: object, /):
        """
        usage.skimage: 92
        usage.xarray: 5
        usage.sklearn: 43
        usage.dask: 17
        """
        ...

    def sum(
        self: object,
        /,
        *,
        axis: Union[Tuple[Union[int, None], ...], None, int] = ...,
        dtype: Union[Literal["f8", "i8"], numpy.dtype, Type[numpy.float64]] = ...,
        keepdims: bool = ...,
        out: numpy.ndarray = ...,
    ):
        """
        usage.skimage: 23
        usage.xarray: 3
        usage.sklearn: 96
        usage.dask: 126
        """
        ...

    def all(self: object, /, *, axis: int = ...):
        """
        usage.skimage: 47
        usage.xarray: 20
        usage.sklearn: 35
        usage.dask: 86
        """
        ...

    def any(self: object, /, *, axis: int = ...):
        """
        usage.skimage: 4
        usage.xarray: 2
        usage.sklearn: 20
        usage.dask: 1
        """
        ...

    def min(
        self: object,
        /,
        *,
        axis: int = ...,
        keepdims: bool = ...,
        out: numpy.ndarray = ...,
    ):
        """
        usage.skimage: 18
        usage.sklearn: 10
        usage.dask: 2
        """
        ...

    def max(self: object, /, *, axis: int = ..., keepdims: bool = ...):
        """
        usage.skimage: 18
        usage.sklearn: 3
        usage.dask: 2
        """
        ...

    def cumsum(self: object, /, *, axis: int):
        """
        usage.skimage: 6
        usage.dask: 4
        """
        ...

    def __lt__(self: object, _0: Union[int, numpy.ndarray, numpy.float64], /):
        """
        usage.skimage: 17
        usage.sklearn: 13
        usage.dask: 3
        """
        ...

    def argmax(self: object, /, *, axis: int = ...):
        """
        usage.skimage: 1
        usage.sklearn: 9
        """
        ...

    def astype(
        self: object,
        /,
        *,
        copy: bool = ...,
        dtype: Union[Literal["i2", ">u4", "i1"], numpy.dtype, type] = ...,
    ):
        """
        usage.skimage: 34
        usage.xarray: 89
        usage.sklearn: 62
        usage.dask: 29
        """
        ...

    def tolist(self: object, /):
        """
        usage.skimage: 6
        usage.xarray: 1
        usage.dask: 7
        """
        ...

    def std(
        self: object,
        /,
        *,
        axis: Union[int, Tuple[int, int]] = ...,
        ddof: int = ...,
        keepdims: bool = ...,
    ):
        """
        usage.skimage: 2
        usage.xarray: 2
        usage.sklearn: 10
        usage.dask: 1
        """
        ...

    def view(
        self: object,
        /,
        *,
        dtype: Union[Literal["|S512", "|S80", "|S16"], Type[numpy.uint8]],
    ):
        """
        usage.skimage: 4
        usage.sklearn: 3
        """
        ...

    def clip(
        self: object,
        _0: int = ...,
        _1: int = ...,
        /,
        *,
        min: int = ...,
        max: Union[int, Tuple[int, ...]] = ...,
    ):
        """
        usage.skimage: 3
        usage.xarray: 2
        usage.dask: 4
        """
        ...

    def repeat(self: object, _0: int, /, *, axis: int):
        """
        usage.skimage: 2
        usage.dask: 1
        """
        ...

    def ravel(self: object, /, *, order: Literal["K", "F", "C"] = ...):
        """
        usage.skimage: 2
        usage.xarray: 1
        usage.sklearn: 2
        usage.dask: 23
        """
        ...

    def var(self: object, /, *, axis: int = ...):
        """
        usage.skimage: 7
        usage.dask: 3
        """
        ...

    def reshape(
        self: object,
        _0: Union[Tuple[Union[int, None], ...], int],
        _1: int = ...,
        _2: int = ...,
        /,
    ):
        """
        usage.xarray: 6
        usage.sklearn: 5
        usage.dask: 11
        """
        ...

    def transpose(self: object, _0: List[int], /):
        """
        usage.xarray: 6
        """
        ...

    def round(self: object, /):
        """
        usage.xarray: 2
        """
        ...

    def argsort(self: object, /):
        """
        usage.xarray: 2
        """
        ...

    def item(self: object, /):
        """
        usage.xarray: 2
        """
        ...

    def take(
        self: object,
        _0: Union[List[numpy.int64], int, numpy.ndarray],
        /,
        *,
        axis: Union[None, int] = ...,
        mode: Literal["clip"] = ...,
    ):
        """
        usage.xarray: 4
        usage.sklearn: 70
        """
        ...

    def searchsorted(self: object, _0: int, /):
        """
        usage.xarray: 1
        """
        ...

    def argmin(self: object, /, *, axis: int):
        """
        usage.sklearn: 3
        usage.dask: 2
        """
        ...

    def squeeze(self: object, /, *, axis: Union[int, None, Tuple[int, int]] = ...):
        """
        usage.sklearn: 3
        usage.dask: 3
        """
        ...

    def copy(self: object, /, *, order: Literal["F", "K"] = ...):
        """
        usage.sklearn: 4
        usage.dask: 1
        """
        ...

    def setflags(self: object, /, *, write: bool):
        """
        usage.sklearn: 3
        """
        ...

    def __xor__(self: object, _0: Union[bool, numpy.ndarray], /):
        """
        usage.dask: 2
        """
        ...

    def __rxor__(self: object, _0: Union[bool, numpy.ndarray], /):
        """
        usage.dask: 2
        """
        ...

    def cumprod(self: object, /, *, axis: int):
        """
        usage.dask: 3
        """
        ...

    def trace(
        self: object,
        _0: int = ...,
        _1: int = ...,
        _2: int = ...,
        _3: type = ...,
        /,
        *,
        axis1: int = ...,
        axis2: int = ...,
        dtype: type = ...,
        offset: int = ...,
    ):
        """
        usage.dask: 7
        """
        ...


class dtype:
    def __init__(_0: Union[dask.delayed.DelayedLeaf, Literal["f4"]], /):
        """
        usage.dask: 2
        """
        ...

    # usage.dask: 1
    __module__: ClassVar[object]

    # usage.skimage: 64
    # usage.xarray: 74
    # usage.sklearn: 14
    # usage.dask: 9
    type: object

    # usage.skimage: 59
    # usage.xarray: 476
    # usage.sklearn: 137
    # usage.dask: 72
    kind: object

    # usage.skimage: 40
    # usage.xarray: 33
    # usage.sklearn: 3
    # usage.dask: 41
    itemsize: object

    # usage.skimage: 6
    # usage.dask: 6
    name: object

    # usage.skimage: 12
    # usage.sklearn: 3
    char: object

    # usage.xarray: 18
    isnative: object

    # usage.xarray: 5
    metadata: object

    # usage.dask: 33
    hasobject: object

    # usage.dask: 20
    shape: object

    # usage.dask: 15
    fields: object

    # usage.dask: 2
    base: object

    # usage.dask: 6
    names: object

    def __eq__(self: object, _0: Union[numpy.dtype, type, str], /):
        """
        usage.skimage: 282
        usage.xarray: 230
        usage.sklearn: 217
        usage.dask: 315
        """
        ...

    def __ne__(
        self: object,
        _0: Union[
            None,
            List[
                Tuple[
                    Literal["values", "indices", "inverse", "counts"],
                    Union[numpy.dtype, Type[numpy.int64]],
                ]
            ],
            type,
            str,
            numpy.dtype,
        ],
        /,
    ):
        """
        usage.skimage: 27
        usage.xarray: 34
        usage.sklearn: 33
        usage.dask: 266
        """
        ...

    def __rmod__(
        self: object,
        _0: Literal[
            ", dtype=%s",
            "            <xarray.Dataset>\n            Dimension",
            "Only bool or integer image types are supported. Go",
        ],
        /,
    ):
        """
        usage.skimage: 1
        usage.xarray: 1
        usage.dask: 2
        """
        ...

    def __getitem__(self: object, _0: str, /):
        """
        usage.dask: 17
        """
        ...


class ufunc:

    # usage.dask: 1
    __module__: ClassVar[object]

    @classmethod
    def reduce(
        _0: Callable,
        _1: Union[
            xarray.core.dataarray.DataArray,
            numpy.ndarray,
            Tuple[int],
            List[numpy.ndarray],
        ],
        /,
    ):
        """
        usage.sample_usage: 1
        usage.skimage: 6
        usage.xarray: 1
        """
        ...

    @classmethod
    def reduceat(_0: Callable, _1: numpy.ndarray, _2: numpy.ndarray, /):
        """
        usage.sklearn: 2
        """
        ...

    @classmethod
    def outer(
        _0: Callable,
        _1: object,
        _2: Union[numpy.ndarray, dask.array.core.Array, int],
        /,
    ):
        """
        usage.dask: 14
        """
        ...


class float64:

    # usage.dask: 2
    __module__: ClassVar[object]

    @classmethod
    def __ne__(_0: numpy.dtype, /):
        """
        usage.sklearn: 11
        usage.dask: 1
        """
        ...

    # usage.skimage: 2
    # usage.dask: 6
    ndim: object

    # usage.skimage: 1
    # usage.sklearn: 5
    # usage.dask: 12
    shape: object

    # usage.xarray: 4
    # usage.sklearn: 8
    # usage.dask: 12
    dtype: object

    def __le__(self: object, _0: object, /):
        """
        usage.skimage: 127
        usage.xarray: 13
        usage.sklearn: 111
        usage.dask: 26
        """
        ...

    def __rmul__(self: object, _0: object, /):
        """
        usage.skimage: 176
        usage.xarray: 3
        usage.sklearn: 203
        usage.dask: 15
        """
        ...

    def __gt__(self: object, _0: object, /):
        """
        usage.skimage: 74
        usage.xarray: 8
        usage.sklearn: 110
        usage.dask: 6
        """
        ...

    def __rsub__(self: object, _0: object, /):
        """
        usage.skimage: 111
        usage.xarray: 12
        usage.sklearn: 130
        usage.dask: 13
        """
        ...

    def __rtruediv__(self: object, _0: object, /):
        """
        usage.skimage: 106
        usage.xarray: 2
        usage.sklearn: 143
        usage.dask: 21
        """
        ...

    def __iadd__(self: object, _0: object, /):
        """
        usage.skimage: 9
        usage.xarray: 6
        usage.sklearn: 49
        usage.dask: 1
        """
        ...

    def __truediv__(self: object, _0: object, /):
        """
        usage.skimage: 96
        usage.xarray: 7
        usage.sklearn: 116
        usage.dask: 25
        """
        ...

    def __radd__(self: object, _0: object, /):
        """
        usage.skimage: 87
        usage.xarray: 9
        usage.sklearn: 114
        usage.dask: 26
        """
        ...

    def __add__(self: object, _0: object, /):
        """
        usage.skimage: 78
        usage.xarray: 9
        usage.sklearn: 98
        usage.dask: 22
        """
        ...

    def __sub__(self: object, _0: object, /):
        """
        usage.skimage: 154
        usage.xarray: 13
        usage.sklearn: 87
        usage.dask: 10
        """
        ...

    def __mul__(self: object, _0: object, /):
        """
        usage.skimage: 81
        usage.xarray: 3
        usage.sklearn: 160
        usage.dask: 7
        """
        ...

    def __getitem__(self: object, _0: Tuple[Union[None, ellipsis], ...], /):
        """
        usage.skimage: 2
        usage.xarray: 1
        usage.dask: 4
        """
        ...

    def __neg__(self: object, /):
        """
        usage.skimage: 22
        usage.xarray: 2
        usage.sklearn: 27
        """
        ...

    def __ge__(self: object, _0: object, /):
        """
        usage.skimage: 62
        usage.xarray: 6
        usage.sklearn: 70
        usage.dask: 29
        """
        ...

    def __pow__(self: object, _0: Union[float, int, numpy.float64], /):
        """
        usage.skimage: 36
        usage.sklearn: 20
        usage.dask: 3
        """
        ...

    def __lt__(self: object, _0: object, /):
        """
        usage.skimage: 60
        usage.xarray: 2
        usage.sklearn: 44
        usage.dask: 3
        """
        ...

    def __imod__(self: object, _0: float, /):
        """
        usage.skimage: 2
        """
        ...

    def __eq__(self: object, _0: object, /):
        """
        usage.skimage: 106
        usage.xarray: 50
        usage.sklearn: 142
        usage.dask: 31
        """
        ...

    def __mod__(self: object, _0: Union[int, float], /):
        """
        usage.skimage: 9
        """
        ...

    def __itruediv__(self: object, _0: object, /):
        """
        usage.skimage: 12
        usage.sklearn: 10
        """
        ...

    def __rpow__(self: object, _0: Union[numpy.ndarray, numpy.float64, float, int], /):
        """
        usage.skimage: 3
        usage.sklearn: 3
        """
        ...

    def __ne__(
        self: object,
        _0: Union[
            int, numpy.float64, float, numpy.int64, _pytest.python_api.ApproxScalar
        ],
        /,
    ):
        """
        usage.skimage: 9
        usage.xarray: 6
        usage.sklearn: 12
        usage.dask: 11
        """
        ...

    def __isub__(self: object, _0: Union[int, numpy.float64, numpy.ndarray], /):
        """
        usage.skimage: 1
        usage.sklearn: 18
        """
        ...

    def __imul__(self: object, _0: Union[numpy.int64, int, numpy.float64, float], /):
        """
        usage.skimage: 5
        usage.sklearn: 10
        usage.dask: 2
        """
        ...

    def __rfloordiv__(self: object, _0: numpy.ndarray, /):
        """
        usage.skimage: 1
        """
        ...

    def __rmod__(
        self: object,
        _0: Literal[
            "%0.2f MB",
            "Increasing number of chunks by factor of %d",
            "Bad index.  Must be integer-like: %s",
            "%.16g",
        ],
        /,
    ):
        """
        usage.sklearn: 2
        usage.dask: 3
        """
        ...

    def __floordiv__(self: object, _0: int, /):
        """
        usage.dask: 1
        """
        ...

    def astype(self: object, _0: numpy.dtype, /):
        """
        usage.dask: 1
        """
        ...


class int64:

    # usage.dask: 1
    __module__: ClassVar[object]

    @classmethod
    def __ne__(_0: numpy.dtype, /):
        """
        usage.dask: 2
        """
        ...

    # usage.skimage: 1
    # usage.dask: 8
    ndim: object

    # usage.xarray: 1
    # usage.dask: 10
    shape: object

    # usage.xarray: 1
    # usage.dask: 10
    dtype: object

    def __rmul__(self: object, _0: object, /):
        """
        usage.skimage: 8
        usage.xarray: 2
        usage.sklearn: 10
        usage.dask: 6
        """
        ...

    def __add__(self: object, _0: object, /):
        """
        usage.skimage: 38
        usage.xarray: 11
        usage.sklearn: 29
        usage.dask: 23
        """
        ...

    def __ne__(
        self: object,
        _0: Union[numpy.int64, int, float, numpy.float64, numpy.ndarray],
        /,
    ):
        """
        usage.skimage: 6
        usage.xarray: 5
        usage.sklearn: 12
        usage.dask: 16
        """
        ...

    def __ge__(self: object, _0: object, /):
        """
        usage.skimage: 17
        usage.xarray: 4
        usage.sklearn: 19
        usage.dask: 37
        """
        ...

    def __rsub__(
        self: object,
        _0: Union[numpy.int64, int, numpy.ndarray, float, numpy.float64],
        /,
    ):
        """
        usage.skimage: 30
        usage.xarray: 9
        usage.sklearn: 13
        usage.dask: 8
        """
        ...

    def __eq__(self: object, _0: object, /):
        """
        usage.skimage: 90
        usage.xarray: 24
        usage.sklearn: 82
        usage.dask: 96
        """
        ...

    def __rtruediv__(self: object, _0: object, /):
        """
        usage.skimage: 11
        usage.xarray: 3
        usage.sklearn: 20
        usage.dask: 12
        """
        ...

    def __sub__(self: object, _0: Union[int, numpy.int64, float, numpy.float64], /):
        """
        usage.skimage: 25
        usage.xarray: 10
        usage.sklearn: 23
        usage.dask: 10
        """
        ...

    def __floordiv__(self: object, _0: Union[int, numpy.int64], /):
        """
        usage.skimage: 5
        usage.xarray: 1
        usage.sklearn: 2
        usage.dask: 4
        """
        ...

    def __isub__(self: object, _0: Union[numpy.int64, int], /):
        """
        usage.skimage: 2
        usage.sklearn: 2
        usage.dask: 2
        """
        ...

    def __le__(
        self: object,
        _0: Union[numpy.int64, int, pandas.core.series.Series, float, numpy.ndarray],
        /,
    ):
        """
        usage.skimage: 18
        usage.xarray: 4
        usage.sklearn: 32
        usage.dask: 32
        """
        ...

    def __iadd__(self: object, _0: Union[int, numpy.int64, numpy.float64], /):
        """
        usage.skimage: 1
        usage.xarray: 3
        usage.sklearn: 3
        usage.dask: 3
        """
        ...

    def __gt__(self: object, _0: Union[float, int, numpy.int64], /):
        """
        usage.skimage: 11
        usage.xarray: 1
        usage.sklearn: 26
        usage.dask: 20
        """
        ...

    def __rfloordiv__(self: object, _0: Union[numpy.int64, int, float], /):
        """
        usage.skimage: 1
        usage.sklearn: 3
        usage.dask: 2
        """
        ...

    def __radd__(self: object, _0: object, /):
        """
        usage.skimage: 17
        usage.xarray: 1
        usage.sklearn: 13
        usage.dask: 26
        """
        ...

    def __truediv__(self: object, _0: Union[numpy.int64, int, float, numpy.float64], /):
        """
        usage.skimage: 15
        usage.xarray: 2
        usage.sklearn: 8
        usage.dask: 7
        """
        ...

    def __pow__(self: object, _0: Union[int, numpy.int64], /):
        """
        usage.skimage: 2
        usage.dask: 3
        """
        ...

    def __mul__(
        self: object,
        _0: Union[numpy.int64, numpy.ndarray, int, numpy.float64, float],
        /,
    ):
        """
        usage.skimage: 4
        usage.sklearn: 12
        usage.dask: 9
        """
        ...

    def __lt__(self: object, _0: object, /):
        """
        usage.skimage: 14
        usage.xarray: 3
        usage.sklearn: 5
        usage.dask: 13
        """
        ...

    def __itruediv__(self: object, _0: numpy.float64, /):
        """
        usage.skimage: 2
        """
        ...

    def __mod__(self: object, _0: Union[int, numpy.int64], /):
        """
        usage.skimage: 1
        usage.sklearn: 2
        usage.dask: 5
        """
        ...

    def __neg__(self: object, /):
        """
        usage.skimage: 7
        usage.xarray: 1
        usage.sklearn: 7
        usage.dask: 5
        """
        ...

    def __imod__(self: object, _0: int, /):
        """
        usage.skimage: 1
        """
        ...

    def __getitem__(self: object, _0: Tuple[Union[ellipsis, None], ...], /):
        """
        usage.xarray: 1
        usage.dask: 8
        """
        ...

    def __rmod__(
        self: object,
        _0: Union[
            numpy.int64,
            int,
            Literal[
                "not %s",
                "Fitting estimator with %d features.",
                "This solver needs samples of at least 2 classes in",
                "%d",
                "[MiniBatchKMeans] Reassigning %i cluster centers.",
            ],
        ],
        /,
    ):
        """
        usage.sklearn: 6
        usage.dask: 2
        """
        ...

    def __bool__(self: object, /):
        """
        usage.dask: 1
        """
        ...

    def __imul__(self: object, _0: int, /):
        """
        usage.dask: 1
        """
        ...

    def reshape(self: object, _0: Tuple[int], /):
        """
        usage.dask: 1
        """
        ...

    def __rpow__(self: object, _0: Union[int, numpy.int64], /):
        """
        usage.dask: 2
        """
        ...

    def __and__(self: object, _0: Union[bool, numpy.int64], /):
        """
        usage.dask: 2
        """
        ...

    def __rand__(self: object, _0: Union[bool, numpy.int64], /):
        """
        usage.dask: 2
        """
        ...

    def __or__(self: object, _0: Union[bool, numpy.int64], /):
        """
        usage.dask: 2
        """
        ...

    def __ror__(self: object, _0: Union[bool, numpy.int64], /):
        """
        usage.dask: 2
        """
        ...

    def __xor__(self: object, _0: Union[bool, numpy.int64], /):
        """
        usage.dask: 2
        """
        ...

    def __rxor__(self: object, _0: Union[bool, numpy.int64], /):
        """
        usage.dask: 2
        """
        ...


class generic:
    @classmethod
    def astype(
        _0: object,
        _1: Union[Literal["int64", "i8", "f8", "timedelta64[ns]"], numpy.dtype, type],
        /,
    ):
        """
        usage.skimage: 12
        usage.xarray: 7
        usage.sklearn: 1
        usage.dask: 11
        """
        ...

    @classmethod
    def conj(_0: numpy.complex128, /):
        """
        usage.skimage: 1
        """
        ...

    @classmethod
    def all(_0: numpy.bool_, /):
        """
        usage.xarray: 5
        """
        ...

    @classmethod
    def squeeze(_0: numpy.float64, /):
        """
        usage.xarray: 1
        """
        ...

    @classmethod
    def item(_0: numpy.float64, /):
        """
        usage.xarray: 3
        usage.sklearn: 2
        """
        ...

    @classmethod
    def any(_0: numpy.bool_, /):
        """
        usage.xarray: 2
        usage.dask: 1
        """
        ...

    @classmethod
    def mean(_0: numpy.float64, /):
        """
        usage.sklearn: 2
        """
        ...

    @classmethod
    def ravel(_0: numpy.int64, /):
        """
        usage.dask: 1
        """
        ...

    @classmethod
    def reshape(_0: numpy.float64, _1: Tuple[int, ...], /):
        """
        usage.dask: 2
        """
        ...


class iinfo:
    def __init__(int_type: Union[type, numpy.dtype, Literal["i"]]):
        """
        usage.skimage: 33
        usage.sklearn: 3
        usage.dask: 1
        """
        ...

    # usage.skimage: 3
    min: object

    # usage.skimage: 7
    # usage.sklearn: 11
    # usage.dask: 2
    max: object


class finfo:

    # usage.skimage: 11
    # usage.sklearn: 35
    # usage.dask: 1
    eps: object

    # usage.skimage: 2
    # usage.sklearn: 5
    resolution: object

    # usage.skimage: 2
    # usage.sklearn: 1
    max: object

    # usage.skimage: 2
    # usage.sklearn: 1
    min: object

    # usage.sklearn: 2
    tiny: object


class flagsobj:

    # usage.skimage: 3
    # usage.xarray: 2
    # usage.sklearn: 6
    writeable: bool

    # usage.skimage: 1
    # usage.sklearn: 2
    f_contiguous: object

    # usage.skimage: 2
    c_contiguous: object

    # usage.xarray: 1
    owndata: object

    # usage.sklearn: 2
    contiguous: object

    def __getitem__(self: object, _0: Literal["F_CONTIGUOUS", "C_CONTIGUOUS"], /):
        """
        usage.skimage: 2
        usage.xarray: 4
        usage.sklearn: 1
        """
        ...


class bool_:

    # usage.dask: 1
    __module__: ClassVar[object]

    @classmethod
    def __ne__(_0: numpy.dtype, /):
        """
        usage.skimage: 1
        """
        ...

    # usage.dask: 4
    dtype: object

    # usage.dask: 5
    ndim: object

    # usage.dask: 7
    shape: object

    def __invert__(self: object, /):
        """
        usage.skimage: 3
        usage.xarray: 1
        usage.dask: 1
        """
        ...

    def __bool__(self: object, /):
        """
        usage.skimage: 18
        usage.xarray: 3
        usage.sklearn: 24
        usage.dask: 12
        """
        ...

    def __rpow__(self: object, _0: int, /):
        """
        usage.skimage: 1
        """
        ...

    def __and__(self: object, _0: Union[numpy.ndarray, numpy.bool_], /):
        """
        usage.xarray: 2
        """
        ...

    def __rand__(
        self: object, _0: Union[dask.array.core.Array, numpy.bool_, numpy.ndarray], /
    ):
        """
        usage.xarray: 3
        """
        ...

    def __or__(self: object, _0: Union[numpy.ndarray, numpy.bool_], /):
        """
        usage.xarray: 3
        """
        ...

    def __ror__(self: object, _0: Union[bool, numpy.bool_, numpy.ndarray], /):
        """
        usage.xarray: 4
        """
        ...

    def all(self: object, /):
        """
        usage.xarray: 4
        usage.dask: 1
        """
        ...

    def __eq__(self: object, _0: Union[numpy.bool_, numpy.ndarray, bool], /):
        """
        usage.xarray: 2
        usage.sklearn: 5
        usage.dask: 2
        """
        ...

    def __gt__(self: object, _0: float, /):
        """
        usage.sklearn: 1
        """
        ...

    def __getitem__(self: object, _0: Tuple[ellipsis, None], /):
        """
        usage.dask: 1
        """
        ...


class flatiter:
    def __eq__(self: object, _0: Union[numpy.float64, int, numpy.int64], /):
        """
        usage.skimage: 4
        usage.sklearn: 1
        """
        ...

    def __iter__(self: object, /):
        """
        usage.skimage: 2
        usage.xarray: 8
        usage.sklearn: 4
        """
        ...

    def __getitem__(
        self: object,
        _0: Union[
            int,
            numpy.int64,
            slice[Union[None, int], Union[int, None], Union[None, int]],
        ],
        /,
    ):
        """
        usage.skimage: 5
        usage.xarray: 8
        usage.sklearn: 26
        usage.dask: 1
        """
        ...

    def __setitem__(
        self: object,
        _0: Union[
            int,
            numpy.ndarray,
            List[int],
            slice[Union[None, int], None, Union[None, int]],
        ],
        _1: Union[Tuple[Union[str, int], ...], float, numpy.ndarray, int],
        /,
    ):
        """
        usage.skimage: 1
        usage.xarray: 1
        usage.sklearn: 33
        usage.dask: 509
        """
        ...


class uint8:
    @classmethod
    def __ne__(_0: numpy.dtype, /):
        """
        usage.sklearn: 2
        """
        ...

    # usage.dask: 2
    ndim: object

    def __eq__(
        self: object, _0: Union[int, numpy.int64, numpy.uint8, numpy.ndarray], /
    ):
        """
        usage.skimage: 20
        usage.xarray: 1
        usage.sklearn: 3
        """
        ...

    def __rsub__(
        self: object, _0: Union[numpy.ndarray, int, numpy.float64, numpy.uint8], /
    ):
        """
        usage.skimage: 9
        """
        ...

    def __rmul__(self: object, _0: float, /):
        """
        usage.skimage: 3
        """
        ...

    def __lt__(self: object, _0: Union[numpy.float64, numpy.ndarray, int], /):
        """
        usage.skimage: 5
        """
        ...

    def __ge__(self: object, _0: Union[numpy.float64, int], /):
        """
        usage.skimage: 4
        """
        ...

    def __truediv__(self: object, _0: int, /):
        """
        usage.skimage: 1
        """
        ...

    def __radd__(self: object, _0: Union[numpy.ndarray, numpy.float64, numpy.uint8], /):
        """
        usage.skimage: 3
        """
        ...

    def __add__(self: object, _0: Union[int, numpy.uint8], /):
        """
        usage.skimage: 9
        """
        ...

    def __sub__(self: object, _0: Union[int, numpy.uint8], /):
        """
        usage.skimage: 5
        """
        ...

    def __le__(self: object, _0: Union[int, numpy.int64, numpy.ndarray], /):
        """
        usage.skimage: 8
        usage.xarray: 2
        """
        ...

    def __ne__(self: object, _0: numpy.uint8, /):
        """
        usage.skimage: 2
        """
        ...

    def __gt__(self: object, _0: Union[numpy.int64, int], /):
        """
        usage.skimage: 5
        usage.xarray: 1
        """
        ...

    def __rtruediv__(self: object, _0: numpy.float64, /):
        """
        usage.skimage: 2
        """
        ...

    def __pow__(self: object, _0: int, /):
        """
        usage.skimage: 1
        """
        ...

    def __iadd__(self: object, _0: int, /):
        """
        usage.xarray: 2
        """
        ...

    def __getitem__(self: object, _0: Tuple[Union[ellipsis, None], ...], /):
        """
        usage.dask: 3
        """
        ...


class uint64:

    # usage.dask: 1
    __module__: ClassVar[object]

    @classmethod
    def __ne__(_0: numpy.dtype, /):
        """
        usage.dask: 1
        """
        ...

    # usage.dask: 2
    ndim: object

    def __eq__(
        self: object, _0: Union[int, numpy.uint64, numpy.int64, numpy.ndarray], /
    ):
        """
        usage.skimage: 19
        usage.sklearn: 7
        """
        ...

    def __rtruediv__(self: object, _0: Union[numpy.uint64, float], /):
        """
        usage.skimage: 2
        usage.dask: 1
        """
        ...

    def __ge__(self: object, _0: int, /):
        """
        usage.skimage: 1
        """
        ...

    def __le__(self: object, _0: int, /):
        """
        usage.skimage: 3
        """
        ...

    def __ne__(self: object, _0: Union[numpy.uint64, float], /):
        """
        usage.skimage: 5
        usage.sklearn: 4
        """
        ...

    def __lt__(self: object, _0: Union[numpy.uint64, int], /):
        """
        usage.skimage: 3
        """
        ...

    def __truediv__(self: object, _0: Union[numpy.uint64, int], /):
        """
        usage.skimage: 1
        usage.dask: 1
        """
        ...

    def __rsub__(self: object, _0: Union[numpy.uint64, numpy.ndarray], /):
        """
        usage.skimage: 1
        usage.dask: 1
        """
        ...

    def __rmul__(self: object, _0: Union[int, float], /):
        """
        usage.skimage: 2
        usage.dask: 2
        """
        ...

    def __gt__(self: object, _0: Union[numpy.uint64, numpy.float64], /):
        """
        usage.skimage: 2
        """
        ...

    def __sub__(self: object, _0: numpy.uint64, /):
        """
        usage.dask: 1
        """
        ...

    def __mul__(self: object, _0: int, /):
        """
        usage.dask: 1
        """
        ...

    def __add__(self: object, _0: numpy.float64, /):
        """
        usage.dask: 2
        """
        ...

    def __getitem__(self: object, _0: Tuple[ellipsis, None], /):
        """
        usage.dask: 1
        """
        ...


class ndindex:
    def __init__(*shape: Literal["v", "t"]):
        """
        usage.skimage: 1
        usage.dask: 6
        """
        ...

    def __iter__(self: object, /):
        """
        usage.skimage: 3
        usage.dask: 5
        """
        ...


class uint32:

    # usage.dask: 1
    __module__: ClassVar[object]

    @classmethod
    def __ne__(_0: numpy.dtype, /):
        """
        usage.dask: 1
        """
        ...

    # usage.dask: 2
    ndim: object

    def __add__(self: object, _0: Union[numpy.int64, int], /):
        """
        usage.skimage: 1
        usage.dask: 2
        """
        ...

    def __ge__(self: object, _0: int, /):
        """
        usage.skimage: 1
        usage.sklearn: 1
        """
        ...

    def __le__(self: object, _0: int, /):
        """
        usage.skimage: 1
        """
        ...

    def __eq__(self: object, _0: Union[int, numpy.int64], /):
        """
        usage.skimage: 2
        usage.sklearn: 1
        """
        ...

    def __sub__(self: object, _0: Union[numpy.uint32, int], /):
        """
        usage.sklearn: 2
        usage.dask: 1
        """
        ...

    def __gt__(self: object, _0: numpy.uint32, /):
        """
        usage.sklearn: 1
        """
        ...

    def __lt__(self: object, _0: numpy.uint32, /):
        """
        usage.sklearn: 1
        """
        ...

    def __getitem__(self: object, _0: Tuple[ellipsis, None], /):
        """
        usage.dask: 1
        """
        ...

    def __rsub__(self: object, _0: numpy.uint32, /):
        """
        usage.dask: 1
        """
        ...

    def __truediv__(self: object, _0: numpy.uint32, /):
        """
        usage.dask: 1
        """
        ...

    def __rtruediv__(self: object, _0: numpy.uint32, /):
        """
        usage.dask: 1
        """
        ...

    def __mul__(self: object, _0: int, /):
        """
        usage.dask: 1
        """
        ...

    def __rmul__(self: object, _0: int, /):
        """
        usage.dask: 2
        """
        ...


class uint16:

    # usage.dask: 1
    ndim: object

    def __ge__(self: object, _0: int, /):
        """
        usage.skimage: 1
        usage.sklearn: 1
        """
        ...

    def __add__(self: object, _0: int, /):
        """
        usage.skimage: 1
        """
        ...

    def __eq__(self: object, _0: Union[numpy.int64, int], /):
        """
        usage.skimage: 9
        """
        ...

    def __le__(self: object, _0: int, /):
        """
        usage.skimage: 4
        usage.sklearn: 1
        """
        ...

    def __ne__(self: object, _0: numpy.uint16, /):
        """
        usage.skimage: 2
        """
        ...


class int16:

    # usage.dask: 2
    ndim: object

    def __ge__(self: object, _0: int, /):
        """
        usage.skimage: 1
        """
        ...

    def __le__(self: object, _0: int, /):
        """
        usage.skimage: 3
        """
        ...

    def __sub__(self: object, _0: numpy.int16, /):
        """
        usage.skimage: 2
        """
        ...

    def __rsub__(self: object, _0: numpy.int16, /):
        """
        usage.skimage: 2
        """
        ...

    def __rtruediv__(self: object, _0: numpy.float64, /):
        """
        usage.skimage: 1
        """
        ...

    def __pow__(self: object, _0: int, /):
        """
        usage.skimage: 1
        """
        ...

    def __eq__(self: object, _0: Union[numpy.ndarray, int, numpy.int64], /):
        """
        usage.skimage: 2
        usage.xarray: 1
        """
        ...

    def __ne__(self: object, _0: int, /):
        """
        usage.sklearn: 1
        """
        ...

    def __getitem__(self: object, _0: Tuple[ellipsis, None, None], /):
        """
        usage.dask: 1
        """
        ...


class int32:

    # usage.dask: 2
    __module__: ClassVar[object]

    @classmethod
    def __ne__(_0: numpy.dtype, /):
        """
        usage.sklearn: 3
        usage.dask: 1
        """
        ...

    # usage.xarray: 1
    # usage.dask: 1
    dtype: object

    # usage.dask: 3
    ndim: object

    # usage.dask: 5
    shape: object

    def __ge__(self: object, _0: Union[int, float], /):
        """
        usage.skimage: 1
        usage.sklearn: 2
        """
        ...

    def __le__(self: object, _0: int, /):
        """
        usage.skimage: 2
        usage.sklearn: 2
        """
        ...

    def __eq__(
        self: object, _0: Union[int, numpy.int64, numpy.int32, numpy.ndarray], /
    ):
        """
        usage.skimage: 3
        usage.xarray: 1
        usage.sklearn: 7
        usage.dask: 5
        """
        ...

    def __rmul__(self: object, _0: Union[int, numpy.ndarray], /):
        """
        usage.sklearn: 1
        usage.dask: 2
        """
        ...

    def __add__(self: object, _0: Union[numpy.int64, bool], /):
        """
        usage.sklearn: 2
        usage.dask: 2
        """
        ...

    def __rmod__(self: object, _0: Literal["%d"], /):
        """
        usage.sklearn: 1
        """
        ...

    def __sub__(self: object, _0: Union[numpy.int32, int], /):
        """
        usage.sklearn: 1
        usage.dask: 1
        """
        ...

    def __getitem__(self: object, _0: Tuple[Union[None, ellipsis], ...], /):
        """
        usage.dask: 2
        """
        ...

    def __rsub__(self: object, _0: numpy.int32, /):
        """
        usage.dask: 1
        """
        ...

    def __truediv__(self: object, _0: numpy.int32, /):
        """
        usage.dask: 1
        """
        ...

    def __rtruediv__(self: object, _0: numpy.int32, /):
        """
        usage.dask: 1
        """
        ...

    def __mul__(self: object, _0: int, /):
        """
        usage.dask: 1
        """
        ...


class float32:

    # usage.dask: 1
    shape: ClassVar[object]

    # usage.dask: 1
    __module__: ClassVar[object]

    @classmethod
    def __ne__(_0: numpy.dtype, /):
        """
        usage.sklearn: 3
        usage.dask: 2
        """
        ...

    # usage.xarray: 1
    # usage.sklearn: 2
    # usage.dask: 2
    dtype: object

    # usage.dask: 4
    ndim: object

    def __sub__(
        self: object, _0: Union[numpy.float32, int, numpy.ndarray, numpy.float64], /
    ):
        """
        usage.skimage: 5
        usage.sklearn: 3
        usage.dask: 2
        """
        ...

    def __gt__(self: object, _0: Union[int, float, numpy.float64], /):
        """
        usage.skimage: 4
        usage.xarray: 1
        usage.sklearn: 2
        """
        ...

    def __add__(self: object, _0: Union[numpy.float64, numpy.float32, int], /):
        """
        usage.skimage: 2
        usage.sklearn: 2
        usage.dask: 3
        """
        ...

    def __ge__(self: object, _0: Union[numpy.float32, float, int], /):
        """
        usage.skimage: 3
        usage.sklearn: 1
        """
        ...

    def __lt__(self: object, _0: Union[numpy.float64, numpy.ndarray, float], /):
        """
        usage.skimage: 5
        usage.sklearn: 2
        """
        ...

    def __truediv__(self: object, _0: Union[numpy.float32, float, numpy.float64], /):
        """
        usage.skimage: 2
        usage.sklearn: 3
        usage.dask: 1
        """
        ...

    def __rmul__(self: object, _0: Union[int, numpy.ndarray, float, numpy.float32], /):
        """
        usage.skimage: 4
        usage.sklearn: 10
        usage.dask: 2
        """
        ...

    def __mul__(self: object, _0: Union[int, numpy.float32, float, numpy.ndarray], /):
        """
        usage.skimage: 1
        usage.sklearn: 10
        usage.dask: 1
        """
        ...

    def __le__(self: object, _0: Union[int, numpy.float32, float, numpy.float64], /):
        """
        usage.skimage: 4
        usage.xarray: 2
        usage.sklearn: 4
        """
        ...

    def __eq__(self: object, _0: Union[numpy.float32, int, float, numpy.ndarray], /):
        """
        usage.skimage: 5
        usage.xarray: 2
        usage.sklearn: 4
        usage.dask: 3
        """
        ...

    def __rtruediv__(
        self: object,
        _0: Union[numpy.float32, float, int, numpy.ndarray, numpy.float64],
        /,
    ):
        """
        usage.skimage: 1
        usage.sklearn: 14
        usage.dask: 1
        """
        ...

    def __rsub__(
        self: object,
        _0: Union[numpy.float32, numpy.float64, int, numpy.ndarray, float],
        /,
    ):
        """
        usage.skimage: 3
        usage.sklearn: 14
        usage.dask: 1
        """
        ...

    def __pow__(self: object, _0: int, /):
        """
        usage.skimage: 1
        """
        ...

    def __iadd__(self: object, _0: Union[numpy.float32, int], /):
        """
        usage.xarray: 2
        usage.sklearn: 2
        """
        ...

    def __itruediv__(self: object, _0: int, /):
        """
        usage.sklearn: 2
        """
        ...

    def __radd__(
        self: object,
        _0: Union[numpy.float32, numpy.ndarray, float, int, numpy.float64],
        /,
    ):
        """
        usage.sklearn: 9
        usage.dask: 1
        """
        ...

    def __ne__(self: object, _0: int, /):
        """
        usage.sklearn: 1
        """
        ...

    def __getitem__(self: object, _0: Tuple[Union[None, ellipsis], ...], /):
        """
        usage.dask: 2
        """
        ...


class matrix:

    # usage.dask: 1
    __name__: ClassVar[object]

    # usage.dask: 2
    __module__: ClassVar[object]

    # usage.skimage: 2
    A: object

    # usage.sklearn: 2
    # usage.dask: 4
    shape: object

    # usage.dask: 3
    dtype: object

    # usage.dask: 1
    __class__: object

    # usage.dask: 4
    ndim: object

    def __rmatmul__(self: object, _0: numpy.ndarray, /):
        """
        usage.skimage: 1
        """
        ...

    def __neg__(self: object, /):
        """
        usage.skimage: 2
        """
        ...

    def __matmul__(self: object, _0: numpy.ndarray, /):
        """
        usage.skimage: 1
        """
        ...

    def __rtruediv__(self: object, _0: Union[numpy.ndarray, float], /):
        """
        usage.sklearn: 3
        """
        ...

    def max(self: object, /):
        """
        usage.sklearn: 3
        """
        ...

    def __getitem__(
        self: object,
        _0: Union[
            int,
            Tuple[
                Union[int, slice[int, int, int]],
                slice[Union[int, None], Union[int, None], Union[int, None]],
            ],
        ],
        /,
    ):
        """
        usage.sklearn: 2
        usage.dask: 2
        """
        ...

    def __sub__(self: object, _0: numpy.ndarray, /):
        """
        usage.sklearn: 2
        """
        ...

    def __truediv__(self: object, _0: float, /):
        """
        usage.sklearn: 1
        """
        ...

    def __eq__(self: object, _0: float, /):
        """
        usage.sklearn: 1
        """
        ...

    def view(self: object, /, *, type: Type[numpy.ndarray]):
        """
        usage.dask: 2
        """
        ...

    def all(self: object, /):
        """
        usage.dask: 2
        """
        ...

    def __setitem__(self: object, _0: slice[None, int, None], _1: int, /):
        """
        usage.dask: 1
        """
        ...


class int8:
    @classmethod
    def __ne__(_0: numpy.dtype, /):
        """
        usage.dask: 2
        """
        ...

    # usage.dask: 2
    ndim: object

    def __lt__(self: object, _0: int, /):
        """
        usage.skimage: 2
        """
        ...

    def __le__(self: object, _0: int, /):
        """
        usage.skimage: 2
        """
        ...

    def __eq__(self: object, _0: Union[numpy.ndarray, numpy.int64, int], /):
        """
        usage.skimage: 3
        usage.xarray: 1
        """
        ...

    def __gt__(self: object, _0: int, /):
        """
        usage.skimage: 1
        """
        ...

    def __getitem__(self: object, _0: Tuple[Union[None, ellipsis], ...], /):
        """
        usage.dask: 2
        """
        ...


class complex128:

    # usage.skimage: 1
    imag: object

    # usage.skimage: 1
    real: object

    # usage.dask: 5
    ndim: object

    # usage.dask: 5
    shape: object

    # usage.dask: 1
    dtype: object

    def __eq__(self: object, _0: numpy.ndarray, /):
        """
        usage.skimage: 1
        """
        ...

    def __mul__(self: object, _0: numpy.complex128, /):
        """
        usage.skimage: 2
        """
        ...

    def __rmul__(self: object, _0: numpy.complex128, /):
        """
        usage.skimage: 2
        """
        ...

    def __truediv__(
        self: object, _0: Union[numpy.ndarray, numpy.float64, numpy.complex128], /
    ):
        """
        usage.skimage: 3
        """
        ...

    def __rsub__(self: object, _0: float, /):
        """
        usage.skimage: 1
        """
        ...

    def __itruediv__(self: object, _0: numpy.float64, /):
        """
        usage.skimage: 2
        """
        ...

    def __rtruediv__(self: object, _0: numpy.complex128, /):
        """
        usage.skimage: 1
        """
        ...

    def __getitem__(self: object, _0: Tuple[Union[None, ellipsis], ...], /):
        """
        usage.dask: 2
        """
        ...


class float16:

    # usage.dask: 1
    ndim: object

    def __sub__(self: object, _0: numpy.float16, /):
        """
        usage.skimage: 2
        """
        ...

    def __rsub__(self: object, _0: Union[numpy.ndarray, numpy.float16], /):
        """
        usage.skimage: 3
        """
        ...

    def __pow__(self: object, _0: int, /):
        """
        usage.skimage: 1
        """
        ...

    def __rmul__(self: object, _0: Union[numpy.ndarray, float], /):
        """
        usage.skimage: 2
        """
        ...

    def __eq__(self: object, _0: int, /):
        """
        usage.skimage: 1
        """
        ...

    def __gt__(self: object, _0: numpy.float64, /):
        """
        usage.skimage: 1
        """
        ...


class nditer:

    # usage.skimage: 1
    multi_index: object

    def __iter__(self: object, /):
        """
        usage.skimage: 1
        """
        ...


class longlong:

    # usage.dask: 1
    ndim: object

    def __le__(self: object, _0: int, /):
        """
        usage.skimage: 1
        usage.sklearn: 1
        """
        ...

    def __eq__(self: object, _0: Union[int, numpy.int64], /):
        """
        usage.skimage: 2
        usage.sklearn: 5
        """
        ...

    def __rtruediv__(self: object, _0: Union[numpy.float64, numpy.ndarray], /):
        """
        usage.sklearn: 3
        """
        ...

    def __gt__(self: object, _0: int, /):
        """
        usage.sklearn: 1
        """
        ...

    def __add__(self: object, _0: int, /):
        """
        usage.sklearn: 1
        """
        ...

    def __ge__(self: object, _0: int, /):
        """
        usage.sklearn: 1
        """
        ...

    def __mul__(self: object, _0: float, /):
        """
        usage.sklearn: 1
        """
        ...


class ulonglong:

    # usage.dask: 1
    ndim: object

    def __le__(self: object, _0: int, /):
        """
        usage.skimage: 1
        """
        ...

    def __eq__(self: object, _0: Union[numpy.int64, int], /):
        """
        usage.skimage: 2
        """
        ...


class void:

    # usage.dask: 1
    __module__: ClassVar[object]

    # usage.dask: 2
    ndim: object

    def __getitem__(
        self: object, _0: Union[Tuple[Union[ellipsis, None], ...], int, str], /
    ):
        """
        usage.skimage: 33
        usage.sklearn: 11
        usage.dask: 2
        """
        ...

    def __setitem__(
        self: object, _0: str, _1: Union[int, float, bool, numpy.float64], /
    ):
        """
        usage.sklearn: 23
        """
        ...


class errstate:
    def __init__():
        """
        usage.xarray: 4
        usage.sklearn: 13
        usage.dask: 10
        """
        ...


class vectorize:
    def __init__(pyfunc: Union[Type[int], Callable, functools.partial]):
        """
        usage.xarray: 75
        usage.dask: 7
        """
        ...

    # usage.dask: 1
    __module__: ClassVar[object]

    # usage.dask: 1
    pyfunc: object


class str_:

    # usage.dask: 1
    __module__: ClassVar[object]

    # usage.xarray: 1
    # usage.dask: 2
    dtype: object

    # usage.dask: 2
    ndim: object

    # usage.dask: 4
    shape: object

    def __getitem__(
        self: object,
        _0: Union[
            Tuple[ellipsis, None],
            slice[Union[None, int], Union[None, int], Union[None, int]],
        ],
        /,
    ):
        """
        usage.xarray: 2
        usage.dask: 1
        """
        ...

    def __iadd__(self: object, _0: Union[str, numpy.str_], /):
        """
        usage.xarray: 12
        """
        ...

    def __radd__(self: object, _0: str, /):
        """
        usage.xarray: 11
        """
        ...

    def __contains__(self: object, _0: Literal[" "], /):
        """
        usage.xarray: 1
        """
        ...

    def __ne__(self: object, _0: Union[str, numpy.ndarray], /):
        """
        usage.xarray: 2
        usage.sklearn: 7
        """
        ...

    def __eq__(
        self: object,
        _0: Union[
            Literal["ZN", "CRIM", "c", "b", "a"],
            numpy.ndarray,
            xarray.core.variable.Variable,
            xarray.core.dataarray.DataArray,
        ],
        /,
    ):
        """
        usage.xarray: 6
        usage.sklearn: 7
        """
        ...

    def __iter__(self: object, /):
        """
        usage.sklearn: 2
        """
        ...


class bytes_:
    def __init__(_0: Union[int, Literal["asdf"]], /):
        """
        usage.xarray: 1
        usage.dask: 1
        """
        ...

    # usage.dask: 1
    ndim: object

    def __getitem__(
        self: object, _0: slice[Union[int, None], Union[int, None], Union[int, None]], /
    ):
        """
        usage.xarray: 2
        """
        ...

    def __iadd__(self: object, _0: Union[numpy.bytes_, bytes], /):
        """
        usage.xarray: 2
        """
        ...

    def __radd__(self: object, _0: bytes, /):
        """
        usage.xarray: 1
        """
        ...

    def __eq__(self: object, _0: numpy.ndarray, /):
        """
        usage.xarray: 1
        """
        ...


class timedelta64:
    def __init__(_0: Union[int, datetime.timedelta], _1: Literal["D", "ns"], /):
        """
        usage.xarray: 1
        usage.dask: 7
        """
        ...

    # usage.dask: 1
    __module__: ClassVar[object]

    # usage.xarray: 7
    dtype: object

    # usage.dask: 1
    ndim: object

    # usage.dask: 2
    shape: object

    def __rtruediv__(
        self: object,
        _0: Union[
            dask.array.core.Array,
            numpy.ndarray,
            pandas.core.indexes.timedeltas.TimedeltaIndex,
            numpy.timedelta64,
        ],
        /,
    ):
        """
        usage.xarray: 7
        usage.dask: 2
        """
        ...

    def __truediv__(self: object, _0: numpy.timedelta64, /):
        """
        usage.xarray: 3
        """
        ...

    def __rmul__(self: object, _0: Union[numpy.ndarray, float], /):
        """
        usage.xarray: 5
        """
        ...

    def __add__(self: object, _0: numpy.ndarray, /):
        """
        usage.xarray: 1
        """
        ...

    def __ne__(self: object, _0: numpy.ndarray, /):
        """
        usage.xarray: 1
        """
        ...

    def __rsub__(self: object, _0: pandas.core.indexes.datetimes.DatetimeIndex, /):
        """
        usage.xarray: 1
        """
        ...

    def __eq__(self: object, _0: numpy.timedelta64, /):
        """
        usage.xarray: 4
        """
        ...


class datetime64:
    def __init__(_0: Literal["NaT", "2014"], /):
        """
        usage.dask: 3
        """
        ...

    # usage.xarray: 3
    # usage.dask: 1
    dtype: object

    # usage.dask: 1
    ndim: object

    def __add__(self: object, _0: numpy.ndarray, /):
        """
        usage.xarray: 4
        """
        ...

    def __rsub__(self: object, _0: numpy.ndarray, /):
        """
        usage.xarray: 1
        """
        ...

    def __eq__(
        self: object,
        _0: Union[
            numpy.ndarray,
            xarray.core.dataarray.DataArray,
            xarray.core.variable.Variable,
            numpy.datetime64,
        ],
        /,
    ):
        """
        usage.xarray: 14
        """
        ...

    def __le__(self: object, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        """
        usage.dask: 1
        """
        ...


class broadcast:
    def __init__(
        _0: Union[dask.array.core.Array, int, numpy.ndarray, List[int]],
        _1: Union[Literal["z", "_not_supplied"], numpy.ndarray, List[int]] = ...,
        _2: numpy.ndarray = ...,
        /,
    ):
        """
        usage.xarray: 14
        """
        ...

    # usage.xarray: 4
    shape: object


class object_:
    def __init__(_0: Union[int, bytes], /):
        """
        usage.xarray: 1
        usage.dask: 1
        """
        ...

    @classmethod
    def __ne__(_0: numpy.dtype, /):
        """
        usage.dask: 1
        """
        ...


class ndenumerate:
    def __iter__(self: object, /):
        """
        usage.xarray: 2
        """
        ...


class memmap:

    # usage.sklearn: 1
    __name__: ClassVar[object]

    # usage.dask: 1
    __module__: ClassVar[object]

    @classmethod
    def __rmod__(_0: Literal["Expected sequence or array-like, got %s"], /):
        """
        usage.sklearn: 1
        """
        ...

    # usage.sklearn: 1
    __class__: object

    # usage.sklearn: 13
    # usage.dask: 8
    shape: object

    # usage.sklearn: 9
    T: object

    # usage.sklearn: 1
    # usage.dask: 1
    ndim: object

    # usage.sklearn: 1
    flags: object

    # usage.sklearn: 2
    # usage.dask: 4
    dtype: object

    # usage.sklearn: 2
    size: object

    # usage.dask: 1
    _mmap: object

    # usage.dask: 5
    base: object

    # usage.dask: 6
    filename: object

    # usage.dask: 3
    strides: object

    # usage.dask: 4
    ctypes: object

    def __getitem__(
        self: object,
        _0: Union[
            slice[Union[None, int], Union[int, None], Union[None, int]],
            Tuple[
                Union[slice[Union[int, None], Union[int, None], Union[int, None]], int],
                Union[None, numpy.ndarray, int, slice[None, Union[None, int], None]],
            ],
            numpy.int64,
            numpy.ndarray,
            int,
        ],
        /,
    ):
        """
        usage.sklearn: 17
        usage.dask: 7
        """
        ...

    def mean(self: object, /, *, axis: int):
        """
        usage.sklearn: 2
        """
        ...

    def __isub__(self: object, _0: Union[numpy.float64, numpy.ndarray], /):
        """
        usage.sklearn: 4
        """
        ...

    def __pow__(self: object, _0: int, /):
        """
        usage.sklearn: 1
        """
        ...

    def __setitem__(
        self: object,
        _0: Union[int, numpy.int64, Tuple[slice[None, None, None], numpy.ndarray]],
        _1: numpy.ndarray,
        /,
    ):
        """
        usage.sklearn: 5
        """
        ...

    def __add__(self: object, _0: numpy.memmap, /):
        """
        usage.dask: 1
        """
        ...

    def __radd__(self: object, _0: numpy.memmap, /):
        """
        usage.dask: 1
        """
        ...


class complex64:

    # usage.dask: 2
    ndim: object

    def __getitem__(self: object, _0: Tuple[ellipsis, None, None], /):
        """
        usage.dask: 1
        """
        ...


class float128:

    # usage.dask: 1
    ndim: object


class complex256:

    # usage.dask: 1
    ndim: object


class AxisError:
    def __init__(axis: str):
        """
        usage.dask: 9
        """
        ...


class recarray:

    # usage.dask: 1
    __module__: ClassVar[object]

    # usage.dask: 7
    shape: object

    # usage.dask: 1
    dtype: object

    # usage.dask: 1
    ndim: object

    def __eq__(self: object, _0: numpy.ndarray, /):
        """
        usage.dask: 3
        """
        ...

    def all(self: object, /):
        """
        usage.dask: 2
        """
        ...

    def __getitem__(self: object, _0: slice[None, int, None], /):
        """
        usage.dask: 1
        """
        ...


class record:

    # usage.dask: 2
    ndim: object

    def __getitem__(self: object, _0: Tuple[ellipsis, None], /):
        """
        usage.dask: 1
        """
        ...
