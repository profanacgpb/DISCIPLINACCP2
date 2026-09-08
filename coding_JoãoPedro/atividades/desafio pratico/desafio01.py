#Lista de alunos

lista = ["Ana", "Rute", "Sara", "Tai", "Jonh"]

print("Lista inicial:")
print(lista)

lista.append("Maria")
print("\n")
print(lista)

lista.remove("Tai")
print("\n")
print(lista)

lista[2] = "João"
print("\n")
print(lista)

print("\n")
print(lista[:4])

print("\n")
print(lista[-2:])

lista.reverse()
print("\n")
print(lista)

lista.sort()
print("\n")
print(lista)