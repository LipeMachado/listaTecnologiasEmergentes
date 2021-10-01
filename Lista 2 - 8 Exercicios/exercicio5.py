# -*- coding: utf-8 -*-

import numpy as np

def second_half(array):
    mt = array[len(array)//2:]
    return mt
        
x1 = np.array([1, 2, 3, 4])
print(second_half(x1))

x2 = np.array([1, 2, 3, 4, 5])
print(second_half(x2))