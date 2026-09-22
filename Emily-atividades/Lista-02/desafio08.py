# Criando o dicionário
aluno = {"nome": "Emily",
    "idade": 18,
    "curso": "Computação",
    "cidade": "Campina Grande",
    "semestre": 2}

# a) Imprima todas as chaves
print(aluno.keys())

# b) Imprima todos os valores
print(aluno.values())

# c) Imprima todos os itens
print(aluno.items())

# d) Imprima o 2º item do dicionário
print(list(aluno.items())[1])

# e) Imprima o dicionário completo
print(aluno)

# f) Percorra o dicionário
for chave, valor in aluno.items():
    print(f"({chave}) tem como valor ({valor})")

list(aluno.items())[1]