from typing import *

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
flexible = ...
infty = ...
object = ...
intc = ...
NINF = ...
euler_gamma = ...
Inf = ...


def arange(
    _0: Union[(float, int, numpy.float64, dask.array.core.Array, numpy.int64)],
    _1: Union[(float, numpy.int64, int, numpy.float64)] = ...,
    _2: Union[(float, None, int, numpy.float64)] = ...,
    _3: Type[numpy.uint8] = ...,
    /,
    *,
    dtype=...,
):
    "usage.sample_usage: 4, usage.skimage: 223, usage.xarray: 393, usage.sklearn: 151"


def array(
    _0=...,
    /,
    *,
    dtype=...,
    copy: bool = ...,
    ndmin: int = ...,
    order: Union[
        (Literal[("C",)], Literal[("F",)], None, Literal[("F", "K", "C")])
    ] = ...,
):
    "usage.sample_usage: 1, usage.skimage: 1076, usage.xarray: 391, usage.sklearn: 815"


def zeros(
    _0=...,
    _1=...,
    /,
    *,
    dtype=...,
    order: Literal[("f", "F", "C")] = ...,
    shape: Union[(int, Tuple[(int, ...)])] = ...,
):
    "usage.sample_usage: 1, usage.skimage: 787, usage.xarray: 52, usage.sklearn: 350"


def ones(shape, dtype=..., order: Literal[("F", "C")] = ...):
    "usage.sample_usage: 1, usage.skimage: 269, usage.xarray: 59, usage.sklearn: 210"


def linspace(
    start: Union[(float, numpy.int64, numpy.float64, int)],
    stop: Union[(float, numpy.float32, int, numpy.float64, numpy.int64)] = ...,
    num: Union[(int, numpy.int64)] = ...,
):
    "usage.sample_usage: 1, usage.skimage: 70, usage.xarray: 95, usage.sklearn: 41"


def eye(N: int, M: int = ..., dtype: type = ...):
    "usage.sample_usage: 1, usage.skimage: 39, usage.sklearn: 27"


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
    _1=...,
    /,
    *,
    dtype: type = ...,
    out: Union[(xarray.core.dataarray.DataArray, numpy.ndarray)] = ...,
):
    "usage.sample_usage: 1, usage.skimage: 11, usage.xarray: 13, usage.sklearn: 1"


def exp(
    _0: Union[
        (float, numpy.ndarray, xarray.core.dataarray.DataArray, int, numpy.float64)
    ] = ...,
    /,
    *,
    dtype: numpy.dtype = ...,
):
    "usage.sample_usage: 1, usage.skimage: 26, usage.xarray: 3, usage.sklearn: 62"


def log(_0=..., /):
    "usage.sample_usage: 1, usage.skimage: 19, usage.xarray: 2, usage.sklearn: 78"


def column_stack(
    tup: Union[(List[numpy.ndarray], Tuple[(numpy.ndarray, numpy.ndarray)])]
):
    "usage.sample_usage: 1, usage.skimage: 9, usage.sklearn: 2"


def concatenate(_0, /, *, axis: int = ...):
    "usage.sample_usage: 1, usage.skimage: 48, usage.xarray: 45, usage.sklearn: 50"


def absolute(_0=..., /):
    "usage.skimage: 113, usage.sklearn: 154"


def asarray(a, dtype=..., order: Union[(Literal[("C",)], Literal[("F",)], None)] = ...):
    "usage.skimage: 247, usage.xarray: 837, usage.sklearn: 2199"


def sum(
    a,
    axis=...,
    dtype: Union[(Type[numpy.float64], Type[float], None)] = ...,
    keepdims: bool = ...,
):
    "usage.skimage: 125, usage.xarray: 51, usage.sklearn: 208"


def vstack(tup):
    "usage.skimage: 33, usage.sklearn: 69"


def all(
    a: Union[
        (
            pandas.core.series.Series,
            numpy.bool_,
            numpy.ndarray,
            numpy.ma.core.MaskedArray,
            bool,
        )
    ] = ...
):
    "usage.skimage: 113, usage.xarray: 14, usage.sklearn: 91"


def round_(a=...):
    "usage.skimage: 30, usage.sklearn: 3"


def asanyarray(a=...):
    "usage.skimage: 50, usage.sklearn: 14"


def obj2sctype(rep):
    "usage.skimage: 14"


def issubdtype(arg1, arg2: type):
    "usage.skimage: 162, usage.xarray: 256, usage.sklearn: 19"


def multiply(
    _0: numpy.ndarray,
    _1: Union[(float, dask.array.core.Array, numpy.ndarray, int)],
    /,
    *,
    out: numpy.ndarray = ...,
    dtype: Union[(Type[numpy.float64], Type[numpy.float32], numpy.dtype, type)] = ...,
    casting: Literal[("no",)] = ...,
):
    "usage.skimage: 25, usage.xarray: 2, usage.sklearn: 2"


def reshape(a, newshape=...):
    "usage.skimage: 43, usage.xarray: 7, usage.sklearn: 50"


def sqrt(_0=..., /, *, out: numpy.ndarray = ...):
    "usage.skimage: 112, usage.xarray: 4, usage.sklearn: 108"


def moveaxis(
    a: Union[(numpy.ndarray, int, numpy.float64)],
    source: Union[(range, numpy.ndarray, int, Tuple[(None, ...)])],
    destination: Union[(List[int], numpy.ndarray, int, Tuple[(None, ...)])],
):
    "usage.skimage: 6, usage.xarray: 17"


def rollaxis(a: numpy.ndarray, axis: int = ...):
    "usage.skimage: 14, usage.sklearn: 5"


def any(a=...):
    "usage.skimage: 39, usage.xarray: 5, usage.sklearn: 45"


def empty_like(
    _0: Union[
        (
            numpy.ma.core.MaskedArray,
            numpy.ndarray,
            xarray.core.variable.Variable,
            xarray.core.variable.IndexVariable,
        )
    ] = ...,
    /,
    *,
    dtype: Union[(type, numpy.dtype, Type[numpy.float32], Type[object])] = ...,
    subok: bool = ...,
    order: Literal[("C",)] = ...,
):
    "usage.skimage: 48, usage.xarray: 2, usage.sklearn: 22"


def triu(m: numpy.ndarray):
    "usage.skimage: 1"


def seterr(
    divide: Literal[("warn",)] = ...,
    over: Literal[("warn",)] = ...,
    under: Literal[("ignore",)] = ...,
    invalid: Literal[("ignore", "warn")] = ...,
):
    "usage.skimage: 2, usage.sklearn: 4"


def isnan(_0, /):
    "usage.skimage: 14, usage.xarray: 14, usage.sklearn: 30"


def floor(
    _0: Union[(float, numpy.ndarray, xarray.core.dataarray.DataArray, numpy.float64)], /
):
    "usage.skimage: 13, usage.xarray: 2, usage.sklearn: 2"


def stack(arrays=...):
    "usage.skimage: 35, usage.xarray: 26"


def choose(a: numpy.ndarray, choices: List[numpy.ndarray]):
    "usage.skimage: 2"


def amin(a=...):
    "usage.skimage: 60, usage.xarray: 25, usage.sklearn: 30"


def amax(
    a,
    axis: Union[(Tuple[(int, int, int)], None, Tuple[(int, int)], int)] = ...,
    keepdims: bool = ...,
):
    "usage.skimage: 105, usage.xarray: 23, usage.sklearn: 32"


def rint(
    _0: Union[(numpy.ndarray, xarray.core.dataarray.DataArray)],
    /,
    *,
    out: numpy.ndarray = ...,
):
    "usage.skimage: 2, usage.xarray: 2"


def clip(a: Union[(numpy.int64, numpy.ndarray, numpy.float64, int)], a_min, a_max=...):
    "usage.skimage: 61, usage.sklearn: 24"


