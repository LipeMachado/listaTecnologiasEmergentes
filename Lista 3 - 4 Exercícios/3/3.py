# -*- coding: utf-8 -*-

Object = lambda : print(10*"-=-")

abrir = open("entrada.txt", "r")

for line in abrir:
    pessoa = line.split(",")
    
    anoNascimento = int(pessoa[1])
    nome = str(pessoa[0]) 
    idade = 2021 - int(pessoa[1])

    if idade < 18:
        msg = "Menor de idade"
    elif idade > 18:
        msg = "Maior de idade"
    else:
        msg = "Entrando na maior idade"

    saida = open("saida.txt", "a")
    saida.write(f"{str(nome)} \n{str(idade)} \n{str(msg)} \n" + 10*"-=-" + "\n")
    saida.close()
    