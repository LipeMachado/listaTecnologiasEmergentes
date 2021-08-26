# -*- coding: utf-8 -*-

userNum = int(input("Digite um número inteiro: "))

if userNum <= 0:
    print("Não é um número inteiro.")
else:
    numero = str(userNum)
    print(numero[::-1])