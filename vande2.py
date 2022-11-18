import math

def f(x, y):
    return float(x*math.cos(x*x+y))

a, b = map(float, input('Nhập cận dưới và trên trong dấu tích phân theo biến x: ').split())
c, d = map(float, input('Nhập cận dưới và trên trong dấu tích phân theo biến y: ').split())
m, n = map(int, input('Nhập số khoảng chia cho biến x,y (phải là sô chẵn): ').split())
h=(d-c)/n; print('Khoảng chia h là: ',h)
k=(b-a)/m; print('Khoảng chia k là: ',k)

s = 0
#Vòng lặp của tích phân bên ngoài-biến y để gắn hệ số cho y0, yn, y-chẵn và y-lẻv
for i in range(0, n+1):
    if i==0 or i==n:
        hesoy = 1
    elif i%2==0:
        hesoy = 2
    else:
        hesoy = 4
    y = c + i * h
    
    for j in range (0, m+1):
        if j == 0 or j == m:
            hesox = 1
        elif j % 2 == 0:
            hesox = 2
        else:
            hesox = 4
        x=a+j*k
        s = s+hesoy*hesox*f(x,y)
I=h*k/9*s
print('Ước lượng tích phân theo Simpson: ',I)