# -*- coding: utf-8 -*-
"""
Created on Wed Sep 10 21:08:23 2025

@author: Thomas Sancho
"""

import numpy as np
import matplotlib.pyplot as plt

arr = np.loadtxt("signal.txt")

x = np.empty(0)
y = np.empty(0)

for coord_pair in arr:
    x = np.append(x,coord_pair[0])
    y = np.append(y,coord_pair[1])

plt.plot(x,y,label='y')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')

def Derivative(y, h=1): # derivee premiere
    n = len(y)
    dy = np.zeros(n)
    for i in range(n):
        if i==0: # derivee premiere avant
            dy[i] = (y[i+1] - y[i])/h
        elif i==n-1: # derivee premiere arriere
            dy[i] = (y[i] - y[i-1])/h
        else: # derivee premiere centree
            dy[i] = (y[i+1] - y[i-1])/(2*h)
    return dy

dy_dx=Derivative(y,h=x[1]-x[0])

plt.plot(x,dy_dx,c='tab:orange',label='dy/dx')
plt.legend()

I=np.trapezoid(y,dx=x[1]-x[0])
print(I)