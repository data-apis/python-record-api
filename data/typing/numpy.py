random = ...
abs = ...
testing = ...
r_ = ...
floating = ...
newaxis = ...
pi = ...
float = ...
bool = ...
int = ...
ogrid = ...
integer = ...
mgrid = ...
round = ...
float16 = ...
float_ = ...
nan = ...
min = ...
max = ...
double = ...
inf = ...
intp = ...
linalg = ...
divide = ...
signedinteger = ...
complex = ...
unsignedinteger = ...
__version__ = ...
int_ = ...
typecodes = ...
e = ...
c_ = ...
uint = ...
NaN = ...
ma = ...
NAN = ...
bitwise_xor = ...
complex64 = ...
s_ = ...
bool8 = ...
ubyte = ...
inexact = ...
character = ...
number = ...
string_ = ...
complexfloating = ...
lib = ...


def arange(
    _0: Union[(float, int, numpy.int64, numpy.float64, dask.array.core.Array)],
    _1: Union[(int, float, numpy.float64, numpy.int64)] = ...,
    _2: Union[(int, None, float, numpy.float64)] = ...,
    _3: list[numpy.uint8] = ...,
    /,
    *,
    dtype=...,
):
    "usage.sample_usage: 4\nusage.skimage: 223\nusage.xarray: 393"


def array(
    _0=...,
    /,
    *,
    dtype=...,
    copy: bool = ...,
    ndmin: int = ...,
    order: Literal[("C", "F", "K")] = ...,
):
    "usage.sample_usage: 1\nusage.skimage: 1076\nusage.xarray: 391"


def zeros(_0=..., /, *, dtype=..., order: Literal[("C", "F")] = ...):
    "usage.sample_usage: 1\nusage.skimage: 787\nusage.xarray: 52"


def ones(shape, dtype=..., order: Literal[("F",)] = ...):
    "usage.sample_usage: 1\nusage.skimage: 269\nusage.xarray: 59"


def linspace(
    start: Union[(int, float, numpy.float64, numpy.int64)],
    stop: Union[(numpy.float32, float, int, numpy.float64, numpy.int64)] = ...,
    num: Union[(int, numpy.int64)] = ...,
):
    "usage.sample_usage: 1\nusage.skimage: 70\nusage.xarray: 95"


def eye(N: int, M: int = ..., dtype: list = ...):
    "usage.sample_usage: 1\nusage.skimage: 39"


def add(
    _0: Union[
        (
            float,
            xarray.core.dataarray.DataArray,
            numpy.ndarray,
            xarray.core.dataset.Dataset,
            dask.array.core.Array,
        )
    ],
    _1,
    /,
    *,
    dtype: list = ...,
    out: Union[(numpy.ndarray, xarray.core.dataarray.DataArray)] = ...,
):
    "usage.sample_usage: 1\nusage.skimage: 11\nusage.xarray: 13"


def exp(
    _0: Union[(int, float, xarray.core.dataarray.DataArray, numpy.ndarray)],
    /,
    *,
    dtype: numpy.dtype = ...,
):
    "usage.sample_usage: 1\nusage.skimage: 26\nusage.xarray: 3"


def log(_0, /):
    "usage.sample_usage: 1\nusage.skimage: 19\nusage.xarray: 2"


def column_stack(
    tup: Union[(tuple[(numpy.ndarray, numpy.ndarray)], list[numpy.ndarray])]
):
    "usage.sample_usage: 1\nusage.skimage: 9"


def concatenate(_0, /, *, axis: int = ...):
    "usage.sample_usage: 1\nusage.skimage: 48\nusage.xarray: 45"


def absolute(_0, /):
    "usage.skimage: 113"


def asarray(a, dtype=..., order: Literal[("C",)] = ...):
    "usage.skimage: 247\nusage.xarray: 837"


def sum(a, axis=..., dtype: Union[(None, list[float])] = ..., keepdims: bool = ...):
    "usage.skimage: 125\nusage.xarray: 51"


def vstack(
    tup: Union[
        (
            tuple[(numpy.ndarray, numpy.ndarray)],
            tuple[
                (
                    Union[
                        (list[Union[(int, float)]], numpy.ndarray, list[numpy.int64])
                    ],
                    Union[
                        (list[Union[(int, float)]], numpy.ndarray, list[numpy.int64])
                    ],
                )
            ],
            tuple[(numpy.ndarray, numpy.ndarray, numpy.ndarray)],
            list[numpy.ndarray],
        )
    ]
):
    "usage.skimage: 33"


def all(a: Union[(numpy.ma.core.MaskedArray, numpy.ndarray)] = ...):
    "usage.skimage: 113\nusage.xarray: 14"


def round_(a=...):
    "usage.skimage: 30"


def asanyarray(a=...):
    "usage.skimage: 50"


def obj2sctype(rep):
    "usage.skimage: 14"


def issubdtype(arg1, arg2: list):
    "usage.skimage: 162\nusage.xarray: 256"


def multiply(
    _0: numpy.ndarray,
    _1: Union[(int, float, dask.array.core.Array, numpy.ndarray)],
    /,
    *,
    out: numpy.ndarray = ...,
    dtype: Union[(list, numpy.dtype, list[numpy.float32], list[numpy.float64])] = ...,
):
    "usage.skimage: 25\nusage.xarray: 2"


def reshape(a: Union[(numpy.ndarray, list[int], list[float])], newshape=...):
    "usage.skimage: 43\nusage.xarray: 7"


def sqrt(_0=..., /, *, out: numpy.ndarray = ...):
    "usage.skimage: 112\nusage.xarray: 4"


def moveaxis(
    a: Union[(int, numpy.float64, numpy.ndarray)],
    source: Union[(tuple[(None, ...)], numpy.ndarray, int, range)],
    destination: Union[(tuple[(None, ...)], numpy.ndarray, list[int], int)],
):
    "usage.skimage: 6\nusage.xarray: 17"


def rollaxis(a: numpy.ndarray, axis: int = ...):
    "usage.skimage: 14"


def any(a: Union[(numpy.bool_, list[bool], numpy.ndarray)] = ...):
    "usage.skimage: 39\nusage.xarray: 5"


def empty_like(
    _0: Union[
        (
            numpy.ma.core.MaskedArray,
            xarray.core.variable.IndexVariable,
            numpy.ndarray,
            xarray.core.variable.Variable,
        )
    ] = ...,
    /,
    *,
    dtype: list = ...,
    subok: bool = ...,
    order: Literal[("C",)] = ...,
):
    "usage.skimage: 48\nusage.xarray: 2"


def triu(m: numpy.ndarray):
    "usage.skimage: 1"