def power(
    _0: Union[(float, numpy.ndarray, int, numpy.float64)],
    _1: Union[(float, numpy.ndarray, int)],
    /,
):
    "usage.skimage: 11, usage.sklearn: 3"


def log10(
    _0: Union[(numpy.ndarray, xarray.core.dataarray.DataArray, numpy.float64)], /
):
    "usage.skimage: 4, usage.xarray: 2, usage.sklearn: 3"


def load(file: Literal[("/Users/saul/Downloads/scikit-image-0.17.0/skimage/",)]):
    "usage.skimage: 28"


def meshgrid(*xi: Literal[("v", "t")]):
    "usage.skimage: 28, usage.xarray: 6, usage.sklearn: 2"


def dstack(
    tup: Union[
        (
            List[numpy.ndarray],
            Tuple[(numpy.ndarray, ...)],
            List[skimage.feature._hessian_det_appx._memoryviewslice],
            Tuple[(numpy.ndarray, numpy.ndarray)],
        )
    ]
):
    "usage.skimage: 12, usage.sklearn: 4"


def nonzero(a: numpy.ndarray):
    "usage.skimage: 22, usage.xarray: 4, usage.sklearn: 7"


def cbrt(_0: numpy.ndarray, /):
    "usage.skimage: 4"


def hypot(
    _0: Union[(int, numpy.ndarray, xarray.core.dataarray.DataArray, numpy.float64)],
    _1: Union[(int, numpy.ndarray, xarray.core.dataarray.DataArray, numpy.float64)],
    /,
):
    "usage.skimage: 13, usage.xarray: 2"


def arctan2(
    _0: Union[
        (xarray.core.dataarray.DataArray, numpy.ndarray, numpy.float64, numpy.int64)
    ],
    _1: Union[
        (xarray.core.dataarray.DataArray, numpy.ndarray, numpy.float64, numpy.int64)
    ],
    /,
):
    "usage.skimage: 8, usage.xarray: 2"


def where(_0, _1=..., _2=..., /):
    "usage.skimage: 26, usage.xarray: 23, usage.sklearn: 44"


def cos(_0, /):
    "usage.skimage: 48, usage.xarray: 14, usage.sklearn: 11"


def sin(_0, /, *, out=...):
    "usage.skimage: 47, usage.xarray: 18, usage.sklearn: 22"


def ascontiguousarray(
    a: Union[
        (
            List[List[int]],
            numpy.ndarray,
            List[float],
            List[int],
            List[Union[(float, int)]],
        )
    ] = ...
):
    "usage.skimage: 67, usage.sklearn: 21"


def swapaxes(a: numpy.ndarray, axis1: int, axis2: int):
    "usage.skimage: 4, usage.xarray: 8, usage.sklearn: 2"


def ravel(a=...):
    "usage.skimage: 12, usage.xarray: 44, usage.sklearn: 43"


def squeeze(a: Union[(float, numpy.ndarray, int, List[float], numpy.float64)] = ...):
    "usage.skimage: 16, usage.sklearn: 18"


def ones_like(
    a: Union[(numpy.ndarray, xarray.core.variable.Variable, numpy.float64)] = ...
):
    "usage.skimage: 26, usage.xarray: 4, usage.sklearn: 19"


def can_cast(
    _0: Union[(float, int, numpy.dtype, numpy.ndarray)],
    _1: Union[(Type[bool], numpy.dtype)],
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
    order: Literal[("F", "C")] = ...,
    shape: Union[(Tuple[(int,)], Tuple[(int, int)], int)] = ...,
):
    "usage.skimage: 129, usage.xarray: 11, usage.sklearn: 131"


def min_scalar_type(_0: Union[(numpy.float64, int, numpy.int64)], /):
    "usage.skimage: 5"


def unique(
    ar, return_index: bool = ..., return_inverse: bool = ..., return_counts: bool = ...
):
    "usage.skimage: 68, usage.xarray: 14, usage.sklearn: 216"


def zeros_like(
    a: Union[(Tuple[(int, int, int)], Tuple[(int, int)], numpy.ndarray)],
    dtype: type = ...,
    order: Literal[("F", "C")] = ...,
):
    "usage.skimage: 70, usage.xarray: 43, usage.sklearn: 15"


def full(shape, fill_value=...):
    "usage.skimage: 36, usage.xarray: 10, usage.sklearn: 41"


def loadtxt(
    fname: Literal[
        (
            "/usr/local/Caskroom/miniconda/base/envs/python-rec",
            "/Users/saul/Downloads/scikit-image-0.17.0/skimage/",
        )
    ] = ...
):
    "usage.skimage: 1, usage.sklearn: 5"


def logical_and(
    _0: Union[(numpy.bool_, numpy.ndarray, xarray.core.dataarray.DataArray)],
    _1: Union[(numpy.bool_, numpy.ndarray, xarray.core.dataarray.DataArray)],
    /,
):
    "usage.skimage: 13, usage.xarray: 2, usage.sklearn: 1"


def deg2rad(
    _0: Union[(xarray.core.dataarray.DataArray, numpy.ndarray, int, List[int])], /
):
    "usage.skimage: 18, usage.xarray: 2"


def rad2deg(
    _0: Union[(numpy.ndarray, xarray.core.dataarray.DataArray, numpy.float64)], /
):
    "usage.skimage: 6, usage.xarray: 2"


def maximum(
    _0,
    _1=...,
    /,
    *,
    out: numpy.ndarray = ...,
    casting: Literal[("unsafe",)] = ...,
    dtype: numpy.dtype = ...,
):
    "usage.skimage: 16, usage.xarray: 87, usage.sklearn: 20"


def percentile(
    a: numpy.ndarray = ...,
    q: Union[(float, numpy.ndarray, int, List[int], numpy.float64)] = ...,
):
    "usage.skimage: 11, usage.xarray: 20, usage.sklearn: 9"


def logical_not(
    _0: Union[
        (
            numpy.bool_,
            numpy.ndarray,
            xarray.core.dataarray.DataArray,
            dask.array.core.Array,
            bool,
        )
    ],
    /,
    *,
    out: numpy.ndarray = ...,
):
    "usage.skimage: 14, usage.xarray: 10, usage.sklearn: 8"


def isscalar(element):
    "usage.skimage: 67, usage.xarray: 33, usage.sklearn: 5"


def ceil(_0, /):
    "usage.skimage: 31, usage.xarray: 5, usage.sklearn: 17"


def minimum(
    _0: Union[
        (
            Tuple[(int, int)],
            numpy.ndarray,
            xarray.core.dataarray.DataArray,
            int,
            Tuple[(int, int, int)],
        )
    ],
    _1,
    /,
    *,
    out: numpy.ndarray = ...,
):
    "usage.skimage: 9, usage.xarray: 4, usage.sklearn: 11"


def dot(
    _0: Union[
        (List[List[int]], List[List[Union[(float, int)]]], numpy.ndarray, numpy.memmap)
    ],
    _1: Union[(List[Union[(float, int)]], numpy.matrix, numpy.ndarray, numpy.memmap)],
    /,
    *,
    out: numpy.ndarray = ...,
):
    "usage.skimage: 1, usage.sklearn: 322"


def diag(v: numpy.ndarray):
    "usage.skimage: 5, usage.sklearn: 28"


def arcsin(_0: Union[(float, numpy.ndarray, xarray.core.dataarray.DataArray)], /):
    "usage.skimage: 1, usage.xarray: 2"


def ellipkinc(_0: numpy.float64, _1: float, /):
    "usage.skimage: 1"


def ellipeinc(_0: numpy.float64, _1: float, /):
    "usage.skimage: 1"


def transpose(a=...):
    "usage.skimage: 21, usage.xarray: 3, usage.sklearn: 6"


def shape(a: Union[(numpy.ndarray, numpy.ma.core.MaskedArray)]):
    "usage.skimage: 1, usage.xarray: 11, usage.sklearn: 15"


def promote_types(_0: numpy.dtype, _1: numpy.dtype, /):
    "usage.skimage: 1"


