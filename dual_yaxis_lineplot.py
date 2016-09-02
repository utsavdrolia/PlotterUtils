from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d


def dual_yaxis_plot(y1, y2, x, y1label="", y2label="", xlabel="", y1lim=None, y2lim=None, title="", legend=None, flag=False):
    """
    :param ticks: Labels for ticks on x axis
    :param xlabel: Label for x axis
    :param y1label: Label for y1 axis
    :param y2label: Label for y2 axis
    :param title: Title of plot
    :param flag: Save to Pdf?
    :return:
    """

    # func_y1 = interp1d(x, y1)
    # func_y2 = interp1d(x, y2)

    # maxticks = x[-1]
    # ticks = range(long(maxticks))

    # cont_y1 = func_y1(ticks)
    # cont_y2 = func_y2(ticks)
    std_y1 = None
    std_y2 = None
    if isinstance(y1[0], tuple):
        y1, std_y1 = zip(*y1)
        y1 = list(y1)
        std_y1 = list(std_y1)

    if isinstance(y2[0], tuple):
        y2, std_y2 = zip(*y2)
        y2 = list(y2)
        std_y2 = list(std_y2)

    fig, ax1 = plt.subplots(figsize=(10.24, 5.12))
    plot1 = ax1.errorbar(x, y1, yerr=std_y1, color='g', linewidth=2.0, label="x1")
    ax1.set_ylabel(y1label)
    ax1.set_xlabel(xlabel)

    if y1lim:
        ax1.set_ylim(y1lim)

    ax2 = ax1.twinx()
    plot2 = ax2.errorbar(x, y2, yerr=std_y2, color='b', linewidth=2.0, label="x2")
    ax2.set_ylabel(y2label)

    if y2lim:
        ax2.set_ylim(y2lim)

    xmin = (3 * x[0] - x[1]) / 2.
    xmax = (3 * x[-1] - x[-2]) / 2.
    plt.xlim(xmin, xmax)

    if legend:
        plt.legend((plot1[0], plot2[0]), legend, loc=0)
    if flag is True:
        pdf = PdfPages(title + ".pdf")
        plt.savefig(pdf, format='pdf', bbox_inches='tight')
        pdf.close()
    plt.show()
    return ax1, plt