def seterr(
    invalid: Literal[("warn", "ignore")],
    divide: Literal[("warn",)] = ...,
    over: Literal[("warn",)] = ...,
    under: Literal[("ignore",)] = ...,
):
    "usage.skimage: 2"


def isnan(
    _0: Union[
        (
            float,
            xarray.core.dataarray.DataArray,
            list[float],
            numpy.ndarray,
            numpy.float64,
        )
    ],
    /,
):
    "usage.skimage: 14\nusage.xarray: 14"


def floor(
    _0: Union[(numpy.float64, float, xarray.core.dataarray.DataArray, numpy.ndarray)], /
):
    "usage.skimage: 13\nusage.xarray: 2"


def stack(arrays=...):
    "usage.skimage: 35\nusage.xarray: 26"


def choose(a: numpy.ndarray, choices: list[numpy.ndarray]):
    "usage.skimage: 2"


def amin(a=...):
    "usage.skimage: 60\nusage.xarray: 25"


def amax(
    a,
    axis: Union[(int, None, tuple[(int, int)], tuple[(int, int, int)])] = ...,
    keepdims: bool = ...,
):
    "usage.skimage: 105\nusage.xarray: 23"


def rint(
    _0: Union[(xarray.core.dataarray.DataArray, numpy.ndarray)],
    /,
    *,
    out: numpy.ndarray = ...,
):
    "usage.skimage: 2\nusage.xarray: 2"


def clip(a: Union[(numpy.ndarray, int, numpy.float64)], a_min, a_max=...):
    "usage.skimage: 61"


def power(_0: Union[(numpy.ndarray, int)], _1: Union[(numpy.ndarray, int, float)], /):
    "usage.skimage: 11"


def log10(
    _0: Union[(numpy.float64, xarray.core.dataarray.DataArray, numpy.ndarray)], /
):
    "usage.skimage: 4\nusage.xarray: 2"


def load(file: Literal[("/Users/saul/Downloads/scikit-image-0.17.0/skimage/",)]):
    "usage.skimage: 28"


def meshgrid(*xi: Literal[("v", "t")]):
    "usage.skimage: 28\nusage.xarray: 6"


def dstack(
    tup: Union[
        (
            tuple[(numpy.ndarray, ...)],
            list[skimage.feature._hessian_det_appx._memoryviewslice],
            list[numpy.ndarray],
        )
    ]
):
    "usage.skimage: 12"


def nonzero(a: numpy.ndarray):
    "usage.skimage: 22\nusage.xarray: 4"


def cbrt(_0: numpy.ndarray, /):
    "usage.skimage: 4"


def hypot(
    _0: Union[(int, numpy.float64, xarray.core.dataarray.DataArray, numpy.ndarray)],
    _1: Union[(int, numpy.float64, xarray.core.dataarray.DataArray, numpy.ndarray)],
    /,
):
    "usage.skimage: 13\nusage.xarray: 2"


def arctan2(
    _0: Union[
        (numpy.int64, numpy.float64, xarray.core.dataarray.DataArray, numpy.ndarray)
    ],
    _1: Union[
        (numpy.int64, numpy.float64, xarray.core.dataarray.DataArray, numpy.ndarray)
    ],
    /,
):
    "usage.skimage: 8\nusage.xarray: 2"


def where(
    _0: Union[(numpy.bool_, numpy.ndarray, list[bool], dask.array.core.Array, bool)],
    _1: Union[(int, float, numpy.float64, numpy.ndarray)] = ...,
    _2: Union[(int, numpy.float64, dask.array.core.Array, numpy.ndarray)] = ...,
    /,
):
    "usage.skimage: 26\nusage.xarray: 23"


def cos(_0, /):
    "usage.skimage: 48\nusage.xarray: 14"


def sin(_0, /, *, out=...):
    "usage.skimage: 47\nusage.xarray: 18"


def ascontiguousarray(
    a: Union[(list[Union[(int, float)]], list[int], list[float], numpy.ndarray)] = ...
):
    "usage.skimage: 67"


def swapaxes(a: numpy.ndarray, axis1: int, axis2: int):
    "usage.skimage: 4\nusage.xarray: 8"


def ravel(a):
    "usage.skimage: 12\nusage.xarray: 44"


def squeeze(a: numpy.ndarray = ...):
    "usage.skimage: 16"


def ones_like(a: Union[(numpy.ndarray, xarray.core.variable.Variable)] = ...):
    "usage.skimage: 26\nusage.xarray: 4"


def can_cast(
    _0: Union[(int, float, numpy.dtype, numpy.ndarray)],
    _1: Union[(numpy.dtype, list[bool])],
    /,
    *,
    casting: Literal[("safe",)] = ...,
):
    "usage.skimage: 9"


def empty(
    _0=...,
    _1=...,
    /,
    *,
    dtype=...,
    order: Literal[("C", "F")] = ...,
    shape: tuple[(int,)] = ...,
):
    "usage.skimage: 129\nusage.xarray: 11"


def min_scalar_type(_0: Union[(numpy.int64, int, numpy.float64)], /):
    "usage.skimage: 5"


def unique(
    ar: Union[(xarray.core.dataarray.DataArray, numpy.ndarray)] = ...,
    return_inverse: bool = ...,
    return_counts: bool = ...,
):
    "usage.skimage: 68\nusage.xarray: 14"


def zeros_like(
    a: Union[(tuple[(int, int, int)], numpy.ndarray, tuple[(int, int)])],
    dtype: list = ...,
    order: Literal[("C",)] = ...,
):
    "usage.skimage: 70\nusage.xarray: 43"


def full(shape, fill_value=...):
    "usage.skimage: 36\nusage.xarray: 10"


def loadtxt(
    fname: Literal[("/Users/saul/Downloads/scikit-image-0.17.0/skimage/",)],
    dtype: list[tuple[(Literal[("1", "b1", "pair", "L1", "a1")], list)]],
):
    "usage.skimage: 1"


def logical_and(
    _0: Union[(numpy.bool_, xarray.core.dataarray.DataArray, numpy.ndarray)],
    _1: Union[(numpy.bool_, xarray.core.dataarray.DataArray, numpy.ndarray)],
    /,
):
    "usage.skimage: 13\nusage.xarray: 2"


def deg2rad(
    _0: Union[(int, xarray.core.dataarray.DataArray, list[int], numpy.ndarray)], /
):
    "usage.skimage: 18\nusage.xarray: 2"


def rad2deg(
    _0: Union[(numpy.float64, xarray.core.dataarray.DataArray, numpy.ndarray)], /
):
    "usage.skimage: 6\nusage.xarray: 2"


