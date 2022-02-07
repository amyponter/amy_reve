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

    assert len(x) > 0

    assert x[0][2] < x[1][2]
    
    assert type(x[0]) == tuple
    assert type(x[0][1]) == str
    assert type(x[0][2]) == float

    stationA = MonitoringStation(station_id='station_id_A',
                                 measure_id='measure_id_A',
                                 label='Station A',
                                 coord=(0., 1.),
                                 typical_range=(0., 1.),
                                 river='river_A',
                                 town='town_A')
    stationB = MonitoringStation(station_id='station_id_B',
                                 measure_id='measure_id_B',
                                 label='Station B',
                                 coord=(1., 1.),
                                 typical_range=(0., 1.),
                                 river='river_B',
                                 town='town_B')   
    stations = [stationA, stationB]
    sorted_stations = stations_by_distance(stations, (0., 0.)) 
    assert sorted_stations[0][0:2] == ('Station A', 'town_A')
    assert sorted_stations[0][0:2] == ('Station B', 'town_B')


def test_stations_within_radius():
    stations = build_station_list()
    centre = (52.2053, 0.1218)
    r = 10

    y = stations_within_radius(stations, centre, r)
    assert type(y[0]) == str

    stationa = MonitoringStation(station_id='station_id_a',
                                 measure_id='measure_id_a',
                                 label='Station A',
                                 coord=(0., 1.),
                                 typical_range=(0., 1.),
                                 river='river_a',
                                 town='town_a')
    stationb = MonitoringStation(station_id='station_id_b',
                                 measure_id='measure_id_b',
                                 label='Station B',
                                 coord=(1., 1.),
                                 typical_range=(0., 1.),
                                 river='river_b',
                                 town='town_b')   
    stationc = MonitoringStation(station_id='station_id_c',
                                 measure_id='measure_id_c',
                                 label='Station C',
                                 coord=(100., 100.),
                                 typical_range=(0., 1.),
                                 river='river_c',
                                 town='town_c') 
    stations = [stationa, stationb, stationc]
    stations_in_r = sorted([i.name for i in stations_within_radius(stations, (0., 0.), 200)])
    assert len(stations_in_r) == 2
    assert stations_in_r[0] == "Station A"
    assert stations_in_r[1] == "Station B"


def test_rivers_with_station():
    stations = build_station_list()
    z = rivers_with_station(stations)
    assert type(z[0]) == str

    stationa = MonitoringStation(station_id='station_id_a',
                                 measure_id='measure_id_a',
                                 label='Station A',
                                 coord=(0., 1.),
                                 typical_range=(0., 1.),
                                 river='river_a',
                                 town='town_a')
    stationb = MonitoringStation(station_id='station_id_b',
                                 measure_id='measure_id_b',
                                 label='Station B',
                                 coord=(1., 1.),
                                 typical_range=(0., 1.),
                                 river='river_b',
                                 town='town_b')   
    stationc = MonitoringStation(station_id='station_id_c',
                                 measure_id='measure_id_c',
                                 label='Station C',
                                 coord=(10., 10.),
                                 typical_range=(0., 1.),
                                 river='river_b',
                                 town='town_c') 
    stations = [stationa, stationb, stationc]
    z = rivers_with_station(stations)
    assert len(z) == 2
    assert 'river_a' in z
    assert 'river_b' in z

    no_stations_per_river = stations_by_river(stations)
    assert stations_by_river['river_b'] == [stationb, stationc]
    assert stations_by_river['river_a'] == [stationa]

def test_stations_by_river():
    stations = build_station_list()
    v = stations_by_river(stations)
    assert type(v[0]) == dict



