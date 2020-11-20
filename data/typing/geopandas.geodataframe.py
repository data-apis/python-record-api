from typing import *


class GeoDataFrame:
    @overload
    def __getitem__(self, /, key: Literal["geometry"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: Literal["iso_a3"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: int):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: Literal["geom2"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: List[Literal["geometry", "name"]]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: List[Literal["geom2", "name"]]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: Literal["geom3"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: List[Literal["geom3", "geom2", "name"]]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: pandas.core.series.Series):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: pandas.core.indexes.base.Index):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: Literal["BoroName"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: Literal["Name"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: Literal["b"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: Literal["continent"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: Literal["value1"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: Literal["value2"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: Literal["the_geom"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: Literal["geom"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: Literal["col1"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: Literal["geom4"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: Literal["column1"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: Literal["col2"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: Literal["myshapes"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: Literal["manhattan_bronx"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: Literal["dup_col"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: Literal["address"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: Literal["location"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: Literal["A"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: Literal["buff"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: Literal["array"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: List[Literal["value2", "value1"]]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: List[Literal["geometry", "value2", "value1"]]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: Literal["other_geom"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: Literal["new_name"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: Literal["nonexistent-column"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: Literal["simplified_geometry"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: List[Literal["b", "a"]]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: List[Literal["name", "lon", "lat", "geometry"]]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(
        self, /, key: List[Literal["geometry", "Shape_Area", "Shape_Leng"]]
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: Literal["B"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: List[Literal["geometry"]]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: Literal["x"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: Literal["my_geom"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: Literal["level_1"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: Literal["values"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: Literal["points"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: numpy.ndarray):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: List[Literal["geometry", "value1"]]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: Literal["geom_list"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: slice[int, None, int]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: Literal["exp"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: Literal["cats_object"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: Literal["cats"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: Literal["singlecat_object"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: Literal["singlecat"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: Literal["cats_ordered"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: Literal["nums"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: Literal["pop_est"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: Literal["NEGATIVES"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: Literal["gdp_md_est"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: List[Literal["col1", "geometry"]]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: Literal["coords"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: List[Literal["value1", "geometry"]]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: slice[None, int, None]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __getitem__(self, /, key: slice[None, None, None]):
        """
        usage.geopandas: 1
        """
        ...

    def __getitem__(self, /, key: object):
        """
        usage.geopandas: 65
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: List[
            Dict[
                str,
                Union[
                    str,
                    shapely.geometry.multipolygon.MultiPolygon,
                    int,
                    float,
                    shapely.geometry.polygon.Polygon,
                ],
            ]
        ],
        columns: List[str],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(self, /, data: pandas.core.internals.managers.BlockManager):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(self, /, data: pandas.core.frame.DataFrame):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: List[
            Dict[Literal["name", "geometry"], Union[shapely.geometry.point.Point, str]]
        ],
        columns: List[Literal["geometry", "name"]],
    ):
        """
        usage.geopandas: 2
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: List[
            Dict[
                Literal["Shape_Area", "Shape_Leng", "BoroName", "BoroCode", "geometry"],
                Union[
                    Literal[
                        "Staten Island", "Queens", "Brooklyn", "Manhattan", "Bronx"
                    ],
                    shapely.geometry.multipolygon.MultiPolygon,
                    int,
                    float,
                ],
            ]
        ],
        columns: List[
            Literal["geometry", "Shape_Area", "Shape_Leng", "BoroName", "BoroCode"]
        ],
    ):
        """
        usage.geopandas: 2
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: List[
            Dict[
                Literal["Name", "geometry"],
                Union[
                    None,
                    Literal["Null Geometry", "SF to NY"],
                    shapely.geometry.linestring.LineString,
                ],
            ]
        ],
        columns: List[Literal["geometry", "Name"]],
    ):
        """
        usage.geopandas: 2
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: Dict[
            Literal["geometry", "b", "a"],
            List[Union[int, bool, shapely.geometry.point.Point]],
        ],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: List[
            Dict[
                Literal["b", "a", "geometry"], Union[shapely.geometry.point.Point, int]
            ]
        ],
        columns: List[Literal["geometry", "b", "a"]],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: List[
            Dict[
                Literal["b", "a", "geometry"],
                Union[shapely.geometry.point.Point, int, bool],
            ]
        ],
        columns: List[Literal["geometry", "b", "a"]],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: Dict[
            Literal["b", "a"], List[Union[int, Literal["2020-11-20T00:02:14.953187"]]]
        ],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: List[
            Dict[
                Literal["b", "a", "geometry"],
                Union[shapely.geometry.point.Point, int, str],
            ]
        ],
        columns: List[Literal["geometry", "b", "a"]],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(self, /, data: Dict[Literal["a"], List[int]]):
        """
        usage.geopandas: 2
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: List[
            Dict[Literal["a", "geometry"], Union[shapely.geometry.point.Point, int]]
        ],
        columns: List[Literal["geometry", "a"]],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: List[
            Dict[Literal["a", "geometry"], Union[shapely.geometry.polygon.Polygon, int]]
        ],
        columns: List[Literal["geometry", "a"]],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(self, /, data: Dict[str, numpy.ndarray]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(self, /):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: List[
            Dict[
                Literal["data", "geometry"],
                Union[shapely.geometry.point.Point, int, None],
            ]
        ],
        columns: List[Literal["geometry", "data"]],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: List[
            Dict[
                Literal["name", "geometry"],
                Union[shapely.geometry.point.Point, Literal["Null Island"]],
            ]
        ],
        columns: List[Literal["geometry", "name"]],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: List[
            Dict[
                Literal["Shape_Area", "Shape_Leng", "BoroName", "BoroCode", "geometry"],
                Union[
                    Literal["Queens", "Bronx"],
                    shapely.geometry.multipolygon.MultiPolygon,
                    int,
                    float,
                ],
            ]
        ],
        columns: List[
            Literal["geometry", "Shape_Area", "Shape_Leng", "BoroName", "BoroCode"]
        ],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: List[
            Dict[
                Literal["Shape_Area", "Shape_Leng", "BoroName", "BoroCode", "geometry"],
                Union[
                    Literal["Staten Island"],
                    shapely.geometry.multipolygon.MultiPolygon,
                    int,
                    float,
                ],
            ]
        ],
        columns: List[
            Literal["geometry", "Shape_Area", "Shape_Leng", "BoroName", "BoroCode"]
        ],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: List[
            Dict[
                Literal["Shape_Area", "Shape_Leng", "BoroName", "BoroCode", "geometry"],
                Union[
                    Literal["Bronx"],
                    shapely.geometry.multipolygon.MultiPolygon,
                    int,
                    float,
                ],
            ]
        ],
        columns: List[
            Literal["geometry", "Shape_Area", "Shape_Leng", "BoroName", "BoroCode"]
        ],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: List[
            Dict[
                Literal["geometry"],
                Union[
                    shapely.geometry.polygon.Polygon,
                    shapely.geometry.multipolygon.MultiPolygon,
                ],
            ]
        ],
        columns: List[Literal["geometry"]],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(self, /, data: list, columns: List[Literal["geometry", "Z", "A"]]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(self, /, data: pandas.core.series.Series):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: List[
            Dict[
                Literal["value1", "geometry"], Union[shapely.geometry.point.Point, int]
            ]
        ],
        columns: List[Literal["geometry", "value1"]],
    ):
        """
        usage.geopandas: 2
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: Dict[Literal["geometry"], geopandas.geoseries.GeoSeries],
        index: pandas.core.indexes.range.RangeIndex,
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: List[
            Dict[Literal["FID", "geometry"], Union[shapely.geometry.point.Point, int]]
        ],
        columns: List[Literal["geometry", "FID"]],
    ):
        """
        usage.geopandas: 2
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: List[
            Dict[
                Literal["value1", "index", "geometry"],
                Union[shapely.geometry.point.Point, int],
            ]
        ],
        columns: List[Literal["geometry", "value1", "index"]],
    ):
        """
        usage.geopandas: 2
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: List[
            Dict[Literal["index", "geometry"], Union[shapely.geometry.point.Point, int]]
        ],
        columns: List[Literal["geometry", "index"]],
    ):
        """
        usage.geopandas: 2
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: Dict[Literal["geometry"], geopandas.geoseries.GeoSeries],
        index: pandas.core.indexes.numeric.Int64Index,
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: List[
            Dict[
                Literal["value1", "foo_index", "geometry"],
                Union[shapely.geometry.point.Point, int],
            ]
        ],
        columns: List[Literal["geometry", "value1", "foo_index"]],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: List[
            Dict[
                Literal["foo_index", "geometry"],
                Union[shapely.geometry.point.Point, int],
            ]
        ],
        columns: List[Literal["geometry", "foo_index"]],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(self, /, data: geopandas.geodataframe.GeoDataFrame):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: List[
            Dict[
                Literal["value3", "value2", "value1", "geometry"],
                Union[shapely.geometry.point.Point, int],
            ]
        ],
        columns: List[Literal["geometry", "value3", "value2", "value1"]],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: Dict[Literal["geometry"], geopandas.geoseries.GeoSeries],
        index: pandas.core.indexes.multi.MultiIndex,
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: List[
            Dict[
                Literal["value2", "value1", "geometry"],
                Union[shapely.geometry.point.Point, int],
            ]
        ],
        columns: List[Literal["geometry", "value2", "value1"]],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: List[
            Dict[
                Literal["value3", "geometry"], Union[shapely.geometry.point.Point, int]
            ]
        ],
        columns: List[Literal["geometry", "value3"]],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: List[
            Dict[
                Literal["value3", "level_1", "first", "geometry"],
                Union[shapely.geometry.point.Point, int],
            ]
        ],
        columns: List[Literal["geometry", "value3", "level_1", "first"]],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: List[
            Dict[
                Literal["level_1", "first", "geometry"],
                Union[shapely.geometry.point.Point, int],
            ]
        ],
        columns: List[Literal["geometry", "level_1", "first"]],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: List[
            Dict[
                Literal["value3", "level_1", "level_0", "geometry"],
                Union[shapely.geometry.point.Point, int],
            ]
        ],
        columns: List[Literal["geometry", "value3", "level_1", "level_0"]],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: List[
            Dict[
                Literal["level_1", "level_0", "geometry"],
                Union[shapely.geometry.point.Point, int],
            ]
        ],
        columns: List[Literal["geometry", "level_1", "level_0"]],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: List[
            Dict[
                Literal["value1", "index", "geometry"],
                Union[shapely.geometry.point.Point, float, int],
            ]
        ],
        columns: List[Literal["geometry", "value1", "index"]],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: Dict[Literal["geometry"], geopandas.geoseries.GeoSeries],
        index: pandas.core.indexes.numeric.Float64Index,
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: List[
            Dict[
                Literal["index", "geometry"], Union[shapely.geometry.point.Point, float]
            ]
        ],
        columns: List[Literal["geometry", "index"]],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: List[
            Dict[
                Literal["value1", "centile", "geometry"],
                Union[shapely.geometry.point.Point, float, int],
            ]
        ],
        columns: List[Literal["geometry", "value1", "centile"]],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: List[
            Dict[
                Literal["centile", "geometry"],
                Union[shapely.geometry.point.Point, float],
            ]
        ],
        columns: List[Literal["geometry", "centile"]],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: List[
            Dict[
                Literal["value1", "index", "geometry"],
                Union[str, shapely.geometry.point.Point, int],
            ]
        ],
        columns: List[Literal["geometry", "value1", "index"]],
    ):
        """
        usage.geopandas: 3
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: Dict[Literal["geometry"], geopandas.geoseries.GeoSeries],
        index: pandas.core.indexes.base.Index,
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: List[
            Dict[Literal["index", "geometry"], Union[shapely.geometry.point.Point, str]]
        ],
        columns: List[Literal["geometry", "index"]],
    ):
        """
        usage.geopandas: 3
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: List[
            Dict[
                Literal["value1", "datetime", "geometry"],
                Union[str, shapely.geometry.point.Point, int],
            ]
        ],
        columns: List[Literal["geometry", "value1", "datetime"]],
    ):
        """
        usage.geopandas: 2
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: List[
            Dict[
                Literal["datetime", "geometry"],
                Union[shapely.geometry.point.Point, str],
            ]
        ],
        columns: List[Literal["geometry", "datetime"]],
    ):
        """
        usage.geopandas: 2
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: List[Dict[Literal["geometry"], shapely.geometry.point.Point]],
        columns: List[Literal["geometry"]],
    ):
        """
        usage.geopandas: 2
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: Dict[Literal["geometry"], geopandas.geoseries.GeoSeries],
        index: pandas.core.indexes.datetimes.DatetimeIndex,
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: List[
            Dict[
                Literal["a", "geometry"],
                Union[shapely.geometry.multipoint.MultiPoint, int],
            ]
        ],
        columns: List[Literal["geometry", "a"]],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: List[
            Dict[
                Literal["a", "geometry"],
                Union[
                    shapely.geometry.multipoint.MultiPoint,
                    int,
                    shapely.geometry.point.Point,
                ],
            ]
        ],
        columns: List[Literal["geometry", "a"]],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: List[
            Dict[
                Literal["a", "geometry"],
                Union[shapely.geometry.linestring.LineString, int],
            ]
        ],
        columns: List[Literal["geometry", "a"]],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: List[
            Dict[
                Literal["a", "geometry"],
                Union[shapely.geometry.multilinestring.MultiLineString, int],
            ]
        ],
        columns: List[Literal["geometry", "a"]],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: List[
            Dict[
                Literal["a", "geometry"],
                Union[
                    shapely.geometry.multilinestring.MultiLineString,
                    int,
                    shapely.geometry.linestring.LineString,
                ],
            ]
        ],
        columns: List[Literal["geometry", "a"]],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: List[
            Dict[
                Literal["a", "geometry"],
                Union[shapely.geometry.multipolygon.MultiPolygon, int],
            ]
        ],
        columns: List[Literal["geometry", "a"]],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: List[
            Dict[
                Literal["a", "geometry"],
                Union[
                    shapely.geometry.multipolygon.MultiPolygon,
                    int,
                    shapely.geometry.polygon.Polygon,
                ],
            ]
        ],
        columns: List[Literal["geometry", "a"]],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: List[
            Dict[
                Literal["a", "geometry"], Union[None, int, shapely.geometry.point.Point]
            ]
        ],
        columns: List[Literal["geometry", "a"]],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: List[Dict[Literal["a", "geometry"], Union[None, int]]],
        columns: List[Literal["geometry", "a"]],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: List[Dict[Literal["a", "geometry"], object]],
        columns: List[Literal["geometry", "a"]],
    ):
        """
        usage.geopandas: 2
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: Dict[
            Literal["value2", "value1", "geometry"],
            Union[numpy.ndarray, geopandas.array.GeometryArray],
        ],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: Dict[
            Literal["geometry", "data"], Union[geopandas.geoseries.GeoSeries, List[int]]
        ],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: List[shapely.geometry.point.Point],
        columns: List[Literal["geom"]],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: Dict[
            Literal["geometry", "col1"], Union[geopandas.array.GeometryArray, List[int]]
        ],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(self, /, data: Dict[Literal["geometry"], List[int]]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self, /, data: geopandas.geoseries.GeoSeries, columns: List[Literal["col1"]]
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(self, /, data: Dict[Literal["col1"], geopandas.array.GeometryArray]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(self, /, data: Dict[Literal["col1"], geopandas.geoseries.GeoSeries]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(self, /, data: Dict[Literal["col2"], geopandas.geoseries.GeoSeries]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(self, /, data: list):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(self, /, data: Dict[Literal["col1"], List[int]]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(self, /, data: geopandas.geoseries.GeoSeries):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self, /, data: collections.defaultdict, index: List[Literal["b", "a"]]
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(self, /, data: collections.defaultdict, index: List[int]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: Dict[
            Literal["location", "B", "A"],
            Union[List[shapely.geometry.point.Point], range],
        ],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: Dict[
            Literal["geometry", "location", "B", "A"],
            Union[List[shapely.geometry.point.Point], range],
        ],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: Dict[
            Literal["geometry", "B", "A"],
            Union[List[shapely.geometry.point.Point], numpy.ndarray, range],
        ],
    ):
        """
        usage.geopandas: 2
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: Dict[
            Literal["geometry", "other_geom", "B", "A"],
            Union[List[shapely.geometry.point.Point], range, numpy.ndarray],
        ],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: List[
            Dict[
                Literal["Shape_Area", "Shape_Leng", "BoroName", "BoroCode", "geometry"],
                Union[
                    Literal[
                        "Staten Island", "Queens", "Brooklyn", "Manhattan", "Bronx"
                    ],
                    shapely.geometry.multipolygon.MultiPolygon,
                    int,
                    float,
                ],
            ]
        ],
        columns: None,
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: List[
            Dict[
                Literal["b", "geometry", "a"], Union[shapely.geometry.point.Point, int]
            ]
        ],
        columns: None,
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: List[
            Dict[Literal["a", "geometry"], Union[shapely.geometry.point.Point, int]]
        ],
        columns: None,
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: List[
            Dict[
                Literal["name", "lon", "lat", "geometry"],
                Union[shapely.geometry.point.Point, float, Literal["a", "b", "c"]],
            ]
        ],
        columns: None,
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: Dict[
            Literal["geom", "values"], List[Union[int, shapely.geometry.point.Point]]
        ],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: Dict[
            Literal["geometry", "B", "A"],
            Union[List[shapely.geometry.point.Point], numpy.ndarray, range],
        ],
        index: List[Literal["c", "b", "a"]],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: Dict[
            Literal["geometry", "B", "A"],
            Union[List[shapely.geometry.point.Point], numpy.ndarray, range],
        ],
        columns: List[Literal["geometry", "A", "B"]],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: Dict[
            Literal["geometry", "B", "A"],
            Union[List[shapely.geometry.point.Point], numpy.ndarray, range],
        ],
        columns: List[Literal["geometry", "A"]],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: Dict[
            Literal["geometry", "B", "A"],
            Union[geopandas.geoseries.GeoSeries, pandas.core.series.Series],
        ],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: Dict[
            Literal["geometry", "B", "A"],
            Union[geopandas.geoseries.GeoSeries, pandas.core.series.Series],
        ],
        index: pandas.core.indexes.numeric.Int64Index,
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: Dict[
            Literal["geometry", "B", "A"],
            Union[
                geopandas.geoseries.GeoSeries, numpy.ndarray, pandas.core.series.Series
            ],
        ],
        index: List[int],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: Dict[
            Literal["other_geom", "B", "A"],
            Union[List[shapely.geometry.point.Point], numpy.ndarray, range],
        ],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: Dict[
            Literal["other_geom", "B", "A"],
            Union[List[shapely.geometry.point.Point], numpy.ndarray, range],
        ],
        columns: List[Literal["other_geom", "B"]],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: Dict[
            Literal["other_geom", "B", "A"],
            Union[List[shapely.geometry.point.Point], numpy.ndarray, range],
        ],
        columns: List[Literal["A", "other_geom"]],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self, /, data: numpy.ndarray, columns: List[Literal["geometry", "B", "A"]]
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self, /, data: numpy.ndarray, columns: List[Literal["other_geom", "B", "A"]]
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: geopandas.geodataframe.GeoDataFrame,
        index: pandas.core.indexes.numeric.Int64Index,
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: geopandas.geodataframe.GeoDataFrame,
        columns: List[Literal["B", "geometry"]],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: pandas.core.frame.DataFrame,
        index: pandas.core.indexes.numeric.Int64Index,
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: pandas.core.frame.DataFrame,
        columns: List[Literal["B", "geometry"]],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: Dict[
            Literal["other", "geometry"],
            Union[range, List[shapely.geometry.point.Point]],
        ],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self, /, data: Dict[Literal["geometry"], List[shapely.geometry.point.Point]]
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self, /, data: Dict[Literal["other_geom"], List[shapely.geometry.point.Point]]
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(self, /, data: Dict[Literal["B", "A"], Union[numpy.ndarray, range]]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(self, /, data: Dict[Literal["x"], List[int]]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(self, /, data: Dict[Literal["B", "A"], list]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: Dict[
            Literal["geometry", "a"], Union[geopandas.geoseries.GeoSeries, List[int]]
        ],
        columns: List[Literal["a", "geometry"]],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: Dict[
            Literal["geometry", "a"], Union[geopandas.geoseries.GeoSeries, List[int]]
        ],
        index: pandas.core.indexes.numeric.Int64Index,
        columns: List[Literal["a", "geometry"]],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: Dict[
            Literal["col2", "col1", "geometry"],
            Union[range, geopandas.array.GeometryArray, Literal["ab"]],
        ],
        index: pandas.core.indexes.range.RangeIndex,
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: Dict[
            Literal["col2", "col1", "geometry"],
            Union[range, geopandas.array.GeometryArray, Literal[""]],
        ],
        index: pandas.core.indexes.range.RangeIndex,
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: Dict[
            Literal["col1", "geometry"], Union[range, geopandas.geoseries.GeoSeries]
        ],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: Dict[
            Literal["geometry", "col"], Union[geopandas.geoseries.GeoSeries, List[int]]
        ],
    ):
        """
        usage.geopandas: 2
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: Dict[
            Literal["geometry", "level_1"],
            Union[geopandas.geoseries.GeoSeries, List[int]],
        ],
    ):
        """
        usage.geopandas: 2
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: List[
            Dict[
                Literal["FID", "geometry"], Union[shapely.geometry.polygon.Polygon, int]
            ]
        ],
        columns: List[Literal["geometry", "FID"]],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self, /, data: Dict[Literal["geometry"], geopandas.geoseries.GeoSeries]
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: Dict[
            Literal["geometry", "a"], Union[geopandas.geoseries.GeoSeries, List[int]]
        ],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: Dict[
            Literal["geometry", "a"], Union[geopandas.geoseries.GeoSeries, list]
        ],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: Dict[
            int, Union[pandas.core.series.Series, geopandas.geoseries.GeoSeries]
        ],
        index: pandas.core.indexes.range.RangeIndex,
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(self, /, data: Dict[Literal["b", "a"], List[int]]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: Dict[
            Literal["value1", "geometry"],
            Union[range, List[shapely.geometry.point.Point]],
        ],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: Dict[
            Literal["values", "geometry"],
            Union[List[int], geopandas.geoseries.GeoSeries],
        ],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: Dict[
            Literal["geometry", "col1"], Union[geopandas.geoseries.GeoSeries, List[int]]
        ],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __init__(
        self,
        /,
        data: Dict[
            Literal["nums", "coords"], Union[range, List[shapely.geometry.point.Point]]
        ],
    ):
        """
        usage.geopandas: 1
        """
        ...

    def __init__(
        self,
        /,
        data: object = ...,
        index: object = ...,
        columns: Union[List[str], None] = ...,
    ):
        """
        usage.geopandas: 143
        """
        ...

    @overload
    def __setattr__(self, /, name: Literal["_crs"], value: Literal["epsg:4326"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setattr__(self, /, name: str, value: Literal["geometry"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setattr__(self, /, name: Literal["crs"], value: pyproj.crs.crs.CRS):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setattr__(self, /, name: Literal["_crs"], value: pyproj.crs.crs.CRS):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setattr__(self, /, name: Literal["_sindex"], value: None):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setattr__(self, /, name: Literal["_sindex_generated"], value: bool):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setattr__(self, /, name: Literal["_crs"], value: None):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setattr__(
        self, /, name: Literal["index"], value: pandas.core.indexes.base.Index
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setattr__(
        self, /, name: Literal["index"], value: pandas.core.indexes.numeric.Int64Index
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setattr__(
        self,
        /,
        name: Literal["_mgr"],
        value: pandas.core.internals.managers.BlockManager,
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setattr__(self, /, name: Literal["_crs"], value: Literal["epsg:2263"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setattr__(
        self, /, name: Literal["index"], value: pandas.core.indexes.range.RangeIndex
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setattr__(self, /, name: Literal["_is_copy"], value: weakref):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setattr__(
        self,
        /,
        name: Literal["__class__"],
        value: Type[geopandas.geodataframe.GeoDataFrame],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setattr__(self, /, name: str, value: Literal["geom2"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setattr__(self, /, name: Literal["crs"], value: None):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setattr__(
        self, /, name: Literal["__class__"], value: Type[pandas.core.frame.DataFrame]
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setattr__(self, /, name: Literal["_crs"], value: Literal[""]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setattr__(self, /, name: Literal["crs"], value: Literal[""]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setattr__(self, /, name: Literal["_crs"], value: dict):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setattr__(self, /, name: Literal["crs"], value: dict):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setattr__(self, /, name: Literal["crs"], value: Literal["epsg:4326"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setattr__(
        self, /, name: Literal["columns"], value: pandas.core.indexes.base.Index
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setattr__(self, /, name: Literal["crs"], value: Literal["epsg:2263"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setattr__(self, /, name: Literal["index"], value: List[int]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setattr__(
        self, /, name: Literal["index"], value: pandas.core.indexes.multi.MultiIndex
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setattr__(
        self, /, name: Literal["index"], value: pandas.core.indexes.numeric.Float64Index
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setattr__(
        self,
        /,
        name: Literal["index"],
        value: pandas.core.indexes.timedeltas.TimedeltaIndex,
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setattr__(
        self,
        /,
        name: Literal["index"],
        value: pandas.core.indexes.datetimes.DatetimeIndex,
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setattr__(self, /, name: Literal["_attrs"], value: dict):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setattr__(self, /, name: Literal["_item_cache"], value: dict):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setattr__(self, /, name: Literal["_crs"], value: Literal["epsg:26918"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setattr__(self, /, name: Literal["crs"], value: Literal["epsg:26918"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setattr__(self, /, name: str, value: Literal["geom"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setattr__(self, /, name: Literal["_crs"], value: int):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setattr__(self, /, name: Literal["crs"], value: int):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setattr__(self, /, name: str, value: Literal["col1"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setattr__(self, /, name: Literal["_crs"], value: Literal["EPSG:4326"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setattr__(self, /, name: Literal["crs"], value: Literal["EPSG:4326"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setattr__(self, /, name: str, value: Literal["myshapes"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setattr__(self, /, name: str, value: Literal["location"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setattr__(self, /, name: str, value: Literal["new_name"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setattr__(self, /, name: Literal["crs"], value: Literal["epsg:26909"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setattr__(self, /, name: str, value: Literal["simplified_geometry"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setattr__(self, /, name: Literal["index"], value: range):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setattr__(self, /, name: Literal["_crs"], value: Literal["epsg:3857"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setattr__(self, /, name: Literal["_crs"], value: str):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setattr__(self, /, name: str, value: Literal["other_geom"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setattr__(self, /, name: Literal["crs"], value: Literal["IGNF:ETRS89UTM28"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setattr__(self, /, name: str, value: Literal["points"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setattr__(self, /, name: str, value: Literal["geom_list"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setattr__(self, /, name: Literal["_crs"], value: Literal["EPSG:31370"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setattr__(self, /, name: Literal["crs"], value: Literal["EPSG:31370"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setattr__(self, /, name: str, value: Literal["coords"]):
        """
        usage.geopandas: 1
        """
        ...

    def __setattr__(self, /, name: str, value: object):
        """
        usage.geopandas: 54
        """
        ...

    @overload
    def __setitem__(
        self, /, key: Literal["geometry"], value: geopandas.array.GeometryArray
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setitem__(self, /, key: int, value: int):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setitem__(
        self, /, key: Literal["geom2"], value: geopandas.geoseries.GeoSeries
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setitem__(
        self, /, key: Literal["geom2"], value: geopandas.array.GeometryArray
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setitem__(
        self, /, key: Literal["geom3"], value: geopandas.geoseries.GeoSeries
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setitem__(self, /, key: Literal["b"], value: pandas.core.series.Series):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setitem__(
        self, /, key: Literal["geometry"], value: geopandas.geoseries.GeoSeries
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setitem__(
        self, /, key: Literal["data"], value: pandas.core.arrays.integer.IntegerArray
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setitem__(self, /, key: Literal["value3"], value: pandas.core.series.Series):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setitem__(
        self, /, key: Literal["int64"], value: pandas.core.arrays.integer.IntegerArray
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setitem__(
        self, /, key: Literal["geom"], value: geopandas.array.GeometryArray
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setitem__(
        self, /, key: Literal["geom"], value: geopandas.geoseries.GeoSeries
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setitem__(
        self, /, key: Literal["col1"], value: geopandas.array.GeometryArray
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setitem__(
        self, /, key: Literal["geom3"], value: geopandas.array.GeometryArray
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setitem__(
        self, /, key: Literal["geom4"], value: geopandas.array.GeometryArray
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setitem__(
        self, /, key: Literal["myshapes"], value: geopandas.array.GeometryArray
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setitem__(self, /, key: Literal["dup_col"], value: pandas.core.series.Series):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setitem__(
        self, /, key: Literal["dup_col"], value: pandas.core.indexes.numeric.Int64Index
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setitem__(
        self, /, key: Literal["location"], value: geopandas.array.GeometryArray
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setitem__(
        self, /, key: Literal["geometry"], value: pandas.core.series.Series
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setitem__(
        self, /, key: Literal["buff"], value: geopandas.geoseries.GeoSeries
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setitem__(
        self, /, key: Literal["array"], value: geopandas.array.GeometryArray
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setitem__(self, /, key: Literal["geometry"], value: numpy.ndarray):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setitem__(
        self, /, key: Literal["other_geom"], value: geopandas.geoseries.GeoSeries
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setitem__(
        self, /, key: Literal["other_geom"], value: geopandas.array.GeometryArray
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setitem__(
        self, /, key: Literal["new_name"], value: geopandas.array.GeometryArray
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        /,
        key: Literal["simplified_geometry"],
        value: geopandas.geoseries.GeoSeries,
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        /,
        key: Literal["simplified_geometry"],
        value: geopandas.array.GeometryArray,
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setitem__(
        self, /, key: Literal["points"], value: geopandas.array.GeometryArray
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setitem__(self, /, key: Literal["new"], value: int):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setitem__(
        self, /, key: Literal["geom_list"], value: geopandas.array.GeometryArray
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setitem__(
        self, /, key: Literal["cats_object"], value: List[Literal["cat2", "cat1"]]
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setitem__(self, /, key: Literal["nums"], value: List[int]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setitem__(
        self, /, key: Literal["singlecat_object"], value: List[Literal["cat2"]]
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setitem__(
        self, /, key: Literal["cats"], value: pandas.core.arrays.categorical.Categorical
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        /,
        key: Literal["singlecat"],
        value: pandas.core.arrays.categorical.Categorical,
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setitem__(
        self,
        /,
        key: Literal["cats_ordered"],
        value: pandas.core.arrays.categorical.Categorical,
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setitem__(
        self, /, key: Literal["coords"], value: geopandas.array.GeometryArray
    ):
        """
        usage.geopandas: 1
        """
        ...

    def __setitem__(self, /, key: Union[str, int], value: object):
        """
        usage.geopandas: 38
        """
        ...

    @overload
    def __setstate__(
        self,
        /,
        state: Dict[
            str,
            Union[
                Literal["the_geom", "dataframe"],
                None,
                dict,
                List[str],
                pandas.core.internals.managers.BlockManager,
            ],
        ],
    ):
        """
        usage.geopandas: 2
        """
        ...

    @overload
    def __setstate__(
        self,
        /,
        state: Dict[
            str,
            Union[
                Literal["geometry", "dataframe"],
                pyproj.crs.crs.CRS,
                pandas.core.internals.managers.BlockManager,
                dict,
                List[str],
            ],
        ],
    ):
        """
        usage.geopandas: 2
        """
        ...

    @overload
    def __setstate__(
        self,
        /,
        state: Dict[
            str,
            Union[
                None,
                Literal["the_geom", "dataframe"],
                List[str],
                pandas.core.internals.managers.BlockManager,
            ],
        ],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def __setstate__(
        self,
        /,
        state: Dict[
            str,
            Union[
                pyproj.crs.crs.CRS,
                pandas.core.internals.managers.BlockManager,
                Literal["geometry", "dataframe"],
                List[str],
            ],
        ],
    ):
        """
        usage.geopandas: 1
        """
        ...

    def __setstate__(self, /, state: Dict[str, object]):
        """
        usage.geopandas: 6
        """
        ...

    def _repr_html_(self, /):
        """
        usage.geopandas: 3
        """
        ...

    @overload
    def align(self, /, other: geopandas.geodataframe.GeoDataFrame):
        """
        usage.geopandas: 5
        """
        ...

    @overload
    def align(self, /, other: pandas.core.frame.DataFrame, axis: int):
        """
        usage.geopandas: 2
        """
        ...

    def align(
        self,
        /,
        other: Union[pandas.core.frame.DataFrame, geopandas.geodataframe.GeoDataFrame],
        axis: int = ...,
    ):
        """
        usage.geopandas: 7
        """
        ...

    def assign(self, /):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def astype(
        self,
        /,
        dtype: Dict[Literal["col1"], Type[str]],
        copy: bool,
        errors: Literal["raise"],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def astype(
        self,
        /,
        dtype: Dict[Literal["value1"], Type[float]],
        copy: bool,
        errors: Literal["raise"],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def astype(self, /, dtype: Type[str], copy: bool, errors: Literal["raise"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def astype(
        self,
        /,
        dtype: Dict[Literal["geom_list"], Type[str]],
        copy: bool,
        errors: Literal["raise"],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def astype(self, /, dtype: Type[object], copy: bool, errors: Literal["raise"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def astype(
        self,
        /,
        dtype: Dict[Literal["value1"], Literal["int64"]],
        copy: bool,
        errors: Literal["raise"],
    ):
        """
        usage.geopandas: 1
        """
        ...

    def astype(
        self,
        /,
        dtype: Union[
            Dict[Literal["col1", "value1", "geom_list"], Union[type, Literal["int64"]]],
            type,
        ],
        copy: bool,
        errors: Literal["raise"],
    ):
        """
        usage.geopandas: 6
        """
        ...

    def copy(self, /):
        """
        usage.geopandas: 44
        """
        ...

    @overload
    def drop(self, /, columns: List[Literal["geometry"]]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def drop(self, /, labels: List[Literal["geometry"]], axis: int):
        """
        usage.geopandas: 2
        """
        ...

    @overload
    def drop(self, /, labels: List[Literal["geom2"]], axis: int):
        """
        usage.geopandas: 2
        """
        ...

    @overload
    def drop(self, /, labels: int, axis: int):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def drop(self, /, labels: List[Literal["the_geom"]], axis: int):
        """
        usage.geopandas: 2
        """
        ...

    @overload
    def drop(self, /, labels: List[Literal["geom"]], axis: int):
        """
        usage.geopandas: 2
        """
        ...

    @overload
    def drop(self, /, labels: Literal["myshapes"], axis: int):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def drop(self, /, labels: Literal["geometry"], axis: int):
        """
        usage.geopandas: 4
        """
        ...

    @overload
    def drop(self, /, labels: List[Literal["other_geom"]], axis: int):
        """
        usage.geopandas: 2
        """
        ...

    def drop(
        self,
        /,
        labels: Union[
            List[Literal["geometry", "geom2", "the_geom", "geom", "other_geom"]],
            int,
            Literal["geometry", "myshapes"],
        ] = ...,
        axis: int = ...,
    ):
        """
        usage.geopandas: 17
        """
        ...

    @overload
    def drop_duplicates(self, /, subset: Literal["geometry"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def drop_duplicates(self, /):
        """
        usage.geopandas: 1
        """
        ...

    def drop_duplicates(self, /, subset: Literal["geometry"] = ...):
        """
        usage.geopandas: 2
        """
        ...

    @overload
    def fillna(self, /, value: shapely.geometry.point.Point):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def fillna(self, /, value: int):
        """
        usage.geopandas: 2
        """
        ...

    def fillna(self, /, value: Union[int, shapely.geometry.point.Point]):
        """
        usage.geopandas: 3
        """
        ...

    @overload
    def groupby(self, /, by: Literal["manhattan_bronx"]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def groupby(self, /, by: Literal["manhattan_bronx"], group_keys: bool):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def groupby(self, /, by: List[Literal["dup_col", "manhattan_bronx"]]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def groupby(
        self, /, by: List[Literal["dup_col", "manhattan_bronx"]], group_keys: bool
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def groupby(self, /, by: Literal["value2"]):
        """
        usage.geopandas: 5
        """
        ...

    def groupby(
        self,
        /,
        by: Union[
            Literal["value2", "manhattan_bronx"],
            List[Literal["dup_col", "manhattan_bronx"]],
        ],
        group_keys: bool = ...,
    ):
        """
        usage.geopandas: 9
        """
        ...

    def iterrows(self, /):
        """
        usage.geopandas: 1
        """
        ...

    def join(self, /, other: geopandas.geodataframe.GeoDataFrame):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def reindex(self, /, index: List[int]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def reindex(self, /, columns: List[Literal["geometry", "value1"]]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def reindex(self, /, columns: List[Literal["geometry", "value2", "value1"]]):
        """
        usage.geopandas: 1
        """
        ...

    def reindex(
        self,
        /,
        columns: List[Literal["geometry", "value1", "value2"]] = ...,
        index: List[int] = ...,
    ):
        """
        usage.geopandas: 3
        """
        ...

    def reindex_like(self, /, other: geopandas.geodataframe.GeoDataFrame):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def rename(self, /, columns: Callable):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def rename(self, /, columns: Dict[Literal["geometry"], Literal["geom"]]):
        """
        usage.geopandas: 4
        """
        ...

    @overload
    def rename(self, /, columns: Dict[Literal["geom"], Literal["geom2"]]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def rename(self, /, columns: Dict[Literal["col1"], Literal["column1"]]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def rename(self, /, columns: Dict[Literal["geometry"], Literal["new_name"]]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def rename(
        self, /, columns: Dict[Literal["geometry"], Literal["new_name"]], inplace: bool
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def rename(self, /, columns: Dict[Literal["geometry"], Literal["other_geom"]]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def rename(self, /, columns: Dict[Literal["level_1"], Literal["__level_1"]]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def rename(self, /, columns: Dict[Literal["__level_1"], Literal["level_1"]]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def rename(self, /, columns: Dict[Literal["geometry"], Literal["points"]]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def rename(self, /, columns: Dict[Literal["geometry"], Literal["geom_list"]]):
        """
        usage.geopandas: 1
        """
        ...

    def rename(
        self,
        /,
        columns: Union[
            Dict[Literal["geometry", "geom", "col1", "level_1", "__level_1"], str],
            Callable,
        ],
        inplace: bool = ...,
    ):
        """
        usage.geopandas: 14
        """
        ...

    @overload
    def reset_index(self, /, drop: bool):
        """
        usage.geopandas: 2
        """
        ...

    @overload
    def reset_index(self, /):
        """
        usage.geopandas: 2
        """
        ...

    def reset_index(self, /, drop: bool = ...):
        """
        usage.geopandas: 4
        """
        ...

    def select_dtypes(self, /, include: List[Type[numpy.number]]):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["iso_a3"]):
        """
        usage.geopandas: 2
        """
        ...

    @overload
    def set_index(self, /, keys: int):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def set_index(self, /, keys: List[Literal["value2", "value1"]], inplace: bool):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def set_index(
        self,
        /,
        keys: List[Union[Literal["dup_col"], pandas.core.indexes.numeric.Int64Index]],
    ):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def set_index(self, /, keys: Literal["level_1"], append: bool, inplace: bool):
        """
        usage.geopandas: 1
        """
        ...

    @overload
    def set_index(self, /, keys: pandas.core.indexes.multi.MultiIndex):
        """
        usage.geopandas: 2
        """
        ...

    def set_index(
        self,
        /,
        keys: Union[
            pandas.core.indexes.multi.MultiIndex,
            int,
            List[
                Union[
                    Literal["value2", "value1", "dup_col"],
                    pandas.core.indexes.numeric.Int64Index,
                ]
            ],
            Literal["level_1", "iso_a3"],
        ],
        append: bool = ...,
        inplace: bool = ...,
    ):
        """
        usage.geopandas: 8
        """
        ...

    def sum(self, /):
        """
        usage.geopandas: 1
        """
        ...

    def take(self, /, indices: numpy.ndarray, axis: int):
        """
        usage.geopandas: 4
        """
        ...

    def to_csv(self, /, index: bool):
        """
        usage.geopandas: 1
        """
        ...

    def to_pickle(self, /, path: str):
        """
        usage.geopandas: 2
        """
        ...
