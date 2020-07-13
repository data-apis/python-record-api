from typing import *


def array(
    data: Union[List[Union[int, float]], numpy.ma.core.MaskedArray, numpy.ndarray],
    mask: Union[List[Union[bool, List[int]]], bool, numpy.ndarray],
):
    """
    usage.pandas: 1
    usage.skimage: 7
    usage.sklearn: 4
    usage.xarray: 1
    """
    ...


def concatenate(
    arrays: Tuple[numpy.ma.core.MaskedArray, numpy.ma.core.MaskedArray], axis: int
):
    """
    usage.xarray: 3
    """
    ...


def getdata(
    a: Union[numpy.ma.core.MaskedArray, numpy.ma.mrecords.MaskedRecords, numpy.ndarray]
):
    """
    usage.pandas: 1
    usage.skimage: 3
    usage.sklearn: 2
    """
    ...


def getmask(a: numpy.ma.core.MaskedArray):
    """
    usage.sklearn: 1
    """
    ...


def getmaskarray(arr: numpy.ma.core.MaskedArray):
    """
    usage.pandas: 7
    usage.skimage: 1
    usage.sklearn: 1
    usage.xarray: 2
    """
    ...


def isMaskedArray(x: Union[numpy.ndarray, numpy.ma.core.MaskedArray]):
    """
    usage.skimage: 18
    """
    ...


def masked_invalid(a: Union[List[float], numpy.ndarray]):
    """
    usage.sklearn: 4
    usage.xarray: 4
    """
    ...


def masked_where(condition: numpy.ndarray, a: numpy.ndarray):
    """
    usage.xarray: 1
    """
    ...


class MaskedArray:

    # usage.xarray: 1
    base: object

    # usage.sklearn: 2
    # usage.xarray: 3
    data: object

    # usage.pandas: 42
    # usage.sklearn: 2
    # usage.xarray: 8
    dtype: object

    # usage.skimage: 2
    fill_value: object

    # usage.skimage: 5
    # usage.sklearn: 2
    # usage.xarray: 6
    mask: object

    # usage.pandas: 6
    # usage.skimage: 8
    # usage.xarray: 3
    ndim: object

    # usage.skimage: 3
    # usage.sklearn: 1
    # usage.xarray: 6
    shape: object

    def __add__(self, _0: numpy.float64, /):
        """
        usage.skimage: 1
        """
        ...

    def __eq__(self, _0: int, /):
        """
        usage.skimage: 1
        """
        ...

    def __getitem__(
        self, _0: Union[Tuple[Union[slice[None, None, None], int], ...], int], /
    ):
        """
        usage.skimage: 6
        usage.sklearn: 21
        usage.xarray: 1
        """
        ...

    def __imul__(self, _0: int, /):
        """
        usage.xarray: 1
        """
        ...

    def __isub__(self, _0: numpy.float64, /):
        """
        usage.skimage: 2
        """
        ...

    def __le__(self, _0: numpy.ndarray, /):
        """
        usage.sklearn: 2
        """
        ...

    def __mul__(self, _0: numpy.float64, /):
        """
        usage.xarray: 1
        """
        ...

    def __radd__(self, _0: numpy.float64, /):
        """
        usage.xarray: 1
        """
        ...

    def __rsub__(self, _0: numpy.ma.core.MaskedArray, /):
        """
        usage.skimage: 2
        usage.sklearn: 1
        """
        ...

    def __rtruediv__(self, _0: numpy.ma.core.MaskedArray, /):
        """
        usage.skimage: 1
        """
        ...

    def __setitem__(
        self,
        _0: Union[
            Tuple[Union[int, numpy.bool_, numpy.ndarray], ...],
            slice[None, None, None],
            numpy.ndarray,
            int,
        ],
        _1: object,
        /,
    ):
        """
        usage.pandas: 18
        usage.skimage: 6
        usage.sklearn: 25
        usage.xarray: 5
        """
        ...

    def __sub__(self, _0: Union[numpy.ma.core.MaskedArray, numpy.float64], /):
        """
        usage.skimage: 4
        usage.sklearn: 1
        """
        ...

    def __truediv__(self, _0: numpy.ma.core.MaskedArray, /):
        """
        usage.skimage: 1
        """
        ...

    def astype(self, _0: numpy.dtype, /):
        """
        usage.pandas: 2
        """
        ...

    def filled(self, /, fill_value: Union[float, int]):
        """
        usage.sklearn: 1
        usage.xarray: 2
        """
        ...

    def harden_mask(self, /):
        """
        usage.pandas: 2
        """
        ...

    def mean(self, /):
        """
        usage.skimage: 1
        usage.sklearn: 1
        """
        ...

    def min(self, /, axis: int):
        """
        usage.sklearn: 2
        """
        ...

    def reshape(self, /, *s: Literal["v", "t"]):
        """
        usage.skimage: 1
        usage.sklearn: 2
        """
        ...

    def soften_mask(self, /):
        """
        usage.pandas: 4
        """
        ...

    def sum(self, /, axis: int):
        """
        usage.sklearn: 1
        """
        ...

    def view(self, /):
        """
        usage.pandas: 4
        """
        ...
