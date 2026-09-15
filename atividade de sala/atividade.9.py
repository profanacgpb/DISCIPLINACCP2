arquivo = open("numeros.txt", "w")

for i in range(1, 11):
    arquivo.write(str(i) + "\n")

arquivo.close()

arquivo = open("numeros.txt", "r")
print(arquivo.read())
arquivo.close()

arquivo = open("numeros.txt", "w")

for i in range(11, 21):
    arquivo.write(str(i) + "\n")

arquivo.close()


arquivo = open("numeros.txt", "a")

for i in range(21, 31):
    arquivo.write(str(i) + "\n")

arquivo.close()

arquivo = open("numeros.txt", "r")
print(arquivo.read())
arquivo.close()

arquivo = open("numeros.txt", "r")

for linha in arquivo:
    print(linha.strip())

arquivo.close()