def maximum(
    _0,
    _1,
    /,
    *,
    out: numpy.ndarray = ...,
    dtype: numpy.dtype = ...,
    casting: Literal[("unsafe",)] = ...,
):
    "usage.skimage: 16\nusage.xarray: 87"


def percentile(
    a: numpy.ndarray,
    q: Union[(float, list[int], numpy.ndarray, int, numpy.float64)] = ...,
):
    "usage.skimage: 11\nusage.xarray: 20"


def logical_not(
    _0: Union[
        (
            numpy.bool_,
            xarray.core.dataarray.DataArray,
            numpy.ndarray,
            dask.array.core.Array,
            bool,
        )
    ],
    /,
    *,
    out: numpy.ndarray = ...,
):
    "usage.skimage: 14\nusage.xarray: 10"


def isscalar(element):
    "usage.skimage: 67\nusage.xarray: 33"


def ceil(_0, /):
    "usage.skimage: 31\nusage.xarray: 5"


def minimum(
    _0: Union[
        (
            tuple[(int, int, int)],
            xarray.core.dataarray.DataArray,
            numpy.ndarray,
            tuple[(int, int)],
        )
    ],
    _1,
    /,
):
    "usage.skimage: 9\nusage.xarray: 4"


def dot(_0: numpy.ndarray, _1: numpy.ndarray, /):
    "usage.skimage: 1"


def diag(v: numpy.ndarray):
    "usage.skimage: 5"


def arcsin(_0: Union[(float, xarray.core.dataarray.DataArray, numpy.ndarray)], /):
    "usage.skimage: 1\nusage.xarray: 2"


def ellipkinc(_0: numpy.float64, _1: float, /):
    "usage.skimage: 1"


def ellipeinc(_0: numpy.float64, _1: float, /):
    "usage.skimage: 1"


def transpose(a=...):
    "usage.skimage: 21\nusage.xarray: 3"


def shape(a: Union[(numpy.ma.core.MaskedArray, numpy.ndarray)]):
    "usage.skimage: 1\nusage.xarray: 11"


def promote_types(_0: numpy.dtype, _1: numpy.dtype, /):
    "usage.skimage: 1"


def bincount(
    _0: Union[(dask.array.core.Array, numpy.ndarray)], /, *, minlength: int = ...
):
    "usage.skimage: 12"


def histogram(
    a: numpy.ndarray = ...,
    bins: Union[
        (
            list[Union[(int, float)]],
            numpy.int64,
            int,
            tuple[
                (
                    numpy.float64,
                    numpy.float64,
                    numpy.float64,
                    numpy.float64,
                    numpy.float64,
                )
            ],
        )
    ] = ...,
):
    "usage.skimage: 7"


def interp(
    x: Union[(numpy.ndarray, numpy.flatiter)], xp: numpy.ndarray, fp: numpy.ndarray
):
    "usage.skimage: 6"


def polyfit(x: numpy.ndarray, y: numpy.ndarray, deg: int):
    "usage.skimage: 1"


def pad(array: Union[(list[int], numpy.ndarray, list[list[int]])], pad_width=...):
    "usage.skimage: 126\nusage.xarray: 44"


def product(*args: Literal[("v", "t")]):
    "usage.skimage: 14"


def apply_along_axis(func1d: Callable, axis: int, arr: numpy.ndarray):
    "usage.skimage: 8"


def count_nonzero(a: numpy.ndarray):
    "usage.skimage: 9"


def cumsum(a=...):
    "usage.skimage: 29\nusage.xarray: 10"


def take_along_axis(arr: numpy.ndarray, indices: numpy.ndarray, axis: int):
    "usage.skimage: 1"


def square(_0: Union[(xarray.core.dataarray.DataArray, numpy.ndarray)], /):
    "usage.skimage: 7\nusage.xarray: 2"


def mean(
    a: Union[
        (
            xarray.core.dataarray.DataArray,
            numpy.ndarray,
            xarray.core.variable.Variable,
            dask.array.core.Array,
            list[numpy.float64],
        )
    ],
    axis: Union[(int, None, tuple[(int,)], tuple[(int, int)])] = ...,
    keepdims: bool = ...,
    dtype: Union[(list[float], None, list)] = ...,
):
    "usage.skimage: 61\nusage.xarray: 32"


def log2(_0: Union[(int, xarray.core.dataarray.DataArray, numpy.ndarray)], /):
    "usage.skimage: 5\nusage.xarray: 2"


def allclose(
    a: Union[
        (
            xarray.core.dataarray.DataArray,
            list[int],
            numpy.ndarray,
            numpy.float64,
            list[numpy.float64],
        )
    ],
    b,
    rtol: Union[(int, float)] = ...,
    equal_nan: bool = ...,
    atol: float = ...,
):
    "usage.skimage: 33\nusage.xarray: 20"


def argsort(a: Union[(numpy.ndarray, numpy.flatiter)]):
    "usage.skimage: 28"


def hstack(tup):
    "usage.skimage: 27\nusage.xarray: 1"


def argmax(a: Union[(dask.array.core.Array, numpy.ndarray)] = ...):
    "usage.skimage: 18\nusage.xarray: 11"


def logspace(
    start: Union[(float, numpy.float64)], stop: Union[(float, numpy.float64)], num: int
):
    "usage.skimage: 2"


def logical_or(
    _0: Union[(xarray.core.dataarray.DataArray, numpy.ndarray)],
    _1: Union[(xarray.core.dataarray.DataArray, numpy.ndarray)],
    /,
):
    "usage.skimage: 3\nusage.xarray: 2"


def isinf(_0: Union[(float, xarray.core.dataarray.DataArray, numpy.ndarray)], /):
    "usage.skimage: 2\nusage.xarray: 2"


def delete(arr: numpy.ndarray, obj: tuple[(Union[(int, None)], ...)], axis: int):
    "usage.skimage: 3"


def split(ary: numpy.ndarray, indices_or_sections: int):
    "usage.skimage: 1"


def atleast_1d(*arys: Literal[("v", "t")]):
    "usage.skimage: 11\nusage.xarray: 23"


def isclose(
    a: Union[(numpy.float64, float, numpy.ndarray)],
    b: Union[(int, numpy.float64, numpy.ndarray, float)],
    rtol: float = ...,
    atol: float = ...,
    equal_nan: bool = ...,
):
    "usage.skimage: 3\nusage.xarray: 12"


def gradient(
    f: Union[(xarray.core.dataarray.DataArray, numpy.ndarray)],
    *varargs: Literal[("v", "t")],
):
    "usage.skimage: 8\nusage.xarray: 5"


