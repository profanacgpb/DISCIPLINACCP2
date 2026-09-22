arquivo = open("professores.txt", "r")

for nome in arquivo:
    print("Professor(a)", nome.strip())

arquivo.close()