tupla = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

try:
    tupla[2] = 10
except TypeError:
    print("Não é possível alterar um elemento da tupla")

print(tupla.index(5))


pessoas = {
    "nome": "Marcos",
    "idade": 18,
    "cidade": "Campina Grande",
    "curso": "Ciência da Computação",
    "semestre": 2
}

print(pessoas.keys())

print(pessoas.values())

print(pessoas.items())

print(list(pessoas.items())[1])

print(pessoas)

for chave, valor in pessoas.items():
    print(chave, "tem como valor", valor)


arquivo = open("numeros.txt", "w")

for numero in range(1, 11):
    arquivo.write(str(numero) + "\n")

arquivo.close()

arquivo = open("numeros.txt", "r")
print(arquivo.read())
arquivo.close()


arquivo = open("numeros.txt", "w")

for numero in range(11, 21):
    arquivo.write(str(numero) + "\n")

arquivo.close()


arquivo = open("numeros.txt", "a")

for numero in range(21, 31):
    arquivo.write(str(numero) + "\n")

arquivo.close()


arquivo = open("numeros.txt", "r")
print(arquivo.read())
arquivo.close()


arquivo = open("numeros.txt", "r")

for linha in arquivo:
    print(linha.strip())

arquivo.close()