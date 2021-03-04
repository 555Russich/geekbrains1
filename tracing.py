import matplotlib.pyplot as plt
import numpy as np
from jupyterthemes import jtplot

jtplot.style('onedork')

g = float(9.806)
s = 10
h = 4
v = 10
alpha = 31.65388

start_place = [0, 2]
x0 = start_place[0]
y0 = start_place[1]
target = [10, 4]
hit = [0, 0]


t = round(s / v * np.cos(alpha * np.pi / 180), 2)
x = round(x0 + v * t * np.cos(alpha * np.pi / 180), 2)
y = round(y0 + v * t * np.sin(alpha * np.pi / 180) - t**2 * g / 2, 2)
tp = v * np.sin(alpha * np.pi / 180) / g
print('t:', t); print('x:', x); print('y:', y); print('tp in highest place', tp)

def plot_trace(v, alpha, file=None, **kwargs):
    time = np.linspace(0, 2 * t, 1000)
    x = round(x0 + v * t * np.cos(alpha * np.pi / 180), 2)
    y = round(y0 + v * t * np.sin(alpha * np.pi / 180) - t ** 2 * g / 2, 2)
    plt.figure(figsize=(20, 10))  # change size for figure
    plt.plot(x, y, **kwargs)
    plt.xlim([-1, np.max(x) * 1.1])  # xlim
    plt.ylim([-1, np.max(y) * 1.1])  # ylim
    plt.xlabel('X', fontsize=24)  # axis labels
    plt.ylabel('Y', fontsize=24)
    plt.title(f'', fontsize=32)  # chart title
    plt.grid(True)
    if 'label' in kwargs:
        plt.legend(loc='best', fontsize=32)

    if file is not None:
        plt.savefig(file)
        plot_trace(12, 30, label='trace', color ='g')