while True:
    print("\n===== MENU =====")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do aluno: ")
    

        with open("alunos.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(nome + "\n")

        print("Aluno cadastrado com sucesso!")

    elif opcao == "2":
        print("\n===== ALUNOS CADASTRADOS =====")

        with open("alunos.txt", "r", encoding="utf-8") as arquivo:
            alunos = arquivo.readlines()

            if len(alunos) == 0:
                print("Nenhum aluno cadastrado.")
            else:
                for i, aluno in enumerate(alunos, start=1):
                    print(f"{i}. {aluno.strip()}")

    elif opcao == "3":
        print("Programa encerrado!")
        break

    else:
        print("Opção inválida!")