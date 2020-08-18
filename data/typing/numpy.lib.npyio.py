from typing import *


class NpzFile:
    @overload
    def __getitem__(self, _0: Literal["arr_0"], /):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["autolevel"], /):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["autolevel_percentile"], /):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["equalize"], /):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["gradient"], /):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["gradient_percentile"], /):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["maximum"], /):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["mean"], /):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["geometric_mean"], /):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["mean_percentile"], /):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["mean_bilateral"], /):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["subtract_mean"], /):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(self, _0: str, /):
        """
        usage.scipy: 256
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["median"], /):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["minimum"], /):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["modal"], /):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["enhance_contrast"], /):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["pop"], /):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["pop_percentile"], /):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["pop_bilateral"], /):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["sum"], /):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["sum_bilateral"], /):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["sum_percentile"], /):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["threshold"], /):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["threshold_percentile"], /):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["noise_filter"], /):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["entropy"], /):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["otsu"], /):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["percentile"], /):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["windowed_histogram"], /):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["majority"], /):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["grad_matlab"], /):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["mssim_matlab"], /):
        """
        usage.skimage: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["000"], /):
        """
        usage.skimage: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["001"], /):
        """
        usage.skimage: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["002"], /):
        """
        usage.skimage: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["003"], /):
        """
        usage.skimage: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["004"], /):
        """
        usage.skimage: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["005"], /):
        """
        usage.skimage: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["006"], /):
        """
        usage.skimage: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["007"], /):
        """
        usage.skimage: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["008"], /):
        """
        usage.skimage: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["009"], /):
        """
        usage.skimage: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["010"], /):
        """
        usage.skimage: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["elevation"], /):
        """
        usage.matplotlib: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["dx"], /):
        """
        usage.matplotlib: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["dy"], /):
        """
        usage.matplotlib: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["ymin"], /):
        """
        usage.matplotlib: 1
        """
        ...

    def __getitem__(self, _0: str, /):
        """
        usage.matplotlib: 4
        usage.scipy: 256
        usage.skimage: 55
        """
        ...

    def close(self, /):
        """
        usage.scipy: 1
        """
        ...
