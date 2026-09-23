arquivo = open("numeros.txt", "w")

for numero in range(1, 21):
    arquivo.write(str(numero) + "\n")

arquivo.close()

arquivo = open("numeros.txt", "r")

for numero in arquivo:
    print(numero.strip())

arquivo.close()