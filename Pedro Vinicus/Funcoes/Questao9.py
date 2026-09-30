alunos = [
    {
        "Nome": "Ana",
        "Idade":20,
        "Curso": "Ciência da computação"
    }
]

def cadastrar_aluno():
    nome= input("Nome:")
    idade = int(input("Idade:"))
    curso = input("Curso:")
    
    aluno = {
        "Nome": nome,
        "Idade": idade,
        "Curso": curso
    }
    
    alunos.append(aluno)
    print("Aluno cadastrado!")
    
def listar_alunos():
    for aluno in alunos:
        print(f"Nome: {aluno['Nome']}")
        print(f"Idade:{aluno['Idade']}")
        print(f"Curso:{aluno['Curso']}")
        print("---")
        
def buscar_aluno():
    nome_buscar = input("Digite o nome do aluno:")
    
    for aluno in alunos:
        if aluno["Nome"].lower() == nome_buscar.lower():
            print(f"Nome: {aluno['Nome']}")
            print(f"Idade: {aluno['Idade']}")
            print(f"Curso: {aluno['Curso']}")
            return
        print("Aluno não encontrado.")
        
def menu():
    while True:
        print("=====Alunos=====")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Buscar")
        print("4 - Sair")
        
        opcao = input ("Escolha uma opção:")
        
        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            listar_alunos()
        elif opcao == "3":
            buscar_aluno()
        elif opcao == "4":
            break
        else:
            print("Opção invalida.")
            
menu()