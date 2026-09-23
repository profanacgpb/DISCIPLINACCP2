arquivo = open("alunos.txt", "a")

quantidade = int(input("Quantos alunos deseja cadastrar? "))

for i in range(quantidade):
    nome = input("Digite o nome do aluno: ")
    arquivo.write(nome + "\n")

arquivo.close()

print("Alunos cadastrados com sucesso!")