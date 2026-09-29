# ============================================
#       SISTEMA ACADÊMICO
# ============================================

alunos = []


# --------------------------------------------
# 1. Cadastrar aluno
# --------------------------------------------
def cadastrar_aluno():
    print("\n========================================")
    print("          CADASTRO DE ALUNO")
    print("========================================")

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

    print("\nAluno cadastrado com sucesso!")


# --------------------------------------------
# 2. Listar alunos
# --------------------------------------------
def listar_alunos():
    print("\n========================================")
    print("          ALUNOS CADASTRADOS")
    print("========================================")

    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return

    for aluno in alunos:
        print(f"\nNome: {aluno['nome']}")
        print(f"Idade: {aluno['idade']}")
        print(f"Curso: {aluno['curso']}")
        print(f"Nota 1: {aluno['nota1']:.2f}")
        print(f"Nota 2: {aluno['nota2']:.2f}")
        print(f"Nota 3: {aluno['nota3']:.2f}")


# --------------------------------------------
# 3. Calcular média
# --------------------------------------------
def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media


def mostrar_media():
    print("\n========================================")
    print("             CALCULAR MÉDIA")
    print("========================================")

    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return

    nome = input("Digite o nome do aluno: ")

    for aluno in alunos:

        if aluno["nome"].lower() == nome.lower():

            media = calcular_media(
                aluno["nota1"],
                aluno["nota2"],
                aluno["nota3"]
            )

            print(f"\nAluno: {aluno['nome']}")
            print(f"Média: {media:.2f}")

            return

    print("Aluno não encontrado.")


# --------------------------------------------
# 4. Verificar situação
# --------------------------------------------
def verificar_situacao(media):

    if media >= 7:
        return "Aprovado"

    elif media >= 5:
        return "Recuperação"

    else:
        return "Reprovado"


def mostrar_situacao():

    print("\n========================================")
    print("          SITUAÇÃO DO ALUNO")
    print("========================================")

    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return

    nome = input("Digite o nome do aluno: ")

    for aluno in alunos:

        if aluno["nome"].lower() == nome.lower():

            media = calcular_media(
                aluno["nota1"],
                aluno["nota2"],
                aluno["nota3"]
            )

            situacao = verificar_situacao(media)

            print(f"\nAluno: {aluno['nome']}")
            print(f"Média: {media:.2f}")
            print(f"Situação: {situacao}")

            return

    print("Aluno não encontrado.")


# --------------------------------------------
# 5. Buscar aluno
# --------------------------------------------
def buscar_aluno():

    print("\n========================================")
    print("             BUSCAR ALUNO")
    print("========================================")

    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return

    nome = input("Digite o nome do aluno: ")

    for aluno in alunos:

        if aluno["nome"].lower() == nome.lower():

            media = calcular_media(
                aluno["nota1"],
                aluno["nota2"],
                aluno["nota3"]
            )

            situacao = verificar_situacao(media)

            print("\nAluno encontrado!")
            print("----------------------------------------")
            print(f"Nome: {aluno['nome']}")
            print(f"Idade: {aluno['idade']}")
            print(f"Curso: {aluno['curso']}")
            print(f"Nota 1: {aluno['nota1']:.2f}")
            print(f"Nota 2: {aluno['nota2']:.2f}")
            print(f"Nota 3: {aluno['nota3']:.2f}")
            print(f"Média: {media:.2f}")
            print(f"Situação: {situacao}")
            print("----------------------------------------")

            return

    print("Aluno não encontrado.")


# --------------------------------------------
# MENU PRINCIPAL
# --------------------------------------------
def menu():

    while True:

        print("\n========================================")
        print("          SISTEMA ACADÊMICO")
        print("========================================")
        print("1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("3 - Calcular média")
        print("4 - Verificar situação")
        print("5 - Buscar aluno")
        print("6 - Sair")
        print("========================================")

        opcao = input("Digite uma opção: ")

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
            print("\n========================================")
            print("Obrigado por utilizar o Sistema Acadêmico!")
            print("========================================")
            break

        else:
            print("\nOpção inválida! Tente novamente.")


# --------------------------------------------
# EXECUÇÃO DO PROGRAMA
# --------------------------------------------

menu()