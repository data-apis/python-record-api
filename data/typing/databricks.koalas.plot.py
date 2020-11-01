from typing import *


class KoalasAreaPlot:
    def __init__(self, /, data: pandas.core.frame.DataFrame):
        """
        usage.koalas: 1
        """
        ...

    def _make_plot(self, /):
        """
        usage.koalas: 1
        """
        ...


class KoalasBarPlot:
    @overload
    def __init__(self, /, data: pandas.core.series.Series):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __init__(self, /, data: pandas.core.frame.DataFrame):
        """
        usage.koalas: 1
        """
        ...

    def __init__(
        self, /, data: Union[pandas.core.frame.DataFrame, pandas.core.series.Series]
    ):
        """
        usage.koalas: 2
        """
        ...


class KoalasBarhPlot:
    @overload
    def __init__(self, /, data: pandas.core.series.Series):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __init__(self, /, data: pandas.core.frame.DataFrame):
        """
        usage.koalas: 1
        """
        ...

    def __init__(
        self, /, data: Union[pandas.core.frame.DataFrame, pandas.core.series.Series]
    ):
        """
        usage.koalas: 2
        """
        ...

    def _make_plot(self, /):
        """
        usage.koalas: 1
        """
        ...


class KoalasHistPlot:
    @overload
    @classmethod
    def _get_stacked_values(
        cls,
        /,
        ax: matplotlib.axes._subplots.AxesSubplot,
        stacking_id: None,
        values: numpy.ndarray,
        label: Literal["0"],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def _get_stacked_values(
        cls,
        /,
        ax: matplotlib.axes._subplots.AxesSubplot,
        stacking_id: None,
        values: numpy.ndarray,
        label: Literal["a"],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    @classmethod
    def _get_stacked_values(
        cls,
        /,
        ax: matplotlib.axes._subplots.AxesSubplot,
        stacking_id: None,
        values: numpy.ndarray,
        label: Literal["single"],
    ):
        """
        usage.koalas: 1
        """
        ...

    @classmethod
    def _get_stacked_values(
        cls,
        /,
        ax: matplotlib.axes._subplots.AxesSubplot,
        stacking_id: None,
        values: numpy.ndarray,
        label: Literal["single", "a", "0"],
    ):
        """
        usage.koalas: 3
        """
        ...

    @classmethod
    def _initialize_stacker(
        cls, /, ax: matplotlib.axes._subplots.AxesSubplot, stacking_id: None, n: int
    ):
        """
        usage.koalas: 1
        """
        ...

    def _get_colors(self, /, num_colors: int):
        """
        usage.koalas: 1
        """
        ...


class KoalasKdePlot:
    def _get_colors(self, /, num_colors: int):
        """
        usage.koalas: 1
        """
        ...


class KoalasLinePlot:
    def __init__(self, /, data: pandas.core.frame.DataFrame):
        """
        usage.koalas: 1
        """
        ...

    def _make_plot(self, /):
        """
        usage.koalas: 1
        """
        ...


class KoalasPiePlot:
    def __init__(self, /, data: pandas.core.series.Series, kind: Literal["pie"]):
        """
        usage.koalas: 1
        """
        ...

    def _make_plot(self, /):
        """
        usage.koalas: 1
        """
        ...


class KoalasScatterPlot:
    @overload
    def __init__(
        self,
        /,
        data: pandas.core.frame.DataFrame,
        x: Literal["length"],
        y: Literal["width"],
        s: None,
        c: Literal["DarkBlue"],
    ):
        """
        usage.koalas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: pandas.core.frame.DataFrame,
        x: Literal["a"],
        y: Literal["b"],
        s: None,
        c: None,
    ):
        """
        usage.koalas: 1
        """
        ...

    def __init__(
        self,
        /,
        data: pandas.core.frame.DataFrame,
        x: Literal["a", "length"],
        y: Literal["b", "width"],
        s: None,
        c: Union[None, Literal["DarkBlue"]],
    ):
        """
        usage.koalas: 2
        """
        ...

    def _make_plot(self, /):
        """
        usage.koalas: 1
        """
        ...
