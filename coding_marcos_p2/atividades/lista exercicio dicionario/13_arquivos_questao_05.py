with open("numeros.txt", "a") as arquivo:
    for numero in range(21, 31):
        arquivo.write(str(numero) + "\n")

with open("numeros.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip())
