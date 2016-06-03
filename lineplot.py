from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import numpy as np


def lineplot(cr, di, ticks, xlabel, ylabel, title, flag, saveas ,cr_legend, di_legend):
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
    fig, ax = plt.subplots()
    if isinstance(cr, list) and isinstance(di, list):
        if len(cr) == len(di) and len(cr) == len(ticks):
            N = len(cr)
        else:
            print("Lengths not same")
            return None
    else:
        print("Both need to be lists")
        return None

    cr_means, cr_stds = zip(*cr)
    di_means, di_stds = zip(*di)
    ind = np.arange(N)
    bar1 = ax.errorbar(ticks, cr_means, color='r', fmt='--o', yerr=cr_stds, linewidth=2.0)
    bar2 = ax.errorbar(ticks, di_means, color='b', fmt='-.^', yerr=di_stds, linewidth=2.0)

    xmin = (3*ticks[0] - ticks[1])/2.
    # shaft half a step to the right
    xmax = (3*ticks[-1] - ticks[-2])/2.
    plt.xlim(xmin, xmax)
    plt.ylim(0, max(max(cr_means) + max(cr_stds), max(di_means) + max(di_stds)))
    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)
    ax.set_xticks(ticks)
    ax.set_xticklabels(ticks)
    ax.legend((bar1[0], bar2[0]), (cr_legend, di_legend), loc=0)
    if flag is True:
        pdf = PdfPages(saveas + ".pdf")
        plt.savefig(pdf, format='pdf', bbox_inches='tight')
        pdf.close()
    else:
        plt.show()
