alunos = []

while True:
    print("\n-------- CADASTRO DE ALUNOS --------")
    print("(1) Incluir aluno")
    print("(2) Listar alunos")
    print("(3) Remover aluno")
    print("(4) Sair")

    opcao = int(input("Digite uma opção: "))

    if opcao == 1:
        nome = input("Digite o nome do aluno: ")
        alunos.append(nome)
        print(f"Aluno {nome} cadastrado com sucesso!")

    elif opcao == 2:
        print("\n-------- ALUNOS CADASTRADOS --------")

        if len(alunos) == 0:
            print("Nenhum aluno cadastrado.")
        else:
            for aluno in alunos:
                print(aluno)

    elif opcao == 3:
        nome = input("Digite o nome do aluno que deseja remover: ")

        if nome in alunos:
            alunos.remove(nome)
            print(f"Aluno {nome} removido com sucesso!")
        else:
            print("Aluno não encontrado.")

    elif opcao == 4:
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida!")