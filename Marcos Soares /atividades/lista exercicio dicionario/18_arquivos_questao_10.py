while True:
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do aluno: ")

        with open("alunos.txt", "a") as arquivo:
            arquivo.write(nome + "\n")

        print("Aluno cadastrado com sucesso!")

    elif opcao == "2":
        with open("alunos.txt", "r") as arquivo:
            for linha in arquivo:
                print(linha.strip())

    elif opcao == "3":
        break

    else:
        print("Opção inválida.")
