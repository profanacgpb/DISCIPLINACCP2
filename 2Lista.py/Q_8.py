# Questão 8 - Crie um dicionário com 5 entradas
dicionario={
    "nome": "Pedro",
    "idade": "18",
    "curso": "C.C.",
    "time": "palmeiras",
    "apelido": "Raio"
}
# a. Imprima todas as chaves do dicionário 
print(dicionario.keys())

# b. Imprima todas os valores do dicionário
print(dicionario.values())
 
# c. Imprima todos os itens do dicionário 
print(dicionario.items())
 
# d. Imprima o 2º item do dicionário
itens = list(dicionario.items())
print(itens[1])
 
# e. Imprima o dicionário completo
for chave, valor in dicionario.items():
    print(chave, " :", valor)
 
# f.  Percorra o dicionário
for chave, valor in dicionario.items():
    print(f"({chave}) tem como valor ({valor})")
 
