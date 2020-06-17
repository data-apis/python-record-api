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
    _0: Union[(dask.array.core.Array, float, int, numpy.float64, numpy.int64)],
    _1: Union[(numpy.int64, float, int, numpy.float64)] = ...,
    _2: Union[(None, float, int, numpy.float64)] = ...,
    _3: Type[numpy.uint8] = ...,
    /,
    *,
    dtype=...,
):
    "usage.sample_usage: 4, usage.skimage: 223, usage.xarray: 403, usage.sklearn: 151"


def array(
    _0=...,
    /,
    *,
    dtype=...,
    ndmin: int = ...,
    copy: bool = ...,
    order: Union[
        (Literal[("C",)], None, Literal[("F", "C", "K")], Literal[("F",)])
    ] = ...,
):
    "usage.sample_usage: 1, usage.skimage: 1076, usage.xarray: 400, usage.sklearn: 815"


def zeros(
    _0=...,
    _1=...,
    /,
    *,
    dtype=...,
    order: Literal[("F", "f", "C")] = ...,
    shape: Union[(int, Tuple[(int, ...)])] = ...,
):
    "usage.sample_usage: 1, usage.skimage: 787, usage.xarray: 52, usage.sklearn: 350"


def ones(shape, dtype=..., order: Literal[("F", "C")] = ...):
    "usage.sample_usage: 1, usage.skimage: 269, usage.xarray: 59, usage.sklearn: 210"


def linspace(
    start: Union[(numpy.int64, float, int, numpy.float64)],
    stop: Union[(float, int, numpy.float32, numpy.float64, numpy.int64)] = ...,
    num: Union[(numpy.int64, int)] = ...,
):
    "usage.sample_usage: 1, usage.skimage: 70, usage.xarray: 95, usage.sklearn: 41"


def eye(N: int, M: int = ..., dtype: type = ...):
    "usage.sample_usage: 1, usage.skimage: 39, usage.sklearn: 27"


