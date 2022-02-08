# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine
from floodsystem.stationdata import build_station_list
from . import datafetcher
from .station import MonitoringStation

#B

def stations_by_distance(stations, p):
    names = []
    towns = []
    distance = []
    for station in stations:
        names.append(station.name)
        towns.append(station.town)
        distance.append(haversine(p, station.coord))
    tpls = list(zip(names, towns, distance))
    tpls = sorted_by_key(tpls,2)
    return tpls

#C

def stations_within_radius(stations, centre, r):
    names = []
    for station in stations:
        if haversine(centre, station.coord) <= r:
            names.append(station.name)
        else:
            pass
    return names

#D

def rivers_with_station(stations):
    rivers = set()
    for station in stations:
        rivers.add(station.river)
    return sorted(list(rivers))

def duplicate_check(list):
    if len(list) == len(set(list)):
        return False
    else:
        return True

def stations_by_river(stations):
    rivers_dict = {}
    for station in stations:
        rivers_dict[station.river] = None

    for river in rivers_dict:
        river_station = []
        for station in stations:
            if station.river == river:
                river_station += [station.name]

        rivers_dict[river] = river_station

    return (rivers_dict)

#E
def rivers_by_station_number(stations, N):
    rivers = []
    for station in stations:
        rivers = rivers + [station.river]
    rivers = set(rivers)
    
    #list of stations for every river
    rivers_with_station = []
    for river in rivers:
        station_num = 0
        for station in stations:
            if station.river == river:
                station_num += 1
        rivers_with_station.append((river,station_num))

    sorted_rivers_with_stations = sorted(rivers_with_station, reverse = True, key= lambda i:i[1] )

    largest = sorted_rivers_with_stations[:N]

    for river in sorted_rivers_with_stations[N:]:
        nth_river = largest[N-1]
        if river[1] == nth_river[1]:
            largest += [river]
    
        
    print(len(largest))
    return largest