def bincount(
    _0: Union[(dask.array.core.Array, numpy.ndarray)] = ...,
    /,
    *,
    minlength: int = ...,
    weights: Union[
        (numpy.ndarray, List[float], None, List[int], List[Union[(float, int)]])
    ] = ...,
):
    "usage.skimage: 12, usage.sklearn: 36"


def histogram(
    a: numpy.ndarray = ...,
    bins: Union[
        (
            int,
            numpy.int64,
            List[Union[(float, int)]],
            Tuple[
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
    x: Union[(numpy.flatiter, numpy.ndarray)], xp: numpy.ndarray, fp: numpy.ndarray
):
    "usage.skimage: 6"


def polyfit(x: numpy.ndarray, y: numpy.ndarray, deg: int):
    "usage.skimage: 1"


def pad(array: Union[(List[List[int]], numpy.ndarray, List[int])], pad_width=...):
    "usage.skimage: 126, usage.xarray: 44"


def product(*args: Literal[("v", "t")]):
    "usage.skimage: 14, usage.sklearn: 1"


def apply_along_axis(
    func1d: Union[(sklearn.gaussian_process.kernels.PairwiseKernel, Callable)],
    axis: int,
    arr: numpy.ndarray,
):
    "usage.skimage: 8, usage.sklearn: 5"


def count_nonzero(a: numpy.ndarray):
    "usage.skimage: 9, usage.sklearn: 12"


def cumsum(a=..., axis: Union[(None, int)] = ..., dtype: Type[numpy.float64] = ...):
    "usage.skimage: 29, usage.xarray: 10, usage.sklearn: 16"


def take_along_axis(arr: numpy.ndarray, indices: numpy.ndarray, axis: int):
    "usage.skimage: 1"


def square(_0: Union[(numpy.ndarray, xarray.core.dataarray.DataArray)], /):
    "usage.skimage: 7, usage.xarray: 2"


def mean(
    a,
    axis: Union[(Tuple[(int,)], None, Tuple[(int, int)], int)] = ...,
    keepdims: bool = ...,
    dtype: Union[(Type[numpy.float64], Type[float], None, type)] = ...,
):
    "usage.skimage: 61, usage.xarray: 32, usage.sklearn: 102"


def log2(
    _0: Union[
        (
            numpy.ndarray,
            xarray.core.dataarray.DataArray,
            int,
            numpy.float64,
            numpy.int64,
        )
    ],
    /,
):
    "usage.skimage: 5, usage.xarray: 2, usage.sklearn: 9"


def allclose(
    a, b, rtol: Union[(float, int)] = ..., equal_nan: bool = ..., atol: float = ...
):
    "usage.skimage: 33, usage.xarray: 20, usage.sklearn: 45"


def argsort(
    a: Union[
        (
            numpy.matrix,
            Tuple[
                (
                    numpy.float64,
                    numpy.float64,
                    numpy.float64,
                    numpy.float64,
                    numpy.float64,
                )
            ],
            numpy.ndarray,
            numpy.flatiter,
            Tuple[(float, float, float, float, float)],
        )
    ] = ...
):
    "usage.skimage: 28, usage.sklearn: 34"


def hstack(tup):
    "usage.skimage: 27, usage.xarray: 1, usage.sklearn: 89"


def argmax(
    a: Union[
        (numpy.matrix, dask.array.core.Array, List[numpy.float64], numpy.ndarray)
    ] = ...
):
    "usage.skimage: 18, usage.xarray: 11, usage.sklearn: 44"


def logspace(
    start: Union[(float, numpy.float64, int)],
    stop: Union[(float, numpy.float64, int)],
    num: int,
):
    "usage.skimage: 2, usage.sklearn: 11"


def logical_or(
    _0: Union[(numpy.ndarray, xarray.core.dataarray.DataArray)],
    _1: Union[(numpy.ndarray, xarray.core.dataarray.DataArray)],
    /,
    *,
    out: numpy.ndarray = ...,
):
    "usage.skimage: 3, usage.xarray: 2, usage.sklearn: 4"


def isinf(
    _0: Union[(float, numpy.ndarray, xarray.core.dataarray.DataArray, numpy.float64)], /
):
    "usage.skimage: 2, usage.xarray: 2, usage.sklearn: 10"


def delete(
    arr: numpy.ndarray,
    obj: Union[(numpy.ndarray, Tuple[(Union[(None, int)], ...)])] = ...,
):
    "usage.skimage: 3, usage.sklearn: 2"


def split(ary: numpy.ndarray, indices_or_sections: Union[(numpy.ndarray, int)]):
    "usage.skimage: 1, usage.sklearn: 4"


def atleast_1d(*arys: Literal[("v", "t")]):
    "usage.skimage: 11, usage.xarray: 23, usage.sklearn: 38"


def isclose(
    a: Union[(float, numpy.ndarray, numpy.float64)],
    b: Union[(float, numpy.float32, numpy.ndarray, int, numpy.float64)],
    rtol: float = ...,
    atol: float = ...,
    equal_nan: bool = ...,
):
    "usage.skimage: 3, usage.xarray: 12, usage.sklearn: 5"


def gradient(
    f: Union[(numpy.ndarray, xarray.core.dataarray.DataArray)],
    *varargs: Literal[("v", "t")],
):
    "usage.skimage: 8, usage.xarray: 5"


def argmin(
    a: Union[
        (
            List[float],
            Tuple[
                (
                    numpy.float64,
                    numpy.float64,
                    numpy.float64,
                    numpy.float64,
                    numpy.float64,
                )
            ],
            List[numpy.float64],
            numpy.ndarray,
        )
    ] = ...
):
    "usage.skimage: 10, usage.xarray: 5, usage.sklearn: 23"


def arctan(
    _0: Union[(numpy.ndarray, xarray.core.dataarray.DataArray, numpy.float64)], /
):
    "usage.skimage: 3, usage.xarray: 2, usage.sklearn: 2"


def sort(
    a: Union[
        (
            List[numpy.float64],
            List[float],
            List[int],
            numpy.ndarray,
            List[Union[(float, int)]],
        )
    ] = ...
):
    "usage.skimage: 14, usage.xarray: 2, usage.sklearn: 31"


def spacing(_0: int, /):
    "usage.skimage: 1"


def isfinite(_0, /):
    "usage.skimage: 7, usage.xarray: 6, usage.sklearn: 19"


def diff(a: Union[(List[numpy.float64], numpy.ndarray)], n: int = ..., axis: int = ...):
    "usage.skimage: 15, usage.xarray: 11, usage.sklearn: 17"


def flatnonzero(a: numpy.ndarray):
    "usage.skimage: 6, usage.xarray: 2, usage.sklearn: 24"


def copy(a: Union[(numpy.ndarray, numpy.float64)] = ...):
    "usage.skimage: 14, usage.sklearn: 23"


def atleast_2d(*arys: Literal[("v", "t")]):
    "usage.skimage: 7, usage.xarray: 2, usage.sklearn: 25"


def rot90(m: numpy.ndarray = ...):
    "usage.skimage: 7"


def roll(
    a: Union[(numpy.ndarray, List[Union[(float, int)]])],
    shift: Union[(Tuple[(int, int)], int)] = ...,
):
    "usage.skimage: 14, usage.xarray: 1"


def indices(
    dimensions: Union[
        (Tuple[(int, int)], generator, Tuple[(Union[(int, numpy.int64)], ...)])
    ] = ...
):
    "usage.skimage: 6, usage.sklearn: 2"


def tri(N: int = ..., M: int = ..., k: int = ...):
    "usage.skimage: 9"


def less(_0, _1: Union[(Tuple[(int, ...)], numpy.ndarray, int)], /):
    "usage.skimage: 3, usage.xarray: 1, usage.sklearn: 5"


def prod(a, axis: int = ..., dtype: Type[numpy.float64] = ...):
    "usage.skimage: 9, usage.xarray: 15, usage.sklearn: 8"


def true_divide(
    _0: numpy.ndarray,
    _1: Union[(numpy.ndarray, numpy.int64)],
    /,
    *,
    out: numpy.ndarray = ...,
):
    "usage.skimage: 2, usage.sklearn: 2"


def unravel_index(
    _0: Union[(numpy.ndarray, int, numpy.int64)], _1: Tuple[(int, ...)], /
):
    "usage.skimage: 18, usage.sklearn: 1"


def apply_over_axes(func: Callable, a: numpy.ndarray, axes: Tuple[(int, int)]):
    "usage.skimage: 10"


def tile(A, reps):
    "usage.skimage: 15, usage.xarray: 5, usage.sklearn: 16"


def real(val: Union[(float, numpy.ndarray, xarray.core.dataarray.DataArray)]):
    "usage.skimage: 8, usage.xarray: 1, usage.sklearn: 1"


def imag(val: Union[(numpy.ndarray, xarray.core.dataarray.DataArray)]):
    "usage.skimage: 1, usage.xarray: 1"


def sign(
    _0: Union[(xarray.core.dataarray.DataArray, numpy.ndarray, numpy.float64, int)], /
):
    "usage.skimage: 4, usage.xarray: 3, usage.sklearn: 24"


def subtract(
    _0: Union[(numpy.ndarray, int)],
    _1: Union[(dask.array.core.Array, numpy.ndarray)] = ...,
    /,
    *,
    dtype: numpy.dtype = ...,
):
    "usage.skimage: 11, usage.xarray: 2, usage.sklearn: 1"


def ix_(*args: Literal[("v", "t")]):
    "usage.skimage: 2, usage.xarray: 3, usage.sklearn: 2"


def convolve(a: numpy.ndarray, v: List[float], mode: Literal[("valid",)]):
    "usage.skimage: 1"


def invert(_0: Union[(numpy.ndarray, List[bool])], /):
    "usage.skimage: 7"


def array_equal(
    a1: Union[(Tuple[(float, float, float)], numpy.ndarray, List[float], List[int])], a2
):
    "usage.skimage: 5, usage.xarray: 3, usage.sklearn: 12"


def reciprocal(_0: numpy.ndarray, /, *, out: numpy.ndarray = None):
    "usage.skimage: 1"


def insert(arr: numpy.ndarray, obj: int, values: Union[(numpy.ndarray, int)] = ...):
    "usage.skimage: 3, usage.sklearn: 1"


def full_like(
    a: Union[
        (xarray.core.variable.Variable, numpy.ndarray, xarray.core.dataarray.DataArray)
    ],
    fill_value: Union[(float, bool, int)] = ...,
):
    "usage.skimage: 1, usage.xarray: 7, usage.sklearn: 3"


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
    "usage.skimage: 5, usage.xarray: 1, usage.sklearn: 15"


def asfortranarray(a: Union[(List[List[int]], numpy.ndarray)] = ...):
    "usage.skimage: 1, usage.sklearn: 20"


def cross(a: numpy.ndarray, b: numpy.ndarray):
    "usage.skimage: 5"


def einsum(*operands: Literal[("v", "t")]):
    "usage.skimage: 1, usage.xarray: 44, usage.sklearn: 10"


def nan_to_num(x: Union[(List[numpy.float64], numpy.ndarray)]):
    "usage.skimage: 1, usage.sklearn: 2"


def frombuffer(
    _0: Union[(array.array, numpy.ndarray, bytes)] = ...,
    /,
    *,
    dtype: Union[(Literal[("int8",)], type)] = ...,
):
    "usage.skimage: 1, usage.sklearn: 8"


def fliplr(m: numpy.ndarray):
    "usage.skimage: 5"


def tril(m: numpy.ndarray = ...):
    "usage.skimage: 1, usage.sklearn: 1"


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
    _2: Union[
        (dask.array.core.Array, numpy.dtype, numpy.ndarray, Type[numpy.float32])
    ] = ...,
    _3: Union[(dask.array.core.Array, numpy.dtype, numpy.ndarray)] = ...,
    _4: Union[(dask.array.core.Array, numpy.dtype, numpy.ndarray)] = ...,
    _5: Union[(dask.array.core.Array, numpy.dtype, numpy.ndarray)] = ...,
    _6: Union[(dask.array.core.Array, numpy.dtype, numpy.ndarray)] = ...,
    _7: Union[(dask.array.core.Array, numpy.dtype, numpy.ndarray)] = ...,
    _8: Union[(dask.array.core.Array, numpy.dtype, numpy.ndarray)] = ...,
    _9: Union[(dask.array.core.Array, numpy.dtype, numpy.ndarray)] = ...,
    _10: Union[(dask.array.core.Array, numpy.dtype, numpy.ndarray)] = ...,
    _11: Union[(dask.array.core.Array, numpy.dtype, numpy.ndarray)] = ...,
    _12: Union[(dask.array.core.Array, numpy.dtype, numpy.ndarray)] = ...,
    _13: Union[(dask.array.core.Array, numpy.dtype, numpy.ndarray)] = ...,
    _14: Union[(dask.array.core.Array, numpy.dtype, numpy.ndarray)] = ...,
    _15: Union[(dask.array.core.Array, numpy.dtype, numpy.ndarray)] = ...,
    _16: Union[(dask.array.core.Array, numpy.dtype, numpy.ndarray)] = ...,
    _17: Union[(dask.array.core.Array, numpy.dtype, numpy.ndarray)] = ...,
    _18: Union[(dask.array.core.Array, numpy.dtype, numpy.ndarray)] = ...,
    _19: Union[(dask.array.core.Array, numpy.dtype, numpy.ndarray)] = ...,
    /,
):
    "usage.skimage: 7, usage.xarray: 94, usage.sklearn: 10"


def ptp(a: numpy.ndarray = ...):
    "usage.skimage: 10, usage.sklearn: 2"


def cumprod(a: Union[(Tuple[(int, ...)], numpy.ndarray)] = ...):
    "usage.skimage: 5, usage.xarray: 4"


def ravel_multi_index(
    _0, _1: Tuple[(int, ...)], /, *, order: Literal[("F", "C")] = ...
):
    "usage.skimage: 18"


def logical_xor(
    _0: Union[(numpy.ndarray, xarray.core.dataarray.DataArray)],
    _1: Union[(numpy.ndarray, xarray.core.dataarray.DataArray)],
    /,
    *,
    out: numpy.ndarray = ...,
):
    "usage.skimage: 1, usage.xarray: 2"


def in1d(
    ar1: Union[(numpy.flatiter, numpy.ndarray)],
    ar2: Union[(Tuple[(int, int)], List[numpy.float64], numpy.ndarray)],
):
    "usage.skimage: 2, usage.sklearn: 13"


def take(
    a: Union[
        (
            List[Literal[("one", "three", "two")]],
            numpy.ndarray,
            List[Literal[("one", "two")]],
            List[int],
        )
    ] = ...,
    indices: Union[(numpy.ndarray, int, List[int])] = ...,
):
    "usage.skimage: 1, usage.xarray: 11, usage.sklearn: 8"


def lexsort(
    _0: Tuple[(Union[(numpy.ndarray, xarray.core.dataarray.DataArray)], ...)], /
):
    "usage.skimage: 1, usage.xarray: 2"


def fmax(
    _0: Union[(numpy.ndarray, xarray.core.dataarray.DataArray)],
    _1: Union[(float, numpy.ndarray, xarray.core.dataarray.DataArray, numpy.float64)],
    /,
):
    "usage.skimage: 3, usage.xarray: 2"


def fix(x: Union[(float, xarray.core.dataarray.DataArray, numpy.float64)]):
    "usage.skimage: 2, usage.xarray: 1"


def tensordot(
    a: numpy.ndarray,
    b: Union[(range, numpy.ndarray)],
    axes: Union[(Tuple[(List[int], List[int])], Tuple[(int, int)], List[int])],
):
    "usage.skimage: 1, usage.xarray: 5"


def atleast_3d(*arys: Literal[("v", "t")]):
    "usage.skimage: 11, usage.sklearn: 6"


def iscomplexobj(x: numpy.ndarray):
    "usage.skimage: 4, usage.sklearn: 1"


def conjugate(_0: Union[(numpy.ndarray, xarray.core.dataarray.DataArray)], /):
    "usage.skimage: 2, usage.xarray: 2, usage.sklearn: 1"


def angle(z: Union[(numpy.ndarray, xarray.core.dataarray.DataArray)]):
    "usage.skimage: 3, usage.xarray: 2"


def require(
    a: numpy.ndarray,
    requirements: Union[(List[Literal[("C",)]], Literal[("W",)])] = ...,
):
    "usage.skimage: 1, usage.sklearn: 4"


def tanh(_0: Union[(numpy.ndarray, xarray.core.dataarray.DataArray)] = ..., /):
    "usage.skimage: 2, usage.xarray: 2, usage.sklearn: 3"


def ndim(a: Union[(numpy.ndarray, numpy.float64)]):
    "usage.skimage: 4, usage.sklearn: 4"


def searchsorted(a: numpy.ndarray, v):
    "usage.skimage: 3, usage.xarray: 1, usage.sklearn: 38"


def fill_diagonal(a: numpy.ndarray, val: Union[(float, int)]):
    "usage.skimage: 1, usage.sklearn: 10"


def array2string(a: numpy.ndarray, separator: Literal[(", ",)]):
    "usage.skimage: 1"


def std(a: numpy.ndarray = ...):
    "usage.skimage: 1, usage.xarray: 3, usage.sklearn: 6"


def hamming(M: int):
    "usage.skimage: 1"


def hanning(M: int):
    "usage.skimage: 1"


def around(a: Union[(Tuple[(numpy.float64, numpy.float64)], numpy.ndarray)]):
    "usage.skimage: 1, usage.xarray: 4"


def alltrue(*args: Literal[("v", "t")]):
    "usage.skimage: 2"


def may_share_memory(
    _0: Union[
        (
            scipy.sparse.csr.csr_matrix,
            scipy.sparse.lil.lil_matrix,
            numpy.ndarray,
            scipy.sparse.csc.csc_matrix,
        )
    ],
    _1,
    /,
):
    "usage.skimage: 2, usage.sklearn: 44"


def isnat(_0: Union[(dask.array.core.Array, numpy.ndarray)], /):
    "usage.xarray: 6"


def get_printoptions():
    "usage.xarray: 3"


def broadcast_arrays(*args: Literal[("v", "t")]):
    "usage.xarray: 3"


def broadcast_to(
    array: Union[(float, numpy.ndarray)], shape: Tuple[(Union[(None, int)], ...)]
):
    "usage.xarray: 25"


def nanmean(
    a: numpy.ndarray,
    axis: Union[
        (Tuple[(int,)], Tuple[(int, int)], int, Tuple[(None, ...)], None)
    ] = ...,
    dtype: Union[
        (
            Type[float],
            Type[numpy.float32],
            Type[numpy.float64],
            None,
            Type[numpy.float16],
        )
    ] = ...,
):
    "usage.xarray: 21, usage.sklearn: 3"


def nanstd(
    a: numpy.ndarray, axis: Union[(None, int)], dtype: None = ..., ddof: int = ...
):
    "usage.xarray: 3, usage.sklearn: 1"


def nanargmax(a: numpy.ndarray, axis: Union[(None, int)]):
    "usage.xarray: 5"


def nanargmin(a: numpy.ndarray, axis: int):
    "usage.xarray: 4"


def expand_dims(a: numpy.ndarray, axis: int):
    "usage.xarray: 5, usage.sklearn: 2"


def nanquantile(
    a: numpy.ndarray,
    q: numpy.ndarray,
    axis: numpy.ndarray,
    interpolation: Literal[("linear",)],
):
    "usage.xarray: 2"


def nanpercentile(
    a: numpy.ndarray,
    q: Union[(Tuple[(float, float)], numpy.ndarray, numpy.float64)] = ...,
):
    "usage.xarray: 20, usage.sklearn: 1"


def quantile(
    a: numpy.ndarray,
    q: numpy.ndarray,
    axis: numpy.ndarray,
    interpolation: Literal[("linear",)],
):
    "usage.xarray: 1"


def repeat(
    a: Union[(float, numpy.ndarray, int, numpy.float64, numpy.int64)],
    repeats: Union[(numpy.ndarray, int, numpy.int64)] = ...,
):
    "usage.xarray: 4, usage.sklearn: 33"


def isin(
    element: Union[(dask.array.core.Array, numpy.ndarray)],
    test_elements: Union[(numpy.ndarray, List[int])],
):
    "usage.xarray: 5"


def nansum(a: Union[(numpy.ndarray, numpy.ma.core.MaskedArray)] = ...):
    "usage.xarray: 8, usage.sklearn: 3"


def nanmax(a: numpy.ndarray = ...):
    "usage.xarray: 17, usage.sklearn: 1"


def nanmin(a: numpy.ndarray = ...):
    "usage.xarray: 16, usage.sklearn: 2"


def nancumsum(a: numpy.ndarray, axis: int, dtype: None):
    "usage.xarray: 1"


def nancumprod(a: numpy.ndarray, axis: int, dtype: None):
    "usage.xarray: 1"


def var(
    a: Union[(List[List[float]], numpy.ndarray)] = ...,
    axis: Union[(None, int, Tuple[(None, ...)])] = ...,
    ddof: int = ...,
):
    "usage.xarray: 22, usage.sklearn: 22"


def nanvar(
    a: numpy.ndarray,
    axis: Union[(None, int)] = ...,
    dtype: Union[(Type[float], None)] = ...,
    ddof: int = ...,
):
    "usage.xarray: 17, usage.sklearn: 3"


def nanmedian(a: numpy.ndarray, axis: Union[(None, int)]):
    "usage.xarray: 3, usage.sklearn: 1"


def datetime_data(_0: numpy.dtype, /):
    "usage.xarray: 1"


def trapz(
    y: Union[(dask.array.core.Array, numpy.ndarray, xarray.core.dataarray.DataArray)],
    x: Union[(numpy.ndarray, xarray.core.dataarray.DataArray)] = ...,
):
    "usage.xarray: 4, usage.sklearn: 1"


def nanprod(
    a: numpy.ndarray,
    axis: Union[(None, Tuple[(int, int)], int)],
    dtype: None,
    out: None,
):
    "usage.xarray: 9"


def greater(_0: numpy.ndarray, _1: numpy.ndarray, /):
    "usage.xarray: 1"


def frexp(
    _0: Union[
        (
            xarray.core.dataarray.DataArray,
            xarray.core.variable.Variable,
            numpy.ndarray,
            int,
            xarray.core.dataset.Dataset,
        )
    ],
    /,
):
    "usage.xarray: 7"


def arccos(_0: Union[(xarray.core.dataarray.DataArray, numpy.ndarray)], /):
    "usage.xarray: 2"


def arccosh(_0: Union[(xarray.core.dataarray.DataArray, numpy.ndarray)], /):
    "usage.xarray: 2"


def arcsinh(_0: Union[(xarray.core.dataarray.DataArray, numpy.ndarray)], /):
    "usage.xarray: 2"


def arctanh(_0: Union[(xarray.core.dataarray.DataArray, numpy.ndarray)], /):
    "usage.xarray: 2"


def copysign(
    _0: Union[(xarray.core.dataarray.DataArray, numpy.ndarray)],
    _1: Union[(xarray.core.dataarray.DataArray, numpy.ndarray)],
    /,
):
    "usage.xarray: 2"


def cosh(_0: Union[(xarray.core.dataarray.DataArray, numpy.ndarray)], /):
    "usage.xarray: 2"


def degrees(_0: Union[(xarray.core.dataarray.DataArray, numpy.ndarray)], /):
    "usage.xarray: 2"


def expm1(_0: Union[(xarray.core.dataarray.DataArray, numpy.ndarray)], /):
    "usage.xarray: 2"


def fabs(_0: Union[(numpy.ndarray, xarray.core.dataarray.DataArray, numpy.float64)], /):
    "usage.xarray: 2, usage.sklearn: 1"


def greater_equal(_0: numpy.ndarray, _1: int, /):
    "usage.xarray: 1"


def fmin(
    _0: Union[(xarray.core.dataarray.DataArray, numpy.ndarray)],
    _1: Union[(xarray.core.dataarray.DataArray, numpy.ndarray)],
    /,
):
    "usage.xarray: 2"


def fmod(
    _0: Union[(xarray.core.dataarray.DataArray, numpy.ndarray)],
    _1: Union[(xarray.core.dataarray.DataArray, numpy.ndarray)],
    /,
):
    "usage.xarray: 2"


def iscomplex(x: xarray.core.dataarray.DataArray):
    "usage.xarray: 1"


def isreal(x: Union[(numpy.ndarray, xarray.core.dataarray.DataArray)]):
    "usage.xarray: 1, usage.sklearn: 1"


def ldexp(
    _0: Union[(xarray.core.dataarray.DataArray, numpy.ndarray)],
    _1: Union[(xarray.core.dataarray.DataArray, numpy.ndarray)],
    /,
):
    "usage.xarray: 2"


def log1p(_0: Union[(numpy.ndarray, xarray.core.dataarray.DataArray)], /):
    "usage.xarray: 2, usage.sklearn: 1"


def logaddexp(
    _0: Union[(float, xarray.core.dataarray.DataArray, numpy.ndarray, int)],
    _1: Union[(float, numpy.ndarray, xarray.core.dataarray.DataArray)],
    /,
):
    "usage.xarray: 2, usage.sklearn: 7"


def logaddexp2(
    _0: Union[(xarray.core.dataarray.DataArray, numpy.ndarray)],
    _1: Union[(xarray.core.dataarray.DataArray, numpy.ndarray)],
    /,
):
    "usage.xarray: 2"


def nextafter(
    _0: Union[(numpy.ndarray, xarray.core.dataarray.DataArray)],
    _1: Union[(numpy.ndarray, xarray.core.dataarray.DataArray, int)],
    /,
):
    "usage.xarray: 2, usage.sklearn: 2"


def radians(_0: Union[(xarray.core.dataarray.DataArray, numpy.ndarray)], /):
    "usage.xarray: 2"


def signbit(_0: Union[(xarray.core.dataarray.DataArray, numpy.ndarray)], /):
    "usage.xarray: 2"


def sinh(_0: Union[(xarray.core.dataarray.DataArray, numpy.ndarray)], /):
    "usage.xarray: 2"


def tan(_0: Union[(xarray.core.dataarray.DataArray, numpy.ndarray)], /):
    "usage.xarray: 2"


def trunc(_0: Union[(xarray.core.dataarray.DataArray, numpy.ndarray)], /):
    "usage.xarray: 2"


def outer(a: numpy.ndarray, b: numpy.ndarray):
    "usage.sklearn: 6"


def compress(condition: numpy.ndarray, a: numpy.ndarray):
    "usage.sklearn: 4"


def size(
    a: Union[
        (
            Tuple[(int, int, int)],
            Tuple[(None, ...)],
            Tuple[(int,)],
            numpy.ndarray,
            Tuple[(int, int)],
        )
    ]
):
    "usage.sklearn: 18"


def diag_indices_from(arr: numpy.ndarray):
    "usage.sklearn: 3"


def triu_indices(n: int, k: int):
    "usage.sklearn: 2"


def append(arr: numpy.ndarray, values: Union[(numpy.ndarray, float)] = ...):
    "usage.sklearn: 15"


def argpartition(a: numpy.ndarray, kth: Union[(int, numpy.int64)], axis: int):
    "usage.sklearn: 3"


def array_equiv(a1: numpy.ndarray, a2: numpy.ndarray):
    "usage.sklearn: 1"


def array_split(ary: numpy.ndarray, indices_or_sections: int):
    "usage.sklearn: 1"


def setdiff1d(ar1: numpy.ndarray, ar2: numpy.ndarray = ...):
    "usage.sklearn: 10"


def average(a: Union[(numpy.ndarray, List[int])], weights=...):
    "usage.sklearn: 69"


def cov(m: numpy.ndarray = ...):
    "usage.sklearn: 4"


def trace(a: numpy.ndarray):
    "usage.sklearn: 4"


def union1d(ar1: numpy.ndarray, ar2: numpy.ndarray):
    "usage.sklearn: 5"


def matmul(_0: numpy.ndarray, _1: numpy.ndarray, /):
    "usage.sklearn: 1"


def fromiter(
    _0: Union[(generator, itertools.chain)],
    /,
    *,
    dtype: Union[(Type[numpy.float64], Literal[("float64",)])] = None,
    count: int = ...,
):
    "usage.sklearn: 3"


def unpackbits(_0: numpy.ndarray, /):
    "usage.sklearn: 1"


def resize(a: numpy.ndarray, new_shape: Union[(int, Tuple[(int, int)])]):
    "usage.sklearn: 6"


def identity(n: int):
    "usage.sklearn: 1"


def find_common_type(array_types: List[numpy.dtype], scalar_types: list):
    "usage.sklearn: 2"


def gammaln(_0: Union[(numpy.ndarray, float)], /):
    "usage.sklearn: 5"


def psi(_0: Union[(numpy.float64, numpy.ndarray, int, numpy.int64)], /):
    "usage.sklearn: 9"


def expit(_0: Union[(numpy.ndarray, numpy.float64)], /, *, out: numpy.ndarray = ...):
    "usage.sklearn: 13"


def ediff1d(ary: numpy.ndarray, to_begin: float):
    "usage.sklearn: 1"


def digitize(x: numpy.ndarray, bins: numpy.ndarray):
    "usage.sklearn: 1"


def fdtrc(_0: int, _1: numpy.int64, _2: numpy.ndarray, /):
    "usage.sklearn: 1"


def corrcoef(x: numpy.ndarray = ...):
    "usage.sklearn: 3"


def xlogy(_0: numpy.ndarray, _1: numpy.ndarray, /):
    "usage.sklearn: 1"


def chdtrc(_0: int, _1: numpy.ndarray, /):
    "usage.sklearn: 1"


def asmatrix(data: numpy.ndarray):
    "usage.sklearn: 2"


def iterable(y):
    "usage.sklearn: 9"


def erf(_0: numpy.ndarray, /):
    "usage.sklearn: 1"


def inner(_0: numpy.ndarray, _1: numpy.ndarray, /):
    "usage.sklearn: 4"


def gamma(_0: float, /):
    "usage.sklearn: 1"


def kv(_0: float, _1: numpy.ndarray, /):
    "usage.sklearn: 1"


def equal(_0: numpy.ndarray, _1, /):
    "usage.sklearn: 9"


def vander(x: numpy.ndarray, N: int):
    "usage.sklearn: 1"


def not_equal(_0: numpy.ndarray, _1: numpy.ndarray, /):
    "usage.sklearn: 1"


def isposinf(x: Union[(float, int)]):
    "usage.sklearn: 2"


class ndarray:
    __name__ = ...

    @classmethod
    def mean(_0: numpy.ndarray = ..., /):
        "usage.sample_usage: 1, usage.skimage: 23, usage.xarray: 1, usage.sklearn: 62"

    @classmethod
    def sum(_0: numpy.ndarray = ..., /):
        "usage.sample_usage: 1, usage.skimage: 86, usage.xarray: 10, usage.sklearn: 147"

    @classmethod
    def sort(_0: numpy.ndarray, /):
        "usage.sample_usage: 1, usage.sklearn: 1"

    @classmethod
    def reshape(
        _0: Union[(numpy.matrix, numpy.ndarray)],
        _1,
        _2: int = ...,
        _3: int = ...,
        _4: int = ...,
        /,
    ):
        "usage.sample_usage: 2, usage.skimage: 168, usage.xarray: 189, usage.sklearn: 163"

    @classmethod
    def astype(_0: numpy.ndarray, _1, /):
        "usage.sample_usage: 1, usage.skimage: 555, usage.xarray: 75, usage.sklearn: 149"

    @classmethod
    def copy(_0: Union[(numpy.ndarray, numpy.memmap)] = ..., /):
        "usage.skimage: 135, usage.xarray: 14, usage.sklearn: 129"

    @classmethod
    def max(_0: numpy.ndarray = ..., /):
        "usage.skimage: 108, usage.xarray: 15, usage.sklearn: 31"

    @classmethod
    def ptp(_0: numpy.ndarray = ..., /):
        "usage.skimage: 5"

    @classmethod
    def min(_0: numpy.ndarray = ..., /):
        "usage.skimage: 80, usage.xarray: 16, usage.sklearn: 29"

    @classmethod
    def any(_0: numpy.ndarray, /):
        "usage.skimage: 11, usage.xarray: 6, usage.sklearn: 13"

    @classmethod
    def nonzero(_0: Union[(numpy.matrix, numpy.ndarray)], /):
        "usage.skimage: 4, usage.xarray: 4, usage.sklearn: 5"

    @classmethod
    def fill(_0: numpy.ndarray, _1: Union[(float, bool, int, numpy.float64)], /):
        "usage.skimage: 5, usage.sklearn: 26"

    @classmethod
    def flatten(_0: numpy.ndarray, /):
        "usage.skimage: 16, usage.xarray: 5, usage.sklearn: 7"

    @classmethod
    def ravel(_0: numpy.ndarray = ..., /):
        "usage.skimage: 207, usage.xarray: 38, usage.sklearn: 142"

    @classmethod
    def cumsum(_0: numpy.ndarray, /):
        "usage.skimage: 1, usage.sklearn: 3"

    @classmethod
    def transpose(_0: numpy.ndarray, _1=..., _2: int = ..., _3: int = ..., /):
        "usage.skimage: 5, usage.xarray: 13, usage.sklearn: 8"

    @classmethod
    def argmin(_0: numpy.ndarray = ..., /):
        "usage.skimage: 2, usage.sklearn: 3"

    @classmethod
    def view(_0: numpy.ndarray = ..., /):
        "usage.skimage: 22, usage.xarray: 11, usage.sklearn: 4"

    @classmethod
    def swapaxes(_0: numpy.ndarray, _1: int, _2: int, /):
        "usage.skimage: 2, usage.sklearn: 1"

    @classmethod
    def argsort(_0: numpy.ndarray = ..., /):
        "usage.skimage: 5, usage.sklearn: 7"

    @classmethod
    def argmax(_0: numpy.ndarray = ..., /):
        "usage.skimage: 6, usage.sklearn: 5"

    @classmethod
    def std(_0: numpy.ndarray, /):
        "usage.skimage: 63, usage.xarray: 2, usage.sklearn: 8"

    @classmethod
    def all(_0: numpy.ndarray, /):
        "usage.skimage: 1, usage.xarray: 9, usage.sklearn: 5"

    @classmethod
    def tobytes(_0: numpy.ndarray, /):
        "usage.skimage: 2"

    @classmethod
    def tolist(_0: Union[(numpy.ndarray, numpy.memmap)], /):
        "usage.skimage: 1, usage.xarray: 17, usage.sklearn: 23"

    @classmethod
    def dot(_0: numpy.ndarray, _1: numpy.ndarray, /):
        "usage.skimage: 1, usage.sklearn: 50"

    @classmethod
    def conj(_0: numpy.ndarray, /):
        "usage.skimage: 4"

    @classmethod
    def item(_0: numpy.ndarray, /):
        "usage.xarray: 18"

    @classmethod
    def squeeze(_0: numpy.ndarray, /):
        "usage.xarray: 3, usage.sklearn: 14"

    @classmethod
    def clip(_0: numpy.ndarray, _1: int, _2: Union[(float, int)] = ..., /):
        "usage.xarray: 1, usage.sklearn: 2"

    @classmethod
    def take(_0: numpy.ndarray, _1: numpy.ndarray, /):
        "usage.sklearn: 8"

    @classmethod
    def tostring(_0: numpy.ndarray, /):
        "usage.sklearn: 1"

    @classmethod
    def repeat(_0: numpy.ndarray, _1: numpy.ndarray, /):
        "usage.sklearn: 1"

    @classmethod
    def var(_0: numpy.ndarray, /):
        "usage.sklearn: 1"

    @classmethod
    def searchsorted(_0: numpy.ndarray, _1: numpy.int64, /):
        "usage.sklearn: 1"

    @classmethod
    def round(_0: numpy.ndarray, /):
        "usage.sklearn: 2"

    shape = ...
    ndim = ...
    dtype = ...
    size = ...
    T = ...
    flags = ...
    flat: numpy.ndarray = ...
    itemsize = ...
    strides: Tuple[(int, int, int)] = ...
    coords = ...
    variables = ...
    variable = ...
    base = ...
    real = ...
    imag = ...
    dims = ...
    attrs = ...
    columns = ...
    __class__ = ...
    nbytes = ...

    def __iter__(self, /):
        ""

    def __getitem__(self, _0, /):
        ""

    def __setitem__(self, _0, _1, /):
        ""

    def sort(self, /, *, axis: int = ..., order: Literal[("accumulator",)] = ...):
        "usage.sample_usage: 1, usage.skimage: 9, usage.sklearn: 1"

    def mean(
        self,
        /,
        *,
        axis: Union[(Tuple[(int, int, int)], int)] = ...,
        keepdims: bool = ...,
    ):
        "usage.skimage: 28, usage.xarray: 5, usage.sklearn: 48"

    def sum(self, /, *, axis: int = ..., dtype: Type[numpy.float64] = ...):
        "usage.skimage: 23, usage.xarray: 3, usage.sklearn: 96"

    def all(self, /, *, axis: int = ...):
        "usage.skimage: 47, usage.xarray: 20, usage.sklearn: 35"

    def any(self, /, *, axis: int = ...):
        "usage.skimage: 4, usage.xarray: 2, usage.sklearn: 20"

    def min(self, /, *, axis: int = ...):
        "usage.skimage: 18, usage.sklearn: 10"

    def max(self, /, *, axis: int = ...):
        "usage.skimage: 18, usage.sklearn: 3"

    def cumsum(self, /, *, axis: int = None):
        "usage.skimage: 6"

    def argmax(self, /, *, axis: int = ...):
        "usage.skimage: 1, usage.sklearn: 9"

    def astype(
        self=...,
        /,
        *,
        copy: bool = ...,
        dtype: Union[
            (
                Type[numpy.float32],
                Literal[(">u4",)],
                numpy.dtype,
                Type[bool],
                Literal[("i1",)],
            )
        ] = ...,
    ):
        "usage.skimage: 34, usage.xarray: 89, usage.sklearn: 62"

    def tolist(self, /):
        "usage.skimage: 6, usage.xarray: 1"

    def std(self, /, *, axis: Union[(Tuple[(int, int)], int)] = ..., ddof: int = ...):
        "usage.skimage: 2, usage.xarray: 2, usage.sklearn: 10"

    def view(
        self,
        /,
        *,
        dtype: Union[(Literal[("|S80", "|S512", "|S16")], Type[numpy.uint8])] = None,
    ):
        "usage.skimage: 4, usage.sklearn: 3"

    def clip(
        self,
        _0: int = ...,
        _1: int = ...,
        /,
        *,
        min: int = ...,
        max: Tuple[(int, ...)] = ...,
    ):
        "usage.skimage: 3, usage.xarray: 2"

    def repeat(self, _0: int, /, *, axis: int = None):
        "usage.skimage: 2"

    def ravel(self, /, *, order: Literal[("F", "C")] = ...):
        "usage.skimage: 2, usage.xarray: 1, usage.sklearn: 2"

    def var(self, /, *, axis: int = ...):
        "usage.skimage: 7"

    def reshape(
        self,
        _0: Union[(Tuple[(int, ...)], Tuple[(int, int, int, int)], int)],
        _1: int = ...,
        _2: int = ...,
        /,
    ):
        "usage.xarray: 6, usage.sklearn: 5"

    def transpose(self, _0: List[int], /):
        "usage.xarray: 6"

    def round(self, /):
        "usage.xarray: 2"

    def argsort(self, /):
        "usage.xarray: 2"

    def item(self, /):
        "usage.xarray: 2"

    def take(
        self,
        _0: Union[(List[numpy.int64], numpy.ndarray, int)],
        /,
        *,
        axis: Union[(None, int)] = ...,
        mode: Literal[("clip",)] = ...,
    ):
        "usage.xarray: 4, usage.sklearn: 70"

    def searchsorted(self, _0: int, /):
        "usage.xarray: 1"

    def argmin(self, /, *, axis: int = None):
        "usage.sklearn: 3"

    def squeeze(self, /, *, axis: int = ...):
        "usage.sklearn: 3"

    def copy(self, /, *, order: Literal[("F", "K")] = None):
        "usage.sklearn: 4"

    def setflags(self, /, *, write: bool = None):
        "usage.sklearn: 3"


class dtype:
    def __init__(_0: Literal[("float32",)], /):
        "usage.sklearn: 1"

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
                Tuple[(int,)],
                List[numpy.ndarray],
                numpy.ndarray,
                xarray.core.dataarray.DataArray,
            )
        ] = ...,
        /,
    ):
        "usage.sample_usage: 1, usage.skimage: 6, usage.xarray: 1"

    @classmethod
    def reduceat(_0: Callable, _1: numpy.ndarray, _2: numpy.ndarray, /):
        "usage.sklearn: 2"


