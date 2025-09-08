# -*- coding: utf-8 -*-
"""
Created on Thu Sep  4 10:49:46 2025

@author: Thomas Sancho
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,100)
y = (np.exp(-x))*(np.cos(2*np.pi*x))

plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("f(x)=e^{-x} cos(2*pi*x)")
plt.grid(True)
plt.show()