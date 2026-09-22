with open("alunos.txt", "a") as arquivo:
    arquivo.write("Ana\n")
    arquivo.write("Kauã\n")
    arquivo.write("Marina\n")

with open("alunos.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip())