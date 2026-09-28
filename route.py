from shapely import LineString, Point
import shapely.ops
from functools import cached_property
import pyproj

class Route:

    __transformer = pyproj.Transformer.from_crs("EPSG:4326", "EPSG:32142", always_xy=True).transform

    def __init__(self, segments: list[LineString]):
        self.segments = segments

    @cached_property
    def base_distances(self):
        distances = [0.0]
        for i in range(0, len(self.segments) - 1):
            distances.append(distances[i] + self.segments[i].length)
        return distances
    
    def distance_marker_for(self, point: Point):
        projected_point = shapely.ops.transform(Route.__transformer, point)

        # Find the segment the point lies on (will be indecisive when the route
        # backtraces over itself)

        distance_to_segments = sorted(
            map(
                lambda a: (a[0], a[1].hausdorff_distance(projected_point)),
                enumerate(self.segments)
            ),
            key=lambda a: a[1]
        )
        nearest_distance = distance_to_segments[0][1]
        nearest_segments = filter(
            lambda a: a[1] == nearest_distance,
            distance_to_segments
        )

        # Find the distance along the route
        
        for id, _ in nearest_segments:
            segment = self.segments[id]
            distance_along_segment = segment.project(projected_point)
            yield self.base_distances[id] + distance_along_segment
