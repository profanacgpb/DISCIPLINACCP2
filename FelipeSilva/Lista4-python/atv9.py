with open("numeros.txt", "w") as arquivo:
    for numero in range(1, 11):
        arquivo.write(f"{numero}\n")


with open("numeros.txt", "r") as arquivo:
    print("9b:")
    print(arquivo.read())


with open("numeros.txt", "w") as arquivo:
    for numero in range(11, 21):
        arquivo.write(f"{numero}\n")


with open("numeros.txt", "a") as arquivo:
    for numero in range(21, 31):
        arquivo.write(f"{numero}\n")


with open("numeros.txt", "r") as arquivo:
    print("9e:")
    print(arquivo.read())

with open("numeros.txt", "r") as arquivo:
    print("9f:")
    for linha in arquivo:
        print(linha.strip())