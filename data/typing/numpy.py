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
    _0: Union[(numpy.float64, int, float, dask.array.core.Array, numpy.int64)],
    _1: Union[(numpy.float64, int, numpy.int64, float)] = ...,
    _2: Union[(numpy.float64, None, int, float)] = ...,
    _3: list[numpy.uint8] = ...,
    /,
    *,
    dtype=...,
):
    "usage.sample_usage: 4, usage.skimage: 223, usage.xarray: 393"


def array(
    _0=...,
    /,
    *,
    dtype=...,
    ndmin: int = ...,
    copy: bool = ...,
    order: Literal[("K", "C", "F")] = ...,
):
    "usage.sample_usage: 1, usage.skimage: 1076, usage.xarray: 391"


def zeros(_0=..., /, *, dtype=..., order: Literal[("C", "F")] = ...):
    "usage.sample_usage: 1, usage.skimage: 787, usage.xarray: 52"


def ones(shape, dtype=..., order: Literal[("F",)] = ...):
    "usage.sample_usage: 1, usage.skimage: 269, usage.xarray: 59"


def linspace(
    start: Union[(float, numpy.float64, numpy.int64, int)],
    stop: Union[(numpy.float64, int, float, numpy.float32, numpy.int64)] = ...,
    num: Union[(int, numpy.int64)] = ...,
):
    "usage.sample_usage: 1, usage.skimage: 70, usage.xarray: 95"


def eye(N: int, M: int = ..., dtype: list = ...):
    "usage.sample_usage: 1, usage.skimage: 39"


def add(
    _0: Union[
        (
            float,
            numpy.ndarray,
            xarray.core.dataarray.DataArray,
            dask.array.core.Array,
            xarray.core.dataset.Dataset,
        )
    ],
    _1,
    /,
    *,
    dtype: list = ...,
    out: Union[(numpy.ndarray, xarray.core.dataarray.DataArray)] = ...,
):
    "usage.sample_usage: 1, usage.skimage: 11, usage.xarray: 13"


def exp(
    _0: Union[(xarray.core.dataarray.DataArray, numpy.ndarray, int, float)],
    /,
    *,
    dtype: numpy.dtype = ...,
):
    "usage.sample_usage: 1, usage.skimage: 26, usage.xarray: 3"


def log(_0, /):
    "usage.sample_usage: 1, usage.skimage: 19, usage.xarray: 2"


def column_stack(
    tup: Union[(tuple[(numpy.ndarray, numpy.ndarray)], list[numpy.ndarray])]
):
    "usage.sample_usage: 1, usage.skimage: 9"


def concatenate(_0, /, *, axis: int = ...):
    "usage.sample_usage: 1, usage.skimage: 48, usage.xarray: 45"


def absolute(_0, /):
    "usage.skimage: 113"


def asarray(a, dtype=..., order: Literal[("C",)] = ...):
    "usage.skimage: 247, usage.xarray: 837"


def sum(a, axis=..., dtype: Union[(list[float], None)] = ..., keepdims: bool = ...):
    "usage.skimage: 125, usage.xarray: 51"


def vstack(
    tup: Union[
        (
            list[numpy.ndarray],
            tuple[(numpy.ndarray, numpy.ndarray)],
            tuple[
                (
                    Union[
                        (numpy.ndarray, list[Union[(float, int)]], list[numpy.int64])
                    ],
                    Union[
                        (numpy.ndarray, list[Union[(float, int)]], list[numpy.int64])
                    ],
                )
            ],
            tuple[(numpy.ndarray, numpy.ndarray, numpy.ndarray)],
        )
    ]
):
    "usage.skimage: 33"


def all(a: Union[(numpy.ma.core.MaskedArray, numpy.ndarray)] = ...):
    "usage.skimage: 113, usage.xarray: 14"


def round_(a=...):
    "usage.skimage: 30"


def asanyarray(a=...):
    "usage.skimage: 50"


def obj2sctype(rep):
    "usage.skimage: 14"


def issubdtype(arg1, arg2: list):
    "usage.skimage: 162, usage.xarray: 256"


def multiply(
    _0: numpy.ndarray,
    _1: Union[(numpy.ndarray, dask.array.core.Array, int, float)],
    /,
    *,
    out: numpy.ndarray = ...,
    dtype: Union[(list[numpy.float32], numpy.dtype, list[numpy.float64], list)] = ...,
):
    "usage.skimage: 25, usage.xarray: 2"


def reshape(a: Union[(list[float], list[int], numpy.ndarray)], newshape=...):
    "usage.skimage: 43, usage.xarray: 7"


