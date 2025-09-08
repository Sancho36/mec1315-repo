# -*- coding: utf-8 -*-
"""
Created on Thu Sep  4 10:42:11 2025

@author: Thomas Sancho
"""

import numpy as np

"""
a = np.array([1,6,7,8,3])
b = np.array([3,9,7,4,3])

dot = np.dot(a,b)

print(dot)
"""

"~As function~"
def dot(a,b):
    s = 0
    
    for i in range(len(a)):
        s = s+a[i]*b[i]
        
    return s

print(dot([1,6,7,8,3],[3,9,7,4,3]))
    
    