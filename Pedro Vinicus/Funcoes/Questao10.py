alunos = [
    {
        "Nome": "Ana",
        "Idade":20,
        "Curso": "Ciência da computação",
        "Nota1": 2,
        "Nota2":3,
        "Nota3":5
    }
]

def cadastrar_aluno():
    nome= input("Nome:").strip()
    idade = int(input("Idade:"))
    curso = input("Curso:")
    nota1 = int(input("Nota1:"))
    nota2= int(input("Nota2:"))
    nota3 = int(input("Nota3:"))
    
    aluno = {
        "Nome": nome,
        "Idade": idade,
        "Curso": curso,
        "Nota1": nota1,
        "Nota2": nota2,
        "Nota3": nota3
    }
    
    alunos.append(aluno)
    print("Aluno cadastrado!")
    
def listar_alunos():
    for aluno in alunos:
        print(f"Nome: {aluno['Nome']}")
        print(f"Idade:{aluno['Idade']}")
        print(f"Curso:{aluno['Curso']}")
        print(f"Nota1:{aluno['Nota1']}")
        print(f"Nota2:{aluno['Nota2']}")
        print(f"Nota3:{aluno['Nota3']}")
        print("---")

def media(nome_buscar):
    for aluno in alunos:
        if aluno["Nome"].strip().casefold() == nome_buscar.strip().casefold():
            return (aluno["Nota1"] + aluno["Nota2"] + aluno["Nota3"]) / 3

    return None

def situacao():
    nome_buscar = input("Digite o nome do aluno:").strip()
    
    for aluno in alunos :
        if aluno["Nome"].lower() == nome_buscar.lower():
            resultado = media(nome_buscar)
            if  resultado>= 7.0:
                    print("Situação:Aprovado")
            elif resultado >=6.0:
                print("Situção:Recuperação")
            else:
                 print("Situação:Reprovado")
            
    
        
        
def buscar_aluno():
    nome_buscar = input("Digite o nome do aluno: ").strip()

    for aluno in alunos:
        if aluno["Nome"].strip().casefold() == nome_buscar.casefold():
            resultado = media(nome_buscar)
            print(f"Nome: {aluno['Nome']}")
            print(f"Idade: {aluno['Idade']}")
            print(f"Curso: {aluno['Curso']}")
            print(f"Média: {resultado:.1f}")
            return

    print("Aluno não encontrado.")
        
        
    
        
def menu():
    while True:
        print("=====Alunos=====")
        print("1 - Cadastrar Aluno")
        print("2 - Listar Aluno")
        print("3 - Calcular média")
        print("4 - Verificar situação")
        print("5 - Buscar aluno")
        print("6 - Sair")
        
        
        opcao = input ("Escolha uma opção:")
        
        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            listar_alunos()
        elif opcao == "3":
            nome_buscar = input("Digite o nome do aluno: ").strip()
            resultado = media(nome_buscar)
            if resultado is None:
                print("Aluno não encontrado.")
            else:
                print(f"Média: {resultado:.1f}")
        elif opcao == "4":
            situacao()
        elif opcao == "5":
            buscar_aluno()
        elif opcao == "6":
            break
        else:
            print("Opção invalida.")
            
menu()