def sqrt(_0=..., /, *, out: numpy.ndarray = ...):
    "usage.skimage: 112, usage.xarray: 4"


def moveaxis(
    a: Union[(numpy.float64, int, numpy.ndarray)],
    source: Union[(range, tuple[(None, ...)], int, numpy.ndarray)],
    destination: Union[(tuple[(None, ...)], int, numpy.ndarray, list[int])],
):
    "usage.skimage: 6, usage.xarray: 17"


def rollaxis(a: numpy.ndarray, axis: int = ...):
    "usage.skimage: 14"


def any(a: Union[(list[bool], numpy.bool_, numpy.ndarray)] = ...):
    "usage.skimage: 39, usage.xarray: 5"


def empty_like(
    _0: Union[
        (
            xarray.core.variable.IndexVariable,
            xarray.core.variable.Variable,
            numpy.ma.core.MaskedArray,
            numpy.ndarray,
        )
    ] = ...,
    /,
    *,
    dtype: list = ...,
    subok: bool = ...,
    order: Literal[("C",)] = ...,
):
    "usage.skimage: 48, usage.xarray: 2"


def triu(m: numpy.ndarray):
    "usage.skimage: 1"


def seterr(
    invalid: Literal[("ignore", "warn")],
    divide: Literal[("warn",)] = ...,
    over: Literal[("warn",)] = ...,
    under: Literal[("ignore",)] = ...,
):
    "usage.skimage: 2"


def isnan(
    _0: Union[
        (
            float,
            numpy.float64,
            numpy.ndarray,
            xarray.core.dataarray.DataArray,
            list[float],
        )
    ],
    /,
):
    "usage.skimage: 14, usage.xarray: 14"


def floor(
    _0: Union[(xarray.core.dataarray.DataArray, numpy.ndarray, numpy.float64, float)], /
):
    "usage.skimage: 13, usage.xarray: 2"


def stack(arrays=...):
    "usage.skimage: 35, usage.xarray: 26"


def choose(a: numpy.ndarray, choices: list[numpy.ndarray]):
    "usage.skimage: 2"


def amin(a=...):
    "usage.skimage: 60, usage.xarray: 25"


def amax(
    a,
    axis: Union[(tuple[(int, int, int)], None, int, tuple[(int, int)])] = ...,
    keepdims: bool = ...,
):
    "usage.skimage: 105, usage.xarray: 23"


def rint(
    _0: Union[(xarray.core.dataarray.DataArray, numpy.ndarray)],
    /,
    *,
    out: numpy.ndarray = ...,
):
    "usage.skimage: 2, usage.xarray: 2"


def clip(a: Union[(numpy.float64, numpy.ndarray, int)], a_min, a_max=...):
    "usage.skimage: 61"


def power(_0: Union[(numpy.ndarray, int)], _1: Union[(float, numpy.ndarray, int)], /):
    "usage.skimage: 11"


def log10(
    _0: Union[(xarray.core.dataarray.DataArray, numpy.float64, numpy.ndarray)], /
):
    "usage.skimage: 4, usage.xarray: 2"


def load(file: Literal[("/Users/saul/Downloads/scikit-image-0.17.0/skimage/",)]):
    "usage.skimage: 28"


def meshgrid(*xi: Literal[("v", "t")]):
    "usage.skimage: 28, usage.xarray: 6"


def dstack(
    tup: Union[
        (
            list[numpy.ndarray],
            tuple[(numpy.ndarray, ...)],
            list[skimage.feature._hessian_det_appx._memoryviewslice],
        )
    ]
):
    "usage.skimage: 12"


def nonzero(a: numpy.ndarray):
    "usage.skimage: 22, usage.xarray: 4"


def cbrt(_0: numpy.ndarray, /):
    "usage.skimage: 4"


def hypot(
    _0: Union[(xarray.core.dataarray.DataArray, numpy.float64, int, numpy.ndarray)],
    _1: Union[(xarray.core.dataarray.DataArray, numpy.float64, int, numpy.ndarray)],
    /,
):
    "usage.skimage: 13, usage.xarray: 2"


def arctan2(
    _0: Union[
        (xarray.core.dataarray.DataArray, numpy.float64, numpy.int64, numpy.ndarray)
    ],
    _1: Union[
        (xarray.core.dataarray.DataArray, numpy.float64, numpy.int64, numpy.ndarray)
    ],
    /,
):
    "usage.skimage: 8, usage.xarray: 2"


