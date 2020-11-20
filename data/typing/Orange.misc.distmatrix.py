from typing import *


class DistMatrix:
    @overload
    def __array_wrap__(
        self,
        _0: Orange.misc.distmatrix.DistMatrix,
        _1: Tuple[numpy.ufunc, Tuple[Orange.misc.distmatrix.DistMatrix], int],
        /,
    ):
        """
        usage.orange3: 2
        """
        ...

    @overload
    def __array_wrap__(
        self,
        _0: Orange.misc.distmatrix.DistMatrix,
        _1: Tuple[
            numpy.ufunc, Tuple[Orange.misc.distmatrix.DistMatrix, numpy.ndarray], int
        ],
        /,
    ):
        """
        usage.orange3: 2
        """
        ...

    @overload
    def __array_wrap__(
        self,
        _0: Orange.misc.distmatrix.DistMatrix,
        _1: Tuple[numpy.ufunc, Tuple[Orange.misc.distmatrix.DistMatrix, float], int],
        /,
    ):
        """
        usage.orange3: 2
        """
        ...

    @overload
    def __array_wrap__(
        self,
        _0: Orange.misc.distmatrix.DistMatrix,
        _1: Tuple[numpy.ufunc, Tuple[Orange.misc.distmatrix.DistMatrix], int],
        /,
    ):
        """
        usage.orange3: 2
        """
        ...

    @overload
    def __array_wrap__(
        self,
        _0: Orange.misc.distmatrix.DistMatrix,
        _1: Tuple[
            numpy.ufunc, Tuple[Orange.misc.distmatrix.DistMatrix, numpy.ndarray], int
        ],
        /,
    ):
        """
        usage.orange3: 2
        """
        ...

    @overload
    def __array_wrap__(
        self,
        _0: Orange.misc.distmatrix.DistMatrix,
        _1: Tuple[numpy.ufunc, Tuple[Orange.misc.distmatrix.DistMatrix], int],
        /,
    ):
        """
        usage.orange3: 2
        """
        ...

    @overload
    def __array_wrap__(
        self,
        _0: Orange.misc.distmatrix.DistMatrix,
        _1: Tuple[numpy.ufunc, Tuple[Orange.misc.distmatrix.DistMatrix, float], int],
        /,
    ):
        """
        usage.orange3: 1
        """
        ...

    @overload
    def __array_wrap__(
        self,
        _0: Orange.misc.distmatrix.DistMatrix,
        _1: Tuple[
            numpy.ufunc,
            Tuple[Orange.misc.distmatrix.DistMatrix, Orange.misc.distmatrix.DistMatrix],
            int,
        ],
        /,
    ):
        """
        usage.orange3: 3
        """
        ...

    @overload
    def __array_wrap__(
        self,
        _0: Orange.misc.distmatrix.DistMatrix,
        _1: Tuple[
            numpy.ufunc,
            Tuple[
                Orange.misc.distmatrix.DistMatrix,
                Orange.misc.distmatrix.DistMatrix,
                Orange.misc.distmatrix.DistMatrix,
            ],
            int,
        ],
        /,
    ):
        """
        usage.orange3: 1
        """
        ...

    @overload
    def __array_wrap__(
        self,
        _0: Orange.misc.distmatrix.DistMatrix,
        _1: Tuple[numpy.ufunc, Tuple[Orange.misc.distmatrix.DistMatrix], int],
        /,
    ):
        """
        usage.orange3: 1
        """
        ...

    @overload
    def __array_wrap__(
        self,
        _0: Orange.misc.distmatrix.DistMatrix,
        _1: Tuple[
            numpy.ufunc,
            Tuple[Orange.misc.distmatrix.DistMatrix, Orange.misc.distmatrix.DistMatrix],
            int,
        ],
        /,
    ):
        """
        usage.orange3: 2
        """
        ...

    @overload
    def __array_wrap__(
        self,
        _0: Orange.misc.distmatrix.DistMatrix,
        _1: Tuple[numpy.ufunc, Tuple[Orange.misc.distmatrix.DistMatrix, int], int],
        /,
    ):
        """
        usage.orange3: 1
        """
        ...

    @overload
    def __array_wrap__(
        self,
        _0: Orange.misc.distmatrix.DistMatrix,
        _1: Tuple[
            numpy.ufunc,
            Tuple[Orange.misc.distmatrix.DistMatrix, Orange.misc.distmatrix.DistMatrix],
            int,
        ],
        /,
    ):
        """
        usage.orange3: 1
        """
        ...

    @overload
    def __array_wrap__(
        self,
        _0: Orange.misc.distmatrix.DistMatrix,
        _1: Tuple[numpy.ufunc, Tuple[Orange.misc.distmatrix.DistMatrix], int],
        /,
    ):
        """
        usage.orange3: 1
        """
        ...

    @overload
    def __array_wrap__(
        self,
        _0: Orange.misc.distmatrix.DistMatrix,
        _1: Tuple[numpy.ufunc, Tuple[float, Orange.misc.distmatrix.DistMatrix], int],
        /,
    ):
        """
        usage.orange3: 1
        """
        ...

    @overload
    def __array_wrap__(
        self,
        _0: Orange.misc.distmatrix.DistMatrix,
        _1: Tuple[numpy.ufunc, Tuple[float, Orange.misc.distmatrix.DistMatrix], int],
        /,
    ):
        """
        usage.orange3: 1
        """
        ...

    @overload
    def __array_wrap__(
        self,
        _0: Orange.misc.distmatrix.DistMatrix,
        _1: Tuple[
            numpy.ufunc,
            Tuple[Orange.misc.distmatrix.DistMatrix, Orange.misc.distmatrix.DistMatrix],
            int,
        ],
        /,
    ):
        """
        usage.orange3: 1
        """
        ...

    @overload
    def __array_wrap__(
        self,
        _0: Orange.misc.distmatrix.DistMatrix,
        _1: Tuple[
            numpy.ufunc, Tuple[numpy.float64, Orange.misc.distmatrix.DistMatrix], int
        ],
        /,
    ):
        """
        usage.orange3: 1
        """
        ...

    @overload
    def __array_wrap__(
        self,
        _0: Orange.misc.distmatrix.DistMatrix,
        _1: Tuple[numpy.ufunc, Tuple[Orange.misc.distmatrix.DistMatrix, float], int],
        /,
    ):
        """
        usage.orange3: 1
        """
        ...

    @overload
    def __array_wrap__(
        self,
        _0: Orange.misc.distmatrix.DistMatrix,
        _1: Tuple[numpy.ufunc, Tuple[Orange.misc.distmatrix.DistMatrix, int], int],
        /,
    ):
        """
        usage.orange3: 1
        """
        ...

    def __array_wrap__(
        self,
        _0: Orange.misc.distmatrix.DistMatrix,
        _1: Tuple[
            numpy.ufunc,
            Tuple[
                Union[
                    int,
                    Orange.misc.distmatrix.DistMatrix,
                    numpy.float64,
                    numpy.ndarray,
                    float,
                ],
                ...,
            ],
            int,
        ],
        /,
    ):
        """
        usage.orange3: 29
        """
        ...
