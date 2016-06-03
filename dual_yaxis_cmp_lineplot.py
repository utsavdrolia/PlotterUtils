from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d


def dual_yaxis_cmp_plot(y1arr, y2arr, x, y1label, y2label, xlabel, y1lim, y2lim, title, legend, flag):
    """
    :param ticks: Labels for ticks on x axis
    :param xlabel: Label for x axis
    :param y1label: Label for y1 axis
    :param y2label: Label for y2 axis
    :param title: Title of plot
    :param flag: Save to Pdf?
    :return:
    """
    colors = [(0.5,0.5,.8), (0.5,.8,0.5), (.8,0.5,0.5), (0.5,.8,.8), (0.8,.8,0.5), (.8,.8,.8)]
    count = 0
    fig, ax1 = plt.subplots(figsize=(10.24, 5.12))
    for y1, y2 in zip(y1arr, y2arr):
        y1, std_y1 = zip(*y1)
        y2, std_y2 = zip(*y2)
        y1 = list(y1)
        y2 = list(y2)
        std_y1 = list(std_y1)
        std_y2 = list(std_y2)

        plot1 = ax1.errorbar(x, y1, yerr=std_y1, color=colors[count], fmt='--o')
        ax1.set_ylabel(y1label)
        ax1.set_ylim(y1lim)
        ax1.set_xlabel(xlabel)

        ax2 = ax1.twinx()
        plot2 = ax2.errorbar(x, y2, yerr=std_y2, color=colors[count], fmt='-.^')
        ax2.set_ylabel(y2label)
        ax2.set_ylim(y2lim)

        count += 1

    xmin = (3 * x[0] - x[1]) / 2.
    xmax = (3 * x[-1] - x[-2]) / 2.
    plt.xlim(xmin, xmax)
    plt.legend(legend, loc=0)
    plt.title(title)

    if flag is True:
        pdf = PdfPages(title + ".pdf")
        plt.savefig(pdf, format='pdf', bbox_inches='tight')
        pdf.close()
    plt.show()
