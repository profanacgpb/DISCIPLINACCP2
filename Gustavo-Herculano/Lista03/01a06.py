# 1. Crie uma lista com números de 0 a 9
lista = [0, 1, 2, 3, 4, 5, 8, 9]

print("Lista inicial:", lista)

# 1.1 Adicione o número 6
lista.append(6)
print("Após adicionar 6:", lista)

# 1.2 Insira o número 7 na 3ª posição
# Em Python, o índice da 3ª posição é 2
lista.insert(2, 7)
print("Após inserir 7 na 3ª posição:", lista)

# 1.3 Remova o elemento 3
lista.remove(3)
print("Após remover o número 3:", lista)

# 1.4 Adicione o número 4
lista.append(4)
print("Após adicionar 4:", lista)

# 1.5 Verifique o número de ocorrências do número 4
print("Quantidade de vezes que o número 4 aparece:", lista.count(4))


# ==================================================
# 2. Fatiamento da lista
# ==================================================

# 2.1 Primeiros 3 elementos
print("Primeiros 3 elementos:", lista[:3])

# 2.2 Elementos da 3ª até a 7ª posição
# Índices 2 até 6
print("Da 3ª até a 7ª posição:", lista[2:7])

# 2.3 Elementos de 3 em 3
print("Elementos de 3 em 3:", lista[::3])

# 2.4 Últimos 3 elementos
print("Últimos 3 elementos:", lista[-3:])

# 2.5 Todos os elementos menos os 4 últimos
print("Menos os 4 últimos:", lista[:-4])


# ==================================================
# 3. Retornar o 6º elemento
# ==================================================

# O índice da 6ª posição é 5
print("6º elemento:", lista[5])


# ==================================================
# 4. Alterar o 7º elemento para 12
# ==================================================

# O índice da 7ª posição é 6
lista[6] = 12

print("Lista após alterar o 7º elemento:", lista)


# ==================================================
# 5. Inverter a ordem
# ==================================================

lista.reverse()

print("Lista invertida:", lista)


# ==================================================
# 6. Ordenar a lista
# ==================================================

lista.sort()

print("Lista ordenada:", lista)