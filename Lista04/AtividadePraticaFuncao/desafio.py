#Desafio - Sistema Acadêmico
def cadastrar_aluno():
    matricula = input("Matrícula: ").strip()

    if matricula in alunos:
        print("Já existe um aluno com essa matrícula.")
        return

    nome = input("Nome: ").strip()
    idade = int(input("Idade: "))
    curso = input("Curso: ").strip()

    alunos[matricula] = {"nome": nome, "idade": idade, "curso": curso}
    print(f"Aluno {nome} cadastrado com sucesso!")


def listar_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    print("\n--- Lista de Alunos ---")
    for matricula, dados in alunos.items():
        print(f"Matrícula: {matricula} | Nome: {dados['nome']} | "
              f"Idade: {dados['idade']} | Curso: {dados['curso']}")


def buscar_aluno():
    termo = input("Digite a matrícula ou parte do nome: ").strip().lower()
    encontrados = False

    for matricula, dados in alunos.items():
        if termo == matricula.lower() or termo in dados["nome"].lower():
            print(f"Matrícula: {matricula} | Nome: {dados['nome']} | "
                  f"Idade: {dados['idade']} | Curso: {dados['curso']}")
            encontrados = True

    if not encontrados:
        print("Aluno não encontrado.")

alunos = {}  # {matricula: {"nome": ..., "idade": ..., "curso": ...}}

while True:
    print("\n1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Buscar aluno")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_aluno()
    elif opcao == "2":
        listar_alunos()
    elif opcao == "3":
            buscar_aluno()
    elif opcao == "0":
        print("Encerrando...")
        break
    else:
        print("Opção inválida.")