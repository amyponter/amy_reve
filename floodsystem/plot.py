
from . import datafetcher
from .station import MonitoringStation
import datetime
import matplotlib.pyplot as plt
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.analysis import polyfit
import matplotlib
import numpy as np
def plot_water_levels(station, dates, levels):

    typical_range = station.typical_range
     
    low_levels = [typical_range[0]]*len(dates)
    high_levels = [typical_range[1]]*len(dates)
     
    plt.plot(dates,low_levels, label = "low range")
    plt.plot(dates,high_levels, label = "high range")  
    plt.plot(dates, levels)

    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)

    plt.tight_layout()  

    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    
    x = matplotlib.dates.date2num(dates)
    x1 = np.linspace(x[0], x[-1], 50)
    typical_range = station.typical_range
     
    low_levels = [typical_range[0]]*len(dates)
    high_levels = [typical_range[1]]*len(dates)
     
    plt.plot(dates,low_levels, label = "low range")
    plt.plot(dates,high_levels, label = "high range")  
    #plt.plot(plot_water_level_with_fit, polyfit)
    plt.plot(dates, levels)

    poly_line = polyfit(dates, levels, p)
    y = poly_line[0]
    plt.plot(x1, y(x1 - x[0]))

    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)

    plt.tight_layout()  

    plt.show()
