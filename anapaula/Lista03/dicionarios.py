# 8. Criando um dicionário

alunos = {
    "Ana": 9.5,
    "Carlos": 8.0,
    "Maria": 10.0,
    "João": 7.5,
    "Pedro": 8.5
}


# 8.1 Imprimir todas as chaves

print("CHAVES:")
print(alunos.keys())


# 8.2 Imprimir todos os valores

print("\nVALORES:")
print(alunos.values())


# 8.3 Imprimir todos os itens

print("\nITENS:")
print(alunos.items())


# 8.4 Imprimir o 2º item do dicionário

print("\n2º ITEM:")

segundo_item = list(alunos.items())[1]

print(segundo_item)


# 8.5 Imprimir o dicionário completo

print("\nDICIONÁRIO COMPLETO:")
print(alunos)


# 8.6 Percorrer o dicionário

print("\nCHAVE E VALOR:")

for chave, valor in alunos.items():
    print(f"{chave} tem como valor {valor}")