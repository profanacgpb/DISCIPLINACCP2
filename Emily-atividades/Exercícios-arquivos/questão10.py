with open("notas.txt", "w") as arquivo:
    arquivo.write("Luiza\n")
    arquivo.write("Carlos\n")
    arquivo.write("Maria\n")
    arquivo.write("Manuel\n")
    arquivo.write("Amanda\n")
    arquivo.write("Ana\n")
    arquivo.write("Kauã\n")
    arquivo.write("Marina\n")

with open("notas.txt", "r") as arquivo:
    for linha in arquivo:
        print ("Aluno(a):")
        print(linha.strip())