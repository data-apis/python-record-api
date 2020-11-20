from typing import *


class PlotAccessor:
    @overload
    def area(self, /):
        """
        usage.hvplot: 2
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
        usage.hvplot: 2
        usage.koalas: 2
        """
        ...

    def bar(self, /):
        """
        usage.hvplot: 2
        usage.koalas: 1
        """
        ...

    def barh(self, /):
        """
        usage.hvplot: 2
        usage.koalas: 1
        """
        ...

    def box(self, /):
        """
        usage.hvplot: 2
        usage.koalas: 1
        """
        ...

    def hexbin(self, /, x: Literal["a"], y: Literal["b"]):
        """
        usage.hvplot: 1
        """
        ...

    def hist(self, /):
        """
        usage.hvplot: 2
        """
        ...

    @overload
    def kde(self, /, bw_method: float):
        """
        usage.koalas: 2
        """
        ...

    @overload
    def kde(self, /):
        """
        usage.hvplot: 2
        """
        ...

    def kde(self, /, bw_method: float = ...):
        """
        usage.hvplot: 2
        usage.koalas: 2
        """
        ...

    def line(self, /):
        """
        usage.hvplot: 2
        """
        ...

    def pie(self, /):
        """
        usage.hvplot: 1
        usage.koalas: 3
        """
        ...

    def scatter(self, /, x: Literal["a"], y: Literal["b"]):
        """
        usage.hvplot: 1
        usage.koalas: 1
        """
        ...
