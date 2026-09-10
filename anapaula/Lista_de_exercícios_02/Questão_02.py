#QUESTÃO 1: Outras manipulações utilizando a lista da questão 1

numeros = [0, 2, 4, 1, 5, 9, 8, 6, 3, 7] #Lista da questão 1
print("Lista:", numeros)
print("\n")

print("Três primeiros elementos:", numeros[:3])
print("Elementos da 3ª até a 7ª posição:", numeros[2:7])
print("Elementos da lista de 3 em 3:", numeros[0:len(numeros):3])
print("Os 3 últimos elementos da lista:", numeros[(len(numeros)-3):len(numeros)])
print("Elementos da lista sem os 4 últimos:", numeros[0:len(numeros)-4])