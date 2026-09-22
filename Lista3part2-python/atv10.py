while True:

    print("\n===== MENU =====")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        nome = input("Digite o nome do aluno: ")

        arquivo = open("alunos.txt", "a")

        arquivo.write(nome + "\n")

        arquivo.close()

        print("Aluno cadastrado com sucesso!")

    elif opcao == "2":

        arquivo = open("alunos.txt", "r")

        print("\n===== ALUNOS =====")

        for nome in arquivo:
            print("Aluno:", nome.strip())

        arquivo.close()

    elif opcao == "3":

        print("Programa encerrado!")

        break

    else:

        print("Opção inválida!")