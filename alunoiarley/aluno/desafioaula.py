alunos = []

while True:
    print("\n===== MENU =====")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do aluno: ")
        idade = int(input("Digite a idade do aluno: "))
        curso = input("Digite o curso: ")

        aluno = {
            "nome": nome,
            "idade": idade,
            "curso": curso
        }

        alunos.append(aluno)

        print("Aluno cadastrado com sucesso!")

    elif opcao == "2":
        print("\n===== ALUNOS CADASTRADOS =====")

        if len(alunos) == 0:
            print("Nenhum aluno cadastrado.")
        else:
            for i, aluno in enumerate(alunos, start=1):
                print(f"\nAluno {i}")
                print(f"Nome: {aluno['nome']}")
                print(f"Idade: {aluno['idade']}")
                print(f"Curso: {aluno['curso']}")

    elif opcao == "3":
        print("Programa encerrado!")
        break

    else:
        print("Opção inválida!")