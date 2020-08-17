from typing import *


class NpzFile:
    @overload
    def __getitem__(self, _0: str, /):
        """
        usage.scipy: 256
        usage.skimage: 55
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["ymin", "dy", "dx", "elevation"], /):
        """
        usage.matplotlib: 4
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
