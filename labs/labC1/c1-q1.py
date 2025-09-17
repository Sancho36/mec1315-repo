# -*- coding: utf-8 -*-
"""
Created on Wed Sep 10 14:47:48 2025

@author: Thomas Sancho
"""

import numpy as np
import matplotlib.pyplot as plt

ti=0
npts=100

def Courbe(n):
    tf=n*np.pi
    t=np.linspace(ti,tf,npts)
    
    x=2*np.cos(t)+5*np.cos(2*t/3)
    y=2*np.sin(t)-5*np.sin(2*t/3)
    
    plt.plot(x,y)
    plt.grid(True)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axis("equal")

Courbe(6)