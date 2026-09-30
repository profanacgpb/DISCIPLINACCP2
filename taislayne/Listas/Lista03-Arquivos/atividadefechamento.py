ARQUIVO = "alunos.txt"


def carregar_alunos():
    alunos = []

    try:
        with open(ARQUIVO, "r") as arquivo:
            linhas = arquivo.readlines()

            for linha in linhas:
                dados = linha.strip().split(";")

                if len(dados) == 4:
                    aluno = {
                        "nome": dados[0],
                        "idade": int(dados[1]),
                        "curso": dados[2],
                        "nota": float(dados[3])
                    }

                    alunos.append(aluno)

    except FileNotFoundError:
        pass

    return alunos


def salvar_alunos(alunos):
    with open(ARQUIVO, "w") as arquivo:
        for aluno in alunos:
            arquivo.write(
                aluno["nome"] + ";" +
                str(aluno["idade"]) + ";" +
                aluno["curso"] + ";" +
                str(aluno["nota"]) + "\n"
            )


alunos = carregar_alunos()


while True:

    print("\n================================")
    print("        SISTEMA DE ALUNOS")
    print("================================")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Pesquisar aluno")
    print("4 - Alterar aluno")
    print("5 - Remover aluno")
    print("6 - Sair")
    print("================================")

    opcao = input("Escolha uma opção: ")


    if opcao == "1":

        nome = input("Nome: ")
        idade = int(input("Idade: "))
        curso = input("Curso: ")
        nota = float(input("Nota: "))

        aluno = {
            "nome": nome,
            "idade": idade,
            "curso": curso,
            "nota": nota
        }

        alunos.append(aluno)
        salvar_alunos(alunos)

        print("Aluno cadastrado com sucesso!")



    elif opcao == "2":

        if len(alunos) == 0:
            print("Nenhum aluno cadastrado.")

        else:
            print("\n--- LISTA DE ALUNOS ---")

            for aluno in alunos:
                print("Nome:", aluno["nome"])
                print("Idade:", aluno["idade"])
                print("Curso:", aluno["curso"])
                print("Nota:", aluno["nota"])
                print("------------------------")



    elif opcao == "3":

        nome_pesquisa = input("Digite o nome do aluno: ")

        encontrado = False

        for aluno in alunos:

            if aluno["nome"].lower() == nome_pesquisa.lower():

                print("\nAluno encontrado!")
                print("Nome:", aluno["nome"])
                print("Idade:", aluno["idade"])
                print("Curso:", aluno["curso"])
                print("Nota:", aluno["nota"])

                encontrado = True

        if encontrado == False:
            print("Aluno não encontrado.")



    elif opcao == "4":

        nome_pesquisa = input("Digite o nome do aluno que deseja alterar: ")

        encontrado = False

        for aluno in alunos:

            if aluno["nome"].lower() == nome_pesquisa.lower():

                print("\nAluno encontrado!")

                aluno["nome"] = input("Novo nome: ")
                aluno["idade"] = int(input("Nova idade: "))
                aluno["curso"] = input("Novo curso: ")
                aluno["nota"] = float(input("Nova nota: "))

                encontrado = True

                salvar_alunos(alunos)

                print("Aluno alterado com sucesso!")

                break

        if encontrado == False:
            print("Aluno não encontrado.")


    
    elif opcao == "5":

        nome_pesquisa = input("Digite o nome do aluno que deseja remover: ")

        encontrado = False

        for aluno in alunos:

            if aluno["nome"].lower() == nome_pesquisa.lower():

                alunos.remove(aluno)

                salvar_alunos(alunos)

                print("Aluno removido com sucesso!")

                encontrado = True

                break

        if encontrado == False:
            print("Aluno não encontrado.")



    elif opcao == "6":

        print("Sistema encerrado!")
        break


    else:
        print("Opção inválida!")