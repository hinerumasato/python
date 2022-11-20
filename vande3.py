import numpy as np
from sympy import *
from sympy.calculus.util import *
from numpy.linalg import inv
import matplotlib.pyplot as plt
def func(L,delta,Tinf,h,T0,Tl):
    height = int(L/delta)-1
    T = np.zeros(height)
    a = np.zeros((height, height))
    m = (1/delta**2)
    n = -(2/delta**2+h)
    p = (1/delta**2)
    for i in range(1,height-2):
        T[i]=-h*Tinf
    T[0] = -(T0/delta**2+h*Tinf)
    T[height-1] = -(Tl/delta**2+h*Tinf)
    for i in range(1, height-1):
        a[i][i] = n
        a[i][i-1] = p
        a[i][i+1] = m
    a[0][0] = n
    a[height-1][height-1] = n
    a[0][1] = m
    a[height-1][height-2] = p
    b = inv(a).dot(T)
    ans = np.zeros((2,height+2))
    for i in range(height):
        ans[1][i+1] = b[i]
    for i in range(height+2):
        ans[0][i] = delta*i
    ans[1][0]=T0
    ans[1][height+1]=Tl
    for i in range(height+2):
        print(ans[0][i],ans[1][i])
    plt.plot(ans[0],ans[1])
    plt.show()
func(12,0.5,220,0.0425,320,450)
