alunos = []


def cadastrar_aluno():
    nome = input("Nome do aluno: ")
    idade = int(input("Idade: "))
    curso = input("Curso: ")

    aluno = {
        "nome": nome,
        "idade": idade,
        "curso": curso
    }

    alunos.append(aluno)

    print("Aluno cadastrado com sucesso.")


def listar_alunos():
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
    else:
        for aluno in alunos:
            print("\nNome:", aluno["nome"])
            print("Idade:", aluno["idade"])
            print("Curso:", aluno["curso"])


def buscar_aluno():
    nome = input("Digite o nome do aluno: ")

    for aluno in alunos:
        if aluno["nome"].lower() == nome.lower():
            print("\nAluno encontrado!")
            print("Nome:", aluno["nome"])
            print("Idade:", aluno["idade"])
            print("Curso:", aluno["curso"])
            return

    print("Aluno não encontrado.")


def menu():
    while True:
        print("\n========== CADASTRO ==========")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Buscar")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_aluno()

        elif opcao == "2":
            listar_alunos()

        elif opcao == "3":
            buscar_aluno()

        elif opcao == "4":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida.")


menu()