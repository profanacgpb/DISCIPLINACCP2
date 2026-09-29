while True:
    print("================================")
    print("SISTEMA DE ALUNOS")
    print("================================")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Pesquisar aluno")
    print("4 - Alterar aluno")
    print("5 - Remover aluno")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        aluno = {}
        aluno["nome"] = input("Nome: ")
        aluno["idade"] = input("Idade: ")
        aluno["curso"] = input("Curso: ")
        aluno["nota"] = input("Nota: ")

        with open("alunos.txt", "a") as arquivo:
            linha = (
                aluno["nome"] + ";" +
                aluno["idade"] + ";" +
                aluno["curso"] + ";" +
                aluno["nota"] + "\n"
            )
            arquivo.write(linha)

        print("Aluno cadastrado com sucesso!")

    elif opcao == "2":
        with open("alunos.txt", "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(";")
                print("Nome:", dados[0])
                print("Idade:", dados[1])
                print("Curso:", dados[2])
                print("Nota:", dados[3])

    elif opcao == "3":
        pesquisa = input("Digite o nome do aluno: ")
        encontrado = False

        with open("alunos.txt", "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(";")

                if dados[0] == pesquisa:
                    print("Nome:", dados[0])
                    print("Idade:", dados[1])
                    print("Curso:", dados[2])
                    print("Nota:", dados[3])
                    encontrado = True

        if encontrado == False:
            print("Aluno não encontrado.")

    elif opcao == "4":
        pesquisa = input("Nome do aluno que deseja alterar: ")
        linhas_novas = []
        encontrado = False

        with open("alunos.txt", "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(";")

                if dados[0] == pesquisa:
                    nome = input("Nome: ")
                    idade = input("Idade: ")
                    curso = input("Curso: ")
                    nota = input("Nota: ")

                    nova_linha = (
                        nome + ";" +
                        idade + ";" +
                        curso + ";" +
                        nota + "\n"
                    )

                    linhas_novas.append(nova_linha)
                    encontrado = True
                else:
                    linhas_novas.append(linha)

        with open("alunos.txt", "w") as arquivo:
            arquivo.writelines(linhas_novas)

        if encontrado:
            print("Aluno alterado com sucesso!")
        else:
            print("Aluno não encontrado.")

    elif opcao == "5":
        pesquisa = input("Nome do aluno que deseja remover: ")
        linhas_novas = []
        encontrado = False

        with open("alunos.txt", "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(";")

                if dados[0] == pesquisa:
                    encontrado = True
                else:
                    linhas_novas.append(linha)

        with open("alunos.txt", "w") as arquivo:
            arquivo.writelines(linhas_novas)

        if encontrado:
            print("Aluno removido com sucesso!")
        else:
            print("Aluno não encontrado.")

    elif opcao == "6":
        break

    else:
        print("Opção inválida.")
