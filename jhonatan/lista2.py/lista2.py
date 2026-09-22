
# LISTA DE EXERCÍCIOS 02 - ESTRUTURA DE DADOS



# 1
lista = list(range(10))

print("Lista inicial:", lista)

# a) 
lista.append(6)

# b) 
lista.insert(2, 7)

# c) 
lista.remove(3)

# d) 
lista.append(4)

# e) 
print("\nQUESTÃO 1")
print("Lista:", lista)
print("Quantidade de números 4:", lista.count(4))


# 2
print("\nQUESTÃO 2")

# a) 
print("Primeiros 3 elementos:", lista[:3])

# b) 
print("Da 3ª até a 7ª posição:", lista[2:7])

# c)
print("De 3 em 3:", lista[::3])

# d) 
print("3 últimos elementos:", lista[-3:])

# e) 
print("Todos menos os 4 últimos:", lista[:-4])


# 3
print("\nQUESTÃO 3")
print("6º elemento da lista:", lista[5])


# 4
lista[6] = 12

print("\nQUESTÃO 4")
print("Lista com o 7º elemento alterado para 12:")
print(lista)


# 5
lista.reverse()

print("\nQUESTÃO 5")
print("Lista invertida:")
print(lista)


# 6
lista.sort()

print("\nQUESTÃO 6")
print("Lista ordenada:")
print(lista)


# 7
tupla = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

print("\nQUESTÃO 7")
print("Tupla:", tupla)

# a)
try:
    tupla[2] = 10
except TypeError:
    print("Não é possível alterar elementos de uma tupla.")

# b)
print("Índice do número 5:", tupla.index(5))


# 8
dicionario = {
    "nome": "José",
    "idade": 18,
    "curso": "Ciência da Computação",
    "cidade": "Campina Grande",
    "periodo": 2
}

print("\nQUESTÃO 8")

# a)
print("Chaves:", dicionario.keys())

# b)
print("Valores:", dicionario.values())

# c)
print("Itens:", dicionario.items())

# d)
print("2º item:", list(dicionario.items())[1])

# e)
print("Dicionário completo:", dicionario)

# f) 
print("\nPercorrendo o dicionário:")

for chave, valor in dicionario.items():
    print(f"{chave} tem como valor {valor}")


# 9

print("\nQUESTÃO 9")

# a) 
with open("numeros.txt", "w") as arquivo:
    for numero in range(1, 11):
        arquivo.write(str(numero) + "\n")


# b) 
print("\nNúmeros de 1 a 10:")

with open("numeros.txt", "r") as arquivo:
    print(arquivo.read())


# c) 
with open("numeros.txt", "w") as arquivo:
    for numero in range(11, 21):
        arquivo.write(str(numero) + "\n")


# d) 
with open("numeros.txt", "a") as arquivo:
    for numero in range(21, 31):
        arquivo.write(str(numero) + "\n")


# e) 
print("Números de 11 a 30:")

with open("numeros.txt", "r") as arquivo:
    print(arquivo.read())


# f) 
print("Números linha por linha:")

with open("numeros.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip())