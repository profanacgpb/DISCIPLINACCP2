tupla = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

try:
    tupla[2] = 10
except TypeError:
    print("7a: Não é possível alterar uma tupla.")

print("7b:", tupla.index(5))