class float64:
    def __init__(x: Union[(float, numpy.ndarray, int, bool, numpy.int64)], /):
        "usage.skimage: 8, usage.xarray: 2, usage.sklearn: 4"

    ndim = ...
    shape = ...
    dtype = ...

    def __getitem__(self, _0: Tuple[(Union[(ellipsis, None)], None)], /):
        ""


class generic:
    @classmethod
    def astype(
        _0,
        _1: Union[
            (
                Type[numpy.int64],
                Type[float],
                Literal[("timedelta64[ns]",)],
                Type[numpy.float64],
            )
        ],
        /,
    ):
        "usage.skimage: 12, usage.xarray: 7, usage.sklearn: 1"

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
        "usage.xarray: 3, usage.sklearn: 2"

    @classmethod
    def any(_0: numpy.bool_, /):
        "usage.xarray: 2"

    @classmethod
    def mean(_0: numpy.float64, /):
        "usage.sklearn: 2"


class iinfo:
    def __init__(
        int_type: Union[(Type[numpy.uint32], numpy.dtype, Literal[("i",)], type)]
    ):
        "usage.skimage: 33, usage.sklearn: 3"

    min = ...
    max = ...


class finfo:
    eps = ...
    resolution = ...
    max = ...
    min = ...
    tiny = ...


