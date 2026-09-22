#QUESTÃO 2: Ainda com a lista criada na questão anterior, faça: 
#a. Retorne os primeiros 3 elementos da lista 
#b. Retorne os elementos que estão da 3ª posição até a 7ª posição da lista 
#c. Retorne os elementos da lista de 3 em 3 elementos 
#d. Retorne os 3 últimos elementos da lista 
#e. Retorne todos os elementos menos os 4 últimos da lista 

numeros = [0, 2, 4, 1, 5, 9, 8, 6, 3, 7] #Lista da questão 1
print("Lista:", numeros)
print("\n")

#Letra a:
print("Três primeiros elementos:", numeros[:3])

#Letra b:
print("Elementos da 3ª até a 7ª posição:", numeros[2:7])

#Letra c:
print("Elementos da lista de 3 em 3:", numeros[0:len(numeros):3])

#Letra d:
print("Os 3 últimos elementos da lista:", numeros[(len(numeros)-3):len(numeros)])

#Letra e:
print("Elementos da lista sem os 4 últimos:", numeros[0:len(numeros)-4])