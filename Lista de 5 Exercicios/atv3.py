# -*- coding: utf-8 -*-

def quantidadeDigitos(num):
    numero = str(num)
    
    if numero[0] == '-':
        return len(numero) - 1
    
    return len(numero)

print("Qual a quantidade de digitos do seu número.")
user = int(input("Digite um número inteiro: "))

print(quantidadeDigitos(user))