def argmin(a: Union[(list[numpy.float64], numpy.ndarray)] = ...):
    "usage.skimage: 10\nusage.xarray: 5"


def arctan(
    _0: Union[(numpy.float64, xarray.core.dataarray.DataArray, numpy.ndarray)], /
):
    "usage.skimage: 3\nusage.xarray: 2"


def sort(a: numpy.ndarray = ...):
    "usage.skimage: 14\nusage.xarray: 2"


def spacing(_0: int, /):
    "usage.skimage: 1"


def isfinite(
    _0: Union[
        (
            tuple[(numpy.ndarray, numpy.ndarray)],
            list[Union[(numpy.int64, numpy.float64)]],
            xarray.core.dataarray.DataArray,
            numpy.ndarray,
        )
    ],
    /,
):
    "usage.skimage: 7\nusage.xarray: 6"


def diff(a: numpy.ndarray, n: int = ..., axis: int = ...):
    "usage.skimage: 15\nusage.xarray: 11"


def flatnonzero(a: numpy.ndarray):
    "usage.skimage: 6\nusage.xarray: 2"


def copy(a: Union[(numpy.ndarray, numpy.float64)]):
    "usage.skimage: 14"


def atleast_2d(*arys: Literal[("v", "t")]):
    "usage.skimage: 7\nusage.xarray: 2"


def rot90(m: numpy.ndarray = ...):
    "usage.skimage: 7"


def roll(
    a: Union[(list[Union[(int, float)]], numpy.ndarray)],
    shift: Union[(int, tuple[(int, int)])] = ...,
):
    "usage.skimage: 14\nusage.xarray: 1"


def indices(dimensions: tuple[(Union[(numpy.int64, int)], ...)] = ...):
    "usage.skimage: 6"


def tri(N: int = ..., M: int = ..., k: int = ...):
    "usage.skimage: 9"


def less(
    _0: Union[(tuple[(int, ...)], numpy.ndarray)],
    _1: Union[(tuple[(int, ...)], numpy.ndarray)],
    /,
):
    "usage.skimage: 3\nusage.xarray: 1"


def prod(a):
    "usage.skimage: 9\nusage.xarray: 15"


def true_divide(
    _0: numpy.ndarray,
    _1: Union[(numpy.int64, numpy.ndarray)],
    /,
    *,
    out: numpy.ndarray = ...,
):
    "usage.skimage: 2"


def unravel_index(
    _0: Union[(numpy.int64, int, numpy.ndarray)], _1: tuple[(int, ...)], /
):
    "usage.skimage: 18"


def apply_over_axes(func: Callable, a: numpy.ndarray, axes: tuple[(int, int)]):
    "usage.skimage: 10"


def tile(
    A: Union[(tuple[(int, int)], list[int], numpy.ndarray)],
    reps: Union[
        (
            tuple[(int, int, int)],
            tuple[(int, int, int, int)],
            list[int],
            tuple[(int, int)],
            tuple[(int, ...)],
        )
    ],
):
    "usage.skimage: 15\nusage.xarray: 5"


def real(val: Union[(float, xarray.core.dataarray.DataArray, numpy.ndarray)]):
    "usage.skimage: 8\nusage.xarray: 1"


def imag(val: Union[(xarray.core.dataarray.DataArray, numpy.ndarray)]):
    "usage.skimage: 1\nusage.xarray: 1"


def sign(_0: Union[(int, xarray.core.dataarray.DataArray, numpy.ndarray)], /):
    "usage.skimage: 4\nusage.xarray: 3"


def subtract(
    _0: Union[(int, numpy.ndarray)],
    _1: Union[(numpy.ndarray, dask.array.core.Array)],
    /,
    *,
    dtype: numpy.dtype = ...,
):
    "usage.skimage: 11\nusage.xarray: 2"


def ix_(*args: Literal[("v", "t")]):
    "usage.skimage: 2\nusage.xarray: 3"


def convolve(a: numpy.ndarray, v: list[float], mode: Literal[("valid",)]):
    "usage.skimage: 1"


def invert(_0: Union[(numpy.ndarray, list[bool])], /):
    "usage.skimage: 7"


def array_equal(
    a1: Union[(tuple[(float, float, float)], list[int], numpy.ndarray)],
    a2: Union[(tuple[(int, int, int)], numpy.ndarray, tuple[(int, int)])],
):
    "usage.skimage: 5\nusage.xarray: 3"


def reciprocal(_0: numpy.ndarray, /, *, out: numpy.ndarray = None):
    "usage.skimage: 1"


def insert(arr: numpy.ndarray, obj: int, values: numpy.ndarray, axis: int):
    "usage.skimage: 3"


def full_like(
    a: Union[
        (xarray.core.dataarray.DataArray, numpy.ndarray, xarray.core.variable.Variable)
    ],
    fill_value: Union[(int, float, bool)] = ...,
):
    "usage.skimage: 1\nusage.xarray: 7"


def sctype2char(sctype: numpy.dtype):
    "usage.skimage: 2"


def floor_divide(
    _0: numpy.ndarray,
    _1: int,
    /,
    *,
    out: numpy.ndarray = None,
    dtype: numpy.dtype = None,
    casting: Literal[("unsafe",)] = None,
):
    "usage.skimage: 4"


def fromfile(_0: _io.TextIOWrapper, /, *, sep: Literal[(" ",)] = None):
    "usage.skimage: 1"


def median(a: numpy.ndarray = ...):
    "usage.skimage: 5\nusage.xarray: 1"


def asfortranarray(a: numpy.ndarray):
    "usage.skimage: 1"


def cross(a: numpy.ndarray, b: numpy.ndarray):
    "usage.skimage: 5"


def einsum(*operands: Literal[("v", "t")]):
    "usage.skimage: 1\nusage.xarray: 44"


def nan_to_num(x: list[numpy.float64]):
    "usage.skimage: 1"


def frombuffer(_0: bytes, /, *, dtype: Literal[("int8",)] = None):
    "usage.skimage: 1"


def fliplr(m: numpy.ndarray):
    "usage.skimage: 5"


def tril(m: numpy.ndarray):
    "usage.skimage: 1"


def flip(m: numpy.ndarray, axis: int):
    "usage.skimage: 3"


def flipud(m: numpy.ndarray):
    "usage.skimage: 2\nusage.xarray: 2"


def set_printoptions(
    precision: int = ...,
    edgeitems: int = ...,
    linewidth: int = ...,
    suppress: bool = ...,
    nanstr: Literal[("nan",)] = ...,
    infstr: Literal[("inf",)] = ...,
    formatter: None = ...,
    sign: Literal[("-",)] = ...,
    floatmode: Literal[("maxprec",)] = ...,
):
    "usage.skimage: 1\nusage.xarray: 3"


