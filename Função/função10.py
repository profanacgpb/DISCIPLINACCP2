alunos = []


def cadastrar_aluno():
    print("\n========== CADASTRO DE ALUNO ==========")

    nome = input("Nome: ")
    idade = int(input("Idade: "))
    curso = input("Curso: ")

    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))

    aluno = {
        "nome": nome,
        "idade": idade,
        "curso": curso,
        "nota1": nota1,
        "nota2": nota2,
        "nota3": nota3
    }

    alunos.append(aluno)

    print("Aluno cadastrado com sucesso!")


def listar_alunos():
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return

    print("\n========== LISTA DE ALUNOS ==========")

    for aluno in alunos:
        print(f"Nome: {aluno['nome']}")
        print(f"Idade: {aluno['idade']}")
        print(f"Curso: {aluno['curso']}")
        print(f"Nota 1: {aluno['nota1']}")
        print(f"Nota 2: {aluno['nota2']}")
        print(f"Nota 3: {aluno['nota3']}")
        print("------------------------------------")


def calcular_media(aluno):
    media = (
        aluno["nota1"]
        + aluno["nota2"]
        + aluno["nota3"]
    ) / 3

    return media


def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


def selecionar_aluno():
    nome = input("Digite o nome do aluno: ")

    for aluno in alunos:
        if aluno["nome"].lower() == nome.lower():
            return aluno

    return None


def mostrar_media():
    aluno = selecionar_aluno()

    if aluno is None:
        print("Aluno não encontrado.")
        return

    media = calcular_media(aluno)

    print(f"\nAluno: {aluno['nome']}")
    print(f"Média: {media:.1f}")


def mostrar_situacao():
    aluno = selecionar_aluno()

    if aluno is None:
        print("Aluno não encontrado.")
        return

    media = calcular_media(aluno)
    situacao = verificar_situacao(media)

    print(f"\nAluno: {aluno['nome']}")
    print(f"Média: {media:.1f}")
    print(f"Situação: {situacao}")


def buscar_aluno():
    aluno = selecionar_aluno()

    if aluno is None:
        print("Aluno não encontrado.")
        return

    print("\n========== ALUNO ENCONTRADO ==========")
    print(f"Nome: {aluno['nome']}")
    print(f"Idade: {aluno['idade']}")
    print(f"Curso: {aluno['curso']}")
    print(f"Nota 1: {aluno['nota1']}")
    print(f"Nota 2: {aluno['nota2']}")
    print(f"Nota 3: {aluno['nota3']}")


def menu():
    while True:
        print("\n========================================")
        print("           SISTEMA ACADÊMICO")
        print("========================================")
        print("1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("3 - Calcular média")
        print("4 - Verificar situação")
        print("5 - Buscar aluno")
        print("6 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_aluno()

        elif opcao == "2":
            listar_alunos()

        elif opcao == "3":
            mostrar_media()

        elif opcao == "4":
            mostrar_situacao()

        elif opcao == "5":
            buscar_aluno()

        elif opcao == "6":
            print("Sistema encerrado.")
            break

        else:
            print("Opção inválida.")


menu()