from floodsystem import stationdata, datafetcher, station
stations = stationdata.build_station_list()
stationdata.update_water_levels(stations)

#Empty lists for each of the risk categories
severe_level_station = []
high_level_station = []
moderate_level_station = []
low_level_station = []

for station in stations: #Sorts out stations into different levels
    level = station.relative_water_level()
    if level is not None:
        if level > 1.2: 
            severe_level_station.append(station)
        elif level > 0.9:
            high_level_station.append(station)
        elif level > 0.7:
            moderate_level_station.append(station)
        else:
            low_level_station.append(station)
    #sets for the different categories
    severe_town = {x.town for x in severe_level_station}
    high_town = {x.town for x in high_level_station}
    moderate_town = {x.town for x in moderate_level_station}
    low_town = {x.town for x in low_level_station}

for town in severe_town:
    print(town)