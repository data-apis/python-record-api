from typing import *


@overload
def pprint_thing(thing: Literal["0"]):
    """
    usage.koalas: 2
    """
    ...


@overload
def pprint_thing(thing: int):
    """
    usage.dask: 2
    usage.koalas: 1
    """
    ...


@overload
def pprint_thing(thing: Literal["a"]):
    """
    usage.koalas: 2
    """
    ...


@overload
def pprint_thing(thing: Literal["float64"]):
    """
    usage.koalas: 1
    """
    ...


@overload
def pprint_thing(thing: Literal["int64"]):
    """
    usage.koalas: 1
    """
    ...


@overload
def pprint_thing(thing: Literal["single"]):
    """
    usage.koalas: 1
    """
    ...


@overload
def pprint_thing(thing: Literal["x"]):
    """
    usage.dask: 2
    """
    ...


@overload
def pprint_thing(thing: Literal["y"]):
    """
    usage.dask: 2
    """
    ...


@overload
def pprint_thing(thing: numpy.dtype):
    """
    usage.dask: 2
    """
    ...


@overload
def pprint_thing(thing: Literal["C"]):
    """
    usage.dask: 2
    """
    ...


@overload
def pprint_thing(thing: Tuple[Literal["C"], Literal["count"]]):
    """
    usage.dask: 2
    """
    ...


@overload
def pprint_thing(thing: Tuple[Literal["C"], Literal["sum"]]):
    """
    usage.dask: 2
    """
    ...


@overload
def pprint_thing(thing: Literal["z"]):
    """
    usage.dask: 2
    """
    ...


@overload
def pprint_thing(thing: pandas.core.dtypes.dtypes.CategoricalDtype):
    """
    usage.dask: 1
    """
    ...


def pprint_thing(
    thing: Union[
        Tuple[Literal["C"], Literal["count", "sum"]],
        str,
        pandas.core.dtypes.dtypes.CategoricalDtype,
        int,
        numpy.dtype,
    ]
):
    """
    usage.dask: 17
    usage.koalas: 8
    """
    ...


