import passiogo
import time

USU_CAMPUS_BUS = 3499
system = passiogo.getSystemFromID(USU_CAMPUS_BUS)

SOUTH_CAMPUS_EXPRESS_OLD = '38768'
SOUTH_CAMPUS_EXPRESS = '53861'
HOUSING_EXPRESS = '38765'
tracked_routes = {SOUTH_CAMPUS_EXPRESS, HOUSING_EXPRESS}

def vehicle_summary(vehicle):
    return f"{vehicle.id}/{vehicle.routeId}@{vehicle.latitude};{vehicle.longitude}"

while True:
    vehicles = system.getVehicles()
    timestamp = str(time.time())
    # filtered_vehicles = filter(lambda a: a.routeId in tracked_routes, vehicles)
    readable = [vehicle_summary(vehicle) for vehicle in vehicles]
    readable.insert(0, timestamp)
    print(*readable, sep=',', flush=True)
    time.sleep(10)