# -*- coding: utf-8 -*-

v = [12, 14, 100, 60, 7, 25, 3, 2, 600]
menor = v.index(min(v))

for i in range(len(v)):
    if i == min(v):
        v[menor] = 0
        print(v)