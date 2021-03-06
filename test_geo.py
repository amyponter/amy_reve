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
    stations = [stationa, stationb]
    sorted_stations = stations_by_distance(stations, (0., 0.)) 
    assert sorted_stations[0][0:2] == ('Station A', 'town_a')
    assert sorted_stations[1][0:2] == ('Station B', 'town_b')


def test_stations_within_radius():
    stations = build_station_list()
    centre = (0.0, 0.0)
    r = 200


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
    output = stations_within_radius(stations, centre, r)
    assert len(output) == 2
    assert output[0] == "Station A"
    assert output[1] == "Station B"
    assert type(output) == list
    assert type(output[0]) == str

def test_rivers_with_station():
    stations = build_station_list()

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
    assert type(z) == list
    assert type(z[0]) == str

    output = stations_by_river(stations)
    assert output['river_b'] == ['Station B', 'Station C']
    assert output['river_a'] == ['Station A']




