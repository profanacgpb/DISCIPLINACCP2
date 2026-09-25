alunos = [
    {
        "nome": "Alfredo",
        "idade": 18,
        "curso": "Ciência da Computação"
    }
]


def cadastrar_aluno():
    nome = input("Nome do aluno: ")
    idade = int(input("Idade do aluno: "))
    curso = input("Curso do aluno: ")                          #talvez isso seja o deminio em forma de codigo

    alunos.append({
        "nome": nome,
        "idade": idade,                  #ESTÁ MERDA ESTA CADASTRANDO 99 ALUNOS NESTA PORR*
        "curso": curso                   #resolvi<3
    })

    print(f"Aluno {nome} cadastrado com sucesso!\n")


def listar_alunos():
    if not alunos:                                             #espero q funcione direito esse negocio
        print("Nenhum aluno cadastrado.\n")                    
        return

    for i, aluno in enumerate(alunos, start=1):
        print(f"{i}. Nome: {aluno['nome']} | Idade: {aluno['idade']} | Curso: {aluno['curso']}")
    print()


def buscar_aluno():
    nome_busca = input("Digite o nome do aluno que deseja buscar: ")

    for aluno in alunos:
        if aluno["nome"].lower() == nome_busca.lower():
            print(f"Encontrado -> Nome: {aluno['nome']} | Idade: {aluno['idade']} | Curso: {aluno['curso']}\n")
            return

    print("Aluno não encontrado.\n")


def menu():
    while True:
        print("===== MENU =====")
        print("1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("3 - Buscar aluno")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            listar_alunos()
        elif opcao == "3":
            buscar_aluno()
        elif opcao == "4":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida.\n")
            break

menu()