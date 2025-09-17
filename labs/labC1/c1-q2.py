# -*- coding: utf-8 -*-
"""
Created on Wed Sep 10 15:18:09 2025

@author: Thomas Sancho
"""

import numpy as np
import matplotlib.pyplot as plt

xi,xf,npts = -8,5,100

x=np.linspace(xi,xf,npts)
y=x**3+5*x**2-17*x-21

coeffs=np.array([1,5,-17,-21])
r=np.roots(coeffs)
print(f"Les racines du polynome sont: {np.sort(r)}")
z=r*0

plt.scatter(r,z,c='r',zorder=2)
plt.plot(x,y,zorder=1)
plt.grid(True,zorder=0)
plt.xlabel("x")
plt.ylabel("y")
