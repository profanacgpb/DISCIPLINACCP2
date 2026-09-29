alunos = []


def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade: "))
    curso = input("Digite o curso: ")

    aluno = {
        "nome": nome,
        "idade": idade,
        "curso": curso
    }

    alunos.append(aluno)

    print("Aluno cadastrado com sucesso!")


def listar_alunos():
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
    else:
        print("\n===== ALUNOS =====")

        for aluno in alunos:
            print(f"Nome: {aluno['nome']}")
            print(f"Idade: {aluno['idade']}")
            print(f"Curso: {aluno['curso']}")
            print("-----------------")


def buscar_aluno():
    nome = input("Digite o nome do aluno que deseja buscar: ")

    for aluno in alunos:
        if aluno["nome"].lower() == nome.lower():
            print("\nAluno encontrado!")
            print(f"Nome: {aluno['nome']}")
            print(f"Idade: {aluno['idade']}")
            print(f"Curso: {aluno['curso']}")
            return

    print("Aluno não encontrado.")


# Programa principal
while True:
    print("\n===== SISTEMA DE ALUNOS =====")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Buscar aluno")
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