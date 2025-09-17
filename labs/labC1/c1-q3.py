# -*- coding: utf-8 -*-
"""
Created on Wed Sep 10 16:04:51 2025

@author: Thomas Sancho
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

xi,xf,npts = 0,10,100

x=np.linspace(xi,xf,npts)

def Bissection(f, a, b, tol=1e-6, maxiter=100):
    if f(a)*f(b)>=0:
        raise ValueError("La fonction est le meme signe aux bornes a et b!")
    i = 0
    while (b-a)/2 > tol and i < maxiter:
        m = (b + a) / 2 # Calcule le point milieu
        if f(m) == 0:
            return m
        elif f(a)*f(m) > 0: # Si vrai, il n’y a pas de changement de signe
            a = m # Alors on deplace la borne de gauche
        else: # Si faux, il y a un changement de signe
            b = m # Alors on deplace la borne de droit
        i += 1
    return m # Retourne la racine m

def f(x):
    return 3*np.exp(-x)-np.sin(2*x)

r1=Bissection(f,4,5)
r2=optimize.bisect(f,4,5)
r3=optimize.fsolve(f,4.8)
print(f"Racine de f(x): r1 = {r1}, r2 = {r2}, r3 = {r3[0]}")

z=r1*0

plt.plot(x,f(x),label=r'$f(x)=3e^{-x}-\sin(2x)$',zorder=1)
plt.scatter(r1,z,c='tab:orange',label='Racine calculée',zorder=2)

plt.grid(True,zorder=0)
gridlines=plt.gca().get_ygridlines()
gridlines[3].set_color('tab:blue')
gridlines[3].set_linewidth(1)

plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()