alunos = []


def cadastrar_aluno():
    aluno = {
        "nome": input("Nome: "),
        "idade": int(input("Idade: ")),
        "curso": input("Curso: "),
        "nota1": float(input("Nota 1: ")),
        "nota2": float(input("Nota 2: ")),
        "nota3": float(input("Nota 3: "))
    }

    alunos.append(aluno)
    print("Aluno cadastrado com sucesso!")


def listar_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    for aluno in alunos:
        print("\nNome:", aluno["nome"])
        print("Idade:", aluno["idade"])
        print("Curso:", aluno["curso"])
        print("Nota 1:", aluno["nota1"])
        print("Nota 2:", aluno["nota2"])
        print("Nota 3:", aluno["nota3"])
        print("Média:", round(calcular_media(aluno), 2))
        print("Situação:", verificar_situacao(calcular_media(aluno)))


def buscar_aluno():
    nome = input("Nome do aluno: ")

    for aluno in alunos:
        if aluno["nome"].lower() == nome.lower():
            return aluno

    return None


def calcular_media(aluno):
    return (aluno["nota1"] + aluno["nota2"] + aluno["nota3"]) / 3


def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


def remover_aluno():
    aluno = buscar_aluno()

    if aluno:
        alunos.remove(aluno)
        print("Aluno removido com sucesso!")
    else:
        print("Aluno não encontrado.")


def alterar_dados():
    aluno = buscar_aluno()

    if aluno:
        aluno["idade"] = int(input("Nova idade: "))
        aluno["curso"] = input("Novo curso: ")
        aluno["nota1"] = float(input("Nova nota 1: "))
        aluno["nota2"] = float(input("Nova nota 2: "))
        aluno["nota3"] = float(input("Nova nota 3: "))

        print("Dados alterados com sucesso!")
    else:
        print("Aluno não encontrado.")


def maior_media():
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    maior = alunos[0]

    for aluno in alunos:
        if calcular_media(aluno) > calcular_media(maior):
            maior = aluno

    print("\nAluno com maior média:")
    print("Nome:", maior["nome"])
    print("Média:", round(calcular_media(maior), 2))


def media_geral():
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    soma = 0

    for aluno in alunos:
        soma += calcular_media(aluno)

    media = soma / len(alunos)

    print("Média geral da turma:", round(media, 2))


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
        print("7 - Remover aluno")
        print("8 - Alterar dados")
        print("9 - Mostrar aluno com maior média")
        print("10 - Mostrar média geral da turma")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_aluno()

        elif opcao == "2":
            listar_alunos()

        elif opcao == "3":
            aluno = buscar_aluno()

            if aluno:
                print("Média:", round(calcular_media(aluno), 2))
            else:
                print("Aluno não encontrado.")

        elif opcao == "4":
            aluno = buscar_aluno()

            if aluno:
                media = calcular_media(aluno)
                print("Situação:", verificar_situacao(media))
            else:
                print("Aluno não encontrado.")

        elif opcao == "5":
            aluno = buscar_aluno()

            if aluno:
                print("Nome:", aluno["nome"])
                print("Idade:", aluno["idade"])
                print("Curso:", aluno["curso"])
            else:
                print("Aluno não encontrado.")

        elif opcao == "6":
            print("Programa encerrado.")
            break

        elif opcao == "7":
            remover_aluno()

        elif opcao == "8":
            alterar_dados()

        elif opcao == "9":
            maior_media()

        elif opcao == "10":
            media_geral()

        else:
            print("Opção inválida.")


menu()
