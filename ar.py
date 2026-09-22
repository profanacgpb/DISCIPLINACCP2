# ==================================
# DESAFIO FINAL - Dicionário + Arquivo
# ==================================


produto = {
    "nome": "Notebook",
    "preco": 2500,
    "quantidade": 5
}


# Gravando produtos no arquivo

arquivo = open("produtos.txt", "w")

arquivo.write(
    produto["nome"] + ";" +
    str(produto["preco"]) + ";" +
    str(produto["quantidade"]) + "\n"
)

arquivo.write("Mouse;50;20\n")
arquivo.write("Teclado;100;10\n")

arquivo.close()



# Lendo produtos do arquivo

arquivo = open("produtos.txt", "r")


for linha in arquivo:

    dados = linha.strip().split(";")

    nome = dados[0]
    preco = dados[1]
    quantidade = dados[2]

    print("Produto:", nome)
    print("Preço:", preco)
    print("Quantidade:", quantidade)
    print("-------------------")


arquivo.close()



# ==================================
# ATIVIDADE DE FECHAMENTO
# SISTEMA DE ALUNOS
# ==================================


def cadastrar_aluno():

    nome = input("Nome: ")
    idade = input("Idade: ")
    curso = input("Curso: ")
    nota = input("Nota: ")


    arquivo = open("alunos.txt", "a")


    arquivo.write(
        nome + ";" +
        idade + ";" +
        curso + ";" +
        nota + "\n"
    )


    arquivo.close()

    print("Aluno cadastrado!")



def listar_alunos():

    arquivo = open("alunos.txt", "r")


    for linha in arquivo:

        dados = linha.strip().split(";")

        print("----------------")
        print("Nome:", dados[0])
        print("Idade:", dados[1])
        print("Curso:", dados[2])
        print("Nota:", dados[3])


    arquivo.close()



def pesquisar_aluno():

    nome_pesquisa = input("Digite o nome do aluno: ")


    arquivo = open("alunos.txt", "r")


    encontrado = False


    for linha in arquivo:

        dados = linha.strip().split(";")

        if dados[0] == nome_pesquisa:

            print("Aluno encontrado:")
            print(dados)

            encontrado = True


    arquivo.close()


    if encontrado == False:

        print("Aluno não encontrado")



def alterar_aluno():

    nome_antigo = input("Nome do aluno que deseja alterar: ")


    arquivo = open("alunos.txt", "r")

    alunos = arquivo.readlines()

    arquivo.close()



    arquivo = open("alunos.txt", "w")


    for aluno in alunos:

        dados = aluno.strip().split(";")

        if dados[0] == nome_antigo:

            novo_nome = input("Novo nome: ")
            nova_idade = input("Nova idade: ")
            novo_curso = input("Novo curso: ")
            nova_nota = input("Nova nota: ")


            arquivo.write(
                novo_nome + ";" +
                nova_idade + ";" +
                novo_curso + ";" +
                nova_nota + "\n"
            )

        else:

            arquivo.write(aluno)


    arquivo.close()



def remover_aluno():

    nome_remover = input("Nome do aluno para remover: ")


    arquivo = open("alunos.txt", "r")

    alunos = arquivo.readlines()

    arquivo.close()



    arquivo = open("alunos.txt", "w")


    for aluno in alunos:

        dados = aluno.strip().split(";")

        if dados[0] != nome_remover:

            arquivo.write(aluno)


    arquivo.close()

    print("Aluno removido!")



# Menu principal

while True:

    print("""
========================
 SISTEMA DE ALUNOS
========================

1 - Cadastrar aluno
2 - Listar alunos
3 - Pesquisar aluno
4 - Alterar aluno
5 - Remover aluno
6 - Sair
""")


    opcao = input("Escolha uma opção: ")


    if opcao == "1":

        cadastrar_aluno()


    elif opcao == "2":

        listar_alunos()


    elif opcao == "3":

        pesquisar_aluno()


    elif opcao == "4":

        alterar_aluno()


    elif opcao == "5":

        remover_aluno()


    elif opcao == "6":

        print("Programa encerrado!")

        break


    else:

        print("Opção inválida!")