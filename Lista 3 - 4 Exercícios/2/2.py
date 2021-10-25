# -*- coding: utf-8 -*-

abrir = open("lista.txt", "r")

soma = 0

for line in abrir:
  preco = line.split(",")
  soma += float(preco[1])

print(soma)