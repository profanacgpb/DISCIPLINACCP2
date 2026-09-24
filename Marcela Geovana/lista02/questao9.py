with open("numeros.txt", "w") as arquivo:
    for numero in range(1, 11):
        arquivo.write(f"{numero}\n")

with open("numeros.txt", "r") as arquivo:
    print(arquivo.read())

with open("numeros.txt", "w") as arquivo:
    for numero in range(11, 21):
        arquivo.write(f"{numero}\n")

with open("numeros.txt", "a") as arquivo:
    for numero in range(21, 31):
        arquivo.write(f"{numero}\n")

with open("numeros.txt", "r") as arquivo:
    print(arquivo.read())

with open("numeros.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip())