def where(
    _0: Union[(numpy.ndarray, bool, list[bool], dask.array.core.Array, numpy.bool_)],
    _1: Union[(numpy.ndarray, numpy.float64, int, float)] = ...,
    _2: Union[(numpy.float64, dask.array.core.Array, int, numpy.ndarray)] = ...,
    /,
):
    "usage.skimage: 26, usage.xarray: 23"


def cos(_0, /):
    "usage.skimage: 48, usage.xarray: 14"


def sin(_0, /, *, out=...):
    "usage.skimage: 47, usage.xarray: 18"


def ascontiguousarray(
    a: Union[(list[float], list[Union[(float, int)]], numpy.ndarray, list[int])] = ...
):
    "usage.skimage: 67"


def swapaxes(a: numpy.ndarray, axis1: int, axis2: int):
    "usage.skimage: 4, usage.xarray: 8"


def ravel(a):
    "usage.skimage: 12, usage.xarray: 44"


def squeeze(a: numpy.ndarray = ...):
    "usage.skimage: 16"


def ones_like(a: Union[(xarray.core.variable.Variable, numpy.ndarray)] = ...):
    "usage.skimage: 26, usage.xarray: 4"


def can_cast(
    _0: Union[(numpy.ndarray, float, numpy.dtype, int)],
    _1: Union[(list[bool], numpy.dtype)],
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
    "usage.skimage: 129, usage.xarray: 11"


def min_scalar_type(_0: Union[(numpy.float64, int, numpy.int64)], /):
    "usage.skimage: 5"


def unique(
    ar: Union[(xarray.core.dataarray.DataArray, numpy.ndarray)] = ...,
    return_inverse: bool = ...,
    return_counts: bool = ...,
):
    "usage.skimage: 68, usage.xarray: 14"


def zeros_like(
    a: Union[(tuple[(int, int, int)], tuple[(int, int)], numpy.ndarray)],
    dtype: list = ...,
    order: Literal[("C",)] = ...,
):
    "usage.skimage: 70, usage.xarray: 43"


def full(shape, fill_value=...):
    "usage.skimage: 36, usage.xarray: 10"


def loadtxt(
    fname: Literal[("/Users/saul/Downloads/scikit-image-0.17.0/skimage/",)],
    dtype: list[tuple[(Literal[("pair", "1", "b1", "L1", "a1")], list)]],
):
    "usage.skimage: 1"


def logical_and(
    _0: Union[(xarray.core.dataarray.DataArray, numpy.ndarray, numpy.bool_)],
    _1: Union[(xarray.core.dataarray.DataArray, numpy.ndarray, numpy.bool_)],
    /,
):
    "usage.skimage: 13, usage.xarray: 2"


def deg2rad(
    _0: Union[(xarray.core.dataarray.DataArray, int, list[int], numpy.ndarray)], /
):
    "usage.skimage: 18, usage.xarray: 2"


def rad2deg(
    _0: Union[(xarray.core.dataarray.DataArray, numpy.float64, numpy.ndarray)], /
):
    "usage.skimage: 6, usage.xarray: 2"


def maximum(
    _0,
    _1,
    /,
    *,
    out: numpy.ndarray = ...,
    casting: Literal[("unsafe",)] = ...,
    dtype: numpy.dtype = ...,
):
    "usage.skimage: 16, usage.xarray: 87"


def percentile(
    a: numpy.ndarray,
    q: Union[(float, numpy.float64, int, numpy.ndarray, list[int])] = ...,
):
    "usage.skimage: 11, usage.xarray: 20"


def logical_not(
    _0: Union[
        (
            bool,
            numpy.ndarray,
            xarray.core.dataarray.DataArray,
            dask.array.core.Array,
            numpy.bool_,
        )
    ],
    /,
    *,
    out: numpy.ndarray = ...,
):
    "usage.skimage: 14, usage.xarray: 10"


def isscalar(element):
    "usage.skimage: 67, usage.xarray: 33"


def ceil(_0, /):
    "usage.skimage: 31, usage.xarray: 5"


def minimum(
    _0: Union[
        (
            xarray.core.dataarray.DataArray,
            tuple[(int, int, int)],
            tuple[(int, int)],
            numpy.ndarray,
        )
    ],
    _1,
    /,
):
    "usage.skimage: 9, usage.xarray: 4"


def dot(_0: numpy.ndarray, _1: numpy.ndarray, /):
    "usage.skimage: 1"


def diag(v: numpy.ndarray):
    "usage.skimage: 5"


def arcsin(_0: Union[(xarray.core.dataarray.DataArray, float, numpy.ndarray)], /):
    "usage.skimage: 1, usage.xarray: 2"


def ellipkinc(_0: numpy.float64, _1: float, /):
    "usage.skimage: 1"


def ellipeinc(_0: numpy.float64, _1: float, /):
    "usage.skimage: 1"


def transpose(a=...):
    "usage.skimage: 21, usage.xarray: 3"


def shape(a: Union[(numpy.ma.core.MaskedArray, numpy.ndarray)]):
    "usage.skimage: 1, usage.xarray: 11"


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
            tuple[
                (
                    numpy.float64,
                    numpy.float64,
                    numpy.float64,
                    numpy.float64,
                    numpy.float64,
                )
            ],
            list[Union[(float, int)]],
            int,
            numpy.int64,
        )
    ] = ...,
):
    "usage.skimage: 7"


