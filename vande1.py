import numpy;
import matplotlib.pyplot as plt

x = numpy.array([0, 500, 1000, 1500, 2200, 2900, 3600, 4300, 5200, 6500, 7000, 7500])
y = numpy.array([2.93 ,2.66, 2.52, 2.4, 2.25, 2.1, 1.95, 1.8, 1.58, 1.32, 0.93, 0.39])
p = numpy.polyfit(x, y, 1)
print(p[0])
print(p[1])

plt.plot(x, y, 'ro-')
plt.xlabel = ('Thời gian (s)')
plt.ylabel = ('Lưu lượng (l/s)')
plt.show()