# EXERCÍCIOS PRÁTICOS — ARQUIVOS


# QUESTÃO 1 — Primeiro arquivo

nomes = ["Ana", "João", "Maria", "Pedro", "Carlos"]

with open("alunos.txt", "w", encoding="utf-8") as arquivo:
    for nome in nomes:
        arquivo.write(nome + "\n")

print("QUESTÃO 1")
print("Arquivo alunos.txt criado com sucesso!")


# QUESTÃO 2 — Leitura

print("\nQUESTÃO 2")

with open("alunos.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

print(conteudo)


# QUESTÃO 3 — Linha por linha

print("QUESTÃO 3")

with open("alunos.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        nome = linha.strip()
        print("Aluno:", nome)


# QUESTÃO 4 — Números

print("\nQUESTÃO 4")

with open("numeros.txt", "w", encoding="utf-8") as arquivo:
    for numero in range(1, 21):
        arquivo.write(str(numero) + "\n")

print("Números de 1 a 20:")

with open("numeros.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(linha.strip())


# QUESTÃO 5 — Append

print("\nQUESTÃO 5")

with open("numeros.txt", "a", encoding="utf-8") as arquivo:
    for numero in range(21, 31):
        arquivo.write(str(numero) + "\n")

print("Todos os números:")

with open("numeros.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(linha.strip())


# QUESTÃO 6 — Substituição

print("\nQUESTÃO 6")

with open("mensagem.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Primeira mensagem")

with open("mensagem.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Nova mensagem")

with open("mensagem.txt", "r", encoding="utf-8") as arquivo:
    mensagem = arquivo.read()

print("Mensagem:", mensagem)


# QUESTÃO 7 — Cadastro de alunos

print("\nQUESTÃO 7")

print("Digite 5 nomes de alunos:")

with open("alunos.txt", "w", encoding="utf-8") as arquivo:
    for i in range(5):
        nome = input(f"Digite o nome do aluno {i + 1}: ")
        arquivo.write(nome + "\n")

print("Alunos cadastrados com sucesso!")


# QUESTÃO 8 — Lista de compras

print("\nQUESTÃO 8")

with open("compras.txt", "w", encoding="utf-8") as arquivo:
    for i in range(5):
        produto = input(f"Digite o produto {i + 1}: ")
        arquivo.write(produto + "\n")

print("\nLista de compras:")

with open("compras.txt", "r", encoding="utf-8") as arquivo:
    contador = 1

    for linha in arquivo:
        produto = linha.strip()
        print(contador, "-", produto)
        contador += 1


# QUESTÃO 9 — Notas dos alunos

print("\nQUESTÃO 9")

with open("notas.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Ana;8.5\n")
    arquivo.write("João;7.0\n")
    arquivo.write("Maria;9.0\n")
    arquivo.write("Pedro;6.5\n")
    arquivo.write("Carlos;8.0\n")

print("Alunos e suas notas:")

with open("notas.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        nome, nota = linha.strip().split(";")
        print("Aluno:", nome, "- Nota:", nota)


# QUESTÃO 10 — Mini sistema

print("\nQUESTÃO 10")

while True:
    print("\n===== MENU =====")
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
        print("\nLista de alunos:")

        with open("alunos.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                print("-", linha.strip())

    elif opcao == "3":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida!")
        
