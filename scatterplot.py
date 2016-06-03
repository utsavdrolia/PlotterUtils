from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d


def scatter_plot(x, y, xlabel, ylabel, xlim, ylim, title, flag):
    """
    :param xlabel: Label for x axis
    :param y1label: Label for y1 axis
    :param title: Title of plot
    :param flag: Save to Pdf?
    :return:
    """
    fig, ax1 = plt.subplots(figsize=(10.24, 5.12))
    plot1 = ax1.scatter(x, y)
    ax1.set_ylabel(ylabel)
    # ax1.set_ylim(y1lim)
    ax1.set_xlabel(xlabel)

    xmin = (3 * x[0] - x[1]) / 2.
    xmax = (3 * x[-1] - x[-2]) / 2.
    # plt.xlim(xmin, xmax)
    plt.title(title)

    if flag is True:
        pdf = PdfPages(title + ".pdf")
        plt.savefig(pdf, format='pdf', bbox_inches='tight')
        pdf.close()
    plt.show()


def scatter_plot_multi(xarr, yarr, xlabel, ylabel, legend, xlim, ylim, title, flag):
    """
    :param xlabel: Label for x axis
    :param y1label: Label for y1 axis
    :param title: Title of plot
    :param flag: Save to Pdf?
    :return:
    """
    colors = [(0.5,0.5,.8), (0.5,.8,0.5), (.8,0.5,0.5), (0.5,.8,.8), (0.8,.8,0.5), (.8,.8,.8)]
    count = 0
    for x, y in zip(xarr, yarr):
        plot1 = plt.scatter(x, y, color=colors[count])
        # trend = np.poly1d(np.polyfit(x, y, 1))
        # plot1 = plt.plot(x, trend(x), color=colors[count])
        count += 1
    
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.title(title)
    plt.legend(legend)
    if flag is True:
        pdf = PdfPages(title + ".pdf")
        plt.savefig(pdf, format='pdf', bbox_inches='tight')
        pdf.close()
    plt.show()


