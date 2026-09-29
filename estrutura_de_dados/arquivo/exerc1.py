
# ==========================================
# QUESTÃO 1 - Primeiro arquivo
# ==========================================
arquivo = open("dados.txt", "w")

def questao_1():
    nomes = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo"]

    with open("alunos.txt", "w", encoding="utf-8") as arquivo:
        for nome in nomes:
            arquivo.write(nome + "\n")

    print("Nomes gravados em alunos.txt")

# ==========================================
# QUESTÃO 2 - Leitura
# ==========================================

def questao_2():
    with open("alunos.txt", "r", encoding="utf-8") as arquivo:
        nomes = arquivo.read()

    print(nomes)


# ==========================================
# QUESTÃO 3 - Linha por linha
# ==========================================

def questao_3():
    with open("alunos.txt", "r", encoding="utf-8") as arquivo:
        for nome in arquivo:
            print("Aluno:", nome.strip())


# ==========================================
# QUESTÃO 4 - Números
# ==========================================

def questao_4():
    with open("numeros.txt", "w", encoding="utf-8") as arquivo:
        for numero in range(1, 21):
            arquivo.write(str(numero) + "\n")

    with open("numeros.txt", "r", encoding="utf-8") as arquivo:
        print(arquivo.read())


# ==========================================
# QUESTÃO 5 - Append
# ==========================================

def questao_5():
    with open("numeros.txt", "a", encoding="utf-8") as arquivo:
        for numero in range(21, 31):
            arquivo.write(str(numero) + "\n")

    with open("numeros.txt", "r", encoding="utf-8") as arquivo:
        print(arquivo.read())


# ==========================================
# QUESTÃO 6 - Substituição
# ==========================================

def questao_6():
    with open("mensagem.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Primeira mensagem")

    with open("mensagem.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Nova mensagem")

    with open("mensagem.txt", "r", encoding="utf-8") as arquivo:
        print(arquivo.read())


# ==========================================
# QUESTÃO 7 - Cadastro de alunos
# ==========================================

def questao_7():
    nome = input("Digite o nome do aluno: ")

    with open("alunos.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(nome + "\n")

    print("Aluno cadastrado!")


# ==========================================
# QUESTÃO 8 - Lista de compras
# ==========================================

def questao_8():
    produtos = []

    for i in range(5):
        produto = input(f"Digite o {i + 1}º produto: ")
        produtos.append(produto)

    with open("compras.txt", "w", encoding="utf-8") as arquivo:
        for produto in produtos:
            arquivo.write(produto + "\n")

    print("\nLista de compras:")

    with open("compras.txt", "r", encoding="utf-8") as arquivo:
        for i, produto in enumerate(arquivo, 1):
            print(f"{i} - {produto.strip()}")


# ==========================================
# QUESTÃO 9 - Notas dos alunos
# ==========================================

def questao_9():
    with open("notas.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Ana;8.5\n")
        arquivo.write("Bruno;7.0\n")
        arquivo.write("Carlos;9.0\n")

    print("Notas dos alunos:")

    with open("notas.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            nome, nota = linha.strip().split(";")
            print(f"Aluno: {nome} - Nota: {nota}")


# ==========================================
# QUESTÃO 10 - Mini sistema
# ==========================================

def questao_10():
    while True:
        print("\n===== MINI SISTEMA =====")
        print("1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do aluno: ")

            with open("alunos.txt", "a", encoding="utf-8") as arquivo:
                arquivo.write(nome + "\n")

            print("Aluno cadastrado com sucesso!")

        elif opcao == "2":
            try:
                with open("alunos.txt", "r", encoding="utf-8") as arquivo:
                    nomes = arquivo.readlines()

                print("\nAlunos cadastrados:")

                for i, nome in enumerate(nomes, 1):
                    print(f"{i} - {nome.strip()}")

            except FileNotFoundError:
                print("Nenhum aluno cadastrado.")

        elif opcao == "3":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida.")

    arquivo.close()
