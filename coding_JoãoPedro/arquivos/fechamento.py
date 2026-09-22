alunos = []

while True:
    print("\n===== SISTEMA DE ALUNOS =====")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Pesquisar aluno")
    print("4 - Alterar aluno")
    print("5 - Remover aluno")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        aluno = {
            "nome": input("Nome: "),
            "idade": int(input("Idade: ")),
            "curso": input("Curso: "),
            "nota": float(input("Nota: "))
        }

        with open("alunos.txt", "a") as arquivo:
            arquivo.write(
                aluno["nome"] + ";" +
                str(aluno["idade"]) + ";" +
                aluno["curso"] + ";" +
                str(aluno["nota"]) + "\n"
            )

        print("Aluno cadastrado!")

    elif opcao == "2":
        with open("alunos.txt", "r") as arquivo:
            linhas = arquivo.readlines()

            for linha in linhas:
                dados = linha.strip().split(";")

                print("----------------")
                print("Nome:", dados[0])
                print("Idade:", dados[1])
                print("Curso:", dados[2])
                print("Nota:", dados[3])

    elif opcao == "3":
        nome = input("Digite o nome: ")

        with open("alunos.txt", "r") as arquivo:
            linhas = arquivo.readlines()

            encontrado = False

            for linha in linhas:
                dados = linha.strip().split(";")

                if dados[0].lower() == nome.lower():
                    print("Nome:", dados[0])
                    print("Idade:", dados[1])
                    print("Curso:", dados[2])
                    print("Nota:", dados[3])

                    encontrado = True

            if encontrado == False:
                print("Aluno não encontrado.")

    elif opcao == "6":
        print("Programa encerrado.")
        break

    else:
        print("Opção ainda não implementada.")