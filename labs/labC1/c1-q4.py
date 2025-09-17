# -*- coding: utf-8 -*-
"""
Created on Wed Sep 10 17:11:09 2025

@author: Thomas Sancho
"""

import numpy as np
import matplotlib.pyplot as plt

n=4
ti,tf,npts = 0,n*(np.pi),1000
t=np.linspace(ti,tf,npts)

x=2*np.cos(t)+5*np.cos(2*t/3)
y=2*np.sin(t)-5*np.sin(2*t/3)

def Length(x,y):
    L=0
    for i in range(len(x)-1):
        L += np.sqrt((x[i+1]-x[i])**2 + (y[i+1]-y[i])**2)
    return L

print(Length(x,y))
plt.plot(x,y)
plt.grid(True)
plt.xlabel("x")
plt.ylabel("y")
plt.axis("equal")

 