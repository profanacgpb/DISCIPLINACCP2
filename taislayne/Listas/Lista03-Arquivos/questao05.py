arquivo = open("numeros.txt", "a")

for numero in range(21, 31):
    arquivo.write(str(numero) + "\n")

arquivo.close()

arquivo = open("numeros.txt", "r")

for numero in arquivo:
    print(numero.strip())

arquivo.close()