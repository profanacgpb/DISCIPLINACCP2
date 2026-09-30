# 7. Crie o dicionário abaixo, calcule a média e informe se o aluno foi aprovado (média ≥ 7) ou reprovado:

aluno_2 = {
    "nome": "João", 
    "nota1" : 8,
    "nota2" : 6
}

media = (aluno_2["nota1"] + aluno_2["nota2"]) / 2

if media >= 7:
    print ("APROVADO")
else:
    print ("REPROVADO")