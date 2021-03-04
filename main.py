import math
import matplotlib.pyplot as plt
import numpy as np
from jupyterthemes import jtplot
# import matplotlib.animation as animation
# from tkinter import *

# math.degrees()  # радианы в градусы
# math.radians()  # градусы в радианы

g = float(9.806)
s = 2
h = 4
v = 12
alpha = 31.65388  # 31.65388
print('alpha:', alpha)
alpha_rad = math.radians(alpha)
print('alpha_rad:', alpha_rad)
alpha_min_rad = math.atan(h/s)
alpha_min = math.degrees(alpha_min_rad)
print('alpha_min:', alpha_min)
range_corner = []
for i in np.arange(alpha_min, 91, 1):
    range_corner.append(i)
print('corners range:', range_corner)


start_place = [0, 2]
x0 = start_place[0]
y0 = start_place[1]
target = [10, 4]
hit = [0, 0]

t = round(s / v * math.cos(alpha_rad), 2)
x = round(x0 + v * t * math.cos(alpha_rad), 2)
y = round(y0 + v * t * math.sin(alpha_rad) - (t**2) * g / 2, 2)
print('t:', t); print('x:', x); print('y:', y)

tt = 2 * v * math.sin(alpha_rad) / g
tp = v * math.sin(alpha_rad) / g
print('highest place in this time:', tp)

hit[0] = x
hit[1] = y
print('hitted place:', hit)

if target[1] == hit[1]:
    print('hitted')
else:
    print('missed')


# def plot_trace(v, alpha, file=None, **kwargs):



# ????????????????????????

# xtar = np.arange(0, 0.1, 0.01)
# ytar = np.arange (0, 0.1, 0.01)
# line = ax.plot(x, y)
#
#
# def animate(z):
# line.set_xdata(x)
# line.set_ydata(y)
# return line
#
# plt.axis([0.0, 10.0 , 0.0, 5.0])
# ax.set_autoscale_on(False)
#
# ani = animation.FuncAnimation(fig, animate, np.arange(1, 200))
# plt.show()


# xtar = np.arange(0, 0.1, 0.01)
# ytar = np.arange (0, 0.1, 0.01)
# line = ax.plot(x, v * math.sin(alpha_rad) * x - 0.5 * g * x**2)
#
#
# def animate(z):
# line.set_xdata(v * math.cos(alpha_rad) * (y + z / 100.0)**2)
# line.set_ydata(v * math.sin(alpha_rad) * (x + z / 100.0) - 0.5 * g * (x+z / 100.0) ** 2)
# return line
#
# plt.axis([0.0, 10.0 , 0.0, 5.0])
# ax.set_autoscale_on(False)
#
# ani = animation.FuncAnimation(fig, animate, np.arange(1, 200))
# plt.show()

# fig, ax = plt.subplots(1, 1)
# ax.plot(y, range_corner)
# plt.title('ball trajectory')
# ax.set_ylabel('y, meters')
# ax.set_xlabel('α, degrees')
# ax.grid(True, which='both')
# plt.show()

# window = Tk()
# window.title('hi')
# window.mainloop()

