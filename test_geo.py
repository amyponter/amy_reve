from floodsystem.utils import sorted_by_key  # noqa
from haversine import haversine
from floodsystem.stationdata import build_station_list
from . import datafetcher
from floodsystem.station import MonitoringStation
from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

#def test_stations_by_distance():
 #   stations = build_station_list()
  #  station_distances = stations_by_distance(stations, (50.000, 0.8))
   # assert isinstance(station_distances[0][1], float)
    #assert isinstance(station_distances[0][0], MonitoringStation)
    #assert sorted_by_key(station_distances, 1) == station_distances

#def test_stations_within_radius():
 #   stations = build_station_list()
  #  station_distances = stations_within_radius(stations, (52.2053, 0.1218), 10)
   # assert isinstance(station_distances[0], MonitoringStation)

def test_rivers_with_station():
    stations = build_station_list()
    river_test = rivers_with_station(stations)
    assert "River Aire" in river_test

def test_stations_by_river():
    stations = build_station_list()
    river_test = stations_by_river(stations)
    assert "River Aire" in river_test



