
#from floodsystem import flood, station, stationdata
from cProfile import label
from floodsystem.geo import stations_by_distance
from floodsystem.station import MonitoringStation
from haversine import haversine
from floodsystem.flood import *

station1 = MonitoringStation(station_id='stat1',
                             river='riv1',
                             measure_id='test_measure_id_1',
                             label='Station 1',
                             coord=(4., 5.),
                             typical_range=(0., 1.),
                             town='town1')
station2 = MonitoringStation(station_id='stat2',
                             measure_id='test_measure_id_1',
                             label='Station 2',
                             coord=(4., 5.),
                             typical_range=(0., 1.),
                             river='riv2',
                             town='town2')
station3 = MonitoringStation(station_id='stat3',
                             measure_id='test_measure_id_1',
                             label='Station 3',
                             coord=(4., 5.),
                             typical_range=(0., 1.),
                             river='riv1',
                             town='town3')
station4 = MonitoringStation(station_id='stat4',
                             river='riv1',
                             measure_id='test_measure_id_1',
                             label='Station 4',
                             coord=(4., 5.),
                             typical_range=(0., 1.),
                             town='town4')
station5 = MonitoringStation(station_id='stat5',
                             measure_id='test_measure_id_1',
                             label='Station 5',
                             coord=(4., 5.),
                             typical_range=(0., 1.),
                             river='riv5',
                             town='town5')
station6 = MonitoringStation(station_id='stat6',
                             measure_id='test_measure_id_1',
                             label='Station 6',
                             coord=(4., 5.),
                             typical_range=(0., 1.),
                             river='riv6',
                             town='town6')       
station7 = MonitoringStation(station_id='stat6',
                             measure_id='test_measure_id_1',
                             label='Station 6',
                             coord=(4., 5.),
                             typical_range=None,
                             river='riv6',
                             town='town6')          


station1.latest_level = 0.5
station2.latest_level = 0.6
station3.latest_level = 0.7
stations = [station1,station2,station3,station4]

def test_stations_level_over_threshold():
    stations = [station1,station2,station3,station4]
    assert stations_level_over_threshold(stations,0.6) == [(station3.name, 0.7)]
    assert stations_level_over_threshold(stations,0.5) == [(station3.name, 0.7), (station2.name, 0.6)]



def test_stations_highest_rel_level():
    assert stations_highest_rel_level(stations,3) == [(station3.name,station3.relative_water_level()), (station2.name, station2.relative_water_level()), (station1.name, station1.relative_water_level())]
    assert stations_highest_rel_level(stations,2) == [(station3.name,station3.relative_water_level()), (station2.name, station2.relative_water_level())]
    assert stations_highest_rel_level(stations,1) == [(station3.name,station3.relative_water_level())]