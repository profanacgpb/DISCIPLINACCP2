#QUESTÃO 1: Crie uma lista com números de 0 a 9 (em qualquer ordem). Com ela, faça: 
#a. Adicione o número 6 
#b. Insira o número 7 na 3ª posição da lista 
#c. Remova o elemento 3 da lista 
#d. Adicione o número 4 
#e. Verifique o número de ocorrências do número 4 na lista

numeros = [0, 2, 4, 1, 5, 9, 8, 6, 3, 7]
print("Lista:", numeros)
print("\n")

#Letra a:
numeros.append(6)
print("Adicionando 6 na lista:", numeros)

#Letra b:
numeros.insert(2, 7)
print("Adicionando o 7 na terceira posição:", numeros)

#Letra c:
numeros.remove(3)
print("Removendo 3 da lista:", numeros)

#Letra d:
numeros.append(4)
print("Adicionando 4 na lista:", numeros)

#Letra e:
print("Ocorrência do número 4 na lista:", numeros.count(4))