def interp(
    x: Union[(numpy.flatiter, numpy.ndarray)], xp: numpy.ndarray, fp: numpy.ndarray
):
    "usage.skimage: 6"


def polyfit(x: numpy.ndarray, y: numpy.ndarray, deg: int):
    "usage.skimage: 1"


def pad(array: Union[(list[list[int]], list[int], numpy.ndarray)], pad_width=...):
    "usage.skimage: 126, usage.xarray: 44"


def product(*args: Literal[("v", "t")]):
    "usage.skimage: 14"


def apply_along_axis(func1d: Callable, axis: int, arr: numpy.ndarray):
    "usage.skimage: 8"


def count_nonzero(a: numpy.ndarray):
    "usage.skimage: 9"


def cumsum(a=...):
    "usage.skimage: 29, usage.xarray: 10"


def take_along_axis(arr: numpy.ndarray, indices: numpy.ndarray, axis: int):
    "usage.skimage: 1"


def square(_0: Union[(xarray.core.dataarray.DataArray, numpy.ndarray)], /):
    "usage.skimage: 7, usage.xarray: 2"


def mean(
    a: Union[
        (
            numpy.ndarray,
            xarray.core.dataarray.DataArray,
            list[numpy.float64],
            dask.array.core.Array,
            xarray.core.variable.Variable,
        )
    ],
    axis: Union[(tuple[(int,)], None, int, tuple[(int, int)])] = ...,
    keepdims: bool = ...,
    dtype: Union[(list[float], list, None)] = ...,
):
    "usage.skimage: 61, usage.xarray: 32"


def log2(_0: Union[(xarray.core.dataarray.DataArray, int, numpy.ndarray)], /):
    "usage.skimage: 5, usage.xarray: 2"


def allclose(
    a: Union[
        (
            numpy.float64,
            numpy.ndarray,
            xarray.core.dataarray.DataArray,
            list[numpy.float64],
            list[int],
        )
    ],
    b,
    rtol: Union[(int, float)] = ...,
    equal_nan: bool = ...,
    atol: float = ...,
):
    "usage.skimage: 33, usage.xarray: 20"


def argsort(a: Union[(numpy.flatiter, numpy.ndarray)]):
    "usage.skimage: 28"


def hstack(tup):
    "usage.skimage: 27, usage.xarray: 1"


def argmax(a: Union[(dask.array.core.Array, numpy.ndarray)] = ...):
    "usage.skimage: 18, usage.xarray: 11"


def logspace(
    start: Union[(numpy.float64, float)], stop: Union[(numpy.float64, float)], num: int
):
    "usage.skimage: 2"


def logical_or(
    _0: Union[(xarray.core.dataarray.DataArray, numpy.ndarray)],
    _1: Union[(xarray.core.dataarray.DataArray, numpy.ndarray)],
    /,
):
    "usage.skimage: 3, usage.xarray: 2"


def isinf(_0: Union[(xarray.core.dataarray.DataArray, float, numpy.ndarray)], /):
    "usage.skimage: 2, usage.xarray: 2"


def delete(arr: numpy.ndarray, obj: tuple[(Union[(None, int)], ...)], axis: int):
    "usage.skimage: 3"


def split(ary: numpy.ndarray, indices_or_sections: int):
    "usage.skimage: 1"


def atleast_1d(*arys: Literal[("v", "t")]):
    "usage.skimage: 11, usage.xarray: 23"


def isclose(
    a: Union[(numpy.ndarray, numpy.float64, float)],
    b: Union[(float, int, numpy.float64, numpy.ndarray)],
    rtol: float = ...,
    atol: float = ...,
    equal_nan: bool = ...,
):
    "usage.skimage: 3, usage.xarray: 12"


def gradient(
    f: Union[(xarray.core.dataarray.DataArray, numpy.ndarray)],
    *varargs: Literal[("v", "t")],
):
    "usage.skimage: 8, usage.xarray: 5"


