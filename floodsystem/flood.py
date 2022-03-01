from floodsystem.station import MonitoringStation
from floodsystem.utils import sorted_by_key  # noqa
from haversine import haversine, Unit
from floodsystem.stationdata import update_water_levels, build_station_list


def stations_level_over_threshold(stations, tol):
    station_list=[]
    
    for station in stations:

        try:
            if station.relative_water_level() > tol:
                station_list.append((station.name, station.relative_water_level()))
            else: pass
        except: 
            pass

    sorted_list = sorted_by_key(station_list,1,reverse =True)

    return sorted_list
 
stations = build_station_list()

def stations_highest_rel_level(stations, N):
    """Requirements for task 2C"""
    stations_over =[]

    for station in stations:
        level = station.relative_water_level()
        
        if level != None:
                stations_over.append((station.name, level))


    station_list = sorted_by_key(stations_over,1, reverse=True)
    
    return station_list[0:N]