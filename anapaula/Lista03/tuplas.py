# 7. Criação da tupla
tupla = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

print("Tupla:", tupla)


# 7.1 Tentar alterar o 3º elemento para 10

try:
    tupla[2] = 10
except TypeError:
    print("Não é possível alterar uma tupla!")


# 7.2 Verificar o índice do valor 5

print("Índice do número 5:", tupla.index(5))