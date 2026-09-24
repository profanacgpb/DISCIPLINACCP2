#1- Crie uma lista com números de 0 a 9 (em qualquer ordem). Com ela, faça: 
# a. Adicione o número 6 
# b. Insira o número 7 na 3ª posição da lista 
# c. Remova o elemento 3 da lista 
# d. Adicione o número 4 
# e. Verifique o número de ocorrências do número 4 na lista
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Lista inicial: {lista}")
lista.append(6)
print(f"Adicionado o 6: {lista}")
lista.insert(2, 7)
print(f"Inserido o 7 na 3ª posição: {lista}")
lista.remove(3)
print(f"Removido o elemento 3: {lista}")
lista.append(4)
print(f"Adicionado o 4: {lista}")
quatro = lista.count(4)
print(f"Número de ocorrências do número 4: {quatro}")
#2- Ainda com a lista criada na questão anterior, faça: 
# a. Retorne os primeiros 3 elementos da lista 
# b. Retorne os elementos que estão da 3ª posição até a 7ª posição da lista 
# c. Retorne os elementos da lista de 3 em 3 elementos 
# d. Retorne os 3 últimos elementos da lista 
# e. Retorne todos os elementos menos os 4 últimos da lista
primeiros_tres = lista[:3]
print(f"Primeiros 3 elementos: {primeiros_tres}")
terceira_a_setima = lista[2:6]
print(f"Da 3ª à 7ª posição: {terceira_a_setima}")
tres_em_tres = lista[::3]
print(f"De 3 em 3 elementos: {tres_em_tres}")
ultimos_tres = lista[-3:]
print(f"Últimos 3 elementos: {ultimos_tres}")
menos_ultimos_quatro = lista[:-4]
print(f"Todos menos os 4 últimos: {menos_ultimos_quatro}")
#3- Com a lista das questões anteriores, retorne o 6º elemento da lista. 
sexto_elemento = lista[5]
print(f"O 6º elemento é: {sexto_elemento}")
#4- Altere o valor do 7º elemento da lista para o valor 12. 
lista[6] = 12
print(f"Lista após alterar o 7º elemento para 12: {lista}")
#5- Inverta a ordem dos elementos na lista.
lista.reverse()
print(f"Lista invertida: {lista}")
#6- Ordene a lista. 
lista.sort()
print(f"6. Lista ordenada: {lista}")