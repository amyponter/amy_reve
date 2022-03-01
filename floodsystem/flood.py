from floodsystem.station import MonitoringStation
#from floodsystem.stationdata import *


##Task 2B
def stations_level_over_threshold(stations, tol):
    station_list = []
    
    for station in stations:
        if station.relative_water_level() is not None and station.relative_water_level() > tol:
            station_list += [(station.name, station.relative_water_level())]
        else:
            pass


    return sorted(station_list, key = lambda b: b[1], reverse=True)

##Task 2C
def stations_highest_rel_level(stations, N):
    stat = []
    for station in stations:
        if station.relative_water_level() != None:
            stat += [station]
        else:
            pass
    stations_ordered = sorted(stat, key=lambda b:b.relative_water_level(), reverse=True)

    stat_names_ordered = []

    for stat in stations_ordered:
        stat_names_ordered += [(stat.name,stat.relative_water_level())]
    
    return stat_names_ordered[0:N]
    #return stations_ordered[0:N]