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
    "\n    usage.sample_usage: 4\n    usage.skimage: 223\n    usage.xarray: 403\n    usage.sklearn: 151\n    usage.dask: 341\n    "
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
    "\n    usage.sample_usage: 3\n    usage.skimage: 1076\n    usage.xarray: 400\n    usage.sklearn: 815\n    usage.dask: 485\n    "
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
    "\n    usage.sample_usage: 1\n    usage.skimage: 787\n    usage.xarray: 52\n    usage.sklearn: 350\n    usage.dask: 50\n    "
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
    "\n    usage.sample_usage: 1\n    usage.skimage: 269\n    usage.xarray: 59\n    usage.sklearn: 210\n    usage.dask: 183\n    "
    ...


def linspace(
    start: Union[float, numpy.float64, int, numpy.int64],
    stop: Union[int, float, numpy.float64, numpy.int64, numpy.float32],
    num: Union[int, numpy.int64] = ...,
    endpoint: bool = ...,
    retstep: bool = ...,
    dtype: Union[type, numpy.dtype] = ...,
):
    "\n    usage.sample_usage: 1\n    usage.skimage: 70\n    usage.xarray: 95\n    usage.sklearn: 41\n    usage.dask: 22\n    "
    ...


def eye(N: int, M: int = ..., k: int = ..., dtype: type = ...):
    "\n    usage.sample_usage: 1\n    usage.skimage: 39\n    usage.sklearn: 27\n    usage.dask: 35\n    "
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
    "\n    usage.sample_usage: 1\n    usage.skimage: 11\n    usage.xarray: 13\n    usage.sklearn: 1\n    usage.dask: 29\n    "
    ...


def exp(
    _0: object, /, *, dtype: numpy.dtype = ..., out: dask.dataframe.core.DataFrame = ...
):
    "\n    usage.sample_usage: 1\n    usage.skimage: 26\n    usage.xarray: 3\n    usage.sklearn: 62\n    usage.dask: 42\n    "
    ...


def log(
    _0: object,
    /,
    *,
    out: Union[dask.dataframe.core.DataFrame, dask.array.core.Array] = ...,
):
    "\n    usage.sample_usage: 1\n    usage.skimage: 19\n    usage.xarray: 2\n    usage.sklearn: 78\n    usage.dask: 47\n    "
    ...


def column_stack(tup: Union[List[numpy.ndarray], Tuple[numpy.ndarray, numpy.ndarray]]):
    "\n    usage.sample_usage: 1\n    usage.skimage: 9\n    usage.sklearn: 2\n    "
    ...


def concatenate(
    _0: Union[list, Tuple[Union[List[Union[int, numpy.float64]], numpy.ndarray], ...]],
    /,
    *,
    axis: int = ...,
):
    "\n    usage.sample_usage: 1\n    usage.skimage: 48\n    usage.xarray: 46\n    usage.sklearn: 50\n    usage.dask: 96\n    "
    ...


