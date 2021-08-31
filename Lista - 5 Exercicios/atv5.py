# -*- coding: utf-8 -*-

def hora(a, b):
    if a >= 12:
        if a <= 23:
            a -= 12
            return print(f'{a}:{b}pm')
        else:
            return print("Valor Incorreto da hora. Apenas 00 as 23")
    else:
        return print(f'{a}:{b}am')
        
userHour = int(input("Digite a hora: "))
userMinute = int(input("Digite os minutos: "))

hora(userHour, userMinute)