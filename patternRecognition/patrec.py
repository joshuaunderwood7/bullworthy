import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import numpy as np
from decimal import Decimal


def graphRawFx():
    date,bid,ask = np.loadtxt('./data/GBPUSD1d.txt', unpack=True,
            delimiter=',',
            converters={0:mdates.strpdate2num('%Y%m%d%H%M%S')})
    fig = plt.figure(figsize=(10,7))
    ax1 = plt.subplot2grid((40,40), (0,0), rowspan=40, colspan=40)

    ax1.plot(date, bid)
    ax1.plot(date, ask)
    plt.gca().get_yaxis().get_major_formatter().set_useOffset(False)

    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))
    for label in ax1.xaxis.get_ticklabels():
            label.set_rotation(45)

    ax1_2 = ax1.twinx()
    ax1_2.fill_between(date, 0, (ask-bid), facecolor='g', alpha=.3)

    plt.subplots_adjust(bottom=.23)

    plt.grid(True)
    plt.show()

def percentChange(startPoint, currentPoint):
    return ((Decimal(currentPoint)-Decimal(startPoint))/Decimal(startPoint))*100



def main():
    #graphRawFx()

if __name__=='__main__':
    main()
