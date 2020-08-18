from typing import *


class Configuration:

    # usage.sklearn: 2
    ext_modules: List[numpy.distutils.extension.Extension]

    def set_options(self, /):
        """
        usage.sklearn: 1
        """
        ...
