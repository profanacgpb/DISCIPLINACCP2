def cadastrar_aluno(alunos):
    matricula = input("Digite a matrícula do aluno: ").strip()
    if not matricula:
        print("A matrícula não pode ficar vazia.")
        return
    if matricula in alunos:
        print("Já existe um aluno com essa matrícula.")
        return

    nome = input("Digite o nome do aluno: ").strip()
    if not nome:
        print("O nome não pode ficar vazio.")
        return

    alunos[matricula] = nome
    print("Aluno cadastrado com sucesso!")


def listar_alunos(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    print("\nAlunos cadastrados:")
    for matricula, nome in alunos.items():
        print(f"Matrícula: {matricula} | Nome: {nome}")


def buscar_aluno(alunos):
    matricula = input("Digite a matrícula que deseja buscar: ").strip()
    if matricula in alunos:
        print(f"Matrícula: {matricula} | Nome: {alunos[matricula]}")
    else:
        print("Aluno não encontrado.")


def main():
    alunos = {}
    while True:
        print("\nCadastro de alunos")
        print("1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("3 - Buscar aluno")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_aluno(alunos)
        elif opcao == "2":
            listar_alunos(alunos)
        elif opcao == "3":
            buscar_aluno(alunos)
        elif opcao == "0":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
