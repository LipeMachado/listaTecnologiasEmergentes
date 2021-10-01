# -*- coding: utf-8 -*-

import numpy as np

values = [7, 4, 5, 8, 9, 0, 1, 3, 2, 6]

x = np.array(values)
impar = x[::-1]
print(impar)