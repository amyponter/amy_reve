from floodsystem.utils import sorted_by_key  # noqa
from haversine import haversine
from floodsystem.stationdata import build_station_list
import floodsystem.datafetcher
from floodsystem.station import MonitoringStation
from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

def test_stations_by_distance():
    stations = build_station_list()
    p = (52.2053, 0.1218)
    x = stations_by_distance(stations, p)

    assert x[0][2] < x[1][2]
    
    assert type(x[0]) == tuple
    assert type(x[0][1]) == str
    assert type(x[0][2]) == tuple


#def test_stations_within_radius():
 #   stations = build_station_list()
  #  station_distances = stations_within_radius(stations, (52.2053, 0.1218), 10)
   # assert isinstance(station_distances[0], MonitoringStation)

#def test_rivers_with_station():
 #   stations = build_station_list()
  #  river_test = rivers_with_station(stations)
   # assert "River Aire" in river_test

#def test_stations_by_river():
 #   stations = build_station_list()
  #  river_test = stations_by_river(stations)
   # assert "River Aire" in river_test



