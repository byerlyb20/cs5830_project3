import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely import LineString
import shapely.ops
from glob import glob

__dataframes = []

for file_path in glob('*.geojson'):
    df = gpd.read_file(file_path)
    df = df.to_crs(epsg=32142)
    __dataframes.append(df)

__df = pd.concat(__dataframes, ignore_index=True)

GREEN_ROUTE = [
    [
        'way/1109090466',
        'way/1109090468',
        'way/10086405',
        'way/1343222529',
        'way/182952354',
        'way/1311629921',
        'way/1310476486',
        'way/1311629920',
        'way/1343862005',
        'way/1204279029',
        'way/1311629919',
        'way/1310476484',
    ],
    [
        'way/1204279011',
    ],
    [
        'way/1343862115',
        'way/258726226'
    ],
    [
        'way/1204279011',
    ],
    [
        'way/1305799465',
        'way/1204279032',
        'way/1310476481',
        'way/105757140',
        'way/1204279024',
        'way/10083950',
        'way/1204279014',
        'way/105757117',
        'way/1338131549',
        'way/105757122'
    ]
]

def import_route(route_segment_ids: list[list[str]]):
    segments: list[LineString] = []

    for route_segment in route_segment_ids:
        road_segments = map(
            lambda id: __df[__df['id'] == id]['geometry'].iloc[0],
            route_segment
        )
        segment: LineString = shapely.ops.linemerge(list(road_segments)) # type: ignore
        segments.append(segment)
    
    return segments