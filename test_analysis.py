from os import times
import pytest
import datetime
from matplotlib import dates
from floodsystem import analysis
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
import numpy as np

stations = build_station_list()
update_water_levels(stations)

def test_analysis():
    dt = 10 
    times, levels = fetch_measure_levels(stations[0].measure_id, dt=datetime.timedelta(days=dt))
    x = dates.date2num(times)

    poly, first_date = analysis.polyfit(times, levels, 2)
    assert first_date == x[0]
    assert isinstance(poly, np.poly)