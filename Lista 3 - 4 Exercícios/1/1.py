# -*- coding: utf-8 -*-

palavras = open('texto.txt', 'r')
dados = palavras.read()

vogais = 0

for caracter in dados:
    if caracter in 'aeiou':
        vogais += 1
    if caracter in 'AEIOU':
        vogais += 1
    
    
print(f"Total de Vogais: {vogais}")