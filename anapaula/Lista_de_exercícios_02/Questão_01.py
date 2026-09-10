#QUESTÃO 1: Criação da lista e algumas manipulações

numeros = [0, 2, 4, 1, 5, 9, 8, 6, 3, 7]
print("Lista:", numeros)
print("\n")

numeros.append(6)
print("Adicionando 6 na lista:", numeros)

numeros.insert(2, 7)
print("Adicionando o 7 na terceira posição:", numeros)

numeros.remove(3)
print("Removendo 3 da lista:", numeros)

numeros.append(4)
print("Adicionando 4 na lista:", numeros)

print("Ocorrência do número 4 na lista:", numeros.count(4))