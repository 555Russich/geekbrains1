import matplotlib.pyplot as plt
import numpy as np

g = 9.806
h = 4
s = 10
v = 0
alpha = 35.535 * np.pi / 180  # 35.535

# v = int(input('Enter V0: '))
# alpha = float(input('Enter alpha(grad): ')) * np.pi / 180  # 35.535  # 90(!) # 0 (!)

start_place = [0, 2]
x0 = start_place[0]
y0 = start_place[1]
target = [s, h]
hit = [0, 0]

if v == 0 :
    x = 0
    y = 0
    t = np.sqrt(2 * h / g)
elif alpha == 90 * np.pi / 180:
    t = v / g
    x = 0
    y = 0
    y0 = 0
elif v != 0:
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
    plt.xlim([-1, 10 * 1.1])  # x0 + np.max(x)
    plt.ylim([0, 5 * 1.1])  # y0 + np.max(y)
    plt.xlabel('X', fontsize=24)
    plt.ylabel('Y', fontsize=24)
    if target == hit:
        plt.title('hitted', fontsize=20)
    elif np.pi / 2 < alpha < 2 * np.pi:
        plt.title('missed, wrong way', fontsize=32)
    else: plt.title('missed', fontsize=32)
    plt.scatter(s, h)
    plt.scatter(0, 2, color='r')
    plt.grid(True)
    if 'label' in kwargs:
        plt.legend(loc='best', fontsize=10)

    if file is not None:
        plt.savefig(file)


plot_trace(label='trace', color='g')
plt.show()
