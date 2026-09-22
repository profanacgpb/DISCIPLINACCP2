from pathlib import Path


alunos = []
arquivo_alunos = Path(__file__).resolve().parent.parent / "alunos.txt"

while True:
    print("\n===== SISTEMA DE CADASTRO =====")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        curso = input("Curso: ")

        aluno = {
            "nome": nome,
            "idade": idade,
            "curso": curso
        }

        alunos.append(aluno)

        with arquivo_alunos.open("a", encoding="cp1252") as arquivo:
            arquivo.write(
                nome + ";" + str(idade) + ";" + curso + "\n"
            )

        print("Aluno cadastrado com sucesso!")

    elif opcao == "2":
        with arquivo_alunos.open("r", encoding="cp1252") as arquivo:
            for linha in arquivo:
                nome, idade, curso = linha.strip().split(";")

                print("Nome:", nome)
                print("Idade:", idade)
                print("Curso:", curso)
                print("-------------------")

    elif opcao == "3":
        break

    else:
        print("Opção inválida!")