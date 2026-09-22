lista = [0,1,2,3,4,5,6,7,8,9]

print("Lista:", lista)

lista.append(6)
lista.insert(2, 7)
lista.remove(3)
lista.append(4)

print("primeiros 3:", lista[:3])
print("3° ate o 7°:", lista[2:7])
print("de 3 em 3:", lista[::3])
print("3 ultimos:"), lista[-3:]
print("menos os 4 ultimos:", lista[:-4])

print("6° elemento:", lista[5])
print[6] = 12

lista.reverse()
print("invertida:", lista)

lista.sort()
print("ordenada:", lista)