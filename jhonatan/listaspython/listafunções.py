
# RESOLUÇÃO — FUNÇÕES EM PYTHON

def mostrar_mensagem():
    print("Bem-vindo à Ciência da Computação!")


def exercicio1():
    mostrar_mensagem()


def saudacao(nome):
    print("Olá,", nome)


def exercicio2():
    saudacao("Ana")
    saudacao("Carlos")


def somar(a, b):
    return a + b


def exercicio3():
    resultado = somar(15, 25)
    print("15 + 25 =", resultado)   # 40



def calcular_media3(n1, n2, n3):
    return (n1 + n2 + n3) / 3


def exercicio4():
    media = calcular_media3(8, 7, 9)
    print("Média:", media)   # 8.0



def verificar_par(numero):
    return numero % 2 == 0


def exercicio5():
    print("10 é par?", verificar_par(10))   # True
    print("7 é par?", verificar_par(7))     # False



def maior(a, b):
    if a > b:
        return a
    return b


def exercicio6():
    print("Maior entre 12 e 30:", maior(12, 30))
    print("Maior entre 50 e 8:", maior(50, 8))



def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return None   # divisão por zero não é possível
    return a / b


def exercicio7():
    print("\n=== CALCULADORA ===")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    opcao = input("Escolha a operação: ").strip()

    if opcao not in ("1", "2", "3", "4"):
        print("Opção inválida!")
        return

    a = float(input("Primeiro número: "))
    b = float(input("Segundo número: "))

    if opcao == "1":
        print("Resultado:", somar(a, b))
    elif opcao == "2":
        print("Resultado:", subtrair(a, b))
    elif opcao == "3":
        print("Resultado:", multiplicar(a, b))
    else:
        resultado = dividir(a, b)
        if resultado is None:
            print("Erro: não é possível dividir por zero.")
        else:
            print("Resultado:", resultado)



def ler_notas():
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    return n1, n2


def calcular_media(n1, n2):
    return (n1 + n2) / 2


def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


def exibir_resultado(nome, media, situacao):
    print("-----------------------")
    print("Aluno:", nome)
    print("Média:", media)
    print("Situação:", situacao)
    print("-----------------------")


def exercicio8():
    nome = input("Nome do aluno: ")
    n1, n2 = ler_notas()
    media = calcular_media(n1, n2)
    situacao = verificar_situacao(media)
    exibir_resultado(nome, media, situacao)



def cadastrar_aluno_simples(alunos):
    nome = input("Nome: ").strip()
    idade = int(input("Idade: "))
    curso = input("Curso: ").strip()
    alunos.append({"nome": nome, "idade": idade, "curso": curso})
    print("Aluno cadastrado!")


def listar_alunos_simples(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    for aluno in alunos:
        print(f"{aluno['nome']} | {aluno['idade']} anos | {aluno['curso']}")


def buscar_aluno_simples(alunos, nome):
    for aluno in alunos:
        if aluno["nome"].lower() == nome.lower():
            return aluno
    return None


def exercicio9():
    alunos = []
    while True:
        print("\n1 - Cadastrar | 2 - Listar | 3 - Buscar | 4 - Voltar")
        opcao = input("Opção: ").strip()

        if opcao == "1":
            cadastrar_aluno_simples(alunos)
        elif opcao == "2":
            listar_alunos_simples(alunos)
        elif opcao == "3":
            nome = input("Nome a buscar: ").strip()
            aluno = buscar_aluno_simples(alunos, nome)
            if aluno:
                print("Encontrado:", aluno)
            else:
                print("Aluno não encontrado.")
        elif opcao == "4":
            break
        else:
            print("Opção inválida!")



def ler_float(mensagem):
    """Lê um número real, repetindo até o usuário digitar um valor válido."""
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Valor inválido. Digite um número.")


def buscar_por_nome(alunos, nome):
    """Retorna o dicionário do aluno ou None se não existir."""
    for aluno in alunos:
        if aluno["nome"].lower() == nome.lower():
            return aluno
    return None


def cadastrar_aluno(alunos):
    nome = input("Nome do aluno: ").strip()
    if nome == "":
        print("Nome inválido.")
        return
    if buscar_por_nome(alunos, nome):
        print("Já existe um aluno com esse nome.")
        return
    n1 = ler_float("Nota 1: ")
    n2 = ler_float("Nota 2: ")
    alunos.append({"nome": nome, "nota1": n1, "nota2": n2})
    print("Aluno cadastrado com sucesso!")


def listar_alunos(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    print("\n--- Alunos cadastrados ---")
    for i, aluno in enumerate(alunos, start=1):
        print(f"{i}. {aluno['nome']} (notas: {aluno['nota1']} e {aluno['nota2']})")


def buscar_aluno(alunos):
    nome = input("Nome do aluno a buscar: ").strip()
    aluno = buscar_por_nome(alunos, nome)
    if aluno:
        print(f"Encontrado: {aluno['nome']} | Nota 1: {aluno['nota1']} | Nota 2: {aluno['nota2']}")
    else:
        print("Aluno não encontrado.")


def calcular_media_aluno(aluno):
    return (aluno["nota1"] + aluno["nota2"]) / 2


def calcular_media(alunos):
    nome = input("Nome do aluno: ").strip()
    aluno = buscar_por_nome(alunos, nome)
    if aluno:
        print(f"Média de {aluno['nome']}: {calcular_media_aluno(aluno):.2f}")
    else:
        print("Aluno não encontrado.")


def situacao_por_media(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    return "Reprovado"


def verificar_situacao_aluno(alunos):
    nome = input("Nome do aluno: ").strip()
    aluno = buscar_por_nome(alunos, nome)
    if aluno:
        media = calcular_media_aluno(aluno)
        print(f"{aluno['nome']} | Média: {media:.2f} | Situação: {situacao_por_media(media)}")
    else:
        print("Aluno não encontrado.")


def exibir_menu():
    print("\n========== SISTEMA ACADÊMICO ==========")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Buscar aluno")
    print("4 - Calcular média")
    print("5 - Verificar situação")
    print("6 - Sair")


def menu():
    alunos = []
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_aluno(alunos)
        elif opcao == "2":
            listar_alunos(alunos)
        elif opcao == "3":
            buscar_aluno(alunos)
        elif opcao == "4":
            calcular_media(alunos)
        elif opcao == "5":
            verificar_situacao_aluno(alunos)
        elif opcao == "6":
            print("Sistema encerrado.")
            break
        else:
            print("Opção inválida!")


def desafio_final():
    menu()



exercicios = {
    "1": exercicio1, "2": exercicio2, "3": exercicio3,
    "4": exercicio4, "5": exercicio5, "6": exercicio6,
    "7": exercicio7, "8": exercicio8, "9": exercicio9,
    "10": desafio_final,
}

if __name__ == "__main__":
    while True:
        escolha = input("\nQual exercício executar (1-9, 10 = Desafio Final, 0 = sair)? ").strip()
        if escolha == "0":
            break
        if escolha in exercicios:
            print(f"\n--- Exercício {escolha} ---")
            exercicios[escolha]()
        else:
            print("Opção inválida.")