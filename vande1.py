import numpy;
from sympy import symbols, solve, Eq
import math

x = numpy.array([0, 500, 1000, 1500, 2200, 2900, 3600, 4300, 5200, 6500, 7000, 7500])
y = numpy.array([2.93 ,2.66, 2.52, 2.4, 2.25, 2.1, 1.95, 1.8, 1.58, 1.32, 0.93, 0.39])

volume = 0
for i in range(len(x)-1):
    volume += 0.5 * (x[i+1] - x[i]) * (y[i+1] + y[i])


print("Thể tích chất lỏng thoát ra: " + str(volume))