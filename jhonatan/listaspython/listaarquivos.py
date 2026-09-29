
# RESOLUÇÃO — Exercícios práticos: ARQUIVOS EM PYTHON
# Execute o programa e escolha o número da questão no menu.

# Questão 1
# Criar alunos.txt com os nomes de 5 alunos.
def questao1():
    with open("alunos.txt", "w") as arquivo:
        arquivo.write("Ana\n")
        arquivo.write("Carlos\n")
        arquivo.write("Maria\n")
        arquivo.write("Pedro\n")
        arquivo.write("Julia\n")
    print("Arquivo alunos.txt criado com 5 nomes.")



# Questão 2 
# Ler alunos.txt e imprimir todos os nomes.
def questao2():
    with open("alunos.txt", "r") as arquivo:
        conteudo = arquivo.read()
    print(conteudo)



# Questão 3 
# Mostrar os nomes um por vez: "Aluno: Ana".
def questao3():
    with open("alunos.txt", "r") as arquivo:
        for linha in arquivo:
            print("Aluno:", linha.strip())



# Questão 4 — Números
# Criar numeros.txt com os números de 1 a 20 e depois ler.

def questao4():
    with open("numeros.txt", "w") as arquivo:
        for numero in range(1, 21):
            arquivo.write(str(numero) + "\n")

    with open("numeros.txt", "r") as arquivo:
        for linha in arquivo:
            print(linha.strip())



# Questão 5 
# a) adicionar 21 a 30  b) ler o arquivo  c) mostrar os números
# (usa o arquivo numeros.txt da questão 4)

def questao5():
    # a) modo "a" acrescenta ao final sem apagar o conteúdo
    with open("numeros.txt", "a") as arquivo:
        for numero in range(21, 31):
            arquivo.write(str(numero) + "\n")

    # b) e c) ler e mostrar
    with open("numeros.txt", "r") as arquivo:
        for linha in arquivo:
            print(linha.strip())



# Questão 6 
def questao6():
    with open("mensagem.txt", "w") as arquivo:
        arquivo.write("Primeira mensagem\n")

    with open("mensagem.txt", "w") as arquivo:   # "w" apaga o conteúdo anterior
        arquivo.write("Nova mensagem\n")

    with open("mensagem.txt", "r") as arquivo:
        print(arquivo.read())   # Mostra apenas "Nova mensagem"



# Questão 7 
def questao7():
    print("Digite os nomes dos alunos (digite 'sair' para encerrar).")
    while True:
        nome = input("Nome: ").strip()
        if nome.lower() == "sair":
            break
        if nome == "":
            print("Nome vazio, tente novamente.")
            continue
        with open("alunos.txt", "a") as arquivo:   # "a" mantém os nomes anteriores
            arquivo.write(nome + "\n")
        print("Aluno cadastrado!")

# Questão 8 
def questao8():
    with open("compras.txt", "w") as arquivo:
        for i in range(1, 6):
            produto = input(f"Produto {i}: ").strip()
            arquivo.write(produto + "\n")

    print("\nLista de compras:")
    with open("compras.txt", "r") as arquivo:
        numero = 1
        for linha in arquivo:
            print(f"{numero} - {linha.strip()}")
            numero += 1



# Questão 9 
def questao9():
    with open("notas.txt", "w") as arquivo:
        arquivo.write("Ana;8.5\n")
        arquivo.write("Carlos;7.0\n")
        arquivo.write("Maria;9.5\n")
        arquivo.write("Pedro;6.0\n")

    with open("notas.txt", "r") as arquivo:
        for linha in arquivo:
            nome, nota = linha.strip().split(";")   # separa pelo ";"
            print(f"Aluno: {nome} | Nota: {nota}")



# Questão 10 
def questao10():
    while True:
        print("\n===== MINI SISTEMA =====")
        print("1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            nome = input("Nome do aluno: ").strip()
            if nome:
                with open("alunos.txt", "a") as arquivo:
                    arquivo.write(nome + "\n")
                print("Aluno cadastrado com sucesso!")
            else:
                print("Nome inválido.")

        elif opcao == "2":
            try:
                with open("alunos.txt", "r") as arquivo:
                    print("\nAlunos cadastrados:")
                    for linha in arquivo:
                        print("-", linha.strip())
            except FileNotFoundError:
                print("Nenhum aluno cadastrado ainda.")

        elif opcao == "3":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida!")



questoes = {
    "1": questao1, "2": questao2, "3": questao3, "4": questao4,
    "5": questao5, "6": questao6, "7": questao7, "8": questao8,
    "9": questao9, "10": questao10,
}

if __name__ == "__main__":
    while True:
        escolha = input("\nQual questão executar (1-10)? Digite 0 para sair: ").strip()
        if escolha == "0":
            break
        if escolha in questoes:
            print(f"\n--- Questão {escolha} ---")
            questoes[escolha]()
        else:
            print("Questão inválida.")