with open("notas.txt", "w") as arquivo:
    arquivo.write("Luiza; 9.0\n")
    arquivo.write("Carlos; 6.0\n")
    arquivo.write("Maria; 7.0\n")
    arquivo.write("Manuel; 7.5\n")
    arquivo.write("Amanda; 8.0\n")
    arquivo.write("Ana; 8.0\n")
    arquivo.write("Kauã; 10.0\n")
    arquivo.write("Marina; 7.5\n")

with open("notas.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip())