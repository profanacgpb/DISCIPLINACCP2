nome = input("Digite o nome do aluno: ")

with open("alunos.txt", "a") as arquivo:
    arquivo.write(nome + "\n")

print("Aluno cadastrado com sucesso!")
