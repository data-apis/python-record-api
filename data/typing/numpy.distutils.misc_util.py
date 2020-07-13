from typing import *


class Configuration:

    # usage.sklearn: 2
    ext_modules: List[numpy.distutils.extension.Extension]

    def add_subpackage(self, /, subpackage_name: Literal["sklearn"]):
        """
        usage.sklearn: 1
        """
        ...

    def set_options(self, /):
        """
        usage.sklearn: 1
        """
        ...
