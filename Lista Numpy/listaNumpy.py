# -*- coding: utf-8 -*-

import numpy as np

separador = lambda : print(40*"=")

'''
1. Dado um array qualquer, faça
uma função que retorne a soma
de todos os elementos.
'''

def soma(a, b):
    return a + b

a = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
b = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])

print(soma(a, b))
separador()

'''
2. Dado um array qualquer, faça
uma função que retorne o valor
mínimo.
'''

def minimo(a):
    return np.nanmin(a)
    

a = np.array([[23, 34, 64], [43, 87, 46], [77, 98, 76]])

print(minimo(a))
separador()

'''
4. Dado um array qualquer, faça
uma função que retorne a média.
'''

def media(a):
    return a.mean()

a = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
print(media(a))
separador()

'''
5. Dado um array qualquer, faça
uma função que retorne a média
de todos os números do array.
'''

def media(a):
    return a.mean()

a = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
print(media(a))
separador()