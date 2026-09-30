lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lista.append(6)

lista.insert(2, 7)

lista.remove(3)

lista.append(4)

print("Quantidade de 4:", lista.count(4))

print("Primeiros 3:", lista[:3])

print("Da 3ª até a 7ª posição:", lista[2:7])

print("De 3 em 3:", lista[::3])

print("Últimos 3:", lista[-3:])

print("Sem os 4 últimos:", lista[:-4])

print("6º elemento:", lista[5])

lista[6] = 12
print("Lista depois da alteração:", lista)

lista.reverse()
print("Lista invertida:", lista)

lista.sort()
print("Lista ordenada:", lista)