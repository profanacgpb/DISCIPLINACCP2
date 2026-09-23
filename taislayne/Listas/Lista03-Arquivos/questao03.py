arquivo = open("alunos.txt", "r")

for nome in arquivo:
    print("Aluno:", nome.strip())

arquivo.close()