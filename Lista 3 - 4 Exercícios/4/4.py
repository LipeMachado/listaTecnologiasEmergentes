# -*- coding: utf-8 -*-

alunos = open("alunos.txt", "r")

dicAlunoNota = {}
soma = 0
maiorNota = 0
menorNota = 0

for linha in alunos:
  alunoNota = linha.split(",")

  nomeAluno = str(alunoNota[0])
  notaAluno = float(alunoNota[1])

  dicAlunoNota.update({nomeAluno: notaAluno})

  soma = soma + (dicAlunoNota[nomeAluno])

  media = (soma / 23)
  media = f"{media:.2f}"

  valores = dicAlunoNota.values()
  maiorNota = max(valores)
  menorNota = min(valores)

print(f"Media: {media}")
print(f"Maior Nota: {maiorNota}")
print(f"Menor Nota: {menorNota}")