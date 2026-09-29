alunos = []


def cadastrar_aluno():
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

    print("Aluno cadastrado com sucesso.")


def listar_alunos():
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return

    for aluno in alunos:
        print("\nNome:", aluno["nome"])
        print("Idade:", aluno["idade"])
        print("Curso:", aluno["curso"])
        print("Nota 1:", aluno["nota1"])
        print("Nota 2:", aluno["nota2"])
        print("Nota 3:", aluno["nota3"])


def calcular_media(aluno):
    media = (aluno["nota1"] + aluno["nota2"] + aluno["nota3"]) / 3
    return media


def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


def buscar_aluno():
    nome = input("Digite o nome do aluno: ")

    for aluno in alunos:
        if aluno["nome"].lower() == nome.lower():
            print("\nAluno encontrado!")
            print("Nome:", aluno["nome"])
            print("Idade:", aluno["idade"])
            print("Curso:", aluno["curso"])
            return aluno

    print("Aluno não encontrado.")
    return None


def menu():
    while True:
        print("\n================================")
        print("        SISTEMA ACADÊMICO")
        print("================================")
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
            aluno = buscar_aluno()

            if aluno is not None:
                media = calcular_media(aluno)
                print("Média:", media)

        elif opcao == "4":
            aluno = buscar_aluno()

            if aluno is not None:
                media = calcular_media(aluno)
                situacao = verificar_situacao(media)

                print("Média:", media)
                print("Situação:", situacao)

        elif opcao == "5":
            buscar_aluno()

        elif opcao == "6":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida.")


menu()