arquivo = open("alunos.txt", "r")

for aluno in arquivo:
    print(aluno.strip())

arquivo.close()