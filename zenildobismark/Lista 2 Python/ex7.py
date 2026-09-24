tupla = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# a. Alterar o valor do 3º elemento da tupla para o valor 10

lista = list(tupla)
lista[2] = 10
tupla = tuple(lista)

print(tupla)

# b. Verificar o índice (posição) do valor 5 na tupla 
print(tupla[5])
