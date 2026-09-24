#Crie um dicionário com 5 entradas e suas respectivas chaves e valores.

aluno = {
    "nome": "Zenildo",
    "idade": 26,
    "curso": "Ciência da Computação",
    "periodo": 8,
    "nota": 8.5
}

# Faça: 
# a. Imprima todas as chaves do dicionário
print(aluno.keys())

# b. Imprima todos os valores do dicionário
print(aluno.values())

# c. Imprima todos os itens do dicionário 
print(aluno)

# d. Imprima o 2º item do dicionário 
print(list(aluno.items())[1])

# e. Imprima o dicionário completo 
print(aluno)

# f. Percorra o dicionário, imprimindo para cada entrada o modelo “(chave) tem como valor (valor)”
for chave, valor in aluno.items():
    print(f"{chave} : {valor}") 