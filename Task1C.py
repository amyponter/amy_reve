from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

def run():
    # Build list of stations
    stations = build_station_list()
    centre = (52.2053, 0.1218)
    r = 10

    list = stations_within_radius(stations, centre, r)
    print(sorted(list))

if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()
