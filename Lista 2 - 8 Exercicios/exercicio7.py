# -*- coding: utf-8 -*-

import numpy as np

def mix(x, y):
    x1 = x[:len(x)//2]
    y1 = y[len(y)//2:]
    return x1, y1


x = np.array([1, 2, 3, 4, 5])
y = np.array([6, 7, 8, 9, 10])
concat = np.concatenate(mix(x, y))
print(concat)