
ARQUIVO_ALUNOS = "alunos.txt"

def questoes_1_a_3():
    nomes = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo"]

    with open(ARQUIVO_ALUNOS, "w", encoding="utf-8") as arquivo:
        for nome in nomes:
            arquivo.write(nome + "\n")

    print("\nTodos os nomes:")
    with open(ARQUIVO_ALUNOS, "r", encoding="utf-8") as arquivo:
        print(arquivo.read(), end="")

    print("\nNomes um por vez:")
    with open(ARQUIVO_ALUNOS, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            print("Aluno:", linha.strip())


def questoes_4_e_5():
    with open("numeros.txt", "w", encoding="utf-8") as arquivo:
        for numero in range(1, 21):
            arquivo.write(f"{numero}\n")

    with open("numeros.txt", "a", encoding="utf-8") as arquivo:
        for numero in range(21, 31):
            arquivo.write(f"{numero}\n")

    print("\nNumeros de 1 a 30:")
    with open("numeros.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            print(linha.strip())


def questao_6():
    with open("mensagem.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Primeira mensagem\n")

    with open("mensagem.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Nova mensagem\n")

    with open("mensagem.txt", "r", encoding="utf-8") as arquivo:
        print("\nMensagem:", arquivo.read().strip())


def questao_7():
    print("\nCadastro de alunos (deixe o nome vazio para encerrar)")
    while True:
        nome = input("Nome: ").strip()
        if not nome:
            break

        with open(ARQUIVO_ALUNOS, "a", encoding="utf-8") as arquivo:
            arquivo.write(nome + "\n")

        print("Aluno cadastrado.")

def questao_8():
    
    with open("compras.txt", "w", encoding="utf-8") as arquivo:
        for indice in range(1, 6):
            produto = input(f"Produto {indice}: ").strip()
            arquivo.write(produto + "\n")

    print("\nLista de compras:")

    with open("compras.txt", "r", encoding="utf-8") as arquivo:
        for indice, linha in enumerate(arquivo, start=1):
            print(f"{indice} - {linha.strip()}")


def questao_9():

    dados = ["Ana;8.5", "Bruno;7.0", "Carlos;9.0"]
    with open("notas.txt", "w", encoding="utf-8") as arquivo:
        for dado in dados:
            arquivo.write(dado + "\n")

    print("\nNotas dos alunos:")

    with open("notas.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            nome, nota = linha.strip().split(";", maxsplit=1)
            print(f"Aluno: {nome} | Nota: {nota}")


def questao_10():
   
    while True:
        print("\n1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("3 - Sair")
        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            nome = input("Nome do aluno: ").strip()
            if nome:
                with open(ARQUIVO_ALUNOS, "a", encoding="utf-8") as arquivo:
                    arquivo.write(nome + "\n")
                print("Aluno cadastrado.")
            else:
                print("O nome nao pode ficar vazio.")
        elif opcao == "2":
            print("\nAlunos cadastrados:")
            try:
                with open(ARQUIVO_ALUNOS, "r", encoding="utf-8") as arquivo:
                    for indice, linha in enumerate(arquivo, start=1):
                        print(f"{indice} - {linha.strip()}")
            except FileNotFoundError:
                print("Nenhum aluno cadastrado.")
        elif opcao == "3":
            print("Programa encerrado.")
            break
        else:
            print("Opcao invalida.")


def main():
    questoes_1_a_3()
    questoes_4_e_5()
    questao_6()
    questao_10()


if __name__ == "__main__":
    main()
