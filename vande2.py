import math

def f(x, y):
    return float(x*math.cos(x*x+y))

a, b = map(float, input('Nhập cận dưới và trên trong dấu tích phân theo biến x: ').split())
c, d = map(float, input('Nhập cận dưới và trên trong dấu tích phân theo biến y: ').split())
m, n = map(int, input('Nhập số khoảng chia cho biến x,y (phải là sô chẵn): ').split())
h=(d-c)/n; print('Khoảng chia h là: ',h)
k=(b-a)/m; print('Khoảng chia k là: ',k)
