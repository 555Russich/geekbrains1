import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

g = 9.806
h = 4
s = 10
v = 12
alpha = 35.535 * np.pi / 180  # 35.535  # 90(!) # 0 (!)

if alpha == 0 or alpha == np.pi / 2:
    print('missed')
    exit()
elif np.pi / 2 < alpha < 2 * np.pi:
    print('are you blind?')
    exit()

start_place = [0, 2]
x0 = start_place[0]
y0 = start_place[1]
target = [10, 4]
hit = [0, 0]

t = s / (v * np.cos(alpha))
# t = 0
x = x0 + (v * t * np.cos(alpha))
y = y0 + (v * t * np.sin(alpha)) - ((t ** 2) * g) / 2

print('t:', round(t, 2)); print('x:', round(x, 2)); print('y:', round(y, 2))
tar = np.arange(0, t, 0.01)
alpha_min = np.arctan(h/s) * 180 / np.pi
alpha_range_grad = np.arange(alpha_min, 90, 1)
alpha_range = alpha_range_grad * np.pi / 180

xhit = round(x, 2)
yhit = round(y, 2)
hit[0] = xhit
hit[1] = yhit
if target == hit:
    print('hitted')
else:
    print('missed')

def plot_trace(file=None, **kwargs):
    xar = x0 + v * np.cos(alpha) * tar
    yar = y0 + v * np.sin(alpha) * tar - g * (tar**2) / 2
    plt.figure(figsize=(10, 20))
    plt.plot(xar, yar, **kwargs)
    plt.xlim([0, x0 + np.max(x) * 1.1])  # x0 + np.max(x)
    plt.ylim([0, y0 + np.max(y) * 1.1])  # y0 + np.max(y)
    plt.xlabel('X', fontsize=24)
    plt.ylabel('Y', fontsize=24)
    plt.title(f'', fontsize=32)
    plt.scatter(10, 4)
    plt.grid(True)
    if 'label' in kwargs:
        plt.legend(loc='best', fontsize=32)

    if file is not None:
        plt.savefig(file)

    # if alpha == 0 or alpha == np.pi / 2:

plot_trace(label='trace', color='g')
plt.show()

