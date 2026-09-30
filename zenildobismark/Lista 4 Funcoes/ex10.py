alunos = [
    {
        "nome": "Ana",
        "idade": 20,
        "curso": "ADS",
        "notas": [8.5, 7.0, 9.0]
    },
    {
        "nome": "Carlos",
        "idade": 22,
        "curso": "Engenharia",
        "notas": [5.0, 6.0, 4.5]
    }
]

def calcular_media_aluno(notas):
    if not notas:
        return 0.0
    return sum(notas) / len(notas)

def determinar_situacao(media):
    if media >= 7.0:
        return "Aprovado(a)"
    elif 5.0 <= media < 7.0:
        return "Recuperação"
    else:
        return "Reprovado(a)"

def cadastrar_aluno():
    print("\n--- 1. CADASTRAR ALUNO ---")
    nome = input("Nome do aluno: ").strip()
    
    while True:
        try:
            idade = int(input("Idade: "))
            break
        except ValueError:
            print("Por favor, digite um número inteiro válido para a idade.")

    curso = input("Curso: ").strip()

    notas = []
    for i in range(1, 4):
        while True:
            try:
                nota = float(input(f"Digite a Nota {i} (0 a 10): "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("A nota deve estar entre 0 e 10.")
            except ValueError:
                print("Entrada inválida. Digite um número para a nota.")

    aluno = {
        "nome": nome,
        "idade": idade,
        "curso": curso,
        "notas": notas
    }

    alunos.append(aluno)
    print(f"\nAluno(a) {nome} cadastrado(a) com sucesso!")

def listar_alunos():
    print("\n--- 2. LISTA DE ALUNOS ---")
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    for i, aluno in enumerate(alunos, start=1):
        n1, n2, n3 = aluno["notas"]
        print(f"{i}. Nome: {aluno['nome']} | Idade: {aluno['idade']} | Curso: {aluno['curso']}")
        print(f"   Notas: [1ª: {n1:.1f} | 2ª: {n2:.1f} | 3ª: {n3:.1f}]")
        print("-" * 50)

def exibir_medias():
    print("\n--- 3. CALCULAR MÉDIA ---")
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    soma_medias_turma = 0

    for aluno in alunos:
        media = calcular_media_aluno(aluno["notas"])
        soma_medias_turma += media
        print(f"Aluno(a): {aluno['nome']} | Média: {media:.2f}")

    media_geral = soma_medias_turma / len(alunos)
    print("=" * 40)
    print(f"Média geral da turma: {media_geral:.2f}")

def verificar_situacao_alunos():
    print("\n--- 4. SITUAÇÃO ACADÊMICA ---")
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    for aluno in alunos:
        media = calcular_media_aluno(aluno["notas"])
        situacao = determinar_situacao(media)
        print(f"Nome: {aluno['nome']} | Média: {media:.2f} | Situação: {situacao}")

def buscar_aluno():
    print("\n--- 5. BUSCAR ALUNO ---")
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    nome_busca = input("Digite o nome do aluno que deseja buscar: ").strip().lower()
    encontrado = False

    for aluno in alunos:
        if aluno["nome"].lower() == nome_busca:
            media = calcular_media_aluno(aluno["notas"])
            situacao = determinar_situacao(media)
            
            print("\n" + "="*30 + " BOLETIM " + "="*30)
            print(f"Nome: {aluno['nome']}")
            print(f"Idade: {aluno['idade']}")
            print(f"Curso: {aluno['curso']}")
            print(f"Notas: {aluno['notas'][0]:.1f}, {aluno['notas'][1]:.1f}, {aluno['notas'][2]:.1f}")
            print(f"Média: {media:.2f}")
            print(f"Situação: {situacao}")
            print("="*69)
            
            encontrado = True
            break

    if not encontrado:
        print("\nAluno não encontrado no sistema.")

def menu():
    while True:
        print("\n" + "=" * 40)
        print("          SISTEMA ACADÊMICO          ")
        print("=" * 40)
        print("1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("3 - Calcular média")
        print("4 - Verificar situação")
        print("5 - Buscar aluno")
        print("6 - Sair")
        print("=" * 40)

        opcao = input("Digite a opção desejada: ").strip()

        if opcao == '1':
            cadastrar_aluno()
        elif opcao == '2':
            listar_alunos()
        elif opcao == '3':
            exibir_medias()
        elif opcao == '4':
            verificar_situacao_alunos()
        elif opcao == '5':
            buscar_aluno()
        elif opcao == '6':
            print("\nEncerrando o Sistema Acadêmico... Até logo!")
            break
        else:
            print("\nOpção inválida! Escolha um número entre 1 e 6.")

if __name__ == "__main__":
    menu()