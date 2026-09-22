# ================================
# QUESTÃO 1 - Primeiro arquivo
# ================================

arquivo = open("alunos.txt", "w")

arquivo.write("Ana\n")
arquivo.write("Carlos\n")
arquivo.write("Maria\n")
arquivo.write("João\n")
arquivo.write("Pedro\n")

arquivo.close()


# ================================
# QUESTÃO 2 - Leitura
# ================================

arquivo = open("alunos.txt", "r")

conteudo = arquivo.read()

print(conteudo)

arquivo.close()


# ================================
# QUESTÃO 3 - Linha por linha
# ================================

arquivo = open("alunos.txt", "r")

for linha in arquivo:
    print("Aluno:", linha.strip())

arquivo.close()


# ================================
# QUESTÃO 4 - Números
# ================================

arquivo = open("numeros.txt", "w")

for numero in range(1, 21):
    arquivo.write(str(numero) + "\n")

arquivo.close()


arquivo = open("numeros.txt", "r")

for linha in arquivo:
    print(linha.strip())

arquivo.close()


# ================================
# QUESTÃO 5 - Append
# ================================

arquivo = open("numeros.txt", "a")

for numero in range(21, 31):
    arquivo.write(str(numero) + "\n")

arquivo.close()


arquivo = open("numeros.txt", "r")

for linha in arquivo:
    print(linha.strip())

arquivo.close()


# ================================
# QUESTÃO 6 - Substituição
# ================================

arquivo = open("mensagem.txt", "w")

arquivo.write("Primeira mensagem")

arquivo.close()


arquivo = open("mensagem.txt", "w")

arquivo.write("Nova mensagem")

arquivo.close()


arquivo = open("mensagem.txt", "r")

print(arquivo.read())

arquivo.close()


# ================================
# QUESTÃO 7 - Cadastro de alunos
# ================================

while True:

    nome = input("Digite o nome do aluno (ou sair): ")

    if nome == "sair":
        break

    arquivo = open("alunos.txt", "a")

    arquivo.write(nome + "\n")

    arquivo.close()


# ================================
# QUESTÃO 8 - Lista de compras
# ================================

arquivo = open("compras.txt", "w")

for i in range(5):

    produto = input("Digite um produto: ")

    arquivo.write(produto + "\n")

arquivo.close()


arquivo = open("compras.txt", "r")

contador = 1

for linha in arquivo:
    print(contador, "-", linha.strip())
    contador += 1

arquivo.close()


# ================================
# QUESTÃO 9 - Notas dos alunos
# ================================

arquivo = open("notas.txt", "w")

arquivo.write("Ana;8.5\n")
arquivo.write("Carlos;7.0\n")
arquivo.write("Maria;9.0\n")

arquivo.close()


arquivo = open("notas.txt", "r")


for linha in arquivo:

    dados = linha.strip().split(";")

    nome = dados[0]
    nota = dados[1]

    print("Aluno:", nome, "- Nota:", nota)


arquivo.close()


# ================================
# QUESTÃO 10 - Mini sistema
# ================================

while True:

    print("\n1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Sair")

    opcao = input("Escolha: ")


    if opcao == "1":

        nome = input("Nome do aluno: ")

        arquivo = open("alunos.txt", "a")

        arquivo.write(nome + "\n")

        arquivo.close()


    elif opcao == "2":

        arquivo = open("alunos.txt", "r")

        for linha in arquivo:
            print(linha.strip())

        arquivo.close()


    elif opcao == "3":

        break


    else:

        print("Opção inválida")