def absolute(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    "\n    usage.skimage: 113\n    usage.sklearn: 154\n    usage.dask: 49\n    "
    ...


def asarray(
    a: object,
    dtype: Union[numpy.dtype, numpy.ndarray, type, str, None] = ...,
    order: Union[Literal["C", "F"], None] = ...,
):
    "\n    usage.skimage: 247\n    usage.xarray: 870\n    usage.sklearn: 2199\n    usage.dask: 126\n    "
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
    "\n    usage.skimage: 125\n    usage.xarray: 54\n    usage.sklearn: 208\n    usage.dask: 256\n    "
    ...


def vstack(tup: object):
    "\n    usage.skimage: 33\n    usage.sklearn: 69\n    usage.dask: 10\n    "
    ...


def all(
    a: object = ...,
    axis: Union[int, Tuple[Union[int, None], ...]] = ...,
    keepdims: bool = ...,
    *,
    computing_meta: bool = ...,
):
    "\n    usage.skimage: 113\n    usage.xarray: 14\n    usage.sklearn: 91\n    usage.dask: 134\n    "
    ...


def round_(a: object):
    "\n    usage.skimage: 30\n    usage.sklearn: 3\n    usage.dask: 9\n    "
    ...


def asanyarray(a: object):
    "\n    usage.skimage: 50\n    usage.sklearn: 14\n    usage.dask: 44\n    "
    ...


def obj2sctype(rep: Union[Literal["float64", "float32"], type, numpy.dtype]):
    "\n    usage.skimage: 14\n    "
    ...


def issubdtype(arg1: Union[numpy.dtype, type], arg2: type):
    "\n    usage.skimage: 162\n    usage.xarray: 256\n    usage.sklearn: 19\n    usage.dask: 43\n    "
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
    "\n    usage.skimage: 25\n    usage.xarray: 2\n    usage.sklearn: 2\n    usage.dask: 23\n    "
    ...


def reshape(
    a: Union[
        numpy.ndarray,
        List[Union[float, int, numpy.ndarray, numpy.float64, numpy.int64]],
        Tuple[numpy.ndarray, ...],
    ],
    newshape: Union[List[int], Tuple[Union[None, numpy.int64, int], ...]],
):
    "\n    usage.skimage: 43\n    usage.xarray: 7\n    usage.sklearn: 50\n    "
    ...


def sqrt(
    _0: object, /, *, out: Union[dask.dataframe.core.DataFrame, numpy.ndarray] = ...
):
    "\n    usage.skimage: 112\n    usage.xarray: 4\n    usage.sklearn: 108\n    usage.dask: 63\n    "
    ...


def moveaxis(
    a: Union[numpy.ndarray, dask.array.core.Array, int, numpy.float64],
    source: Union[int, numpy.ndarray, range, Tuple[None, ...]],
    destination: Union[int, numpy.ndarray, Tuple[None, ...], List[int]],
):
    "\n    usage.skimage: 6\n    usage.xarray: 17\n    usage.dask: 4\n    "
    ...


def rollaxis(a: Union[numpy.ndarray, dask.array.core.Array], axis: int):
    "\n    usage.skimage: 14\n    usage.sklearn: 5\n    usage.dask: 5\n    "
    ...


def any(
    a: object = ...,
    axis: Union[int, Tuple[Union[int, None], ...]] = ...,
    keepdims: bool = ...,
    *,
    computing_meta: bool = ...,
):
    "\n    usage.skimage: 39\n    usage.xarray: 5\n    usage.sklearn: 45\n    usage.dask: 124\n    "
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
    "\n    usage.skimage: 48\n    usage.xarray: 2\n    usage.sklearn: 22\n    usage.dask: 8\n    "
    ...


def triu(m: numpy.ndarray):
    "\n    usage.skimage: 1\n    usage.dask: 8\n    "
    ...


def seterr(
    divide: Literal["warn"] = ...,
    over: Literal["warn"] = ...,
    under: Literal["ignore"] = ...,
    invalid: Literal["warn", "ignore"] = ...,
):
    "\n    usage.skimage: 2\n    usage.sklearn: 4\n    usage.dask: 2\n    "
    ...


def isnan(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    "\n    usage.skimage: 14\n    usage.xarray: 14\n    usage.sklearn: 30\n    usage.dask: 150\n    "
    ...


def floor(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    "\n    usage.skimage: 13\n    usage.xarray: 2\n    usage.sklearn: 2\n    usage.dask: 41\n    "
    ...


def stack(arrays: Union[list, Tuple[Union[numpy.float64, numpy.ndarray], ...]]):
    "\n    usage.skimage: 35\n    usage.xarray: 26\n    usage.dask: 30\n    "
    ...


def choose(
    a: numpy.ndarray,
    choices: Union[
        Tuple[Union[int, numpy.ndarray], numpy.ndarray], List[Union[numpy.ndarray, int]]
    ],
):
    "\n    usage.skimage: 2\n    usage.dask: 4\n    "
    ...


def amin(
    a: object = ...,
    axis: Union[int, Tuple[Union[int, None], ...], None] = ...,
    out: Union[dask.dataframe.core.Scalar, dask.dataframe.core.Series] = ...,
    keepdims: bool = ...,
    *,
    computing_meta: bool = ...,
):
    "\n    usage.skimage: 60\n    usage.xarray: 25\n    usage.sklearn: 30\n    usage.dask: 159\n    "
    ...


def amax(
    a: object = ...,
    axis: Union[int, Tuple[Union[int, None], ...], None] = ...,
    out: Union[dask.dataframe.core.Scalar, dask.dataframe.core.Series] = ...,
    keepdims: bool = ...,
    *,
    computing_meta: bool = ...,
):
    "\n    usage.skimage: 105\n    usage.xarray: 23\n    usage.sklearn: 32\n    usage.dask: 158\n    "
    ...


def rint(
    _0: object, /, *, out: Union[dask.dataframe.core.DataFrame, numpy.ndarray] = ...
):
    "\n    usage.skimage: 2\n    usage.xarray: 2\n    usage.dask: 40\n    "
    ...


def clip(a: object, a_min: object, a_max: object):
    "\n    usage.skimage: 61\n    usage.sklearn: 24\n    usage.dask: 23\n    "
    ...


def power(
    _0: Union[numpy.ndarray, dask.array.core.Array, int, numpy.float64, float],
    _1: Union[int, float, dask.array.core.Array, numpy.ndarray],
    /,
):
    "\n    usage.skimage: 11\n    usage.sklearn: 3\n    usage.dask: 21\n    "
    ...


def log10(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    "\n    usage.skimage: 4\n    usage.xarray: 2\n    usage.sklearn: 3\n    usage.dask: 40\n    "
    ...


def load(
    file: Literal[
        "/var/folders/xn/05ktz3056kqd9n8frgd6236h0000gn/T/t",
        "/Users/saul/Downloads/scikit-image-0.17.0/skimage/",
    ]
):
    "\n    usage.skimage: 28\n    usage.dask: 7\n    "
    ...


def meshgrid(*xi: Literal["v", "t"]):
    "\n    usage.skimage: 28\n    usage.xarray: 6\n    usage.sklearn: 2\n    usage.dask: 5\n    "
    ...


def dstack(tup: object):
    "\n    usage.skimage: 12\n    usage.sklearn: 4\n    usage.dask: 8\n    "
    ...


def nonzero(a: numpy.ndarray):
    "\n    usage.skimage: 22\n    usage.xarray: 4\n    usage.sklearn: 7\n    usage.dask: 2\n    "
    ...


def cbrt(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    "\n    usage.skimage: 4\n    usage.dask: 37\n    "
    ...


def hypot(_0: object, _1: object, /):
    "\n    usage.skimage: 13\n    usage.xarray: 2\n    usage.dask: 112\n    "
    ...


def arctan2(_0: object, _1: object, /):
    "\n    usage.skimage: 8\n    usage.xarray: 2\n    usage.dask: 112\n    "
    ...


def where(_0: object, _1: object = ..., _2: object = ..., /):
    "\n    usage.skimage: 26\n    usage.xarray: 23\n    usage.sklearn: 44\n    usage.dask: 59\n    "
    ...


def cos(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    "\n    usage.skimage: 48\n    usage.xarray: 14\n    usage.sklearn: 11\n    usage.dask: 42\n    "
    ...


def sin(_0: object, /, *, out: object = ...):
    "\n    usage.skimage: 47\n    usage.xarray: 21\n    usage.sklearn: 22\n    usage.dask: 52\n    "
    ...


def ascontiguousarray(a: Union[numpy.ndarray, List[Union[List[int], float, int]]]):
    "\n    usage.skimage: 67\n    usage.sklearn: 21\n    usage.dask: 4\n    "
    ...


def swapaxes(a: numpy.ndarray, axis1: int, axis2: int):
    "\n    usage.skimage: 4\n    usage.xarray: 8\n    usage.sklearn: 2\n    usage.dask: 4\n    "
    ...


def ravel(a: object):
    "\n    usage.skimage: 12\n    usage.xarray: 44\n    usage.sklearn: 43\n    usage.dask: 1\n    "
    ...


def squeeze(a: Union[numpy.ndarray, float, numpy.float64, int, List[float]]):
    "\n    usage.skimage: 16\n    usage.sklearn: 18\n    usage.dask: 3\n    "
    ...


def ones_like(
    a: Union[
        numpy.ma.core.MaskedArray,
        numpy.ndarray,
        xarray.core.variable.Variable,
        numpy.float64,
    ]
):
    "\n    usage.skimage: 26\n    usage.xarray: 4\n    usage.sklearn: 19\n    usage.dask: 5\n    "
    ...


def can_cast(
    _0: Union[numpy.ndarray, numpy.dtype, int, float],
    _1: Union[numpy.dtype, Type[bool]],
    /,
    *,
    casting: Literal["unsafe", "safe", "same_kind"] = ...,
):
    "\n    usage.skimage: 9\n    usage.dask: 19\n    "
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
    "\n    usage.skimage: 129\n    usage.xarray: 11\n    usage.sklearn: 131\n    usage.dask: 137\n    "
    ...


def min_scalar_type(
    _0: Union[numpy.ndarray, dask.array.core.Array, int, numpy.int64, numpy.float64], /
):
    "\n    usage.skimage: 5\n    usage.dask: 3\n    "
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
    "\n    usage.skimage: 68\n    usage.xarray: 14\n    usage.sklearn: 216\n    usage.dask: 30\n    "
    ...


def zeros_like(
    a: Union[numpy.ndarray, Tuple[int, ...]],
    dtype: Union[numpy.dtype, type] = ...,
    shape: Union[int, Tuple[int, int]] = ...,
    order: Literal["F", "C"] = ...,
):
    "\n    usage.skimage: 70\n    usage.xarray: 43\n    usage.sklearn: 15\n    usage.dask: 8\n    "
    ...


def full(
    shape: Union[Tuple[Union[int, None], ...], List[int], numpy.ndarray, int],
    fill_value: object,
):
    "\n    usage.skimage: 36\n    usage.xarray: 10\n    usage.sklearn: 41\n    usage.dask: 10\n    "
    ...


def loadtxt(
    fname: Literal[
        "/usr/local/Caskroom/miniconda/base/envs/python-rec",
        "/Users/saul/Downloads/scikit-image-0.17.0/skimage/",
    ]
):
    "\n    usage.skimage: 1\n    usage.sklearn: 5\n    "
    ...


def logical_and(_0: object, _1: object, /):
    "\n    usage.skimage: 13\n    usage.xarray: 2\n    usage.sklearn: 1\n    usage.dask: 112\n    "
    ...


def deg2rad(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    "\n    usage.skimage: 18\n    usage.xarray: 2\n    usage.dask: 40\n    "
    ...


def rad2deg(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    "\n    usage.skimage: 6\n    usage.xarray: 2\n    usage.dask: 40\n    "
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
    "\n    usage.skimage: 16\n    usage.xarray: 87\n    usage.sklearn: 20\n    usage.dask: 200\n    "
    ...


def percentile(
    a: numpy.ndarray, q: Union[numpy.ndarray, numpy.float64, float, int, List[int]]
):
    "\n    usage.skimage: 11\n    usage.xarray: 20\n    usage.sklearn: 9\n    usage.dask: 8\n    "
    ...


def logical_not(
    _0: object, /, *, out: Union[dask.dataframe.core.DataFrame, numpy.ndarray] = ...
):
    "\n    usage.skimage: 14\n    usage.xarray: 10\n    usage.sklearn: 8\n    usage.dask: 31\n    "
    ...


def isscalar(element: object):
    "\n    usage.skimage: 67\n    usage.xarray: 40\n    usage.sklearn: 5\n    usage.dask: 537\n    "
    ...


def ceil(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    "\n    usage.skimage: 31\n    usage.xarray: 5\n    usage.sklearn: 17\n    usage.dask: 45\n    "
    ...


def minimum(_0: object, _1: object, /, *, out: numpy.ndarray = ...):
    "\n    usage.skimage: 9\n    usage.xarray: 4\n    usage.sklearn: 11\n    usage.dask: 115\n    "
    ...


def dot(_0: object, _1: object, /, *, out: numpy.ndarray = ...):
    "\n    usage.skimage: 1\n    usage.sklearn: 322\n    usage.dask: 13\n    "
    ...


def diag(v: Union[dask.array.core.Array, numpy.ndarray]):
    "\n    usage.skimage: 5\n    usage.sklearn: 28\n    usage.dask: 8\n    "
    ...


def arcsin(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    "\n    usage.skimage: 1\n    usage.xarray: 2\n    usage.dask: 40\n    "
    ...


def ellipkinc(_0: numpy.float64, _1: float, /):
    "\n    usage.skimage: 1\n    "
    ...


def ellipeinc(_0: numpy.float64, _1: float, /):
    "\n    usage.skimage: 1\n    "
    ...


def transpose(a: object):
    "\n    usage.skimage: 21\n    usage.xarray: 6\n    usage.sklearn: 6\n    usage.dask: 25\n    "
    ...


def shape(a: Union[dask.array.core.Array, numpy.ma.core.MaskedArray, numpy.ndarray]):
    "\n    usage.skimage: 1\n    usage.xarray: 11\n    usage.sklearn: 15\n    usage.dask: 1\n    "
    ...


def promote_types(_0: numpy.dtype, _1: Union[Type[float], numpy.dtype], /):
    "\n    usage.skimage: 1\n    usage.dask: 7\n    "
    ...


def bincount(
    _0: Union[List[int], numpy.ndarray, dask.array.core.Array],
    /,
    *,
    minlength: int = ...,
    weights: Union[List[Union[int, float]], numpy.ndarray, None] = ...,
):
    "\n    usage.skimage: 12\n    usage.sklearn: 36\n    usage.dask: 6\n    "
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
    "\n    usage.skimage: 7\n    usage.dask: 11\n    "
    ...


def interp(
    x: Union[numpy.ndarray, numpy.flatiter],
    xp: numpy.ndarray,
    fp: Union[
        numpy.ndarray, List[Union[pandas._libs.tslibs.nattype.NaTType, float, None]]
    ],
):
    "\n    usage.skimage: 6\n    usage.dask: 8\n    "
    ...


def polyfit(x: numpy.ndarray, y: numpy.ndarray, deg: int):
    "\n    usage.skimage: 1\n    "
    ...


def pad(array: Union[numpy.ndarray, List[Union[List[int], int]]], pad_width: object):
    "\n    usage.skimage: 126\n    usage.xarray: 44\n    usage.dask: 21\n    "
    ...


def product(*args: Literal["v", "t"]):
    "\n    usage.skimage: 14\n    usage.sklearn: 1\n    "
    ...


def apply_along_axis(
    func1d: Union[int, sklearn.gaussian_process.kernels.PairwiseKernel, Callable],
    axis: Union[Callable, int],
    arr: Union[int, numpy.ndarray],
    *args: Literal["v", "t"],
):
    "\n    usage.skimage: 8\n    usage.sklearn: 5\n    usage.dask: 4\n    "
    ...


def count_nonzero(a: Union[str, List[bool], numpy.ndarray]):
    "\n    usage.skimage: 9\n    usage.sklearn: 12\n    usage.dask: 21\n    "
    ...


def cumsum(
    a: object,
    axis: Union[None, int] = ...,
    out: Union[
        dask.array.core.Array, dask.dataframe.core.DataFrame, numpy.ndarray
    ] = ...,
    dtype: Type[numpy.float64] = ...,
):
    "\n    usage.skimage: 29\n    usage.xarray: 10\n    usage.sklearn: 16\n    usage.dask: 39\n    "
    ...


def take_along_axis(arr: numpy.ndarray, indices: numpy.ndarray, axis: int):
    "\n    usage.skimage: 1\n    usage.dask: 3\n    "
    ...


def square(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    "\n    usage.skimage: 7\n    usage.xarray: 2\n    usage.dask: 42\n    "
    ...


def mean(
    a: object,
    axis: Union[int, Tuple[Union[int, None], ...], None] = ...,
    out: Union[dask.dataframe.core.Scalar, dask.dataframe.core.Series] = ...,
    keepdims: bool = ...,
    dtype: Union[Literal["float32", "i8", "f8"], None, type] = ...,
):
    "\n    usage.skimage: 61\n    usage.xarray: 32\n    usage.sklearn: 102\n    usage.dask: 116\n    "
    ...


def log2(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    "\n    usage.skimage: 5\n    usage.xarray: 2\n    usage.sklearn: 9\n    usage.dask: 37\n    "
    ...


def allclose(
    a: object,
    b: object,
    rtol: Union[float, int] = ...,
    atol: float = ...,
    equal_nan: bool = ...,
):
    "\n    usage.skimage: 33\n    usage.xarray: 22\n    usage.sklearn: 45\n    usage.dask: 83\n    "
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
    "\n    usage.skimage: 28\n    usage.sklearn: 34\n    usage.dask: 12\n    "
    ...


def hstack(tup: object):
    "\n    usage.skimage: 27\n    usage.xarray: 1\n    usage.sklearn: 89\n    usage.dask: 7\n    "
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
    "\n    usage.skimage: 18\n    usage.xarray: 11\n    usage.sklearn: 44\n    usage.dask: 36\n    "
    ...


def logspace(
    start: Union[numpy.float64, int, float],
    stop: Union[numpy.float64, int, float],
    num: int,
):
    "\n    usage.skimage: 2\n    usage.sklearn: 11\n    "
    ...


def logical_or(_0: object, _1: object, /, *, out: numpy.ndarray = ...):
    "\n    usage.skimage: 3\n    usage.xarray: 2\n    usage.sklearn: 4\n    usage.dask: 112\n    "
    ...


def isinf(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    "\n    usage.skimage: 2\n    usage.xarray: 2\n    usage.sklearn: 10\n    usage.dask: 31\n    "
    ...


def delete(arr: numpy.ndarray, obj: Union[numpy.ndarray, Tuple[Union[None, int], ...]]):
    "\n    usage.skimage: 3\n    usage.sklearn: 2\n    "
    ...


def split(ary: numpy.ndarray, indices_or_sections: Union[numpy.ndarray, int]):
    "\n    usage.skimage: 1\n    usage.sklearn: 4\n    "
    ...


def atleast_1d(*arys: Literal["v", "t"]):
    "\n    usage.skimage: 11\n    usage.xarray: 24\n    usage.sklearn: 38\n    usage.dask: 4\n    "
    ...


def isclose(
    a: Union[numpy.float64, numpy.ndarray, float],
    b: Union[int, numpy.ndarray, float, numpy.float32, numpy.float64],
    rtol: float = ...,
    atol: Union[int, float] = ...,
    equal_nan: bool = ...,
):
    "\n    usage.skimage: 3\n    usage.xarray: 12\n    usage.sklearn: 5\n    usage.dask: 3\n    "
    ...


def gradient(
    f: Union[float, int, numpy.ndarray, xarray.core.dataarray.DataArray],
    *varargs: Literal["v", "t"],
):
    "\n    usage.skimage: 8\n    usage.xarray: 5\n    usage.dask: 14\n    "
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
    "\n    usage.skimage: 10\n    usage.xarray: 5\n    usage.sklearn: 23\n    usage.dask: 35\n    "
    ...


def arctan(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    "\n    usage.skimage: 3\n    usage.xarray: 2\n    usage.sklearn: 2\n    usage.dask: 40\n    "
    ...


def sort(
    a: Union[
        dask.array.core.Array, numpy.ndarray, List[Union[int, float, numpy.float64]]
    ]
):
    "\n    usage.skimage: 14\n    usage.xarray: 2\n    usage.sklearn: 31\n    usage.dask: 14\n    "
    ...


def spacing(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    "\n    usage.skimage: 1\n    usage.dask: 37\n    "
    ...


def isfinite(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    "\n    usage.skimage: 7\n    usage.xarray: 6\n    usage.sklearn: 19\n    usage.dask: 31\n    "
    ...


def diff(
    a: Union[numpy.ndarray, List[Union[numpy.float64, numpy.int64]]],
    n: int = ...,
    axis: int = ...,
):
    "\n    usage.skimage: 15\n    usage.xarray: 11\n    usage.sklearn: 17\n    usage.dask: 11\n    "
    ...


def flatnonzero(a: numpy.ndarray):
    "\n    usage.skimage: 6\n    usage.xarray: 2\n    usage.sklearn: 24\n    usage.dask: 2\n    "
    ...


def copy(a: Union[numpy.ndarray, numpy.float64]):
    "\n    usage.skimage: 14\n    usage.sklearn: 23\n    "
    ...


def atleast_2d(*arys: Literal["v", "t"]):
    "\n    usage.skimage: 7\n    usage.xarray: 2\n    usage.sklearn: 25\n    usage.dask: 3\n    "
    ...


def rot90(m: numpy.ndarray):
    "\n    usage.skimage: 7\n    "
    ...


def roll(
    a: Union[numpy.ndarray, List[Union[int, float]]], shift: Union[int, Tuple[int, int]]
):
    "\n    usage.skimage: 14\n    usage.xarray: 1\n    usage.dask: 5\n    "
    ...


def indices(dimensions: Union[Tuple[Union[int, numpy.int64, None], ...], generator]):
    "\n    usage.skimage: 6\n    usage.sklearn: 2\n    usage.dask: 8\n    "
    ...


def tri(N: int, M: int = ..., k: int = ...):
    "\n    usage.skimage: 9\n    "
    ...


def less(_0: object, _1: object, /):
    "\n    usage.skimage: 3\n    usage.xarray: 1\n    usage.sklearn: 5\n    usage.dask: 109\n    "
    ...


def prod(
    a: object,
    axis: Union[int, Tuple[Union[None, int], ...], None] = ...,
    out: Union[dask.dataframe.core.Scalar, dask.dataframe.core.Series] = ...,
    keepdims: bool = ...,
    dtype: Union[Literal["i8", "f8", "i4", "f4"], type] = ...,
):
    "\n    usage.skimage: 9\n    usage.xarray: 15\n    usage.sklearn: 8\n    usage.dask: 134\n    "
    ...


def true_divide(_0: object, _1: object, /, *, out: numpy.ndarray = ...):
    "\n    usage.skimage: 2\n    usage.sklearn: 2\n    usage.dask: 32\n    "
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
    "\n    usage.skimage: 18\n    usage.sklearn: 1\n    usage.dask: 12\n    "
    ...


def apply_over_axes(
    func: Callable, a: numpy.ndarray, axes: Union[int, Tuple[Union[int, None], ...]]
):
    "\n    usage.skimage: 10\n    usage.dask: 5\n    "
    ...


def tile(
    A: Union[
        list, numpy.ndarray, int, numpy.float64, Tuple[Union[numpy.ndarray, int], ...]
    ],
    reps: Union[int, Tuple[int, ...], List[int]],
):
    "\n    usage.skimage: 15\n    usage.xarray: 5\n    usage.sklearn: 16\n    usage.dask: 18\n    "
    ...


def real(val: object):
    "\n    usage.skimage: 8\n    usage.xarray: 1\n    usage.sklearn: 1\n    usage.dask: 32\n    "
    ...


def imag(val: object):
    "\n    usage.skimage: 1\n    usage.xarray: 1\n    usage.dask: 31\n    "
    ...


def sign(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    "\n    usage.skimage: 4\n    usage.xarray: 3\n    usage.sklearn: 24\n    usage.dask: 38\n    "
    ...


def subtract(
    _0: Union[numpy.ndarray, numpy.float64, dask.array.core.Array, int],
    _1: Union[int, dask.array.core.Array, numpy.ndarray],
    /,
    *,
    dtype: numpy.dtype = ...,
):
    "\n    usage.skimage: 11\n    usage.xarray: 2\n    usage.sklearn: 1\n    usage.dask: 21\n    "
    ...


def ix_(*args: Literal["v", "t"]):
    "\n    usage.skimage: 2\n    usage.xarray: 3\n    usage.sklearn: 2\n    "
    ...


def convolve(a: numpy.ndarray, v: List[float], mode: Literal["valid"]):
    "\n    usage.skimage: 1\n    "
    ...


def invert(_0: Union[numpy.ndarray, dask.array.core.Array, List[bool]], /):
    "\n    usage.skimage: 7\n    usage.dask: 8\n    "
    ...


def array_equal(
    a1: Union[numpy.ndarray, Tuple[float, float, float], List[Union[float, int]]],
    a2: Union[
        numpy.ndarray,
        Tuple[int, ...],
        List[Union[numpy.float32, float, int, numpy.float64]],
    ],
):
    "\n    usage.skimage: 5\n    usage.xarray: 3\n    usage.sklearn: 12\n    usage.dask: 4\n    "
    ...


def reciprocal(
    _0: object, /, *, out: Union[dask.dataframe.core.DataFrame, numpy.ndarray] = ...
):
    "\n    usage.skimage: 1\n    usage.dask: 37\n    "
    ...


def insert(
    arr: numpy.ndarray,
    obj: Union[slice[int, int, int], int, List[int]],
    values: Union[numpy.ndarray, int],
):
    "\n    usage.skimage: 3\n    usage.sklearn: 1\n    usage.dask: 11\n    "
    ...


def full_like(
    a: object,
    fill_value: object,
    dtype: Union[type, Literal["i8", "f8", "i4", "f4"], numpy.dtype, None] = ...,
    shape: Tuple[int, ...] = ...,
):
    "\n    usage.skimage: 1\n    usage.xarray: 10\n    usage.sklearn: 3\n    usage.dask: 50\n    "
    ...


def sctype2char(sctype: numpy.dtype):
    "\n    usage.skimage: 2\n    "
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
    "\n    usage.skimage: 4\n    usage.dask: 20\n    "
    ...


def fromfile(_0: _io.TextIOWrapper, /, *, sep: Literal[" "]):
    "\n    usage.skimage: 1\n    "
    ...


def median(
    a: Union[Tuple[Union[numpy.int64, int], ...], numpy.ndarray],
    axis: Union[int, List[int], Tuple[int, ...]] = ...,
    keepdims: bool = ...,
):
    "\n    usage.skimage: 5\n    usage.xarray: 1\n    usage.sklearn: 15\n    usage.dask: 17\n    "
    ...


def asfortranarray(a: Union[numpy.ndarray, List[List[int]]]):
    "\n    usage.skimage: 1\n    usage.sklearn: 20\n    usage.dask: 2\n    "
    ...


def cross(a: numpy.ndarray, b: numpy.ndarray):
    "\n    usage.skimage: 5\n    "
    ...


def einsum(*operands: Literal["v", "t"]):
    "\n    usage.skimage: 1\n    usage.xarray: 80\n    usage.sklearn: 10\n    usage.dask: 136\n    "
    ...


def nan_to_num(x: object):
    "\n    usage.skimage: 1\n    usage.sklearn: 2\n    usage.dask: 23\n    "
    ...


def frombuffer(
    _0: Union[bytes, array.array, numpy.ndarray],
    /,
    *,
    dtype: Union[type, Literal["int8"]] = ...,
):
    "\n    usage.skimage: 1\n    usage.sklearn: 8\n    usage.dask: 1\n    "
    ...


def fliplr(m: numpy.ndarray):
    "\n    usage.skimage: 5\n    usage.dask: 1\n    "
    ...


def tril(m: numpy.ndarray):
    "\n    usage.skimage: 1\n    usage.sklearn: 1\n    usage.dask: 7\n    "
    ...


def flip(m: object, axis: int):
    "\n    usage.skimage: 3\n    usage.dask: 5\n    "
    ...


def flipud(m: numpy.ndarray):
    "\n    usage.skimage: 2\n    usage.xarray: 2\n    usage.dask: 1\n    "
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
    "\n    usage.skimage: 1\n    usage.xarray: 3\n    "
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
    "\n    usage.skimage: 7\n    usage.xarray: 94\n    usage.sklearn: 10\n    usage.dask: 80\n    "
    ...


def ptp(a: numpy.ndarray):
    "\n    usage.skimage: 10\n    usage.sklearn: 2\n    usage.dask: 2\n    "
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
    "\n    usage.skimage: 5\n    usage.xarray: 4\n    usage.dask: 14\n    "
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
    "\n    usage.skimage: 18\n    usage.dask: 3\n    "
    ...


def logical_xor(_0: object, _1: object, /, *, out: numpy.ndarray = ...):
    "\n    usage.skimage: 1\n    usage.xarray: 2\n    usage.dask: 112\n    "
    ...


def in1d(
    ar1: Union[numpy.ndarray, numpy.flatiter],
    ar2: Union[numpy.ndarray, Tuple[int, int], List[numpy.float64]],
):
    "\n    usage.skimage: 2\n    usage.sklearn: 13\n    usage.dask: 1\n    "
    ...


def take(
    a: Union[numpy.ndarray, List[Union[Literal["three", "two", "one"], int]]],
    indices: Union[List[int], int, numpy.ndarray],
):
    "\n    usage.skimage: 1\n    usage.xarray: 11\n    usage.sklearn: 8\n    usage.dask: 3\n    "
    ...


def lexsort(_0: Tuple[Union[numpy.ndarray, xarray.core.dataarray.DataArray], ...], /):
    "\n    usage.skimage: 1\n    usage.xarray: 2\n    "
    ...


def fmax(_0: object, _1: object, /):
    "\n    usage.skimage: 3\n    usage.xarray: 2\n    usage.dask: 112\n    "
    ...


def fix(x: Union[numpy.ndarray, numpy.float64, float, xarray.core.dataarray.DataArray]):
    "\n    usage.skimage: 2\n    usage.xarray: 1\n    usage.dask: 3\n    "
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
    "\n    usage.skimage: 1\n    usage.xarray: 5\n    usage.dask: 23\n    "
    ...


def atleast_3d(*arys: Literal["v", "t"]):
    "\n    usage.skimage: 11\n    usage.sklearn: 6\n    usage.dask: 3\n    "
    ...


def iscomplexobj(x: Union[dask.array.core.Array, numpy.ndarray]):
    "\n    usage.skimage: 4\n    usage.sklearn: 1\n    usage.dask: 2\n    "
    ...


def conjugate(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    "\n    usage.skimage: 2\n    usage.xarray: 2\n    usage.sklearn: 1\n    usage.dask: 45\n    "
    ...


def angle(z: object):
    "\n    usage.skimage: 3\n    usage.xarray: 2\n    usage.dask: 25\n    "
    ...


def require(a: numpy.ndarray, requirements: Union[Literal["W"], List[Literal["C"]]]):
    "\n    usage.skimage: 1\n    usage.sklearn: 4\n    "
    ...


def tanh(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    "\n    usage.skimage: 2\n    usage.xarray: 2\n    usage.sklearn: 3\n    usage.dask: 40\n    "
    ...


def ndim(a: Union[numpy.float64, numpy.ndarray]):
    "\n    usage.skimage: 4\n    usage.sklearn: 4\n    "
    ...


def searchsorted(a: Union[List[int], Tuple[int, ...], numpy.ndarray], v: object):
    "\n    usage.skimage: 3\n    usage.xarray: 1\n    usage.sklearn: 38\n    usage.dask: 16\n    "
    ...


def fill_diagonal(a: numpy.ndarray, val: Union[float, int]):
    "\n    usage.skimage: 1\n    usage.sklearn: 10\n    "
    ...


def array2string(a: numpy.ndarray, separator: Literal[", "]):
    "\n    usage.skimage: 1\n    "
    ...


def std(
    a: object,
    axis: Union[int, Tuple[Union[int, None], ...], None] = ...,
    out: Union[dask.dataframe.core.Scalar, dask.dataframe.core.Series] = ...,
    ddof: int = ...,
    keepdims: bool = ...,
):
    "\n    usage.skimage: 1\n    usage.xarray: 3\n    usage.sklearn: 6\n    usage.dask: 92\n    "
    ...


def hamming(M: int):
    "\n    usage.skimage: 1\n    "
    ...


def hanning(M: int):
    "\n    usage.skimage: 1\n    "
    ...


def around(a: Union[numpy.ndarray, Tuple[numpy.float64, numpy.float64]]):
    "\n    usage.skimage: 1\n    usage.xarray: 4\n    usage.dask: 1\n    "
    ...


def alltrue(*args: Literal["v", "t"]):
    "\n    usage.skimage: 2\n    usage.dask: 1\n    "
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
    "\n    usage.skimage: 2\n    usage.sklearn: 44\n    "
    ...


def isnat(_0: Union[numpy.ndarray, dask.array.core.Array], /):
    "\n    usage.xarray: 6\n    "
    ...


def get_printoptions():
    "\n    usage.xarray: 3\n    "
    ...


def broadcast_arrays(*args: Literal["v", "t"]):
    "\n    usage.xarray: 3\n    usage.dask: 10\n    "
    ...


def broadcast_to(
    array: Union[numpy.ndarray, int, numpy.float64, float],
    shape: Union[List[int], Tuple[Union[int, numpy.int64, None], ...]],
):
    "\n    usage.xarray: 25\n    usage.dask: 23\n    "
    ...


def nanmean(
    a: numpy.ndarray,
    axis: Union[int, Tuple[Union[int, None], ...], None] = ...,
    keepdims: bool = ...,
    dtype: Union[None, type] = ...,
):
    "\n    usage.xarray: 21\n    usage.sklearn: 3\n    usage.dask: 11\n    "
    ...


def nanstd(
    a: numpy.ndarray,
    axis: Union[int, Tuple[Union[int, None], ...], None] = ...,
    keepdims: bool = ...,
    dtype: None = ...,
    ddof: int = ...,
):
    "\n    usage.xarray: 3\n    usage.sklearn: 1\n    usage.dask: 49\n    "
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
    "\n    usage.xarray: 5\n    usage.dask: 28\n    "
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
    "\n    usage.xarray: 4\n    usage.dask: 28\n    "
    ...


def expand_dims(a: numpy.ndarray, axis: int):
    "\n    usage.xarray: 5\n    usage.sklearn: 2\n    usage.dask: 2\n    "
    ...


def nanquantile(
    a: numpy.ndarray,
    q: numpy.ndarray,
    axis: numpy.ndarray,
    interpolation: Literal["linear"],
):
    "\n    usage.xarray: 2\n    "
    ...


def nanpercentile(
    a: numpy.ndarray, q: Union[Tuple[float, float], numpy.float64, numpy.ndarray]
):
    "\n    usage.xarray: 20\n    usage.sklearn: 1\n    "
    ...


def quantile(
    a: numpy.ndarray,
    q: numpy.ndarray,
    axis: numpy.ndarray,
    interpolation: Literal["linear"],
):
    "\n    usage.xarray: 1\n    "
    ...


def repeat(
    a: Union[numpy.ndarray, numpy.float64, float, int, numpy.int64],
    repeats: Union[int, numpy.ndarray, numpy.int64],
):
    "\n    usage.xarray: 4\n    usage.sklearn: 33\n    usage.dask: 4\n    "
    ...


def isin(
    element: Union[numpy.ndarray, dask.array.core.Array],
    test_elements: Union[dask.array.core.Array, numpy.ndarray, List[int]],
):
    "\n    usage.xarray: 5\n    usage.dask: 4\n    "
    ...


def nansum(
    a: Union[numpy.ndarray, numpy.ma.core.MaskedArray],
    axis: Union[int, Tuple[Union[int, None], ...], None] = ...,
    dtype: Union[numpy.dtype, Literal["i8", "f8"]] = ...,
    keepdims: bool = ...,
):
    "\n    usage.xarray: 8\n    usage.sklearn: 3\n    usage.dask: 135\n    "
    ...


def nanmax(
    a: numpy.ndarray = ...,
    axis: Union[None, int, Tuple[Union[int, None], ...]] = ...,
    keepdims: bool = ...,
    *,
    computing_meta: bool = ...,
):
    "\n    usage.xarray: 17\n    usage.sklearn: 1\n    usage.dask: 106\n    "
    ...


def nanmin(
    a: numpy.ndarray = ...,
    axis: Union[None, int, Tuple[Union[None, int], ...]] = ...,
    keepdims: bool = ...,
    *,
    computing_meta: bool = ...,
):
    "\n    usage.xarray: 16\n    usage.sklearn: 2\n    usage.dask: 106\n    "
    ...


def nancumsum(a: numpy.ndarray, axis: Union[int, None] = ..., dtype: None = ...):
    "\n    usage.xarray: 1\n    usage.dask: 16\n    "
    ...


def nancumprod(a: numpy.ndarray, axis: Union[int, None] = ..., dtype: None = ...):
    "\n    usage.xarray: 1\n    usage.dask: 16\n    "
    ...


def var(
    a: object,
    axis: Union[int, Tuple[Union[None, int], ...], None] = ...,
    out: Union[dask.dataframe.core.Scalar, dask.dataframe.core.Series] = ...,
    ddof: int = ...,
    keepdims: bool = ...,
):
    "\n    usage.xarray: 22\n    usage.sklearn: 22\n    usage.dask: 96\n    "
    ...


def nanvar(
    a: numpy.ndarray,
    axis: Union[int, Tuple[Union[int, None], ...], None] = ...,
    keepdims: bool = ...,
    dtype: Union[Type[float], None] = ...,
    ddof: int = ...,
):
    "\n    usage.xarray: 17\n    usage.sklearn: 3\n    usage.dask: 49\n    "
    ...


def nanmedian(a: numpy.ndarray, axis: Union[int, List[int], None]):
    "\n    usage.xarray: 3\n    usage.sklearn: 1\n    usage.dask: 8\n    "
    ...


def datetime_data(_0: numpy.dtype, /):
    "\n    usage.xarray: 1\n    "
    ...


def trapz(
    y: Union[numpy.ndarray, dask.array.core.Array, xarray.core.dataarray.DataArray],
    x: Union[numpy.ndarray, xarray.core.dataarray.DataArray],
):
    "\n    usage.xarray: 4\n    usage.sklearn: 1\n    "
    ...


def nanprod(
    a: numpy.ndarray,
    axis: Union[int, Tuple[Union[int, None], ...], None] = ...,
    dtype: Union[Literal["i8", "f8"], None] = ...,
    out: None = ...,
    keepdims: bool = ...,
):
    "\n    usage.xarray: 9\n    usage.dask: 71\n    "
    ...


def greater(_0: object, _1: object, /):
    "\n    usage.xarray: 1\n    usage.dask: 109\n    "
    ...


def frexp(_0: object, /):
    "\n    usage.xarray: 7\n    usage.dask: 9\n    "
    ...


def arccos(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    "\n    usage.xarray: 2\n    usage.dask: 40\n    "
    ...


def arccosh(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    "\n    usage.xarray: 2\n    usage.dask: 38\n    "
    ...


def arcsinh(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    "\n    usage.xarray: 2\n    usage.dask: 38\n    "
    ...


def arctanh(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    "\n    usage.xarray: 2\n    usage.dask: 40\n    "
    ...


def copysign(_0: object, _1: object, /):
    "\n    usage.xarray: 2\n    usage.dask: 112\n    "
    ...


def cosh(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    "\n    usage.xarray: 2\n    usage.dask: 38\n    "
    ...


def degrees(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    "\n    usage.xarray: 2\n    usage.dask: 38\n    "
    ...


def expm1(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    "\n    usage.xarray: 2\n    usage.dask: 41\n    "
    ...


def fabs(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    "\n    usage.xarray: 2\n    usage.sklearn: 1\n    usage.dask: 39\n    "
    ...


def greater_equal(_0: object, _1: object, /):
    "\n    usage.xarray: 1\n    usage.dask: 111\n    "
    ...


def fmin(_0: object, _1: object, /):
    "\n    usage.xarray: 2\n    usage.dask: 112\n    "
    ...


def fmod(_0: object, _1: object, /):
    "\n    usage.xarray: 2\n    usage.dask: 112\n    "
    ...


def iscomplex(x: object):
    "\n    usage.xarray: 1\n    usage.dask: 28\n    "
    ...


def isreal(x: object):
    "\n    usage.xarray: 1\n    usage.sklearn: 1\n    usage.dask: 28\n    "
    ...


def ldexp(_0: object, _1: object, /):
    "\n    usage.xarray: 2\n    usage.dask: 88\n    "
    ...


def log1p(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    "\n    usage.xarray: 2\n    usage.sklearn: 1\n    usage.dask: 40\n    "
    ...


def logaddexp(_0: object, _1: object, /):
    "\n    usage.xarray: 2\n    usage.sklearn: 7\n    usage.dask: 112\n    "
    ...


def logaddexp2(_0: object, _1: object, /):
    "\n    usage.xarray: 2\n    usage.dask: 112\n    "
    ...


def nextafter(_0: object, _1: object, /):
    "\n    usage.xarray: 2\n    usage.sklearn: 2\n    usage.dask: 112\n    "
    ...


def radians(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    "\n    usage.xarray: 2\n    usage.dask: 40\n    "
    ...


def signbit(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    "\n    usage.xarray: 2\n    usage.dask: 31\n    "
    ...


def sinh(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    "\n    usage.xarray: 2\n    usage.dask: 40\n    "
    ...


def tan(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    "\n    usage.xarray: 2\n    usage.dask: 40\n    "
    ...


def trunc(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    "\n    usage.xarray: 2\n    usage.dask: 40\n    "
    ...


def outer(
    a: Union[numpy.ndarray, numpy.float64], b: Union[numpy.ndarray, numpy.float64]
):
    "\n    usage.sklearn: 6\n    usage.dask: 4\n    "
    ...


def compress(condition: Union[numpy.ndarray, List[bool]], a: numpy.ndarray):
    "\n    usage.sklearn: 4\n    usage.dask: 4\n    "
    ...


def size(a: Union[Tuple[Union[int, None], ...], numpy.ndarray]):
    "\n    usage.sklearn: 18\n    "
    ...


def diag_indices_from(arr: numpy.ndarray):
    "\n    usage.sklearn: 3\n    "
    ...


def triu_indices(n: int, k: int):
    "\n    usage.sklearn: 2\n    "
    ...


def append(arr: numpy.ndarray, values: Union[float, numpy.ndarray]):
    "\n    usage.sklearn: 15\n    usage.dask: 1\n    "
    ...


def argpartition(a: numpy.ndarray, kth: Union[int, numpy.int64], axis: int):
    "\n    usage.sklearn: 3\n    usage.dask: 1\n    "
    ...


def array_equiv(a1: numpy.ndarray, a2: numpy.ndarray):
    "\n    usage.sklearn: 1\n    "
    ...


def array_split(ary: numpy.ndarray, indices_or_sections: int):
    "\n    usage.sklearn: 1\n    "
    ...


def setdiff1d(ar1: numpy.ndarray, ar2: numpy.ndarray):
    "\n    usage.sklearn: 10\n    "
    ...


def average(
    a: Union[numpy.ndarray, List[int]],
    axis: int = ...,
    weights: Union[
        numpy.ndarray, None, List[Union[numpy.float64, numpy.int64, float, int]]
    ] = ...,
):
    "\n    usage.sklearn: 69\n    usage.dask: 2\n    "
    ...


def cov(m: object):
    "\n    usage.sklearn: 4\n    usage.dask: 11\n    "
    ...


def trace(a: numpy.ndarray):
    "\n    usage.sklearn: 4\n    "
    ...


def union1d(
    ar1: Union[dask.array.core.Array, numpy.ndarray],
    ar2: Union[dask.array.core.Array, numpy.ndarray],
):
    "\n    usage.sklearn: 5\n    usage.dask: 2\n    "
    ...


def matmul(_0: object, _1: object, /):
    "\n    usage.sklearn: 1\n    usage.dask: 12\n    "
    ...


def fromiter(
    _0: Union[generator, itertools.chain],
    /,
    *,
    dtype: Union[Type[numpy.float64], Literal["float64"]],
    count: int = ...,
):
    "\n    usage.sklearn: 3\n    "
    ...


def unpackbits(_0: numpy.ndarray, /):
    "\n    usage.sklearn: 1\n    "
    ...


def resize(a: numpy.ndarray, new_shape: Union[Tuple[int, int], int]):
    "\n    usage.sklearn: 6\n    "
    ...


def identity(n: int):
    "\n    usage.sklearn: 1\n    "
    ...


def find_common_type(array_types: List[numpy.dtype], scalar_types: list):
    "\n    usage.sklearn: 2\n    "
    ...


def gammaln(_0: Union[float, numpy.ndarray], /):
    "\n    usage.sklearn: 5\n    "
    ...


def psi(_0: Union[int, numpy.int64, numpy.float64, numpy.ndarray], /):
    "\n    usage.sklearn: 9\n    "
    ...


def expit(_0: Union[numpy.ndarray, numpy.float64], /, *, out: numpy.ndarray = ...):
    "\n    usage.sklearn: 13\n    "
    ...


def ediff1d(ary: numpy.ndarray, to_begin: Union[List[int], None, int, float]):
    "\n    usage.sklearn: 1\n    usage.dask: 4\n    "
    ...


def digitize(x: Union[List[int], numpy.ndarray], bins: numpy.ndarray):
    "\n    usage.sklearn: 1\n    usage.dask: 8\n    "
    ...


def fdtrc(_0: int, _1: Union[int, numpy.int64], _2: numpy.ndarray, /):
    "\n    usage.sklearn: 1\n    usage.dask: 2\n    "
    ...


def corrcoef(x: numpy.ndarray):
    "\n    usage.sklearn: 3\n    usage.dask: 5\n    "
    ...


def xlogy(_0: numpy.ndarray, _1: numpy.ndarray, /):
    "\n    usage.sklearn: 1\n    usage.dask: 2\n    "
    ...


def chdtrc(_0: int, _1: numpy.ndarray, /):
    "\n    usage.sklearn: 1\n    "
    ...


def asmatrix(data: numpy.ndarray):
    "\n    usage.sklearn: 2\n    usage.dask: 1\n    "
    ...


def iterable(y: object):
    "\n    usage.sklearn: 9\n    usage.dask: 8\n    "
    ...


def erf(_0: numpy.ndarray, /):
    "\n    usage.sklearn: 1\n    "
    ...


def inner(_0: numpy.ndarray, _1: numpy.ndarray, /):
    "\n    usage.sklearn: 4\n    "
    ...


def gamma(_0: float, /):
    "\n    usage.sklearn: 1\n    "
    ...


def kv(_0: float, _1: numpy.ndarray, /):
    "\n    usage.sklearn: 1\n    "
    ...


def equal(_0: object, _1: object, /):
    "\n    usage.sklearn: 9\n    usage.dask: 113\n    "
    ...


def vander(x: numpy.ndarray, N: int):
    "\n    usage.sklearn: 1\n    "
    ...


def not_equal(_0: object, _1: object, /):
    "\n    usage.sklearn: 1\n    usage.dask: 109\n    "
    ...


def isposinf(x: Union[numpy.ndarray, float, int]):
    "\n    usage.sklearn: 2\n    usage.dask: 1\n    "
    ...


def inv(
    _0: Union[dask.array.core.Array, numpy.ndarray],
    /,
    *,
    output_dtypes: Type[float] = ...,
):
    "\n    usage.dask: 3\n    "
    ...


def eig(
    _0: Union[dask.array.core.Array, numpy.ndarray],
    /,
    *,
    output_dtypes: Tuple[Type[float], Type[float]] = ...,
):
    "\n    usage.dask: 3\n    "
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
    "\n    usage.dask: 18\n    "
    ...


def modf(_0: Union[dask.array.core.Array, numpy.ndarray], /):
    "\n    usage.dask: 9\n    "
    ...


def save(
    file: Literal["/var/folders/xn/05ktz3056kqd9n8frgd6236h0000gn/T/t"],
    arr: Union[numpy.ndarray, numpy.memmap],
):
    "\n    usage.dask: 6\n    "
    ...


def diagonal(
    a: Union[numpy.ndarray, dask.array.core.Array],
    offset: int = ...,
    axis1: int = ...,
    axis2: int = ...,
):
    "\n    usage.dask: 23\n    "
    ...


def fromfunction(function: Callable, shape: Tuple[int, int]):
    "\n    usage.dask: 2\n    "
    ...


def g(
    _0: Union[numpy.ndarray, dask.array.core.Array],
    _1: Union[numpy.ndarray, dask.array.core.Array],
    /,
    *,
    axis: int = ...,
):
    "\n    usage.dask: 3\n    "
    ...


def mysum(
    _0: Union[numpy.ndarray, dask.array.core.Array],
    /,
    *,
    allow_rechunk: bool = ...,
    axis: int = ...,
    keepdims: bool = ...,
):
    "\n    usage.dask: 3\n    "
    ...


def partition(a: numpy.ndarray, kth: int, axis: int):
    "\n    usage.dask: 1\n    "
    ...


def vdot(_0: numpy.ndarray, _1: numpy.ndarray, /):
    "\n    usage.dask: 2\n    "
    ...


def extract(condition: numpy.ndarray, arr: numpy.ndarray):
    "\n    usage.dask: 1\n    "
    ...


def piecewise(
    x: Union[int, numpy.ndarray],
    condlist: Union[numpy.ndarray, List[numpy.ndarray]],
    funclist: List[Union[Callable, int, numpy.ndarray]],
    *args: Literal["v", "t"],
):
    "\n    usage.dask: 6\n    "
    ...


def argwhere(a: numpy.ndarray):
    "\n    usage.dask: 3\n    "
    ...


def einsum_path(*operands: Literal["v", "t"]):
    "\n    usage.dask: 2\n    "
    ...


def exp2(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    "\n    usage.dask: 37\n    "
    ...


def negative(_0: object, /, *, out: dask.dataframe.core.DataFrame = ...):
    "\n    usage.dask: 40\n    "
    ...


def bitwise_and(
    _0: Union[int, dask.array.core.Array, numpy.ndarray],
    _1: Union[numpy.ndarray, dask.array.core.Array, int],
    /,
):
    "\n    usage.dask: 18\n    "
    ...


def bitwise_or(
    _0: Union[int, dask.array.core.Array, numpy.ndarray],
    _1: Union[numpy.ndarray, dask.array.core.Array, int],
    /,
):
    "\n    usage.dask: 18\n    "
    ...


def bitwise_xor(
    _0: Union[int, dask.array.core.Array, numpy.ndarray],
    _1: Union[numpy.ndarray, dask.array.core.Array, int],
    /,
):
    "\n    usage.dask: 18\n    "
    ...


def less_equal(_0: object, _1: object, /):
    "\n    usage.dask: 109\n    "
    ...


def remainder(
    _0: Union[numpy.ndarray, int, dask.array.core.Array],
    _1: Union[int, numpy.ndarray, dask.array.core.Array],
    /,
    *,
    out: numpy.ndarray = ...,
):
    "\n    usage.dask: 23\n    "
    ...


def float_power(
    _0: Union[int, dask.array.core.Array, numpy.ndarray],
    _1: Union[numpy.ndarray, dask.array.core.Array, int],
    /,
):
    "\n    usage.dask: 18\n    "
    ...


def isneginf(x: numpy.ndarray):
    "\n    usage.dask: 1\n    "
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
    "\n    usage.dask: 17\n    "
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
    "\n    usage.dask: 17\n    "
    ...


def frompyfunc(_0: Callable, _1: int, _2: int, /):
    "\n    usage.dask: 4\n    "
    ...


def divmod(
    _0: Union[numpy.ndarray, dask.array.core.Array],
    _1: Union[numpy.ndarray, float, dask.array.core.Array],
    /,
):
    "\n    usage.dask: 4\n    "
    ...


class ndarray:

    # usage.sklearn: 1
    # usage.dask: 5
    __name__: ClassVar[object]

    # usage.dask: 8
    __module__: ClassVar[object]

    @classmethod
    def mean(_0: numpy.ndarray, /):
        "\n    usage.sample_usage: 1\n    usage.skimage: 23\n    usage.xarray: 1\n    usage.sklearn: 62\n    usage.dask: 2\n    "
        ...

    @classmethod
    def sum(_0: numpy.ndarray, /):
        "\n    usage.sample_usage: 1\n    usage.skimage: 86\n    usage.xarray: 10\n    usage.sklearn: 147\n    usage.dask: 34\n    "
        ...

    @classmethod
    def sort(_0: numpy.ndarray, /):
        "\n    usage.sample_usage: 1\n    usage.sklearn: 1\n    usage.dask: 3\n    "
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
        "\n    usage.sample_usage: 2\n    usage.skimage: 168\n    usage.xarray: 190\n    usage.sklearn: 163\n    usage.dask: 177\n    "
        ...

    @classmethod
    def astype(
        _0: Union[numpy.ma.core.MaskedArray, numpy.ndarray],
        _1: Union[type, numpy.dtype, str],
        /,
    ):
        "\n    usage.sample_usage: 1\n    usage.skimage: 555\n    usage.xarray: 75\n    usage.sklearn: 149\n    usage.dask: 160\n    "
        ...

    @classmethod
    def copy(_0: Union[numpy.ndarray, numpy.matrix, numpy.memmap], /):
        "\n    usage.skimage: 135\n    usage.xarray: 14\n    usage.sklearn: 129\n    usage.dask: 7\n    "
        ...

    @classmethod
    def max(_0: numpy.ndarray, /):
        "\n    usage.skimage: 108\n    usage.xarray: 15\n    usage.sklearn: 31\n    usage.dask: 7\n    "
        ...

    @classmethod
    def ptp(_0: numpy.ndarray, /):
        "\n    usage.skimage: 5\n    "
        ...

    @classmethod
    def min(_0: numpy.ndarray, /):
        "\n    usage.skimage: 80\n    usage.xarray: 16\n    usage.sklearn: 29\n    usage.dask: 5\n    "
        ...

    @classmethod
    def any(_0: numpy.ndarray, /):
        "\n    usage.skimage: 11\n    usage.xarray: 6\n    usage.sklearn: 13\n    usage.dask: 13\n    "
        ...

    @classmethod
    def nonzero(_0: Union[numpy.ndarray, numpy.matrix], /):
        "\n    usage.skimage: 4\n    usage.xarray: 4\n    usage.sklearn: 5\n    usage.dask: 1\n    "
        ...

    @classmethod
    def fill(_0: numpy.ndarray, _1: Union[int, bool, float, numpy.float64], /):
        "\n    usage.skimage: 5\n    usage.sklearn: 26\n    "
        ...

    @classmethod
    def flatten(_0: numpy.ndarray, /):
        "\n    usage.skimage: 16\n    usage.xarray: 5\n    usage.sklearn: 7\n    usage.dask: 6\n    "
        ...

    @classmethod
    def ravel(_0: numpy.ndarray, /):
        "\n    usage.skimage: 207\n    usage.xarray: 40\n    usage.sklearn: 142\n    usage.dask: 12\n    "
        ...

    @classmethod
    def cumsum(_0: numpy.ndarray, /):
        "\n    usage.skimage: 1\n    usage.sklearn: 3\n    usage.dask: 3\n    "
        ...

    @classmethod
    def transpose(
        _0: numpy.ndarray,
        _1: Union[List[int], int, range, Tuple[int, ...]] = ...,
        _2: int = ...,
        _3: int = ...,
        /,
    ):
        "\n    usage.skimage: 5\n    usage.xarray: 13\n    usage.sklearn: 8\n    usage.dask: 10\n    "
        ...

    @classmethod
    def argmin(_0: numpy.ndarray, /):
        "\n    usage.skimage: 2\n    usage.sklearn: 3\n    "
        ...

    @classmethod
    def view(_0: numpy.ndarray, /):
        "\n    usage.skimage: 22\n    usage.xarray: 11\n    usage.sklearn: 4\n    usage.dask: 35\n    "
        ...

    @classmethod
    def swapaxes(_0: numpy.ndarray, _1: int, _2: int, /):
        "\n    usage.skimage: 2\n    usage.sklearn: 1\n    usage.dask: 5\n    "
        ...

    @classmethod
    def argsort(_0: numpy.ndarray, /):
        "\n    usage.skimage: 5\n    usage.sklearn: 7\n    "
        ...

    @classmethod
    def argmax(_0: numpy.ndarray, /):
        "\n    usage.skimage: 6\n    usage.sklearn: 5\n    "
        ...

    @classmethod
    def std(_0: numpy.ndarray, /):
        "\n    usage.skimage: 63\n    usage.xarray: 2\n    usage.sklearn: 8\n    usage.dask: 3\n    "
        ...

    @classmethod
    def all(_0: numpy.ndarray, /):
        "\n    usage.skimage: 1\n    usage.xarray: 9\n    usage.sklearn: 5\n    usage.dask: 4\n    "
        ...

    @classmethod
    def tobytes(_0: numpy.ndarray, /):
        "\n    usage.skimage: 2\n    "
        ...

    @classmethod
    def tolist(_0: Union[numpy.ndarray, numpy.memmap], /):
        "\n    usage.skimage: 1\n    usage.xarray: 17\n    usage.sklearn: 23\n    usage.dask: 32\n    "
        ...

    @classmethod
    def dot(_0: numpy.ndarray, _1: Union[dask.array.core.Array, numpy.ndarray], /):
        "\n    usage.skimage: 1\n    usage.sklearn: 50\n    usage.dask: 9\n    "
        ...

    @classmethod
    def conj(_0: numpy.ndarray, /):
        "\n    usage.skimage: 4\n    usage.dask: 2\n    "
        ...

    @classmethod
    def __ne__(_0: Type[numpy.ndarray], /):
        "\n    usage.skimage: 2\n    "
        ...

    @classmethod
    def item(_0: numpy.ndarray, /):
        "\n    usage.xarray: 18\n    usage.dask: 21\n    "
        ...

    @classmethod
    def squeeze(_0: numpy.ndarray, /):
        "\n    usage.xarray: 3\n    usage.sklearn: 14\n    "
        ...

    @classmethod
    def clip(
        _0: numpy.ndarray,
        _1: int,
        _2: Union[int, float] = ...,
        _3: numpy.ndarray = ...,
        /,
    ):
        "\n    usage.xarray: 1\n    usage.sklearn: 2\n    usage.dask: 3\n    "
        ...

    @classmethod
    def __rmod__(_0: Literal["Expected sequence or array-like, got %s"], /):
        "\n    usage.sklearn: 1\n    "
        ...

    @classmethod
    def take(_0: numpy.ndarray, _1: numpy.ndarray, /):
        "\n    usage.sklearn: 8\n    usage.dask: 1\n    "
        ...

    @classmethod
    def tostring(_0: numpy.ndarray, /):
        "\n    usage.sklearn: 1\n    "
        ...

    @classmethod
    def repeat(_0: numpy.ndarray, _1: Union[int, numpy.ndarray], /):
        "\n    usage.sklearn: 1\n    usage.dask: 1\n    "
        ...

    @classmethod
    def var(_0: numpy.ndarray, /):
        "\n    usage.sklearn: 1\n    "
        ...

    @classmethod
    def searchsorted(_0: numpy.ndarray, _1: numpy.int64, /):
        "\n    usage.sklearn: 1\n    "
        ...

    @classmethod
    def round(_0: numpy.ndarray, /):
        "\n    usage.sklearn: 2\n    usage.dask: 2\n    "
        ...

    @classmethod
    def __array_wrap__(_0: numpy.ndarray, _1: numpy.ndarray, /):
        "\n    usage.dask: 2\n    "
        ...

    @classmethod
    def cumprod(_0: numpy.ndarray, /):
        "\n    usage.dask: 1\n    "
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
        "\n    usage.dask: 30\n    "
        ...

    @classmethod
    def prod(_0: numpy.ndarray, /):
        "\n    usage.dask: 4\n    "
        ...

    @classmethod
    def choose(_0: numpy.ndarray, _1: List[Union[int, numpy.ndarray]], /):
        "\n    usage.dask: 2\n    "
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
        "\n    usage.sample_usage: 1\n    usage.dask: 1\n    "
        ...

    def __neg__(self: object, /):
        "\n    usage.sample_usage: 1\n    usage.skimage: 42\n    usage.xarray: 21\n    usage.sklearn: 78\n    usage.dask: 7\n    "
        ...

    def __invert__(self: object, /):
        "\n    usage.sample_usage: 1\n    usage.skimage: 26\n    usage.xarray: 7\n    usage.sklearn: 63\n    usage.dask: 9\n    "
        ...

    def __bool__(self: object, /):
        "\n    usage.sample_usage: 1\n    "
        ...

    def __iter__(self: object, /):
        "\n    usage.sample_usage: 2\n    usage.skimage: 149\n    usage.xarray: 83\n    usage.sklearn: 104\n    usage.dask: 6\n    "
        ...

    def __getitem__(self: object, _0: object, /):
        "\n    usage.sample_usage: 5\n    usage.skimage: 2171\n    usage.xarray: 747\n    usage.sklearn: 2575\n    usage.dask: 1145\n    "
        ...

    def __pow__(self: object, _0: Union[numpy.ndarray, int, numpy.float64, float], /):
        "\n    usage.sample_usage: 1\n    usage.skimage: 173\n    usage.xarray: 11\n    usage.sklearn: 176\n    usage.dask: 12\n    "
        ...

    def __rpow__(self: object, _0: Union[int, numpy.ndarray, float], /):
        "\n    usage.sample_usage: 2\n    usage.skimage: 3\n    usage.sklearn: 2\n    usage.dask: 3\n    "
        ...

    def __mul__(self: object, _0: object, /):
        "\n    usage.sample_usage: 1\n    usage.skimage: 402\n    usage.xarray: 41\n    usage.sklearn: 319\n    usage.dask: 66\n    "
        ...

    def __rmul__(self: object, _0: object, /):
        "\n    usage.sample_usage: 2\n    usage.skimage: 574\n    usage.xarray: 56\n    usage.sklearn: 545\n    usage.dask: 73\n    "
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
        "\n    usage.sample_usage: 1\n    usage.skimage: 50\n    usage.sklearn: 11\n    "
        ...

    def __rmatmul__(self: object, _0: object, /):
        "\n    usage.sample_usage: 1\n    usage.skimage: 52\n    usage.sklearn: 15\n    "
        ...

    def __floordiv__(
        self: object,
        _0: Union[int, numpy.ndarray, float, numpy.float64, List[Union[float, int]]],
        /,
    ):
        "\n    usage.sample_usage: 1\n    usage.skimage: 14\n    usage.xarray: 1\n    usage.sklearn: 12\n    usage.dask: 6\n    "
        ...

    def __rfloordiv__(self: object, _0: Union[numpy.ndarray, int], /):
        "\n    usage.sample_usage: 1\n    usage.skimage: 2\n    usage.sklearn: 1\n    usage.dask: 2\n    "
        ...

    def __mod__(self: object, _0: Union[numpy.ndarray, int, float], /):
        "\n    usage.sample_usage: 1\n    usage.skimage: 7\n    usage.xarray: 2\n    usage.sklearn: 8\n    usage.dask: 12\n    "
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
        "\n    usage.sample_usage: 1\n    usage.skimage: 1\n    usage.xarray: 1\n    usage.sklearn: 2\n    usage.dask: 2\n    "
        ...

    def __add__(self: object, _0: object, /):
        "\n    usage.sample_usage: 2\n    usage.skimage: 316\n    usage.xarray: 32\n    usage.sklearn: 232\n    usage.dask: 188\n    "
        ...

    def __radd__(self: object, _0: object, /):
        "\n    usage.sample_usage: 2\n    usage.skimage: 268\n    usage.xarray: 40\n    usage.sklearn: 171\n    usage.dask: 72\n    "
        ...

    def __sub__(self: object, _0: object, /):
        "\n    usage.sample_usage: 1\n    usage.skimage: 374\n    usage.xarray: 25\n    usage.sklearn: 358\n    usage.dask: 45\n    "
        ...

    def __rsub__(self: object, _0: object, /):
        "\n    usage.sample_usage: 1\n    usage.skimage: 274\n    usage.xarray: 14\n    usage.sklearn: 314\n    usage.dask: 20\n    "
        ...

    def __lshift__(self: object, _0: int, /):
        "\n    usage.sample_usage: 1\n    "
        ...

    def __rlshift__(self: object, _0: int, /):
        "\n    usage.sample_usage: 1\n    usage.dask: 1\n    "
        ...

    def __rshift__(self: object, _0: int, /):
        "\n    usage.sample_usage: 1\n    usage.dask: 1\n    "
        ...

    def __rrshift__(self: object, _0: int, /):
        "\n    usage.sample_usage: 1\n    "
        ...

    def __and__(
        self: object,
        _0: Union[bool, numpy.ndarray, dask.array.core.Array, numpy.bool_, int],
        /,
    ):
        "\n    usage.sample_usage: 1\n    usage.skimage: 33\n    usage.xarray: 3\n    usage.sklearn: 8\n    usage.dask: 5\n    "
        ...

    def __rand__(
        self: object,
        _0: Union[bool, numpy.ndarray, dask.array.core.Array, numpy.bool_, int],
        /,
    ):
        "\n    usage.sample_usage: 1\n    usage.skimage: 31\n    usage.xarray: 3\n    usage.sklearn: 8\n    usage.dask: 5\n    "
        ...

    def __or__(
        self: object,
        _0: Union[bool, numpy.ndarray, numpy.bool_, dask.array.core.Array, int],
        /,
    ):
        "\n    usage.sample_usage: 1\n    usage.skimage: 8\n    usage.xarray: 4\n    usage.sklearn: 6\n    usage.dask: 3\n    "
        ...

    def __ror__(
        self: object,
        _0: Union[bool, numpy.ndarray, dask.array.core.Array, numpy.bool_, int],
        /,
    ):
        "\n    usage.sample_usage: 1\n    usage.skimage: 8\n    usage.xarray: 6\n    usage.sklearn: 6\n    usage.dask: 3\n    "
        ...

    def __ipow__(self: object, _0: Union[int, float], /):
        "\n    usage.sample_usage: 1\n    usage.sklearn: 22\n    "
        ...

    def __imul__(self: object, _0: object, /):
        "\n    usage.sample_usage: 1\n    usage.skimage: 42\n    usage.xarray: 2\n    usage.sklearn: 123\n    usage.dask: 1\n    "
        ...

    def __ifloordiv__(self: object, _0: int, /):
        "\n    usage.sample_usage: 1\n    usage.skimage: 5\n    "
        ...

    def __imod__(self: object, _0: int, /):
        "\n    usage.sample_usage: 1\n    usage.dask: 3\n    "
        ...

    def __iadd__(self: object, _0: object, /):
        "\n    usage.sample_usage: 1\n    usage.skimage: 131\n    usage.xarray: 4\n    usage.sklearn: 164\n    usage.dask: 12\n    "
        ...

    def __isub__(self: object, _0: object, /):
        "\n    usage.sample_usage: 1\n    usage.skimage: 45\n    usage.xarray: 1\n    usage.sklearn: 90\n    usage.dask: 2\n    "
        ...

    def __ilshift__(self: object, _0: int, /):
        "\n    usage.sample_usage: 1\n    "
        ...

    def __irshift__(self: object, _0: int, /):
        "\n    usage.sample_usage: 1\n    "
        ...

    def __iand__(self: object, _0: Union[numpy.ndarray, int], /):
        "\n    usage.sample_usage: 1\n    usage.skimage: 2\n    usage.sklearn: 3\n    "
        ...

    def __ior__(self: object, _0: Union[numpy.ndarray, int], /):
        "\n    usage.sample_usage: 1\n    usage.skimage: 3\n    usage.xarray: 1\n    "
        ...

    def __setitem__(self: object, _0: object, _1: object, /):
        "\n    usage.sample_usage: 1\n    usage.skimage: 1514\n    usage.xarray: 142\n    usage.sklearn: 840\n    usage.dask: 527\n    "
        ...

    def __eq__(self: object, _0: object, /):
        "\n    usage.sample_usage: 2\n    usage.skimage: 327\n    usage.xarray: 330\n    usage.sklearn: 280\n    usage.dask: 189\n    "
        ...

    def __le__(
        self: object,
        _0: Union[float, numpy.ndarray, int, numpy.float64, numpy.int64],
        /,
    ):
        "\n    usage.sample_usage: 1\n    usage.skimage: 122\n    usage.xarray: 15\n    usage.sklearn: 94\n    usage.dask: 35\n    "
        ...

    def sort(
        self: object,
        /,
        *,
        axis: int = ...,
        order: Literal["accumulator"] = ...,
        kind: Literal["mergesort"] = ...,
    ):
        "\n    usage.sample_usage: 1\n    usage.skimage: 9\n    usage.sklearn: 1\n    usage.dask: 1\n    "
        ...

    def __gt__(self: object, _0: object, /):
        "\n    usage.sample_usage: 1\n    usage.skimage: 159\n    usage.xarray: 9\n    usage.sklearn: 81\n    usage.dask: 26\n    "
        ...

    def __contains__(self: object, _0: Union[int, numpy.int64, Tuple[int, int]], /):
        "\n    usage.sample_usage: 1\n    usage.skimage: 13\n    usage.xarray: 3\n    usage.sklearn: 19\n    "
        ...

    def mean(
        self: object,
        /,
        *,
        axis: Union[Tuple[Union[int, None], ...], None, int] = ...,
        keepdims: bool = ...,
    ):
        "\n    usage.skimage: 28\n    usage.xarray: 5\n    usage.sklearn: 48\n    usage.dask: 10\n    "
        ...

    def __truediv__(self: object, _0: object, /):
        "\n    usage.skimage: 249\n    usage.xarray: 9\n    usage.sklearn: 223\n    usage.dask: 23\n    "
        ...

    def __rtruediv__(
        self: object,
        _0: Union[int, numpy.ndarray, numpy.float64, numpy.complex128, float],
        /,
    ):
        "\n    usage.skimage: 102\n    usage.xarray: 1\n    usage.sklearn: 153\n    usage.dask: 13\n    "
        ...

    def __itruediv__(self: object, _0: object, /):
        "\n    usage.skimage: 38\n    usage.xarray: 2\n    usage.sklearn: 80\n    usage.dask: 1\n    "
        ...

    def __ne__(self: object, _0: object, /):
        "\n    usage.skimage: 44\n    usage.xarray: 15\n    usage.sklearn: 98\n    usage.dask: 6\n    "
        ...

    def __ge__(self: object, _0: object, /):
        "\n    usage.skimage: 92\n    usage.xarray: 5\n    usage.sklearn: 43\n    usage.dask: 17\n    "
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
        "\n    usage.skimage: 23\n    usage.xarray: 3\n    usage.sklearn: 96\n    usage.dask: 126\n    "
        ...

    def all(self: object, /, *, axis: int = ...):
        "\n    usage.skimage: 47\n    usage.xarray: 20\n    usage.sklearn: 35\n    usage.dask: 86\n    "
        ...

    def any(self: object, /, *, axis: int = ...):
        "\n    usage.skimage: 4\n    usage.xarray: 2\n    usage.sklearn: 20\n    usage.dask: 1\n    "
        ...

    def min(
        self: object,
        /,
        *,
        axis: int = ...,
        keepdims: bool = ...,
        out: numpy.ndarray = ...,
    ):
        "\n    usage.skimage: 18\n    usage.sklearn: 10\n    usage.dask: 2\n    "
        ...

    def max(self: object, /, *, axis: int = ..., keepdims: bool = ...):
        "\n    usage.skimage: 18\n    usage.sklearn: 3\n    usage.dask: 2\n    "
        ...

    def cumsum(self: object, /, *, axis: int):
        "\n    usage.skimage: 6\n    usage.dask: 4\n    "
        ...

    def __lt__(self: object, _0: Union[int, numpy.ndarray, numpy.float64], /):
        "\n    usage.skimage: 17\n    usage.sklearn: 13\n    usage.dask: 3\n    "
        ...

    def argmax(self: object, /, *, axis: int = ...):
        "\n    usage.skimage: 1\n    usage.sklearn: 9\n    "
        ...

    def astype(
        self: object,
        /,
        *,
        copy: bool = ...,
        dtype: Union[Literal["i2", ">u4", "i1"], numpy.dtype, type] = ...,
    ):
        "\n    usage.skimage: 34\n    usage.xarray: 89\n    usage.sklearn: 62\n    usage.dask: 29\n    "
        ...

    def tolist(self: object, /):
        "\n    usage.skimage: 6\n    usage.xarray: 1\n    usage.dask: 7\n    "
        ...

    def std(
        self: object,
        /,
        *,
        axis: Union[int, Tuple[int, int]] = ...,
        ddof: int = ...,
        keepdims: bool = ...,
    ):
        "\n    usage.skimage: 2\n    usage.xarray: 2\n    usage.sklearn: 10\n    usage.dask: 1\n    "
        ...

    def view(
        self: object,
        /,
        *,
        dtype: Union[Literal["|S512", "|S80", "|S16"], Type[numpy.uint8]],
    ):
        "\n    usage.skimage: 4\n    usage.sklearn: 3\n    "
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
        "\n    usage.skimage: 3\n    usage.xarray: 2\n    usage.dask: 4\n    "
        ...

    def repeat(self: object, _0: int, /, *, axis: int):
        "\n    usage.skimage: 2\n    usage.dask: 1\n    "
        ...

    def ravel(self: object, /, *, order: Literal["K", "F", "C"] = ...):
        "\n    usage.skimage: 2\n    usage.xarray: 1\n    usage.sklearn: 2\n    usage.dask: 23\n    "
        ...

    def var(self: object, /, *, axis: int = ...):
        "\n    usage.skimage: 7\n    usage.dask: 3\n    "
        ...

    def reshape(
        self: object,
        _0: Union[Tuple[Union[int, None], ...], int],
        _1: int = ...,
        _2: int = ...,
        /,
    ):
        "\n    usage.xarray: 6\n    usage.sklearn: 5\n    usage.dask: 11\n    "
        ...

    def transpose(self: object, _0: List[int], /):
        "\n    usage.xarray: 6\n    "
        ...

    def round(self: object, /):
        "\n    usage.xarray: 2\n    "
        ...

    def argsort(self: object, /):
        "\n    usage.xarray: 2\n    "
        ...

    def item(self: object, /):
        "\n    usage.xarray: 2\n    "
        ...

    def take(
        self: object,
        _0: Union[List[numpy.int64], int, numpy.ndarray],
        /,
        *,
        axis: Union[None, int] = ...,
        mode: Literal["clip"] = ...,
    ):
        "\n    usage.xarray: 4\n    usage.sklearn: 70\n    "
        ...

    def searchsorted(self: object, _0: int, /):
        "\n    usage.xarray: 1\n    "
        ...

    def argmin(self: object, /, *, axis: int):
        "\n    usage.sklearn: 3\n    usage.dask: 2\n    "
        ...

    def squeeze(self: object, /, *, axis: Union[int, None, Tuple[int, int]] = ...):
        "\n    usage.sklearn: 3\n    usage.dask: 3\n    "
        ...

    def copy(self: object, /, *, order: Literal["F", "K"] = ...):
        "\n    usage.sklearn: 4\n    usage.dask: 1\n    "
        ...

    def setflags(self: object, /, *, write: bool):
        "\n    usage.sklearn: 3\n    "
        ...

    def __xor__(self: object, _0: Union[bool, numpy.ndarray], /):
        "\n    usage.dask: 2\n    "
        ...

    def __rxor__(self: object, _0: Union[bool, numpy.ndarray], /):
        "\n    usage.dask: 2\n    "
        ...

    def cumprod(self: object, /, *, axis: int):
        "\n    usage.dask: 3\n    "
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
        "\n    usage.dask: 7\n    "
        ...


class dtype:
    def __init__(_0: Union[dask.delayed.DelayedLeaf, Literal["f4"]], /):
        "\n    usage.dask: 2\n    "
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
        "\n    usage.skimage: 282\n    usage.xarray: 230\n    usage.sklearn: 217\n    usage.dask: 315\n    "
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
        "\n    usage.skimage: 27\n    usage.xarray: 34\n    usage.sklearn: 33\n    usage.dask: 266\n    "
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
        "\n    usage.skimage: 1\n    usage.xarray: 1\n    usage.dask: 2\n    "
        ...

    def __getitem__(self: object, _0: str, /):
        "\n    usage.dask: 17\n    "
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
        "\n    usage.sample_usage: 1\n    usage.skimage: 6\n    usage.xarray: 1\n    "
        ...

    @classmethod
    def reduceat(_0: Callable, _1: numpy.ndarray, _2: numpy.ndarray, /):
        "\n    usage.sklearn: 2\n    "
        ...

    @classmethod
    def outer(
        _0: Callable,
        _1: object,
        _2: Union[numpy.ndarray, dask.array.core.Array, int],
        /,
    ):
        "\n    usage.dask: 14\n    "
        ...


class float64:

    # usage.dask: 2
    __module__: ClassVar[object]

    @classmethod
    def __ne__(_0: numpy.dtype, /):
        "\n    usage.sklearn: 11\n    usage.dask: 1\n    "
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
        "\n    usage.skimage: 127\n    usage.xarray: 13\n    usage.sklearn: 111\n    usage.dask: 26\n    "
        ...

    def __rmul__(self: object, _0: object, /):
        "\n    usage.skimage: 176\n    usage.xarray: 3\n    usage.sklearn: 203\n    usage.dask: 15\n    "
        ...

    def __gt__(self: object, _0: object, /):
        "\n    usage.skimage: 74\n    usage.xarray: 8\n    usage.sklearn: 110\n    usage.dask: 6\n    "
        ...

    def __rsub__(self: object, _0: object, /):
        "\n    usage.skimage: 111\n    usage.xarray: 12\n    usage.sklearn: 130\n    usage.dask: 13\n    "
        ...

    def __rtruediv__(self: object, _0: object, /):
        "\n    usage.skimage: 106\n    usage.xarray: 2\n    usage.sklearn: 143\n    usage.dask: 21\n    "
        ...

    def __iadd__(self: object, _0: object, /):
        "\n    usage.skimage: 9\n    usage.xarray: 6\n    usage.sklearn: 49\n    usage.dask: 1\n    "
        ...

    def __truediv__(self: object, _0: object, /):
        "\n    usage.skimage: 96\n    usage.xarray: 7\n    usage.sklearn: 116\n    usage.dask: 25\n    "
        ...

    def __radd__(self: object, _0: object, /):
        "\n    usage.skimage: 87\n    usage.xarray: 9\n    usage.sklearn: 114\n    usage.dask: 26\n    "
        ...

    def __add__(self: object, _0: object, /):
        "\n    usage.skimage: 78\n    usage.xarray: 9\n    usage.sklearn: 98\n    usage.dask: 22\n    "
        ...

    def __sub__(self: object, _0: object, /):
        "\n    usage.skimage: 154\n    usage.xarray: 13\n    usage.sklearn: 87\n    usage.dask: 10\n    "
        ...

    def __mul__(self: object, _0: object, /):
        "\n    usage.skimage: 81\n    usage.xarray: 3\n    usage.sklearn: 160\n    usage.dask: 7\n    "
        ...

    def __getitem__(self: object, _0: Tuple[Union[None, ellipsis], ...], /):
        "\n    usage.skimage: 2\n    usage.xarray: 1\n    usage.dask: 4\n    "
        ...

    def __neg__(self: object, /):
        "\n    usage.skimage: 22\n    usage.xarray: 2\n    usage.sklearn: 27\n    "
        ...

    def __ge__(self: object, _0: object, /):
        "\n    usage.skimage: 62\n    usage.xarray: 6\n    usage.sklearn: 70\n    usage.dask: 29\n    "
        ...

    def __pow__(self: object, _0: Union[float, int, numpy.float64], /):
        "\n    usage.skimage: 36\n    usage.sklearn: 20\n    usage.dask: 3\n    "
        ...

    def __lt__(self: object, _0: object, /):
        "\n    usage.skimage: 60\n    usage.xarray: 2\n    usage.sklearn: 44\n    usage.dask: 3\n    "
        ...

    def __imod__(self: object, _0: float, /):
        "\n    usage.skimage: 2\n    "
        ...

    def __eq__(self: object, _0: object, /):
        "\n    usage.skimage: 106\n    usage.xarray: 50\n    usage.sklearn: 142\n    usage.dask: 31\n    "
        ...

    def __mod__(self: object, _0: Union[int, float], /):
        "\n    usage.skimage: 9\n    "
        ...

    def __itruediv__(self: object, _0: object, /):
        "\n    usage.skimage: 12\n    usage.sklearn: 10\n    "
        ...

    def __rpow__(self: object, _0: Union[numpy.ndarray, numpy.float64, float, int], /):
        "\n    usage.skimage: 3\n    usage.sklearn: 3\n    "
        ...

    def __ne__(
        self: object,
        _0: Union[
            int, numpy.float64, float, numpy.int64, _pytest.python_api.ApproxScalar
        ],
        /,
    ):
        "\n    usage.skimage: 9\n    usage.xarray: 6\n    usage.sklearn: 12\n    usage.dask: 11\n    "
        ...

    def __isub__(self: object, _0: Union[int, numpy.float64, numpy.ndarray], /):
        "\n    usage.skimage: 1\n    usage.sklearn: 18\n    "
        ...

    def __imul__(self: object, _0: Union[numpy.int64, int, numpy.float64, float], /):
        "\n    usage.skimage: 5\n    usage.sklearn: 10\n    usage.dask: 2\n    "
        ...

    def __rfloordiv__(self: object, _0: numpy.ndarray, /):
        "\n    usage.skimage: 1\n    "
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
        "\n    usage.sklearn: 2\n    usage.dask: 3\n    "
        ...

    def __floordiv__(self: object, _0: int, /):
        "\n    usage.dask: 1\n    "
        ...

    def astype(self: object, _0: numpy.dtype, /):
        "\n    usage.dask: 1\n    "
        ...


class int64:

    # usage.dask: 1
    __module__: ClassVar[object]

    @classmethod
    def __ne__(_0: numpy.dtype, /):
        "\n    usage.dask: 2\n    "
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
        "\n    usage.skimage: 8\n    usage.xarray: 2\n    usage.sklearn: 10\n    usage.dask: 6\n    "
        ...

    def __add__(self: object, _0: object, /):
        "\n    usage.skimage: 38\n    usage.xarray: 11\n    usage.sklearn: 29\n    usage.dask: 23\n    "
        ...

    def __ne__(
        self: object,
        _0: Union[numpy.int64, int, float, numpy.float64, numpy.ndarray],
        /,
    ):
        "\n    usage.skimage: 6\n    usage.xarray: 5\n    usage.sklearn: 12\n    usage.dask: 16\n    "
        ...

    def __ge__(self: object, _0: object, /):
        "\n    usage.skimage: 17\n    usage.xarray: 4\n    usage.sklearn: 19\n    usage.dask: 37\n    "
        ...

    def __rsub__(
        self: object,
        _0: Union[numpy.int64, int, numpy.ndarray, float, numpy.float64],
        /,
    ):
        "\n    usage.skimage: 30\n    usage.xarray: 9\n    usage.sklearn: 13\n    usage.dask: 8\n    "
        ...

    def __eq__(self: object, _0: object, /):
        "\n    usage.skimage: 90\n    usage.xarray: 24\n    usage.sklearn: 82\n    usage.dask: 96\n    "
        ...

    def __rtruediv__(self: object, _0: object, /):
        "\n    usage.skimage: 11\n    usage.xarray: 3\n    usage.sklearn: 20\n    usage.dask: 12\n    "
        ...

    def __sub__(self: object, _0: Union[int, numpy.int64, float, numpy.float64], /):
        "\n    usage.skimage: 25\n    usage.xarray: 10\n    usage.sklearn: 23\n    usage.dask: 10\n    "
        ...

    def __floordiv__(self: object, _0: Union[int, numpy.int64], /):
        "\n    usage.skimage: 5\n    usage.xarray: 1\n    usage.sklearn: 2\n    usage.dask: 4\n    "
        ...

    def __isub__(self: object, _0: Union[numpy.int64, int], /):
        "\n    usage.skimage: 2\n    usage.sklearn: 2\n    usage.dask: 2\n    "
        ...

    def __le__(
        self: object,
        _0: Union[numpy.int64, int, pandas.core.series.Series, float, numpy.ndarray],
        /,
    ):
        "\n    usage.skimage: 18\n    usage.xarray: 4\n    usage.sklearn: 32\n    usage.dask: 32\n    "
        ...

    def __iadd__(self: object, _0: Union[int, numpy.int64, numpy.float64], /):
        "\n    usage.skimage: 1\n    usage.xarray: 3\n    usage.sklearn: 3\n    usage.dask: 3\n    "
        ...

    def __gt__(self: object, _0: Union[float, int, numpy.int64], /):
        "\n    usage.skimage: 11\n    usage.xarray: 1\n    usage.sklearn: 26\n    usage.dask: 20\n    "
        ...

    def __rfloordiv__(self: object, _0: Union[numpy.int64, int, float], /):
        "\n    usage.skimage: 1\n    usage.sklearn: 3\n    usage.dask: 2\n    "
        ...

    def __radd__(self: object, _0: object, /):
        "\n    usage.skimage: 17\n    usage.xarray: 1\n    usage.sklearn: 13\n    usage.dask: 26\n    "
        ...

    def __truediv__(self: object, _0: Union[numpy.int64, int, float, numpy.float64], /):
        "\n    usage.skimage: 15\n    usage.xarray: 2\n    usage.sklearn: 8\n    usage.dask: 7\n    "
        ...

    def __pow__(self: object, _0: Union[int, numpy.int64], /):
        "\n    usage.skimage: 2\n    usage.dask: 3\n    "
        ...

    def __mul__(
        self: object,
        _0: Union[numpy.int64, numpy.ndarray, int, numpy.float64, float],
        /,
    ):
        "\n    usage.skimage: 4\n    usage.sklearn: 12\n    usage.dask: 9\n    "
        ...

    def __lt__(self: object, _0: object, /):
        "\n    usage.skimage: 14\n    usage.xarray: 3\n    usage.sklearn: 5\n    usage.dask: 13\n    "
        ...

    def __itruediv__(self: object, _0: numpy.float64, /):
        "\n    usage.skimage: 2\n    "
        ...

    def __mod__(self: object, _0: Union[int, numpy.int64], /):
        "\n    usage.skimage: 1\n    usage.sklearn: 2\n    usage.dask: 5\n    "
        ...

    def __neg__(self: object, /):
        "\n    usage.skimage: 7\n    usage.xarray: 1\n    usage.sklearn: 7\n    usage.dask: 5\n    "
        ...

    def __imod__(self: object, _0: int, /):
        "\n    usage.skimage: 1\n    "
        ...

    def __getitem__(self: object, _0: Tuple[Union[ellipsis, None], ...], /):
        "\n    usage.xarray: 1\n    usage.dask: 8\n    "
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
        "\n    usage.sklearn: 6\n    usage.dask: 2\n    "
        ...

    def __bool__(self: object, /):
        "\n    usage.dask: 1\n    "
        ...

    def __imul__(self: object, _0: int, /):
        "\n    usage.dask: 1\n    "
        ...

    def reshape(self: object, _0: Tuple[int], /):
        "\n    usage.dask: 1\n    "
        ...

    def __rpow__(self: object, _0: Union[int, numpy.int64], /):
        "\n    usage.dask: 2\n    "
        ...

    def __and__(self: object, _0: Union[bool, numpy.int64], /):
        "\n    usage.dask: 2\n    "
        ...

    def __rand__(self: object, _0: Union[bool, numpy.int64], /):
        "\n    usage.dask: 2\n    "
        ...

    def __or__(self: object, _0: Union[bool, numpy.int64], /):
        "\n    usage.dask: 2\n    "
        ...

    def __ror__(self: object, _0: Union[bool, numpy.int64], /):
        "\n    usage.dask: 2\n    "
        ...

    def __xor__(self: object, _0: Union[bool, numpy.int64], /):
        "\n    usage.dask: 2\n    "
        ...

    def __rxor__(self: object, _0: Union[bool, numpy.int64], /):
        "\n    usage.dask: 2\n    "
        ...


class generic:
    @classmethod
    def astype(
        _0: object,
        _1: Union[Literal["int64", "i8", "f8", "timedelta64[ns]"], numpy.dtype, type],
        /,
    ):
        "\n    usage.skimage: 12\n    usage.xarray: 7\n    usage.sklearn: 1\n    usage.dask: 11\n    "
        ...

    @classmethod
    def conj(_0: numpy.complex128, /):
        "\n    usage.skimage: 1\n    "
        ...

    @classmethod
    def all(_0: numpy.bool_, /):
        "\n    usage.xarray: 5\n    "
        ...

    @classmethod
    def squeeze(_0: numpy.float64, /):
        "\n    usage.xarray: 1\n    "
        ...

    @classmethod
    def item(_0: numpy.float64, /):
        "\n    usage.xarray: 3\n    usage.sklearn: 2\n    "
        ...

    @classmethod
    def any(_0: numpy.bool_, /):
        "\n    usage.xarray: 2\n    usage.dask: 1\n    "
        ...

    @classmethod
    def mean(_0: numpy.float64, /):
        "\n    usage.sklearn: 2\n    "
        ...

    @classmethod
    def ravel(_0: numpy.int64, /):
        "\n    usage.dask: 1\n    "
        ...

    @classmethod
    def reshape(_0: numpy.float64, _1: Tuple[int, ...], /):
        "\n    usage.dask: 2\n    "
        ...


class iinfo:
    def __init__(int_type: Union[type, numpy.dtype, Literal["i"]]):
        "\n    usage.skimage: 33\n    usage.sklearn: 3\n    usage.dask: 1\n    "
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
        "\n    usage.skimage: 2\n    usage.xarray: 4\n    usage.sklearn: 1\n    "
        ...


class bool_:

    # usage.dask: 1
    __module__: ClassVar[object]

    @classmethod
    def __ne__(_0: numpy.dtype, /):
        "\n    usage.skimage: 1\n    "
        ...

    # usage.dask: 4
    dtype: object

    # usage.dask: 5
    ndim: object

    # usage.dask: 7
    shape: object

    def __invert__(self: object, /):
        "\n    usage.skimage: 3\n    usage.xarray: 1\n    usage.dask: 1\n    "
        ...

    def __bool__(self: object, /):
        "\n    usage.skimage: 18\n    usage.xarray: 3\n    usage.sklearn: 24\n    usage.dask: 12\n    "
        ...

    def __rpow__(self: object, _0: int, /):
        "\n    usage.skimage: 1\n    "
        ...

    def __and__(self: object, _0: Union[numpy.ndarray, numpy.bool_], /):
        "\n    usage.xarray: 2\n    "
        ...

    def __rand__(
        self: object, _0: Union[dask.array.core.Array, numpy.bool_, numpy.ndarray], /
    ):
        "\n    usage.xarray: 3\n    "
        ...

    def __or__(self: object, _0: Union[numpy.ndarray, numpy.bool_], /):
        "\n    usage.xarray: 3\n    "
        ...

    def __ror__(self: object, _0: Union[bool, numpy.bool_, numpy.ndarray], /):
        "\n    usage.xarray: 4\n    "
        ...

    def all(self: object, /):
        "\n    usage.xarray: 4\n    usage.dask: 1\n    "
        ...

    def __eq__(self: object, _0: Union[numpy.bool_, numpy.ndarray, bool], /):
        "\n    usage.xarray: 2\n    usage.sklearn: 5\n    usage.dask: 2\n    "
        ...

    def __gt__(self: object, _0: float, /):
        "\n    usage.sklearn: 1\n    "
        ...

    def __getitem__(self: object, _0: Tuple[ellipsis, None], /):
        "\n    usage.dask: 1\n    "
        ...


class flatiter:
    def __eq__(self: object, _0: Union[numpy.float64, int, numpy.int64], /):
        "\n    usage.skimage: 4\n    usage.sklearn: 1\n    "
        ...

    def __iter__(self: object, /):
        "\n    usage.skimage: 2\n    usage.xarray: 8\n    usage.sklearn: 4\n    "
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
        "\n    usage.skimage: 5\n    usage.xarray: 8\n    usage.sklearn: 26\n    usage.dask: 1\n    "
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
        "\n    usage.skimage: 1\n    usage.xarray: 1\n    usage.sklearn: 33\n    usage.dask: 509\n    "
        ...


class uint8:
    @classmethod
    def __ne__(_0: numpy.dtype, /):
        "\n    usage.sklearn: 2\n    "
        ...

    # usage.dask: 2
    ndim: object

    def __eq__(
        self: object, _0: Union[int, numpy.int64, numpy.uint8, numpy.ndarray], /
    ):
        "\n    usage.skimage: 20\n    usage.xarray: 1\n    usage.sklearn: 3\n    "
        ...

    def __rsub__(
        self: object, _0: Union[numpy.ndarray, int, numpy.float64, numpy.uint8], /
    ):
        "\n    usage.skimage: 9\n    "
        ...

    def __rmul__(self: object, _0: float, /):
        "\n    usage.skimage: 3\n    "
        ...

    def __lt__(self: object, _0: Union[numpy.float64, numpy.ndarray, int], /):
        "\n    usage.skimage: 5\n    "
        ...

    def __ge__(self: object, _0: Union[numpy.float64, int], /):
        "\n    usage.skimage: 4\n    "
        ...

    def __truediv__(self: object, _0: int, /):
        "\n    usage.skimage: 1\n    "
        ...

    def __radd__(self: object, _0: Union[numpy.ndarray, numpy.float64, numpy.uint8], /):
        "\n    usage.skimage: 3\n    "
        ...

    def __add__(self: object, _0: Union[int, numpy.uint8], /):
        "\n    usage.skimage: 9\n    "
        ...

    def __sub__(self: object, _0: Union[int, numpy.uint8], /):
        "\n    usage.skimage: 5\n    "
        ...

    def __le__(self: object, _0: Union[int, numpy.int64, numpy.ndarray], /):
        "\n    usage.skimage: 8\n    usage.xarray: 2\n    "
        ...

    def __ne__(self: object, _0: numpy.uint8, /):
        "\n    usage.skimage: 2\n    "
        ...

    def __gt__(self: object, _0: Union[numpy.int64, int], /):
        "\n    usage.skimage: 5\n    usage.xarray: 1\n    "
        ...

    def __rtruediv__(self: object, _0: numpy.float64, /):
        "\n    usage.skimage: 2\n    "
        ...

    def __pow__(self: object, _0: int, /):
        "\n    usage.skimage: 1\n    "
        ...

    def __iadd__(self: object, _0: int, /):
        "\n    usage.xarray: 2\n    "
        ...

    def __getitem__(self: object, _0: Tuple[Union[ellipsis, None], ...], /):
        "\n    usage.dask: 3\n    "
        ...


class uint64:

    # usage.dask: 1
    __module__: ClassVar[object]

    @classmethod
    def __ne__(_0: numpy.dtype, /):
        "\n    usage.dask: 1\n    "
        ...

    # usage.dask: 2
    ndim: object

    def __eq__(
        self: object, _0: Union[int, numpy.uint64, numpy.int64, numpy.ndarray], /
    ):
        "\n    usage.skimage: 19\n    usage.sklearn: 7\n    "
        ...

    def __rtruediv__(self: object, _0: Union[numpy.uint64, float], /):
        "\n    usage.skimage: 2\n    usage.dask: 1\n    "
        ...

    def __ge__(self: object, _0: int, /):
        "\n    usage.skimage: 1\n    "
        ...

    def __le__(self: object, _0: int, /):
        "\n    usage.skimage: 3\n    "
        ...

    def __ne__(self: object, _0: Union[numpy.uint64, float], /):
        "\n    usage.skimage: 5\n    usage.sklearn: 4\n    "
        ...

    def __lt__(self: object, _0: Union[numpy.uint64, int], /):
        "\n    usage.skimage: 3\n    "
        ...

    def __truediv__(self: object, _0: Union[numpy.uint64, int], /):
        "\n    usage.skimage: 1\n    usage.dask: 1\n    "
        ...

    def __rsub__(self: object, _0: Union[numpy.uint64, numpy.ndarray], /):
        "\n    usage.skimage: 1\n    usage.dask: 1\n    "
        ...

    def __rmul__(self: object, _0: Union[int, float], /):
        "\n    usage.skimage: 2\n    usage.dask: 2\n    "
        ...

    def __gt__(self: object, _0: Union[numpy.uint64, numpy.float64], /):
        "\n    usage.skimage: 2\n    "
        ...

    def __sub__(self: object, _0: numpy.uint64, /):
        "\n    usage.dask: 1\n    "
        ...

    def __mul__(self: object, _0: int, /):
        "\n    usage.dask: 1\n    "
        ...

    def __add__(self: object, _0: numpy.float64, /):
        "\n    usage.dask: 2\n    "
        ...

    def __getitem__(self: object, _0: Tuple[ellipsis, None], /):
        "\n    usage.dask: 1\n    "
        ...


class ndindex:
    def __init__(*shape: Literal["v", "t"]):
        "\n    usage.skimage: 1\n    usage.dask: 6\n    "
        ...

    def __iter__(self: object, /):
        "\n    usage.skimage: 3\n    usage.dask: 5\n    "
        ...


class uint32:

    # usage.dask: 1
    __module__: ClassVar[object]

    @classmethod
    def __ne__(_0: numpy.dtype, /):
        "\n    usage.dask: 1\n    "
        ...

    # usage.dask: 2
    ndim: object

    def __add__(self: object, _0: Union[numpy.int64, int], /):
        "\n    usage.skimage: 1\n    usage.dask: 2\n    "
        ...

    def __ge__(self: object, _0: int, /):
        "\n    usage.skimage: 1\n    usage.sklearn: 1\n    "
        ...

    def __le__(self: object, _0: int, /):
        "\n    usage.skimage: 1\n    "
        ...

    def __eq__(self: object, _0: Union[int, numpy.int64], /):
        "\n    usage.skimage: 2\n    usage.sklearn: 1\n    "
        ...

    def __sub__(self: object, _0: Union[numpy.uint32, int], /):
        "\n    usage.sklearn: 2\n    usage.dask: 1\n    "
        ...

    def __gt__(self: object, _0: numpy.uint32, /):
        "\n    usage.sklearn: 1\n    "
        ...

    def __lt__(self: object, _0: numpy.uint32, /):
        "\n    usage.sklearn: 1\n    "
        ...

    def __getitem__(self: object, _0: Tuple[ellipsis, None], /):
        "\n    usage.dask: 1\n    "
        ...

    def __rsub__(self: object, _0: numpy.uint32, /):
        "\n    usage.dask: 1\n    "
        ...

    def __truediv__(self: object, _0: numpy.uint32, /):
        "\n    usage.dask: 1\n    "
        ...

    def __rtruediv__(self: object, _0: numpy.uint32, /):
        "\n    usage.dask: 1\n    "
        ...

    def __mul__(self: object, _0: int, /):
        "\n    usage.dask: 1\n    "
        ...

    def __rmul__(self: object, _0: int, /):
        "\n    usage.dask: 2\n    "
        ...


class uint16:

    # usage.dask: 1
    ndim: object

    def __ge__(self: object, _0: int, /):
        "\n    usage.skimage: 1\n    usage.sklearn: 1\n    "
        ...

    def __add__(self: object, _0: int, /):
        "\n    usage.skimage: 1\n    "
        ...

    def __eq__(self: object, _0: Union[numpy.int64, int], /):
        "\n    usage.skimage: 9\n    "
        ...

    def __le__(self: object, _0: int, /):
        "\n    usage.skimage: 4\n    usage.sklearn: 1\n    "
        ...

    def __ne__(self: object, _0: numpy.uint16, /):
        "\n    usage.skimage: 2\n    "
        ...


class int16:

    # usage.dask: 2
    ndim: object

    def __ge__(self: object, _0: int, /):
        "\n    usage.skimage: 1\n    "
        ...

    def __le__(self: object, _0: int, /):
        "\n    usage.skimage: 3\n    "
        ...

    def __sub__(self: object, _0: numpy.int16, /):
        "\n    usage.skimage: 2\n    "
        ...

    def __rsub__(self: object, _0: numpy.int16, /):
        "\n    usage.skimage: 2\n    "
        ...

    def __rtruediv__(self: object, _0: numpy.float64, /):
        "\n    usage.skimage: 1\n    "
        ...

    def __pow__(self: object, _0: int, /):
        "\n    usage.skimage: 1\n    "
        ...

    def __eq__(self: object, _0: Union[numpy.ndarray, int, numpy.int64], /):
        "\n    usage.skimage: 2\n    usage.xarray: 1\n    "
        ...

    def __ne__(self: object, _0: int, /):
        "\n    usage.sklearn: 1\n    "
        ...

    def __getitem__(self: object, _0: Tuple[ellipsis, None, None], /):
        "\n    usage.dask: 1\n    "
        ...


class int32:

    # usage.dask: 2
    __module__: ClassVar[object]

    @classmethod
    def __ne__(_0: numpy.dtype, /):
        "\n    usage.sklearn: 3\n    usage.dask: 1\n    "
        ...

    # usage.xarray: 1
    # usage.dask: 1
    dtype: object

    # usage.dask: 3
    ndim: object

    # usage.dask: 5
    shape: object

    def __ge__(self: object, _0: Union[int, float], /):
        "\n    usage.skimage: 1\n    usage.sklearn: 2\n    "
        ...

    def __le__(self: object, _0: int, /):
        "\n    usage.skimage: 2\n    usage.sklearn: 2\n    "
        ...

    def __eq__(
        self: object, _0: Union[int, numpy.int64, numpy.int32, numpy.ndarray], /
    ):
        "\n    usage.skimage: 3\n    usage.xarray: 1\n    usage.sklearn: 7\n    usage.dask: 5\n    "
        ...

    def __rmul__(self: object, _0: Union[int, numpy.ndarray], /):
        "\n    usage.sklearn: 1\n    usage.dask: 2\n    "
        ...

    def __add__(self: object, _0: Union[numpy.int64, bool], /):
        "\n    usage.sklearn: 2\n    usage.dask: 2\n    "
        ...

    def __rmod__(self: object, _0: Literal["%d"], /):
        "\n    usage.sklearn: 1\n    "
        ...

    def __sub__(self: object, _0: Union[numpy.int32, int], /):
        "\n    usage.sklearn: 1\n    usage.dask: 1\n    "
        ...

    def __getitem__(self: object, _0: Tuple[Union[None, ellipsis], ...], /):
        "\n    usage.dask: 2\n    "
        ...

    def __rsub__(self: object, _0: numpy.int32, /):
        "\n    usage.dask: 1\n    "
        ...

    def __truediv__(self: object, _0: numpy.int32, /):
        "\n    usage.dask: 1\n    "
        ...

    def __rtruediv__(self: object, _0: numpy.int32, /):
        "\n    usage.dask: 1\n    "
        ...

    def __mul__(self: object, _0: int, /):
        "\n    usage.dask: 1\n    "
        ...


class float32:

    # usage.dask: 1
    shape: ClassVar[object]

    # usage.dask: 1
    __module__: ClassVar[object]

    @classmethod
    def __ne__(_0: numpy.dtype, /):
        "\n    usage.sklearn: 3\n    usage.dask: 2\n    "
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
        "\n    usage.skimage: 5\n    usage.sklearn: 3\n    usage.dask: 2\n    "
        ...

    def __gt__(self: object, _0: Union[int, float, numpy.float64], /):
        "\n    usage.skimage: 4\n    usage.xarray: 1\n    usage.sklearn: 2\n    "
        ...

    def __add__(self: object, _0: Union[numpy.float64, numpy.float32, int], /):
        "\n    usage.skimage: 2\n    usage.sklearn: 2\n    usage.dask: 3\n    "
        ...

    def __ge__(self: object, _0: Union[numpy.float32, float, int], /):
        "\n    usage.skimage: 3\n    usage.sklearn: 1\n    "
        ...

    def __lt__(self: object, _0: Union[numpy.float64, numpy.ndarray, float], /):
        "\n    usage.skimage: 5\n    usage.sklearn: 2\n    "
        ...

    def __truediv__(self: object, _0: Union[numpy.float32, float, numpy.float64], /):
        "\n    usage.skimage: 2\n    usage.sklearn: 3\n    usage.dask: 1\n    "
        ...

    def __rmul__(self: object, _0: Union[int, numpy.ndarray, float, numpy.float32], /):
        "\n    usage.skimage: 4\n    usage.sklearn: 10\n    usage.dask: 2\n    "
        ...

    def __mul__(self: object, _0: Union[int, numpy.float32, float, numpy.ndarray], /):
        "\n    usage.skimage: 1\n    usage.sklearn: 10\n    usage.dask: 1\n    "
        ...

    def __le__(self: object, _0: Union[int, numpy.float32, float, numpy.float64], /):
        "\n    usage.skimage: 4\n    usage.xarray: 2\n    usage.sklearn: 4\n    "
        ...

    def __eq__(self: object, _0: Union[numpy.float32, int, float, numpy.ndarray], /):
        "\n    usage.skimage: 5\n    usage.xarray: 2\n    usage.sklearn: 4\n    usage.dask: 3\n    "
        ...

    def __rtruediv__(
        self: object,
        _0: Union[numpy.float32, float, int, numpy.ndarray, numpy.float64],
        /,
    ):
        "\n    usage.skimage: 1\n    usage.sklearn: 14\n    usage.dask: 1\n    "
        ...

    def __rsub__(
        self: object,
        _0: Union[numpy.float32, numpy.float64, int, numpy.ndarray, float],
        /,
    ):
        "\n    usage.skimage: 3\n    usage.sklearn: 14\n    usage.dask: 1\n    "
        ...

    def __pow__(self: object, _0: int, /):
        "\n    usage.skimage: 1\n    "
        ...

    def __iadd__(self: object, _0: Union[numpy.float32, int], /):
        "\n    usage.xarray: 2\n    usage.sklearn: 2\n    "
        ...

    def __itruediv__(self: object, _0: int, /):
        "\n    usage.sklearn: 2\n    "
        ...

    def __radd__(
        self: object,
        _0: Union[numpy.float32, numpy.ndarray, float, int, numpy.float64],
        /,
    ):
        "\n    usage.sklearn: 9\n    usage.dask: 1\n    "
        ...

    def __ne__(self: object, _0: int, /):
        "\n    usage.sklearn: 1\n    "
        ...

    def __getitem__(self: object, _0: Tuple[Union[None, ellipsis], ...], /):
        "\n    usage.dask: 2\n    "
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
        "\n    usage.skimage: 1\n    "
        ...

    def __neg__(self: object, /):
        "\n    usage.skimage: 2\n    "
        ...

    def __matmul__(self: object, _0: numpy.ndarray, /):
        "\n    usage.skimage: 1\n    "
        ...

    def __rtruediv__(self: object, _0: Union[numpy.ndarray, float], /):
        "\n    usage.sklearn: 3\n    "
        ...

    def max(self: object, /):
        "\n    usage.sklearn: 3\n    "
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
        "\n    usage.sklearn: 2\n    usage.dask: 2\n    "
        ...

    def __sub__(self: object, _0: numpy.ndarray, /):
        "\n    usage.sklearn: 2\n    "
        ...

    def __truediv__(self: object, _0: float, /):
        "\n    usage.sklearn: 1\n    "
        ...

    def __eq__(self: object, _0: float, /):
        "\n    usage.sklearn: 1\n    "
        ...

    def view(self: object, /, *, type: Type[numpy.ndarray]):
        "\n    usage.dask: 2\n    "
        ...

    def all(self: object, /):
        "\n    usage.dask: 2\n    "
        ...

    def __setitem__(self: object, _0: slice[None, int, None], _1: int, /):
        "\n    usage.dask: 1\n    "
        ...


class int8:
    @classmethod
    def __ne__(_0: numpy.dtype, /):
        "\n    usage.dask: 2\n    "
        ...

    # usage.dask: 2
    ndim: object

    def __lt__(self: object, _0: int, /):
        "\n    usage.skimage: 2\n    "
        ...

    def __le__(self: object, _0: int, /):
        "\n    usage.skimage: 2\n    "
        ...

    def __eq__(self: object, _0: Union[numpy.ndarray, numpy.int64, int], /):
        "\n    usage.skimage: 3\n    usage.xarray: 1\n    "
        ...

    def __gt__(self: object, _0: int, /):
        "\n    usage.skimage: 1\n    "
        ...

    def __getitem__(self: object, _0: Tuple[Union[None, ellipsis], ...], /):
        "\n    usage.dask: 2\n    "
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
        "\n    usage.skimage: 1\n    "
        ...

    def __mul__(self: object, _0: numpy.complex128, /):
        "\n    usage.skimage: 2\n    "
        ...

    def __rmul__(self: object, _0: numpy.complex128, /):
        "\n    usage.skimage: 2\n    "
        ...

    def __truediv__(
        self: object, _0: Union[numpy.ndarray, numpy.float64, numpy.complex128], /
    ):
        "\n    usage.skimage: 3\n    "
        ...

    def __rsub__(self: object, _0: float, /):
        "\n    usage.skimage: 1\n    "
        ...

    def __itruediv__(self: object, _0: numpy.float64, /):
        "\n    usage.skimage: 2\n    "
        ...

    def __rtruediv__(self: object, _0: numpy.complex128, /):
        "\n    usage.skimage: 1\n    "
        ...

    def __getitem__(self: object, _0: Tuple[Union[None, ellipsis], ...], /):
        "\n    usage.dask: 2\n    "
        ...


class float16:

    # usage.dask: 1
    ndim: object

    def __sub__(self: object, _0: numpy.float16, /):
        "\n    usage.skimage: 2\n    "
        ...

    def __rsub__(self: object, _0: Union[numpy.ndarray, numpy.float16], /):
        "\n    usage.skimage: 3\n    "
        ...

    def __pow__(self: object, _0: int, /):
        "\n    usage.skimage: 1\n    "
        ...

    def __rmul__(self: object, _0: Union[numpy.ndarray, float], /):
        "\n    usage.skimage: 2\n    "
        ...

    def __eq__(self: object, _0: int, /):
        "\n    usage.skimage: 1\n    "
        ...

    def __gt__(self: object, _0: numpy.float64, /):
        "\n    usage.skimage: 1\n    "
        ...


class nditer:

    # usage.skimage: 1
    multi_index: object

    def __iter__(self: object, /):
        "\n    usage.skimage: 1\n    "
        ...


class longlong:

    # usage.dask: 1
    ndim: object

    def __le__(self: object, _0: int, /):
        "\n    usage.skimage: 1\n    usage.sklearn: 1\n    "
        ...

    def __eq__(self: object, _0: Union[int, numpy.int64], /):
        "\n    usage.skimage: 2\n    usage.sklearn: 5\n    "
        ...

    def __rtruediv__(self: object, _0: Union[numpy.float64, numpy.ndarray], /):
        "\n    usage.sklearn: 3\n    "
        ...

    def __gt__(self: object, _0: int, /):
        "\n    usage.sklearn: 1\n    "
        ...

    def __add__(self: object, _0: int, /):
        "\n    usage.sklearn: 1\n    "
        ...

    def __ge__(self: object, _0: int, /):
        "\n    usage.sklearn: 1\n    "
        ...

    def __mul__(self: object, _0: float, /):
        "\n    usage.sklearn: 1\n    "
        ...


class ulonglong:

    # usage.dask: 1
    ndim: object

    def __le__(self: object, _0: int, /):
        "\n    usage.skimage: 1\n    "
        ...

    def __eq__(self: object, _0: Union[numpy.int64, int], /):
        "\n    usage.skimage: 2\n    "
        ...


class void:

    # usage.dask: 1
    __module__: ClassVar[object]

    # usage.dask: 2
    ndim: object

    def __getitem__(
        self: object, _0: Union[Tuple[Union[ellipsis, None], ...], int, str], /
    ):
        "\n    usage.skimage: 33\n    usage.sklearn: 11\n    usage.dask: 2\n    "
        ...

    def __setitem__(
        self: object, _0: str, _1: Union[int, float, bool, numpy.float64], /
    ):
        "\n    usage.sklearn: 23\n    "
        ...


class errstate:
    def __init__():
        "\n    usage.xarray: 4\n    usage.sklearn: 13\n    usage.dask: 10\n    "
        ...


class vectorize:
    def __init__(pyfunc: Union[Type[int], Callable, functools.partial]):
        "\n    usage.xarray: 75\n    usage.dask: 7\n    "
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
        "\n    usage.xarray: 2\n    usage.dask: 1\n    "
        ...

    def __iadd__(self: object, _0: Union[str, numpy.str_], /):
        "\n    usage.xarray: 12\n    "
        ...

    def __radd__(self: object, _0: str, /):
        "\n    usage.xarray: 11\n    "
        ...

    def __contains__(self: object, _0: Literal[" "], /):
        "\n    usage.xarray: 1\n    "
        ...

    def __ne__(self: object, _0: Union[str, numpy.ndarray], /):
        "\n    usage.xarray: 2\n    usage.sklearn: 7\n    "
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
        "\n    usage.xarray: 6\n    usage.sklearn: 7\n    "
        ...

    def __iter__(self: object, /):
        "\n    usage.sklearn: 2\n    "
        ...


class bytes_:
    def __init__(_0: Union[int, Literal["asdf"]], /):
        "\n    usage.xarray: 1\n    usage.dask: 1\n    "
        ...

    # usage.dask: 1
    ndim: object

    def __getitem__(
        self: object, _0: slice[Union[int, None], Union[int, None], Union[int, None]], /
    ):
        "\n    usage.xarray: 2\n    "
        ...

    def __iadd__(self: object, _0: Union[numpy.bytes_, bytes], /):
        "\n    usage.xarray: 2\n    "
        ...

    def __radd__(self: object, _0: bytes, /):
        "\n    usage.xarray: 1\n    "
        ...

    def __eq__(self: object, _0: numpy.ndarray, /):
        "\n    usage.xarray: 1\n    "
        ...


class timedelta64:
    def __init__(_0: Union[int, datetime.timedelta], _1: Literal["D", "ns"], /):
        "\n    usage.xarray: 1\n    usage.dask: 7\n    "
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
        "\n    usage.xarray: 7\n    usage.dask: 2\n    "
        ...

    def __truediv__(self: object, _0: numpy.timedelta64, /):
        "\n    usage.xarray: 3\n    "
        ...

    def __rmul__(self: object, _0: Union[numpy.ndarray, float], /):
        "\n    usage.xarray: 5\n    "
        ...

    def __add__(self: object, _0: numpy.ndarray, /):
        "\n    usage.xarray: 1\n    "
        ...

    def __ne__(self: object, _0: numpy.ndarray, /):
        "\n    usage.xarray: 1\n    "
        ...

    def __rsub__(self: object, _0: pandas.core.indexes.datetimes.DatetimeIndex, /):
        "\n    usage.xarray: 1\n    "
        ...

    def __eq__(self: object, _0: numpy.timedelta64, /):
        "\n    usage.xarray: 4\n    "
        ...


class datetime64:
    def __init__(_0: Literal["NaT", "2014"], /):
        "\n    usage.dask: 3\n    "
        ...

    # usage.xarray: 3
    # usage.dask: 1
    dtype: object

    # usage.dask: 1
    ndim: object

    def __add__(self: object, _0: numpy.ndarray, /):
        "\n    usage.xarray: 4\n    "
        ...

    def __rsub__(self: object, _0: numpy.ndarray, /):
        "\n    usage.xarray: 1\n    "
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
        "\n    usage.xarray: 14\n    "
        ...

    def __le__(self: object, _0: pandas._libs.tslibs.timestamps.Timestamp, /):
        "\n    usage.dask: 1\n    "
        ...


class broadcast:
    def __init__(
        _0: Union[dask.array.core.Array, int, numpy.ndarray, List[int]],
        _1: Union[Literal["z", "_not_supplied"], numpy.ndarray, List[int]] = ...,
        _2: numpy.ndarray = ...,
        /,
    ):
        "\n    usage.xarray: 14\n    "
        ...

    # usage.xarray: 4
    shape: object


class object_:
    def __init__(_0: Union[int, bytes], /):
        "\n    usage.xarray: 1\n    usage.dask: 1\n    "
        ...

    @classmethod
    def __ne__(_0: numpy.dtype, /):
        "\n    usage.dask: 1\n    "
        ...


class ndenumerate:
    def __iter__(self: object, /):
        "\n    usage.xarray: 2\n    "
        ...


class memmap:

    # usage.sklearn: 1
    __name__: ClassVar[object]

    # usage.dask: 1
    __module__: ClassVar[object]

    @classmethod
    def __rmod__(_0: Literal["Expected sequence or array-like, got %s"], /):
        "\n    usage.sklearn: 1\n    "
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
        "\n    usage.sklearn: 17\n    usage.dask: 7\n    "
        ...

    def mean(self: object, /, *, axis: int):
        "\n    usage.sklearn: 2\n    "
        ...

    def __isub__(self: object, _0: Union[numpy.float64, numpy.ndarray], /):
        "\n    usage.sklearn: 4\n    "
        ...

    def __pow__(self: object, _0: int, /):
        "\n    usage.sklearn: 1\n    "
        ...

    def __setitem__(
        self: object,
        _0: Union[int, numpy.int64, Tuple[slice[None, None, None], numpy.ndarray]],
        _1: numpy.ndarray,
        /,
    ):
        "\n    usage.sklearn: 5\n    "
        ...

    def __add__(self: object, _0: numpy.memmap, /):
        "\n    usage.dask: 1\n    "
        ...

    def __radd__(self: object, _0: numpy.memmap, /):
        "\n    usage.dask: 1\n    "
        ...


class complex64:

    # usage.dask: 2
    ndim: object

    def __getitem__(self: object, _0: Tuple[ellipsis, None, None], /):
        "\n    usage.dask: 1\n    "
        ...


class float128:

    # usage.dask: 1
    ndim: object


class complex256:

    # usage.dask: 1
    ndim: object


class AxisError:
    def __init__(axis: str):
        "\n    usage.dask: 9\n    "
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
        "\n    usage.dask: 3\n    "
        ...

    def all(self: object, /):
        "\n    usage.dask: 2\n    "
        ...

    def __getitem__(self: object, _0: slice[None, int, None], /):
        "\n    usage.dask: 1\n    "
        ...


class record:

    # usage.dask: 2
    ndim: object

    def __getitem__(self: object, _0: Tuple[ellipsis, None], /):
        "\n    usage.dask: 1\n    "
        ...