class flagsobj:
    writeable: bool = ...
    f_contiguous = ...
    c_contiguous = ...
    owndata = ...
    contiguous = ...

    def __getitem__(self, _0: Literal[("C_CONTIGUOUS", "F_CONTIGUOUS")], /):
        ""


class flatiter:
    def __iter__(self, /):
        ""

    def __getitem__(
        self,
        _0: Union[
            (
                slice[(Union[(None, int)], Union[(None, int)], None)],
                slice[(None, None, int)],
                int,
                numpy.int64,
            )
        ],
        /,
    ):
        ""

    def __setitem__(
        self,
        _0: Union[(slice[(Union[(None, int)], None, int)], numpy.ndarray, List[int])],
        _1: Union[(float, numpy.ndarray, int)],
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
        _0: Union[(numpy.ndarray, int, numpy.float64, numpy.int32, numpy.int64)], /
    ):
        "usage.skimage: 6, usage.xarray: 1"


class int64:
    def __init__(_0: Union[(numpy.ndarray, int)], /):
        "usage.sklearn: 4"

    ndim = ...
    shape = ...
    dtype = ...

    def __getitem__(self, _0: Tuple[(None, ellipsis)], /):
        ""


class float32:
    dtype = ...


class matrix:
    A = ...
    shape = ...

    def max(self, /):
        "usage.sklearn: 3"

    def __getitem__(self, _0: Tuple[(int, slice[(None, None, None)])], /):
        ""