def add(
    _0: Union[
        (
            dask.array.core.Array,
            float,
            numpy.ndarray,
            xarray.core.dataset.Dataset,
            xarray.core.dataarray.DataArray,
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
        (float, int, numpy.ndarray, numpy.float64, xarray.core.dataarray.DataArray)
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
    "usage.sample_usage: 1, usage.skimage: 48, usage.xarray: 46, usage.sklearn: 50"


def absolute(_0=..., /):
    "usage.skimage: 113, usage.sklearn: 154"


def asarray(a, dtype=..., order: Union[(Literal[("C",)], None, Literal[("F",)])] = ...):
    "usage.skimage: 247, usage.xarray: 870, usage.sklearn: 2199"


def sum(
    a,
    axis=...,
    dtype: Union[(None, Type[numpy.float64], Type[float])] = ...,
    keepdims: bool = ...,
):
    "usage.skimage: 125, usage.xarray: 54, usage.sklearn: 208"


def vstack(tup):
    "usage.skimage: 33, usage.sklearn: 69"


def all(
    a: Union[
        (
            pandas.core.series.Series,
            bool,
            numpy.bool_,
            numpy.ndarray,
            numpy.ma.core.MaskedArray,
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
    _1: Union[(dask.array.core.Array, float, int, numpy.ndarray)],
    /,
    *,
    out: numpy.ndarray = ...,
    dtype: Union[(Type[numpy.float32], Type[numpy.float64], type, numpy.dtype)] = ...,
    casting: Literal[("no",)] = ...,
):
    "usage.skimage: 25, usage.xarray: 2, usage.sklearn: 2"


def reshape(a, newshape=...):
    "usage.skimage: 43, usage.xarray: 7, usage.sklearn: 50"


def sqrt(_0=..., /, *, out: numpy.ndarray = ...):
    "usage.skimage: 112, usage.xarray: 4, usage.sklearn: 108"


def moveaxis(
    a: Union[(int, numpy.ndarray, numpy.float64)],
    source: Union[(int, Tuple[(None, ...)], range, numpy.ndarray)],
    destination: Union[(List[int], Tuple[(None, ...)], int, numpy.ndarray)],
):
    "usage.skimage: 6, usage.xarray: 17"


def rollaxis(a: numpy.ndarray, axis: int = ...):
    "usage.skimage: 14, usage.sklearn: 5"


def any(a=...):
    "usage.skimage: 39, usage.xarray: 5, usage.sklearn: 45"


def empty_like(
    _0: Union[
        (
            xarray.core.variable.Variable,
            xarray.core.variable.IndexVariable,
            numpy.ndarray,
            numpy.ma.core.MaskedArray,
        )
    ] = ...,
    /,
    *,
    dtype: Union[(Type[object], numpy.dtype, Type[numpy.float32], type)] = ...,
    order: Literal[("C",)] = ...,
    subok: bool = ...,
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
    _0: Union[(xarray.core.dataarray.DataArray, float, numpy.ndarray, numpy.float64)], /
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
    axis: Union[(None, int, Tuple[(int, int, int)], Tuple[(int, int)])] = ...,
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


def clip(a: Union[(numpy.int64, int, numpy.ndarray, numpy.float64)], a_min, a_max=...):
    "usage.skimage: 61, usage.sklearn: 24"


def power(
    _0: Union[(float, int, numpy.ndarray, numpy.float64)],
    _1: Union[(float, int, numpy.ndarray)],
    /,
):
    "usage.skimage: 11, usage.sklearn: 3"


def log10(
    _0: Union[(xarray.core.dataarray.DataArray, numpy.ndarray, numpy.float64)], /
):
    "usage.skimage: 4, usage.xarray: 2, usage.sklearn: 3"


def load(file: Literal[("/Users/saul/Downloads/scikit-image-0.17.0/skimage/",)]):
    "usage.skimage: 28"


def meshgrid(*xi: Literal[("t", "v")]):
    "usage.skimage: 28, usage.xarray: 6, usage.sklearn: 2"


def dstack(
    tup: Union[
        (
            Tuple[(numpy.ndarray, ...)],
            List[numpy.ndarray],
            Tuple[(numpy.ndarray, numpy.ndarray)],
            List[skimage.feature._hessian_det_appx._memoryviewslice],
        )
    ]
):
    "usage.skimage: 12, usage.sklearn: 4"


def nonzero(a: numpy.ndarray):
    "usage.skimage: 22, usage.xarray: 4, usage.sklearn: 7"


def cbrt(_0: numpy.ndarray, /):
    "usage.skimage: 4"


def hypot(
    _0: Union[(xarray.core.dataarray.DataArray, int, numpy.ndarray, numpy.float64)],
    _1: Union[(xarray.core.dataarray.DataArray, int, numpy.ndarray, numpy.float64)],
    /,
):
    "usage.skimage: 13, usage.xarray: 2"


def arctan2(
    _0: Union[
        (numpy.int64, xarray.core.dataarray.DataArray, numpy.ndarray, numpy.float64)
    ],
    _1: Union[
        (numpy.int64, xarray.core.dataarray.DataArray, numpy.ndarray, numpy.float64)
    ],
    /,
):
    "usage.skimage: 8, usage.xarray: 2"


def where(_0, _1=..., _2=..., /):
    "usage.skimage: 26, usage.xarray: 23, usage.sklearn: 44"


def cos(_0, /):
    "usage.skimage: 48, usage.xarray: 14, usage.sklearn: 11"


def sin(_0, /, *, out=...):
    "usage.skimage: 47, usage.xarray: 21, usage.sklearn: 22"


def ascontiguousarray(
    a: Union[
        (
            List[int],
            numpy.ndarray,
            List[float],
            List[List[int]],
            List[Union[(float, int)]],
        )
    ] = ...
):
    "usage.skimage: 67, usage.sklearn: 21"


def swapaxes(a: numpy.ndarray, axis1: int, axis2: int):
    "usage.skimage: 4, usage.xarray: 8, usage.sklearn: 2"


def ravel(a=...):
    "usage.skimage: 12, usage.xarray: 44, usage.sklearn: 43"


def squeeze(a: Union[(float, int, numpy.ndarray, numpy.float64, List[float])] = ...):
    "usage.skimage: 16, usage.sklearn: 18"


def ones_like(
    a: Union[(xarray.core.variable.Variable, numpy.ndarray, numpy.float64)] = ...
):
    "usage.skimage: 26, usage.xarray: 4, usage.sklearn: 19"


def can_cast(
    _0: Union[(float, numpy.dtype, int, numpy.ndarray)],
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
    shape: Union[(Tuple[(int, int)], Tuple[(int,)], int)] = ...,
):
    "usage.skimage: 129, usage.xarray: 11, usage.sklearn: 131"


def min_scalar_type(_0: Union[(int, numpy.float64, numpy.int64)], /):
    "usage.skimage: 5"


def unique(
    ar, return_index: bool = ..., return_inverse: bool = ..., return_counts: bool = ...
):
    "usage.skimage: 68, usage.xarray: 14, usage.sklearn: 216"


def zeros_like(
    a: Union[(Tuple[(int, int)], Tuple[(int, int, int)], numpy.ndarray)],
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
    _0: Union[(List[int], int, numpy.ndarray, xarray.core.dataarray.DataArray)], /
):
    "usage.skimage: 18, usage.xarray: 2"


def rad2deg(
    _0: Union[(xarray.core.dataarray.DataArray, numpy.ndarray, numpy.float64)], /
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
    q: Union[(List[int], float, int, numpy.ndarray, numpy.float64)] = ...,
):
    "usage.skimage: 11, usage.xarray: 20, usage.sklearn: 9"


def logical_not(
    _0: Union[
        (
            dask.array.core.Array,
            bool,
            numpy.bool_,
            numpy.ndarray,
            xarray.core.dataarray.DataArray,
        )
    ],
    /,
    *,
    out: numpy.ndarray = ...,
):
    "usage.skimage: 14, usage.xarray: 10, usage.sklearn: 8"


def isscalar(element):
    "usage.skimage: 67, usage.xarray: 40, usage.sklearn: 5"


def ceil(_0, /):
    "usage.skimage: 31, usage.xarray: 5, usage.sklearn: 17"


def minimum(
    _0: Union[
        (
            int,
            Tuple[(int, int, int)],
            numpy.ndarray,
            Tuple[(int, int)],
            xarray.core.dataarray.DataArray,
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
        (numpy.memmap, List[List[Union[(int, float)]]], List[List[int]], numpy.ndarray)
    ],
    _1: Union[(numpy.memmap, numpy.matrix, List[Union[(int, float)]], numpy.ndarray)],
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
    "usage.skimage: 21, usage.xarray: 6, usage.sklearn: 6"


def shape(a: Union[(numpy.ma.core.MaskedArray, numpy.ndarray)]):
    "usage.skimage: 1, usage.xarray: 11, usage.sklearn: 15"


def promote_types(_0: numpy.dtype, _1: numpy.dtype, /):
    "usage.skimage: 1"


def bincount(
    _0: Union[(dask.array.core.Array, numpy.ndarray)] = ...,
    /,
    *,
    minlength: int = ...,
    weights: Union[
        (List[int], List[float], numpy.ndarray, None, List[Union[(int, float)]])
    ] = ...,
):
    "usage.skimage: 12, usage.sklearn: 36"


def histogram(
    a: numpy.ndarray = ...,
    bins: Union[
        (
            int,
            numpy.int64,
            Tuple[
                (
                    numpy.float64,
                    numpy.float64,
                    numpy.float64,
                    numpy.float64,
                    numpy.float64,
                )
            ],
            List[Union[(float, int)]],
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


def pad(array: Union[(List[int], List[List[int]], numpy.ndarray)], pad_width=...):
    "usage.skimage: 126, usage.xarray: 44"


def product(*args: Literal[("t", "v")]):
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
    axis: Union[(None, Tuple[(int,)], int, Tuple[(int, int)])] = ...,
    keepdims: bool = ...,
    dtype: Union[(None, Type[numpy.float64], type, Type[float])] = ...,
):
    "usage.skimage: 61, usage.xarray: 32, usage.sklearn: 102"


def log2(
    _0: Union[
        (
            int,
            numpy.ndarray,
            numpy.float64,
            numpy.int64,
            xarray.core.dataarray.DataArray,
        )
    ],
    /,
):
    "usage.skimage: 5, usage.xarray: 2, usage.sklearn: 9"


def allclose(
    a, b, rtol: Union[(float, int)] = ..., equal_nan: bool = ..., atol: float = ...
):
    "usage.skimage: 33, usage.xarray: 22, usage.sklearn: 45"


def argsort(
    a: Union[
        (
            Tuple[
                (
                    numpy.float64,
                    numpy.float64,
                    numpy.float64,
                    numpy.float64,
                    numpy.float64,
                )
            ],
            numpy.matrix,
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
        (dask.array.core.Array, List[numpy.float64], numpy.matrix, numpy.ndarray)
    ] = ...
):
    "usage.skimage: 18, usage.xarray: 11, usage.sklearn: 44"


def logspace(
    start: Union[(float, int, numpy.float64)],
    stop: Union[(float, int, numpy.float64)],
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
    _0: Union[(xarray.core.dataarray.DataArray, float, numpy.ndarray, numpy.float64)], /
):
    "usage.skimage: 2, usage.xarray: 2, usage.sklearn: 10"


def delete(
    arr: numpy.ndarray,
    obj: Union[(Tuple[(Union[(None, int)], ...)], numpy.ndarray)] = ...,
):
    "usage.skimage: 3, usage.sklearn: 2"


def split(ary: numpy.ndarray, indices_or_sections: Union[(int, numpy.ndarray)]):
    "usage.skimage: 1, usage.sklearn: 4"


def atleast_1d(*arys: Literal[("t", "v")]):
    "usage.skimage: 11, usage.xarray: 24, usage.sklearn: 38"


def isclose(
    a: Union[(float, numpy.ndarray, numpy.float64)],
    b: Union[(float, int, numpy.float32, numpy.ndarray, numpy.float64)],
    rtol: float = ...,
    atol: float = ...,
    equal_nan: bool = ...,
):
    "usage.skimage: 3, usage.xarray: 12, usage.sklearn: 5"


def gradient(
    f: Union[(numpy.ndarray, xarray.core.dataarray.DataArray)],
    *varargs: Literal[("t", "v")],
):
    "usage.skimage: 8, usage.xarray: 5"


def argmin(
    a: Union[
        (
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
            List[float],
            numpy.ndarray,
        )
    ] = ...
):
    "usage.skimage: 10, usage.xarray: 5, usage.sklearn: 23"


def arctan(
    _0: Union[(xarray.core.dataarray.DataArray, numpy.ndarray, numpy.float64)], /
):
    "usage.skimage: 3, usage.xarray: 2, usage.sklearn: 2"


def sort(
    a: Union[
        (
            List[int],
            List[numpy.float64],
            numpy.ndarray,
            List[Union[(int, float)]],
            List[float],
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


def atleast_2d(*arys: Literal[("t", "v")]):
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
        (Tuple[(int, int)], generator, Tuple[(Union[(numpy.int64, int)], ...)])
    ] = ...
):
    "usage.skimage: 6, usage.sklearn: 2"


def tri(N: int = ..., M: int = ..., k: int = ...):
    "usage.skimage: 9"


def less(_0, _1: Union[(int, numpy.ndarray, Tuple[(int, ...)])], /):
    "usage.skimage: 3, usage.xarray: 1, usage.sklearn: 5"


def prod(a, axis: int = ..., dtype: Type[numpy.float64] = ...):
    "usage.skimage: 9, usage.xarray: 15, usage.sklearn: 8"


def true_divide(
    _0: numpy.ndarray,
    _1: Union[(numpy.int64, numpy.ndarray)],
    /,
    *,
    out: numpy.ndarray = ...,
):
    "usage.skimage: 2, usage.sklearn: 2"


def unravel_index(
    _0: Union[(numpy.int64, int, numpy.ndarray)], _1: Tuple[(int, ...)], /
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
    _0: Union[(xarray.core.dataarray.DataArray, int, numpy.ndarray, numpy.float64)], /
):
    "usage.skimage: 4, usage.xarray: 3, usage.sklearn: 24"


def subtract(
    _0: Union[(int, numpy.ndarray)],
    _1: Union[(dask.array.core.Array, numpy.ndarray)] = ...,
    /,
    *,
    dtype: numpy.dtype = ...,
):
    "usage.skimage: 11, usage.xarray: 2, usage.sklearn: 1"


def ix_(*args: Literal[("t", "v")]):
    "usage.skimage: 2, usage.xarray: 3, usage.sklearn: 2"


def convolve(a: numpy.ndarray, v: List[float], mode: Literal[("valid",)]):
    "usage.skimage: 1"


def invert(_0: Union[(List[bool], numpy.ndarray)], /):
    "usage.skimage: 7"


def array_equal(
    a1: Union[(List[int], Tuple[(float, float, float)], List[float], numpy.ndarray)], a2
):
    "usage.skimage: 5, usage.xarray: 3, usage.sklearn: 12"


def reciprocal(_0: numpy.ndarray, /, *, out: numpy.ndarray = None):
    "usage.skimage: 1"


def insert(arr: numpy.ndarray, obj: int, values: Union[(int, numpy.ndarray)] = ...):
    "usage.skimage: 3, usage.sklearn: 1"


def full_like(
    a: Union[
        (xarray.core.variable.Variable, numpy.ndarray, xarray.core.dataarray.DataArray)
    ],
    fill_value: Union[(float, int, bool)] = ...,
):
    "usage.skimage: 1, usage.xarray: 10, usage.sklearn: 3"


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


def einsum(*operands: Literal[("t", "v")]):
    "usage.skimage: 1, usage.xarray: 80, usage.sklearn: 10"


def nan_to_num(x: Union[(List[numpy.float64], numpy.ndarray)]):
    "usage.skimage: 1, usage.sklearn: 2"


def frombuffer(
    _0: Union[(bytes, array.array, numpy.ndarray)] = ...,
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
        (dask.array.core.Array, Type[numpy.float32], numpy.dtype, numpy.ndarray)
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


def cumprod(a: Union[(numpy.ndarray, Tuple[(int, ...)])] = ...):
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
            List[Literal[("three", "two", "one")]],
            List[int],
            List[Literal[("two", "one")]],
            numpy.ndarray,
        )
    ] = ...,
    indices: Union[(List[int], int, numpy.ndarray)] = ...,
):
    "usage.skimage: 1, usage.xarray: 11, usage.sklearn: 8"


def lexsort(
    _0: Tuple[(Union[(numpy.ndarray, xarray.core.dataarray.DataArray)], ...)], /
):
    "usage.skimage: 1, usage.xarray: 2"


def fmax(
    _0: Union[(numpy.ndarray, xarray.core.dataarray.DataArray)],
    _1: Union[(xarray.core.dataarray.DataArray, float, numpy.ndarray, numpy.float64)],
    /,
):
    "usage.skimage: 3, usage.xarray: 2"


def fix(x: Union[(xarray.core.dataarray.DataArray, float, numpy.float64)]):
    "usage.skimage: 2, usage.xarray: 1"


def tensordot(
    a: numpy.ndarray,
    b: Union[(range, numpy.ndarray)],
    axes: Union[(Tuple[(int, int)], List[int], Tuple[(List[int], List[int])])],
):
    "usage.skimage: 1, usage.xarray: 5"


def atleast_3d(*arys: Literal[("t", "v")]):
    "usage.skimage: 11, usage.sklearn: 6"


def iscomplexobj(x: numpy.ndarray):
    "usage.skimage: 4, usage.sklearn: 1"


def conjugate(_0: Union[(numpy.ndarray, xarray.core.dataarray.DataArray)], /):
    "usage.skimage: 2, usage.xarray: 2, usage.sklearn: 1"


def angle(z: Union[(numpy.ndarray, xarray.core.dataarray.DataArray)]):
    "usage.skimage: 3, usage.xarray: 2"


def require(
    a: numpy.ndarray,
    requirements: Union[(Literal[("W",)], List[Literal[("C",)]])] = ...,
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


def alltrue(*args: Literal[("t", "v")]):
    "usage.skimage: 2"


def may_share_memory(
    _0: Union[
        (
            scipy.sparse.csr.csr_matrix,
            scipy.sparse.lil.lil_matrix,
            scipy.sparse.csc.csc_matrix,
            numpy.ndarray,
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


def broadcast_arrays(*args: Literal[("t", "v")]):
    "usage.xarray: 3"


def broadcast_to(
    array: Union[(float, numpy.ndarray)], shape: Tuple[(Union[(int, None)], ...)]
):
    "usage.xarray: 25"


def nanmean(
    a: numpy.ndarray,
    axis: Union[
        (None, Tuple[(int,)], int, Tuple[(None, ...)], Tuple[(int, int)])
    ] = ...,
    dtype: Union[
        (
            Type[float],
            Type[numpy.float64],
            None,
            Type[numpy.float32],
            Type[numpy.float16],
        )
    ] = ...,
):
    "usage.xarray: 21, usage.sklearn: 3"


def nanstd(
    a: numpy.ndarray, axis: Union[(None, int)], dtype: None = ..., ddof: int = ...
):
    "usage.xarray: 3, usage.sklearn: 1"


def nanargmax(a: numpy.ndarray, axis: Union[(int, None)]):
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
    a: Union[(float, int, numpy.ndarray, numpy.float64, numpy.int64)],
    repeats: Union[(numpy.int64, int, numpy.ndarray)] = ...,
):
    "usage.xarray: 4, usage.sklearn: 33"


def isin(
    element: Union[(dask.array.core.Array, numpy.ndarray)],
    test_elements: Union[(List[int], numpy.ndarray)],
):
    "usage.xarray: 5"


def nansum(a: Union[(numpy.ma.core.MaskedArray, numpy.ndarray)] = ...):
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
    axis: Union[(None, Tuple[(None, ...)], int)] = ...,
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
    axis: Union[(int, Tuple[(int, int)], None)],
    dtype: None,
    out: None,
):
    "usage.xarray: 9"


def greater(_0: numpy.ndarray, _1: numpy.ndarray, /):
    "usage.xarray: 1"


def frexp(
    _0: Union[
        (
            xarray.core.dataset.Dataset,
            numpy.ndarray,
            xarray.core.dataarray.DataArray,
            xarray.core.variable.Variable,
            int,
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


def fabs(_0: Union[(numpy.float64, numpy.ndarray, xarray.core.dataarray.DataArray)], /):
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
    _0: Union[(float, int, numpy.ndarray, xarray.core.dataarray.DataArray)],
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
    _1: Union[(int, numpy.ndarray, xarray.core.dataarray.DataArray)],
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
            Tuple[(int, int)],
            Tuple[(None, ...)],
            Tuple[(int,)],
            Tuple[(int, int, int)],
            numpy.ndarray,
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


def psi(_0: Union[(int, numpy.ndarray, numpy.int64, numpy.float64)], /):
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


def isposinf(x: Union[(int, float)]):
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
        "usage.sample_usage: 2, usage.skimage: 168, usage.xarray: 190, usage.sklearn: 163"

    @classmethod
    def astype(_0: numpy.ndarray, _1, /):
        "usage.sample_usage: 1, usage.skimage: 555, usage.xarray: 75, usage.sklearn: 149"

    @classmethod
    def copy(_0: Union[(numpy.memmap, numpy.ndarray)] = ..., /):
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
    def fill(_0: numpy.ndarray, _1: Union[(float, int, bool, numpy.float64)], /):
        "usage.skimage: 5, usage.sklearn: 26"

    @classmethod
    def flatten(_0: numpy.ndarray, /):
        "usage.skimage: 16, usage.xarray: 5, usage.sklearn: 7"

    @classmethod
    def ravel(_0: numpy.ndarray = ..., /):
        "usage.skimage: 207, usage.xarray: 40, usage.sklearn: 142"

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
    def tolist(_0: Union[(numpy.memmap, numpy.ndarray)], /):
        "usage.skimage: 1, usage.xarray: 17, usage.sklearn: 23"

    @classmethod
    def dot(_0: numpy.ndarray, _1: numpy.ndarray, /):
        "usage.skimage: 1, usage.sklearn: 50"

    @classmethod
    def conj(_0: numpy.ndarray, /):
        "usage.skimage: 4"

    @classmethod
    def __ne__(_0: Type[numpy.ndarray], /):
        ""

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
    def __rmod__(_0: Literal[("Expected sequence or array-like, got %s",)], /):
        ""

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

    def __pos__(self, /):
        ""

    def __neg__(self, /):
        ""

    def __invert__(self, /):
        ""

    def __bool__(self, /):
        ""

    def __iter__(self, /):
        ""

    def __getitem__(self, _0, /):
        ""

    def __pow__(self, _0: Union[(float, int, numpy.ndarray, numpy.float64)], /):
        ""

    def __rpow__(self, _0: Union[(float, int, numpy.ndarray)], /):
        ""

    def __mul__(self, _0, /):
        ""

    def __rmul__(self, _0, /):
        ""

    def __matmul__(
        self,
        _0: Union[
            (
                scipy.sparse.csr.csr_matrix,
                scipy.sparse.csc.csc_matrix,
                numpy.matrix,
                numpy.ndarray,
            )
        ],
        /,
    ):
        ""

    def __rmatmul__(self, _0, /):
        ""

    def __floordiv__(
        self, _0: Union[(List[int], int, numpy.ndarray, numpy.float64, List[float])], /
    ):
        ""

    def __rfloordiv__(self, _0: Union[(int, numpy.ndarray)], /):
        ""

    def __mod__(self, _0: Union[(float, int, numpy.ndarray)], /):
        ""

    def __rmod__(
        self,
        _0: Union[
            (
                Literal[("unable to convert object into a variable without a",)],
                int,
                Literal[
                    (
                        "Deleting features without observed values: %s",
                        "Features %s are constant.",
                    )
                ],
                numpy.ndarray,
            )
        ],
        /,
    ):
        ""

    def __add__(self, _0, /):
        ""

    def __radd__(self, _0, /):
        ""

    def __sub__(self, _0, /):
        ""

    def __rsub__(self, _0, /):
        ""

    def __lshift__(self, _0: int, /):
        ""

    def __rlshift__(self, _0: int, /):
        ""

    def __rshift__(self, _0: int, /):
        ""

    def __rrshift__(self, _0: int, /):
        ""

    def __and__(
        self, _0: Union[(dask.array.core.Array, int, numpy.bool_, numpy.ndarray)], /
    ):
        ""

    def __rand__(
        self, _0: Union[(dask.array.core.Array, int, numpy.bool_, numpy.ndarray)], /
    ):
        ""

    def __or__(
        self, _0: Union[(dask.array.core.Array, int, numpy.bool_, numpy.ndarray)], /
    ):
        ""

    def __ror__(
        self,
        _0: Union[(dask.array.core.Array, int, bool, numpy.bool_, numpy.ndarray)],
        /,
    ):
        ""

    def __ipow__(self, _0: Union[(float, int)], /):
        ""

    def __imul__(self, _0, /):
        ""

    def __ifloordiv__(self, _0: int, /):
        ""

    def __imod__(self, _0: int, /):
        ""

    def __iadd__(self, _0, /):
        ""

    def __isub__(self, _0, /):
        ""

    def __ilshift__(self, _0: int, /):
        ""

    def __irshift__(self, _0: int, /):
        ""

    def __iand__(self, _0: Union[(int, numpy.ndarray)], /):
        ""

    def __ior__(self, _0: Union[(int, numpy.ndarray)], /):
        ""

    def __setitem__(self, _0, _1, /):
        ""

    def __eq__(self, _0, /):
        ""

    def __le__(
        self, _0: Union[(float, int, numpy.ndarray, numpy.float64, numpy.int64)], /
    ):
        ""

    def sort(self, /, *, axis: int = ..., order: Literal[("accumulator",)] = ...):
        "usage.sample_usage: 1, usage.skimage: 9, usage.sklearn: 1"

    def __gt__(self, _0, /):
        ""

    def __contains__(self, _0: Union[(Tuple[(int, int)], numpy.int64, int)], /):
        ""

    def mean(
        self,
        /,
        *,
        axis: Union[(int, Tuple[(int, int, int)])] = ...,
        keepdims: bool = ...,
    ):
        "usage.skimage: 28, usage.xarray: 5, usage.sklearn: 48"

    def __truediv__(self, _0, /):
        ""

    def __rtruediv__(
        self, _0: Union[(float, int, numpy.ndarray, numpy.float64, numpy.complex128)], /
    ):
        ""

    def __itruediv__(self, _0, /):
        ""

    def __ne__(self, _0, /):
        ""

    def __ge__(self, _0, /):
        ""

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

    def __lt__(self, _0: Union[(int, numpy.ndarray, numpy.float64)], /):
        ""

    def argmax(self, /, *, axis: int = ...):
        "usage.skimage: 1, usage.sklearn: 9"

    def astype(
        self=...,
        /,
        *,
        copy: bool = ...,
        dtype: Union[
            (
                Type[bool],
                Type[numpy.float32],
                Literal[("i1",)],
                numpy.dtype,
                Literal[(">u4",)],
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
        dtype: Union[(Literal[("|S512", "|S16", "|S80")], Type[numpy.uint8])] = None,
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
        _0: Union[(int, Tuple[(int, int, int, int)], Tuple[(int, ...)])],
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
        _0: Union[(int, numpy.ndarray, List[numpy.int64])],
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
    type = ...
    kind = ...
    itemsize = ...
    name = ...
    char = ...
    isnative = ...
    metadata = ...

    def __eq__(self, _0, /):
        ""

    def __ne__(self, _0, /):
        ""

    def __rmod__(
        self,
        _0: Literal[
            (
                "            <xarray.Dataset>\n            Dimension",
                "Only bool or integer image types are supported. Go",
            )
        ],
        /,
    ):
        ""


class ufunc:
    @classmethod
    def reduce(
        _0: Callable,
        _1: Union[
            (
                List[numpy.ndarray],
                Tuple[(int,)],
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
    @classmethod
    def __ne__(_0: numpy.dtype, /):
        ""

    ndim = ...
    shape = ...
    dtype = ...

    def __le__(self, _0, /):
        ""

    def __rmul__(self, _0, /):
        ""

    def __gt__(self, _0, /):
        ""

    def __rsub__(self, _0, /):
        ""

    def __rtruediv__(self, _0, /):
        ""

    def __iadd__(self, _0, /):
        ""

    def __truediv__(self, _0, /):
        ""

    def __radd__(self, _0, /):
        ""

    def __add__(self, _0, /):
        ""

    def __sub__(self, _0, /):
        ""

    def __mul__(self, _0, /):
        ""

    def __getitem__(self, _0: Tuple[(Union[(ellipsis, None)], None)], /):
        ""

    def __neg__(self, /):
        ""

    def __ge__(
        self, _0: Union[(float, int, numpy.float32, numpy.ndarray, numpy.float64)], /
    ):
        ""

    def __pow__(self, _0: Union[(float, int, numpy.float64)], /):
        ""

    def __lt__(self, _0, /):
        ""

    def __imod__(self, _0: float, /):
        ""

    def __eq__(self, _0, /):
        ""

    def __mod__(self, _0: Union[(float, int)], /):
        ""

    def __itruediv__(self, _0, /):
        ""

    def __rpow__(self, _0: Union[(float, int, numpy.ndarray, numpy.float64)], /):
        ""

    def __ne__(
        self,
        _0: Union[
            (float, int, numpy.float64, numpy.int64, _pytest.python_api.ApproxScalar)
        ],
        /,
    ):
        ""

    def __isub__(self, _0: Union[(int, numpy.ndarray, numpy.float64)], /):
        ""

    def __imul__(self, _0: Union[(numpy.int64, float, int, numpy.float64)], /):
        ""

    def __rfloordiv__(self, _0: numpy.ndarray, /):
        ""

    def __rmod__(self, _0: Literal[("%.16g",)], /):
        ""


class int64:
    ndim = ...
    shape = ...
    dtype = ...

    def __rmul__(self, _0, /):
        ""

    def __add__(self, _0, /):
        ""

    def __ne__(self, _0: Union[(numpy.int64, int, numpy.ndarray, numpy.float64)], /):
        ""

    def __ge__(self, _0, /):
        ""

    def __rsub__(
        self, _0: Union[(float, int, numpy.ndarray, numpy.float64, numpy.int64)], /
    ):
        ""

    def __eq__(self, _0, /):
        ""

    def __rtruediv__(
        self, _0: Union[(float, int, numpy.ndarray, numpy.float64, numpy.int64)], /
    ):
        ""

    def __sub__(self, _0: Union[(numpy.int64, float, int, numpy.float64)], /):
        ""

    def __floordiv__(self, _0: int, /):
        ""

    def __isub__(self, _0: Union[(numpy.int64, int)], /):
        ""

    def __le__(self, _0: Union[(numpy.int64, float, int, numpy.ndarray)], /):
        ""

    def __iadd__(self, _0: Union[(numpy.int64, int, numpy.float64)], /):
        ""

    def __gt__(self, _0: Union[(numpy.int64, float, int)], /):
        ""

    def __rfloordiv__(self, _0: Union[(float, int)], /):
        ""

    def __radd__(self, _0, /):
        ""

    def __truediv__(self, _0: Union[(numpy.int64, float, int, numpy.float64)], /):
        ""

    def __pow__(self, _0: int, /):
        ""

    def __mul__(
        self, _0: Union[(float, int, numpy.ndarray, numpy.float64, numpy.int64)], /
    ):
        ""

    def __lt__(
        self,
        _0: Union[(numpy.uint8, int, numpy.ndarray, numpy.float64, numpy.int64)],
        /,
    ):
        ""

    def __itruediv__(self, _0: numpy.float64, /):
        ""

    def __mod__(self, _0: int, /):
        ""

    def __neg__(self, /):
        ""

    def __imod__(self, _0: int, /):
        ""

    def __getitem__(self, _0: Tuple[(None, ellipsis)], /):
        ""

    def __rmod__(
        self,
        _0: Literal[
            (
                "%d",
                "[MiniBatchKMeans] Reassigning %i cluster centers.",
                "This solver needs samples of at least 2 classes in",
                "not %s",
                "Fitting estimator with %d features.",
            )
        ],
        /,
    ):
        ""


class generic:
    @classmethod
    def astype(
        _0,
        _1: Union[
            (
                Literal[("timedelta64[ns]",)],
                Type[numpy.float64],
                Type[numpy.int64],
                Type[float],
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
        int_type: Union[(Type[numpy.uint32], Literal[("i",)], numpy.dtype, type)]
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

    def __getitem__(self, _0: Literal[("F_CONTIGUOUS", "C_CONTIGUOUS")], /):
        ""


class bool_:
    @classmethod
    def __ne__(_0: numpy.dtype, /):
        ""

    def __invert__(self, /):
        ""

    def __bool__(self, /):
        ""

    def __rpow__(self, _0: int, /):
        ""

    def __and__(self, _0: Union[(numpy.bool_, numpy.ndarray)], /):
        ""

    def __rand__(
        self, _0: Union[(dask.array.core.Array, numpy.bool_, numpy.ndarray)], /
    ):
        ""

    def __or__(self, _0: Union[(numpy.bool_, numpy.ndarray)], /):
        ""

    def __ror__(self, _0: Union[(bool, numpy.bool_, numpy.ndarray)], /):
        ""

    def all(self, /):
        "usage.xarray: 4"

    def __eq__(self, _0: Union[(bool, numpy.ndarray)], /):
        ""

    def __gt__(self, _0: float, /):
        ""


class flatiter:
    def __eq__(self, _0: Union[(numpy.int64, int, numpy.float64)], /):
        ""

    def __iter__(self, /):
        ""

    def __getitem__(
        self,
        _0: Union[
            (
                numpy.int64,
                slice[(None, None, int)],
                int,
                slice[(Union[(int, None)], Union[(int, None)], None)],
            )
        ],
        /,
    ):
        ""

    def __setitem__(
        self,
        _0: Union[(List[int], slice[(Union[(None, int)], None, int)], numpy.ndarray)],
        _1: Union[(float, int, numpy.ndarray)],
        /,
    ):
        ""


class uint8:
    @classmethod
    def __ne__(_0: numpy.dtype, /):
        ""

    def __eq__(self, _0: Union[(numpy.uint8, int, numpy.ndarray, numpy.int64)], /):
        ""

    def __rsub__(self, _0: Union[(int, numpy.float64, numpy.uint8, numpy.ndarray)], /):
        ""

    def __rmul__(self, _0: float, /):
        ""

    def __lt__(self, _0: Union[(int, numpy.float64, numpy.ndarray)], /):
        ""

    def __ge__(self, _0: Union[(int, numpy.float64)], /):
        ""

    def __truediv__(self, _0: int, /):
        ""

    def __radd__(self, _0: Union[(numpy.ndarray, numpy.float64, numpy.uint8)], /):
        ""

    def __add__(self, _0: Union[(int, numpy.uint8)], /):
        ""

    def __sub__(self, _0: Union[(int, numpy.uint8)], /):
        ""

    def __le__(self, _0: Union[(numpy.int64, int, numpy.ndarray)], /):
        ""

    def __ne__(self, _0: numpy.uint8, /):
        ""

    def __gt__(self, _0: Union[(numpy.int64, int)], /):
        ""

    def __rtruediv__(self, _0: numpy.float64, /):
        ""

    def __pow__(self, _0: int, /):
        ""

    def __iadd__(self, _0: int, /):
        ""


class uint64:
    def __eq__(self, _0: Union[(numpy.int64, int, numpy.uint64, numpy.ndarray)], /):
        ""

    def __rtruediv__(self, _0: float, /):
        ""

    def __ge__(self, _0: int, /):
        ""

    def __le__(self, _0: int, /):
        ""

    def __ne__(self, _0: Union[(float, numpy.uint64)], /):
        ""

    def __lt__(self, _0: Union[(int, numpy.uint64)], /):
        ""

    def __truediv__(self, _0: int, /):
        ""

    def __rsub__(self, _0: numpy.ndarray, /):
        ""

    def __rmul__(self, _0: Union[(float, int)], /):
        ""

    def __gt__(self, _0: Union[(numpy.float64, numpy.uint64)], /):
        ""


class ndindex:
    def __init__(*shape: Literal[("t", "v")]):
        "usage.skimage: 1"

    def __iter__(self, /):
        ""


class uint32:
    def __add__(self, _0: int, /):
        ""

    def __ge__(self, _0: int, /):
        ""

    def __le__(self, _0: int, /):
        ""

    def __eq__(self, _0: Union[(numpy.int64, int)], /):
        ""

    def __sub__(self, _0: int, /):
        ""

    def __gt__(self, _0: numpy.uint32, /):
        ""

    def __lt__(self, _0: numpy.uint32, /):
        ""


class uint16:
    def __ge__(self, _0: int, /):
        ""

    def __add__(self, _0: int, /):
        ""

    def __eq__(self, _0: Union[(int, numpy.int64)], /):
        ""

    def __le__(self, _0: int, /):
        ""

    def __ne__(self, _0: numpy.uint16, /):
        ""


class int16:
    def __ge__(self, _0: int, /):
        ""

    def __le__(self, _0: int, /):
        ""

    def __sub__(self, _0: numpy.int16, /):
        ""

    def __rsub__(self, _0: numpy.int16, /):
        ""

    def __rtruediv__(self, _0: numpy.float64, /):
        ""

    def __pow__(self, _0: int, /):
        ""

    def __eq__(self, _0: Union[(numpy.int64, int, numpy.ndarray)], /):
        ""

    def __ne__(self, _0: int, /):
        ""


class int32:
    @classmethod
    def __ne__(_0: numpy.dtype, /):
        ""

    dtype = ...

    def __ge__(self, _0: Union[(float, int)], /):
        ""

    def __le__(self, _0: int, /):
        ""

    def __eq__(self, _0: Union[(numpy.int64, numpy.int32, int, numpy.ndarray)], /):
        ""

    def __rmul__(self, _0: numpy.ndarray, /):
        ""

    def __add__(self, _0: Union[(numpy.int64, bool)], /):
        ""

    def __rmod__(self, _0: Literal[("%d",)], /):
        ""

    def __sub__(self, _0: int, /):
        ""


class float32:
    @classmethod
    def __ne__(_0: numpy.dtype, /):
        ""

    dtype = ...

    def __sub__(self, _0: Union[(numpy.float64, numpy.float32, numpy.ndarray)], /):
        ""

    def __gt__(self, _0: Union[(float, int, numpy.float64)], /):
        ""

    def __add__(self, _0: Union[(int, numpy.float64)], /):
        ""

    def __ge__(self, _0: Union[(float, int, numpy.float32)], /):
        ""

    def __lt__(self, _0: Union[(float, numpy.ndarray, numpy.float64)], /):
        ""

    def __truediv__(self, _0: Union[(float, numpy.float32, numpy.float64)], /):
        ""

    def __rmul__(self, _0: Union[(numpy.float32, float, int, numpy.ndarray)], /):
        ""

    def __mul__(self, _0: Union[(float, int, numpy.float32, numpy.ndarray)], /):
        ""

    def __le__(self, _0: Union[(float, int, numpy.float32, numpy.float64)], /):
        ""

    def __eq__(self, _0: Union[(float, int, numpy.float32, numpy.ndarray)], /):
        ""

    def __rtruediv__(
        self, _0: Union[(float, int, numpy.float32, numpy.ndarray, numpy.float64)], /
    ):
        ""

    def __rsub__(
        self, _0: Union[(float, int, numpy.float32, numpy.ndarray, numpy.float64)], /
    ):
        ""

    def __pow__(self, _0: int, /):
        ""

    def __iadd__(self, _0: Union[(int, numpy.float32)], /):
        ""

    def __itruediv__(self, _0: int, /):
        ""

    def __radd__(self, _0: Union[(int, numpy.ndarray, float, numpy.float64)], /):
        ""

    def __ne__(self, _0: int, /):
        ""


class matrix:
    A = ...
    shape = ...

    def __rmatmul__(self, _0: numpy.ndarray, /):
        ""

    def __neg__(self, /):
        ""

    def __matmul__(self, _0: numpy.ndarray, /):
        ""

    def __rtruediv__(self, _0: Union[(numpy.ndarray, float)], /):
        ""

    def max(self, /):
        "usage.sklearn: 3"

    def __getitem__(self, _0: Tuple[(int, slice[(None, None, None)])], /):
        ""

    def __sub__(self, _0: numpy.ndarray, /):
        ""

    def __truediv__(self, _0: float, /):
        ""

    def __eq__(self, _0: float, /):
        ""


class int8:
    def __lt__(self, _0: int, /):
        ""

    def __le__(self, _0: int, /):
        ""

    def __eq__(self, _0: Union[(numpy.int64, int, numpy.ndarray)], /):
        ""

    def __gt__(self, _0: int, /):
        ""


class complex128:
    imag = ...
    real = ...

    def __eq__(self, _0: numpy.ndarray, /):
        ""

    def __mul__(self, _0: numpy.complex128, /):
        ""

    def __rmul__(self, _0: numpy.complex128, /):
        ""

    def __truediv__(
        self, _0: Union[(numpy.ndarray, numpy.float64, numpy.complex128)], /
    ):
        ""

    def __rsub__(self, _0: float, /):
        ""

    def __itruediv__(self, _0: numpy.float64, /):
        ""

    def __rtruediv__(self, _0: numpy.complex128, /):
        ""


class float16:
    def __sub__(self, _0: numpy.float16, /):
        ""

    def __rsub__(self, _0: Union[(numpy.ndarray, numpy.float16)], /):
        ""

    def __pow__(self, _0: int, /):
        ""

    def __rmul__(self, _0: Union[(float, numpy.ndarray)], /):
        ""

    def __eq__(self, _0: int, /):
        ""

    def __gt__(self, _0: numpy.float64, /):
        ""


class nditer:
    multi_index = ...

    def __iter__(self, /):
        ""


class longlong:
    def __le__(self, _0: int, /):
        ""

    def __eq__(self, _0: Union[(numpy.int64, int)], /):
        ""

    def __rtruediv__(self, _0: Union[(numpy.ndarray, numpy.float64)], /):
        ""

    def __gt__(self, _0: int, /):
        ""

    def __add__(self, _0: int, /):
        ""

    def __ge__(self, _0: int, /):
        ""

    def __mul__(self, _0: float, /):
        ""


class ulonglong:
    def __le__(self, _0: int, /):
        ""

    def __eq__(self, _0: Union[(int, numpy.int64)], /):
        ""


class void:
    def __getitem__(
        self,
        _0: Union[
            (
                int,
                Literal[
                    (
                        "count",
                        "is_leaf",
                        "right",
                        "bin_threshold",
                        "left",
                        "value",
                        "threshold",
                    )
                ],
            )
        ],
        /,
    ):
        ""

    def __setitem__(
        self,
        _0: Literal[
            (
                "count",
                "gain",
                "depth",
                "is_leaf",
                "right",
                "bin_threshold",
                "left",
                "feature_idx",
                "value",
                "missing_go_to_left",
                "threshold",
            )
        ],
        _1: Union[(int, float, bool, numpy.float64)],
        /,
    ):
        ""


class errstate:
    def __init__():
        "usage.xarray: 4, usage.sklearn: 13"


class vectorize:
    def __init__(
        pyfunc: Callable, otypes: Union[(list, None, List[Type[float]])] = ...
    ):
        "usage.xarray: 75"


class str_:
    dtype = ...

    def __getitem__(self, _0: slice[(Union[(int, None)], Union[(int, None)], int)], /):
        ""

    def __iadd__(self, _0, /):
        ""

    def __radd__(
        self,
        _0: Literal[
            (
                "",
                "short",
                "ev",
                "evenlongerthantha",
                "a ",
                "evenlong",
                "a bit ",
                "sh",
                "a bit longe",
                "shor",
                "evenlo",
            )
        ],
        /,
    ):
        ""

    def __contains__(self, _0: Literal[(" ",)], /):
        ""

    def __ne__(
        self,
        _0: Union[
            (
                Literal[("space", "z")],
                numpy.ndarray,
                Literal[("bar", "baz", "foo", "foobar", "setosa")],
            )
        ],
        /,
    ):
        ""

    def __eq__(
        self,
        _0: Union[
            (
                numpy.ndarray,
                xarray.core.variable.Variable,
                Literal[("b", "a", "c")],
                Literal[("ZN", "CRIM")],
                xarray.core.dataarray.DataArray,
            )
        ],
        /,
    ):
        ""

    def __iter__(self, /):
        ""


class bytes_:
    def __init__(_0: Literal[("asdf",)], /):
        "usage.xarray: 1"

    def __getitem__(self, _0: slice[(Union[(int, None)], Union[(int, None)], int)], /):
        ""

    def __iadd__(self, _0: Union[(bytes, numpy.bytes_)], /):
        ""

    def __radd__(self, _0: bytes, /):
        ""

    def __eq__(self, _0: numpy.ndarray, /):
        ""


class timedelta64:
    def __init__(_0: datetime.timedelta, _1: Literal[("ns",)], /):
        "usage.xarray: 1"

    dtype = ...

    def __rtruediv__(
        self,
        _0: Union[
            (
                numpy.timedelta64,
                numpy.ndarray,
                pandas.core.indexes.timedeltas.TimedeltaIndex,
            )
        ],
        /,
    ):
        ""

    def __truediv__(self, _0: numpy.timedelta64, /):
        ""

    def __rmul__(self, _0: Union[(float, numpy.ndarray)], /):
        ""

    def __add__(self, _0: numpy.ndarray, /):
        ""

    def __ne__(self, _0: numpy.ndarray, /):
        ""

    def __rsub__(self, _0: pandas.core.indexes.datetimes.DatetimeIndex, /):
        ""

    def __eq__(self, _0: numpy.timedelta64, /):
        ""


class datetime64:
    dtype = ...

    def __add__(self, _0: numpy.ndarray, /):
        ""

    def __rsub__(self, _0: numpy.ndarray, /):
        ""

    def __eq__(
        self,
        _0: Union[
            (
                xarray.core.variable.Variable,
                xarray.core.dataarray.DataArray,
                numpy.datetime64,
                numpy.ndarray,
            )
        ],
        /,
    ):
        ""


class broadcast:
    def __init__(
        _0: Union[(int, dask.array.core.Array, List[int], numpy.ndarray)],
        _1: Union[
            (List[int], numpy.ndarray, Literal[("z",)], Literal[("_not_supplied",)])
        ] = ...,
        _2: numpy.ndarray = ...,
        /,
    ):
        "usage.xarray: 14"

    shape = ...


class object_:
    def __init__(_0: bytes, /):
        "usage.xarray: 1"


class ndenumerate:
    def __iter__(self, /):
        ""


class memmap:
    __name__ = ...

    @classmethod
    def __rmod__(_0: Literal[("Expected sequence or array-like, got %s",)], /):
        ""

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

    def __isub__(self, _0: Union[(numpy.ndarray, numpy.float64)], /):
        ""

    def __pow__(self, _0: int, /):
        ""

    def __setitem__(
        self,
        _0: Union[
            (int, numpy.int64, Tuple[(slice[(None, None, None)], numpy.ndarray)])
        ],
        _1: numpy.ndarray,
        /,
    ):
        ""
