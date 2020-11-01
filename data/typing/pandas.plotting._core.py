from typing import *


class PlotAccessor:
    @overload
    def area(self, /):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def area(self, /, y: Literal["sales"]):
        """
        usage.koalas: 1
        """
        ...

    def area(self, /, y: Literal["sales"] = ...):
        """
        usage.koalas: 2
        """
        ...

    def bar(self, /):
        """
        usage.koalas: 1
        """
        ...

    def barh(self, /):
        """
        usage.koalas: 1
        """
        ...

    def box(self, /):
        """
        usage.koalas: 1
        """
        ...

    def kde(self, /, bw_method: float):
        """
        usage.koalas: 2
        """
        ...

    def pie(self, /):
        """
        usage.koalas: 3
        """
        ...

    def scatter(self, /, x: Literal["a"], y: Literal["b"]):
        """
        usage.koalas: 1
        """
        ...
