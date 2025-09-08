# -*- coding: utf-8 -*-
"""
Created on Thu Sep  4 11:19:03 2025

@author: Thomas Sancho
"""

import numpy as np
import matplotlib.pyplot as plt

""" ~Method 1~
sn = 0
x = np.linspace(1,100,100)
y = np.empty((0))

for n in range(1,101):
    sn += 1/n
    y = np.append(y,sn)
"""

"~Method 2~"
x = np.linspace(1,100,100)
y = np.cumsum(1/x)

plt.plot(x,y)
plt.xlabel("n")
plt.ylabel("Sn")
plt.title("Sn=Sum{1/k} de k=1 à n")
plt.grid(True)
plt.show()