def argmin(a: Union[(list[numpy.float64], numpy.ndarray)] = ...):
    "usage.skimage: 10, usage.xarray: 5"


def arctan(
    _0: Union[(xarray.core.dataarray.DataArray, numpy.float64, numpy.ndarray)], /
):
    "usage.skimage: 3, usage.xarray: 2"


def sort(a: numpy.ndarray = ...):
    "usage.skimage: 14, usage.xarray: 2"


def spacing(_0: int, /):
    "usage.skimage: 1"


def isfinite(
    _0: Union[
        (
            tuple[(numpy.ndarray, numpy.ndarray)],
            xarray.core.dataarray.DataArray,
            list[Union[(numpy.float64, numpy.int64)]],
            numpy.ndarray,
        )
    ],
    /,
):
    "usage.skimage: 7, usage.xarray: 6"


def diff(a: numpy.ndarray, n: int = ..., axis: int = ...):
    "usage.skimage: 15, usage.xarray: 11"


def flatnonzero(a: numpy.ndarray):
    "usage.skimage: 6, usage.xarray: 2"


def copy(a: Union[(numpy.float64, numpy.ndarray)]):
    "usage.skimage: 14"


def atleast_2d(*arys: Literal[("v", "t")]):
    "usage.skimage: 7, usage.xarray: 2"


def rot90(m: numpy.ndarray = ...):
    "usage.skimage: 7"


def roll(
    a: Union[(list[Union[(float, int)]], numpy.ndarray)],
    shift: Union[(tuple[(int, int)], int)] = ...,
):
    "usage.skimage: 14, usage.xarray: 1"


def indices(dimensions: tuple[(Union[(int, numpy.int64)], ...)] = ...):
    "usage.skimage: 6"


def tri(N: int = ..., M: int = ..., k: int = ...):
    "usage.skimage: 9"


def less(
    _0: Union[(tuple[(int, ...)], numpy.ndarray)],
    _1: Union[(tuple[(int, ...)], numpy.ndarray)],
    /,
):
    "usage.skimage: 3, usage.xarray: 1"


def prod(a):
    "usage.skimage: 9, usage.xarray: 15"


def true_divide(
    _0: numpy.ndarray,
    _1: Union[(numpy.ndarray, numpy.int64)],
    /,
    *,
    out: numpy.ndarray = ...,
):
    "usage.skimage: 2"


def unravel_index(
    _0: Union[(numpy.ndarray, int, numpy.int64)], _1: tuple[(int, ...)], /
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
            tuple[(int, ...)],
            list[int],
            tuple[(int, int)],
        )
    ],
):
    "usage.skimage: 15, usage.xarray: 5"


def real(val: Union[(xarray.core.dataarray.DataArray, float, numpy.ndarray)]):
    "usage.skimage: 8, usage.xarray: 1"


def imag(val: Union[(xarray.core.dataarray.DataArray, numpy.ndarray)]):
    "usage.skimage: 1, usage.xarray: 1"


def sign(_0: Union[(xarray.core.dataarray.DataArray, int, numpy.ndarray)], /):
    "usage.skimage: 4, usage.xarray: 3"


def subtract(
    _0: Union[(int, numpy.ndarray)],
    _1: Union[(dask.array.core.Array, numpy.ndarray)],
    /,
    *,
    dtype: numpy.dtype = ...,
):
    "usage.skimage: 11, usage.xarray: 2"


def ix_(*args: Literal[("v", "t")]):
    "usage.skimage: 2, usage.xarray: 3"


def convolve(a: numpy.ndarray, v: list[float], mode: Literal[("valid",)]):
    "usage.skimage: 1"


def invert(_0: Union[(numpy.ndarray, list[bool])], /):
    "usage.skimage: 7"


def array_equal(
    a1: Union[(list[int], tuple[(float, float, float)], numpy.ndarray)],
    a2: Union[(tuple[(int, int, int)], tuple[(int, int)], numpy.ndarray)],
):
    "usage.skimage: 5, usage.xarray: 3"


def reciprocal(_0: numpy.ndarray, /, *, out: numpy.ndarray = None):
    "usage.skimage: 1"


def insert(arr: numpy.ndarray, obj: int, values: numpy.ndarray, axis: int):
    "usage.skimage: 3"


def full_like(
    a: Union[
        (xarray.core.dataarray.DataArray, xarray.core.variable.Variable, numpy.ndarray)
    ],
    fill_value: Union[(bool, int, float)] = ...,
):
    "usage.skimage: 1, usage.xarray: 7"


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
    "usage.skimage: 5, usage.xarray: 1"


