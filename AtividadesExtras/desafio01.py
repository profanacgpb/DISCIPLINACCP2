lista = ["Lucia", "Jason", "Arthur", "John"]
print(lista)
lista.append("Alfredo")
print(lista)
lista.remove("John")
print(lista)
lista[2] = "Daniel"
print(lista)
fatiar  = [s[0:3] for s in lista]
print(fatiar)
lista.reverse()
print(lista)