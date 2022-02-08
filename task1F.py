from floodsystem.station import inconsistant_typical_range_stations
from floodsystem.stationdata import build_station_list
from floodsystem import station 


station_data = build_station_list()
print(inconsistant_typical_range_stations(station_data))