def result_type(
    _0,
    _1=...,
    _2: Union[(numpy.ndarray, list[numpy.float32], dask.array.core.Array)] = ...,
    _3: Union[(numpy.ndarray, dask.array.core.Array)] = ...,
    _4: Union[(numpy.ndarray, dask.array.core.Array)] = ...,
    _5: Union[(numpy.ndarray, dask.array.core.Array)] = ...,
    _6: Union[(numpy.ndarray, dask.array.core.Array)] = ...,
    _7: Union[(numpy.ndarray, dask.array.core.Array)] = ...,
    _8: Union[(numpy.ndarray, dask.array.core.Array)] = ...,
    _9: Union[(numpy.ndarray, dask.array.core.Array)] = ...,
    _10: Union[(numpy.ndarray, dask.array.core.Array)] = ...,
    _11: Union[(numpy.ndarray, dask.array.core.Array)] = ...,
    _12: Union[(numpy.ndarray, dask.array.core.Array)] = ...,
    _13: Union[(numpy.ndarray, dask.array.core.Array)] = ...,
    _14: Union[(numpy.ndarray, dask.array.core.Array)] = ...,
    _15: Union[(numpy.ndarray, dask.array.core.Array)] = ...,
    _16: Union[(numpy.ndarray, dask.array.core.Array)] = ...,
    _17: Union[(numpy.ndarray, dask.array.core.Array)] = ...,
    _18: Union[(numpy.ndarray, dask.array.core.Array)] = ...,
    _19: Union[(numpy.ndarray, dask.array.core.Array)] = ...,
    /,
):
    "usage.skimage: 7\nusage.xarray: 94"


def ptp(a: numpy.ndarray):
    "usage.skimage: 10"


def cumprod(a: Union[(tuple[(int, ...)], numpy.ndarray)] = ...):
    "usage.skimage: 5\nusage.xarray: 4"


def ravel_multi_index(
    _0, _1: tuple[(int, ...)], /, *, order: Literal[("C", "F")] = ...
):
    "usage.skimage: 18"


def logical_xor(
    _0: Union[(xarray.core.dataarray.DataArray, numpy.ndarray)],
    _1: Union[(xarray.core.dataarray.DataArray, numpy.ndarray)],
    /,
    *,
    out: numpy.ndarray = ...,
):
    "usage.skimage: 1\nusage.xarray: 2"


def in1d(
    ar1: Union[(numpy.ndarray, numpy.flatiter)],
    ar2: Union[(numpy.ndarray, tuple[(int, int)])],
):
    "usage.skimage: 2"


def take(a: numpy.ndarray, indices: Union[(int, numpy.ndarray, list[int])] = ...):
    "usage.skimage: 1\nusage.xarray: 11"


def lexsort(
    _0: tuple[(Union[(xarray.core.dataarray.DataArray, numpy.ndarray)], ...)], /
):
    "usage.skimage: 1\nusage.xarray: 2"


def fmax(
    _0: Union[(xarray.core.dataarray.DataArray, numpy.ndarray)],
    _1: Union[(float, numpy.float64, xarray.core.dataarray.DataArray, numpy.ndarray)],
    /,
):
    "usage.skimage: 3\nusage.xarray: 2"


def fix(x: Union[(numpy.float64, float, xarray.core.dataarray.DataArray)]):
    "usage.skimage: 2\nusage.xarray: 1"


def tensordot(
    a: numpy.ndarray,
    b: Union[(range, numpy.ndarray)],
    axes: Union[(tuple[(int, int)], list[int], tuple[(list[int], list[int])])],
):
    "usage.skimage: 1\nusage.xarray: 5"


def atleast_3d(*arys: Literal[("v", "t")]):
    "usage.skimage: 11"


def iscomplexobj(x: numpy.ndarray):
    "usage.skimage: 4"


def conjugate(_0: Union[(xarray.core.dataarray.DataArray, numpy.ndarray)], /):
    "usage.skimage: 2\nusage.xarray: 2"


def angle(z: Union[(xarray.core.dataarray.DataArray, numpy.ndarray)]):
    "usage.skimage: 3\nusage.xarray: 2"


def require(
    a: numpy.ndarray, dtype: list[numpy.uint8], requirements: list[Literal[("C",)]]
):
    "usage.skimage: 1"


def tanh(_0: Union[(xarray.core.dataarray.DataArray, numpy.ndarray)], /):
    "usage.skimage: 2\nusage.xarray: 2"


def ndim(a: numpy.ndarray):
    "usage.skimage: 4"


def searchsorted(a: numpy.ndarray, v: Union[(int, numpy.float64, numpy.ndarray)]):
    "usage.skimage: 3\nusage.xarray: 1"


def fill_diagonal(a: numpy.ndarray, val: float):
    "usage.skimage: 1"


def array2string(a: numpy.ndarray, separator: Literal[(", ",)]):
    "usage.skimage: 1"


def std(a: numpy.ndarray = ...):
    "usage.skimage: 1\nusage.xarray: 3"


def hamming(M: int):
    "usage.skimage: 1"


def hanning(M: int):
    "usage.skimage: 1"


def around(a: Union[(tuple[(numpy.float64, numpy.float64)], numpy.ndarray)]):
    "usage.skimage: 1\nusage.xarray: 4"


def alltrue(*args: Literal[("v", "t")]):
    "usage.skimage: 2"


def may_share_memory(_0: numpy.ndarray, _1: numpy.ndarray, /):
    "usage.skimage: 2"


def isnat(_0: Union[(numpy.ndarray, dask.array.core.Array)], /):
    "usage.xarray: 6"


def get_printoptions():
    "usage.xarray: 3"


def broadcast_arrays(*args: Literal[("v", "t")]):
    "usage.xarray: 3"


def broadcast_to(
    array: Union[(numpy.ndarray, float)], shape: tuple[(Union[(None, int)], ...)]
):
    "usage.xarray: 25"


def nanmean(
    a: numpy.ndarray,
    axis: Union[
        (int, None, tuple[(int,)], tuple[(None, ...)], tuple[(int, int)])
    ] = ...,
    dtype: Union[
        (
            list[numpy.float16],
            list[numpy.float64],
            list[float],
            None,
            list[numpy.float32],
        )
    ] = ...,
):
    "usage.xarray: 21"


def nanstd(
    a: numpy.ndarray, axis: Union[(None, int)], dtype: None = ..., ddof: int = ...
):
    "usage.xarray: 3"


def nanargmax(a: numpy.ndarray, axis: Union[(None, int)]):
    "usage.xarray: 5"


def nanargmin(a: numpy.ndarray, axis: int):
    "usage.xarray: 4"


def expand_dims(a: numpy.ndarray, axis: int):
    "usage.xarray: 5"


def nanquantile(
    a: numpy.ndarray,
    q: numpy.ndarray,
    axis: numpy.ndarray,
    interpolation: Literal[("linear",)],
):
    "usage.xarray: 2"


def nanpercentile(
    a: numpy.ndarray,
    q: Union[(numpy.ndarray, numpy.float64)],
    axis: Union[(None, list[int], int)],
):
    "usage.xarray: 20"


def quantile(
    a: numpy.ndarray,
    q: numpy.ndarray,
    axis: numpy.ndarray,
    interpolation: Literal[("linear",)],
):
    "usage.xarray: 1"


def repeat(a: numpy.ndarray, repeats: int, axis: int):
    "usage.xarray: 4"


def isin(
    element: Union[(numpy.ndarray, dask.array.core.Array)],
    test_elements: Union[(numpy.ndarray, list[int])],
):
    "usage.xarray: 5"


def nansum(a: numpy.ndarray = ...):
    "usage.xarray: 8"


def nanmax(a: numpy.ndarray = ...):
    "usage.xarray: 17"


def nanmin(a: numpy.ndarray = ...):
    "usage.xarray: 16"


def nancumsum(a: numpy.ndarray, axis: int, dtype: None):
    "usage.xarray: 1"


def nancumprod(a: numpy.ndarray, axis: int, dtype: None):
    "usage.xarray: 1"


def var(a: numpy.ndarray = ..., axis: Union[(None, tuple[(None, ...)], int)] = ...):
    "usage.xarray: 22"


def nanvar(
    a: numpy.ndarray,
    axis: Union[(None, int)] = ...,
    dtype: Union[(None, list[float])] = ...,
    ddof: int = ...,
):
    "usage.xarray: 17"


def nanmedian(a: numpy.ndarray, axis: Union[(None, int)]):
    "usage.xarray: 3"


def datetime_data(_0: numpy.dtype, /):
    "usage.xarray: 1"


def trapz(
    y: Union[(numpy.ndarray, xarray.core.dataarray.DataArray, dask.array.core.Array)],
    x: Union[(numpy.ndarray, xarray.core.dataarray.DataArray)],
    axis: int,
):
    "usage.xarray: 4"


def nanprod(
    a: numpy.ndarray,
    axis: Union[(None, tuple[(int, int)], int)],
    dtype: None,
    out: None,
):
    "usage.xarray: 9"


def greater(_0: numpy.ndarray, _1: numpy.ndarray, /):
    "usage.xarray: 1"


def frexp(
    _0: Union[
        (
            xarray.core.variable.Variable,
            int,
            xarray.core.dataset.Dataset,
            numpy.ndarray,
            xarray.core.dataarray.DataArray,
        )
    ],
    /,
):
    "usage.xarray: 7"


def arccos(_0: Union[(numpy.ndarray, xarray.core.dataarray.DataArray)], /):
    "usage.xarray: 2"


def arccosh(_0: Union[(numpy.ndarray, xarray.core.dataarray.DataArray)], /):
    "usage.xarray: 2"


def arcsinh(_0: Union[(numpy.ndarray, xarray.core.dataarray.DataArray)], /):
    "usage.xarray: 2"


def arctanh(_0: Union[(numpy.ndarray, xarray.core.dataarray.DataArray)], /):
    "usage.xarray: 2"


def copysign(
    _0: Union[(numpy.ndarray, xarray.core.dataarray.DataArray)],
    _1: Union[(numpy.ndarray, xarray.core.dataarray.DataArray)],
    /,
):
    "usage.xarray: 2"


def cosh(_0: Union[(numpy.ndarray, xarray.core.dataarray.DataArray)], /):
    "usage.xarray: 2"


def degrees(_0: Union[(numpy.ndarray, xarray.core.dataarray.DataArray)], /):
    "usage.xarray: 2"


def expm1(_0: Union[(numpy.ndarray, xarray.core.dataarray.DataArray)], /):
    "usage.xarray: 2"


def fabs(_0: Union[(numpy.ndarray, xarray.core.dataarray.DataArray)], /):
    "usage.xarray: 2"


def greater_equal(_0: numpy.ndarray, _1: int, /):
    "usage.xarray: 1"


def fmin(
    _0: Union[(numpy.ndarray, xarray.core.dataarray.DataArray)],
    _1: Union[(numpy.ndarray, xarray.core.dataarray.DataArray)],
    /,
):
    "usage.xarray: 2"


def fmod(
    _0: Union[(numpy.ndarray, xarray.core.dataarray.DataArray)],
    _1: Union[(numpy.ndarray, xarray.core.dataarray.DataArray)],
    /,
):
    "usage.xarray: 2"


def iscomplex(x: xarray.core.dataarray.DataArray):
    "usage.xarray: 1"


def isreal(x: xarray.core.dataarray.DataArray):
    "usage.xarray: 1"


def ldexp(
    _0: Union[(numpy.ndarray, xarray.core.dataarray.DataArray)],
    _1: Union[(numpy.ndarray, xarray.core.dataarray.DataArray)],
    /,
):
    "usage.xarray: 2"


def log1p(_0: Union[(numpy.ndarray, xarray.core.dataarray.DataArray)], /):
    "usage.xarray: 2"


def logaddexp(
    _0: Union[(numpy.ndarray, xarray.core.dataarray.DataArray)],
    _1: Union[(numpy.ndarray, xarray.core.dataarray.DataArray)],
    /,
):
    "usage.xarray: 2"


def logaddexp2(
    _0: Union[(numpy.ndarray, xarray.core.dataarray.DataArray)],
    _1: Union[(numpy.ndarray, xarray.core.dataarray.DataArray)],
    /,
):
    "usage.xarray: 2"


def nextafter(
    _0: Union[(numpy.ndarray, xarray.core.dataarray.DataArray)],
    _1: Union[(numpy.ndarray, xarray.core.dataarray.DataArray)],
    /,
):
    "usage.xarray: 2"


def radians(_0: Union[(numpy.ndarray, xarray.core.dataarray.DataArray)], /):
    "usage.xarray: 2"


def signbit(_0: Union[(numpy.ndarray, xarray.core.dataarray.DataArray)], /):
    "usage.xarray: 2"


def sinh(_0: Union[(numpy.ndarray, xarray.core.dataarray.DataArray)], /):
    "usage.xarray: 2"


def tan(_0: Union[(numpy.ndarray, xarray.core.dataarray.DataArray)], /):
    "usage.xarray: 2"


