import os

NOME_FICHEIRO = "alunos.txt"


def carregar_alunos():
    """Lê o ficheiro e devolve uma lista de dicionários de alunos."""
    alunos = []
    if not os.path.exists(NOME_FICHEIRO):
        return alunos

    with open(NOME_FICHEIRO, "r", encoding="utf-8") as ficheiro:
        for linha in ficheiro:
            linha = linha.strip()
            if linha:
                partes = linha.split(";")
                if len(partes) == 4:
                    nome, idade, curso, nota = partes
                    alunos.append(
                        {
                            "nome": nome,
                            "idade": int(idade),
                            "curso": curso,
                            "nota": float(nota),
                        }
                    )
    return alunos


def guardar_alunos(alunos):
    """Guarda a lista completa de alunos no ficheiro."""
    with open(NOME_FICHEIRO, "w", encoding="utf-8") as ficheiro:
        for aluno in alunos:
            ficheiro.write(
                f"{aluno['nome']};{aluno['idade']};{aluno['curso']};{aluno['nota']}\n"
            )


def cadastrar_aluno(alunos):
    """Regista um novo aluno."""
    print("\n--- Cadastrar Aluno ---")
    nome = input("Nome: ").strip()
    idade = int(input("Idade: "))
    curso = input("Curso: ").strip()
    nota = float(input("Nota: "))

    aluno = {"nome": nome, "idade": idade, "curso": curso, "nota": nota}

    alunos.append(aluno)
    guardar_alunos(alunos)
    print(f"Aluno(a) '{nome}' cadastrado(a) com sucesso!")


def listar_alunos(alunos):
    """Lista todos os alunos registados."""
    print("\n--- Lista de Alunos ---")
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    for i, aluno in enumerate(alunos, 1):
        print(
            f"{i}. Nome: {aluno['nome']} | Idade: {aluno['idade']} | Curso: {aluno['curso']} | Nota: {aluno['nota']}"
        )


def pesquisar_aluno(alunos):
    """Pesquisa alunos pelo nome."""
    print("\n--- Pesquisar Aluno ---")
    nome_busca = input("Digite o nome (ou parte do nome) para pesquisar: ").strip().lower()
    encontrados = [
        a for a in alunos if nome_busca in a["nome"].lower()
    ]

    if encontrados:
        print("\nAlunos encontrados:")
        for aluno in encontrados:
            print(
                f"- Nome: {aluno['nome']} | Idade: {aluno['idade']} | Curso: {aluno['curso']} | Nota: {aluno['nota']}"
            )
    else:
        print("Nenhum aluno encontrado com esse nome.")


def alterar_aluno(alunos):
    """Altera os dados de um aluno existente."""
    print("\n--- Alterar Aluno ---")
    nome_busca = input("Digite o nome exato do aluno a alterar: ").strip().lower()

    for aluno in alunos:
        if aluno["nome"].lower() == nome_busca:
            print(f"Aluno encontrado: {aluno['nome']}")
            aluno["nome"] = input(f"Novo nome [{aluno['nome']}]: ") or aluno["nome"]
            idade_input = input(f"Nova idade [{aluno['idade']}]: ")
            if idade_input:
                aluno["idade"] = int(idade_input)
            aluno["curso"] = input(f"Novo curso [{aluno['curso']}]: ") or aluno["curso"]
            nota_input = input(f"Nova nota [{aluno['nota']}]: ")
            if nota_input:
                aluno["nota"] = float(nota_input)

            guardar_alunos(alunos)
            print("Dados do aluno atualizados com sucesso!")
            return

    print("Aluno não encontrado.")


def remover_aluno(alunos):
    """Remove um aluno registado."""
    print("\n--- Remover Aluno ---")
    nome_busca = input("Digite o nome exato do aluno a remover: ").strip().lower()

    for aluno in alunos:
        if aluno["nome"].lower() == nome_busca:
            alunos.remove(aluno)
            guardar_alunos(alunos)
            print(f"Aluno(a) '{aluno['nome']}' removido(a) com sucesso!")
            return

    print("Aluno não encontrado.")


def main():
    alunos = carregar_alunos()

    while True:
        print("\n==============================")
        print("SISTEMA DE ALUNOS")
        print("==============================")
        print("1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("3 - Pesquisar aluno")
        print("4 - Alterar aluno")
        print("5 - Remover aluno")
        print("6 - Sair")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_aluno(alunos)
        elif opcao == "2":
            listar_alunos(alunos)
        elif opcao == "3":
            pesquisar_aluno(alunos)
        elif opcao == "4":
            alterar_aluno(alunos)
        elif opcao == "5":
            remover_aluno(alunos)
        elif opcao == "6":
            print("A encerrar o sistema... Até breve!")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
    