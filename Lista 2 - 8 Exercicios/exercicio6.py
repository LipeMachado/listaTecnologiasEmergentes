# -*- coding: utf-8 -*-

import numpy as np

x = np.array([5, 7, 4, 6, 3, 9])
y = np.array([2, 1, 8, 0])

concat = np.concatenate([x, y])

print(concat)