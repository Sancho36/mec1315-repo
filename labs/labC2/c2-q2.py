# -*- coding: utf-8 -*-
"""
Created on Wed Sep 17 15:39:37 2025

@author: Thomas Sancho
"""

import numpy as np

M = np.array([[2,-1,3],[1,2,-1],[-3,9,5],[-3,9,5]])
b = np.array([[9,4,11,10]]).T

a = np.linalg.pinv(M).dot(b)
print(a)