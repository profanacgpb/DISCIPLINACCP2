with open("numeros.txt", "w") as arquivo:
    for numero in range(1, 21):
        arquivo.write(str(numero) + "\n")

with open("numeros.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip())
