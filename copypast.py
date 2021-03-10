import matplotlib.pyplot as plt
import numpy as np
# from jupyterthemes import jtplot
#
# jtplot.style('onedork')

g = 9.8066
v0 = 12
alpha = 0.5

def plot_trace(v0, alpha, file=None, **kwargs):
    # acceleration of gravity
    # time to max height
    tp = v0 * np.sin(alpha) / g
    # converting to time range
    t = np.arange(0, 2 * tp, 0.01)
    # x axis
    x = v0 * np.cos(alpha) * t
    # y axis
    y = v0 * np.sin(alpha) * t - g * (t**2) / 2
    # change size for figure
    plt.figure(figsize=(30, 50))
    plt.plot(x, y, **kwargs)
    # xlim
    plt.xlim([0, np.max(x) * 1.1])
    # ylim
    plt.ylim([0, np.max(y) * 1.1])
    # axis labels
    plt.xlabel('X', fontsize=24)
    plt.ylabel('Y', fontsize=24)
    # chart title
    plt.title(f'', fontsize=32)
    plt.grid(True)
    # set legend
    if 'label' in kwargs:
        plt.legend(loc='best', fontsize=32)

    if file is not None:
        plt.savefig(file)
# if __name__ == '__main__':
plot_trace(v0, alpha, label='trace', color='g')