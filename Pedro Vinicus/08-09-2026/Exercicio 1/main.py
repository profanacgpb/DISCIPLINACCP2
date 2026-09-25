#1 Crie uma lista com números de 0 a 9 (em qualquer ordem).
print("======Exercicio 1====")
lista = list(range(10)) #gerando de 0 a 9 os numeros com range 
lista.append(6) #adicionando 6 no final
print(lista)
lista.insert(2,7) # inserindo o 7 na 3 posição que seria o 2
print(lista)
lista.remove(3) #removendo o 3
print(lista)
lista.append(4) #Adicionando 4 no final
print(lista)
print("O numero ocorrência do 4 :", lista.count(4)) #mostra quantas vezes o 4 aparece

#2 Ainda com a lista criada na questão anterior, faça: 

print("======Exercicio 2====")
print("Primeiros 3:", lista[:3]) # primeiros 3 elementos
print("Da 3ª à 7ª posição:", lista[2:7]) # da 3 ate a 7 posição
print("De 3 em 3:", lista[::3]) # pega um elemento e pula os proximos 2
print("Últimos 3:", lista[-3:]) #ultimos 3 elementos
print("Sem os últimos 4:", lista[:-4]) #todos, exceto os ultimos 4


# 3. Com a lista das questões anteriores, retorne o 6º elemento da lista.
print("======Exercicio 3====")
print("6º elemento:", lista[5])

# 4.  Altere o valor do 7º elemento da lista para o valor 12. 
print("======Exercicio 4====")
lista[6] = 12
print("Lista alterada:", lista)

# 5.  Inverta a ordem dos elementos na lista.
print("======Exercicio 5====")
lista.reverse()
print("Lista invertida:", lista)

# 6. Ordene a lista
print("======Exercicio 6====")
lista.sort()
print("Lista ordenada:", lista)

# 7. Crie uma tupla com números de 0 a 9 (em qualquer ordem)...
print("======Exercicio 7====")
tupla = tuple(range(10))  #Crianção da tupla que parece com uma lista, entretanto ela não pode ser alterar seus elementos
try:
    tupla[2] = 10
except TypeError:
    print("Não é possível alterar uma tupla.") #fazendo uma tentativa de alteração na tupla com o try mais isso vai gerar um erro aonde o except TypeError captura esse erro para o programa continuar
print("Posição do valor 5:", tupla.index(5) + 1) #O programa vai esta procurando o valor 5 e retornando o seu indice que é 5. Somando mais 1 para mostra que ele esta na 6 posição da tupla

# 8. Crie um dicionário com 5 entradas e suas respectivas chaves e valores. 
print("======Exercicio 8====")
dados = {"nome": "Pedro", "idade": 20, "curso": "Informática",
         "cidade": "Campina Grande", "linguagem": "Python"} #Dicionario guardando pares da chave e valor

print("Chaves:", dados.keys()) #Todas as chaves
print("Valores:", dados.values()) #todos os valores
print("Itens:", dados.items()) #Pares de chaves e dos valores no dicionario
print("2º item:", list(dados.items())[1]) #fornece os pares os dados.items e o list permite acessa pelo o indice e [1] pega o 2 item
print("Dicionário:", dados)

for chave, valor in dados.items():
    print(f"{chave} tem como valor {valor}") #for para percorre cada par do dicionario a cada volta as chaves e valores recebem os dados de uma entrada

# 9. Crie um arquivo e:...
print("======Exercicio 9====")
with open("numeros.txt", "w") as arquivo: 
    for numero in range(1, 11):
        arquivo.write(f"{numero}\n")#cria o arquivo o "w"abre para escrita. range gera de 1 a 10 o write() vai graver os numeros e \n pula para a proxima linha

with open("numeros.txt", "r") as arquivo:
    print("Números de 1 a 10:\n" + arquivo.read()) #Le o arquivo de 1 a 10 aonde "r" abre para leitura e o read le todo o arquivo de uma vez

with open("numeros.txt", "w") as arquivo:
    for numero in range(11, 21):
        arquivo.write(f"{numero}\n")#Substituir o conteudo anterior para 11 a 21 com "w"

with open("numeros.txt", "a") as arquivo:
    for numero in range(21, 31):
        arquivo.write(f"{numero}\n") #acrescentar o conteudo anterior mais numeros no final com "a"

with open("numeros.txt", "r") as arquivo:
    print("Números de 11 a 30:\n" + arquivo.read()) #Le o arquivo de 11 a 30 aonde "r" abre para leitura e o read le todo o arquivo de uma vez

with open("numeros.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip()) #vai le uma linha por vez e o strip vai quebrar a linha