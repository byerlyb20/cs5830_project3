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

SYSTEM_STOPS = [
    ('Public Safety', (-111.812388131, 41.754533657), {'38764'}),
    ('Center Stadium', (-111.813083561, 41.752851769), {'38764', '38772'}),
    ('South Stadium', (-111.81307018, 41.750570122), {'38764', '38772'}),
    ('Taggart Student Center', (-111.813960182, 41.743714774), {'38764', '38772', '50063', '53861', '38768', '56194', '61652'}),
    ('Field House', (-111.8134483, 41.74445999), {'38765'}),
    ('Veterinary Science', (-111.8110267, 41.744432), {'38765'}),
    ('Industrial Science', (-111.808262326, 41.744343979), {'38765', '38772', '61652'}),
    ('Aggie Ice Cream', (-111.80430747, 41.745159696), {'38765', '38772'}),
    ('Lundstrum', (-111.802081881, 41.749617062), {'38765', '38772', '53861', '38768'}),
    ('Aggie Village 1', (-111.804389116, 41.750817743), {'38765'}),
    ('Aggie Village 2', (-111.806060476, 41.75307753), {'38765', '38772'}),
    ('Aggie Village 3', (-111.809274072, 41.751605001), {'38765'}),
    ('800 E 900 N', (-111.814078833, 41.748601779), {'38765', '38772'}),
    ('800 E 1250 N Crossing', (-111.813527686, 41.755104011), {'38772'}),
    ('Blue Square Apartments', (-111.813955385, 41.75159571), {'38772', '50063'}),
    ('West Stadium', (-111.813881118, 41.751683139), {'50063', '72975'}),
    ('ASTE Bldg', (-111.813820422, 41.758878976), {'50063', '56194'}),
    ('Oakridge Apartments', (-111.813913384, 41.756462812), {'50063'}),
    ('The Bull', (-111.813282805, 41.750053756), {'53861', '38768'}),
    ('Logan Cemetery', (-111.805868979, 41.749962755), {'53861', '38768'}),
    ('Fine Arts Bldg', (-111.8043394, 41.74344203), {'53861', '38768'}),
    ('Family Life Bldg', (-111.811128394, 41.74007151), {'53861', '38768'}),
    ('670 E 500 N', (-111.8176719, 41.74060939), {'53861', '38768'}),
    ('Innovation Visitor Center', (-111.817828264, 41.761290882), {'56194'}),
    ('Innovation Campus', (-111.819979396, 41.762193842), {'56194'}),
    ('USTAR Bldg', (-111.817237, 41.76110498), {'56194'}),
    ('Water Lab', (-111.792734741, 41.739962091), {'61652'}),
    ('650 N 1200 E', (-111.80426, 41.74343), {'61652'}),
    ('Richards Hall', (-111.8081033, 41.74445859), {'61652', '72975'}),
    ('Veterinary Medicine BLDG', (-111.805770091, 41.75824945), {'72975'}),
    ('Aggie Village 1200 East', (-111.804493386, 41.751619106), {'72975'}),
    ('CCA BLDG', (-111.805440431, 41.744401791), {'72975'}),
    ('Education Bldg', (-111.8109409, 41.74447595), {'72975'}),
    ('Aggie Rec Center', (-111.8131125, 41.74455757), {'72975'})
]

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