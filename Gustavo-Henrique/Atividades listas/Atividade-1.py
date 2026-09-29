# 1. Criando uma lista com números de 0 a 9
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


lista.append(6)


lista.insert(2, 7)


lista.remove(3)


lista.append(4)


print("Quantidade de números 4:", lista.count(4))


# 2. Retorne os primeiros 3 elementos da lista
print("Primeiros 3 elementos:", lista[:3])


print("Da 3ª até a 7ª posição:", lista[2:7])


print("Elementos de 3 em 3:", lista[::3])


print("3 últimos elementos:", lista[-3:])


print("Lista sem os 4 últimos:", lista[:-4])


# 3. Retorne o 6º elemento da lista
print("6º elemento:", lista[5])


# 4. Altere o valor do 7º elemento da lista para 12
lista[6] = 12
print("Lista com o 7º elemento alterado:", lista)


# 5. Inverta a ordem dos elementos da lista
lista.reverse()
print("Lista invertida:", lista)


# 6. Ordene a lista
lista.sort()
print("Lista ordenada:", lista)