def trunc(_0: Union[(numpy.ndarray, xarray.core.dataarray.DataArray)], /):
    "usage.xarray: 2"


class ndarray:
    @classmethod
    def mean(_0: numpy.ndarray = ..., /):
        "usage.sample_usage: 1\nusage.skimage: 23\nusage.xarray: 1"

    @classmethod
    def sum(_0: numpy.ndarray = ..., /):
        "usage.sample_usage: 1\nusage.skimage: 86\nusage.xarray: 10"

    @classmethod
    def sort(_0: numpy.ndarray, /):
        "usage.sample_usage: 1"

    @classmethod
    def reshape(_0: numpy.ndarray, _1, _2: int = ..., _3: int = ..., _4: int = ..., /):
        "usage.sample_usage: 2\nusage.skimage: 168\nusage.xarray: 189"

    @classmethod
    def astype(_0: numpy.ndarray, _1, /):
        "usage.sample_usage: 1\nusage.skimage: 555\nusage.xarray: 75"

    @classmethod
    def copy(_0: numpy.ndarray, /):
        "usage.skimage: 135\nusage.xarray: 14"

    @classmethod
    def max(_0: numpy.ndarray = ..., /):
        "usage.skimage: 108\nusage.xarray: 15"

    @classmethod
    def ptp(_0: numpy.ndarray = ..., /):
        "usage.skimage: 5"

    @classmethod
    def min(_0: numpy.ndarray = ..., /):
        "usage.skimage: 80\nusage.xarray: 16"

    @classmethod
    def any(_0: numpy.ndarray, /):
        "usage.skimage: 11\nusage.xarray: 6"

    @classmethod
    def nonzero(_0: numpy.ndarray, /):
        "usage.skimage: 4\nusage.xarray: 4"

    @classmethod
    def fill(_0: numpy.ndarray, _1: Union[(bool, int)], /):
        "usage.skimage: 5"

    @classmethod
    def flatten(_0: numpy.ndarray, /):
        "usage.skimage: 16\nusage.xarray: 5"

    @classmethod
    def ravel(_0: numpy.ndarray = ..., /):
        "usage.skimage: 207\nusage.xarray: 38"

    @classmethod
    def cumsum(_0: numpy.ndarray, /):
        "usage.skimage: 1"

    @classmethod
    def transpose(_0: numpy.ndarray, _1=..., _2: int = ..., _3: int = ..., /):
        "usage.skimage: 5\nusage.xarray: 13"

    @classmethod
    def argmin(_0: numpy.ndarray = ..., /):
        "usage.skimage: 2"

    @classmethod
    def view(_0: numpy.ndarray = ..., /):
        "usage.skimage: 22\nusage.xarray: 11"

    @classmethod
    def swapaxes(_0: numpy.ndarray, _1: int, _2: int, /):
        "usage.skimage: 2"

    @classmethod
    def argsort(_0: numpy.ndarray = ..., /):
        "usage.skimage: 5"

    @classmethod
    def argmax(_0: numpy.ndarray = ..., /):
        "usage.skimage: 6"

    @classmethod
    def std(_0: numpy.ndarray, /):
        "usage.skimage: 63\nusage.xarray: 2"

    @classmethod
    def all(_0: numpy.ndarray, /):
        "usage.skimage: 1\nusage.xarray: 9"

    @classmethod
    def tobytes(_0: numpy.ndarray, /):
        "usage.skimage: 2"

    @classmethod
    def tolist(_0: numpy.ndarray, /):
        "usage.skimage: 1\nusage.xarray: 17"

    @classmethod
    def dot(_0: numpy.ndarray, _1: numpy.ndarray, /):
        "usage.skimage: 1"

    @classmethod
    def conj(_0: numpy.ndarray, /):
        "usage.skimage: 4"

    @classmethod
    def item(_0: numpy.ndarray, /):
        "usage.xarray: 18"

    @classmethod
    def squeeze(_0: numpy.ndarray, /):
        "usage.xarray: 3"

    @classmethod
    def clip(_0: numpy.ndarray, _1: int, _2: int, /):
        "usage.xarray: 1"

    shape: Union[
        (tuple[(int, int)], tuple[(int, ...)], tuple[(int,)], numpy.ndarray)
    ] = ...
    ndim = ...
    dtype = ...
    size = ...
    T = ...
    flags = ...
    flat: numpy.ndarray = ...
    itemsize = ...
    strides: tuple[(int, int, int)] = ...
    coords = ...
    variables = ...
    variable = ...
    base = ...
    real = ...
    imag = ...
    dims = ...
    attrs = ...

    def __iter__(self, /):
        ""

    def __getitem__(self, _0, /):
        ""

    def __setitem__(self, _0, _1, /):
        ""

    def sort(self, /, *, axis: int = ..., order: Literal[("accumulator",)] = ...):
        "usage.sample_usage: 1\nusage.skimage: 9"

    def mean(
        self,
        /,
        *,
        axis: Union[(int, tuple[(int, int, int)])] = ...,
        keepdims: bool = ...,
    ):
        "usage.skimage: 28\nusage.xarray: 5"

    def sum(self, /, *, axis: int = ...):
        "usage.skimage: 23\nusage.xarray: 3"

    def all(self, /):
        "usage.skimage: 47\nusage.xarray: 20"

    def any(self, /):
        "usage.skimage: 4\nusage.xarray: 2"

    def min(self, /):
        "usage.skimage: 18"

    def max(self, /):
        "usage.skimage: 18"

    def cumsum(self, /, *, axis: int = None):
        "usage.skimage: 6"

    def argmax(self, /, *, axis: int = None):
        "usage.skimage: 1"

    def astype(
        self=...,
        /,
        *,
        copy: bool = ...,
        dtype: Union[(list[numpy.float32], Literal[("i1",)], numpy.dtype)] = ...,
    ):
        "usage.skimage: 34\nusage.xarray: 89"

    def tolist(self, /):
        "usage.skimage: 6\nusage.xarray: 1"

    def std(self, /, *, axis: Union[(int, tuple[(int, int)])] = ...):
        "usage.skimage: 2\nusage.xarray: 2"

    def view(self, /, *, dtype: list[numpy.uint8] = None):
        "usage.skimage: 4"

    def clip(
        self,
        _0: int = ...,
        _1: int = ...,
        /,
        *,
        min: int = ...,
        max: tuple[(int, ...)] = ...,
    ):
        "usage.skimage: 3\nusage.xarray: 2"

    def repeat(self, _0: int, /, *, axis: int = None):
        "usage.skimage: 2"

    def ravel(self, /, *, order: Literal[("F",)] = ...):
        "usage.skimage: 2\nusage.xarray: 1"

    def var(self, /, *, axis: int = ...):
        "usage.skimage: 7"

    def reshape(
        self, _0: Union[(tuple[(int, ...)], tuple[(int, int, int, int)], int)] = ..., /
    ):
        "usage.xarray: 6"

    def transpose(self, _0: list[int], /):
        "usage.xarray: 6"

    def round(self, /):
        "usage.xarray: 2"

    def argsort(self, /):
        "usage.xarray: 2"

    def item(self, /):
        "usage.xarray: 2"

    def take(self, _0: numpy.ndarray, /, *, axis: int = None):
        "usage.xarray: 4"

    def searchsorted(self, _0: int, /):
        "usage.xarray: 1"


