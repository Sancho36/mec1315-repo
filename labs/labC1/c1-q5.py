# -*- coding: utf-8 -*-
"""
Created on Wed Sep 10 17:34:08 2025

@author: Thomas Sancho
"""

import numpy as np
from scipy import integrate

xi,xf,npts = 0,4,15
x=np.linspace(xi,xf,npts)
h=x[1]-x[0]

y=1+2*np.exp(-x)*np.sin(4*x)

I1=0
for i in range(0,npts-1):
    I1+=(y[i]+y[i+1])/2 * h

I2=np.trapezoid(y,dx=h)
I3=integrate.trapezoid(y,dx=h)

print(f"Intégrale de y: I1 = {I1}, I2 = {I2}, I3 = {I3}")