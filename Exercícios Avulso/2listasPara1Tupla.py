# -*- coding: utf-8 -*-

import numpy as np

def concatenacao(lista1, lista2):
    concat = np.concatenate([lista1, lista2])    
    return concat

lista1 = [10, 21, 2, 4]
lista2 = [2, 45, 7, 64]

print(tuple(concatenacao(lista1, lista2)))