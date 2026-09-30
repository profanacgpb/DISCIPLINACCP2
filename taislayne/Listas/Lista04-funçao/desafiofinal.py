alunos = []


def cadastrar_aluno():
    nome = input("Nome do aluno: ")
    idade = int(input("Idade: "))
    curso = input("Curso: ")

    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))

    aluno = {
        "nome": nome,
        "idade": idade,
        "curso": curso,
        "notas": [nota1, nota2, nota3]
    }

    alunos.append(aluno)

    print("\nAluno cadastrado com sucesso!")


def calcular_media(notas):
    return sum(notas) / len(notas)


def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 4:
        return "Recuperação"
    else:
        return "Reprovado"


def listar_alunos():
    if len(alunos) == 0:
        print("\nNenhum aluno cadastrado.")
        return

    print("\n===== LISTA DE ALUNOS =====")

    for aluno in alunos:
        media = calcular_media(aluno["notas"])
        situacao = verificar_situacao(media)

        print(f"\nNome: {aluno['nome']}")
        print(f"Idade: {aluno['idade']}")
        print(f"Curso: {aluno['curso']}")
        print(f"Média: {media:.2f}")
        print(f"Situação: {situacao}")


def buscar_aluno():
    nome = input("Digite o nome do aluno: ")

    for aluno in alunos:
        if aluno["nome"].lower() == nome.lower():
            media = calcular_media(aluno["notas"])
            situacao = verificar_situacao(media)

            print("\n===== ALUNO ENCONTRADO =====")
            print(f"Nome: {aluno['nome']}")
            print(f"Idade: {aluno['idade']}")
            print(f"Curso: {aluno['curso']}")
            print(f"Média: {media:.2f}")
            print(f"Situação: {situacao}")

            return

    print("\nAluno não encontrado.")


# PROGRAMA PRINCIPAL

while True:

    print("\n================================")
    print("       SISTEMA ACADÊMICO")
    print("================================")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Buscar aluno")
    print("4 - Sair")
    print("================================")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_aluno()

    elif opcao == "2":
        listar_alunos()

    elif opcao == "3":
        buscar_aluno()

    elif opcao == "4":
        print("\nSistema encerrado.")
        break

    else:
        print("\nOpção inválida!")