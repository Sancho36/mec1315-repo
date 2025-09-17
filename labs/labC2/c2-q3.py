# -*- coding: utf-8 -*-
"""
Created on Wed Sep 17 15:56:01 2025

@author: Thomas Sancho
"""

import numpy as np
import matplotlib.pyplot as plt

xp=np.array([[-4,-1,2,5]])
yp=np.array([[2,0.5,2,1]])

M=np.vstack((xp**3,xp**2,xp**1,xp**0)).T
#Mc=y
c=np.linalg.inv(M).dot(yp.T)
print(c)

xa=np.linspace(-8,8,100)
ya=np.polyval(c,xa)

plt.plot(xa,ya,'b')
plt.scatter(xp,yp,color='r')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Méthode de Vandermonde')