<<<<<<< Updated upstream

tupla = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

try:
    tupla[2] = 10
except TypeError as e:
    print("\n7a. Erro proposital capturado (Tuplas são imutáveis!):", e)

print("7b. O índice do valor 5 na tupla é:", tupla.index(5))# 7. Crie uma tupla com números de 0 a 9
tupla = (9, 2, 5, 0, 8, 1, 3, 4, 7, 6)

try:
    tupla[2] = 10
except TypeError as e:
    print("\n7a. Erro proposital capturado (Tuplas são imutáveis!):", e)

=======
tupla = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

try:
    tupla[2] = 10
except TypeError as e:
    print("\n7a. Erro proposital capturado (Tuplas são imutáveis!):", e)

print("7b. O índice do valor 5 na tupla é:", tupla.index(5))# 7. Crie uma tupla com números de 0 a 9
tupla = (9, 2, 5, 0, 8, 1, 3, 4, 7, 6)

try:
    tupla[2] = 10
except TypeError as e:
    print("\n7a. Erro proposital capturado (Tuplas são imutáveis!):", e)

>>>>>>> Stashed changes
print("7b. O índice do valor 5 na tupla é:", tupla.index(5))