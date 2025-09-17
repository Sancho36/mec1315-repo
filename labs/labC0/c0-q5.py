# -*- coding: utf-8 -*-
"""
Created on Thu Sep  4 11:51:01 2025

@author: Thomas Sancho
"""

import numpy as np
import matplotlib.pyplot as plt

arr = np.loadtxt("fibonacci.txt")
"print(arr)"

x = np.empty(0)
y = np.empty(0)

for coord_pair in arr:
    x = np.append(x,coord_pair[0])
    y = np.append(y,coord_pair[1])

plt.plot(x,y,color="b")
plt.scatter(x,y,color="b",marker="*")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Courbe de Fibonacci")
plt.show()

""" ~Using differentials~
dx = np.diff(x)
dy = np.diff(y)
L = np.sum(np.sqrt(dx**2 + dy**2))
"""

L = 0
n = len(x)
for i in range(n-1):
    L += np.sqrt((x[i+1]-x[i])**2 + (y[i+1]-y[i])**2)

print(f"Longueur approximative de la courbe = {L:.4f}")