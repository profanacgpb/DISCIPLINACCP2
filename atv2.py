# QUESTÃO 1

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# a) Adicione o número 6
lista.append(6)

# b) Insira o número 7 na 3ª posição
lista.insert(2, 7)

# c) Remova o elemento 3
lista.remove(3)

# d) Adicione o número 4
lista.append(4)

# e) Verifique o número de ocorrências do número 4
print("Quantidade de vezes que o número 4 aparece:", lista.count(4))

print("Lista:", lista)


# QUESTÃO 2

# a) Retorne os primeiros 3 elementos
print("\n2a - Primeiros 3 elementos:")
print(lista[:3])

# b) Retorne os elementos da 3ª posição até a 7ª posição
print("\n2b - Da 3ª até a 7ª posição:")
print(lista[2:7])

# c) Retorne os elementos de 3 em 3
print("\n2c - De 3 em 3:")
print(lista[::3])

# d) Retorne os 3 últimos elementos
print("\n2d - 3 últimos elementos:")
print(lista[-3:])

# e) Retorne todos os elementos menos os 4 últimos
print("\n2e - Menos os 4 últimos:")
print(lista[:-4])


# QUESTÃO 3

# Retorne o 6º elemento
print("\n3 - 6º elemento:")
print(lista[5])


# QUESTÃO 4

# Altere o 7º elemento para 12
lista[6] = 12

print("\n4 - Lista com o 7º elemento alterado:")
print(lista)


# QUESTÃO 5

# Inverta a ordem dos elementos
lista.reverse()

print("\n5 - Lista invertida:")
print(lista)


# QUESTÃO 6

# Ordene a lista
lista.sort()

print("\n6 - Lista ordenada:")
print(lista)


# QUESTÃO 7

tupla = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# a) Tente alterar o 3º elemento para 10
print("\n7a - Tentando alterar a tupla:")

try:
    tupla[2] = 10
except TypeError:
    print("Não é possível alterar uma tupla.")


# b) Verifique o índice do valor 5
print("\n7b - Índice do número 5:")
print(tupla.index(5))


# QUESTÃO 8

dicionario = {
    "nome": "João",
    "idade": 20,
    "cidade": "Recife",
    "curso": "Python",
    "nota": 9
}

# a) Imprima todas as chaves
print("\n8a - Chaves:")
print(dicionario.keys())

# b) Imprima todos os valores
print("\n8b - Valores:")
print(dicionario.values())

# c) Imprima todos os itens
print("\n8c - Itens:")
print(dicionario.items())

# d) Imprima o 2º item
print("\n8d - Segundo item:")
print(list(dicionario.items())[1])

# e) Imprima o dicionário completo
print("\n8e - Dicionário completo:")
print(dicionario)

# f) Percorra o dicionário
print("\n8f - Chave e valor:")

for chave, valor in dicionario.items():
    print(chave, "tem como valor", valor)


# QUESTÃO 9

# a) Escreva os números de 1 a 10
with open("numeros.txt", "w") as arquivo:
    for numero in range(1, 11):
        arquivo.write(str(numero) + "\n")


# b) Imprima todos os números do arquivo
print("\n9b - Números de 1 a 10:")

with open("numeros.txt", "r") as arquivo:
    print(arquivo.read())


# c) Escreva os números de 11 a 20,
# substituindo os números anteriores
with open("numeros.txt", "w") as arquivo:
    for numero in range(11, 21):
        arquivo.write(str(numero) + "\n")


# d) Adicione os números de 21 a 30
with open("numeros.txt", "a") as arquivo:
    for numero in range(21, 31):
        arquivo.write(str(numero) + "\n")


# e) Imprima todos os números do arquivo novamente
print("\n9e - Números de 11 a 30:")

with open("numeros.txt", "r") as arquivo:
    print(arquivo.read())


# f) Imprima linha por linha
print("\n9f - Linha por linha:")

with open("numeros.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip())