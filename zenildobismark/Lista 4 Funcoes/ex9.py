#QUESTÃO 09 — Sistema de cadastro de alunos Crie um sistema com 1-Cadastrar, 2-Listar, 3-Buscar e 4-Sair. 
# Cada aluno possui Nome, Idade e Curso. 
# Use uma lista de dicionários e as funções cadastrar_aluno(), listar_alunos(), buscar_aluno() e menu().

# Lista global de alunos iniciada com o exemplo da questão
alunos = [
    {
        "nome": "Ana",
        "idade": 20,
        "curso": "Ciência da Computação"
    }
]

def cadastrar_aluno():
    print("\n--- CADASTRAR ALUNO ---")
    nome = input("Digite o nome do aluno: ").strip()
    idade = int(input("Digite a idade do aluno: "))
    curso = input("Digite o curso do aluno: ").strip()

    aluno = {
        "nome": nome,
        "idade": idade,
        "curso": curso
    }

    alunos.append(aluno)
    print(f"\nAluno(a) '{nome}' cadastrado(a) com sucesso!")

def listar_alunos():
    print("\n--- LISTA DE ALUNOS ---")
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    for i, aluno in enumerate(alunos, start=1):
        print(f"{i}. Nome: {aluno['nome']} | Idade: {aluno['idade']} | Curso: {aluno['curso']}")

def buscar_aluno():
    print("\n--- BUSCAR ALUNO ---")
    if not alunos:
        print("Nenhum aluno cadastrado para busca.")
        return

    nome_busca = input("Digite o nome do aluno que deseja buscar: ").strip().lower()
    encontrado = False

    for aluno in alunos:
        if aluno['nome'].lower() == nome_busca:
            print("\nAluno encontrado:")
            print(f"Nome: {aluno['nome']} | Idade: {aluno['idade']} | Curso: {aluno['curso']}")
            encontrado = True
            break

    if not encontrado:
        print("\nAluno não encontrado na lista.")

def menu():
    while True:
        print("\n================ MENU ================")
        print("1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("3 - Buscar aluno")
        print("4 - Sair")

        opcao = input("Escolha uma opção (1-4): ").strip()

        if opcao == '1':
            cadastrar_aluno()
        elif opcao == '2':
            listar_alunos()
        elif opcao == '3':
            buscar_aluno()
        elif opcao == '4':
            print("\nSaindo do sistema... Até logo!")
            break
        else:
            print("\nOpção inválida! Digite um número entre 1 e 4.")

menu()