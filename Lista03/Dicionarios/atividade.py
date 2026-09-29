
# Questão 1 - Cadastro de aluno
print("=======Questão 1=======")
aluno = {
    "nome" : "Daniel",
    "idade" : 18,
    "curso" : "Ciência da Computação",
    "cidade" : "São Sebastião de Lagoa de Roça"
}

print(aluno)
print(aluno["nome"])
print(aluno["curso"])

# Questão 2 - Alteração
print("=======Questão 2=======")
aluno["idade"] = 20
aluno["curso"] = "ADS"
print(aluno)

# Questão 3 - Nova informação
print("=======Questão 3=======")
aluno["email"] = "danielmotaita@gmail.com"
aluno["telefone"] = "(83) 8903-8017"
print(aluno)

#Questão 4 - Remoção
print("=======Questão 4=======")
del aluno["telefone"]
print(aluno)

#Questão 5 - Verificação
print("=======Questão 5=======")
if "email" in aluno:
    print("E-mail cadastrado!")
else:
    print("E-mail não cadastrado!")

#Questão 6 - Percorrendo o dicionário
print("=======Questão 6=======")
produto = {
    "nome": "Notebook",
    "preco" : 2500,
    "marca" : "acer",
    "estoque" : 10
}

for chave in produto.keys():
    print(chave)

for valor in produto.values():
    print(valor)

#Questão 7 - Sistema de notas
print("=======Questão 7=======")
aluno2 = {
    "nome" : "João",
    "nota1" : 8,
    "nota2" : 6
}

soma = aluno2["nota1"] + aluno2["nota2"]
media = soma / 2
print(media)

#Questão 8 - Sistema de notas
print("=======Questão 8=======")
produtos2 = {
    "macarrão" : 7.65,
    "cuscuz" : 4.76,
    "arroz" : 14.89,
    "feijão" : 16.79,
    "carne" : 20.00
}

for chave in produtos2.keys():
    print(chave)
print("=~"*12)

for valor in produtos2.values():
    print(valor)
print("=~"*12)

print(produtos2)
mais_caro = max(produtos2)
print(f"O produto mais caro é o {mais_caro}!")