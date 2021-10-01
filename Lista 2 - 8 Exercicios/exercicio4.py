# -*- coding: utf-8 -*-

import numpy as np

def first_half(array):
    mt = array[:len(array)//2:]
    return mt
        
x1 = np.array([1, 2, 3, 4])
print(first_half(x1))

x2 = np.array([1, 2, 3, 4, 5])
print(first_half(x2))