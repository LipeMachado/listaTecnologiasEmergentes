# -*- coding: utf-8 -*-

paises = ("Brazil", "EUA", "Russia", "China")
linguas = ("Portugues", "Ingles", "Russo", "Mandarim")
dic = {}

def dicionario(p, l):
    for i in range(len(paises)):
        print(paises[i], linguas[i])
        i += i
    
dic = dicionario(paises, linguas)