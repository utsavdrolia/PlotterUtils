from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d


def ecdfplot(xarr, xlabel, ylabel, legend, xlim, ylim, title, flag, saveas):
    """
    :param xlabel: Label for x axis
    :param y1label: Label for y1 axis
    :param title: Title of plot
    :param flag: Save to Pdf?
    :return:
    """
    colors = ["r", "b", (.8,0.5,0.5), (0.5,.8,.8), (0.8,.8,0.5), (.8,.8,.8)]
    count = 0
    for x in xarr:
        x = np.sort(x)
        y = np.arange(len(x))/float(len(x))
        plot1 = plt.semilogx(x, y, color=colors[count], linewidth=2)
        # trend = np.poly1d(np.polyfit(x, y, 1))
        # plot1 = plt.plot(x, trend(x), color=colors[count])
        count += 1
    
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.title(title)
    plt.legend(legend)
    if flag is True:
        pdf = PdfPages(saveas + ".pdf")
        plt.savefig(pdf, format='pdf', bbox_inches='tight')
        pdf.close()
    plt.show()


