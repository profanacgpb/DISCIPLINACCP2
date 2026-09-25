alunos = [
    {
        "nome": "Alfredo",
        "idade": 18,
        "curso": "Ciência da Computação",
        "nota1":8.5,
        "nota2":7.0,
        "nota3":9.0
    }
]
def cadastrar_aluno():
    nome = input("Nome do aluno: ")
    idade = int(input("Idade do aluno: "))
    curso = input("Curso do aluno: ")
    nota1 = float(input("Nota 1 do aluno: "))
    nota2 = float(input("Nota 2 do aluno: "))
    nota3 = float(input("Nota 3 do aluno: "))

    alunos.append({
        "nome": nome,
        "idade": idade,
        "curso": curso,
        "nota1": nota1,
        "nota2": nota2,
        "nota3": nota3
    })

    print(f"Aluno {nome} cadastrado com sucesso!\n")
def listar_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado.\n")
        return

    for i, aluno in enumerate(alunos, start=1):
        print(f"{i}. Nome: {aluno['nome']} | Idade: {aluno['idade']} | Curso: {aluno['curso']} | Notas: {aluno['nota1']}, {aluno['nota2']}, {aluno['nota3']}")
    print()
def calcular_media(aluno):
    media = (aluno['nota1'] + aluno['nota2'] + aluno['nota3']) / 3
    return media
def verificar_situacao(aluno):
    media = calcular_media(aluno)
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"
def buscar_aluno():
    nome_busca = input("Digite o nome do aluno que deseja buscar: ")

    for aluno in alunos:
        if aluno["nome"].lower() == nome_busca.lower():
            media = calcular_media(aluno)
            situacao = verificar_situacao(aluno)
            print(f"Encontrado -> Nome: {aluno['nome']} | Idade: {aluno['idade']} | Curso: {aluno['curso']} | Notas: {aluno['nota1']}, {aluno['nota2']}, {aluno['nota3']} | Média: {media:.2f} | Situação: {situacao}\n")
            return

    print("Aluno não encontrado.\n")
def sair():
    print("Saindo do programa...")
    exit()
def menu():
    while True:
        print("===============" \
        "===== MENU =====" \
        "===============")
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
            sair()
        else:
            print("Opção inválida. Tente novamente.\n")
menu()