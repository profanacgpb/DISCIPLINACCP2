tupla = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

try:
    tupla[2] = 10
except TypeError:
    print("Não é possível alterar um elemento da tupla")

print(tupla.index(5))