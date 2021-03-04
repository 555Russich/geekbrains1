import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

g = 9.806
s = 16
v = 12
alpha = 36.35388 * np.pi / 180

start_place = [0, 2]
x0 = start_place[0]
y0 = start_place[1]
target = [10, 4]
hit = [0, 0]

t = round(s / v * np.cos(alpha), 2)
# t = 0
x = round(x0 + v * t * np.cos(alpha), 2)
y = round(y0 + v * t * np.sin(alpha) - (t ** 2) * g / 2, 2)
print('t:', t); print('x:', x); print('y:', y)
tar = np.arange(0, t, 0.01)

hit[0] = x
hit[1] = y
if target == hit:
    print('hitted')
else:
    print('missed')

# def plot_trace(file=None, **kwargs):
#     xar = x0 + v * np.cos(alpha) * tar
#     yar = y0 + v * np.sin(alpha) * tar - g * (tar**2) / 2
#     plt.figure(figsize=(20, 30))
#     plt.plot(xar, yar, **kwargs)
#     plt.xlim([0, x0 + np.max(x) * 1.2])  # x0 + np.max(x)
#     plt.ylim([0, y0 + np.max(y) * 1.2])  # y0 + np.max(y)
#     plt.xlabel('X', fontsize=24)
#     plt.ylabel('Y', fontsize=24)
#     plt.title(f'', fontsize=32)
#     plt.grid(True)
#     if 'label' in kwargs:
#         plt.legend(loc='best', fontsize=32)
#
#     if file is not None:
#         plt.savefig(file)
# plot_trace(label='trace', color='g')
# plt.show()

fig, ax = plt.subplots()

tan = np.arange(0, 0.1, 0.01)  # time of flight into an array
xan = np.arange(0, 0.1, 0.01)
ax.scatter(target[0], target[1], c = 'red')
line, = ax.plot(xan, v * np.sin(alpha) * xan - (0.5) * g * xan**2)   # plot of x and y in time

def animate(i):
    """change the divisor of i to get a faster (but less precise) animation """
    line.set_xdata( x0 + (v * np.cos(alpha) * (tan + i /10.0)))
    line.set_ydata( y0 + (v * np.sin(alpha) * (xan + i /10.0) - (0.5) * g * (xan + i / 10.0)**2))
    return line,

plt.axis([0.0, 10.0, 0.0, 5.0])
ax.set_autoscale_on(False)

ani = animation.FuncAnimation(fig, animate, np.arange(1, 200))
plt.show()

