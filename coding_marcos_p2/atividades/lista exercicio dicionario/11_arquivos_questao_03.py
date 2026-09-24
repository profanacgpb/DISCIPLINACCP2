with open("alunos.txt", "r") as arquivo:
    for linha in arquivo:
        print("Aluno:", linha.strip())