class dtype:
    type = ...
    kind = ...
    itemsize = ...
    name = ...
    char = ...
    isnative = ...
    metadata = ...


class ufunc:
    @classmethod
    def reduce(
        _0: Callable,
        _1: Union[
            (
                xarray.core.dataarray.DataArray,
                list[numpy.ndarray],
                numpy.ndarray,
                tuple[(int,)],
            )
        ] = ...,
        /,
    ):
        "usage.sample_usage: 1\nusage.skimage: 6\nusage.xarray: 1"


class float64:
    def __init__(x: Union[(int, numpy.int64, float, numpy.ndarray)], /):
        "usage.skimage: 8\nusage.xarray: 2"

    ndim = ...
    shape = ...
    dtype = ...

    def __getitem__(self, _0: tuple[(Union[(None, ellipsis)], None)], /):
        ""


class generic:
    @classmethod
    def astype(
        _0,
        _1: Union[
            (
                list[numpy.float64],
                Literal[("timedelta64[ns]",)],
                list[numpy.int64],
                list[float],
            )
        ],
        /,
    ):
        "usage.skimage: 12\nusage.xarray: 7"

    @classmethod
    def conj(_0: numpy.complex128, /):
        "usage.skimage: 1"

    @classmethod
    def all(_0: numpy.bool_, /):
        "usage.xarray: 5"

    @classmethod
    def squeeze(_0: numpy.float64, /):
        "usage.xarray: 1"

    @classmethod
    def item(_0: numpy.float64, /):
        "usage.xarray: 3"

    @classmethod
    def any(_0: numpy.bool_, /):
        "usage.xarray: 2"


class iinfo:
    def __init__(int_type: Union[(numpy.dtype, list)]):
        "usage.skimage: 33"

    min = ...
    max = ...


class finfo:
    def __init__(dtype: numpy.dtype):
        "usage.skimage: 1"

    eps = ...
    resolution = ...
    max = ...
    min = ...


class flagsobj:
    writeable: bool = ...
    f_contiguous = ...
    c_contiguous = ...
    owndata = ...

    def __getitem__(self, _0: Literal[("C_CONTIGUOUS", "F_CONTIGUOUS")], /):
        ""


class flatiter:
    def __iter__(self, /):
        ""

    def __getitem__(
        self,
        _0: Union[
            (int, slice[(Union[(None, int)], Union[(None, int)], None)], numpy.int64)
        ],
        /,
    ):
        ""

    def __setitem__(
        self,
        _0: Union[(list[int], numpy.ndarray)],
        _1: Union[(float, numpy.ndarray)],
        /,
    ):
        ""


class ndindex:
    def __init__(*shape: Literal[("v", "t")]):
        "usage.skimage: 1"

    def __iter__(self, /):
        ""


class uint8:
    def __init__(
        _0: Union[(numpy.ndarray, int, numpy.int32, numpy.float64, numpy.int64)], /
    ):
        "usage.skimage: 6\nusage.xarray: 1"


class int64:
    ndim = ...
    shape = ...
    dtype = ...

    def __getitem__(self, _0: tuple[(None, ellipsis)], /):
        ""


class float32:
    dtype = ...


class matrix:
    A = ...


class complex128:
    imag = ...
    real = ...


class nditer:
    multi_index = ...

    def __iter__(self, /):
        ""


class int32:
    dtype = ...


class int8:
    def __init__(_0: Union[(int, numpy.ndarray, numpy.int64)], /):
        "usage.skimage: 5\nusage.xarray: 1"


class int16:
    def __init__(_0: Union[(int, list[int], numpy.int64)], /):
        "usage.skimage: 2\nusage.xarray: 2"


class longlong:
    def __init__(_0: numpy.int64, /):
        "usage.skimage: 1"


class uint16:
    def __init__(_0: Union[(numpy.int64, int)], /):
        "usage.skimage: 2"


class uint32:
    def __init__(_0: numpy.int64, /):
        "usage.skimage: 1"


class uint64:
    def __init__(_0: Union[(int, numpy.int64)], /):
        "usage.skimage: 1\nusage.xarray: 2"


class ulonglong:
    def __init__(_0: numpy.int64, /):
        "usage.skimage: 1"


class void:
    def __getitem__(self, _0: int, /):
        ""


class errstate:
    def __init__():
        "usage.xarray: 4"


class vectorize:
    def __init__(
        pyfunc: Callable, otypes: Union[(None, list[list[float]], list)] = ...
    ):
        "usage.xarray: 75"


class str_:
    def __init__(_0: Literal[("asdf",)], /):
        "usage.xarray: 1"

    dtype = ...

    def __getitem__(self, _0: slice[(Union[(None, int)], Union[(None, int)], int)], /):
        ""


class bytes_:
    def __init__(_0: Literal[("asdf", "x", "z")], /):
        "usage.xarray: 3"

    def __getitem__(self, _0: slice[(Union[(None, int)], Union[(None, int)], int)], /):
        ""


class timedelta64:
    def __init__(_0: Union[(Literal[("NaT",)], datetime.timedelta, int)] = ..., /):
        "usage.xarray: 16"

    dtype = ...


class datetime64:
    def __init__(_0: Literal[("NaT",)], _1: Literal[("ns",)], /):
        "usage.xarray: 1"

    dtype = ...


class broadcast:
    def __init__(
        _0: Union[(numpy.ndarray, list[int], int)],
        _1: Union[
            (Literal[("_not_supplied",)], numpy.ndarray, list[int], Literal[("z",)])
        ] = ...,
        _2: numpy.ndarray = ...,
        /,
    ):
        "usage.xarray: 13"

    shape = ...


class object_:
    def __init__(_0: bytes, /):
        "usage.xarray: 1"


class bool_:
    def all(self, /):
        "usage.xarray: 4"


class ndenumerate:
    def __iter__(self, /):
        ""
