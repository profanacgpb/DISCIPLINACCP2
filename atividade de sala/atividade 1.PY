# Lista com números de 0 a 9
lista = [0, 1, 2, 3, 4, 5, 8, 9]

# a) Adicione o número 6
lista.append(6)

# b) Insira o número 7 na 3ª posição
lista.insert(2, 7)

# c) Remova o elemento 3
lista.remove(3)

# d) Adicione o número 4
lista.append(4)

# e) Verifique o número de ocorrências do número 4
ocorrencias = lista.count(4)

print("Lista final:", lista)
print("Número de ocorrências do 4:", ocorrencias)