class complex128:
    imag = ...
    real = ...


class nditer:
    multi_index = ...

    def __iter__(self, /):
        ""


class int32:
    def __init__(_0: Union[(numpy.ndarray, int)], /):
        "usage.sklearn: 3"

    dtype = ...


class int8:
    def __init__(_0: Union[(numpy.ndarray, int, numpy.int64)], /):
        "usage.skimage: 5, usage.xarray: 1"


class int16:
    def __init__(_0: Union[(numpy.int64, int, List[int])], /):
        "usage.skimage: 2, usage.xarray: 2, usage.sklearn: 3"


class longlong:
    def __init__(_0: numpy.int64, /):
        "usage.skimage: 1"


class uint16:
    def __init__(_0: Union[(int, numpy.int64)], /):
        "usage.skimage: 2, usage.sklearn: 1"


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
    def __getitem__(
        self,
        _0: Union[
            (
                Literal[
                    (
                        "right",
                        "count",
                        "is_leaf",
                        "value",
                        "bin_threshold",
                        "left",
                        "threshold",
                    )
                ],
                int,
            )
        ],
        /,
    ):
        ""

    def __setitem__(
        self,
        _0: Literal[
            (
                "right",
                "count",
                "is_leaf",
                "depth",
                "feature_idx",
                "value",
                "bin_threshold",
                "missing_go_to_left",
                "left",
                "gain",
                "threshold",
            )
        ],
        _1: Union[(bool, numpy.float64, float, int)],
        /,
    ):
        ""


