arquivo = open("alunos.txt", "a")

while True:
    nome = input("Digite o nome do aluno ou 'sair' para encerrar: ")

    if nome.lower() == "sair":
        break

    arquivo.write(nome + "\n")

arquivo.close()