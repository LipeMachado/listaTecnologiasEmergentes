# -*- coding: utf-8 -*-

def trueOrFalse(num):
    if num <= 0:
        return 'N'
    else:
        return 'P'
    
user = float(input("Digite um número: "))

print(trueOrFalse(user))