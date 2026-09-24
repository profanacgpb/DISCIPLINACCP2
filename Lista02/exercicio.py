print("=====Exercicio1=====")

lista = list(range(10))
lista.append(6)
print(lista)

lista.insert(2,7)
print(lista)

lista.remove(3)
print(lista)

lista.append(4)
print(lista)

contagem = lista.count(4)
print(f"O número de ocorrências do número 4 é {contagem}")

#Exercicio 2
print("=====Exercicio2=====")

print(lista[:3])
print(lista[2:7])
print(lista[::3])
print(lista[-3:])
print(lista[:-4])

#Exercicio 3
print("=====Exercicio3=====")
print(lista[5])

#Exercício 4
print("=====Exercicio4=====")
lista[6] = 12
print(lista)

#Exercício 5
print("=====Exercicio5=====")
lista.reverse()
print(lista)

#Exercício 6
print("=====Exercicio6=====")
lista.sort()
print(lista)

#Exercício 7
print("=====Exercicio7=====")
tupla = tuple(range(10))

try:
    tupla[2] = 10
except TypeError:
    print("Não é possível alterar uma tupla!")
print(f"Posição do valor 5: {tupla.index(5) + 1}")

#Exercício 8
print("=====Exercicio8=====")
alunos = {
    "Daniel" : 9.1,
    "Kaynan" : 3.6,
    "Pedro" : 5.3,
    "Gabriel" : 1.0,
    "Lucas" : 8.0,
}

print(alunos.keys())
print(alunos.values())
print(alunos.items())
print(list(alunos.items())[1])
print(alunos)

for chave, valor in alunos.items():
    print(f"{chave} tem como valor {valor}")

#Exercício9
print("=====Exercicio9=====")
with open("numeros.txt", "w") as arquivo:
    for numero in range(1,11):
        arquivo.write(f"{numero}\n")

with open("numeros.txt" , "r") as arquivo:
    print(f"Números de 1 a 10:\n" + arquivo.read())

with open("numeros.txt", "w") as arquivo:
    for numero in range(11,21):
        arquivo.write(f"{numero}\n")

with open("numeros.txt", "a") as arquivo:
    for numero in range(21,31):
        arquivo.write(f"{numero}\n")

with open("numeros.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip)