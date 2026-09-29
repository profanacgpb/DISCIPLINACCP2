alunos = []


def cadastrar_aluno():
    print("\n===== CADASTRAR ALUNO =====")

    nome = input("Nome: ")
    idade = int(input("Idade: "))
    curso = input("Curso: ")

    aluno = {
        "nome": nome,
        "idade": idade,
        "curso": curso,
        "notas": []
    }

    alunos.append(aluno)

    print("Aluno cadastrado com sucesso!")


def listar_alunos():
    print("\n===== LISTA DE ALUNOS =====")

    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return

    for i, aluno in enumerate(alunos, start=1):
        print(f"\nAluno {i}")
        print(f"Nome: {aluno['nome']}")
        print(f"Idade: {aluno['idade']}")
        print(f"Curso: {aluno['curso']}")


def buscar_aluno():
    print("\n===== BUSCAR ALUNO =====")

    nome = input("Digite o nome do aluno: ")

    for aluno in alunos:
        if aluno["nome"].lower() == nome.lower():
            print("\nAluno encontrado!")
            print(f"Nome: {aluno['nome']}")
            print(f"Idade: {aluno['idade']}")
            print(f"Curso: {aluno['curso']}")
            return aluno

    print("Aluno não encontrado.")
    return None


def calcular_media():
    print("\n===== CALCULAR MÉDIA =====")

    aluno = buscar_aluno()

    if aluno is None:
        return

    notas = []

    for i in range(3):
        nota = float(input(f"Digite a {i + 1}ª nota: "))
        notas.append(nota)

    aluno["notas"] = notas

    media = sum(notas) / len(notas)

    print(f"Média do aluno: {media:.2f}")

    return media


def verificar_situacao():
    print("\n===== VERIFICAR SITUAÇÃO =====")

    aluno = buscar_aluno()

    if aluno is None:
        return

    if len(aluno["notas"]) == 0:
        print("O aluno ainda não possui notas cadastradas.")
        return

    media = sum(aluno["notas"]) / len(aluno["notas"])

    if media >= 7:
        situacao = "Aprovado"

    elif media >= 5:
        situacao = "Recuperação"

    else:
        situacao = "Reprovado"

    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")


def menu():
    while True:
        print("\n========== SISTEMA ACADÊMICO ==========")
        print("1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("3 - Buscar aluno")
        print("4 - Calcular média")
        print("5 - Verificar situação")
        print("6 - Sair")
        print("========================================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_aluno()

        elif opcao == "2":
            listar_alunos()

        elif opcao == "3":
            buscar_aluno()

        elif opcao == "4":
            calcular_media()

        elif opcao == "5":
            verificar_situacao()

        elif opcao == "6":
            print("Sistema encerrado.")
            break

        else:
            print("Opção inválida. Tente novamente.")


menu()