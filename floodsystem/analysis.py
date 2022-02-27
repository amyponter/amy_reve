import matplotlib
import numpy as np
import matplotlib.pyplot as plt

def polyfit(dates, levels, p):

    x = matplotlib.dates.date2num(dates)
    y = levels
    p_coeff = np.polyfit(x - x[0], y, p)
    poly = np.poly1d(p_coeff)

    return poly, x[0]

   # plt.plot(dates, y, '.')

    #x1 = np.linspace(x[0], x[-1], 30)
    #plt.plot(x1, poly(x1 - x[0]))
    #plt.show()


