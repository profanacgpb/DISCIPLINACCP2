while True:

    print("\n1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        nome = input("Digite o nome do aluno: ")

        arquivo = open("alunos.txt", "a")
        arquivo.write(nome + "\n")
        arquivo.close()

        print("Aluno cadastrado!")

    elif opcao == "2":

        arquivo = open("alunos.txt", "r")

        print("\nLista de alunos:")

        for nome in arquivo:
            print("-", nome.strip())

        arquivo.close()

    elif opcao == "3":

        print("Programa encerrado.")
        break

    else:

        print("Opção inválida.")