class PrettyDict:
    def __contains__(self, _0: int, /):
        """
        usage.dask: 1
        """
        ...

    @overload
    def __getitem__(self, _0: int, /):
        """
        usage.statsmodels: 3
        """
        ...

    @overload
    def __getitem__(self, _0: Tuple[numpy.float64, numpy.int32], /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __getitem__(self, _0: float, /):
        """
        usage.statsmodels: 2
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["A"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["B"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["C"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["D"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["E"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["F"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["G"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["H"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["I"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["J"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g0"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g1"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g10"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g100"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g101"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g102"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g103"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g104"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g105"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g106"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g107"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g108"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g109"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g11"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g110"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g111"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g112"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g113"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g114"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g115"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g116"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g117"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g118"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g119"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g12"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g120"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g121"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g122"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g123"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g124"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g125"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g126"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g127"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g128"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g129"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g13"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g130"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g131"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g132"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g133"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g134"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g135"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g136"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g137"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g138"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g139"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g14"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g140"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g141"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g142"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g143"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g144"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g145"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g146"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g147"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g148"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g149"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g15"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g150"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g151"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g152"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g153"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g154"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g155"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g156"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g157"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g158"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g159"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g16"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g160"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g161"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g162"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g163"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g164"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g165"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g166"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g167"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g168"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g169"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g17"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g170"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g171"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g172"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g173"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g174"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g175"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g176"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g177"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g178"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g179"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g18"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g180"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g181"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g182"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g183"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g184"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g185"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g186"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g187"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g188"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g189"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g19"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g190"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g191"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g192"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g193"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g194"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g195"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g196"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g197"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g198"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g199"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g2"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g20"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g200"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g201"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g202"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g203"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g204"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g205"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g206"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g207"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g208"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g209"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g21"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g210"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g211"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g212"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g213"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g214"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g215"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g216"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g217"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g218"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g219"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g22"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g220"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g221"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g222"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g223"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g224"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g225"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g226"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g227"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g228"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g229"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g23"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g230"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g231"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g232"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g233"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g234"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g235"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g236"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g237"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g238"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g239"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g24"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g240"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g241"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g242"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g243"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g244"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g245"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g246"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g247"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g248"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g249"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g25"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g250"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g251"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g252"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g253"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g254"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g255"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g256"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g257"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g258"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g259"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g26"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g260"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g261"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g262"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g263"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g264"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g265"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g266"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g267"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g268"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g269"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g27"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g270"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g271"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g272"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g273"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g274"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g275"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g276"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g277"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g278"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g279"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g28"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g280"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g281"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g282"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g283"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g284"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g285"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g286"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g287"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g288"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g289"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g29"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g290"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g291"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g292"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g293"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g294"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g295"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g296"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g297"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g298"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g299"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g3"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g30"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g300"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g301"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g302"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g303"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g304"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g305"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g306"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g307"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g308"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g309"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g31"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g310"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g311"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g312"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g313"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g314"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g315"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g316"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g317"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g318"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g319"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g32"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g320"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g321"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g322"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g323"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g324"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g325"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g326"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g327"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g328"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g329"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g33"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g330"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g331"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g332"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g333"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g334"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g335"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g336"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g337"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g338"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g339"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g34"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g340"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g341"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g342"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g343"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g344"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g345"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g346"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g347"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g348"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g349"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g35"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g350"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g351"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g352"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g353"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g354"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g355"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g356"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g357"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g358"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g359"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g36"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g360"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g361"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g362"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g363"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g364"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g365"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g366"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g367"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g368"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g369"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g37"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g370"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g371"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g372"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g373"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g374"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g375"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g376"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g377"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g378"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g379"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g38"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g380"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g381"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g382"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g383"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g384"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g385"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g386"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g387"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g388"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g389"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g39"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g390"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g391"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g392"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g393"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g394"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g395"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g396"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g397"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g398"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g399"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g4"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g40"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g400"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g401"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g402"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g403"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g404"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g405"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g406"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g407"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g408"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g409"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g41"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g410"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g411"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g412"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g413"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g414"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g415"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g416"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g417"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g418"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g419"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g42"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g420"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g421"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g422"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g423"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g424"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g425"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g426"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g427"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g428"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g429"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g43"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g430"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g431"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g432"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g433"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g434"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g435"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g436"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g437"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g438"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g439"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g44"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g440"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g441"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g442"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g443"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g444"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g445"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g446"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g447"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g448"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g449"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g45"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g450"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g451"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g452"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g453"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g454"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g455"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g456"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g457"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g458"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g459"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g46"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g460"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g461"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g462"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g463"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g464"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g465"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g466"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g467"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g468"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g469"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g47"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g470"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g471"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g472"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g473"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g474"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g475"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g476"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g477"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g478"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g479"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g48"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g480"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g481"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g482"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g483"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g484"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g485"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g486"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g487"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g488"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g489"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g49"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g490"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g491"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g492"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g493"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g494"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g495"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g496"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g497"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g498"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g499"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g5"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g50"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g51"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g52"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g53"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g54"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g55"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g56"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g57"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g58"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g59"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g6"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g60"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g61"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g62"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g63"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g64"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g65"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g66"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g67"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g68"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g69"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g7"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g70"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g71"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g72"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g73"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g74"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g75"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g76"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g77"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g78"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g79"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g8"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g80"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g81"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g82"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g83"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g84"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g85"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g86"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g87"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g88"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g89"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g9"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g90"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g91"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g92"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g93"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g94"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g95"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g96"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g97"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g98"], /):
        """
        usage.statsmodels: 1
        """
        ...

    @overload
    def __getitem__(self, _0: Literal["g99"], /):
        """
        usage.statsmodels: 1
        """
        ...

    def __getitem__(
        self, _0: Union[str, float, int, Tuple[numpy.float64, numpy.int32]], /
    ):
        """
        usage.statsmodels: 517
        """
        ...

    def __iter__(self, /):
        """
        usage.dask: 1
        usage.statsmodels: 1
        """
        ...

    def keys(self, /):
        """
        usage.statsmodels: 1
        """
        ...