def asfortranarray(a: numpy.ndarray):
    "usage.skimage: 1"


def cross(a: numpy.ndarray, b: numpy.ndarray):
    "usage.skimage: 5"


def einsum(*operands: Literal[("v", "t")]):
    "usage.skimage: 1, usage.xarray: 44"


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
    "usage.skimage: 2, usage.xarray: 2"


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
    "usage.skimage: 1, usage.xarray: 3"


def result_type(
    _0,
    _1=...,
    _2: Union[(dask.array.core.Array, list[numpy.float32], numpy.ndarray)] = ...,
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
    "usage.skimage: 7, usage.xarray: 94"


def ptp(a: numpy.ndarray):
    "usage.skimage: 10"


def cumprod(a: Union[(tuple[(int, ...)], numpy.ndarray)] = ...):
    "usage.skimage: 5, usage.xarray: 4"


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
    "usage.skimage: 1, usage.xarray: 2"


def in1d(
    ar1: Union[(numpy.flatiter, numpy.ndarray)],
    ar2: Union[(numpy.ndarray, tuple[(int, int)])],
):
    "usage.skimage: 2"


def take(a: numpy.ndarray, indices: Union[(int, list[int], numpy.ndarray)] = ...):
    "usage.skimage: 1, usage.xarray: 11"


def lexsort(
    _0: tuple[(Union[(xarray.core.dataarray.DataArray, numpy.ndarray)], ...)], /
):
    "usage.skimage: 1, usage.xarray: 2"


def fmax(
    _0: Union[(xarray.core.dataarray.DataArray, numpy.ndarray)],
    _1: Union[(xarray.core.dataarray.DataArray, float, numpy.float64, numpy.ndarray)],
    /,
):
    "usage.skimage: 3, usage.xarray: 2"


def fix(x: Union[(xarray.core.dataarray.DataArray, numpy.float64, float)]):
    "usage.skimage: 2, usage.xarray: 1"


def tensordot(
    a: numpy.ndarray,
    b: Union[(range, numpy.ndarray)],
    axes: Union[(tuple[(int, int)], list[int], tuple[(list[int], list[int])])],
):
    "usage.skimage: 1, usage.xarray: 5"


def atleast_3d(*arys: Literal[("v", "t")]):
    "usage.skimage: 11"


def iscomplexobj(x: numpy.ndarray):
    "usage.skimage: 4"


def conjugate(_0: Union[(xarray.core.dataarray.DataArray, numpy.ndarray)], /):
    "usage.skimage: 2, usage.xarray: 2"


def angle(z: Union[(xarray.core.dataarray.DataArray, numpy.ndarray)]):
    "usage.skimage: 3, usage.xarray: 2"


def require(
    a: numpy.ndarray, dtype: list[numpy.uint8], requirements: list[Literal[("C",)]]
):
    "usage.skimage: 1"


def tanh(_0: Union[(xarray.core.dataarray.DataArray, numpy.ndarray)], /):
    "usage.skimage: 2, usage.xarray: 2"


def ndim(a: numpy.ndarray):
    "usage.skimage: 4"


def searchsorted(a: numpy.ndarray, v: Union[(numpy.ndarray, numpy.float64, int)]):
    "usage.skimage: 3, usage.xarray: 1"


def fill_diagonal(a: numpy.ndarray, val: float):
    "usage.skimage: 1"


def array2string(a: numpy.ndarray, separator: Literal[(", ",)]):
    "usage.skimage: 1"


def std(a: numpy.ndarray = ...):
    "usage.skimage: 1, usage.xarray: 3"


def hamming(M: int):
    "usage.skimage: 1"


def hanning(M: int):
    "usage.skimage: 1"


def around(a: Union[(tuple[(numpy.float64, numpy.float64)], numpy.ndarray)]):
    "usage.skimage: 1, usage.xarray: 4"


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
    array: Union[(numpy.ndarray, float)], shape: tuple[(Union[(int, None)], ...)]
):
    "usage.xarray: 25"


def nanmean(
    a: numpy.ndarray,
    axis: Union[
        (tuple[(None, ...)], tuple[(int, int)], int, None, tuple[(int,)])
    ] = ...,
    dtype: Union[
        (
            list[numpy.float32],
            list[float],
            list[numpy.float16],
            list[numpy.float64],
            None,
        )
    ] = ...,
):
    "usage.xarray: 21"


def nanstd(
    a: numpy.ndarray, axis: Union[(int, None)], dtype: None = ..., ddof: int = ...
):
    "usage.xarray: 3"


