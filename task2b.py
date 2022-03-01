
#from floodsystem import geo
#from floodsystem.stationdata import build_station_list
from floodsystem.station import *
from floodsystem.flood import stations_level_over_threshold
####
from floodsystem.stationdata import *

stations = build_station_list()
update_water_levels(stations)

#station_list = []

#for station in stations:
    #station_list += [station.relative_water_level()]

    #return sorted(station_list,1,reverse=True)
#print(station_list) 


print(stations_level_over_threshold(stations, 0.8))