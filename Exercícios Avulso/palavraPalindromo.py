# -*- coding: utf-8 -*-

def palindromo(frase):
    if frase == frase[::-1]:
        print("É um palíndromo!!!")
    else:
        print("Não é um palíndromo!!!")

frase = input("Qual a frase ou palavra? ").upper().replace(" ", "")
palindromo(frase)