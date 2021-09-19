# -*- coding: utf-8 -*-

separadorDeCodigo = lambda : print('-=-'*20)

# 1º Atividade

def count(n):
    #Dobro
    dobro = n * 2
    
    #Fatorial
    fat = 1
    i = 2
    while i <= n:
        fat = fat*i
        i = i + 1
    
    #Produto com 5
    produto = n * 5
    
    return print(f"Dobro: {dobro} \nFatorial: {fat} \nProduto: {produto}")

num = int(input("Digite um número inteiro: "))

count(num)

# 2º Atividade

separadorDeCodigo()

dicCores = {
    "Juan" : "Azul",
    "Marcos" : "Verde",
    "Rick" : "Amarelo",
    "Gustavo" : "Laranja",
    "Karen" : "Rosa",
}

for nomes, cores in dicCores.items():
    print (f"{nomes} => {cores}")

# 3º Atividade

separadorDeCodigo()

semana = {
    "segunda" : ["Geometria e algebra linear", "Geometria e algebra linear", "Geometria e algebra linear"],
    "terca" : ["Tecnologias Emergentes", "Estrutura de dados 2", "Redes de Computadores", "Redes de Computadores"],
    "quarta" : ["Redes de Computadores", "Redes de Computadores", "Tecnologias Emergentes"],
    "quinta" : ["Linguagens formais e autômatos", "Linguagens formais e autômatos", "Linguagens formais e autômatos", "Estrutura de dados 2", "Estrutura de dados 2"],
    "sabado" : ["Tecnologias Emergentes", "Fundamentos do cristianismo"]
}

for dia, materias in semana.items():
    print (f"{dia} => {materias}")

# 4º Atividade

separadorDeCodigo()

def media(notas):
    result = 0
    
    for i in notas:
        result += i
    result / 4
    
    if result < 4.00:
        situacao = "Aluno Reprovado"
    elif result <= 6.00:
        situacao = "Aluno em substitutiva"
    else:
        situacao = "Aluno Aprovado"
    return result, situacao

A = {
    "nome" : "Juan Souza",
    "idade" : 24,
    "notas" : [10, 5, 4, 8]
}

B = {
    "nome" : "Felipe Santos",
    "idade" : 20,
    "notas" : [10, 9, 8]
}

resultA = media(A.get("notas"))
A["media"] = resultA[0]
A["resultado"] = resultA[1]

resultB = media(A.get("notas"))
B["media"] = resultB[0]
B["resultado"] = resultB[1]

# 5º Atividade

paises = ("Brazil", "EUA", "Russia", "China")
linguas = ("Portugues", "Ingles", "Russo", "Mandarim")
dicPaisesLinguas = {}

def dicionario(p, l):
    for i in range(len(paises)):
        print(f"{paises[i]} => {linguas[i]}")
        i += i
    
dicPaisesLinguas = dicionario(paises, linguas)

# 6º Atividade

separadorDeCodigo()

traducaoFrase = {
    "senhor" : "matey",
    "hotel" : "fleabag in",
    "estudante" : "swabbie",
    "garoto" : "matey",
    "madame" : "pround beauty",
    "professor" : "foul blaggart",
    "restaurante" : "galley",
    "seu" : "yer",
    "com licença" : "arr",
    "estudantes" : "swabbies",
    "são" : "be",
    "advogado" : "foul blaggart",
    "o" : "th",
    "banheiro" : "head",
    "meu" : "me",
    "oi" : "avast",
    "é" : "be",
    "homem" : "matey",
}

portugues = input("Digite uma palavra: ")
traducao = traducaoFrase.get(portugues)
print(traducao)
