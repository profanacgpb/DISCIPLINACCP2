#Questão 7 — Sistema de notas
#Crie o dicionário abaixo, calcule a média e informe se o aluno foi aprovado (média ‡ 7) ou reprovado:
#aluno = {" + '"nome": "João", "nota1": 8, "nota2": 6' + "}

aluno = {"nome": "João", "nota1": 8, "nota2": 6}

media = (aluno["nota1"]+aluno["nota2"])/2

if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")