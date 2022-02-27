import datetime
from floodsystem.analysis import polyfit
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.utils import sorted_by_key

def highest_levels(stations):

    update_water_levels(stations)
    highest = []
    for station in stations:
        if station.latest_level == None: 
            pass
        elif station.latest_level >= 90:
            pass
        else:
            highest.append((station, station.latest_level))
        sortedlist = sorted_by_key(highest, 1)
        x = sortedlist[-5:]
    return x

def run():

    stations = build_station_list()

    # Sort top 5 highest levels
    top_water_levels = highest_levels(stations)
    
    
 # Fetch data over past 10 days
    dt = 2
    for i in top_water_levels:    
        dates, levels = fetch_measure_levels(i[0].measure_id, dt=datetime.timedelta(days=dt))
        plot_water_level_with_fit(i[0], dates, levels, 4)

if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()