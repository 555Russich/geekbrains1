import math
from math import pi
import matplotlib.pyplot as plt
import numpy as np


g = float(9.806)
s = 10
h = 4
v = 12
alpha = 31.65388  # 31.65388
print('alpha', alpha)

start_place = [0, 2]
x0 = start_place[0]
y0 = start_place[1]


t = round(s / v * math.cos(alpha * np.pi/180) , 2)
x = round(x0 + v * t * math.cos(alpha * np.pi/180), 2)
y = round(y0 + v * t * math.sin(alpha * np.pi/180) - t ** 2 * g / 2, 2)

print('t:', t); print('x:', x); print('y:', y)


'''corner range

alpha_rad = math.radians(alpha)
print('alpha_rad', alpha_rad)
alpha_min_rad = math.atan(h/s)
alpha_min = math.degrees(alpha_min_rad)
print('alpha_min', alpha_min)
# range_corner = list(range(31, 91, 1))
range_corner = []
for i in np.arange(alpha_min, 91, 1):
    range_corner.append(i)
print(range_corner)
'''
