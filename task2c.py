from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels


def run():
    stations = build_station_list()
    update_water_levels(stations)
    high_risk_stations = stations_highest_rel_level(stations, 10)
    print(high_risk_stations)
    for station in high_risk_stations:
        print(station.name, station.relative_water_level())

run()