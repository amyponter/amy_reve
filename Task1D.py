from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

def run():
    # Build list of stations
    stations = build_station_list()

    x = rivers_with_station(stations)
    print(len(rivers_with_station(stations)), "stations")
    print(x[:10])

    print("River Aire:", sorted(stations_by_river(stations)['River Aire']))
    print("River Cam:", sorted(stations_by_river(stations)['River Cam']))
    print("River Thames:", sorted(stations_by_river(stations)['River Thames']))


if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()

