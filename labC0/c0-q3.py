# -*- coding: utf-8 -*-
"""
Created on Thu Sep  4 10:58:04 2025

@author: Thomas Sancho
"""

from scipy.special import factorial

def Approx_Sin(n,x):
    ans = 0
    for i in range(0,n):
        ans += ((-1)**i/factorial(2*i+1))*x**(2*i+1)
    
    return ans

print(Approx_Sin(4,1.5))