def nanargmax(a: numpy.ndarray, axis: Union[(int, None)]):
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
    q: Union[(numpy.float64, numpy.ndarray)],
    axis: Union[(None, int, list[int])],
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


def var(a: numpy.ndarray = ..., axis: Union[(tuple[(None, ...)], int, None)] = ...):
    "usage.xarray: 22"


def nanvar(
    a: numpy.ndarray,
    axis: Union[(int, None)] = ...,
    dtype: Union[(list[float], None)] = ...,
    ddof: int = ...,
):
    "usage.xarray: 17"


def nanmedian(a: numpy.ndarray, axis: Union[(int, None)]):
    "usage.xarray: 3"


def datetime_data(_0: numpy.dtype, /):
    "usage.xarray: 1"


def trapz(
    y: Union[(numpy.ndarray, dask.array.core.Array, xarray.core.dataarray.DataArray)],
    x: Union[(numpy.ndarray, xarray.core.dataarray.DataArray)],
    axis: int,
):
    "usage.xarray: 4"


def nanprod(
    a: numpy.ndarray,
    axis: Union[(tuple[(int, int)], int, None)],
    dtype: None,
    out: None,
):
    "usage.xarray: 9"


def greater(_0: numpy.ndarray, _1: numpy.ndarray, /):
    "usage.xarray: 1"


def frexp(
    _0: Union[
        (
            numpy.ndarray,
            xarray.core.dataarray.DataArray,
            int,
            xarray.core.dataset.Dataset,
            xarray.core.variable.Variable,
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
        "usage.sample_usage: 1, usage.skimage: 23, usage.xarray: 1"

    @classmethod
    def sum(_0: numpy.ndarray = ..., /):
        "usage.sample_usage: 1, usage.skimage: 86, usage.xarray: 10"

    @classmethod
    def sort(_0: numpy.ndarray, /):
        "usage.sample_usage: 1"

    @classmethod
    def reshape(_0: numpy.ndarray, _1, _2: int = ..., _3: int = ..., _4: int = ..., /):
        "usage.sample_usage: 2, usage.skimage: 168, usage.xarray: 189"

    @classmethod
    def astype(_0: numpy.ndarray, _1, /):
        "usage.sample_usage: 1, usage.skimage: 555, usage.xarray: 75"

    @classmethod
    def copy(_0: numpy.ndarray, /):
        "usage.skimage: 135, usage.xarray: 14"

    @classmethod
    def max(_0: numpy.ndarray = ..., /):
        "usage.skimage: 108, usage.xarray: 15"

    @classmethod
    def ptp(_0: numpy.ndarray = ..., /):
        "usage.skimage: 5"

    @classmethod
    def min(_0: numpy.ndarray = ..., /):
        "usage.skimage: 80, usage.xarray: 16"

    @classmethod
    def any(_0: numpy.ndarray, /):
        "usage.skimage: 11, usage.xarray: 6"

    @classmethod
    def nonzero(_0: numpy.ndarray, /):
        "usage.skimage: 4, usage.xarray: 4"

    @classmethod
    def fill(_0: numpy.ndarray, _1: Union[(int, bool)], /):
        "usage.skimage: 5"

    @classmethod
    def flatten(_0: numpy.ndarray, /):
        "usage.skimage: 16, usage.xarray: 5"

    @classmethod
    def ravel(_0: numpy.ndarray = ..., /):
        "usage.skimage: 207, usage.xarray: 38"

    @classmethod
    def cumsum(_0: numpy.ndarray, /):
        "usage.skimage: 1"

    @classmethod
    def transpose(_0: numpy.ndarray, _1=..., _2: int = ..., _3: int = ..., /):
        "usage.skimage: 5, usage.xarray: 13"

    @classmethod
    def argmin(_0: numpy.ndarray = ..., /):
        "usage.skimage: 2"

    @classmethod
    def view(_0: numpy.ndarray = ..., /):
        "usage.skimage: 22, usage.xarray: 11"

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
        "usage.skimage: 63, usage.xarray: 2"

    @classmethod
    def all(_0: numpy.ndarray, /):
        "usage.skimage: 1, usage.xarray: 9"

    @classmethod
    def tobytes(_0: numpy.ndarray, /):
        "usage.skimage: 2"

    @classmethod
    def tolist(_0: numpy.ndarray, /):
        "usage.skimage: 1, usage.xarray: 17"

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
        (tuple[(int,)], tuple[(int, ...)], tuple[(int, int)], numpy.ndarray)
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
        "usage.sample_usage: 1, usage.skimage: 9"

    def mean(
        self,
        /,
        *,
        axis: Union[(tuple[(int, int, int)], int)] = ...,
        keepdims: bool = ...,
    ):
        "usage.skimage: 28, usage.xarray: 5"

    def sum(self, /, *, axis: int = ...):
        "usage.skimage: 23, usage.xarray: 3"

    def all(self, /):
        "usage.skimage: 47, usage.xarray: 20"

    def any(self, /):
        "usage.skimage: 4, usage.xarray: 2"

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
        dtype: Union[(list[numpy.float32], numpy.dtype, Literal[("i1",)])] = ...,
    ):
        "usage.skimage: 34, usage.xarray: 89"

    def tolist(self, /):
        "usage.skimage: 6, usage.xarray: 1"

    def std(self, /, *, axis: Union[(tuple[(int, int)], int)] = ...):
        "usage.skimage: 2, usage.xarray: 2"

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
        "usage.skimage: 3, usage.xarray: 2"

    def repeat(self, _0: int, /, *, axis: int = None):
        "usage.skimage: 2"

    def ravel(self, /, *, order: Literal[("F",)] = ...):
        "usage.skimage: 2, usage.xarray: 1"

    def var(self, /, *, axis: int = ...):
        "usage.skimage: 7"

    def reshape(
        self, _0: Union[(int, tuple[(int, int, int, int)], tuple[(int, ...)])] = ..., /
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
                tuple[(int,)],
                numpy.ndarray,
            )
        ] = ...,
        /,
    ):
        "usage.sample_usage: 1, usage.skimage: 6, usage.xarray: 1"


