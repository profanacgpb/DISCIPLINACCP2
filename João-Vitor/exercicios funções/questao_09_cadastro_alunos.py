def cadastrar_aluno(alunos):
    aluno = {
        "nome": input("Nome: ").strip(),
        "idade": input("Idade: ").strip(),
        "curso": input("Curso: ").strip(),
    }
    alunos.append(aluno)
    print("Aluno cadastrado com sucesso.")


def listar_alunos(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    for indice, aluno in enumerate(alunos, start=1):
        print(f"{indice}. {aluno['nome']} | {aluno['idade']} anos | {aluno['curso']}")


def buscar_aluno(alunos):
    nome = input("Nome para buscar: ").strip().casefold()
    encontrados = [aluno for aluno in alunos if nome in aluno["nome"].casefold()]
    if not encontrados:
        print("Aluno não encontrado.")
        return
    for aluno in encontrados:
        print(f"Nome: {aluno['nome']} | Idade: {aluno['idade']} | Curso: {aluno['curso']}")


def menu():
    alunos = []
    while True:
        print("\n1 - Cadastrar\n2 - Listar\n3 - Buscar\n4 - Sair")
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            cadastrar_aluno(alunos)
        elif opcao == "2":
            listar_alunos(alunos)
        elif opcao == "3":
            buscar_aluno(alunos)
        elif opcao == "4":
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()
