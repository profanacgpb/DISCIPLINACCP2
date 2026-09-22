lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lista.append(6)

lista.insert(2, 7)

lista.remove(3)

lista.append(4)

print (lista[:3])

print (lista[2:7])

print (lista[::3])

print (lista[-3:])

print (lista[:-4])

print (lista[:6])

lista[6] = 12
print (lista)

lista.reverse()
print(lista)