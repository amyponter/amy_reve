from re import S
from floodsystem import geo
from floodsystem.stationdata import build_station_list


N = 9
stations = build_station_list()
S = geo.rivers_by_station_number(stations, N)
print(S)
#if __name__ == "__main__":
 #   print("*** Task 1E: CUED Part IA Flood Warning System ***")
 #   run()