class float64:
    def __init__(x: Union[(numpy.ndarray, int, numpy.int64, float)], /):
        "usage.skimage: 8, usage.xarray: 2"

    ndim = ...
    shape = ...
    dtype = ...

    def __getitem__(self, _0: tuple[(Union[(ellipsis, None)], None)], /):
        ""


class generic:
    @classmethod
    def astype(
        _0,
        _1: Union[
            (
                list[float],
                list[numpy.float64],
                list[numpy.int64],
                Literal[("timedelta64[ns]",)],
            )
        ],
        /,
    ):
        "usage.skimage: 12, usage.xarray: 7"

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
    def __init__(int_type: Union[(list, numpy.dtype)]):
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

    def __getitem__(self, _0: Literal[("F_CONTIGUOUS", "C_CONTIGUOUS")], /):
        ""


class flatiter:
    def __iter__(self, /):
        ""

    def __getitem__(
        self,
        _0: Union[
            (slice[(Union[(int, None)], Union[(int, None)], None)], numpy.int64, int)
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
        _0: Union[(numpy.int32, numpy.float64, int, numpy.ndarray, numpy.int64)], /
    ):
        "usage.skimage: 6, usage.xarray: 1"


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
    def __init__(_0: Union[(int, numpy.int64, numpy.ndarray)], /):
        "usage.skimage: 5, usage.xarray: 1"


class int16:
    def __init__(_0: Union[(list[int], numpy.int64, int)], /):
        "usage.skimage: 2, usage.xarray: 2"


class longlong:
    def __init__(_0: numpy.int64, /):
        "usage.skimage: 1"


class uint16:
    def __init__(_0: Union[(int, numpy.int64)], /):
        "usage.skimage: 2"


class uint32:
    def __init__(_0: numpy.int64, /):
        "usage.skimage: 1"


class uint64:
    def __init__(_0: Union[(int, numpy.int64)], /):
        "usage.skimage: 1, usage.xarray: 2"


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
        pyfunc: Callable, otypes: Union[(list, list[list[float]], None)] = ...
    ):
        "usage.xarray: 75"


class str_:
    def __init__(_0: Literal[("asdf",)], /):
        "usage.xarray: 1"

    dtype = ...

    def __getitem__(self, _0: slice[(Union[(int, None)], Union[(int, None)], int)], /):
        ""


class bytes_:
    def __init__(_0: Literal[("asdf", "z", "x")], /):
        "usage.xarray: 3"

    def __getitem__(self, _0: slice[(Union[(int, None)], Union[(int, None)], int)], /):
        ""


class timedelta64:
    def __init__(_0: Union[(datetime.timedelta, Literal[("NaT",)], int)] = ..., /):
        "usage.xarray: 16"

    dtype = ...


class datetime64:
    def __init__(_0: Literal[("NaT",)], _1: Literal[("ns",)], /):
        "usage.xarray: 1"

    dtype = ...


class broadcast:
    def __init__(
        _0: Union[(numpy.ndarray, int, list[int])],
        _1: Union[
            (list[int], Literal[("z",)], numpy.ndarray, Literal[("_not_supplied",)])
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
