import scipy
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
from scipy import signal


def traceplot(cr, tickscr, dr, ticksdr, xlabel, ylabel, title, flag, legend):
    '''

    :param cr: crowd items (tuples of mean and std) to plot. If a list, should be same size as :param di
    :param di: direct items (tuples of mean and std) to plot.If a list, should be same size as :param cr
    :param ticks: Labels for ticks on x axis
    :param xlabel: Label for x axis
    :param ylabel: Label for y axis
    :param title: Title of plot
    :param flag: Save to Pdf?
    :return:
    '''

    cr = np.cumsum(cr)
    dr = np.cumsum(dr)

    func = interp1d(tickscr, cr)
    fund = interp1d(ticksdr, dr)

    maxticks = min(tickscr[-1], ticksdr[-1])
    maxticks = 3300
    ticks = range(long(maxticks))

    cont_cr = func(ticks)
    cont_dr = fund(ticks)

    # cr_peaks = peaks(cont_cr, max(cr)/10)
    # dr_peaks = peaks(cont_dr, max(dr)/10)
    fig, ax = plt.subplots(figsize=(10.24, 5.12))
    ax.plot(ticks, cont_cr, 'r', ticks, cont_dr, 'b',
            linewidth=2.0)  # , cr_peaks, cont_cr[cr_peaks], 'ro', dr_peaks, cont_dr[dr_peaks], "bs")

    xmin = (3 * ticks[0] - ticks[1]) / 2.
    # shaft half a step to the right
    xmax = (3 * ticks[-1] - ticks[-2]) / 2.
    plt.ylim(0, 110)
    plt.xlim(xmin, xmax)
    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)
    ax.legend(("CrowdFilter", "Baseline"), loc=2)  # , "CrowdFilter Peaks", "Baseline Peaks"))
    # ax.set_xticks(ticks)
    # ax.set_xticklabels(ticks)
    # ax.set_yscale('log')
    if flag is True:
        pdf = PdfPages(title + ".pdf")
        plt.savefig(pdf, format='pdf')
        pdf.close()
    else:
        plt.show()


def peaks(data, min):
    return [time for time in signal.argrelmax(data, order=1000)[0] if data[time] > min]
