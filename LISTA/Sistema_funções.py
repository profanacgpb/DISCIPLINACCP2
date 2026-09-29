# Sistema Acadêmico
alunos = []

def cadastrar_aluno():
    nome = input("Nome do aluno: ")
    nota1 = float(input("Digite a 1ª nota: "))
    nota2 = float(input("Digite a 2ª nota: "))
    aluno = {"nome": nome, "nota1": nota1, "nota2": nota2}
    alunos.append(aluno)
    print("Aluno cadastrado com sucesso!")
def listar_alunos():
    print("\n--- LISTA DE ALUNOS ---")
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado no momento.")
        return
    for aluno in alunos:
        print(f"Nome: {aluno['nome']} | Notas: {aluno['nota1']} e {aluno['nota2']}")
def buscar_aluno():
    nome_busca = input("Digite o nome para buscar: ")
    for aluno in alunos:
        if aluno["nome"].lower() == nome_busca.lower():
            print(f"Encontrado! Nome: {aluno['nome']} | Notas: {aluno['nota1']} e {aluno['nota2']}")
            return
    print("Aluno não encontrado.")
def calcular_media():
    nome_busca = input("Digite o nome do aluno: ")
    for aluno in alunos:
        if aluno["nome"].lower() == nome_busca.lower():
            media = (aluno["nota1"] + aluno["nota2"]) / 2
            print(f"A média do(a) {aluno['nome']} é {media}")
            return media
    print("Aluno não encontrado.")
    return 0
def verificar_situacao():
    nome_busca = input("Digite o nome do aluno: ")
    for aluno in alunos:
        if aluno["nome"].lower() == nome_busca.lower():
            media = (aluno["nota1"] + aluno["nota2"]) / 2
            if media >= 7:
                print(f"{aluno['nome']} está APROVADO.")
            elif media >= 5:
                print(f"{aluno['nome']} está EM RECUPERAÇÃO.")
            else:
                print(f"{aluno['nome']} está REPROVADO.")
            return
    print("Aluno não encontrado.")
    while True:
        print("\n========== SISTEMA ACADÊMICO ==========")
        print("1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("3 - Buscar aluno")
        print("4 - Calcular média")
        print("5 - Verificar situação")
        print("6 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar_aluno()
        elif opcao == '2':
            listar_alunos()
        elif opcao == '3':
            buscar_aluno()
        elif opcao == '4':
            calcular_media()
        elif opcao == '5':
            verificar_situacao()
        elif opcao == '6':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")