class errstate:
    def __init__():
        "usage.xarray: 4, usage.sklearn: 13"


class vectorize:
    def __init__(
        pyfunc: Callable, otypes: Union[(list, List[Type[float]], None)] = ...
    ):
        "usage.xarray: 75"


class str_:
    dtype = ...

    def __getitem__(self, _0: slice[(Union[(None, int)], Union[(None, int)], int)], /):
        ""

    def __iter__(self, /):
        ""


class bytes_:
    def __init__(_0: Literal[("z", "asdf", "x")], /):
        "usage.xarray: 3"

    def __getitem__(self, _0: slice[(Union[(None, int)], Union[(None, int)], int)], /):
        ""


class timedelta64:
    def __init__(_0: Union[(datetime.timedelta, int, Literal[("NaT",)])] = ..., /):
        "usage.xarray: 16"

    dtype = ...


class datetime64:
    def __init__(_0: Literal[("NaT",)], _1: Literal[("ns",)], /):
        "usage.xarray: 1"

    dtype = ...


class broadcast:
    def __init__(
        _0: Union[(int, numpy.ndarray, List[int])],
        _1: Union[
            (Literal[("z",)], Literal[("_not_supplied",)], numpy.ndarray, List[int])
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


class memmap:
    __name__ = ...
    __class__ = ...
    shape = ...
    T = ...
    ndim = ...
    flags = ...
    dtype = ...
    size = ...

    def __getitem__(self, _0, /):
        ""

    def mean(self, /, *, axis: int = None):
        "usage.sklearn: 2"

    def __setitem__(
        self,
        _0: Union[
            (Tuple[(slice[(None, None, None)], numpy.ndarray)], int, numpy.int64)
        ],
        _1: numpy.ndarray,
        /,
    ):
        ""
