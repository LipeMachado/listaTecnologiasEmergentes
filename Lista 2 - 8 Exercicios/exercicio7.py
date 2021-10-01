# -*- coding: utf-8 -*-

import numpy as np

def mix(x, y):
    x[:2]
    y[2:]
    concat = np.concatenate(x, y)
    return concat


x = np.array([1, 2, 3, 4, 5])
y = np.array([6, 7, 8, 9, 10])
print(mix(x, y))