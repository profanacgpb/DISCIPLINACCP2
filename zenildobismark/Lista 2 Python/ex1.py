# Crie uma lista com números de 0 a 9 (em qualquer ordem).
lista = [0, 1, 2, 3, 4, 5, 8, 9]

# a. Adicione o número 6
lista.append(6)
print("a.", lista)

# b. Insira o número 7 na 3ª posição da lista
lista.insert(2, 7)
print("b.", lista)

# c. Remova o elemento 3 da lista
lista.remove(3)
print("c.", lista)

# d. Adicione o número 4
lista.append(4)
print("d.", lista)

# e. Verifique o número de ocorrências do número 4 na lista
quantidade = lista.count(4)
print("e. O número 4 aparece", quantidade, "vez(es)")