with open("compras.txt", "w") as arquivo:
    arquivo.write("Arroz\n")
    arquivo.write("Macarrão\n")
    arquivo.write("Feijão\n")
    arquivo.write("Linguiça\n")
    arquivo.write("Tomate\n")

with open("compras.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip())