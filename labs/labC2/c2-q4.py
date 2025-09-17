# -*- coding: utf-8 -*-
"""
Created on Wed Sep 17 16:25:09 2025

@author: Thomas Sancho
"""

import numpy as np
import matplotlib.pyplot as plt

xp=np.array([[-1,0,1,2]])
yp=np.array([[1,0.5,1.5,2.5]])
xt=np.array([[1,-1]])
yt=np.array([[0,0]])

y=np.hstack((yp,yt)).T

Mp=np.vstack((xp**5,xp**4,xp**3,xp**2,xp**1,xp**0)).T
Mt=np.vstack((5*xt**4,4*xt**3,3*xt**2,2*xt**1,xt**0,0*xt)).T
M=np.vstack((Mp,Mt))

c=np.linalg.inv(M).dot(y)
print(c)

xa=np.linspace(-1,2,100)
ya=np.polyval(c,xa)
plt.plot(xa,ya,'tab:blue')
plt.scatter(xp,yp,color='r')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')

#tangents
plt.hlines(y=1,xmin=-1.25,xmax=-0.75,color='r')
plt.hlines(y=1.5,xmin=0.75,xmax=1.25,color='r')